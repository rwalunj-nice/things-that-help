# WFM Integration Platform — Architecture Diagrams

Canonical, version-controllable architecture diagrams for the NICE WFM Integration Platform. Diagrams are stored as **source** (PlantUML `.puml` and mermaid `.mmd`) and rendered to `images/*.svg` + `images/*.png` via the bundled Makefile.

This folder is a sibling of the skill folders (`../wfm-*/`) and is referenced from the skills.

---

## Quick start

```bash
cd /Users/Swapnil.Zade/SwapnilZade/HostedIntegration/skills/architecture

# One-time install of rendering tools (brew + npm)
make install

# Render everything
make

# Render PlantUML only / mermaid only
make plantuml
make mermaid

# Watch mode (auto re-render on change)
make watch

# Outputs land in:
#   images/*.svg   - clean, scalable, paste-into-Confluence-friendly
#   images/*.png   - for screenshots, decks, dashboards
```

If `make install` fails or you don't have brew/npm, fall back to:

| Renderer | Online option |
|----------|---------------|
| PlantUML | https://www.plantuml.com/plantuml/uml/ |
| Mermaid  | https://mermaid.live |

GitHub also renders **both** PlantUML (with extensions) and mermaid (natively) inline in `.md` files.

---

## Diagram catalogue

### PlantUML (C4 model)

The C4 layers go from broad (Context) to narrow (Component). All four cover the same system at different zoom levels.

| File | Level | Purpose |
|------|-------|---------|
| [plantuml/01-system-context.puml](plantuml/01-system-context.puml) | C4 L1 — Context | Black-box view: external actors, source systems, target WFM backends |
| [plantuml/02-container-diagram.puml](plantuml/02-container-diagram.puml) | C4 L2 — Container | All 11 services + Kinesis/SQS/Redis/DynamoDB/Aurora and how they connect |
| [plantuml/03-deployment-topology.puml](plantuml/03-deployment-topology.puml) | Deployment | Jenkins → ECS Fargate per region (NA2, NA3, UK2, ZA1) + shared AWS services |
| [plantuml/04-component-aggregation-pipeline.puml](plantuml/04-component-aggregation-pipeline.puml) | C4 L3 — Component | Inside StreamConsumer + StateAggregator: record processors, aggregator services, DynamoDB helpers |

### Mermaid (sequence + flow)

Best for showing **what happens over time** or **who owns what**.

| File | Type | Purpose |
|------|------|---------|
| [mermaid/01-real-time-state-flow.mmd](mermaid/01-real-time-state-flow.mmd) | Sequence | ACD/DFO event → StateAggregator (DynamoDB) → Verint; parallel StateCollector → StatePublisher → IEX |
| [mermaid/02-etlscheduler-interval-flow.mmd](mermaid/02-etlscheduler-interval-flow.mmd) | Sequence | Full EtlScheduler loop: cluster fetch → DW poll → IntervalAggregator → SQS → IntervalPublisher |
| [mermaid/03-streamconsumer-interval-flow.mmd](mermaid/03-streamconsumer-interval-flow.mmd) | Sequence | StreamConsumer → IR queue → IntervalReader (Redis lock) → IntervalAggregator (alternate interval path) |
| [mermaid/04-configuration-flow.mmd](mermaid/04-configuration-flow.mmd) | Sequence | Admin REST → WfmConfig → Aurora; how services pick up config |
| [mermaid/05-etlscheduler-catchup.mmd](mermaid/05-etlscheduler-catchup.mmd) | Sequence | Failure recovery: EtlScheduler catch-up backfill after downtime |
| [mermaid/06-sqs-visibility-recovery.mmd](mermaid/06-sqs-visibility-recovery.mmd) | Sequence | Failure recovery: SQS visibility-timeout redelivery + DLQ path |
| [mermaid/07-aws-resource-ownership.mmd](mermaid/07-aws-resource-ownership.mmd) | Flowchart | Which service writes/reads each AWS resource (Kinesis, SQS, Redis, DynamoDB, Aurora, DW) |
| [mermaid/08-database-ownership.mmd](mermaid/08-database-ownership.mmd) | Flowchart | Which service calls which Aurora stored procedure / table (incl. `wfm_config`, `SftpConnectionData`) |
| [mermaid/09-verint-s3-file-flow.mmd](mermaid/09-verint-s3-file-flow.mmd) | Sequence | Detailed Verint S3 file-drop flow: DynamoDB → S3 → SqsVerintPublishQueue → VerintPublisher → per-tenant Verint API |

---

## Picking the right diagram for the situation

| You need to... | Use |
|---------------|-----|
| Onboard a new engineer to the platform | 01 → 02 → 07 (in that order) |
| Explain the platform to a stakeholder/PM | 01 only |
| Write a design doc for a new service | 02 (extend it) |
| Debug "why is interval data missing?" | 02 + 03 + 06 |
| Plan multi-region rollout | 03 |
| Understand internals of a single service | 04 + the relevant module skill |
| Trace one event end-to-end in logs | 01 (real-time) or 02 (interval) |
| Audit "who can read DB X" | 07 + 08 |
| Write a runbook for SQS DLQ | 06 |

---

## Conventions used

- **Sources are authoritative.** Edit `.puml` / `.mmd` only — never the rendered `images/*`.
- **C4 PlantUML stdlib** is pulled via `!include` URL — first render needs network; subsequent renders cached.
- **SVG** is preferred for embedding in docs (scales cleanly). **PNG** is fallback for tools that don't render SVG.
- **Filenames** are prefixed with two-digit numbers for stable sort order.

### Coloring conventions (mermaid 07/08)

- 🟦 Blue — C# services
- 🟨 Yellow — Java services
- 🟩 Green — AWS managed stores
- 🟥 Red — External systems
- 🟡 Pale yellow — Aurora stored procedures

---

## Related skills (text companions)

Each diagram has a textual sibling skill:

- [wfm-system-architecture](../wfm-system-architecture/SKILL.md) — pairs with 01, 02
- [wfm-execution-flow](../wfm-execution-flow/SKILL.md) — pairs with 01, 02, 03, 04 (mermaid)
- [wfm-dependency-mapping](../wfm-dependency-mapping/SKILL.md) — pairs with 07, 08
- [wfm-observability](../wfm-observability/SKILL.md) — pairs with 05, 06
- Module skills — pair with 04 (component) for that module's internals

---

## Existing PlantUML diagrams in the source repo

The codebase itself has per-service PlantUML diagrams at `Code/<service>/architecture/*.puml`. Those describe individual services in depth. The diagrams in **this** folder are the **cross-service / platform-level** view that doesn't exist anywhere else.

Existing per-service diagrams (not duplicated here):

- `Code/Web-Config/architecture/WFM-Configuration-Component.puml`
- `Code/integrations-wfm-aggregator/architecture/WFM-Aggregator-Component.puml` and 4 related diagrams
- `Code/integrations-wfm-etlscheduler/architecture/WFM-Scheduler-Component.puml`
- `Code/integrations-wfm-statecollector/architecture/WFM-Adherence-*.puml` (5 files)
- `Code/integrations-wfm-intervalpublisher/architecture/WFM-Publisher-Component.puml` + 1 more
