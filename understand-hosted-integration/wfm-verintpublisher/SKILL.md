---
name: wfm-verintpublisher
description: Use this skill when the user works on, debugs, or asks about the `integrations-wfm-verintpublisher` Java service — the S3-file-driven publisher that consumes Verint-format JSON files from S3 (written by IntervalAggregator), parses them, and POSTs to per-tenant Verint REST APIs. Triggers include "VerintPublisher", "SqsVerintPublishQueue", "AwsS3Service", "MessageProcessingService", "CSIQueuePerformanceService", "AgentPerformanceService", "AgentPerformanceHelper", "TTI_*.json", "verint/{BU}_{TenantId}", "Verint API base URL", "External_GetAllTenantData", "QueueStatsController", "AgentPerformanceController", or any Verint-publishing question. Do NOT use for: file generation (use `wfm-aggregator`), IEX SFTP publishing (use `wfm-intervalpublisher`), or real-time IEX ASCWS publishing (use `wfm-statepublisher`).
---

# Module: integrations-wfm-verintpublisher

## Architecture Overview

VerintPublisher is a **file-driven, SQS-notified Java service** that consumes Verint interval files from S3. IntervalAggregator writes JSON files into `s3://<bucket>/verint/{BU}_{TenantId}/` and `s3://<bucket>/verintadherence/{BU}_{TenantId}/`; S3 PutObject events notify `SqsVerintPublishQueue`; VerintPublisher receives the SQS message, fetches the file from S3, parses it, and POSTs the formatted payload to the tenant's configured Verint REST endpoint.

It does **not** read DynamoDB directly. The DynamoDB-read happens upstream in `wfm-aggregator`.

> **Routing is by message content, not filename.** `MessageProcessingService.determineMessageType()` (verified `MessageProcessingService.java` lines 50-62; `AgentPerformanceHelper.java` line 251) examines the message body for the string `"AGENT_PERFORMANCE_TRIGGER"`. If matched → `processAgentPerformanceAggregation()` (fetches `TTI_*.json` from S3 at `AgentPerformanceHelper.java` line 292). Otherwise → `processQueuePerformanceFiles()` at line 96 for queue files.

### Tech stack

- Java / Spring Boot (`@EnableScheduling`)
- AWS SDK for S3 + SQS
- Aurora MySQL via Dapper-style helpers (tenant config + per-tenant Verint API base URL)
- Spring `RestTemplate` for outbound Verint REST calls
- xUnit-style JUnit tests under `src/test/java/com/nicewfm/`

### Entry point

```
src/main/java/com/nicewfm/
├── IntegrationsWfmVerintpublisherApplication.java   # @SpringBootApplication + @EnableScheduling
├── sqs/SqsQueueService.java                         # SQS listener wiring (line 20-24)
├── service/MessageProcessingService.java            # parses S3 event payloads
├── service/AwsS3Service.java                        # S3 fetch (line 35-59)
├── service/CSIQueuePerformanceService.java          # queue-perf publisher
├── service/AgentPerformanceService.java             # agent-perf publisher (TTI files)
├── service/AgentPerformanceHelper.java              # parses TTI_*.json paths
└── controller/{QueueStats,AgentPerformance}Controller.java
```

### Request lifecycle

```mermaid
flowchart LR
    AGG[IntervalAggregator] -->|PutObject| S3[(S3 verint/{BU}_{TenantId}/ + verintadherence/)]
    S3 -->|S3 event| Q[(SqsVerintPublishQueue)]
    Q -->|listener| SQ[SqsQueueService]
    SQ --> MP[MessageProcessingService<br/>getFileDetailsFromMessage]
    MP --> AS[AwsS3Service.fetchFile]
    AS -->|read JSON| ROUTE{TTI_ prefix?}
    ROUTE -- yes --> AP[AgentPerformanceService]
    ROUTE -- no --> CSI[CSIQueuePerformanceService]
    AP -->|POST| V[(Verint API per-tenant)]
    CSI -->|POST| V
```

### External dependencies

- **S3** — bucket `aws.S3Bucket` (default `integrations-wfm-interval-data-dev-us-west-2`)
- **SQS** — queue `SqsVerintPublishQueue`
- **Aurora** — per-tenant Verint config via `External_GetAllTenantData()` stored procedure (returns `TenantConfigRelation` mapped to `TenantData`)
- **Verint REST API** — endpoint per tenant
- **CloudWatch** — metrics + logs

---

## Core Components

### `IntegrationsWfmVerintpublisherApplication.java`

Spring Boot main; `@EnableScheduling` for any retry / periodic jobs.

### `SqsQueueService.java` (lines 20-24)

Wires an SQS listener (long-poll) on `SqsVerintPublishQueue`. Each message body is an **S3 event notification** containing bucket + key.

### `MessageProcessingService.java`

```java
FileDetails getFileDetailsFromMessage(Message m);   // line 107-119
```

Parses the SQS message body (S3 event JSON) into a `FileDetails` object: bucket, key, BU+TenantId, filename, file-type detection.

### `AwsS3Service.java` (lines 35-59)

```java
String fetchFile(String bucket, String key);   // reads JSON content from S3
```

Single responsibility: fetch the file body. Errors propagate so SQS visibility timeout drives retry.

### Two publishing pipelines

| Message type (via `determineMessageType()`) | Service | Files read |
|---------------------------------------------|---------|------------|
| `AGENT_PERFORMANCE_TRIGGER` | `AgentPerformanceService` (helper `AgentPerformanceHelper`) | `TTI_*.json` from S3 |
| (other) | `CSIQueuePerformanceService` | Queue files under `verint/` |

Both build a Verint REST payload and POST via `RestTemplate`. Tenant config (including API endpoint URL fragments) is loaded via `AuroraDbService.java` line 56 calling stored procedure `External_GetAllTenantData()`, which returns `TenantConfigRelation` objects mapped to `TenantData`.

> The underlying tenant-config table is in the Aurora schema (the `External_GetAllTenantData` procedure abstracts the schema). Do not assume specific column names like `api_base_url` without reading the procedure body — verify against `integrations-wfm-database/StoredProcedures/External_GetAllTenantData.sql`.

### REST controllers (admin / on-demand)

| Controller | Endpoint |
|-----------|---------|
| `QueueStatsController` | `POST /api/verint/queue-performance` (lines 17-52) |
| `AgentPerformanceController` | `POST /api/verint/agent-performance` (lines 22-71) |
| `CacheController` | tenant cache management |
| `TokenTestController` | Verint token diagnostic |
| `SqsQueueController` | SQS admin |
| `HealthCheckController` | health endpoint |

These let operators trigger the same publish path manually without waiting for an SQS message.

### Invariants

- One SQS message → one S3 GetObject → one Verint POST → one SQS DeleteMessage
- Routing is **filename-based**: `TTI_` prefix means agent performance; otherwise queue performance
- Verint endpoint URL is **per-tenant**, looked up from Aurora — not in env vars
- VerintPublisher does **not** generate files; it only consumes them

---

## Service Interactions

### Inbound

- `SqsVerintPublishQueue` SQS messages (S3 event notifications from `verint/` and `verintadherence/` prefixes)
- REST API for on-demand publishing (`/api/verint/*`)

### Outbound

- S3 `GetObject` against the bucket in the SQS event
- Verint REST per tenant (base URL + credentials returned by `External_GetAllTenantData()`)
- Aurora MySQL (tenant config, datasource keys, auth)
- CloudWatch metrics + logs

### Auth & error

- AWS: ECS task role for SQS + S3 + CloudWatch
- Aurora: credentials from Secrets Manager
- Verint: per-tenant credentials returned by `External_GetAllTenantData()`
- On failure: throw → SQS visibility timeout → redelivery; persistent → DLQ

---

## Data Models

### S3 event (incoming SQS message body)

Standard S3 event JSON; `MessageProcessingService` extracts bucket + key.

### File content

- **Queue file** (`verint/{BU}_{TenantId}/yyMMdd.HHmm.json`) — JSON array of skill-level interval metrics
- **Agent file** (`verintadherence/{BU}_{TenantId}/TTI_yyyyMMdd.HHmm.json`) — JSON array of agent time-tracking rows

### Tenant config lookup

```
TenantData {
    WfmConfig {
        Config {
            ApiBaseUrl;           // Verint REST base
            DatasourceCsi;        // queue datasource key
            DatasourceAgent;      // agent datasource key
            // ... auth / token / business unit details
        }
    }
}
```

Sourced from Aurora via `AuroraDbService.getAllTenantData()` calling `CALL External_GetAllTenantData()` (verified `AuroraDbService.java` line 56). The underlying table layout is encapsulated in the stored procedure — read `External_GetAllTenantData.sql` for the exact columns.

---

## Conventions & Patterns

### File layout

```
src/main/java/com/nicewfm/
├── IntegrationsWfmVerintpublisherApplication.java
├── sqs/                  # SQS listeners
├── service/              # AwsS3Service, MessageProcessingService, CSI/Agent services, AuroraDbService
├── controller/           # REST endpoints
├── dto/                  # QueuedMessage, payload DTOs
├── config/               # SwaggerConfig, RestTemplate config
├── util/                 # BatchUtils, StatLabels, Utility
├── monitoring/           # CloudWatch + health
└── exception/            # GlobalExceptionHandler
```

### Tests (`src/test/java/com/nicewfm/`)

A large suite — examples:

- `service/AwsS3ServiceTest`
- `service/MessageProcessingServiceTest`
- `service/CSIQueuePerformanceServiceTest`, `AgentPerformanceServiceTest`
- `service/TenantServiceTest`, `AuroraDbServiceTest`, `AuthenticationServiceTest`
- `service/AwsSecretFetcherTest`
- `controller/QueueStatsControllerTest`, `AgentPerformanceControllerTest`
- `sqs/QueueListenerServiceTest`, `SqsQueueServiceTest`
- `monitoring/AwsCloudWatchServiceTest`, `HealthMonitorTest`

### Logging

- Structured JSON to CloudWatch log group `integrations-wfm-verintpublisher`
- Correlation: `tenantId`, `bu`, `intervalStart`, `s3Key`, HTTP status from Verint

---

## Configuration

### Application config (`application.yml`)

```yaml
aws:
  S3Bucket: integrations-wfm-interval-data-dev-us-west-2   # line 25
  SqsVerintPublishQueue: <queue-name>                       # line 27
  region: <region>
```

### Environment variables

```bash
AWS_REGION                          # AWS region
SqsVerintPublishQueue               # SQS notification queue from S3
S3_BUCKET                           # interval-data bucket
AuroraSecret                        # Secrets Manager key for Aurora creds
```

### Secrets Manager

- Aurora credentials (per `AwsSecretFetcher`)
- Per-tenant Verint credentials are returned by `External_GetAllTenantData()` (Aurora-backed). Not Secrets Manager.

### Operational runbook

`L3-OPERATIONAL-RUNBOOK.md` at the repo root has SRE-facing operational steps.

---

## Common Tasks

### Trigger a manual publish

```bash
# Queue performance for a specific file
curl -X POST https://<host>/api/verint/queue-performance \
     -d '{ "bucket": "...", "key": "verint/<BU>_<TenantId>/yyMMdd.HHmm.json" }'

# Agent performance
curl -X POST https://<host>/api/verint/agent-performance \
     -d '{ "bucket": "...", "key": "verintadherence/<BU>_<TenantId>/TTI_*.json" }'
```

### Verify a tenant's Verint endpoint

```sql
CALL External_GetAllTenantData();
-- inspect the row for your tenant; column names depend on the procedure body
-- (read integrations-wfm-database/StoredProcedures/External_GetAllTenantData.sql)
```

### Diagnose "Verint not receiving data"

1. **Is the file in S3?** `aws s3 ls s3://<bucket>/verint/<BU>_<TenantId>/`
2. **Did the S3 → SQS notification fire?** Check `SqsVerintPublishQueue` depth + recent receives.
3. **Is VerintPublisher consuming?** Check CloudWatch logs for the file key.
4. **Did Verint accept the POST?** Check HTTP status logs (`CSIQueuePerformanceService` / `AgentPerformanceService`).
5. **Is the Verint URL correct?** Run `CALL External_GetAllTenantData()` and inspect the row for your tenant.

### Rotate per-tenant Verint creds

Update the underlying tenant-config row in Aurora (the table updated by `External_GetAllTenantData` — read the SQL to find it) or via WfmConfig REST endpoints if exposed. VerintPublisher reads tenant data on each request (or via in-memory cache invalidated by `CacheController`).

---

## Troubleshooting

| Symptom | Diagnosis |
|---------|-----------|
| SQS depth growing | VerintPublisher listener stopped or per-file processing failing |
| 401/403 from Verint | Per-tenant credentials wrong in Aurora; use `TokenTestController` to verify auth |
| Wrong tenant data sent | `MessageProcessingService` parsing wrong BU/TenantId from S3 key — file naming convention drift |
| File in S3 but no SQS event | S3 → SQS event notification config missing for the prefix |
| Files in `verintadherence/` not routed to agent service | Filename missing `TTI_` prefix or routing rule incorrect |

---

## Reference Files

- `src/main/java/com/nicewfm/IntegrationsWfmVerintpublisherApplication.java`
- `src/main/java/com/nicewfm/sqs/SqsQueueService.java` (lines 20-24)
- `src/main/java/com/nicewfm/service/AwsS3Service.java` (lines 35-59)
- `src/main/java/com/nicewfm/service/MessageProcessingService.java` (line 107-119)
- `src/main/java/com/nicewfm/service/CSIQueuePerformanceService.java`
- `src/main/java/com/nicewfm/service/AgentPerformanceService.java`
- `src/main/java/com/nicewfm/service/AgentPerformanceHelper.java`
- `src/main/java/com/nicewfm/controller/QueueStatsController.java` (lines 17-52)
- `src/main/java/com/nicewfm/controller/AgentPerformanceController.java` (lines 22-71)
- `src/main/resources/application.yml` (line 25 = bucket, line 27 = queue)
- `L3-OPERATIONAL-RUNBOOK.md` — operator runbook

### Related skills

- `wfm-aggregator` — generates the files this service consumes
- `wfm-intervalpublisher` — sibling publisher for IEX (SFTP) files
- `wfm-statepublisher` — different service: real-time agent state to IEX ASCWS
- `wfm-config` / `wfm-database` — Aurora schema reached via `External_GetAllTenantData` procedure
- `wfm-execution-flow` — historic interval file pipeline
- `wfm-observability` — log group + metrics
