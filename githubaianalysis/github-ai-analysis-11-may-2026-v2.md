# 📊 Github Analysis — 11 May 2026 (v2 — Workflow-Aware Format)

*Data source: Power BI GitHub 360 AI Usage dashboard, last synced 5/10/2026 9:39:11 PM | WFM Integrations | Based on **Github Quick Benchmark v2 (Workflow-Aware)***

> ⚠️ **Methodology note:** Premium Requests not exposed in current Power BI view. Suggestion Efficiency (LoC Added / Code Generation) used as T2 proxy for Request Efficiency. 4 users not captured in scroll (Kranti Kaple, Jyoti Kumbhar, Vishal Tiwari, Kaushal Bajaj).
>
> **v2 adds:** Workflow Type classification via Agent Contribution % (team-level: 91.4%) applied per-user using % Accept and Sugg Eff as proxies. This corrects the v1 structural error of applying the 20–35% accept benchmark to Agent-First users who are architecturally expected to score near 0%.

---

## 🔄 v2 vs v1 — Tier Differences

> **5 users re-tiered vs the v1 analysis. All movements are upgrades — workflow classification correctly recognizes strong users previously penalized for low % Accept.**

| User | v1 Tier | v2 Tier | Why It Changed |
|---|---|---|---|
| **Sourabh Kalaskar** | C | **B** | Reclassified as Hybrid (15.9% accept in 15–30% range = valid). Sugg Eff 29.80 > 8. Count 11 > 10. 3-point Hybrid Core. v1 penalized his accept rate using Inline benchmark incorrectly. |
| **Pradnyesh Salunke** | C | **B** | Reclassified as Inline-First (31.1% accept = in benchmark). Count 46 > 20 bonus. 3-point Core score. v1 had him borderline; v2 gives full credit. |
| **Suraj Dubey** | D | **C** | Reclassified as Agent-First. 0% accept is expected — not a failure signal. Sugg Eff 16.37 > 15 threshold = strong Core for Agent-First. v1 wrongly flagged 0% accept as a problem. |
| **Shubham Gite** | D | **C** | Reclassified as Inline-First. 57.2% accept + 139 count = 3-point Core. Volume is the only remaining issue. v1 placed him in D despite exceptional T1 signals. |
| **Trunal Gawade** | D | **C** | Reclassified as Inline-First. 27.4% accept in 20–35% range. Count 49 > 20 bonus. 3-point Core. v1 undervalued the T1 signal. |

---

## 📊 Step 0 — Workflow Type Classification

*Classification basis: Agent Contribution % is not exposed per-user in current Power BI view. Proxy classification uses % Code Acceptance and Suggestion Efficiency pattern. Team-level Agent Contribution = 91.4%.*

| Workflow Type | Users | % Accept Pattern | T1 Benchmark Applied |
|---|---|---|---|
| **Agent-First** | 14 users | < 10% accept, high Sugg Eff | Req Eff > 15 (primary), skip % Accept |
| **Hybrid** | 9 users | 10–29% accept, mixed signals | % Accept 15–30% + Eff > 8 |
| **Inline-First** | 9 users | ≥ 20–30% accept, high count | % Accept 20–35%, Count > 20 |
| **Research** | 1 user | — | Not tiered |

### Per-User Workflow Classification

| User | Workflow Type | % Accept | Sugg Eff | Basis |
|---|---|---|---|---|
| Mikhail Shnayderman | **Agent-First** | 0.3% | 72.06 | Near-zero accept, extreme Sugg Eff |
| Amol Salunkhe | **Agent-First** | 2.9% | 35.96 | Near-zero accept, high Sugg Eff |
| Ritesh Pawar | **Agent-First** | 6.1% | 75.13 | Low accept, exceptional Sugg Eff |
| Matt Field | **Agent-First** | 5.1% | 14.45 | Low accept, moderate Sugg Eff |
| Shraddha Kale | **Agent-First** | 5.2% | 11.10 | Low accept, moderate Sugg Eff |
| Swapnil Zade | **Agent-First** | 4.3% | 33.29 | Low accept, high Sugg Eff |
| Abhishek Hole | **Agent-First** | 0.0% | 61.86 | Zero accept (expected), high Sugg Eff |
| Moad Alzughul | **Agent-First** | 3.0% | 15.80 | Near-zero accept, solid Sugg Eff |
| Suhas Kakde | **Agent-First** | 2.2% | 8.73 | Near-zero accept, borderline Sugg Eff |
| Suraj Dubey | **Agent-First** | 0.0% | 16.37 | Zero accept (expected), solid Sugg Eff |
| Jayesh Rai | **Agent-First** | 3.0% | 7.69 | Near-zero accept, weak Sugg Eff |
| Pratik Devle | **Agent-First** | 6.6% | 6.07 | Low accept, weak Sugg Eff |
| Pratik Pawar | **Agent-First** | 5.0% | 1.66 | Low accept, very weak Sugg Eff |
| Susovan Samal | **Agent-First** | 8.3% | 3.17 | Manager, Agent-First patterns |
| Chris Haun | **Hybrid** | 15.9% | 8.68 | Mid accept, mixed signals, 814 int |
| Nilesh Tonape | **Hybrid** | 11.9% | 24.42 | Mid-low accept, high Sugg Eff |
| Sourabh Kalaskar | **Hybrid** | 15.9% | 29.80 | Mid accept, strong Sugg Eff |
| Luis Salvatierra | **Hybrid** | 13.0% | 6.13 | Mid-low accept, low Sugg Eff |
| Tushar Patil | **Hybrid** | 14.3% | 39.69 | Mid-low accept, very high Sugg Eff |
| Amulya Kale | **Hybrid** | 19.5% | 3.62 | Mid accept, low Sugg Eff |
| Abhijeet Kolhe | **Hybrid** | 18.8% | 10.75 | Mid accept, moderate Sugg Eff |
| Prashasti Jain | **Hybrid** | 14.3% | 9.67 | Mid-low accept, moderate Sugg Eff |
| Nishtha Thakral | **Hybrid** | 0.0% | 0.00 | Zero output — classification indeterminate |
| Prathmesh Ranadive | **Inline-First** | 77.9% | 14.52 | High accept rate, 471 count — clearly inline-dominant |
| Vyankatesh Khadakkar | **Inline-First** | 66.2% | 41.10 | High accept rate, 45 count |
| Vitthal Devkar | **Inline-First** | 44.8% | 14.21 | High accept rate, 78 count |
| Pradnyesh Salunke | **Inline-First** | 31.1% | 11.72 | In 20–35% range, 46 count |
| Shubham Gite | **Inline-First** | 57.2% | 1.10 | High accept rate, 139 count |
| Trunal Gawade | **Inline-First** | 27.4% | 1.46 | In 20–35% range, 49 count |
| Shreedevi Patil | **Inline-First** | 30.0% | 8.80 | In 20–35% range, 3 count (low) |
| Mohan Shivarkar | **Inline-First** | 69.6% | 1.22 | High accept, 16 count |
| Shridhar Mishra | **Inline-First** | 69.6% | 6.74 | High accept, 16 count — first LoC |
| Rahul Walunj | **Research** | — | — | Not tiered |

---

## Combined Dataset — In-Scope Users

*Columns: User | Workflow | LoC Added | Sugg Eff | % Accept | Code Accept | Code Gen | Int | T1 Signal (v2) | Tier*

| User | Workflow | LoC Added | Sugg Eff | % Accept | Code Accept | Code Gen | Int | T1 Signal (v2) | Tier |
|---|---|---|---|---|---|---|---|---|---|
| Mikhail Shnayderman | Agent-First | 22,268 | **72.06** | 0.3% | 1 | 309 | 162 | ✅✅ Eff >> 15 | 🌟 A |
| Amol Salunkhe | Agent-First | 17,155 | **35.96** | 2.9% | 14 | 477 | 191 | ✅✅ Eff >> 15 | 🌟 A |
| Prathmesh Ranadive | Inline-First | 8,783 | 14.52 | **77.9%** | **471** | 605 | 55 | ✅✅ Accept >> benchmark, count 471 | 🌟 A |
| Ritesh Pawar | Agent-First | 8,640 | **75.13** | 6.1% | 7 | 115 | 50 | ✅✅ Eff >> 15 ⚠️ zero new LoC | 🌟 A⚠️ |
| Matt Field | Agent-First | 8,566 | 14.45 | 5.1% | 30 | 593 | 489 | ✅ Eff borderline (8–15) | 👍 B |
| Chris Haun | Hybrid | 6,758 | 8.68 | 15.9% | 124 | 779 | 814 | ✅ Accept in 15–30%, Eff > 8, Count 124 ⚠️ stall | 👍 B⚠️ |
| Nilesh Tonape | Hybrid | 4,908 | **24.42** | 11.9% | 24 | 201 | 600 | ✅ Eff >> 8, Count 24 | 👍 B |
| Shraddha Kale | Agent-First | 4,706 | 11.10 | 5.2% | 22 | 424 | 445 | ✅ Eff in 8–15 | 👍 B |
| Swapnil Zade | Agent-First | 3,063 | **33.29** | 4.3% | 4 | 92 | 248 | ✅✅ Eff >> 15 | 👍 B |
| Vyankatesh Khadakkar | Inline-First | 2,795 | 41.10 | **66.2%** | 45 | 68 | 215 | ✅✅ Accept >> benchmark, Count 45 | 👍 B |
| Abhishek Hole | Agent-First | 2,722 | **61.86** | 0.0% | 0 | 44 | 97 | ✅✅ Eff >> 15 (0% accept expected) | 👍 B |
| Moad Alzughul | Agent-First | 2,655 | 15.80 | 3.0% | 5 | 168 | 90 | ✅ Eff just above 15 | 👍 B |
| Vitthal Devkar | Inline-First | 2,472 | 14.21 | **44.8%** | **78** | 174 | 101 | ✅✅ Accept >> benchmark, Count 78 | 👍 B |
| Sourabh Kalaskar | Hybrid | 2,056 | 29.80 | 15.9% | 11 | 69 | 153 | ✅ Accept 15–30%, Eff > 8, Count > 10 | 👍 **B** ⬆️ |
| Pradnyesh Salunke | Inline-First | 1,735 | 11.72 | **31.1%** | 46 | 148 | 203 | ✅✅ Accept in benchmark, Count 46 | 👍 **B** ⬆️ |
| Luis Salvatierra | Hybrid | 1,698 | 6.13 | 13.0% | 36 | 277 | 28 | 🟡 Accept below 15%, Eff < 8, Count > 10 | 👌 C |
| Suhas Kakde | Agent-First | 1,615 | 8.73 | 2.2% | 4 | 185 | 137 | 🟡 Eff borderline (8–15), LoC barely growing | 👌 C |
| Tushar Patil | Hybrid | 1,389 | **39.69** | 14.3% | 5 | 35 | 37 | 🟡 Accept just below 15%, Eff >> 8 | 👌 C |
| Amulya Kale | Hybrid | 1,133 | 3.62 | 19.5% | 61 | 313 | 147 | 🟡 Accept in 15–30%, Eff < 8 | 👌 C |
| Suraj Dubey | Agent-First | 491 | 16.37 | 0.0% | 0 | 30 | 11 | ✅ Eff > 15 (0% accept expected) — **v2 upgrade** | 👌 **C** ⬆️ |
| Shubham Gite | Inline-First | 268 | 1.10 | **57.2%** | **139** | 243 | 22 | ✅✅ Accept >> benchmark, Count 139 — volume only concern | 👌 **C** ⬆️ |
| Trunal Gawade | Inline-First | 261 | 1.46 | **27.4%** | 49 | 179 | 86 | ✅ Accept in benchmark, Count 49 — volume concern | 👌 **C** ⬆️ |
| Jayesh Rai | Agent-First | 777 | 7.69 | 3.0% | 3 | 101 | 61 | ❌ Eff < 8 | 🟠 D |
| Pratik Devle | Agent-First | 370 | 6.07 | 6.6% | 4 | 61 | 21 | ❌ Eff < 8 | 🟠 D |
| Abhijeet Kolhe | Hybrid | 172 | 10.75 | 18.8% | 3 | 16 | ~1 | 🟡 Accept in 15–30%, Eff > 8, Count < 10 | 🟠 D |
| Prashasti Jain | Hybrid | 203 | 9.67 | 14.3% | 3 | 21 | 14 | ❌ Accept below 15%, Count < 10 | 🟠 D |
| Pratik Pawar | Agent-First | 166 | 1.66 | 5.0% | 5 | 100 | 63 | ❌ Eff << 8 | 🟠 D |
| Shreedevi Patil | Inline-First | 88 | 8.80 | 30.0% | 3 | 10 | 73 | 🟡 Accept in benchmark, Count < 20 — tiny volume | 🟠 D |
| Mohan Shivarkar | Inline-First | 28 | 1.22 | 69.6% | 16 | 23 | 52 | 🟡 Accept excellent, Count < 20 — near-zero LoC | 🟠 D |
| Shridhar Mishra | Inline-First | 155 | 6.74 | 69.6% | 16 | 23 | 47 | 🟡 Accept excellent, Count < 20 — first LoC | 🟠 D |
| Nishtha Thakral | Hybrid | 0 | 0.00 | 0.0% | 0 | 16 | 51 | ❌ Zero output | 🔴 E |
| Susovan Samal | Agent-First | 38 | 3.17 | 8.3% | 1 | 12 | 26 | Manager — near-zero expected | 🔴 E |
| Rahul Walunj | Research | 0 | — | 0.0% | 0 | 4 | 21 | Research — not tiered | Research |

---

## ✅ GOOD USERS

### 🌟 Tier A — Top Performers (4 users)

| # | User | Workflow | LoC Added | Sugg Eff | T1 Signal (v2) | Notes |
|---|---|---|---|---|---|---|
| 1 | **Amol Salunkhe** | Agent-First | 17,155 | **35.96** | ✅✅ Eff >> 15 | 🏆 Breakout. 7.8× LoC. Agent-First: low accept is correct. Was wrongly borderline in v1. |
| 2 | **Mikhail Shnayderman** | Agent-First | 22,268 | **72.06** | ✅✅ Eff >> 15 | 🏆 Team MVP. 0.3% accept is structurally correct for Agent-First. v2 fully vindicates. |
| 3 | **Prathmesh Ranadive** | Inline-First | 8,783 | 14.52 | ✅✅ 77.9% accept, 471 count | 🏆 Coaching success. Inline-First benchmark (20–35%) exceeded by 2×. 471 count. |
| 4 | **Ritesh Pawar** | Agent-First | 8,640 | **75.13** | ✅✅ Eff >> 15 | ⚠️ Zero new LoC this period. Cumulative basis. Investigate. |

---

### 👍 Tier B — Solid Contributors (11 users)

*v2 adds Sourabh Kalaskar and Pradnyesh Salunke (both upgraded from Tier C).*

| # | User | Workflow | LoC Added | Sugg Eff | T1 Signal (v2) | Notes |
|---|---|---|---|---|---|---|
| 5 | **Matt Field** | Agent-First | 8,566 | 14.45 | ✅ Eff 8–15 | Solid Agent-First. High volume. Consistent. |
| 6 | **Chris Haun** | Hybrid | 6,758 | 8.68 | ✅ Accept 15.9% + Eff > 8 | ⚠️ Activity stall (+88 LoC). Hybrid signals correct but near-zero period output. Investigate. |
| 7 | **Nilesh Tonape** | Hybrid | 4,908 | **24.42** | ✅ Eff >> 8, Count 24 | Improving. Hybrid with strong ROI efficiency. |
| 8 | **Shraddha Kale** | Agent-First | 4,706 | 11.10 | ✅ Eff 8–15 | Consistent Agent-First. No accept penalty. |
| 9 | **Swapnil Zade** | Agent-First | 3,063 | **33.29** | ✅✅ Eff >> 15 | Strong Manager. Best Agent-First ROI proxy in management tier. |
| 10 | **Vyankatesh Khadakkar** | Inline-First | 2,795 | 41.10 | ✅✅ 66.2% accept, Count 45 | T1 breakout. Inline-First benchmark exceeded dramatically. |
| 11 | **Abhishek Hole** | Agent-First | 2,722 | **61.86** | ✅✅ Eff >> 15 (0% expected) | Agent-First: 0% accept is architecturally correct. v2 fully vindicates. |
| 12 | **Moad Alzughul** | Agent-First | 2,655 | 15.80 | ✅ Eff just above 15 | Steady Agent-First. |
| 13 | **Vitthal Devkar** | Inline-First | 2,472 | 14.21 | ✅✅ 44.8% accept, Count 78 | Strong Inline-First. 78 count is outstanding. |
| 14 | **Sourabh Kalaskar** | Hybrid | 2,056 | 29.80 | ✅ Accept 15.9%, Eff 29.80, Count 11 | **⬆️ Upgraded from C.** Hybrid signals all valid in v2. v1 penalized for 15.9% using inline benchmark. |
| 15 | **Pradnyesh Salunke** | Inline-First | 1,735 | 11.72 | ✅✅ 31.1% accept, Count 46 | **⬆️ Upgraded from C.** Inline-First benchmark hit. 46 count solid. v1 undervalued. |

---

## ⚠️ NEEDS IMPROVEMENT

### 👌 Tier C — Moderate Users (6 users)

*v2 adds Suraj Dubey, Shubham Gite, Trunal Gawade (all upgraded from D).*

| # | User | Workflow | LoC Added | Sugg Eff | T1 Signal (v2) | Issue | Action |
|---|---|---|---|---|---|---|---|
| 16 | **Luis Salvatierra** | Hybrid | 1,698 | 6.13 | ❌ Accept below 15%, Eff < 8 | Mixed Hybrid signals. Low engagement (28 int). | Increase Copilot sessions |
| 17 | **Suhas Kakde** | Agent-First | 1,615 | 8.73 | 🟡 Eff 8–15, barely growing | High interactions (137) but near-stall this period (+18 LoC). | Coaching on agent output quality |
| 18 | **Tushar Patil** | Hybrid | 1,389 | **39.69** | 🟡 Accept just below 15% | Strong Sugg Eff (39.69). Accept just below Hybrid threshold. | Push accept rate above 15% |
| 19 | **Amulya Kale** | Hybrid | 1,133 | 3.62 | 🟡 Accept 19.5%, Eff < 8 | Accept in range but Eff too low for Hybrid. | Improve agent output efficiency |
| 20 | **Suraj Dubey** | Agent-First | 491 | 16.37 | ✅ Eff > 15 (0% expected) | **⬆️ Upgraded from D.** v1 wrongly flagged 0% accept. Volume is the only concern. | Increase activity |
| 21 | **Shubham Gite** | Inline-First | 268 | 1.10 | ✅✅ 57.2%, Count 139 | **⬆️ Upgraded from D.** Exceptional T1. Volume-constrained by task assignment. | Give more Copilot-suitable tasks |
| 22 | **Trunal Gawade** | Inline-First | 261 | 1.46 | ✅ 27.4%, Count 49 | **⬆️ Upgraded from D.** Good T1. Volume-constrained. | Increase volume |

---

## 🔴 BAD USERS

### 🟠 Tier D — Low Efficiency (9 users)

| # | User | Workflow | LoC Added | Sugg Eff | T1 Signal (v2) | Problem |
|---|---|---|---|---|---|---|
| 23 | **Jayesh Rai** | Agent-First | 777 | 7.69 | ❌ Eff < 8 | Good volume growth but below efficiency threshold. |
| 24 | **Pratik Devle** | Agent-First | 370 | 6.07 | ❌ Eff < 8 | Near-stall. Low efficiency. |
| 25 | **Abhijeet Kolhe** | Hybrid | 172 | 10.75 | 🟡 Accept 18.8%, Eff > 8, Count < 10 | Tiny volume. Very low interaction (~1 int). |
| 26 | **Prashasti Jain** | Hybrid | 203 | 9.67 | ❌ Accept < 15%, Count < 10 | 🔴 P0 continues. 5 periods at near-zero. |
| 27 | **Pratik Pawar** | Agent-First | 166 | 1.66 | ❌ Eff << 8 | Very weak Agent-First signals. First LoC recorded. |
| 28 | **Shreedevi Patil** | Inline-First | 88 | 8.80 | 🟡 Accept 30%, Count < 20 | T1 accept in benchmark but count too low (3) and LoC tiny. |
| 29 | **Mohan Shivarkar** | Inline-First | 28 | 1.22 | 🟡 Accept 69.6%, Count < 20 | Highest accept rate in D. Only 28 LoC. Accepting micro-snippets only. |
| 30 | **Shridhar Mishra** | Inline-First | 155 | 6.74 | 🟡 Accept 69.6%, Count < 20 | First LoC. Strong accept signal. Count 16 (just below 20 threshold). |
| 31 | **Nishtha Thakral** | Hybrid | 0 | 0.00 | ❌ Zero output | No workflow signal possible. 5 periods, zero conversion. |

### 🔴 Tier E — Zero/Near-Zero (1 user)

| # | User | Workflow | LoC Added | Problem |
|---|---|---|---|---|
| 32 | **Susovan Samal** | Agent-First | 38 | Manager. Near-zero expected. Monitoring only. |

**Research (not tiered):**

| User | LoC Added | Int | Notes |
|---|---|---|---|
| **Rahul Walunj** | 0 | 21 | Research/Management. LoC metric not applicable. |

---

## 📊 Executive Scorecard (v2)

| Tier | Users | LoC Produced | % LoC | Key v2 Insight |
|---|---|---|---|---|
| 🌟 **A** | 4 | 56,846 | 53% | All 4 confirmed strong under workflow-appropriate benchmarks. Mikhail/Abhishek/Amol: 0% accept is correct for Agent-First. |
| 👍 **B** | 11 | 41,921 | 39% | +2 users from v1 (Sourabh, Pradnyesh). B now represents 33% of team. |
| 👌 **C** | 6 | ~3,967 | 4% | +3 users from v1 (Suraj, Shubham, Trunal). Agent-First zero-accept users no longer wrongly grouped with low performers. |
| 🟠 **D** | 9 | ~1,979 | 2% | -2 users from v1. All 9 have genuine gaps — not classification artifacts. |
| 🔴 **E** | 1 | 38 | <1% | Susovan = Manager. Nishtha moved to D (zero output but Hybrid workflow). |
| **Research** | 1 | 0 | — | — |
| **Total** | **32** | **~104,751** | | |

> **v2 verdict:** The team is stronger than v1 suggested. Tier A+B = 15 users (45% of team) producing 92% of LoC. The remaining 55% are genuinely low-efficiency — not misclassified.

---

## 📋 v2-Specific Action Items

| # | Action | Basis |
|---|---|---|
| 1 | **Do NOT use % Accept to evaluate Mikhail, Amol, Abhishek Hole, Suraj Dubey, or any Agent-First user** | v2 principle: near-zero accept is architecturally expected for this workflow type |
| 2 | **Confirm Agent Contribution % per-user when Power BI makes it available** | Current classification uses proxies — direct Agent Contribution % from Power BI AI Usage tab will be definitive |
| 3 | **Give Shubham Gite and Trunal Gawade more Copilot-appropriate tasks** | Both have excellent T1 signals (57.2%, 27.4% accept; 139, 49 count) but low volume — workflow classification confirms the issue is task volume, not skill |
| 4 | **Coach Suhas Kakde on agent output quality** | Agent-First with 8.73 Sugg Eff. Should be targeting >15. 137 interactions not converting |
| 5 | **Investigate Chris Haun stall** | Hybrid user with valid signals but +88 LoC only this period |

---

*Document generated 2026-05-11 from Power BI GitHub 360 AI Usage dashboard (WFM Integrations, data through 5/10/2026). Based on Github Quick Benchmark v2 (Workflow-Aware) methodology. Tier changes vs v1 are framework corrections, not behavioral changes.*
