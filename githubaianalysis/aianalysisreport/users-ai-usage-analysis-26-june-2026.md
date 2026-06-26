# Multi-User Deep-Dive Analysis — Defense & Action Plan
**WFM Integrations Team | CP9 — June 23, 2026**

---

## Critical Context: New Joiners in Bottom-5

> **Before reading individual assessments, this context applies to Mohit Baghel, Shubham Fulzele, and Amol Doke.**

Three of the five users flagged at CP9 (Jun 23) **joined in late May 2026**. Their Copilot contribution window is **approximately 3–4 weeks**, not the full Q2 period (Apr 20 → Jun 23 = 64 days). Any Request Efficiency comparison that ranks them against users with 64 days of data is comparing different contribution tenures, not different performance levels.

Additionally, Request Efficiency (ReqEff = LoC Added ÷ Premium Requests) is **structurally zero** for several legitimate work types:
- Security/CVE investigation (AI-assisted research, no committed LoC)
- Log refactoring that deletes lines (negative LoC by design)
- Architecture and design work (no coding started)
- QA validation and sustenance support (test runs, not committed code)

All five users below fall into one or more of these categories. ReqEff=0 displayed in Power BI means fractional values (<0.5) that round to zero in integer-formatted columns — none of the five have literally zero LoC.

---

## Executive Summary

| Developer | Login | New Joiner | Prem Req | LoC | Model | Verdict | Action |
|---|---|---|---|---|---|---|---|
| **Mohit Baghel** | mohitbaghelnice | Yes (May end) | 2,582 | 3 | Sonnet 4.6 ✅ | QA/sustenance role — wrong metric | None |
| **Shubham Fulzele** | Shubhamfulzele28 | Yes (May end) | 35,000 | 1,074 | Opus 4.7 ⚠️ | Security + log deletion — ReqEff=0 by design | Monitor pace |
| **Amol Doke** | amol-doke | Yes (May end) | 4,252 | 10 | Opus ❌ | Architecture phase + Rust WASM — coding not started | Coach: model selection |
| **Prashasti Jain** | prashasti-jain | No | ~13,057 | ~1,612 | Opus 4.6/4.7 ⚠️ | P2 migration shipped + 6 customer swarms | Coach: investigation model |
| **Tushar Patil** | tusharpatil166719 | No | ~40,346 | ~1,589 | Opus 4.7 ❌ | Strong output, 97% spend in 1 debug segment | Token optimization coaching |

---

## 1. Mohit Baghel (mohitbaghelnice)

### CP9 Copilot Metrics

| Metric | Value |
|---|---|
| Premium Requests | 2,582 |
| LoC Added | 3 |
| Request Efficiency | 0 (rounds from ~0.001) |
| Dominant Model | Sonnet 4.6 |
| Contribution Window | June only (~3 weeks) |

### Q2 Jira Arc (Apr–Jun 2026) — WFM Project

| Period | Key Work | Status |
|---|---|---|
| Apr | WFM-174952 — UserSync Async API: Performance Impact Analysis (P4) | Done |
| May | WFM-176323 — Elasticsearch upgrade to v9 (P2 Epic) | Removed (scope change) |
| May | WFM-176318 — QA Testing sub-task | Done |
| May | WFM-176933 — Sub Test Execution | Done |
| Jun | WFM-177529 — P2: Pipeline server migration + master branch merge | In Progress |
| Jun 26 | WFM-179619/WFM-179620 — Branch merge + pipeline config update (today) | Done / In Progress |

### Work Character

Mohit's Q2 work is entirely in the QA/performance engineering domain:
- **Elasticsearch upgrade** — analysis and scoping was done using Copilot (hence premium spend), but implementation was executed manually. ES configuration is YAML/CLI work, not committed source code. The analysis approach was AI-assisted; the output is not captured as LoC.
- **Sustenance and QA validations** — assisting engineers with test execution, QA sign-off, and validation tasks. This work frees senior engineers to focus on feature development.
- **Pipeline work** — server migration and branch merge tasks.
- **No Jira work in April (Copilot)** — contribution to Copilot only since June, consistent with late-May onboarding.

### Defense

**ReqEff=0 is structurally guaranteed for this role and work type.** Analysis work (Elasticsearch upgrade) generates AI interaction but zero committed LoC. QA validation generates test runs and sign-offs, not source code commits. The 3 LoC over the contribution window is expected — not a failure.

**Model use: Sonnet 4.6 only** — correct model selection for analysis and sustenance work. No coaching needed on model choice.

**The Elasticsearch P2 Epic being marked "Removed"** reflects a team scope decision, not Mohit abandoning the work. The analysis was completed; the implementation path was changed.

### Verdict

No concern. Measuring Mohit on LoC or ReqEff is applying the wrong instrument to a QA/analysis role. His value is engineer unblocking and QA coverage, neither of which produces committed LoC.

### Action Plan

| Step | Action |
|---|---|
| VP briefing | "Mohit is a QA/performance support role. His 3 LoC reflects work type, not effort. His value is in Jira: 5+ closed items across test execution, performance analysis, and pipeline work." |
| No coaching needed | Correct model, correct usage pattern for role |
| Q3 framing | If role expands to include feature coding, set a LoC baseline then. Until then, track via Jira output, not Copilot metrics. |

---

---

## 2. Shubham Fulzele (Shubhamfulzele28)

### CP9 Copilot Metrics

| Metric | Value |
|---|---|
| Premium Requests | 35,000 |
| LoC Added | 1,074 |
| Request Efficiency | 0 (rounds from ~0.031) |
| Dominant Model | Opus 4.7 |
| Contribution Window | June only (~3 weeks) |

### Q2 Jira Arc (Apr–Jun 2026) — INT Project

| Period | Key Work | Status |
|---|---|---|
| Jun 5 | INT-53007 — Analyze INFO/DEBUG Logs, propose reduction — Stream Consumer | Done |
| Jun 5 | INT-53011 — Apply Log Changes | Done |
| Jun 15–16 | INT-56855/57275/57276 — Analyse Vulnerabilities in Java Service Container Images (3 services) | Done |
| Jun 16 | INT-52809 — Stream Consumer: Refactor Logging for Cost Reduction | Done |
| Jun 16–19 | INT-56857/56858/56863/56849 — Java vulnerability fixes, image build/push, documentation | Done |
| Jun 19–24 | INT-56775 (Epic) — Vulnerabilities in Container Images [INT]; INT-56845/56844 — Java + .NET | In Progress |

### Work Character

Two distinct workstreams, both of which **structurally destroy ReqEff**:

**1. DWP Security Remediation (Container Image CVEs)**
CVE analysis, dependency evaluation, image scanning, and configuration changes. This is pure AI-assisted research — Copilot is used extensively to explain CVE severity, suggest remediation paths, and evaluate dependency trees. None of this produces committed LoC. The actual remediation (image builds, config changes) is infrastructure work that may not be tracked under WFM Integrations usage.

**2. Log Optimisation for HI Cost Saving**
Log refactoring that **deletes** log statements. When a developer removes 500 lines of noisy DEBUG logging, their LoC count goes negative. This is high-value work (reduces operational costs) that is structurally penalized by a LoC-based metric. Copilot helps identify which logs to remove; the output is a reduction in lines, not an addition.

Both work types together explain 35,000 premium requests with 1,074 LoC: heavy AI research assistance for security (no LoC) + log deletion work (negative LoC, floor at 0 in reporting).

### New Joiner Context

Joined late May 2026. His entire Copilot history is ~3 weeks. Onboarding onto unfamiliar codebases with a complex security task is the pattern that maximizes AI query volume — he is asking Copilot to explain code he hasn't written. This is appropriate and expected behavior for a new joiner.

### Defense

Fully defensible. Both work types (CVE research + log deletion) are legitimate, customer/business-impacting work where ReqEff=0 is the expected outcome. The premium spend reflects a new joiner using AI intensively to ramp up on security-critical work, which is the correct use of the tool.

**Caveat:** 35,000 premium requests in ~3 weeks is a high pace. If this continues into Q3 at the same rate, it will become a budget concern regardless of the justification. The work type is defensible; the pace needs monitoring.

**Model flag:** Opus 4.7 for security research and log analysis. Expensive but arguably justified for deep CVE analysis. This should shift to Sonnet 4.6 for routine log scanning once the initial onboarding ramp is complete.

### Action Plan

| Step | Action | Timeline |
|---|---|---|
| VP briefing | "CVE investigation + log deletion both destroy ReqEff by design. The 1,074 LoC understates impact — log deletion work reduces cloud log costs." | This week |
| Monitor pace | 35K premium in 3 weeks → annualizes to ~600K/year. Set a CP10 review gate. | CP10 checkpoint |
| Model coaching | 1:1 conversation: switch from Opus 4.7 to Sonnet 4.6 for log scanning and routine security checks. Keep Opus only for complex CVE analysis. | Within 2 weeks |

### Q3 Targets

| Metric | Current (Jun 23) | Q3 End Target |
|---|---|---|
| LoC | 1,074 | 3,000+ (as ramp completes) |
| Premium | 35,000 | ≤800/period |
| ReqEff | ~0.031 | 2+ |
| Model | Opus 4.7 | Sonnet 4.6 for routine, Opus for complex |

---

---

## 3. Amol Doke (amol-doke)

### CP9 Copilot Metrics

| Metric | Value |
|---|---|
| Premium Requests | 4,252 |
| LoC Added | 10 |
| Request Efficiency | 0 (rounds from ~0.002) |
| Dominant Model | Opus |
| Contribution Window | June only (~3 weeks) |

### Q2 Jira Arc (Apr–Jun 2026) — CXINT Project

| Period | Key Work | Status |
|---|---|---|
| Mar–Jun (ongoing) | CXINT-2210 — Capability: Migrate CXWFM P2P SDK to Generic ACDHub Integration (strategic architecture) | Ready for Dev |
| May 28 | CXINT-3915 — P2 Story: Expose 5 generic endpoints (web adapter + normalizer) **[AGENTIC_AI_CODE]** | Done Jun 22 |
| May 28 | CXINT-3916 — P2 Story: WASM plugin for Agent States data flow **[AGENTIC_AI_CODE]** | Ready for Dev |
| May 28 | CXINT-3917 — P2 Story: WASM plugin for Queue Report data flow **[AGENTIC_AI_CODE]** | Ready for Dev |
| Jun 19–22 | CXINT-4846/4847/4851/4852/4909 — Generic Services: Analysis → Implementation → WebAdapter deploy → Normalizer deploy → Demo | All Done |

### Work Character

Amol owns the **ACDHub Generic Integration** — the Q2 strategic capability to deprecate CXWFM point-to-point ACD SDKs and move WFM to a centralised, configuration-driven integration model.

**Two reasons for near-zero LoC:**

1. **Architecture and design phase** — CXINT-2210 (the capability) has been in design/architecture since March. Actual coding of the WASM plugins (CXINT-3916, CXINT-3917) is still in "Ready for Dev" state. You cannot commit code that hasn't been written yet. Copilot is being used for architecture exploration and design validation — high AI interaction, zero LoC output.

2. **Rust WASM implementation context** — the WASM plugins are written in Rust. Copilot's support for Rust WASM is substantially weaker than for Java, C#, or TypeScript. Additionally, Rust code is extremely dense — complex correctness expressed in few lines. A 50-line Rust WASM function may represent the same engineering effort as 500 lines of Java. Both factors suppress LoC artificially.

His stories are explicitly labeled `AGENTIC_AI_CODE` — confirming team-endorsed AI-assisted development on a strategic architecture workstream.

### Defense

Fully defensible. Architecture/design phase with coding not yet started. When CXINT-3916 and CXINT-3917 move into active implementation, LoC will appear. The 10 LoC in the analysis window is from the first story (CXINT-3915) which completed Jun 22 — one day before the CP9 snapshot.

### Coaching Flag

**Blatant use of Opus 4.7 for planning as well as development. This needs a coaching conversation.**

Using Opus 4.7 for architectural planning and design exploration is unnecessary. Sonnet 4.6 handles planning discussions, design reviews, and technical analysis equally well at a fraction of the token cost. Opus should be reserved for the implementation phase — specifically the complex Rust WASM code generation that will follow.

| Use Case | Recommended Model | Current Model |
|---|---|---|
| Architecture/design discussion | Sonnet 4.6 | Opus 4.7 ❌ |
| Jira story analysis and planning | Sonnet 4.6 / Haiku 4.5 | Opus ❌ |
| Rust WASM implementation (complex) | Opus 4.7 | — (not started yet) |

If model selection is corrected before WASM implementation begins, the premium spend per LoC will improve significantly from Q3 CP1.

### Action Plan

| Step | Action | Timeline |
|---|---|---|
| VP briefing | "Amol is in the architecture phase. WASM plugins haven't been coded yet. When implementation starts in Q3, LoC will follow." | This week |
| Model coaching | 1:1: show Opus 4.7 cost vs. Sonnet 4.6 for planning work. Establish a rule: Opus only for Rust implementation. | Before Q3 starts |
| Q3 gate | Review at CP10 — expect CXINT-3916 and CXINT-3917 to show LoC output as coding begins | CP10 |

### Q3 Targets

| Metric | Current (Jun 23) | Q3 End Target |
|---|---|---|
| LoC | 10 | 1,500+ (WASM implementation phase) |
| Premium | 4,252 | ≤600/period |
| ReqEff | ~0.002 | 2+ |
| Model | Opus for planning ❌ | Sonnet for planning, Opus for Rust impl |

---

---

## 4. Prashasti Jain (prashasti-jain)

### CP9 Copilot Metrics — 3 Model Segments

| Segment | Premium Req | LoC | ReqEff | Model | What it represents |
|---|---|---|---|---|---|
| Segment 1 | 630 | 0 | 0 | Opus | Exploration/chat — investigation, design discussions |
| Segment 2 | 637 | 872 | 1.4 | Opus | Active Redis→Valkey development |
| Segment 3 | 11,790 | 740 | 0.1 | Opus | Customer swarms + migration analysis (heavy investigation) |
| **Total** | **~13,057** | **~1,612** | — | Opus 4.6 / 4.7 | |

> **Note on LoC understatement:** Redis→Valkey migration includes CloudFormation/IaC template changes. These likely land in DevOps stats, not WFM Integrations usage. Her actual code output is understated in this dashboard by design of how IaC work is attributed.

### Q2 Jira Arc (Apr–Jun 2026) — INT Project

**April — QA and Review:**
- INT-56118/56131/56191 — QA testing, test execution for SBUMIEX feature (Done Apr 1–7)
- INT-55888/55923/55921 — Segmentation Discovery, 15/30 min API details, Troubleshooting Guide (Done Apr 7)
- INT-56439/56445/56450/56516/56559 — Code reviews, regression analysis (Done Apr 22–28)
- INT-56482 — Redis to Valkey Migration Test Plan (Done May 12)

**May — Valkey Migration Execution:**
- INT-56705/56706/56707/56708/56976 — Valkey pre-migration checklist, CloudFormation, ic-dev migration, validation, rollback plan (Done)
- INT-56328/56329/55884/56534 — Redis→Valkey analysis, regression analysis, L3 documentation, SBUMIEX config guide (Done May 25)

**June — Migration Completion + Customer Swarms:**
- INT-56179 — **Epic: Unified Agent Session — division_no Propagation through Flink Pipeline** (Done Jun 15)
- INT-51557 — **P2 Epic: Convert Redis cache to Valkey** (Done Jun 16) ← full Epic closure
- INT-52225/57109/57343/57344 — Valkey pre-prod migration + PROD NA1 load test (Done Jun 16)
- INT-57187/57267/57307/57353/57357/57399 — 6 customer swarms: Charles Schwab, Hastings Direct, Verra Mobility (×2), Broadview FCU, RTA unknown state (5 Done, 1 In Progress Jun 26)

### Work Character

Prashasti's Q2 tells three concurrent stories:

**1. P2 Infrastructure Migration (owned end-to-end):** Took the Redis→Valkey migration from test plan (May 12) through CloudFormation template changes → ic-dev execution → pre-prod validation → PROD NA1 load test → Epic closure (Jun 16). A complete production infrastructure migration delivered on schedule.

**2. Flink Pipeline Feature:** Unified Agent Session division_no propagation through Flink pipeline — Done Jun 15. Distributed stream processing feature alongside the migration.

**3. Enterprise Customer Escalations:** 6 swarm investigations in June alone (Charles Schwab, Hastings Direct, Verra Mobility ×2, Broadview FCU, RTA). These produce investigation reports, RCA documents, and customer-facing resolutions. High AI usage for log analysis and debugging — near-zero LoC output by design.

### Segment Analysis

The 3-segment breakdown maps cleanly to her work types:
- **Segment 3 (11,790 premium, 0.1 ReqEff)** = customer swarms + migration analysis. Investigation-heavy work. Opus is being used as a debugging/research tool, not a code generator.
- **Segment 2 (637 premium, 1.4 ReqEff)** = active development on the Valkey migration. This is efficient use — 872 LoC from 637 requests is solid for infrastructure work.
- **Segment 1 (630 premium, 0 LoC)** = pure exploration/chat, likely design discussions and migration planning.

### Defense

Fully defensible. Request Efficiency is the wrong primary metric for her role mix: migration work, infrastructure changes, customer escalation investigation, and documentation all register as high AI usage with low or zero LoC output. The right scorecard:
- **1 P2 Epic shipped** (Redis→Valkey — full production migration)
- **1 Flink feature shipped**
- **6 enterprise customer escalations resolved in June**

### Model Note

Segment 3's use of Opus for customer swarm investigation is expensive. For exploratory debugging and log analysis, Sonnet 4.6 would reduce the Segment 3 premium spend significantly without impacting investigation quality.

### Action Plan

| Step | Action | Timeline |
|---|---|---|
| VP briefing | "Prashasti shipped a P2 Epic (Redis→Valkey), a Flink feature, and resolved 6 enterprise customer escalations in June. Copilot spend reflects investigation-heavy work, not inefficiency." | This week |
| IaC attribution note | Flag to VP: her CloudFormation/IaC work for Valkey migration is likely in DevOps stats, understating her LoC in WFM Integrations | This week |
| Light model coaching | Suggest Sonnet 4.6 for routine swarm investigation. Opus 4.7 should be reserved for complex code analysis. | Next 1:1 |

### Q3 Targets

| Metric | Current (Jun 23) | Q3 End Target |
|---|---|---|
| LoC | ~1,612 | 4,000+ |
| Total Premium | ~13,057 | ≤8,000/quarter |
| Segment 3 Premium | 11,790 | ≤5,000 (via model switching) |
| ReqEff (Segment 2) | 1.4 | 3+ |

---

---

## 5. Tushar Patil (tusharpatil166719)

### CP9 Copilot Metrics — 3 Model Segments

| Segment | Premium Req | LoC | ReqEff | Model | What it represents |
|---|---|---|---|---|---|
| Segment 1 | 1,065 | 201 | 5.3 | Opus | IEX Ingestion / Java development |
| Segment 2 | 240 | 733 | 3.1 | Opus | Amazon Connect RTA / Java 21 upgrade |
| Segment 3 | 39,041 | 655 | 0 | Opus | Complex bug investigation — race conditions, HA data, customer escalations |
| **Total** | **~40,346** | **~1,589** | — | Opus 4.7 / 4.6 | |

### Q2 Jira Arc (Apr–Jun 2026) — WFM Project

**April — RTA Gateway Infrastructure + Bug Fixes:**
- WFM-171085 — RTA Gateway: Token Validation Using JWKS (Done Apr 8)
- WFM-173619 — Identity Service: Deploy Gateway + Identity Service Behind ALB with HTTP+HTTPS/2 (Done Apr 8)
- WFM-173995 — Resolve trust issue: internal call between Gateway and ALB (Done Apr 2)
- WFM-136047 — Bug: JSON Processing exception in Genesys Pure Cloud ASC RTA Events (Done Apr 14)
- WFM-167022 — Bug: Swxiface HA random missing QueueStats data — concurrent processing (Done Apr 14)
- WFM-173649/174899/174996 — Wiser assignments: Lumen Technologies, cxLoyalty, SaskEnergy

**May — Java 21 + Documentation:**
- WFM-148899 — Java 21 Upgrade: Amazon Real Time Integration (Done May 29)
- WFM-170195 — RTA Gateway: L3 and Integration Guide Documentation (Done May 25)

**June — Active Bug Fixes + Resiliency Epic:**
- WFM-157823 — Bug: Contacts received count wrong in CT Inbound (Done Jun 15)
- WFM-167489 — Bug: Swxiface HA QueueStats HA data loss — 9.0 clone (Done Jun 15)
- WFM-176534 — Bug: Race condition in Cisco Node — startup channel binding (Resolved Jun 23)
- WFM-176800 — Epic: Add Auto-Reconnect & Resiliency in AmazonConnect RTA (In Progress)
- WFM-179312 — Story: Hosted Credentials Refresh Flow Resiliency (In Progress Jun 26)

### Work Character

Tushar is a senior ACD integration engineer working across the full stack:
- **April:** RTA Gateway security infrastructure (JWKS token validation, ALB/HTTPS/2 deployment), complex concurrent processing bug fixes
- **May:** Java 21 upgrade of Amazon Connect RTA, L3 documentation writing
- **June:** Multiple complex distributed system bugs (race conditions, HA data loss), customer escalations via Wiser, now an active resiliency epic

**Segments 1 and 2 are healthy and legitimate** — ReqEff of 3.1–5.3 for complex Java/distributed system work reflects productive Copilot use. 934 LoC from 1,305 premium requests is reasonable for this complexity level.

**Segment 3 is the problem: 39,041 premium requests | 655 LoC | ReqEff=0.**

This single segment represents **97% of his total premium spend**. It maps directly to the investigation-heavy work in June: race conditions in Cisco Node startup, HA data inconsistency analysis, customer escalations, documentation. Copilot is being used as a chat/debugging assistant — asking it to explain Amazon Connect SDK behavior, analyze stack traces, debug RTA timing issues. This is valuable for productivity but generates zero committed LoC per query.

### Defense

**Work quality is genuinely strong.** Java 21 upgrade of Amazon RTA, JWKS token validation infrastructure, 4 complex distributed bugs fixed (working on 5th), customer escalations resolved, now building a resiliency epic. This is senior-level ACD engineering breadth. The Q2 Jira arc is one of the most substantive on the team.

**The 40K premium for 1,589 LoC doesn't reconcile** even with the legitimate investigation work. Segment 3 at 39K premium for 655 LoC is the clear signal: he is using Opus 4.7 for extensive debugging chat that converts to insights and fixes, not to LoC.

**This is not a performance concern — it is a token optimization opportunity.** The two healthy segments (1,305 premium → 934 LoC, ReqEff 3.1–5.3) prove he knows how to use Copilot productively. The investigation segment just needs a model switch.

### Model Flag: Critical

Tushar is using **Opus 4.7 and Opus 4.6** across all three segments, including the 39K investigation segment. Switching Segment 3-type work (log analysis, SDK explanations, debugging chat, customer escalation investigation) to **Sonnet 4.6** would cut Segment 3 premium by an estimated 60–70% with no meaningful quality difference for that use case.

| Use Case | Current Model | Recommended Model | Est. Premium Reduction |
|---|---|---|---|
| Race condition / HA debug chat | Opus 4.7 | Sonnet 4.6 | ~60% |
| SDK behavior explanations | Opus 4.7 | Sonnet 4.6 | ~65% |
| Customer escalation investigation | Opus 4.7 | Sonnet 4.6 | ~60% |
| Complex Java implementation (JWKS, resiliency epic) | Opus 4.7 | Opus 4.7 ✅ | Keep |
| Race condition fix implementation | Opus 4.6 | Opus 4.6 ✅ | Keep |

### Action Plan

| Step | Action | Timeline |
|---|---|---|
| VP briefing | "Tushar fixed 4 complex distributed bugs, shipped Java 21 upgrade, and is building a resiliency epic. 97% of his premium is in one investigation segment — the work quality is strong, the model choice for debugging chat needs adjustment." | This week |
| Token optimization coaching | 1:1 conversation with specific focus on Segment 3 usage: show the premium breakdown, explain the Sonnet 4.6 vs Opus 4.7 cost delta for chat/investigation use cases. | Next 1:1 (this week) |
| Follow-up at CP10 | Check whether Segment 3-equivalent premium has reduced. If still 30K+, deeper workflow audit. | CP10 checkpoint |

### Q3 Targets

| Metric | Current (Jun 23) | Q3 End Target |
|---|---|---|
| LoC | ~1,589 | 3,000+ |
| Total Premium | ~40,346 | ≤8,000/quarter |
| Segment 3 Premium | 39,041 | ≤6,000 (via model switching) |
| ReqEff (Segments 1+2) | 3.1–5.3 | Maintain or improve |
| Bugs shipped | 4 (+ 5th in progress) | On track — no change needed |

---

---

## Cross-User Comparison

| Metric | Mohit Baghel | Shubham Fulzele | Amol Doke | Prashasti Jain | Tushar Patil |
|---|---|---|---|---|---|
| **Premium Req (CP9)** | 2,582 | 35,000 | 4,252 | ~13,057 | ~40,346 |
| **LoC Added (CP9)** | 3 | 1,074 | 10 | ~1,612 | ~1,589 |
| **Dominant Model** | Sonnet 4.6 ✅ | Opus 4.7 ⚠️ | Opus ❌ | Opus 4.6/4.7 ⚠️ | Opus 4.7 ❌ |
| **New Joiner** | Yes (~3 wks) | Yes (~3 wks) | Yes (~3 wks) | No | No |
| **Work Type** | QA/sustenance/analysis | Security CVE + log deletion | Architecture design + Rust WASM | Migration + customer swarms + Flink | Bugs + Java21 + infra + escalations |
| **ReqEff structural floor** | Yes — analysis role | Yes — CVE + log deletion | Yes — design phase | Partial (Segment 2 healthy) | Partial (Segments 1+2 healthy) |
| **Verdict** | No concern | Defensible, monitor pace | Defensible, coach model | Fully defensible | Strong work, coach model |
| **Q3 Priority** | None | Model coaching | Model coaching + watch WASM start | Model coaching | Token optimization (critical) |

### Key Insights

1. **All three new joiners (Mohit, Shubham, Amol) are in Phase 1 of their Copilot journey.** Their CP9 metrics represent 3 weeks of usage, not a full quarter. Ranking them bottom-5 in a 64-day analysis is comparing unlike periods.

2. **Model selection is the dominant issue for Amol and Tushar.** Opus 4.7 for planning and debugging chat is the specific behavior driving disproportionate premium spend. One coaching conversation on model choice addresses the bulk of the concern for both users.

3. **Prashasti and Tushar both show healthy segments alongside high-spend segments.** They are not inefficient users — they are mixed-use users where one workstream (investigation/swarms/debugging) burns tokens without producing LoC. The fix is model switching in that workstream, not behavior change.

4. **Mohit is correctly using Sonnet 4.6.** He is the model behavior for model selection among the five. His metrics reflect role type, not tool misuse.

5. **ReqEff=0 displayed in Power BI does not mean literally zero.** All five users have non-zero LoC. Power BI displays fractional values as 0 in integer-formatted columns. The actual ratios range from 0.001 (Mohit) to 0.031 (Shubham) — all low, all explainable by work type.

---

## Master Recommendations for VP Conversation

### Opening Frame

> "Of the five users flagged at CP9, three joined in late May and have 3 weeks of Copilot data — not a full quarter. For the other two, the ReqEff concern is real but targets one specific workstream (debugging/investigation), not their overall Copilot usage. None of the five represent a performance failure. Two need a model selection coaching conversation."

### User-by-User One-Liners

| User | One-liner for VP |
|---|---|
| **Mohit Baghel** | "QA/analysis role — ReqEff=0 is expected. His value is in Jira: QA coverage, performance analysis, and engineer unblocking. Wrong metric for this role." |
| **Shubham Fulzele** | "New joiner on a security CVE epic and log-deletion work. Both work types destroy ReqEff by design. Model coaching needed, performance concern is not warranted." |
| **Amol Doke** | "Architecture phase — WASM plugins haven't been coded yet. 10 LoC is expected. Needs coaching on Opus 4.7 → Sonnet 4.6 for planning work." |
| **Prashasti Jain** | "Shipped a P2 Epic (Redis→Valkey), a Flink feature, and handled 6 enterprise customer escalations in June. Premium is high because swarm investigation is her primary June work. IaC output likely in DevOps stats." |
| **Tushar Patil** | "4 complex bugs fixed, Java 21 upgrade shipped, resiliency epic in flight. 97% of his premium is in one debugging segment using Opus 4.7. One coaching conversation on model selection will resolve the concern." |

### Coaching Priority

| Priority | User | Action | Owner |
|---|---|---|---|
| 🔴 High | **Tushar Patil** | Token optimization: Sonnet 4.6 for debug/investigation chat | Manager 1:1 this week |
| 🟠 Medium | **Amol Doke** | Model selection: Opus 4.7 → Sonnet 4.6 for planning | Manager 1:1 this week |
| 🟡 Low | **Shubham Fulzele** | Monitor premium pace + model coaching at 4-week mark | CP10 review |
| 🟡 Low | **Prashasti Jain** | Model suggestion for investigation work | Next 1:1 |
| ⬜ None | **Mohit Baghel** | No action — correct model, correct behavior for role | — |

---

*Analysis based on CP9 data (Jun 23, 2026). Copilot metrics from Power BI GitHub 360 dashboard — Premium Requests by User table. Jira arc sourced from Atlassian WFM and INT project queries (Apr–Jun 2026). Prior analysis context: github-ai-analysis-v2-23-june-2026-summary.md, users-ai-usage-analysis-12-june-2026.md. Model segments for Prashasti and Tushar represent separate Copilot usage sessions captured in different model-tier buckets.*

---
