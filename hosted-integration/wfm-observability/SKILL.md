---
name: wfm-observability
description: Use this skill when the user needs to monitor, debug, log, or alert on the NICE WFM Integration Platform — CloudWatch metrics, Prometheus `/metrics`, alarms, log groups, structured-log fields, FIPS audit, health probes, runbooks, S3-file-drop tracing, or production diagnostics. Triggers include "is the system healthy", "what metrics exist", "set up an alarm", "find this log", "why is X slow", "trace this event/file", SRE onboarding, runbook authoring, and any "where do I look in logs/metrics" question. Do NOT use for: high-level service responsibilities (use `wfm-system-architecture`) or flow walkthroughs (use `wfm-execution-flow`).
---

# WFM Integration Platform — Observability

## Architecture Overview

Three telemetry channels:

1. **CloudWatch Logs** — structured JSON, one log group per service
2. **CloudWatch Metrics** — pushed every 60 s; alarms via `cicd/CloudwatchAlarms.yaml`
3. **Prometheus `/metrics`** — exposed by C# services; scraped by internal monitoring

Per-event correlation fields are emitted by every service (`tenantId`, `clusterId`, `agentId`, `shardId`, `sequenceNumber`, plus `s3Key` for the S3-file pipeline). Java uses SLF4J + Logback + `logstash-logback-encoder`. C# logs structured JSON to stdout.

---

## Core Components — Per-Service Telemetry

### Log groups

| Log group | Service |
|-----------|---------|
| `integrations-wfm-streamconsumer` | StreamConsumer |
| `integrations-wfm-stateaggregator` | StateAggregator |
| `integrations-wfm-intervalreader` | IntervalReader |
| `integrations-wfm-verintpublisher` | VerintPublisher |
| `integrations-wfm-config` | WfmConfig |
| `integrations-wfm-statecollector` | StateCollector |
| `integrations-wfm-statepublisher` | StatePublisher |
| `integrations-wfm-aggregator` | IntervalAggregator |
| `integrations-wfm-intervalpublisher` | IntervalPublisher |
| `integrations-wfm-etlscheduler` | EtlScheduler |

### Health endpoints

| Service | Endpoint(s) |
|---------|-------------|
| StreamConsumer | `GET /actuator/health` |
| StateAggregator | `HealthCheckController.java` |
| IntervalReader | `GET /actuator/health` |
| VerintPublisher | `HealthCheckController` |
| WfmConfig | C# health middleware |
| StateCollector | Port 8080 |
| StatePublisher | Health monitoring controllers |
| IntervalAggregator | Port 8080 |
| IntervalPublisher | Port 8080 |
| EtlScheduler | `/probe/healthcheck`, `/probe/host`, `/probe/startup`, `/probe/ready`, `/probe/healthreport` |

### Prometheus exporters

- WfmConfig — `http_requests_total`, `http_request_duration_seconds`
- EtlScheduler — ETL-specific counters/gauges (below)

---

## Service Interactions — Key Metrics

**StreamConsumer (CloudWatch):**

| Metric | Meaning |
|--------|---------|
| `RecordsProcessed` | Kinesis records consumed |
| `ProcessingErrors` | Record-processor failures |
| `RedisWriteLatency` | Sorted-set write latency |
| `SQSPublishCount` | Notifications to SA/IR queues |

**StateAggregator:**

| Metric | Meaning |
|--------|---------|
| `AggregationCount` | Events aggregated |
| `DynamoDBWriteCount` | Successful writes |
| `DynamoDBWriteErrors` | Failed writes |
| `SQSMessageLatency` | Receive → DDB write latency |
| `InFlightPurgeCount` | Stale Redis entries cleaned |

**IntervalReader (per-domain):**

| Metric | Meaning |
|--------|---------|
| `InflightSetSize{domain=ac|cs|acdfo|csdfo|as}` | Redis sorted set length |
| `BatchProcessed` | Batches sent to FIFO queue |
| `FifoSendErrors` | FIFO publish failures |
| `ExternalNotifyCount` | External completion-queue messages |

**IntervalAggregator:**

| Metric | Meaning |
|--------|---------|
| `IntervalRequestsReceived` | HTTP POSTs from EtlScheduler |
| `DynamoReadCount` | Reads from aggregated facts |
| `S3PutCount{prefix=verint|verintadherence|iexsftp|cxonewfm}` | Files written per WFM target |
| `S3PutErrors` | Failed S3 writes |
| `GenerationLatency` | DynamoDB read → S3 write end-to-end |

**VerintPublisher:**

| Metric | Meaning |
|--------|---------|
| `SqsReceiveCount` | S3-event messages received |
| `S3FetchLatency` | GetObject duration |
| `VerintPostCount{type=queue|agent}` | Successful POSTs by type |
| `VerintPostErrors{httpStatus}` | Failures by HTTP code |
| `TenantConfigCacheHits` / `Misses` | Per-tenant config cache |

**IntervalPublisher:**

| Metric | Meaning |
|--------|---------|
| `SqsReceiveCount` | S3-event messages received |
| `SftpUploadCount` | Successful uploads |
| `SftpUploadErrors{stack,tenant}` | Per-tenant SFTP failures |
| `SftpUploadDuration` | Per-file upload latency |
| `SftpConnectionFailures` | Connect / auth failures |

**EtlScheduler (Prometheus + CloudWatch):**

| Metric | Type | Meaning |
|--------|------|---------|
| `etl_aggregation_requests` | Counter | IntervalRequests posted |
| `etl_aggregation_failures_service` | Counter | Service-tier failures |
| `etl_aggregation_failures_other` | Counter | DB/timeout failures |
| `etl_aggregator_send_failures` | Counter | HTTP POST failures |
| `etl_missed_intervals{cluster}` | Counter | ETL window timeouts |
| `etl_poll_failures{cluster}` | Counter | DW polling errors |
| `etl_interval_count{cluster}` | Counter | Successful intervals |
| `etl_interval_end_to_etl_upload_time{cluster}` | Gauge (min) | Time-to-data |
| `etl_cluster_count` | Gauge | Clusters being monitored |
| `etl_errors{type}` | Counter | Service/Database/Aws/Other |
| `api_build_info{name,version,branch,commit,instance_id}` | Counter | Build provenance |

**WfmConfig (Prometheus):**

| Metric | Meaning |
|--------|---------|
| `http_requests_total` | Per-endpoint count |
| `http_request_duration_seconds` | Latency histogram |

### CloudWatch alarms

Auto-provisioned via `cicd/CloudwatchAlarms.yaml`:

- High error rate per service
- SQS queue depth
- DynamoDB write failures
- Health-check failures

**Recommended additional alarms (post Verint-flow rewrite):**

- `S3PutCount{prefix=verint}` drops to 0 for sustained interval (aggregator not generating)
- `SqsVerintPublishQueue` depth > N (publisher behind)
- `SftpUploadErrors` > 0 sustained per tenant (SFTP issues)
- `VerintPostErrors{httpStatus=5xx}` rising
- `etl_missed_intervals` > 0 sustained
- `etl_aggregator_send_failures` rising

SNS topic: `cloudwatch-bmc-info`. Stack: `integrations-wfm-config-alarms`.

---

## Data Models — Structured Log Schema

Common JSON fields across services:

```json
{
  "timestamp": "2026-05-23T10:15:00.123Z",
  "level": "INFO",
  "service": "integrations-wfm-verintpublisher",
  "tenantId": "tenant-abc",
  "bu": "BU01",
  "clusterId": "cluster-na2-01",
  "agentId": "agent-12345",
  "shardId": "shardId-000000000001",
  "sequenceNumber": "49584...",
  "s3Key": "verint/BU01_tenant-abc/260523.1015.json",
  "instance-id": "uuid",
  "message": "...",
  "class": "CSIQueuePerformanceService"
}
```

**EtlScheduler format** (`UtilityClasses/Logger.cs`):

```
{LogType} {ClientIp} {MethodName}: {Message}
```

Error-level entries auto-increment matching `etl_errors{type}` counter.

---

## Conventions & Patterns

### Log levels

- `DEBUG` — verbose details
- `INFO` — milestones (batch start/end, files written)
- `WARN` — recoverable issues
- `ERROR` — failures needing investigation

### FIPS audit

When `ENABLE_FIPS=true`, services enumerate security providers at startup and log them.

### Metric cadence

CloudWatch every minute (`0 0/1 * * * *`).

### Multi-region

| Environment | Region | AWS Account |
|-------------|--------|-------------|
| Dev | us-west-2 | 300813158921 |
| Staging | us-west-2 | 545209810301 |
| Production NA2, NA3, UK2, ZA1, ... | multi-region | per-region prod accounts |

---

## Common Tasks

### Trace one agent event end-to-end

```
1. integrations-wfm-streamconsumer:
   filter agentId = "agent-12345" and class = "AgentSessionRecordProcessor"

2. integrations-wfm-stateaggregator:
   filter agentId = "agent-12345" and class like /AggregatorService/

3. Confirm class = "DynamoInserter" write log line.
```

### Trace one Verint interval file end-to-end

```
1. integrations-wfm-etlscheduler:
   filter clusterId = "cluster-na2-01" and MethodName = "PollEtl"
   → confirm POST IntervalRequest

2. integrations-wfm-aggregator:
   filter clusterId = "cluster-na2-01"
   → confirm S3 PutObject "verint/BU_tenant/.../*.json"

3. aws s3 ls s3://<bucket>/verint/BU_tenant/

4. integrations-wfm-verintpublisher:
   filter s3Key = "verint/BU_tenant/.../*.json"
   → confirm AwsS3Service.fetchFile
   → confirm CSIQueuePerformanceService POST
   → confirm Verint HTTP response status
```

### Trace one IEX SFTP file end-to-end

```
1. Aggregator side (same as above but iexsftp/Stack/Tenant/*.xml)
2. aws s3 ls s3://<bucket>/iexsftp/<Stack>/<Tenant>/
3. integrations-wfm-intervalpublisher:
   filter s3Key contains "iexsftp/<Stack>/<Tenant>/"
   → confirm SftpPublisher.PublishIntervalReport
   → confirm SFTP upload success
```

### Add an alarm for a custom metric

1. Edit `cicd/CloudwatchAlarms.yaml`.
2. Define alarm (namespace, metric, dimension, threshold, period).
3. Link to SNS topic `cloudwatch-bmc-info`.
4. Commit → CI applies CloudFormation.

### Verify Prometheus scraping

```bash
curl https://<service-host>/metrics
# Look for api_build_info{...} line confirming the service is alive
```

---

## Troubleshooting

### Real-time events missing in DynamoDB

1. StreamConsumer health + `RecordsProcessed` rising?
2. SQS `NICEWFM_CONSUMER_SA_QUEUE` depth growing?
3. StateAggregator `HealthCheckController` healthy?
4. Redis reachable? Redisson connect logs?
5. DynamoDB throttling? `DynamoDBWriteErrors` rising?

### Verint missing data

1. `S3PutCount{prefix=verint}` non-zero in IntervalAggregator?
2. File present at `s3://<bucket>/verint/<BU>_<TenantId>/`?
3. `SqsVerintPublishQueue` depth — has VerintPublisher received the event?
4. VerintPublisher logs: `MessageProcessingService` → `AwsS3Service.fetchFile` → `CSIQueuePerformanceService` / `AgentPerformanceService` → POST status?
5. `VerintPostErrors{httpStatus}` — what HTTP code is Verint returning?
6. Tenant config: `CALL External_GetAllTenantData()` and inspect the row for your tenant.

### IEX SFTP files not arriving

1. `S3PutCount{prefix=iexsftp}` non-zero in IntervalAggregator?
2. File present at `s3://<bucket>/iexsftp/<Stack>/<Tenant>/`?
3. `SqsPublishQueue` depth?
4. IntervalPublisher logs: `SqsClient` → `SftpPublisher.PublishIntervalReport`?
5. `SftpUploadErrors{stack,tenant}` — what kind of failure?
6. SFTP credentials current? Network reachable to IEX SFTP host?

### Interval files missing in S3

1. DynamoDB has aggregated rows for the window? `DynamoReadCount` in IntervalAggregator?
2. EtlScheduler `etl_interval_count{cluster}` rising?
3. EtlScheduler logs: `POST /api/v1/Interval/cluster` returning 200?
4. IntervalAggregator logs: `<Target>ReportGenerator` run?

### EtlScheduler not triggering

1. `/probe/ready` and `/probe/startup` — 200?
2. `etl_cluster_count` gauge — Aurora returning clusters?
3. `etl_poll_failures{cluster}` — DW reachable?
4. `CALL Interval_GetLastEtlRequest('<cluster>', 'COMPOSITE_ETL')` — stuck?
5. `AggregatorServiceHost` env var correct?

### WfmConfig 5xx

1. ECS task healthy?
2. Secrets Manager access?
3. Aurora/COR/MyGlobal reachable from ECS subnet?
4. CloudWatch logs for Dapper SQL errors?

---

## Reference Files

- `cicd/CloudwatchAlarms.yaml` — alarm definitions
- `boot/*-Service-task.json` — log driver + log group binding
- Java services: `src/main/resources/logback.xml`
- EtlScheduler: `WfmEtlScheduler/UtilityClasses/Logger.cs`, `Monitoring/PrometheusService.cs`, `Monitoring/AwsCloudWatch.cs`
- WfmConfig: `Startup.cs` (Prometheus middleware)
- VerintPublisher: `src/main/java/com/nicewfm/monitoring/`

### Related skills

- `wfm-system-architecture`
- `wfm-execution-flow`
- `wfm-dependency-mapping`
- Module skills for service-specific metric details
