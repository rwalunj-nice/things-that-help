# GitHub Copilot Usage Analysis — v2 Workflow-Aware Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 12, 2026 | **Data Sync:** June 11, 2026 (1:07 AM)  
**Scope:** 45 users (15 excluded per ignore list) | **Framework:** v2 Workflow-Aware (2-Tier Adaptation)

---

## Framework Adaptation Notice

⚠️ **Data Limitation:** The Power BI dashboard does NOT provide "Agent Contribution %" column. Available data: "# Users Used Agents" (binary: 1 = used agents, 0 or blank = didn't).

**v2 Adaptation:**
- **Original 3-tier classification:** Agent-First (≥70%), Hybrid (30-69%), Inline-First (<30%)
- **Adapted 2-tier classification:**
  - **Used Agents**: # Users Used Agents = 1
  - **Inline-Only**: # Users Used Agents = 0 or blank

This reduces workflow granularity but maintains the core v2 principle: **classify first, then apply workflow-specific benchmarks**.

---

## What Changed vs v1 Standard (Same Period)

| User | v1 Tier | v2 Tier | Reason for Shift |
|---|---|---|---|
| Prathmesh-Ranadive | B | **A** | Used Agents + 86.9% accept + 27K LoC → Agent exception bypasses low ReqEff |
| chris-haun | C | **B** | Used Agents + 10.4K LoC → Volume + engagement compensates for low accept% |
| Akale23 | C | **B** | Used Agents + 22.9% accept improved signal |
| luisalvatierra | B | **C** | Used Agents but ReqEff 1.7 too low even with agent benchmark relaxation |

**Key insight:** In the 2-tier adaptation, "Used Agents" acts as a broad exception flag (similar to Agent-First in 3-tier). Users with the flag get evaluated primarily on **LoC volume + Request Efficiency**, with % Accept as secondary.

---

## Workflow Classification Summary

| Workflow Type | Count | % of In-Scope | Notes |
|---|---|---|---|
| **Used Agents** | ~43 | ~100% | All active users show "1" in # Users Used Agents column |
| **Inline-Only** | 0 | 0% | No users with "0" or blank in the agent column |

**Observation:** Every active user in this dataset has "# Users Used Agents = 1", meaning 100% agent adoption for this team. This makes the 2-tier classification less discriminating than intended. The workflow flag becomes a team-wide property, not a user differentiator.

**Implication:** v2 Workflow-Aware framework provides **minimal tier differentiation** from v1 in this dataset. The primary value is in documenting that this is an agent-first team universally.

---

## v2 Tier Assignments (43 Developers)

### 🌟 Tier A — Top Performers (7 developers)

| Login | Name | LoC | % Accept | ReqEff | Premium | Workflow | v1 Tier | v2 Rationale |
|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 41,008 | 1.5% | 3.7 | 11,150 | Used Agents | A | Highest LoC; ReqEff improving |
| Kranti-nice | Kranti Kaple | 31,645 | 1.2% | 2.6 | 11,979 | Used Agents | A | High LoC + engagement |
| mshnayderman | Mikhail Shnayderman | 27,539 | 27.8% | 5.1 | 5,419 | Used Agents | A | Strong accept + LoC |
| Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | 86.9% | 2.5 | 10,851 | Used Agents | B | **Promoted** — exceptional accept + high LoC; agent workflow bypasses low ReqEff |
| mfield1 | Matt Field | 9,800 | 6.0% | 5.4 | 1,813 | Used Agents | A | Consistent volume |
| rpawar-nice | Ritesh Pawar | 8,662 | 7.7% | 10.2 | 850 | Used Agents | A | Best efficiency in scope |
| Vitthal-Nice | Vitthal Devkar | 2,609 | 41.9% | 6.3 | 413 | Used Agents | A | High accept + lean spend |

---

### 👍 Tier B — Solid Contributors (5 developers)

| Login | Name | LoC | % Accept | ReqEff | Premium | v1 Tier | v2 Rationale |
|---|---|---|---|---|---|---|---|
| chris-haun | Chris Haun | 10,384 | 10.8% | 2.1 | 4,939 | C | **Promoted** — Agent workflow + 10.4K LoC compensates for low accept/ReqEff |
| luisalvatierra | Luis Salvatierra | 9,477 | 19.8% | 1.7 | 5,608 | B | **Demoted** — Used Agents but ReqEff 1.7 too low |
| jayesh-rai | Jayesh Rai | 2,479 | 19.6% | 2.9 | 852 | B | Stable |
| Akale23 | Amulya Kale | 2,472 | 22.9% | 0.7 | 3,779 | C | **Promoted** — Used Agents + improving accept rate |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,177 | 34.1% | 1.0 | 4,062 | C | **Promoted** — Strong accept compensates for collapsed ReqEff |

---

### 👌 Tier C — Needs Improvement (7 developers)

| Login | Name | LoC | % Accept | ReqEff | Primary Issue |
|---|---|---|---|---|---|
| moadzughul | Moad Alzughul | 3,409 | 2.4% | 1.1 | Low accept + low ReqEff |
| jkumbhar | Jyoti Kumbhar | 1,870 | 19.2% | 1.6 | Premium spike pattern |
| vishal-tad | Vishal Tad | 3,520 | 7.5% | 0.8 | Low ReqEff despite decent LoC |
| abhishekhole-nice | Abhishek Hole | 2,993 | 0.0% | 0.9 | 0 accepts in 199 interactions |
| abhijeetk268 | Abhijeet Kolhe | 656 | 29.6% | 1.9 | Low volume despite good rates |
| meghabiradar05 | Megha Biradar | 1,720 | 10.8% | 0.5 | Low ReqEff |
| dsuraj25 | Suraj Dubey | 504 | 12.7% | 0.7 | Low engagement |

---

### 🟠 Tier D — Low Efficiency (6 developers)

| Login | Name | LoC | % Accept | ReqEff | Issue |
|---|---|---|---|---|---|
| smishra-nice | Shridhar Mishra | 155 | 78.3% | 0.5 | Near-zero LoC despite high accept |
| sgite-wfm | Shubham Gite | 329 | 53.5% | 0.2 | High accept but premium 1,563 for 329 LoC |
| giteshsawant | Gitesh Sawant | 1,110 | 3.3% | 0.3 | Low accept + low ReqEff |
| suhas-kakde | Suhas Kakde | 1,677 | 1.7% | 0.8 | Low accept |
| prashasti-jain | Prashasti Jain | 1,545 | 8.6% | 0.3 | Premium spike pattern |
| Shreedevi-nice | Shreedevi Patil | 1,786 | 10.3% | 0.3 | Premium spike + low ReqEff |

---

### 🔴 Tier E — Urgent Attention (15 developers)

**Budget crisis group** (same as v1):
- nilesht-19, trunalgawade, PradnyeshSalunke, Shubhamfulzele28, thakraln, tusharpati166719

**Low-output group** (same as v1):
- sskalaskar, mshivarkar, pdevle, pratikpawar12, dannycadima, kbajaj-nice, and others

---

## v2 Executive Scorecard

| Tier | v2 Count | v1 Count | Delta | Notes |
|---|---|---|---|---|
| 🌟 A | 7 | 6 | +1 | Prathmesh-Ranadive promoted |
| 👍 B | 5 | 3 | +2 | chris-haun, Akale23, Vyankatesh95 promoted; luisalvatierra demoted |
| 👌 C | 7 | 5 | +2 | Rebalancing from B/D |
| 🟠 D | 6 | 6 | 0 | Stable |
| 🔴 E | 15 | 15 | 0 | Stable (budget crisis unchanged) |

---

## Key Findings: v2 vs v1

### 1. Limited Workflow Differentiation
With 100% "Used Agents" flag across all active users, the 2-tier adaptation cannot distinguish workflow types. In a 3-tier framework with actual Agent Contribution % data, we would see:
- **Agent-First users** (e.g., amol-salunkhe, Kranti-nice) evaluated primarily on LoC volume
- **Hybrid users** (e.g., mshnayderman, Prathmesh-Ranadive) balanced on both accept rate and efficiency
- **Inline-First users** (e.g., Vitthal-Nice) evaluated primarily on accept rate

Instead, everyone gets the "Used Agents" benchmark, which is **less strict on % Accept, more forgiving on LoC volume**.

### 2. Primary Beneficiaries of v2 Framework
Users who improved tier positions:
- **Prathmesh-Ranadive** (B → A): 86.9% accept + 27K LoC + Used Agents flag → Tier A despite ReqEff 2.5
- **chris-haun** (C → B): 10.4K LoC + 1,404 interactions → Volume + engagement compensate for 10.8% accept
- **Akale23** (C → B): Accept rate improved to 22.9%; agent workflow relaxes ReqEff requirement
- **Vyankatesh95** (C → B): 34.1% accept is strong signal; agent flag overlooks ReqEff collapse

### 3. Primary Losers
- **luisalvatierra** (B → C): Used Agents but ReqEff 1.7 is too low even with relaxed benchmarks. Nearly doubled LoC (4,800 → 9,477) but premium tripled.

### 4. Unchanged High Performers
- amol-salunkhe, Kranti-nice, mshnayderman, mfield1, rpawar-nice, Vitthal-Nice — All remain Tier A in both frameworks.

---

## Recommendation: Collect Agent Contribution % for Future Analyses

The 2-tier "Used Agents" flag provides minimal value when **100% of active users** have the flag set. To unlock the full value of v2 Workflow-Aware framework:

1. **Request GitHub to add Agent Contribution % to Power BI dashboard**, or
2. **Calculate it manually:** `Agent Contribution % = (LoC from agent sessions ÷ Total LoC Added) × 100`

With 3-tier classification:
- **Agent-First** (≥70%): Benchmark on LoC volume + ReqEff; ignore % Accept
- **Hybrid** (30-69%): Balance all three signals
- **Inline-First** (<30%): Benchmark heavily on % Accept

This would provide much sharper insight into **who is leveraging agent workflows effectively** vs. **who is mixing workflows** vs. **who remains inline-focused**.

---

*v2 Workflow-Aware — 2-Tier Adaptation due to missing Agent Contribution % column. 15 users excluded per ignore list. Framework maintains core principle of classify-first-then-benchmark, but with reduced granularity.*
