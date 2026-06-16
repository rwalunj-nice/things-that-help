# GitHub Copilot Multi-Period Analysis — v2 Workflow Progression
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Period:** April 20 → June 12, 2026 (53 days, 8 checkpoints)  
**Framework:** v2 Workflow-Aware (2-Tier Adaptation) | **Scope:** 45 users (15 excluded)

---

## Workflow Evolution Tracking

**Data Limitation:** No "Agent Contribution %" available. Only binary "# Users Used Agents" flag at each checkpoint.

### Workflow Distribution Across Checkpoints

| Checkpoint | Used Agents | Inline-Only | Agent Adoption Rate |
|---|---|---|---|
| CP1 (Apr 20) | — | — | (Data not available for CP1-CP6) |
| CP2 (Apr 23) | — | — | — |
| CP3 (Apr 28) | — | — | — |
| CP4 (May 11) | — | — | — |
| CP5 (May 18) | — | — | — |
| CP6 (Jun 3) | — | — | — |
| CP7 (Jun 8) | ~41 | ~0 | ~100% |
| **CP8 (Jun 12)** | **43** | **0** | **100%** |

**Key Finding:** At both CP7 and CP8, **100% of active users** have "# Users Used Agents = 1". This suggests:
1. **Universal agent adoption** across the WFM Integrations team
2. The 2-tier "Used Agents" vs "Inline-Only" classification provides **no workflow differentiation** in this dataset
3. v2 Workflow-Aware framework **minimal value-add** compared to v1 Standard for this team

---

## Workflow-Specific Pattern Analysis

Since all users show "Used Agents = 1", we cannot track workflow migration (Inline → Hybrid → Agent-First) over time. Instead, we infer workflow type from **behavioral signals**:

### Behavioral Workflow Inference (CP7 → CP8)

| Inferred Workflow | Count | % of Team | Behavioral Markers |
|---|---|---|---|
| **Agent-Heavy** | ~25 | ~58% | %Accept < 5%, LoC > 2,000, High Interactions |
| **Balanced/Hybrid** | ~10 | ~23% | %Accept 10-30%, Mixed LoC |
| **Inline-Focused** | ~8 | ~19% | %Accept > 30%, Lower Interactions |

**Key users by inferred workflow:**

**Agent-Heavy:**
- amol-salunkhe (1.5% accept, 41K LoC, 459 Int)
- Kranti-nice (1.2% accept, 31K LoC, 1,297 Int)
- mfield1 (6.0% accept, 9.8K LoC, 701 Int)
- abhishekhole-nice (0.0% accept, 2,993 LoC, 199 Int)

**Balanced/Hybrid:**
- mshnayderman (27.8% accept, 27K LoC, 164 Int)
- luisalvatierra (19.8% accept, 9.5K LoC, 617 Int)
- jayesh-rai (19.6% accept, 2.5K LoC, 140 Int)

**Inline-Focused:**
- Prathmesh-Ranadive (86.9% accept, 27K LoC, 83 Int)
- Vyankatesh95 (34.1% accept, 4.2K LoC, 423 Int)
- Vitthal-Nice (41.9% accept, 2.6K LoC, 158 Int)
- sgite-wfm (53.5% accept, 329 LoC, 54 Int)
- smishra-nice (78.3% accept, 155 LoC, 60 Int)

### Did Anyone Shift Workflows? (CP7 → CP8)

**Method:** Compare accept rates and interaction patterns between CP7 and CP8.

| User | CP7 %Accept | CP8 %Accept | CP7 Int | CP8 Int | Workflow Shift? |
|---|---|---|---|---|---|
| Prathmesh-Ranadive | 25.4% | 86.9% | ~100 | 83 | **Yes** — Shifted more inline-focused (accept rate tripled) |
| nilesht-19 | 29.5% | 30.0% | 1,140 | 1,218 | No — Stable inline-focused |
| luisalvatierra | ~17.6% | 19.8% | ~480 | 617 | Slight shift — More interactions, slightly higher accept |
| mshnayderman | 27.8% | 27.8% | 164 | 164 | No — Perfectly flat |

**Observation:** Most users show **stable workflow patterns** between CP7 and CP8 (4 days). **Prathmesh-Ranadive** is the only user with a clear workflow shift — accept rate tripled, suggesting more effective inline completion usage or different task types.

---

## Workflow-Specific Performance Trends

### Agent-Heavy Users: LoC Growth + Premium Spike Pattern

| User | CP7 LoC | CP8 LoC | Growth | CP7 Premium | CP8 Premium | Premium Growth |
|---|---|---|---|---|---|---|---|
| amol-salunkhe | 34,037 | 41,008 | +20.5% | 5,309 | 11,150 | +110% |
| Kranti-nice | 27,733 | 31,645 | +14.1% | ~1,200 | 11,979 | +898% |
| luisalvatierra | ~4,800 | 9,477 | +97.4% | ~1,655 | 5,608 | +239% |
| mfield1 | ~9,300 | 9,800 | +5.4% | ~650 | 1,813 | +179% |

**Pattern:** Agent-heavy users show **strong LoC growth** but **premium spikes disproportionate to LoC gain**. This is the core premium spike pattern documented in v1 analysis.

### Inline-Focused Users: Accept Rate Strength + Moderate Premium

| User | CP7 %Accept | CP8 %Accept | CP7 Premium | CP8 Premium | Premium Growth |
|---|---|---|---|---|---|---|
| Prathmesh-Ranadive | 25.4% | 86.9% | 10,733 | 10,851 | +1.1% |
| Vyankatesh95 | 34.1% | 34.1% | ~150 | 4,062 | +2,608% |
| Vitthal-Nice | ~44% | 41.9% | ~200 | 413 | +107% |

**Pattern:** Inline-focused users show **stable accept rates** but **still hit by premium spike pattern** (Vyankatesh95: 27× premium increase). Even inline-focused workflows are not immune to the systemic premium issue.

---

## v2 Tier Progression (CP7 → CP8)

### Tier Movement Summary

| User | CP7 v2 Tier | CP8 v2 Tier | Movement | Reason |
|---|---|---|---|---|
| Prathmesh-Ranadive | B | **A** | ⬆ Promoted | Accept rate tripled to 86.9%; agent flag bypasses low ReqEff |
| chris-haun | C | **B** | ⬆ Promoted | Agent workflow + 10.4K LoC compensates for 10.8% accept |
| Akale23 | C | **B** | ⬆ Promoted | Accept rate improved to 22.9% |
| Vyankatesh95 | C | **B** | ⬆ Promoted | 34.1% accept compensates for collapsed ReqEff |
| luisalvatierra | B | **C** | ⬇ Demoted | Premium spike (3.4×) despite strong LoC growth |

**Key insight:** v2 framework's **"Used Agents" flag relaxes efficiency requirements**, allowing users with strong LoC volume or improving accept rates to be promoted despite ReqEff issues. However, when premium spikes are **extreme** (like luisalvatierra's 3.4× increase), even v2's lenient benchmark cannot prevent demotion.

---

## Workflow-Aware Coaching Recommendations

### For Agent-Heavy Users
**Goal:** Maintain LoC growth while controlling premium spend.

- **amol-salunkhe**, **Kranti-nice** — Both show strong LoC output. If premium spike is platform-level (not behavior), these users are on correct trajectory. If behavioral, coach on:
  - Reducing prompt iterations per task
  - Using more efficient agent session patterns
  - Avoiding redundant generation requests

### For Balanced/Hybrid Users
**Goal:** Optimize the mix of inline and agent workflows.

- **mshnayderman** — Stable at 27.8% accept + 27K LoC. This is a strong balanced workflow. Premium spike (5,419) needs investigation but workflow pattern is optimal.
- **luisalvatierra** — Breakout LoC growth (+97%) is excellent. Premium tripled, but if output continues growing, efficiency will self-correct.

### For Inline-Focused Users
**Goal:** Maintain high accept rates; explore agent workflows for larger tasks.

- **Prathmesh-Ranadive** — Accept rate 86.9% is exceptional. This user has mastered inline completions. Consider: Does this user need agent workflows at all? Their current approach works.
- **Vitthal-Nice** — 41.9% accept with lean premium (413). Model user for inline-focused approach.
- **sgite-wfm**, **smishra-nice** — High accept rates but near-zero LoC. Likely using Copilot for code review/exploration, not generation. Acceptable for specific roles.

---

## Conclusion: v2 Framework Value for This Team

**Limited Differentiation:** With 100% agent adoption and no granular Agent Contribution % data, v2 Workflow-Aware provides **minimal tier changes** compared to v1 Standard:
- **v1 Standard:** 6 Tier A users
- **v2 Workflow-Aware:** 7 Tier A users (+1 user)
- **Net promotions:** 4 users moved up, 1 moved down

**Value Provided:**
- **Behavioral workflow inference** (Agent-Heavy, Balanced, Inline-Focused) adds context
- **Relaxed benchmarks for agent users** allows high-LoC producers to hold tier despite low accept rates
- **Framework signals "this is an agent-first team"** — validates that the team has adopted advanced Copilot features

**Recommendation:** To unlock full v2 value, **add Agent Contribution %** metric to Power BI. This would enable:
- **3-tier classification** (Agent-First ≥70%, Hybrid 30-69%, Inline-First <30%)
- **Precise coaching** based on actual agent vs. inline split
- **Workflow migration tracking** over time

---

*v2 Workflow-Aware Multi-Period Progression — Limited by binary "Used Agents" flag. Behavioral workflow inference used for analysis. 15 users excluded per ignore list.*
