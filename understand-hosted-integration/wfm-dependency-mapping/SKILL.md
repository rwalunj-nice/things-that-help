---
name: wfm-dependency-mapping
description: Use this skill when the user needs to know exactly which services in the NICE WFM Integration Platform communicate, what AWS resource each service owns (Kinesis, SQS, S3 prefix, Redis key, DynamoDB, Aurora), what library versions are pinned, or what the impact radius of a change is. Triggers include "which services use X", "who calls whom", "what queue does Y consume", "which S3 prefix", "which secret is needed", "impact analysis", "dependency graph", "shared resource ownership", "what does this change break". Do NOT use for: high-level architecture overview (use `wfm-system-architecture`) or step-by-step execution flow (use `wfm-execution-flow`).
---

# WFM Integration Platform — Dependency Mapping

## Architecture Overview

Authoritative map of who-talks-to-whom: every Kinesis stream, SQS queue, S3 prefix, Redis key, DynamoDB table, REST endpoint, Aurora stored procedure, AWS secret, and IAM permission has an owner and one or more consumers. Use for impact analysis, IAM audit, or contract verification.

### Inter-service communication map

```
SERVICE                  PUBLISHES TO                       CONSUMES FROM
─────────────────────────────────────────────────────────────────────────
StateCollector (C#)      Kinesis WFM State                  Kinesis Orchestration
StreamConsumer (Java)    Redis sorted sets + SQS SA queue   Kinesis Orchestration
                         + prefixed IR queue signals
StateAggregator (Java)   DynamoDB                           SQS SA queue + Redis
IntervalReader (Java)    FIFO IR_SA_QUEUE + external        SQS IR queue (prefixed) + Redis
                         batch-completion queue
StatePublisher (C#)      IEX ASCWS REST (real-time)         Kinesis WFM State
IntervalAggregator (C#)  S3 files (4 prefixes)              HTTP from EtlScheduler + DynamoDB
EtlScheduler (C#)        HTTP POST → IntervalAggregator     Aurora + per-cluster SQL Server DW
VerintPublisher (Java)   Verint REST per tenant             SqsVerintPublishQueue (S3 events
                                                            on verint/ + verintadherence/) + S3
IntervalPublisher (C#)   IEX SFTP per tenant                SqsPublishQueue (S3 events
                                                            on iexsftp/) + S3 + MySQL SFTP creds
WfmConfig (C#)           Aurora / COR / MyGlobal            (REST API; consumed by all)
```

---

## Core Components — Resource Ownership

### Kinesis streams

| Stream env var | Producer | Consumers |
|---------------|----------|-----------|
| `NICEWFM_STREAM_NAME` (orchestration) | ACD/DFO platform | StreamConsumer (Java), StateCollector (C#) |
| WFM State stream | StateCollector | StatePublisher |

### SQS queues

| Queue env var | Producer | Consumer | Notes |
|---------------|----------|----------|-------|
| `NICEWFM_CONSUMER_SA_QUEUE` | StreamConsumer | StateAggregator | Standard |
| `NICEWFM_CONSUMER_IR_QUEUE` | StreamConsumer | IntervalReader | Prefixed: `AC_/CS_/ACDFO_/CSDFO_/AS_` batch-start signals |
| `NICEWFM_IR_SA_QUEUE` | IntervalReader | aggregation | FIFO (`.fifo`) — preserves per-tenant order |
| `NICEWFM_EXTERNAL_BATCH_COMPLETION_QUEUE_NAME` | IntervalReader | external systems | "batch complete" notifications |
| `SqsVerintPublishQueue` | S3 event notification (PutObject on `verint/`, `verintadherence/`) | VerintPublisher | |
| `SqsPublishQueue` | S3 event notification (PutObject on `iexsftp/`) | IntervalPublisher | |

### S3 prefixes (interval-data bucket)

Bucket env var: `IntegrationsWFMIntervalBucket` (aggregator) / `aws.S3Bucket` (publisher).

Default name: `integrations-wfm-interval-data-<env>-<region>`.

| Prefix | File format | Producer | Consumer |
|--------|-------------|----------|----------|
| `verint/{BU}_{TenantId}/yyMMdd.HHmm.json` | JSON | IntervalAggregator (`VerintReportGenerator`) | VerintPublisher (`CSIQueuePerformanceService`) |
| `verintadherence/{BU}_{TenantId}/TTI_yyyyMMdd.HHmm.json` | JSON | IntervalAggregator (Verint Agent Profile) | VerintPublisher (`AgentPerformanceService`) |
| `iexsftp/{Stack}/{Tenant}/MMddyy.HHmm.xml` | XML | IntervalAggregator (`IexReportGenerator`) | IntervalPublisher → SFTP push |
| `cxonewfm/{BU}_{TenantId}/yyMMdd.HHmm.json` | JSON | IntervalAggregator (`CxOneReportGenerator`) | External CxOne process (no in-repo consumer) |

### Internal REST contracts

| Endpoint | Provider | Caller(s) | Body |
|----------|----------|-----------|------|
| `POST /api/v1/Interval/cluster` | IntervalAggregator | EtlScheduler | `IntervalRequest{Cluster,ClusterNumber,StartDateUTC,EndDateUTC,Interval=15}` |
| `POST /api/v1/Interval/cluster/ETLErrorInterval` | IntervalAggregator | EtlScheduler | `ErrorIntervalRequest{...,StatusReason}` |
| `POST /api/verint/queue-performance` | VerintPublisher | Operators (manual trigger) | S3 file ref |
| `POST /api/verint/agent-performance` | VerintPublisher | Operators | S3 file ref (TTI_*) |
| `GET /api/tenant*`, `/api/clusters`, `/api/settings` | WfmConfig | All services | DTOs per controller |

### Redis (ElastiCache) keys

| Key / pattern | Writer | Reader | Type |
|---------------|--------|--------|------|
| Per-event references | StreamConsumer | StateAggregator | Standard keys |
| `ac:inflight` | StreamConsumer | IntervalReader | RScoredSortedSet (agent contact) |
| `cs:inflight` | StreamConsumer | IntervalReader | RScoredSortedSet (contact skill) |
| `acdfo:inflight` | StreamConsumer | IntervalReader | RScoredSortedSet (DFO agent contact) |
| `csdfo:inflight` | StreamConsumer | IntervalReader | RScoredSortedSet (DFO contact skill) |
| `as:inflight` | StreamConsumer | IntervalReader | RScoredSortedSet (agent session) |

### DynamoDB

| Table purpose | Writer | Reader |
|--------------|--------|--------|
| Aggregated event store (`NICEWFM_DYNAMODB_TABLE_NAME`) | StateAggregator | **IntervalAggregator** (via `DynamoConnector`/`DynamoReader`) |

### Aurora MySQL databases

| Database | Schema owner | Used by |
|----------|--------------|---------|
| Aurora (primary WFM config) | WfmConfig | StateCollector, StatePublisher, EtlScheduler, **VerintPublisher** (via `External_GetAllTenantData`), **IntervalPublisher** (via `Interval_GetSftpConnectionsByTenantStack`) |
| COR (Customer Org Records) | WfmConfig | StatePublisher, IntervalPublisher (tenant lookup), EtlScheduler |
| MyGlobal (multi-tenant global) | WfmConfig | All services (tenant resolution) |

### Per-cluster SQL Server Data Warehouses

| DB | Reached via | Polled by | Stored procedure |
|----|-------------|-----------|------------------|
| Cluster DW | `cluster_dw_vip` (from Aurora `Interval_GetClusters`) | EtlScheduler | `IC_GetETLData(etlName)` |

### Aurora stored-procedure ownership

| Procedure family | Caller |
|------------------|--------|
| `TenantStatus_*`, `TenantInfo_*`, `TenantConfig_*` | WfmConfig |
| `Clusters_*`, `Shard_*`, `Settings_*` | WfmConfig |
| `Adherence_*`, `DigitalAbandoned_*` | WfmConfig |
| `Interval_GetClusters`, `Interval_GetLastEtlRequest`, `Interval_UpdateLastEtlRequest` | **EtlScheduler** |
| `External_GetAllTenantData` (procedure) | **VerintPublisher** (read tenant external WFM config) |
| `Interval_GetSftpConnectionsByTenantStack` (procedure) — sources from `tbl_409_iex_config` | **IntervalPublisher** (read SFTP creds) |

---

## Service Interactions

### Library pins per service

**Java:**

```
StreamConsumer pom.xml:
  software.amazon.awssdk:kinesis:2.25.20
  software.amazon.awssdk:sqs:2.25.20
  software.amazon.awssdk:cloudwatch:2.25.20
  software.amazon.kinesis:amazon-kinesis-client:2.5.8
  org.redisson:redisson:3.45.0
  spring-boot-starter-webflux
  net.logstash.logback:logstash-logback-encoder:4.9

StateAggregator pom.xml:
  software.amazon.awssdk:dynamodb:2.29.29
  software.amazon.awssdk:sqs:2.29.29
  org.redisson:redisson:3.45.0  (MASTER_SLAVE + MASTER modes)
  com.amazonaws:amazon-sqs-java-messaging-lib:2.1.3 + jakarta.jms-api (NOT activemq)
  spring-boot-starter-actuator

IntervalReader pom.xml:
  AWS SDK SQS, Redisson, Spring Boot Scheduler

VerintPublisher pom.xml:
  AWS SDK S3 + SQS
  Spring RestTemplate
  MySQL JDBC + Dapper-style helpers
```

**C#:**

```
WfmConfig:           Dapper, JWT Bearer, Prometheus.DotNet, Swashbuckle
StateCollector:      KCL (C#), ConcurrentQueue(cap=10,000)
StatePublisher:      HttpClient → IEX ASCWS
IntervalAggregator:  ASP.NET Core, DynamoConnector, AwsS3Publisher, 22+ DTOs
IntervalPublisher:   AWS SDK S3 + SQS, Renci.SshNet (SFTP), MySQL
EtlScheduler:        Dapper, HttpClient, IHostedService, Prometheus.DotNet
```

### Auth & error

- WfmConfig: JWT Bearer (custom signature; relaxed in dev)
- AWS calls: ECS task role `Role-integrations-ecs-service`
- Internal HTTP: VPC + security groups (no mTLS)
- Verint REST per tenant: credentials returned by `External_GetAllTenantData`
- IEX SFTP per tenant: credentials returned by `Interval_GetSftpConnectionsByTenantStack` (data in `tbl_409_iex_config`)

### Failure recovery

| Failure | Recovery |
|---------|----------|
| StreamConsumer ↔ SA missed | StateAggregator purge scheduler |
| StateAggregator mid-batch crash | SQS visibility timeout |
| IntervalReader cron miss | Next tick re-reads cumulative sorted sets |
| EtlScheduler DB auth | Auto-reload from Secrets Manager |
| EtlScheduler ETL timeout | `ErrorIntervalRequest` POST |
| Aggregator → S3 failure | Retry; persistent → metric alarm |
| S3 → SQS event miss | Configuration issue; check S3 event notification settings |
| Verint REST 5xx / IEX SFTP fail | Visibility timeout → redelivery → DLQ |

---

## Data Models

### Shared DTOs

```csharp
// EtlScheduler → IntervalAggregator
class IntervalRequest {
    string   Cluster;          int      ClusterNumber;
    DateTime StartDateUTC;     DateTime EndDateUTC;
    int      Interval = 15;
}
class ErrorIntervalRequest : IntervalRequest { string StatusReason; }

// Aurora → EtlScheduler (Interval_GetClusters)
class ClusterInfo {
    string Id;       // cluster_id
    int    Number;   // cluster_number
    string Vip;      // cluster_vip
    string DWVip;    // cluster_dw_vip
}

// S3 event payload (consumed by VerintPublisher, IntervalPublisher)
// Standard S3 event JSON: Records[*].s3.bucket.name + s3.object.key
```

### File-name conventions

| Format | Used by |
|--------|---------|
| `yyMMdd.HHmm.json` | CxOne, Verint queue files |
| `TTI_yyyyMMdd.HHmm.json` | Verint agent files |
| `MMddyy.HHmm.xml` | IEX SFTP files |

### Secrets Manager dependencies

| Secret | Consumer | Env var |
|--------|----------|---------|
| `integrations-ic-encryption-key` | WfmConfig, StateCollector | `NiCEncryptionKeySecret` |
| `integrations-wfm-aurora-db` | WfmConfig, EtlScheduler, VerintPublisher, IntervalPublisher | `AuroraSecret` (varies) |
| `integrations-wfm-cor-db` | WfmConfig, EtlScheduler | `DwSecret` / `CorSecret` |
| `integrations-wfm-myglobal-db` | WfmConfig | `MyGlobalSecret` |

### Shared env vars

```
NICEWFM_REGION              — all Java services
NICEWFM_REDIS_URL / _PORT   — StreamConsumer, StateAggregator, IntervalReader
```

---

## Conventions & Patterns

### IAM permission profiles (ECS task role)

| Service | Required permissions |
|---------|---------------------|
| StreamConsumer | `kinesis:GetRecords`, `sqs:SendMessage`, `cloudwatch:PutMetricData`, ElastiCache |
| StateAggregator | `sqs:ReceiveMessage`, `dynamodb:PutItem`/`Query`, CloudWatch, ElastiCache |
| IntervalReader | `sqs:ReceiveMessage`/`SendMessage` (multi-queue), CloudWatch, ElastiCache |
| WfmConfig | `secretsmanager:GetSecretValue` (3 secrets), RDS Aurora connect |
| EtlScheduler | `secretsmanager:GetSecretValue` (Aurora+DW), `s3:GetObject` (TLS), CloudWatch |
| **IntervalAggregator** | DynamoDB Query, **`s3:PutObject`** on the interval bucket, CloudWatch |
| **VerintPublisher** | `sqs:ReceiveMessage` on SqsVerintPublishQueue, **`s3:GetObject`** on bucket, Aurora connect, CloudWatch |
| **IntervalPublisher** | `sqs:ReceiveMessage` on SqsPublishQueue, **`s3:GetObject`** on bucket, MySQL connect, outbound SFTP (network egress), CloudWatch |
| StatePublisher | `kinesis:GetRecords`, CloudWatch |
| All | `secretsmanager:GetSecretValue`, CloudWatch Logs |

### S3 event configuration (bucket-level)

The interval-data bucket has S3 event notifications wired up to:

- `verint/*` and `verintadherence/*` → `SqsVerintPublishQueue`
- `iexsftp/*` → `SqsPublishQueue`
- `cxonewfm/*` → (no in-repo notification target)

### Branching strategy

- Old: `master` (dev), `release` (prod)
- New: `main` (dev), `release-main` (prod)

---

## Common Tasks

### "I'm changing X — what breaks?"

| Change | Impacted | Why |
|--------|----------|-----|
| StreamConsumer SQS message shape | StateAggregator, IntervalReader | They parse the messages |
| Redis sorted-set key naming | StreamConsumer (writer), IntervalReader (reader) | Five domain-specific keys |
| Aurora `TenantStatus` schema | WfmConfig + all config readers | Dapper row mapping |
| `IntervalRequest` JSON contract | EtlScheduler ↔ IntervalAggregator | REST body shared |
| DynamoDB aggregated record schema | StateAggregator (writer), **IntervalAggregator (reader)** | DynamoConnector mapping |
| `Interval_GetClusters` columns | EtlScheduler `ClusterInfo` Dapper mapping | Column attributes |
| Aurora `External_GetAllTenantData` | VerintPublisher (per-tenant target config) | URL/credentials build |
| Aurora `Interval_GetSftpConnectionsByTenantStack` + `tbl_409_iex_config` | IntervalPublisher (SFTP creds per Stack+Tenant) | SFTP routing |
| **S3 file naming convention** | **All three publishers** | File-name parsing |
| **S3 prefix layout** | **IntervalAggregator (writer) + 3 consumers** | Routing + S3 event config |
| WfmConfig REST schema | Every config consumer | Cached after first fetch |

### Verify a service can reach a resource

```bash
aws iam list-attached-role-policies --role-name Role-integrations-ecs-service
aws secretsmanager get-secret-value --secret-id integrations-wfm-aurora-db
aws sqs get-queue-url --queue-name <SqsVerintPublishQueue>
aws s3 ls s3://<bucket>/verint/<BU>_<TenantId>/
```

### Find what calls a stored procedure / S3 prefix

```bash
grep -r "TenantStatus_Put" WfmConfig/
grep -r "Interval_GetClusters" integrations-wfm-etlscheduler/
grep -r "External_GetAllTenantData" integrations-wfm-verintpublisher/
grep -r "iexsftp" integrations-wfm-intervalpublisher/
```

---

## Troubleshooting

| Question | Where to look |
|----------|---------------|
| "Does service X have access to Y?" | IAM permission profiles |
| "Which queue carries Z?" | SQS queues table |
| "Which S3 prefix has the file?" | S3 prefixes table |
| "Who reads table/key T?" | DynamoDB / Redis / Aurora tables |
| "Which secret feeds DB connection?" | Secrets Manager dependencies |
| "What's the contract for endpoint E?" | Internal REST contracts |
| "Did upgrading library L break anything?" | Library pins per service |

---

## Reference Files

Cross-cutting:

- `pipeline.properties`
- `cicd/CloudwatchAlarms.yaml`
- `boot/*-Service-task.json`

Per-service POMs / csproj:

- `integrations-wfm-streamconsumer/pom.xml`
- `integrations-wfm-stateaggregator/pom.xml`
- `integrations-wfm-intervalreader/pom.xml`
- `integrations-wfm-verintpublisher/pom.xml`
- `WfmConfig/WfmConfig.csproj`
- `integrations-wfm-etlscheduler/WfmEtlScheduler/WfmEtlScheduler.csproj`
- `integrations-wfm-aggregator/wfm-intervalaggregator/wfm-intervalaggregator.csproj`
- `integrations-wfm-intervalpublisher/WfmIntervalPublisher/WfmIntervalPublisher.csproj`

### Related skills

- `wfm-system-architecture` — high-level platform overview
- `wfm-execution-flow` — step-by-step flows
- `wfm-observability` — metrics + log group ownership
- Module skills for service-specific internals
