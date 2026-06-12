# GitHub Copilot Usage Analysis — CRQC 4-Pillar Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 12, 2026 | **Data Sync:** June 11, 2026 (1:07 AM)  
**Scope:** 45 users (15 excluded per ignore list) | **Framework:** CRQC (Core + ROI + Quality + Context)

---

## CRQC Framework Overview

Four explicitly named pillars with scored evidence:

| Pillar | Score Range | Purpose | Source |
|---|---|---|---|
| **C** (Core) | 0–3 | Is the user engaged in productive workflow? | Power BI AI Usage |
| **R** (ROI) | 0–3 | Is premium spend justified by output? | Power BI AI Usage |
| **Q** (Quality) | 0–3 | Is output shipping and meeting review standards? | Power BI PR Details |
| **Context** | Diagnostic | Why do C/R/Q scores look this way? | Power BI AI Usage |

**Final tier:** Sum C + R + Q (0–9 total) → Tier A-E

---

## Workflow Type Classification (Required for Core Scoring)

**Limitation:** No Agent Contribution % available. Using binary "# Users Used Agents" flag.

| Workflow Type | Count | % of Team |
|---|---|---|
| **Used Agents** | 43 | 100% (all active users) |
| **Inline-Only** | 0 | 0% |

**Implication:** All users scored using "Agent-First" Core rules (LoC volume + trend, not % Accept).

---

## Core (C) Pillar Scoring (0–3 points)

**Rules for "Used Agents" workflow:**

| Signal | Condition | Points |
|---|---|---|
| LoC Added | > 10,000 | 3 |
| LoC Added | 5,000–10,000 | 2 |
| LoC Added | 2,000–5,000 | 1 |
| LoC Added | < 2,000 | 0 |
| LoC trend vs Jun 8 | Increasing | +1 bonus (cap at 3) |

**Core Scores (Top 15):**

| Login | Name | LoC | Jun 8 LoC | Trend | Base C | Trend Bonus | **C Score** |
|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 41,008 | 34,037 | ↑ +20.5% | 3 | +1 (cap) | **3** |
| Kranti-nice | Kranti Kaple | 31,645 | 27,733 | ↑ +14.1% | 3 | +1 (cap) | **3** |
| mshnayderman | Mikhail Shnayderman | 27,539 | 27,539 | → 0% | 3 | 0 | **3** |
| Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | 27,052 | → 0% | 3 | 0 | **3** |
| chris-haun | Chris Haun | 10,384 | ~10,359 | → +0.2% | 3 | 0 | **3** |
| mfield1 | Matt Field | 9,800 | ~9,300 | ↑ +5.4% | 2 | +1 | **3** |
| luisalvatierra | Luis Salvatierra | 9,477 | ~4,800 | ↑ +97.4% | 2 | +1 | **3** |
| rpawar-nice | Ritesh Pawar | 8,662 | 8,662 | → 0% | 2 | 0 | **2** |
| nilesht-19 | Nilesh Tonape | 7,346 | 7,160 | ↑ +2.6% | 2 | +1 | **3** |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,177 | 4,177 | → 0% | 1 | 0 | **1** |
| PradnyeshSalunke | Pradnyesh Salunke | 3,731 | ~2,968 | ↑ +25.7% | 1 | +1 | **2** |
| vishal-tad | Vishal Tad | 3,520 | ~2,900 | ↑ +21.4% | 1 | +1 | **2** |
| moadzughul | Moad Alzughul | 3,409 | ~3,100 | ↑ +10.0% | 1 | +1 | **2** |
| abhishekhole-nice | Abhishek Hole | 2,993 | 2,936 | ↑ +1.9% | 1 | +1 | **2** |
| sskalaskar | Sourabh Kalaskar | 2,698 | ~2,700 | → 0% | 1 | 0 | **1** |

**Core Score Distribution:**
- **C = 3:** 9 users (21%)
- **C = 2:** 10 users (23%)
- **C = 1:** 16 users (37%)
- **C = 0:** 8 users (19%)

---

## ROI (R) Pillar Scoring (0–3 points)

**Universal rules (same for all workflow types):**

| Signal | Condition | Points |
|---|---|---|
| Request Efficiency | > 20 LoC/request | 3 |
| Request Efficiency | 10–20 LoC/request | 2 |
| Request Efficiency | 5–10 LoC/request | 1 |
| Request Efficiency | < 5 LoC/request | 0 |
| Lean spend | Premium ≤ 500 | +1 bonus |
| Outlier spend | Premium > 1,700 | −1 penalty |

**ROI Scores (Top 15):**

| Login | Name | LoC | Premium | ReqEff | Base R | Lean Bonus | Outlier Penalty | **R Score** |
|---|---|---|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 8,662 | 850 | 10.2 | 2 | 0 | 0 | **2** |
| mfield1 | Matt Field | 9,800 | 1,813 | 5.4 | 1 | 0 | −1 | **0** |
| mshnayderman | Mikhail Shnayderman | 27,539 | 5,419 | 5.1 | 1 | 0 | −1 | **0** |
| amol-salunkhe | Amol Salunkhe | 41,008 | 11,150 | 3.7 | 0 | 0 | −1 | **−1 → 0** |
| jayesh-rai | Jayesh Rai | 2,479 | 852 | 2.9 | 0 | 0 | 0 | **0** |
| Kranti-nice | Kranti Kaple | 31,645 | 11,979 | 2.6 | 0 | 0 | −1 | **−1 → 0** |
| Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | 10,851 | 2.5 | 0 | 0 | −1 | **−1 → 0** |
| chris-haun | Chris Haun | 10,384 | 4,939 | 2.1 | 0 | 0 | −1 | **−1 → 0** |
| abhijeetk268 | Abhijeet Kolhe | 656 | 345 | 1.9 | 0 | 0 | 0 | **0** |
| luisalvatierra | Luis Salvatierra | 9,477 | 5,608 | 1.7 | 0 | 0 | −1 | **−1 → 0** |
| jkumbhar | Jyoti Kumbhar | 1,870 | 1,203 | 1.6 | 0 | 0 | 0 | **0** |
| moadzughul | Moad Alzughul | 3,409 | 3,052 | 1.1 | 0 | 0 | −1 | **−1 → 0** |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,177 | 4,062 | 1.0 | 0 | 0 | −1 | **−1 → 0** |
| Vitthal-Nice | Vitthal Devkar | 2,609 | 413 | 6.3 | 1 | 0 | 0 | **1** |
| dannycadima | Danny Cadima | 34 | 3 | 11.0 | 2 | 0 | 0 | **2** |

**Critical Observation:** 7 major producers (amol-salunkhe, Kranti-nice, Prathmesh-Ranadive, chris-haun, luisalvatierra, moadzughul, Vyankatesh95) all have **R = 0** due to outlier premium (>1,700) with low ReqEff (<5).

**ROI Score Distribution:**
- **R = 2:** 2 users (5%)
- **R = 1:** 2 users (5%)
- **R = 0:** 39 users (91%)

**Budget crisis impact:** The Jun 8 → Jun 12 premium spike pattern (documented in v1 analysis) causes **91% of users to score R = 0**. This is the most severe ROI failure rate observed.

---

## Quality (Q) Pillar Scoring (0–3 points)

**Source:** Power BI PR Details tab (Q2 2026 aggregate data, not Jun 12-specific)

**Team-level metrics:**
- PR Merge Rate: 89.7% (572 ÷ 638)
- Reviews per PR: 2.2 (1,402 ÷ 638)
- Avg Time to Merge: 166h 55m (~7 days)

**Scoring rules:**

| Signal | Condition | Points |
|---|---|---|
| PR Merge Rate | ≥ 80% | 2 |
| PR Merge Rate | 50–79% | 1 |
| PR Merge Rate | < 50% | 0 |
| Reviews per PR | ≥ 1 review/PR | +1 |
| Time to Merge | ≤ 3 days (72h) | +1 bonus (cap at 3) |

**Application:** Team-wide merge rate (89.7%) and review rate (2.2/PR) qualify for **Q = 2 + 1 = 3 points (max)** for all users with meaningful PR contribution (LoC > 1,000).

**Time to Merge bonus:** Team avg 166h 55m (~7 days) > 72h threshold → No bonus at team level.

**Quality Scores:**

| Login | Name | LoC | Q Score | Notes |
|---|---|---|---|---|
| Users with LoC > 1,000 | (27 users) | >1,000 | **3** | Team merge 89.7%, reviews 2.2/PR |
| Users with LoC < 1,000 | (16 users) | <1,000 | **0** | Insufficient PR contribution |

**Quality Score Distribution:**
- **Q = 3:** 27 users (63%)
- **Q = 0:** 16 users (37%)

---

## Context (C) Pillar — Diagnostic Only

**Not scored.** Used to explain anomalies in C/R/Q.

| Signal | What to Look For | Key Observations |
|---|---|---|
| Initiated Interactions | Very high with low C/R/Q → struggling | Kranti-nice (1,297 Int, C=3, R=0, Q=3) — High engagement, premium crisis |
| Suggestion Efficiency | High for Agent-First = healthy | amol-salunkhe (31.62), Kranti-nice (43.59), mshnayderman (60.79) — All healthy |
| LoC Suggested vs Added | Large gap in Inline = low acceptance | Not applicable (all users "Used Agents") |
| Code Generation Count | Very high with low C → volume without value | Kranti-nice (726 Gen) + amol-salunkhe (1,297 Gen) — High generation, both C=3 (good) |

---

## CRQC Final Tier Assignment

**Formula:** Total Score = C + R + Q (0–9)

**Tier mapping:**
| Total Score | Tier |
|---|---|
| 7–9 | 🌟 **A** |
| 5–6 | 👍 **B** |
| 3–4 | 👌 **C** |
| 1–2 | 🟠 **D** |
| 0 | 🔴 **E** |

### Override Rules Applied

| Condition | Override | Impact |
|---|---|---|
| Q = 0 (< 1,000 LoC) | Cannot be Tier A regardless of C + R | Applied to 16 users |
| R = 0 AND Premium > 500 | Cannot exceed Tier C regardless of C + Q | Applied to 37 users |
| Momentum > +100% | Eligible for one-tier promotion | Not applicable (no users with >+100% momentum) |
| Research role | Not tiered | Applied to rwalunj-nice |

**Critical Impact of R=0 Override:**
- 37 users have **R = 0 AND Premium > 500**
- These users are **capped at Tier C** regardless of C/R scores
- This includes major producers: amol-salunkhe (C=3, Q=3, Total=6 → **capped at C**), Kranti-nice (C=3, Q=3, Total=6 → **capped at C**), Prathmesh-Ranadive (C=3, Q=3, Total=6 → **capped at C**)

---

## CRQC Scorecard (All 43 Developers)

| Login | Name | **C** | **R** | **Q** | Total | Base Tier | Override Applied | **Final Tier** |
|---|---|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 2 | 2 | 3 | **7** | A | None | **A** |
| Vitthal-Nice | Vitthal Devkar | 1 | 1 | 3 | **5** | B | None | **B** |
| dannycadima | Danny Cadima | 0 | 2 | 0 | **2** | D | None | **D** |
| amol-salunkhe | Amol Salunkhe | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| Kranti-nice | Kranti Kaple | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| mshnayderman | Mikhail Shnayderman | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| Prathmesh-Ranadive | Prathmesh Ranadive | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| chris-haun | Chris Haun | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| mfield1 | Matt Field | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| luisalvatierra | Luis Salvatierra | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| nilesht-19 | Nilesh Tonape | 3 | 0 | 3 | **6** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| PradnyeshSalunke | Pradnyesh Salunke | 2 | 0 | 3 | **5** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| vishal-tad | Vishal Tad | 2 | 0 | 3 | **5** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| moadzughul | Moad Alzughul | 2 | 0 | 3 | **5** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| abhishekhole-nice | Abhishek Hole | 2 | 0 | 3 | **5** | B | **R=0 + Premium > 500 → Cap at C** | **C** ⬇ |
| Vyankatesh95 | Vyankatesh Khadakkar | 1 | 0 | 0 | **1** | D | None | **D** |
| sskalaskar | Sourabh Kalaskar | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| jayesh-rai | Jayesh Rai | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| Akale23 | Amulya Kale | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| mshivarkar | Mohan Shivarkar | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| trunalgawade | Trunal Gawade | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| jkumbhar | Jyoti Kumbhar | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| Shreedevi-nice | Shreedevi Patil | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| tusharpati166719 | Tushar Patil | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| meghabiradar05 | Megha Biradar | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| suhas-kakde | Suhas Kakde | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| prashasti-jain | Prashasti Jain | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| pdevle | Pratik Devle | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| giteshsawant | Gitesh Sawant | 1 | 0 | 3 | **4** | C | **R=0 + Premium > 500 → Cap at C** | **C** |
| thakraln | Nishtha Thakral | 1 | 0 | 0 | **1** | D | None | **D** |
| Shubhamfulzele28 | Shubham Fulzele | 1 | 0 | 0 | **1** | D | None | **D** |
| abhijeetk268 | Abhijeet Kolhe | 1 | 0 | 0 | **1** | D | None | **D** |
| dsuraj25 | Suraj Dubey | 1 | 0 | 0 | **1** | D | None | **D** |
| smishra-nice | Shridhar Mishra | 1 | 0 | 0 | **1** | D | None | **D** |
| sgite-wfm | Shubham Gite | 1 | 0 | 0 | **1** | D | None | **D** |
| pratikpawar12 | Pratik Pawar | 1 | 0 | 0 | **1** | D | None | **D** |
| kbajaj-nice | Kaushal Bajaj | 0 | 0 | 0 | **0** | E | None | **E** |

---

## CRQC vs v1 Comparison

| User | v1 Tier | CRQC Tier | Delta | Reason |
|---|---|---|---|---|
| amol-salunkhe | **A** | **C** | ⬇⬇ | R=0 override (Premium 11,150, ReqEff 3.7) |
| Kranti-nice | **A** | **C** | ⬇⬇ | R=0 override (Premium 11,979, ReqEff 2.6) |
| mshnayderman | **A** | **C** | ⬇⬇ | R=0 override (Premium 5,419, ReqEff 5.1) |
| mfield1 | **A** | **C** | ⬇⬇ | R=0 override (Premium 1,813, ReqEff 5.4) |
| rpawar-nice | **A** | **A** | — | Only user with R=2 (best efficiency) |
| Vitthal-Nice | **A** | **B** | ⬇ | R=1 (good but not excellent) |
| Prathmesh-Ranadive | **B** | **C** | ⬇ | R=0 override |
| luisalvatierra | **B** | **C** | ⬇ | R=0 override |
| jayesh-rai | **B** | **C** | ⬇ | R=0 override |
| nilesht-19 | **E** | **C** | ⬆⬆ | High C+Q scores; R=0 cap prevents further promotion |

**Key insight:** CRQC's R=0 override rule is **extremely punitive** when 91% of users fail ROI benchmarks due to the Jun 8 → Jun 12 premium spike pattern. The framework correctly identifies the budget crisis but produces **tier compression** where most productive users (amol-salunkhe, Kranti-nice) are downgraded to Tier C despite high output.

---

## Executive Summary: CRQC Framework Findings

### 1. ROI Pillar Drives Tier Outcomes
- **R = 0:** 39 users (91%)
- **R = 1:** 2 users (5%)
- **R = 2:** 2 users (5%)

The systematic premium spike (documented in v1 analysis) causes near-universal ROI failure. **CRQC's strength—explicit ROI scoring—becomes its limitation when a platform-level anomaly affects everyone.**

### 2. Quality Pillar Shows Team Strength
- **Q = 3:** 27 users (63%) — Team merge rate 89.7%, reviews 2.2/PR
- **Q = 0:** 16 users (37%) — Low LoC, insufficient PR contribution

The Q pillar validates strong team-wide PR quality.

### 3. Override Rules Cause Tier Compression
- **"R=0 AND Premium >500 → Cap at Tier C"** affects 37 users
- Result: Top producers (amol-salunkhe, Kranti-nice, Prathmesh-Ranadive) all capped at Tier C
- Only 2 users (rpawar-nice, Vitthal-Nice) avoid the override

### 4. CRQC Best Use Case
CRQC excels at **identifying budget inefficiency** with explicit scoring. In normal periods, the R pillar distinguishes lean/efficient users from wasteful ones. In this period's **platform anomaly context**, CRQC surfaces the systematic problem clearly but produces **tier outcomes misaligned with output value**.

**Recommendation:** Use CRQC alongside v1 Standard. When R scores are universally low (like this period), **investigate for systematic causes** before applying tier caps. The R=0 override rule should apply to **individual inefficiency**, not **platform-wide events**.

---

*CRQC 4-Pillar Framework — Explicit scoring across Core (productivity), ROI (efficiency), Quality (PR performance), and Context (diagnostic). R=0 override applied to 37 users due to Jun 8 → Jun 12 premium spike pattern.*
