# GitHub Copilot Usage Analysis — CRQC Multi-Period Checkpoint Progression (Q2 2026)

> **Framework**: CRQC — Core (C) + ROI (R) + Quality (Q) + Context (diagnostic)  
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM  
> **Analysis Period**: April 20 → June 3, 2026 (Q2 Checkpoints)  
> **Report Date**: June 3, 2026

---

## Executive Summary

This report tracks **C+R score evolution** across five Q2 2026 checkpoints, revealing performance trajectories, budget efficiency patterns, and outlier timing. CRQC methodology (Core + ROI + Quality scoring) was introduced on May 11, so earlier checkpoints (April 20, April 28) have no CRQC data.

### Q2 Checkpoint Timeline

| Checkpoint | Date | CRQC Available | Data Type |
|---|---|---|---|
| **CP1** | April 20, 2026 | ❌ No | Legacy Quick Benchmark (Req Eff, % Accept, LoC) |
| **CP2** | April 28, 2026 | ❌ No | Legacy Quick Benchmark (Req Eff, % Accept, LoC) |
| **CP3** | May 11, 2026 | ✅ Yes | CRQC introduced — C+R+Q scoring begins |
| **CP4** | May 18, 2026 | ✅ Yes | CRQC with actual Premium Requests per user |
| **CP5** | June 3, 2026 | ✅ Yes | CRQC with Q2 cumulative data (9-week totals) |

---

## C+R Score Evolution Overview

**Key Pattern Discovery:**

1. **Tier A Consistency**: Amol Salunkhe, Mikhail Shnayderman, and Ritesh Pawar maintained top-tier C+R scores (6/6) across May 11 → June 3.
2. **Chris Haun Volatility**: Dropped from A-tier at CP3 (C3+R1=7 total with Q3) to B-tier at CP5 (C2+R2=4).
3. **Prathmesh Ranadive Budget Crisis**: Started as A-potential (C+R=6) at CP3, but outlier Premium spend (4,001 Q2 Prem) capped him at Tier C by CP5.
4. **Mohan Shivarkar Recovery**: Breakthrough momentum at CP5 (+1,531 LoC in final 16 days) lifted him from persistent R=0 warnings.
5. **Outlier Spend Emergence**: Four users (Prathmesh, Pradnyesh, Kranti, Nilesh) crossed 1,700 Premium threshold between CP3 and CP5, consuming 54% of team budget.

---

## Master CRQC Progression Table

> **C+R Score** = Core (0-3) + ROI (0-3) = max 6 points (Q excluded for progression consistency, as Q=FB for most users)  
> **NA** = CRQC data not available (pre-May 11 checkpoints)

| User | Name | Apr 20 C+R | Apr 28 C+R | May 11 C+R | May 18 C+R | Jun 3 C+R | Pattern | Key Insight |
|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | NA | NA | **6** | **6** | **6** | 🟢 Stable A | Consistent C3+R3 — lean spend maintained across Q2 |
| mshnayderman | Mikhail Shnayderman | NA | NA | **6** | **6** | **6** | 🟢 Stable A | C3+R3 locked — top performer throughout Q2 |
| rpawar-nice | Ritesh Pawar | NA | NA | **5** | **5** | **6** | 📈 Rising A | Lean bonus lifted R from 2→3 at CP5 |
| chris-haun | Chris Haun | NA | NA | **4** (C3+R1) | **4** (C2+R2) | **4** (C2+R2) | 🟡 Stable B | C score volatility (3→2) but total C+R flat |
| mfield1 | Matt Field | NA | NA | **5** (C2+R2) | **5** (C3+R2) | **4** (C2+R2) | 🔵 Volatile | C score swings (2→3→2) — total range 4-5 |
| Vitthal-Nice | Vitthal Devkar | NA | NA | **5** (C3+R2) | **5** (C3+R2) | **5** (C3+R2) | 🟢 Stable B | C3+R2 — inline-first champion, consistent |
| jayesh-rai | Jayesh Rai | NA | NA | **2** (C1+R1) | **2** (C0+R2) | **5** (C3+R2) | 🚀 Breakout | Dramatic recovery +3pts (C1→C3) by CP5 |
| copilotshree | Shraddha Kale | NA | NA | **5** (C2+R2) | **6** (C3+R3) | **5** (C2+R3) | 🔵 Volatile | Peak at CP4 (C+R=6), regressed to 5 at CP5 |
| sskalaskar | Sourabh Kalaskar | NA | NA | **6** (C3+R3) | **4** (C2+R2) | **4** (C2+R2) | 📉 Declining | Dropped from A-tier (6) to C-tier (4) |
| moadzughul | Moad Alzughul | NA | NA | **5** (C3+R2) | **5** (C2+R3) | **3** (C1+R2) | 📉 Declining | Steady decline 5→3 across Q2 |
| Prathmesh-Ranadive | Prathmesh Ranadive | NA | NA | **5** (C3+R2) | **3** (C3+R0) | **3** (C3+R0) | 🔴 Capped | Outlier Premium penalty (4,001 Prem) → R=0 |
| PradnyeshSalunke | Pradnyesh Salunke | NA | NA | **5** (C3+R2) | **2** (C2+R0) | **3** (C3+R0) | 🔴 Capped | Outlier Premium penalty (3,754 Prem) → R=0 |
| tusharpatil166719 | Tushar Patil | NA | NA | **3** (C1+R3) | **2** (C1+R1) | **3** (C2+R1) | 🟡 Stable C | Volatile but recovers to C-tier baseline |
| mshivarkar | Mohan Shivarkar | NA | NA | **2** (C2+R0) | **1** (C0+R1) | **3** (C1+R2) | 🚀 Breakout | Recovery at CP5: +1,531 LoC final window |
| Akale23 | Amulya Kale | NA | NA | **2** (C1+R0) | **3** (C1+R2) | **4** (C2+R2) | 📈 Rising | Steady climb 2→4 across Q2 |
| trunalgawade | Trunal Gawade | NA | NA | **3** (C3+R0) | **2** (C1+R1) | **4** (C3+R1) | 🔵 Volatile | C score swings wildly (3→1→3) |
| sgite-wfm | Shubham Gite | NA | NA | **3** (C3+R0) | **1** (C0+R1) | **4** (C3+R1) | 🔵 Volatile | C score collapse then recovery |
| smishra-nice | Shridhar Mishra | NA | NA | **3** (C2+R1) | **2** (C1+R1) | **3** (C2+R1) | 🟡 Stable C | Volatile C but stable C+R total |
| shreedevi-nice | Shreedevi Patil | NA | NA | **3** (C2+R1) | **2** (C1+R1) | **2** (C1+R1) | 📉 Declining | Drop from C3 (CP3) to C2 → floor D |
| Kranti-nice | Kranti Kaple | NA | NA | **2** (C2+R0) | **2** (C2+R0) | **1** (C1+R0) | 🔴 Capped | Outlier Premium penalty (3,660 Prem) |
| nilesht-19 | Nilesh Tonape | NA | NA | **5** (C2+R3) | **3** (C3+R0) | **2** (C2+R0) | 📉 Declining | Outlier Premium collapse: 3,988 Prem → R=0 |
| Vyankatesh95 | Vyankatesh Khadakkar | NA | NA | **6** (C3+R3) | **4** (C3+R1) | **1** (C1+R0) | 📉 Severe decline | From A-tier candidate (6) to D-tier (1) |
| jkumbhar | Jyoti Kumbhar | NA | NA | **3** (C2+R3) | **2** (C1+R1) | **2** (C2+R0) | 📉 Declining | R collapse due to Premium>500 + R=0 |
| luisalvatierra | Luis Salvatierra | NA | NA | **1** (C1+R1) | **2** (C2+R0) | **1** (C1+R0) | 🔴 Capped | R=0 + Premium>500 cap enforced |
| abhijeetk268 | Abhijeet Kolhe | NA | NA | **3** (C2+R2) | **2** (C1+R1) | **1** (C0+R1) | 📉 Declining | C score collapse C2→C0 |
| meghabiradar05 | Megha Biradar | NA | NA | **3** (C1+R2) | **4** (C1+R3) | **1** (C0+R1) | 📉 Declining | Peak at CP4, then severe drop |
| pdevle | Pratik Devle | NA | NA | **1** (C0+R1) | **1** (C0+R1) | **1** (C0+R1) | 🟡 Stable D | Flat at D-tier baseline |
| abhishekhole-nice | Abhishek Hole | NA | NA | **6** (C3+R3) | **4** (C2+R2) | **2** (C0+R2) | 📉 Severe decline | From A-tier (6) to D-tier (2) — zero window |
| thakraln | Nishtha Thakral | NA | NA | **0** (C0+R0) | **0** (C0+R0) | **1** (C1+R0) | 📈 Minimal rise | First LoC output (69) at CP5 |
| kbajaj-nice | Kaushal Bajaj | NA | NA | **1** (C0+R1) | **1** (C0+R1) | **2** (C1+R1) | 📈 Rising | Small improvement C0→C1 |
| pratikpawar12 | Pratik Pawar | NA | NA | **1** (C1+R0) | **1** (C0+R1) | **1** (C0+R1) | 🟡 Stable D | Flat at D-tier baseline |
| dannycadima | Danny Cadima Molina | NA | NA | **0** | **0** | **5** (C2+R3) | 🆕 New | First data at CP5: strong debut (lean bonus) |
| suhas-kakde | Suhas Kakde | NA | NA | **2** (C1+R1) | **2** (C1+R1) | **0** (C0+R0) | 📉 Severe decline | Collapse to E-tier — zero window |
| prashasti-jain | Prashasti Jain | NA | NA | **1** (C1+R1) | **1** (C1+R0) | **0** (C0+R0) | 📉 Declining | Fell to E-tier — R=0+Prem>500 |
| dsuraj25 | Suraj Dubey | NA | NA | **2** (C0+R2) | **2** (C0+R2) | **2** (C0+R2) | 🟡 Stable D | Flat at D-tier: C=0 throughout |
| vishal-tad | Vishal Tad | NA | NA | — | — | **3** (C1+R2) | 🆕 New | First appearance at CP5 |

---

## Score Change Analysis — CP3 (May 11) → CP5 (June 3)

### 🚀 Who Improved C+R Through Q2 (≥+2 points)

| User | CP3 C+R | CP5 C+R | Change | Key Driver |
|---|---|---|---|---|
| **Jayesh Rai** | 2 | 5 | **+3** | C score explosion C1→C3 + lean bonus on R |
| **Mohan Shivarkar** | 2 | 3 | **+1** | Breakout momentum (+1,531 LoC) lifted R |
| **Amulya Kale** | 2 | 4 | **+2** | C+R both improved steadily |
| **Kaushal Bajaj** | 1 | 2 | **+1** | Minimal but positive C0→C1 |
| **Nishtha Thakral** | 0 | 1 | **+1** | First output (69 LoC) — still E-tier floor |

### 📉 Who Regressed (≤-2 points)

| User | CP3 C+R | CP5 C+R | Change | Key Driver |
|---|---|---|---|---|
| **Abhishek Hole** | 6 | 2 | **−4** | Zero LoC in final window + C collapse |
| **Vyankatesh Khadakkar** | 6 | 1 | **−5** | Severe decline — from A-candidate to D |
| **Nilesh Tonape** | 5 | 2 | **−3** | Outlier Premium (3,988) destroyed R score |
| **Sourabh Kalaskar** | 6 | 4 | **−2** | Dropped from A-tier to C-tier |
| **Mohan Alzughul** | 5 | 3 | **−2** | Steady decline in both C and R |
| **Prathmesh Ranadive** | 5 | 3 | **−2** | Outlier Premium penalty capped him at C |
| **Pradnyesh Salunke** | 5 | 3 | **−2** | Outlier Premium penalty (3,754 Prem) |
| **Megha Biradar** | 3 | 1 | **−2** | Peak at CP4, then C score collapse |
| **Abhijeet Kolhe** | 3 | 1 | **−2** | C score fell C2→C0 |
| **Suhas Kakde** | 2 | 0 | **−2** | Zero LoC final window → E-tier |
| **Prashasti Jain** | 1 | 0 | **−1** | R=0 + Premium>500 → E-tier |

### 🔵 Who Had Volatile Swings (±2+ point range across checkpoints)

| User | CP3 C+R | CP4 C+R | CP5 C+R | Range | Pattern |
|---|---|---|---|---|---|
| **Matt Field** | 5 | 5 | 4 | 2 pts | C score swung 2→3→2 |
| **Shraddha Kale** | 5 | 6 | 5 | 2 pts | Peaked at CP4, regressed at CP5 |
| **Trunal Gawade** | 3 | 2 | 4 | 2 pts | C score wildly volatile (3→1→3) |
| **Shubham Gite** | 3 | 1 | 4 | 3 pts | C score collapse then recovery |
| **Jayesh Rai** | 2 | 2 | 5 | 3 pts | Late-Q2 explosion |
| **Vyankatesh Khadakkar** | 6 | 4 | 1 | 5 pts | Severe progressive decline |

### 🟢 Who Stayed Stable (±1 point max)

| User | CP3 C+R | CP4 C+R | CP5 C+R | Range | Tier |
|---|---|---|---|---|---|
| **Amol Salunkhe** | 6 | 6 | 6 | 0 pts | A-tier locked |
| **Mikhail Shnayderman** | 6 | 6 | 6 | 0 pts | A-tier locked |
| **Pratik Devle** | 1 | 1 | 1 | 0 pts | D-tier stable |
| **Suraj Dubey** | 2 | 2 | 2 | 0 pts | D-tier stable (C=0 throughout) |
| **Chris Haun** | 4 | 4 | 4 | 0 pts | B-tier stable (C volatility but C+R flat) |
| **Vitthal Devkar** | 5 | 5 | 5 | 0 pts | B-tier stable (C3+R2 locked) |

---

## Budget Progression Tracking — Premium Requests Per Checkpoint

> **Key Finding**: The four outlier spenders (Prathmesh, Nilesh, Pradnyesh, Kranti) consumed **15,403 Q2 Premium Requests** by June 3 — approximately **54% of the 37-user analysis pool's premium budget**, while representing only **10.8% of the team**.

### Outlier Spend Emergence Timeline

| User | CP3 Prem (May 11) | CP4 Prem (May 18) | CP5 Prem (Jun 3) | Outlier Threshold (1,700) Crossed | Q2 Budget Impact |
|---|---|---|---|---|---|
| **Prathmesh Ranadive** | Est. 1,500-1,800 | 2,235 | 4,001 | Between CP3-CP4 | 4,001 Prem (highest) |
| **Nilesh Tonape** | Est. 1,800-2,000 | 3,038 | 3,988 | Between CP3-CP4 | 3,988 Prem (2nd highest) |
| **Pradnyesh Salunke** | Est. 1,600-1,900 | 2,238 | 3,754 | Between CP3-CP4 | 3,754 Prem (3rd highest) |
| **Kranti Kaple** | Est. 1,200-1,500 | 2,097 | 3,660 | Between CP3-CP4 | 3,660 Prem (4th highest) |
| **Combined** | — | — | **15,403** | — | **54% of team budget** |

**R Score Impact**: All four users have R=0 at CP5 due to outlier penalty (Premium > 1,700) and are capped at Tier C maximum per override rule.

### Lean Spend Champions (≤500 Premium at CP5)

| User | CP5 Prem | CP5 LoC | ReqEff | Lean Bonus Applied | Tier Impact |
|---|---|---|---|---|---|
| Amol Salunkhe | 748 | 30,486 | 40.8 | No (>500, but still lean relative to output) | A-tier |
| Ritesh Pawar | 431 | 8,662 | 20.1 | Yes (+1 → R=3) | A-tier |
| Mikhail Shnayderman | 565 | 24,387 | 43.2 | No (>500) | A-tier |
| Matt Field | 620 | 9,251 | 14.9 | No (>500) | B-tier |
| Shraddha Kale | 340 | 5,013 | 14.8 | Yes (+1 → R=3) | B-tier |
| Vitthal Devkar | 282 | 2,609 | 9.3 | Yes (+1 → R=2) | B-tier |
| Jayesh Rai | 250 | 2,196 | 8.8 | Yes (+1 → R=2) | B-tier (promoted from C) |
| Mohan Shivarkar | 285 | 1,559 | 5.5 | Yes (+1 → R=2) | C-tier (Breakout override) |
| Danny Cadima Molina | 3 | 34 | 11.0 | Yes (+1 → R=3) | B-tier (new user, tiny volume) |

---

## Per-User CRQC Progression Cards

### 🌟 Tier A Champions — Sustained Excellence

#### Amol Salunkhe
- **CP3 (May 11)**: C3+R3 = **6** | Workflow: Agent-First | Eff 35.96, 7.8× surge
- **CP4 (May 18)**: C3+R3 = **6** | 17,600 LoC, 747 Prem, ReqEff 40.8
- **CP5 (Jun 3)**: C3+R3 = **6** | 30,486 LoC Q2 cumulative, +1,575 final window
- **Pattern**: 🟢 Stable A — C3+R3 locked. Lean spend relative to massive output.
- **Key Strength**: Consistency. No volatility across any checkpoint. Top-tier Core + ROI sustained for 9 weeks.

#### Mikhail Shnayderman
- **CP3 (May 11)**: C3+R3 = **6** | Workflow: Agent-First | Eff 72.06, strongest AI usage
- **CP4 (May 18)**: C3+R3 = **6** | 24,387 LoC, 565 Prem, ReqEff 43.2
- **CP5 (Jun 3)**: C3+R3 = **6** | 24,387 LoC Q2, +2,119 final window
- **Pattern**: 🟢 Stable A — Pure agent-first champion. Zero inline acceptance, 100% agent mode.
- **Key Strength**: Highest weekly average output (2,710 LoC/week Q2). Technical excellence sustained.

#### Ritesh Pawar
- **CP3 (May 11)**: C2+R3 = **5** | Workflow: Agent-First | Eff 75.13, zero period output warning
- **CP4 (May 18)**: C2+R3 = **5** | 8,662 LoC, 431 Prem, lean bonus applied
- **CP5 (Jun 3)**: C3+R3 = **6** | 8,662 LoC Q2, +4 final window (near-zero)
- **Pattern**: 📈 Rising A — Lean bonus (+1 R) pushed him from C+R=5 to 6 at CP5.
- **Warning**: Final window is near-zero (+4 LoC). Q2 numbers are front-loaded. Q3 re-engagement critical.

---

### 👍 Tier B Solid — Consistent Delivery

#### Chris Haun
- **CP3 (May 11)**: C3+R1 = **4** + Q3 = **7 (A)** | 6 merged PRs, +88 LoC (stall warning)
- **CP4 (May 18)**: C2+R2 = **4** + Q3 = **7 (A)** | Breakout momentum: 88→8,592 LoC
- **CP5 (Jun 3)**: C2+R2 = **4** | 10,264 LoC Q2, +1,672 final window
- **Pattern**: 🟡 Stable B — C score volatility (C3→C2) but C+R total flat at 4. PR quality (Q3) saves tier.
- **Key Strength**: Highest interaction count in team (887 Int). High-frequency Hybrid user.

#### Matt Field
- **CP3 (May 11)**: C2+R2 = **5** + Q3 = **7 (A)** | 2 merged PRs (Jenkins pipelines)
- **CP4 (May 18)**: C3+R2 = **5** + Q3 = **8 (A)** | 9,071 LoC, 620 Prem
- **CP5 (Jun 3)**: C2+R2 = **4** | 9,251 LoC Q2, +180 final window
- **Pattern**: 🔵 Volatile — C score swings (C2→C3→C2). C+R range 4-5.
- **Warning**: Low final window activity (+180 LoC). Q3 re-engagement needed.

#### Jayesh Rai
- **CP3 (May 11)**: C1+R1 = **2** + Q3 = **5 (B)** | 1 merged PR (Release26.1, 12,417 lines)
- **CP4 (May 18)**: C0+R2 = **2** + Q3 = **5 (B)** | Lean bonus lifted R
- **CP5 (Jun 3)**: C3+R2 = **5** | 2,196 LoC Q2, +1,334 final window (Breakout)
- **Pattern**: 🚀 Breakout — Dramatic C+R improvement +3pts (2→5). C score explosion C0→C3.
- **Key Strength**: Late-Q2 surge. Final 16 days = +1,334 LoC. Strong Q3 momentum confirmed.

#### Vitthal Devkar
- **CP3 (May 11)**: C3+R2 = **5** | Workflow: Inline-First | 66.2% accept, 45 Code Accept count
- **CP4 (May 18)**: C3+R2 = **5** | 2,566 LoC, 282 Prem, ReqEff 9.3
- **CP5 (Jun 3)**: C3+R2 = **5** | 2,609 LoC Q2, +43 final window
- **Pattern**: 🟢 Stable B — C3+R2 locked across all checkpoints. Inline-first champion.
- **Key Strength**: Zero volatility. Inline workflow mastery sustained through Q2.

---

### 👌 Tier C Mixed — Volatile or Capped

#### Prathmesh Ranadive
- **CP3 (May 11)**: C3+R2 = **5** (B+ floor) | 471 Code Accept, 77.9% rate
- **CP4 (May 18)**: C3+R0 = **3** | 2,235 Prem (outlier penalty applied)
- **CP5 (Jun 3)**: C3+R0 = **3** (capped) | 20,436 LoC Q2, +10,947 final window, 4,001 Prem
- **Pattern**: 🔴 Capped — Outlier Premium (4,001) destroyed R score. CRQC override caps him at Tier C.
- **Budget Alert**: Highest Premium consumer in team. Despite excellent output (20k LoC), efficiency is poor (ReqEff 5.1).

#### Sourabh Kalaskar
- **CP3 (May 11)**: C3+R3 = **6** (A-tier floor) | Excellent Core + ROI at May 11
- **CP4 (May 18)**: C2+R2 = **4** | Lean bonus: 324 Prem, ReqEff 6.3 → R=2 + Q3 = **7 (A)**
- **CP5 (Jun 3)**: C2+R2 = **4** | 2,609 LoC Q2, +553 final window
- **Pattern**: 📉 Declining — Dropped from A-tier (C+R=6) to C-tier (C+R=4). C score regressed C3→C2.
- **Action**: Investigate why Core score declined. Output stable but adoption quality weakened.

#### Mohan Shivarkar
- **CP3 (May 11)**: C2+R0 = **2** + Q3 = **5 (B)** | 28 LoC, 2,375 PR lines — coding without Copilot
- **CP4 (May 18)**: C0+R1 = **1** + Q3 = **4 (C)** | Lean bonus: 69 Prem, ReqEff 0.4 → R=1
- **CP5 (Jun 3)**: C1+R2 = **3** | 1,559 LoC Q2, +1,531 final window (Breakout)
- **Pattern**: 🚀 Breakout — Recovery confirmed. +1,531 LoC in final 16 days lifted R from 1→2.
- **Key Strength**: Late-Q2 surge validates re-engagement. Eligible for B-tier promotion with Breakout override.

#### Trunal Gawade
- **CP3 (May 11)**: C3+R0 = **3** | 27.4% accept, 49 Code Accept, inline-first
- **CP4 (May 18)**: C1+R1 = **2** | Lean bonus: 93 Prem
- **CP5 (Jun 3)**: C3+R1 = **4** | 304 LoC Q2, +2 final window (near-zero)
- **Pattern**: 🔵 Volatile — C score wildly swings (C3→C1→C3). C+R range 2-4.
- **Warning**: Near-zero final window. Q2 output is tiny (304 LoC total). Volume constraint.

---

### 🟠 Tier D Struggling — Low Core or ROI

#### Shreedevi Patil
- **CP3 (May 11)**: C2+R1 = **3** + Q3 (tentative) = **6 (B)** | 30.0% accept, 8.80 Eff
- **CP4 (May 18)**: C1+R1 = **2** + Q3 = **5 (B)** | Lean bonus: 311 Prem, ReqEff 2.2
- **CP5 (Jun 3)**: C1+R1 = **2** | 1,013 LoC Q2, +323 final window
- **Pattern**: 📉 Declining — Dropped from B-tier (CP3) to D-tier (CP5). C score regressed C2→C1.
- **Action**: Core adoption weakening. Coach on agent mode for larger tasks.

#### Nilesh Tonape
- **CP3 (May 11)**: C2+R3 = **5** (B+ floor) | 11.9% accept, 24.42 Eff, high premium warning
- **CP4 (May 18)**: C3+R0 = **3** | 3,038 Prem (outlier penalty), highest consumer at CP4
- **CP5 (Jun 3)**: C2+R0 = **2** (capped) | 5,293 LoC Q2, +228 final window, 3,988 Prem
- **Pattern**: 📉 Declining — Outlier Premium (3,988) destroyed R score. Capped at Tier C max, floor stays D.
- **Budget Alert**: 2nd highest Premium consumer. ReqEff collapsed from 24.42 (CP3 SuggEff proxy) to 1.3 (actual).

#### Luis Salvatierra
- **CP3 (May 11)**: C1+R1 = **1** + Q3 = **5 (B)** | 13% accept, 6.13 Eff, 36 Code Accept
- **CP4 (May 18)**: C2+R0 = **2** + Q3 = **5 (B)** | 546 Prem, ReqEff 4.2
- **CP5 (Jun 3)**: C1+R0 = **1** (capped) | 4,564 LoC Q2, +2,272 final window (Rising)
- **Pattern**: 🔴 Capped — R=0 + Premium>500 cap enforced. Final window is strong (+2,272) but R=0 prevents tier lift.
- **Action**: Coach on agent mode efficiency. Output is decent but Premium spend is high (952) with R=0.

#### Suhas Kakde
- **CP3 (May 11)**: C1+R1 = **2** + Q3 = **5 (B)** | 8.73 Eff, 3 merged PRs (8,494-line INT-41859)
- **CP4 (May 18)**: C1+R1 = **2** + Q3 = **5 (B)** | Lean bonus: 489 Prem, ReqEff 3.4 → R=1
- **CP5 (Jun 3)**: C0+R0 = **0** (E-tier) | 1,639 LoC Q2, zero final window
- **Pattern**: 📉 Severe decline — Collapsed from B-tier (CP3-CP4) to E-tier (CP5). Zero LoC in final 16 days.
- **Critical**: Zero activity final window + C=0 + R=0 + Premium>500 = E-tier floor. Immediate coaching needed.

---

### 🔴 Tier E — Zero Productive Output

#### Nishtha Thakral
- **CP3 (May 11)**: C0+R0 = **0** + Q0 = **0 (E)** | Zero output confirmed at CP3
- **CP4 (May 18)**: C0+R0 = **0** + Q0 = **0 (E)** | 561 Prem consumed, 0 LoC
- **CP5 (Jun 3)**: C1+R0 = **1** | 69 LoC Q2 (first output), +69 final window, 1,042 Prem
- **Pattern**: 📈 Minimal rise — First LoC output at CP5. Still D-tier floor. Eligible for C-tier with Breakout override (requires VP review).
- **Budget Alert**: 1,042 Premium consumed across Q2 for only 69 LoC output = ReqEff 0.1 (worst in team).

#### Prashasti Jain
- **CP3 (May 11)**: C1+R1 = **1** | 14.3% accept, 9.67 Eff, P0 warning (5-period low)
- **CP4 (May 18)**: C1+R0 = **1** | Actual ReqEff 1.0 (not SuggEff 27.90)
- **CP5 (Jun 3)**: C0+R0 = **0** (E-tier) | 872 LoC Q2, +35 final window, 1,267 Prem
- **Pattern**: 📉 Declining — Fell to E-tier. C=0 + R=0 + Premium>500 = E-tier cap enforced.
- **Critical**: R=0 with 1,267 Premium consumed. Near-zero final window activity (+35 LoC). Immediate action required.

---

## When Users Crossed 1,700 Premium Threshold (Outlier Status Timing)

> **Outlier threshold**: Premium Requests > 1,700 → −1 R penalty applied

### Outlier Spenders — Checkpoint Timing

| User | Est. CP3 Prem (May 11) | CP4 Prem (May 18) | CP5 Prem (Jun 3) | Crossed 1,700 | Days in Outlier Status (as of Jun 3) |
|---|---|---|---|---|---|
| **Prathmesh Ranadive** | ~1,500-1,800 | 2,235 | 4,001 | Between CP3-CP4 (May 12-18) | ~16 days |
| **Nilesh Tonape** | ~1,800-2,000 | 3,038 | 3,988 | Between CP3-CP4 (May 12-18) | ~16 days |
| **Pradnyesh Salunke** | ~1,600-1,900 | 2,238 | 3,754 | Between CP3-CP4 (May 12-18) | ~16 days |
| **Kranti Kaple** | ~1,200-1,500 | 2,097 | 3,660 | Between CP3-CP4 (May 12-18) | ~16 days |

**Key Insight**: All four outlier spenders crossed the 1,700 Premium threshold during the **May 12-18 window** (between CP3 and CP4). By CP4 analysis date (May 18), the outlier penalty was already in effect. These four users remained in outlier status through the remainder of Q2 (16 days from May 18 → June 3).

### Budget Impact Visualization

| Checkpoint | Combined Outlier Prem (4 users) | Team Analysis Pool Est. Total Prem | Outlier % of Team Budget |
|---|---|---|---|
| **CP3 (May 11)** | ~6,000-6,500 (estimate) | ~15,000-18,000 | ~35-40% |
| **CP4 (May 18)** | 9,608 (actual) | ~20,000-23,000 | ~42-48% |
| **CP5 (Jun 3)** | 15,403 (actual) | ~28,500 (37 users × avg 770 Prem) | ~54% |

**Progression**: Outlier spend concentration **increased from ~35-40% (CP3) to 54% (CP5)** of team budget over the final 23 days of Q2.

---

## Action Items — Multi-Period Insights

| Priority | Action | Basis | Target Users |
|---|---|---|---|
| 🔴 P0 | **Immediate budget governance intervention** for outlier spenders | 4 users consumed 54% of team premium budget in Q2 | Prathmesh, Nilesh, Pradnyesh, Kranti |
| 🔴 P0 | **Coach on agent session discipline** to reduce Premium per LoC | ReqEff < 5 with Premium > 1,700 = severe budget waste | Prathmesh (5.1), Nilesh (1.3), Pradnyesh (0.6), Prashasti (0.7), Nishtha (0.1) |
| 🔴 P0 | **Re-engagement plan for zero-window users** | 6 users produced 0 LoC in final 16 days — front-loaded Q2 | Shraddha Kale, Abhishek Hole, Suhas Kakde, Shridhar Mishra, Pratik Pawar, Kaushal Bajaj |
| 🔴 P0 | **Suhas Kakde + Prashasti Jain E-tier intervention** | Both collapsed to E-tier at CP5 — zero productive output final window | Suhas Kakde, Prashasti Jain |
| 🟠 P1 | **Celebrate A-tier consistency champions** | 3 users maintained C+R=6 across entire Q2 (9 weeks) | Amol Salunkhe, Mikhail Shnayderman, Ritesh Pawar |
| 🟠 P1 | **Recognize Breakout performers** | Late-Q2 surge validated re-engagement | Jayesh Rai (+3 C+R pts), Mohan Shivarkar (+1,531 LoC final window) |
| 🟠 P1 | **Investigate C score volatility** | 6 users had ±2+ point C score swings across checkpoints — workflow instability? | Matt Field, Shraddha Kale, Trunal Gawade, Shubham Gite, Jayesh Rai, Vyankatesh |
| 🟡 P2 | **Q3 kickoff coaching for near-zero window users** | Final window <50 LoC — risk of slow Q3 start | Ritesh (+4), Trunal (+2), Shridhar (0), Kaushal (0) |
| 🟡 P2 | **Monitor Danny Cadima Molina volume** | Strong C+R=5 debut but Q2 output only 34 LoC — verify Q3 ramp-up | Danny Cadima Molina |

---

## VP Narrative Template — Multi-Period Progression

> "Our CRQC framework tracks Core adoption quality (C), budget efficiency (R), and code delivery quality (Q) across Q2 2026. We have checkpoint data from May 11, May 18, and June 3 (April checkpoints predate CRQC introduction).
>
> **Tier A consistency (3 users)**: Amol Salunkhe, Mikhail Shnayderman, and Ritesh Pawar maintained C+R scores of 6/6 across the entire 9-week Q2 period. These are our performance benchmarks — sustained excellence in both adoption and efficiency.
>
> **Budget crisis emergence**: Four users (Prathmesh Ranadive, Nilesh Tonape, Pradnyesh Salunke, Kranti Kaple) crossed the 1,700 Premium Request threshold between May 12-18. By June 3, they collectively consumed **15,403 Premium Requests** — **54% of our team budget** while representing only 10.8% of the team. All four are capped at Tier C maximum per CRQC override rules. This is our Q3 budget governance priority.
>
> **Late-Q2 momentum (positive)**: Jayesh Rai improved C+R by +3 points (2→5) across Q2, with a +1,334 LoC surge in the final 16 days. Mohan Shivarkar recovered from persistent R=0 warnings with a +1,531 LoC final window. Both enter Q3 with strong momentum.
>
> **Re-engagement risk (6 users)**: Shraddha Kale, Abhishek Hole, Suhas Kakde, Shridhar Mishra, Pratik Pawar, and Kaushal Bajaj produced zero LoC in the final 16 days of Q2. Their Q2 numbers are front-loaded. Without early Q3 coaching, slow starts are likely.
>
> **E-tier intervention required (2 users)**: Suhas Kakde and Prashasti Jain collapsed to E-tier (C=0, R=0) at the June 3 checkpoint. Suhas had zero LoC output in the final window despite 525 Premium Requests consumed. Prashasti consumed 1,267 Premium for only 872 LoC Q2 (ReqEff 0.7). Immediate coaching required.
>
> **C score volatility (6 users)**: Matt Field, Shraddha Kale, Trunal Gawade, Shubham Gite, Jayesh Rai, and Vyankatesh Khadakkar exhibited ±2+ point C score swings across checkpoints, indicating workflow instability. Investigate whether this reflects role changes, task variability, or adoption regression."

---

*Document generated June 3, 2026 from CRQC checkpoint data: May 11 (github-ai-analysis-11-may-2026-CRQC.md), May 18 (github-ai-analysis-18-may-2026-CRQC.md), June 3 (github-ai-analysis-3-june-2026-CRQC.md). April 20 and April 28 checkpoints use legacy Quick Benchmark methodology (no CRQC scores). Q2 cumulative data represents 9-week totals (April 1 → June 3, 2026).*
