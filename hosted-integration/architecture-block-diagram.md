# WFM Integration Platform — Simple Block Diagram

A high-level block diagram showing the two main pipelines, core services, and data stores.

---

## Block Diagram

```mermaid
block-beta
    columns 5

    %% Row 1 - External Sources
    block:sources:2
        ACD["ACD / DFO\n(Contact Center Events)"]
        DW["Cluster Data\nWarehouses"]
    end
    space
    block:targets:2
        VERINT["Verint WFM\n(REST)"]
        IEX["IEX WFM\n(SFTP + ASCWS)"]
    end

```

---

## Simplified Architecture (Flowchart)

```mermaid
flowchart TB
    subgraph Sources ["📥 EVENT SOURCES"]
        ACD["ACD / DFO Events"]
        DW["Cluster Data Warehouses\n(SQL Server)"]
        ADMIN["Admin / REST Clients"]
    end

    subgraph Ingestion ["🔵 INGESTION LAYER"]
        KINESIS["Kinesis Orchestration Stream"]
    end

    subgraph RealTime ["🟦 PIPELINE A: REAL-TIME AGENT STATE"]
        SC["StateCollector\n(C#)"]
        STC["StreamConsumer\n(Java)"]
        SA["StateAggregator\n(Java)"]
        SP["StatePublisher\n(C#)"]
    end

    subgraph Historic ["🟨 PIPELINE B: HISTORIC INTERVALS (15-min batch)"]
        ES["EtlScheduler\n(C#)"]
        IR["IntervalReader\n(Java)"]
        IA["IntervalAggregator\n(C#)"]
    end

    subgraph Publishers ["📤 PUBLISHER LAYER"]
        VP["VerintPublisher\n(Java)"]
        IP["IntervalPublisher\n(C#)"]
    end

    subgraph DataStores ["🟩 AWS DATA STORES"]
        REDIS[("Redis\n(Sorted Sets)")]
        DDB[("DynamoDB\n(Aggregated Facts)")]
        S3[("S3\n(Interval Files)")]
        SQS["SQS Queues\n(Standard + FIFO)"]
    end

    subgraph Config ["⚙️ CONFIGURATION"]
        CFG["WfmConfig\n(C#)"]
        AURORA[("Aurora MySQL")]
    end

    subgraph Targets ["📡 EXTERNAL TARGETS"]
        VERINT["Verint REST API"]
        IEXRT["IEX ASCWS\n(Real-Time)"]
        IEXSFTP["IEX SFTP\n(Historic)"]
        CXONE["CxOne WFM\n(Pickup)"]
    end

    %% Source → Ingestion
    ACD --> KINESIS
    DW --> ES

    %% Ingestion → Processing
    KINESIS --> SC
    KINESIS --> STC

    %% Real-Time Pipeline
    SC -->|"Kinesis WFM State"| SP
    SP --> IEXRT
    STC --> REDIS
    STC -->|"SQS"| SA
    STC -->|"SQS (prefixed)"| IR
    SA --> DDB

    %% Historic Pipeline
    ES -->|"HTTP"| IA
    IR --> SQS
    SQS --> IA
    DDB --> IA
    IA --> S3

    %% S3 → Publishers
    S3 -->|"S3 Event → SQS"| VP
    S3 -->|"S3 Event → SQS"| IP

    %% Publishers → Targets
    VP --> VERINT
    IP --> IEXSFTP
    S3 -.->|"File pickup"| CXONE

    %% Config
    ADMIN --> CFG
    CFG --> AURORA
    CFG -.->|"Config REST"| SC
    CFG -.->|"Config REST"| ES

    %% Styling
    classDef java fill:#4A90D9,color:#fff,stroke:#2C5F8A
    classDef csharp fill:#68217A,color:#fff,stroke:#4B1557
    classDef aws fill:#FF9900,color:#fff,stroke:#CC7A00
    classDef external fill:#E74C3C,color:#fff,stroke:#B03A2E
    classDef source fill:#27AE60,color:#fff,stroke:#1E8449

    class STC,SA,IR,VP java
    class SC,SP,ES,IA,IP,CFG csharp
    class REDIS,DDB,S3,SQS,KINESIS,AURORA aws
    class VERINT,IEXRT,IEXSFTP,CXONE external
    class ACD,DW,ADMIN source
```

---

## Legend

| Color | Meaning |
|-------|---------|
| 🟣 Purple | C# services (.NET 6+) |
| 🔵 Blue | Java services (Spring Boot 3.x) |
| 🟠 Orange | AWS managed services |
| 🔴 Red | External target systems |
| 🟢 Green | Event sources |

---

## Key Takeaways

1. **Two Pipelines**: The platform has a **real-time** streaming pipeline (per-event, Kinesis-driven) and a **historic batch** pipeline (15-min intervals, file-based via S3).

2. **Polyglot**: Java handles high-throughput stream processing (StreamConsumer, StateAggregator, IntervalReader, VerintPublisher). C# handles orchestration, configuration, and file generation.

3. **Event-Driven**: Services communicate via Kinesis streams, SQS queues, and S3 event notifications — minimal direct HTTP coupling.

4. **Multi-Tenant**: All services are multi-tenant; events carry `tenantId`. Publisher services route to per-tenant external endpoints.

5. **Multi-Region**: Deployed on ECS Fargate across 4 regions (NA2, NA3, UK2, ZA1) via Jenkins CI/CD.
