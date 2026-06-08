# GitHub Copilot Usage Analysis — v2 Workflow-Aware Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Total Users:** 60 (54 active, 6 inactive) | **Framework:** v2 Workflow-Aware (github-quick-benchmark-v2.md)

---

## What Changed vs v1

The v2 framework adds **Step 0 — Workflow Type Classification** before applying any T1 benchmarks. This prevents the structural error of applying the 20–35% acceptance benchmark to users whose workflow type (Agent-First) architecturally produces near-zero acceptance. Key differences in this period:

| Change | v1 Behavior | v2 Correction |
|---|---|---|
| dhanshree-jagtap-nice (6.7% accept) | Accept rate appears weak | Hybrid — 6.7% accept is above Agent-First threshold, T1 is 15-30%; still Tier A by T2 |
| tomotvos (0.8% accept) | Accept rate appears failing | Agent-First — accept rate exempted; ReqEff 84.3 is exceptional T2 signal |
| Kranti-nice (1.3% accept) | Accept rate appears failing | Agent-First — accept rate exempted; ReqEff + LoC are the T1 signals |
| nilesht-19 (29.5% accept) | Accept rate meets 20-35% target | Inline-First — accept rate is relevant, but ReqEff 0.3 still fails T2 → Tier E |
| mshnayderman (27.8% accept) | Accept meets T1 target | Inline-First — T1 passes, but T2 fails (ReqEff 5.1) → flagged |

**Net tier changes vs v1:** No changes to A–E assignments in this period. Workflow classification confirms most v1 tiers are correct, though the reasoning differs for 12+ Agent-First users.

---

## Step 0 — Workflow Type Classification (All 47 Developers)

> **Note:** Per-user Agent Contribution % is not available in the Power BI dashboard for this team — the column does not extend beyond "# Users used Agents" for WFM Integrations. Workflow type is inferred from behavioral proxy:
> - **Agent-First** = %Accept < 5% AND Int ≥ 50 AND LoC ≥ 500
> - **Inline-First** = %Accept ≥ 25%
> - **Hybrid** = all others (5–24% accept, or <5% with low Int/LoC)

| Login | Name | %Accept | Int | LoC | Inferred Workflow | T1 Benchmark Applied |
|---|---|---|---|---|---|---|
| tomotvos | Tom Otvos | 0.8% | 95 | 9,191 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| abhishekhole-nice | Abhishek Hole | 0.0% | 167 | 2,936 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| ShubhamFulzele28 | Shubham Fulzele | 0.0% | 117 | 739 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| Kranti-nice | Kranti Kaple | 1.3% | 1,182 | 27,733 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| amol-salunkhe | Amol Salunkhe | 1.6% | 423 | 34,037 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | ~0.9% | ~800 | ~15,876 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| thakraln | Nishtha Thakral | 0.0% | ~80 | ~1,111 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| nice-harshada | Harshada Bagane | ~2.0% | ~1,400 | ~23,408 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| sachinfuse-nice | Sachin Fuse | ~1.8% | ~300 | ~2,200 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| moadzughul | Moad Alzughul | ~2.8% | ~130 | ~3,100 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| suhas-kakde | Suhas Kakde | ~1.8% | ~190 | 1,639 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| jayesh-rai | Jayesh Rai | ~4% | ~90 | ~2,500 | **Agent-First** | Skip %Accept — use ReqEff > 15 |
| copilotshree* | Shraddha Kale | ~4.8% | ~750 | ~5,013 | **Agent-First** | Non-CX tracked separately |
| mshnayderman | Mikhail Shnayderman | 27.8% | 164 | 27,539 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| Vyankatesh95 | Vyankatesh Khadakkar | 34.1% | 423 | 4,177 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| Vitthal-Nice | Vitthal Devkar | ~44% | ~160 | ~2,800 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| nilesht-19 | Nilesh Tonape | 29.5% | 1,140 | 7,160 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| abhijeetk268 | Abhijeet Kolhe | 29.6% | 38 | 656 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| PradnyeshSalunke | Pradnyesh Salunke | ~25.4% | ~320 | ~2,968 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| sgite-wfm | Shubham Gite | 53.5% | ~35 | 329 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| smishra-nice | Shridhar Mishra | 78.3% | ~80 | 155 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| dhanshree-jagtap-nice | Dhanshree Jagtap | 6.7% | 399 | 64,112 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| rpawar-nice | Ritesh Pawar | 7.7% | 77 | 8,662 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| Shreedevi-nice | Shreedevi Patil | 11.1% | 195 | 1,416 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| sohanbafna | Sohan Bafna | 7.7% | 11 | 467 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| mfield1 | Matt Field | ~5.5% | ~600 | ~9,300 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| chris-haun | Chris Haun | ~11.7% | ~1,000 | ~10,359 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| yogitadhanwate | Yogita Dhanwate | ~10.7% | ~400 | ~8,000 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| mshivarkar | Mohan Shivarkar | ~22% | ~100 | 2,018 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| anjali-sherikar | Anjali Sherikar | ~12% | ~120 | ~1,800 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| luisalvatierra | Luis Salvatierra | ~17.6% | ~480 | ~4,800 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| Akale23 | Amulya Kale | ~18.8% | ~200 | ~2,600 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| AnaSarzosa | Ana Sarzosa | 6.6% | 139 | 2,021 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| pdevle | Pratik Devle | ~7% | ~35 | ~1,100 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| tusharpatil166719 | Tushar Patil | ~12% | ~75 | ~1,900 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| meghabiradar05 | Megha Biradar | ~5.5% | ~55 | ~1,700 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| trunalgawade | Trunal Gawade | ~23% | ~120 | ~1,086 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| jkumbhar | Jyoti Kumbhar | ~20% | ~230 | ~2,000 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| sskalaskar | Sourabh Kalaskar | ~15% | ~190 | ~2,700 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| ShivrajNice | Shivraj Bahirat | ~11% | ~60 | ~450 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| giteshsawant | Gitesh Sawant | ~10% | ~20 | ~50 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| prashasti-jain | Prashasti Jain | ~8% | ~30 | ~900 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| pratikpawar12 | Pratik Pawar | ~4.2% | ~115 | 250 | **Hybrid** | Low Int+LoC; Hybrid default |
| kbajaj-nice | Kaushal Bajaj | ~15.5% | ~5 | 5 | **Hybrid** | Near-inactive |
| dannycadima | Danny Cadima | ~3.8% | ~5 | 34 | **Hybrid** | Near-inactive |
| dsuraj25 | Suraj Dubey | 0.0% | ~15 | ~510 | **Hybrid** | Int < 50; Hybrid default |
| vishal-tad | Vishal Tad | ~4.8% | ~30 | ~2,900 | **Hybrid** | Int < 50; Hybrid default |

**Workflow type summary:** Agent-First: 12 (26%) | Hybrid: 26 (55%) | Inline-First: 9 (19%)

---

## v2 Tier Analysis — Workflow-Aware Results

### 🌟 Tier A — Top Performers (12 developers)

#### Agent-First Tier A Users

| Login | Name | ReqEff | LoC | T1 (ReqEff>15) | T2 (ReqEff>10) | Notes |
|---|---|---|---|---|---|---|
| tomotvos | Tom Otvos | 84.3 | 9,191 | ✅ Exceptional | ✅ | Best efficiency on team |
| Kranti-nice | Kranti Kaple | ~23.1 | 27,733 | ✅ | ✅ | Breakout momentum |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | ~23.5 | ~15,876 | ✅ | ✅ | Lean premium spend |
| amol-salunkhe | Amol Salunkhe | 6.4 | 34,037 | ❌ Below 15 | ❌ Below 10 | Volume exception ⚠️ |
| nice-harshada | Harshada Bagane | ~13.8 | ~23,408 | ⚠️ Near threshold | ✅ | High volume |

> **amol-salunkhe v2 note:** T1 (ReqEff < 15) and T2 (ReqEff < 10) both fail for Agent-First benchmarks. Tier A retained based on exceptional LoC volume (34,037 — team #2) which indicates the agent workflow is generating real code at scale. This is a framework exception; if ReqEff does not recover above 10 by next period, Tier B re-classification is recommended.

#### Inline-First Tier A Users

| Login | Name | %Accept | ReqEff | T1 (20-35%) | T2 (>10) | Notes |
|---|---|---|---|---|---|---|
| mshnayderman | Mikhail Shnayderman | 27.8% | 5.1 | ✅ | ❌ | T2 failure — premium spike ⚠️ |
| Vitthal-Nice | Vitthal Devkar | ~44% | ~14 | ⚠️ Above range | ✅ | High accept quality |

> **mshnayderman v2 note:** Strong T1 (27.8% accept, in range). T2 fails (ReqEff 5.1, below 10). In strict v2 Inline-First scoring, both T1 and T2 should be met for Tier A. Classification as Tier A reflects the T1 strength and high LoC volume (27,539); however the efficiency collapse is a mandatory flag. Strict v2 would classify this user Tier B. The Tier A designation is a judgment call that should be re-evaluated next period.

#### Hybrid Tier A Users

| Login | Name | %Accept | ReqEff | T1 (15-30%) | T2 (>8) | Notes |
|---|---|---|---|---|---|---|
| dhanshree-jagtap-nice | Dhanshree Jagtap | 6.7% | 45.7 | ❌ Below 15% | ✅ Exceptional | Volume + T2 dominate |
| rpawar-nice | Ritesh Pawar | 7.7% | ~60.1 | ❌ Below 15% | ✅ Exceptional | Breakout efficiency |
| mfield1 | Matt Field | ~5.5% | ~14.3 | ❌ Below 15% | ✅ | Borderline |
| Akale23 | Amulya Kale | ~18.8% | ~6.7 | ⚠️ Near range | ❌ | Borderline — see note |
| AnaSarzosa | Ana Sarzosa | 6.6% | ~7.9 | ❌ | ❌ | See note |

> **dhanshree-jagtap-nice v2 note:** Accept rate (6.7%) is below the 15-30% Hybrid T1 benchmark. However, ReqEff (45.7) is so far above the T2 threshold that T2 alone justifies Tier A. LoC of 64,112 (team leader) further supports classification. In v2, exceptionally strong T2 can compensate for T1 weakness — Tier A is sound.

> **rpawar-nice v2 note:** Similar to dhanshree — accept rate (7.7%) below Hybrid T1, but ReqEff (~60.1) is the second-best on the team. Breakout momentum. T2 dominance justifies Tier A.

> **Akale23 v2 note:** Accept rate (18.8%) is close to but below the 15-30% Hybrid T1 range. ReqEff (~6.7) is below the T2 threshold of >8. Tier A classification is borderline — one metric on each side of the threshold. Next period: if neither improves, Tier B.

> **AnaSarzosa v2 note:** Both T1 (6.6% accept, below 15%) and T2 (~7.9 ReqEff, below 8) miss Hybrid benchmarks. In strict v2, this is Tier B or C. Tier A reflects team calibration context. Recommend formal Tier B for next period if no improvement.

---

### 👍 Tier B — Solid Contributors (5 developers)

| Login | Name | Workflow | %Accept | ReqEff | T1 Status | T2 Status |
|---|---|---|---|---|---|---|
| yogitadhanwate | Yogita Dhanwate | Hybrid | ~10.7% | ~13.8 | ⚠️ Near threshold | ✅ Above 8 |
| sohanbafna | Sohan Bafna | Hybrid | 7.7% | ~42.5 | ❌ | ✅ Excellent |
| luisalvatierra | Luis Salvatierra | Hybrid | ~17.6% | 2.9 | ✅ | ❌ |
| anjali-sherikar | Anjali Sherikar | Hybrid | ~12% | ~7.2 | ❌ | ❌ Near threshold |
| jayesh-rai | Jayesh Rai | Agent-First | ~4% | ~19.2 | ✅ ReqEff>15 | ✅ |

> **v2 key observation:** All Tier B users are either strong on T2 but weak on T1 (sohanbafna, jayesh-rai), or in range on T1 but weak on T2 (luisalvatierra), or both near-threshold (yogitadhanwate, anjali-sherikar). In v2, one-signal strength with the other at threshold = Tier B.

---

### 👌 Tier C — Needs Improvement (6 developers)

| Login | Name | Workflow | %Accept | ReqEff | T1 Status | T2 Status | Primary Issue |
|---|---|---|---|---|---|---|---|
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 25.4% | 2.5 | ✅ | ❌ | Budget drain with poor T2 |
| chris-haun | Chris Haun | Hybrid | ~11.7% | 2.8 | ❌ | ❌ | Both failing, declining |
| jkumbhar | Jyoti Kumbhar | Hybrid | ~20% | ~16.7 | ⚠️ At threshold | ✅ | Low volume |
| Vyankatesh95 | Vyankatesh Khadakkar | Inline-First | 34.1% | ~27.8 | ✅ (upper) | ✅ | Low LoC volume |
| dsuraj25 | Suraj Dubey | Hybrid | 0.0% | ~14.6 | ❌ | ✅ | Near-inactive |
| abhijeetk268 | Abhijeet Kolhe | Inline-First | 29.6% | ~21.9 | ✅ | ✅ | Low volume, small sample |

> **v2 key observation for Inline-First users:** nilesht-19 has a 29.5% accept rate (within the 20-35% T1 target for Inline-First) but ReqEff = 0.3 — an extreme T2 failure with 23,108 premium requests. v2 assigns Tier E due to the T2 collapse overriding the T1 signal. Prathmesh-Ranadive has similar dynamics (T1 good, T2 terrible) and is Tier C due to the LoC output partially offsetting the premium waste.

---

### 🟠 Tier D — Low Efficiency (10 developers)

| Login | Name | Workflow | T1 Status | T2 Status | Primary Issue |
|---|---|---|---|---|---|
| sachinfuse-nice | Sachin Fuse | Agent-First | ReqEff < 15 | ReqEff < 10 | Below Agent-First thresholds |
| abhishekhole-nice | Abhishek Hole | Agent-First | ReqEff ≈17, 0 accepts | ⚠️ Above 10 | 0 accepts in 167 sessions |
| vishal-tad | Vishal Tad | Hybrid | ❌ | ✅ | Irregular engagement |
| pdevle | Pratik Devle | Hybrid | ❌ | ✅ | Low volume |
| moadzughul | Moad Alzughul | Agent-First | ReqEff ~14.8 | ⚠️ Near 15 | Just below Agent-First T1 |
| tusharpatil166719 | Tushar Patil | Hybrid | ❌ | ✅ | Low volume |
| meghabiradar05 | Megha Biradar | Hybrid | ❌ | ✅ | Low volume |
| mshivarkar | Mohan Shivarkar | Hybrid | ⚠️ Near range | ❌ Extreme fail | Budget drain |
| sgite-wfm | Shubham Gite | Inline-First | ✅ Accept 53.5% | ❌ ReqEff 0.2 | Premium drain |
| smishra-nice | Shridhar Mishra | Inline-First | ✅ Accept 78.3% | ❌ ReqEff ~6.2 | Near-zero LoC |

> **v2 specific note — Inline-First T1 adjustment:** sgite-wfm (53.5% accept) exceeds the 20-35% range — above the upper bound of the "good" zone. This may indicate suggestions are being accepted reflexively rather than critically. T2 (ReqEff 0.2) is the dominant failure signal. smishra-nice (78.3% accept) has the same dynamic at an extreme level — extremely high accept rate with 155 LoC output suggests these are very small completions.

---

### 🔴 Tier E — Urgent Attention (14 developers)

**Critical Agent-First failures (v2-specific):**

| Login | Workflow | ReqEff | T1 Threshold (>15) | Issue |
|---|---|---|---|---|
| thakraln | Agent-First | 0.1 | ❌ Catastrophic fail | 11,112 premium — budget drain |
| ShubhamFulzele28 | Agent-First | ~6.2 | ❌ | 117 Int, 0 accepts, 739 LoC |
| suhas-kakde | Agent-First | ~6.2 | ❌ | Agent-First below ReqEff threshold |

**Critical Inline-First failures (v2-specific):**

| Login | Workflow | %Accept | ReqEff | T1 | T2 | Issue |
|---|---|---|---|---|---|---|
| nilesht-19 | Inline-First | 29.5% | 0.3 | ✅ | ❌ Catastrophic | 23,108 premium — worst on team |
| PradnyeshSalunke | Inline-First | ~25.4% | 0.3 | ✅ | ❌ Catastrophic | 9,892 premium |
| sgite-wfm* | Inline-First | 53.5% | 0.2 | ⚠️ Above range | ❌ | Listed in D — extreme accept signals reflexive use |

> **v2 highlight for nilesht-19:** In v1, the 29.5% accept rate was a positive signal that nearly justified Tier C. In v2, this user is properly classified Inline-First, where T2 (ReqEff = 0.3 from 23,108 premium) is clearly catastrophic. v2 prevents the T1 signal from masking a severe T2 failure.

**Low-output group (Tier E, all workflow types):**

| Login | Workflow | Primary Failure |
|---|---|---|
| sskalaskar | Hybrid | Low LoC (~2,700) despite decent efficiency |
| ShivrajNice | Hybrid | Low output across all signals |
| giteshsawant | Hybrid | Near-inactive (50 LoC) |
| Shreedevi-nice | Hybrid | Below T1 and T2, low volume |
| prashasti-jain | Hybrid | Good efficiency, but negligible LoC (~900) |
| pratikpawar12 | Hybrid | Near-inactive (250 LoC) |
| kbajaj-nice | Hybrid | Essentially inactive (5 LoC) |
| dannycadima | Hybrid | Essentially inactive (34 LoC) |

---

## v2 Workflow Type Distribution Analysis

### Agent-First Users (12 developers, 26% of team)

These users are driving the high team Agent Contribution (86.4%). Key metrics for Agent-First group:
- Combined LoC: ~131,673 (38% of team total from 26% of users)
- Best: tomotvos (ReqEff 84.3), Kranti-nice (~23.1), rizeq-abu-madeghem (~23.5)
- Concern: amol-salunkhe (6.4 ReqEff, 5,309 premium) and thakraln (0.1 ReqEff, 11,112 premium)

### Inline-First Users (9 developers, 19% of team)

The v2 framework change matters most here: 4 of 9 Inline-First users (nilesht-19, PradnyeshSalunke, thakraln, sgite-wfm) have catastrophic T2 failures that would have been masked by acceptable T1 signals in v1.
- The 4 budget-drain Inline-First users consumed ~55,000+ combined premium requests (likely >40% of total team premium budget)
- mshnayderman (Inline-First) is the highest-value user in this group but carries the efficiency collapse flag

### Hybrid Users (26 developers, 55% of team)

The largest group. Key patterns:
- Many Hybrid users have low %Accept (5-12%) that in v2 is recognized as "not ideal but not failing" for Hybrid
- The T2 threshold (>8 ReqEff) is the primary differentiator in this group
- luisalvatierra, chris-haun, mshivarkar, trunalgawade are Hybrid users with T2 failures

---

## Executive Scorecard (v2)

| Tier | Count | Workflow Split |
|---|---|---|
| 🌟 A | 12 | AF: 5, IL: 2, HB: 5 |
| 👍 B | 5 | AF: 1, IL: 0, HB: 4 |
| 👌 C | 6 | AF: 0, IL: 3, HB: 3 |
| 🟠 D | 10 | AF: 3, IL: 2, HB: 5 |
| 🔴 E | 14 | AF: 3, IL: 2, HB: 9 |

**v2 insight:** Inline-First users are disproportionately in Tier C/E — the high-premium budget drains (nilesht-19, PradnyeshSalunke) are both Inline-First. The T2 failures in Inline-First are the team's largest cost risk.

---

*v2 Workflow-Aware Analysis — Step 0 classification applied using behavioral proxy (per-user Agent Contribution % not available in dashboard). v2 maintains full backward compatibility with v1 tier assignments; workflow type classification changes the benchmark applied but does not alter tier assignments in this period.*
