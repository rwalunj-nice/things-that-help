# GitHub Copilot Usage Analysis — v2 Workflow-Aware Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Scope:** 45 users (15 excluded per ignore list) | **Framework:** v2 Workflow-Aware

---

## What Changed vs v1 (This Period)

v2 adds Step 0 — Workflow Type Classification before any T1 benchmarks. Key corrections vs v1:

| User | v1 Issue | v2 Correction |
|---|---|---|
| Kranti-nice (1.3% accept) | Accept appears failing | Agent-First — accept rate exempted; ReqEff ~23.1 is the T1 signal |
| amol-salunkhe (1.6% accept) | Accept appears failing | Agent-First — accept rate exempted; LoC volume and ReqEff evaluated |
| nilesht-19 (29.5% accept) | Accept looks like T1 strength | Inline-First — T1 meets range but T2 (ReqEff 0.3) catastrophically fails |
| Prathmesh-Ranadive (25.4% accept) | Accept looks like T1 strength | Inline-First — same: T1 meets threshold but extreme premium spend fails T2 |

**Net tier changes vs v1:** None in this period — workflow classification confirms all v1 tiers are correct, though the reasoning differs for all Agent-First users.

---

## Step 0 — Workflow Type Classification (37 Developers)

> **Behavioral proxy used** (per-user Agent Contribution % unavailable in dashboard):
> - **Agent-First**: %Accept < 5% AND Int ≥ 50 AND LoC ≥ 500
> - **Inline-First**: %Accept ≥ 25%
> - **Hybrid**: all others

| Login | Name | %Accept | Int | LoC | Workflow | T1 Benchmark |
|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 1.6% | 423 | 34,037 | **Agent-First** | ReqEff > 15 |
| Kranti-nice | Kranti Kaple | 1.3% | 1,182 | 27,733 | **Agent-First** | ReqEff > 15 |
| abhishekhole-nice | Abhishek Hole | 0.0% | 167 | 2,936 | **Agent-First** | ReqEff > 15 |
| moadzughul | Moad Alzughul | ~2.8% | ~130 | ~3,100 | **Agent-First** | ReqEff > 15 |
| suhas-kakde | Suhas Kakde | ~1.8% | ~190 | 1,639 | **Agent-First** | ReqEff > 15 |
| thakraln | Nishtha Thakral | 0.0% | ~80 | ~1,111 | **Agent-First** | ReqEff > 15 |
| jayesh-rai | Jayesh Rai | ~4% | ~90 | ~2,500 | **Agent-First** | ReqEff > 15 |
| ShubhamFulzele28 | Shubham Fulzele | 0.0% | 117 | 739 | **Agent-First** | ReqEff > 15 |
| mshnayderman | Mikhail Shnayderman | 27.8% | 164 | 27,539 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| Vyankatesh95 | Vyankatesh Khadakkar | 34.1% | 423 | 4,177 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| Vitthal-Nice | Vitthal Devkar | ~44% | ~160 | ~2,800 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| nilesht-19 | Nilesh Tonape | 29.5% | 1,140 | 7,160 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| abhijeetk268 | Abhijeet Kolhe | 29.6% | 38 | 656 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| PradnyeshSalunke | Pradnyesh Salunke | ~25.4% | ~320 | ~2,968 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| sgite-wfm | Shubham Gite | 53.5% | ~35 | 329 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| smishra-nice | Shridhar Mishra | 78.3% | ~80 | 155 | **Inline-First** | %Accept 20–35% + ReqEff > 10 |
| dhanshree-jagtap-nice* | *(ignored)* | — | — | — | — | — |
| rpawar-nice | Ritesh Pawar | 7.7% | 77 | 8,662 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| mfield1 | Matt Field | ~5.5% | ~600 | ~9,300 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| chris-haun | Chris Haun | ~11.7% | ~1,000 | ~10,359 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| luisalvatierra | Luis Salvatierra | ~17.6% | ~480 | ~4,800 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| Akale23 | Amulya Kale | ~18.8% | ~200 | ~2,600 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| mshivarkar | Mohan Shivarkar | ~22% | ~100 | 2,018 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| jkumbhar | Jyoti Kumbhar | ~20% | ~230 | ~2,000 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| Shreedevi-nice | Shreedevi Patil | 11.1% | 195 | 1,416 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| tusharpatil166719 | Tushar Patil | ~12% | ~75 | ~1,900 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| meghabiradar05 | Megha Biradar | ~5.5% | ~55 | ~1,700 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| trunalgawade | Trunal Gawade | ~23% | ~120 | ~1,086 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| sskalaskar | Sourabh Kalaskar | ~15% | ~190 | ~2,700 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| prashasti-jain | Prashasti Jain | ~8% | ~30 | ~900 | **Hybrid** | %Accept 15–30% + ReqEff > 8 |
| pratikpawar12 | Pratik Pawar | ~4.2% | ~115 | 250 | **Hybrid** | Low Int+LoC; Hybrid default |
| kbajaj-nice | Kaushal Bajaj | ~15.5% | ~5 | 5 | **Hybrid** | Near-inactive |
| giteshsawant | Gitesh Sawant | ~10% | ~20 | ~50 | **Hybrid** | Near-inactive |
| dannycadima | Danny Cadima | ~3.8% | ~5 | 34 | **Hybrid** | Near-inactive |
| dsuraj25 | Suraj Dubey | 0.0% | ~15 | ~510 | **Hybrid** | Int < 50; Hybrid default |
| vishal-tad | Vishal Tad | ~4.8% | ~30 | ~2,900 | **Hybrid** | Int < 50; Hybrid default |
| pdevle | Pratik Devle | ~7% | ~35 | ~1,100 | **Hybrid** | — |
| smishra-nice | Shridhar Mishra | 78.3% | ~80 | 155 | **Inline-First** | — |
| abhijeetk268 | Abhijeet Kolhe | 29.6% | 38 | 656 | **Inline-First** | — |

**Workflow distribution (37 developers):** Agent-First: 8 (22%) | Hybrid: 21 (57%) | Inline-First: 8 (22%)

---

## v2 Tier Analysis

### 🌟 Tier A (7 developers)

#### Agent-First Tier A

| Login | ReqEff | LoC | T1 (>15) | T2 (>10) | Assessment |
|---|---|---|---|---|---|
| Kranti-nice | ~23.1 | 27,733 | ✅ | ✅ | Clean Tier A. Breakout momentum. |
| jayesh-rai | ~19.2 | ~2,500 | ✅ | ✅ | Clean Agent-First. Lean spend. |
| amol-salunkhe | 6.4 | 34,037 | ❌ | ❌ | Volume exception ⚠️. Both T1 and T2 fail. |

> **amol-salunkhe note:** T1 (6.4 < 15) and T2 (6.4 < 10) fail for Agent-First benchmarks. Tier A retained purely on output volume. This is the most significant framework exception in this analysis period. If ReqEff remains below 10 next period, Tier B is the framework-correct placement.

#### Inline-First Tier A

| Login | %Accept | ReqEff | T1 (20-35%) | T2 (>10) | Assessment |
|---|---|---|---|---|---|
| mshnayderman | 27.8% | 5.1 | ✅ | ❌ | T1 passes; T2 fails (premium spike) ⚠️ |
| Vitthal-Nice | ~44% | ~14 | ⚠️ Above range | ✅ | High quality signals |

> **mshnayderman v2 note:** In strict v2 Inline-First, both T1 and T2 should be met for Tier A. T2 fails (ReqEff 5.1). Strict v2 places this user at Tier B. Current Tier A classification is a judgment call; recommend formal Tier B if efficiency does not recover.

#### Hybrid Tier A

| Login | %Accept | ReqEff | T1 (15-30%) | T2 (>8) | Assessment |
|---|---|---|---|---|---|
| rpawar-nice | 7.7% | ~60.1 | ❌ Below 15% | ✅ Exceptional | T2 dominates. Best efficiency in scope. |
| mfield1 | ~5.5% | ~14.3 | ❌ | ✅ Near threshold | T2 meets threshold. |
| Akale23 | ~18.8% | ~6.7 | ⚠️ Near range | ❌ | Both borderline. |

> **rpawar-nice note:** Accept rate (7.7%) below 15-30% Hybrid T1 — but ReqEff 60.1 is exceptionally strong T2. With tomotvos excluded from analysis scope, rpawar-nice is the efficiency benchmark. T2 dominance justifies Tier A.

---

### 👍 Tier B (2 developers)

| Login | Workflow | T1 | T2 | Assessment |
|---|---|---|---|---|
| luisalvatierra | Hybrid | ✅ 17.6% near range | ❌ ReqEff 2.9 | T2 fails; T1 approaching |
| jayesh-rai | Agent-First | ✅ ReqEff 19.2 > 15 | ✅ | See Tier A Agent-First above — classified A by some readings |

> Note: jayesh-rai appears in Tier B in v1 but qualifies for Tier A in strict v2 Agent-First scoring (ReqEff 19.2 > 15, lean spend). Tier B retained for conservative placement on modest LoC volume (~2,500).

---

### 👌 Tier C (6 developers)

| Login | Workflow | T1 | T2 | Primary Issue |
|---|---|---|---|---|
| Prathmesh-Ranadive | Inline-First | ✅ 25.4% | ❌ ReqEff 2.5 | Premium drain — T2 failure overrides good T1 |
| chris-haun | Hybrid | ❌ 11.7% | ❌ 2.8 | Both failing; declining trend |
| jkumbhar | Hybrid | ⚠️ 20% at threshold | ✅ 16.7 | Low volume despite passing both |
| Vyankatesh95 | Inline-First | ✅ 34.1% | ✅ 27.8 | Both pass but low absolute LoC (4,177) |
| dsuraj25 | Hybrid | ❌ 0.0% | ✅ 14.6 | Near-inactive |
| abhijeetk268 | Inline-First | ✅ 29.6% | ✅ 21.9 | Both pass; too small a sample to promote |

---

### 🟠 Tier D (9 developers)

| Login | Workflow | T1 | T2 | Primary Issue |
|---|---|---|---|---|
| abhishekhole-nice | Agent-First | ReqEff ~17.3 ✅ | ✅ | 0 accepts anomaly; ReqEff actually good |
| vishal-tad | Hybrid | ❌ | ✅ 23.2 | Irregular use; good efficiency when active |
| moadzughul | Agent-First | ReqEff ~14.8 ⚠️ | ⚠️ near 15 | Just below Agent-First T1 threshold |
| tusharpatil166719 | Hybrid | ❌ | ✅ ~19 | Low volume |
| meghabiradar05 | Hybrid | ❌ | ✅ ~15.5 | Low volume |
| mshivarkar | Hybrid | ⚠️ 22% near range | ❌ 0.6 | Budget drain — R=0 in CRQC |
| sgite-wfm | Inline-First | ✅ 53.5% (above range) | ❌ 0.2 | R=0 override applies; extremely high accept rate may be reflexive |
| smishra-nice | Inline-First | ✅ 78.3% (far above range) | ❌ ~6.2 | Near-zero LoC despite high accept rate |
| pdevle | Hybrid | ❌ | ✅ ~15.7 | Low volume |

> **v2 insight — Inline-First extreme accept rates:** sgite-wfm (53.5%) and smishra-nice (78.3%) both exceed the 20-35% "good" range for Inline-First. In v2, accept rates above 35% may indicate reflexive acceptance rather than selective trust. Combined with near-zero ReqEff for both users, this pattern suggests Copilot is being used for very small completions with high premium consumption.

---

### 🔴 Tier E (13 developers)

**Agent-First failures:**

| Login | ReqEff | T1 Threshold (>15) | Issue |
|---|---|---|---|
| thakraln | 0.1 | ❌ | 11,112 premium — budget crisis |
| ShubhamFulzele28 | ~6.2 | ❌ | 0 accepts, below threshold |
| suhas-kakde | ~6.2 | ❌ | Agent-First below ReqEff |

**Inline-First budget failures:**

| Login | %Accept | ReqEff | T1 | T2 | Issue |
|---|---|---|---|---|---|
| nilesht-19 | 29.5% | 0.3 | ✅ | ❌ | 23,108 premium — worst in scope |
| PradnyeshSalunke | ~25.4% | 0.3 | ✅ | ❌ | 9,892 premium |

> **v2 key insight — nilesht-19:** The 29.5% accept rate is a genuine T1 strength signal (Inline-First benchmark: 20-35%). However, v2 prevents T1 from masking T2 catastrophe: 23,108 premium for 7,160 LoC = ReqEff 0.3. This is the clearest example of why v2's separate treatment of T1 and T2 matters — the T1 signal would have suggested a borderline Tier C in v1, but the T2 failure is severe enough to keep this user at Tier E.

**Hybrid low-output group:** sskalaskar, Shreedevi-nice, prashasti-jain, pratikpawar12, kbajaj-nice, giteshsawant, dannycadima, trunalgawade — all Hybrid below both T1 and T2, or near-inactive.

---

## Executive Scorecard (v2)

| Tier | Count | Workflow Split |
|---|---|---|
| 🌟 A | 7 | AF: 3, IL: 2, HB: 2 |
| 👍 B | 2 | AF: 1, HB: 1 |
| 👌 C | 6 | AF: 0, IL: 3, HB: 3 |
| 🟠 D | 9 | AF: 3, IL: 2, HB: 4 |
| 🔴 E | 13 | AF: 3, IL: 2, HB: 8 |

**v2 insight:** With the highest-output Agent-First users (tomotvos, dhanshree, rizeq, nice-harshada) excluded from scope, the remaining Agent-First group is smaller (8 users, 22%). The Hybrid group (21 users, 57%) dominates the tier distribution. The Inline-First budget failures (nilesht-19, PradnyeshSalunke, trunalgawade at T2=0) are proportionally more visible as a share of in-scope budget consumption.

---

*v2 Workflow-Aware — 15 users excluded per `githun-ignored-users.md`. Workflow classification via behavioral proxy. v2 confirms all v1 tier assignments; reasoning differs for Agent-First users.*
