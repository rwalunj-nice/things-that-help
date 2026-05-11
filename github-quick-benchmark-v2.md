# 📊 Github Quick Benchmark v2 — Workflow-Aware Metrics

> **What's new in v2:** A pre-classification step using **Agent Contribution %** (available directly from the Power BI AI Usage dashboard) assigns each user a Workflow Type before applying T1 benchmarks. This fixes the core structural gap in v1 where the 20–35% acceptance benchmark was applied to agent-mode users who are architecturally expected to score near 0%.

---

## Step 0 — Workflow Type Classification (Run This First)

Determine each user's workflow type from the **Agent Contribution %** metric in the Power BI AI Usage tab.

| Workflow Type | Agent Contribution % | What It Means |
|---|---|---|
| **Agent-First** | ≥ 70% | User primarily works through agent prompts. Copilot generates large code blocks autonomously. % Code Acceptance is structurally near zero. |
| **Hybrid** | 30–69% | User mixes agent sessions with inline completions. Both acceptance rate and efficiency are relevant. |
| **Inline-First** | < 30% | User primarily uses inline completions. % Code Acceptance is the most reliable T1 signal. |

> **How to calculate Agent Contribution %:** Available directly in Power BI AI Usage dashboard as "Agent Contribution." No manual calculation needed.

---

## 🥇 TIER 1 — Core Signals (Apply per Workflow Type)

### Agent-First Users (Agent Contribution ≥ 70%)

| Metric | What It Tells You | Good Looks Like |
|---|---|---|
| **Request Efficiency** | LoC produced per premium request — primary signal for agent-mode users | > 15 LoC/request |
| **Agent Contribution %** | Confirms workflow classification; stability signals consistent agent usage | Stable or increasing |
| **Code Acceptance Count** | Even at low rates, non-zero count confirms completions are being used alongside agent | Any positive count |

> ⚠️ **Do NOT apply % Code Acceptance benchmark to Agent-First users.** Near-zero acceptance is correct behavior for this workflow type, not a failure signal.

---

### Hybrid Users (Agent Contribution 30–69%)

| Metric | What It Tells You | Good Looks Like |
|---|---|---|
| **% Code Acceptance** | Partial signal — inline suggestions are part of their workflow | 15–30% (lower than inline benchmark due to agent sessions diluting the rate) |
| **Request Efficiency** | Still important — agent sessions should justify their premium cost | > 8 LoC/request |
| **Code Acceptance Count** | Volume of inline suggestions accepted | Trending upward |

---

### Inline-First Users (Agent Contribution < 30%)

| Metric | What It Tells You | Good Looks Like |
|---|---|---|
| **% Code Acceptance** | Primary signal — are suggestions relevant and trusted? | 20–35% |
| **Code Acceptance Count** | Volume of accepted suggestions | Higher = more value; compare within team |
| **Agent Adoption** | Are they advancing toward agent workflows? | Any upward movement |

---

## 🥈 TIER 2 — ROI Signals (Universal — Apply to All Workflow Types)

| Metric | What It Tells You | Good Looks Like |
|---|---|---|
| **Request Efficiency** | LoC produced per paid premium request | > 10 (all types); > 15 preferred for Agent-First |
| **Premium Requests Count** | Budget consumption | Watch outliers at 1,700+; always pair with efficiency |

---

## 🥉 TIER 3 — Context Signals (Never Standalone — All Workflow Types)

| Metric | What It Tells You | ⚠️ Caveat |
|---|---|---|
| **Initiated Interactions** | How many prompts did a dev send? | High count in Agent-First = normal; high count in Inline-First = may indicate struggling |
| **Suggestion Efficiency** | Lines added per generation event | Inflated by agent mode — only compare within same workflow type |
| **LoC Suggested** | Lines Copilot offered (accepted or not) | Directional only; varies by IDE and workflow type |
| **LoC Added** | Lines that actually landed in the editor | Agent mode can add 2,000+ from one prompt |
| **Code Generation Count** | Total Copilot output events (including rejected) | High generation + low acceptance is normal for Agent-First; problematic for Inline-First only |

---

## ⚡ Quick Decision Map (v2 — Workflow-Aware)

| Question | Look At | What Good Looks Like |
|---|---|---|
| What's their workflow type? | **Step 0:** Agent Contribution % | Classify before applying any benchmark |
| Is Copilot useful (Agent-First)? | **T2:** Req Eff + **T1:** LoC trend | Eff > 15, LoC growing week-over-week |
| Is Copilot useful (Inline-First)? | **T1:** % Acceptance + Count | Acceptance 20–35%, Count trending up |
| Is the spend justified? | **T2:** Req Eff + Premium Requests | High efficiency (> 10 LoC/request), no outlier spend |
| Why are numbers off (Agent-First)? | **T3:** Interactions, LoC Added vs Sugg | Agent-First should have LoC Added >>> LoC Sugg |
| Why are numbers off (Inline-First)? | **T3:** Code Gen vs Acceptance | High gen + low accept = poor suggestion fit for their code |
| Is their Agent Contribution % appropriate? | Compare to team average | Sudden spikes may indicate workflow drift, not improvement |

---

## Workflow Type Summary Card

Use this to quickly label each user before tiering:

| User | Agent Contribution % | Workflow Type | Apply T1 Benchmark |
|---|---|---|---|
| *Example: Mikhail Shnayderman* | *~100%* | *Agent-First* | *Req Eff > 15, skip % Accept* |
| *Example: Chris Haun* | *~50%* | *Hybrid* | *% Accept 15–30% + Eff > 8* |
| *Example: Vitthal Devkar* | *~20%* | *Inline-First* | *% Accept 20–35%* |

> Fill this table from Power BI AI Usage → Agent Contribution column filtered per user before running the weekly analysis.

---

*v2 maintains full backward compatibility with v1 tier definitions (A–E). The only change is Step 0 classification gates which T1 benchmark applies. Existing T2 and T3 signals are unchanged.*
