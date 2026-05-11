# 📊 Github Analysis — 11 May 2026 (v1 — Standard Format)

*Data source: Power BI GitHub 360 AI Usage dashboard, last synced 5/10/2026 9:39:11 PM | WFM Integrations | ~38 users with data | 4 users not captured in scroll (see note) | Based on **Github Quick Benchmark v1***

> ⚠️ **Methodology note for this period:** Premium Requests data is not exposed in the current Power BI AI Usage view. Request Efficiency (LoC/Premium Request) has been replaced by **Suggestion Efficiency (LoC Added / Code Generation)** as the primary T2 proxy for this report. All other metrics are unchanged. This will be corrected in the next period once Premium Requests are accessible.

---

## 🔄 What Changed vs April 28 Analysis

> **7 users re-tiered. 2 extraordinary breakouts. 1 concerning stall.**
>
> | Movement | User | Direction | Notes |
> |---|---|---|---|
> | **Amol Salunkhe** | C → **A** | 📈📈🏆 | LoC 2,210→17,155 (7.8×). Biggest breakout this period. |
> | **Prathmesh Ranadive** | D → **A** | 📈📈🏆 | LoC 1,848→8,783 (+6,935). Accept rate 35.8%→77.9%, count 38→471. Coaching worked. |
> | **Nilesh Tonape** | D → **B** | 📈 | LoC 3,598→4,908. Eff 1.9→24.42 Sugg. |
> | **Swapnil Zade** | C → **B** | 📈 | LoC 2,507→3,063. Eff improving, manager showing strong results. |
> | **Abhishek Hole** | D → **B** | 📈 | LoC 319→2,722 (+2,403). Pure agent mode. |
> | **Vyankatesh Khadakkar** | B → **B** | ➡️📈 | LoC steady 2,350→2,795 but accept rate surged 23.1%→66.2%, count 6→45. |
> | **Chris Haun** | A → **B** | 📉 | Cumulative LoC 6,670→6,758 (+88 only). Near-zero activity this period. |
> | **Ritesh Pawar** | A → **A** | ⚠️ | Cumulative LoC exactly 8,640 — zero new activity. Possible leave. |

---

## 📋 Team Overview

| Metric | May 11 | vs Apr 28 | vs Apr 20 |
|---|---|---|---|
| **Team Size** | ~38 (data) + 4 new | ➡️ +4 new (Megha Biradar, Mohit Baghel, Sanket Nikam, Danny Cadima Molina) | — |
| **Total LoC Added (in-scope)** | ~108,134 | 📈 +31,846 vs Apr 28 (+42%) | — |
| **Agent Adoption** | ✅ 98% | ➡️ Same | — |
| **Agent Contribution** | ✅ 91.4% | — | — |
| **Team Avg % Code Acceptance** | ~20.8% | 📈 Was 12.1% (Apr 28) | — |
| **Team Total Code Acceptances** | ~1,230 | 📈 Was 501 (Apr 28) | — |
| **Team Total Code Generations** | ~5,925 | 📈 Was 4,143 | — |

> ⚠️ **4 users not captured in dashboard scroll:** Kranti Kaple, Jyoti Kumbhar, Kaushal Bajaj, Vishal Tiwari. Their Apr 28 metrics are referenced in notes. They should be looked up individually in Power BI AI Usage → USER METRICS table.

---

## 📊 Excluded Users

| # | User | Manager | Reason |
|---|---|---|---|
| 1 | Anand Krishnaswamy | Yoav Shulman | Different reporting chain |
| 2 | Ana Sarzosa | Stan Dalence Pierola | Different reporting chain |
| 3 | Anjali Sherikar | Govind Somani | Different reporting chain |
| 4 | Dhanshree Jagtap | Govind Somani | Different reporting chain |
| 5 | Govind Somani | Piyush Shirke | Different reporting chain |
| 6 | Harshada Bagane | Vaibhao Mahore | Different reporting chain |
| 7 | Prashant Shete | Non-CX | Non-CX |
| 8 | Sachin Fuse | Govind Somani | Different reporting chain |
| 9 | Shivraj Bahirat | Govind Somani | Different reporting chain |
| 10 | Sohan Bafna | Piyush Shirke | Different reporting chain |
| 11 | Tom Otvos | Bala Katta | Different reporting chain |
| 12 | Yogita Dhanwate | Govind Somani | Different reporting chain |

---

## 📊 New Users — No Data Yet (4)

| # | User | Manager |
|---|---|---|
| 1 | Danny Cadima Molina | Swapnil Zade |
| 2 | Megha Biradar | Swapnil Zade |
| 3 | Mohit Baghel | Susovan Samal |
| 4 | Sanket Nikam | Susovan Samal |

---

## Combined Dataset — In-Scope Users (sorted by LoC Added)

*Columns: # | User | Manager | Init Int | LoC Added | LoC Sugg | Code Accept | Code Gen | % Accept | Sugg Eff | vs Apr 28*

| # | User | Manager | Int | LoC Added | LoC Sugg | Code Accept | Code Gen | % Accept | Sugg Eff | vs Apr 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Mikhail Shnayderman | Alon Vax | 162 | 22,268 | 2,567 | 1 | 309 | 0.3% | 72.06 | 📈 +1,317 LoC |
| 2 | Amol Salunkhe | Swapnil Zade | 191 | 17,155 | 2,221 | 14 | 477 | 2.9% | 35.96 | 📈📈🏆 +14,945 |
| 3 | Prathmesh Ranadive | Swapnil Zade | 55 | 8,783 | 1,240 | 471 | 605 | 77.9% | 14.52 | 📈📈🏆 +6,935 |
| 4 | Ritesh Pawar | Susovan Samal | 50 | 8,640 | 113 | 7 | 115 | 6.1% | 75.13 | ⚠️ 0 change |
| 5 | Matt Field | Swapnil Zade | 489 | 8,566 | 3,743 | 30 | 593 | 5.1% | 14.45 | 📈 +2,929 |
| 6 | Chris Haun | Swapnil Zade | 814 | 6,758 | 6,795 | 124 | 779 | 15.9% | 8.68 | 📉 +88 only |
| 7 | Nilesh Tonape | Swapnil Zade | 600 | 4,908 | 2,359 | 24 | 201 | 11.9% | 24.42 | 📈 +1,310 |
| 8 | Shraddha Kale | Swapnil Zade | 445 | 4,706 | 3,350 | 22 | 424 | 5.2% | 11.10 | 📈 +153 |
| 9 | Swapnil Zade | Rahul Walunj | 248 | 3,063 | 32 | 4 | 92 | 4.3% | 33.29 | 📈 +556 |
| 10 | Vyankatesh Khadakkar | Swapnil Zade | 215 | 2,795 | 42 | 45 | 68 | 66.2% | 41.10 | 📈 +445, T1 surge |
| 11 | Moad Alzughul | Swapnil Zade | 90 | 2,655 | 598 | 5 | 168 | 3.0% | 15.80 | 📈 +35 |
| 12 | Abhishek Hole | Swapnil Zade | 97 | 2,722 | 14 | 0 | 44 | 0.0% | 61.86 | 📈📈 +2,403 |
| 13 | Vitthal Devkar | Susovan Samal | 101 | 2,472 | 174 | 78 | 174 | 44.8% | 14.21 | 📈 +1,292 |
| 14 | Sourabh Kalaskar | Swapnil Zade | 153 | 2,056 | 65 | 11 | 69 | 15.9% | 29.80 | 📈 +539 |
| 15 | Pradnyesh Salunke | Swapnil Zade | 203 | 1,735 | 1,127 | 46 | 148 | 31.1% | 11.72 | 📈 +878 |
| 16 | Luis Salvatierra | Swapnil Zade | 28 | 1,698 | 1,380 | 36 | 277 | 13.0% | 6.13 | 📈 +254 |
| 17 | Suhas Kakde | Swapnil Zade | 137 | 1,615 | 1,030 | 4 | 185 | 2.2% | 8.73 | 📈 +18 |
| 18 | Tushar Patil | Susovan Samal | 37 | 1,389 | 102 | 5 | 35 | 14.3% | 39.69 | 📈 +536 |
| 19 | Amulya Kale | Susovan Samal | 147 | 1,133 | 983 | 61 | 313 | 19.5% | 3.62 | 📈 +354 |
| 20 | Jayesh Rai | Swapnil Zade | 61 | 777 | 325 | 3 | 101 | 3.0% | 7.69 | 📈 +776 |
| 21 | Suraj Dubey | Susovan Samal | 11 | 491 | 264 | 0 | 30 | 0.0% | 16.37 | ➡️ 0 |
| 22 | Pratik Devle | Susovan Samal | 21 | 370 | 76 | 4 | 61 | 6.6% | 6.07 | 📈 +2 |
| 23 | Shubham Gite | Susovan Samal | 22 | 268 | 470 | 139 | 243 | 57.2% | 1.10 | 📈 +189, T1 surge |
| 24 | Trunal Gawade | Susovan Samal | 86 | 261 | 182 | 49 | 179 | 27.4% | 1.46 | 📈 +200 |
| 25 | Prashasti Jain | Swapnil Zade | 14 | 203 | 35 | 3 | 21 | 14.3% | 9.67 | 📉 Still low |
| 26 | Abhijeet Kolhe | Swapnil Zade | ~1 | 172 | 15 | 3 | 16 | 18.8% | 10.75 | ➡️ Stable |
| 27 | Pratik Pawar | Swapnil Zade | 63 | 166 | 2,248 | 5 | 100 | 5.0% | 1.66 | 📈 +166 |
| 28 | Shridhar Mishra | Rahul Walunj | 47 | 155 | 103 | 16 | 23 | 69.6% | 6.74 | 📈 +155 (was 0!) |
| 29 | Shreedevi Patil | Swapnil Zade | 73 | 88 | 8 | 3 | 10 | 30.0% | 8.80 | ➡️ Stable |
| 30 | Mohan Shivarkar | Swapnil Zade | 52 | 28 | 58 | 16 | 23 | 69.6% | 1.22 | ➡️ Stable |
| 31 | Susovan Samal | Rahul Walunj | 26 | 38 | 65 | 1 | 12 | 8.3% | 3.17 | ➡️ Manager |
| 32 | Nishtha Thakral | Susovan Samal | 51 | 0 | 103 | 0 | 16 | 0.0% | 0.00 | ➡️ Still zero |
| 33 | Rahul Walunj | Alon Vax | 21 | 0 | 76 | 0 | 4 | 0.0% | 0.00 | ➡️ Research |
| — | Kranti Kaple* | Swapnil Zade | — | — | — | — | — | — | — | ⚠️ Not captured |
| — | Jyoti Kumbhar* | Swapnil Zade | — | — | — | — | — | — | — | ⚠️ Not captured |
| — | Vishal Tiwari* | Swapnil Zade | — | — | — | — | — | — | — | ⚠️ Not captured |
| — | Kaushal Bajaj* | Susovan Samal | — | — | — | — | — | — | — | ⚠️ Not captured |

*Apr 28 reference: Kranti 3,259 LoC; Jyoti Kumbhar 1,412 LoC; Vishal Tiwari 1,156 LoC; Kaushal Bajaj 5 LoC*

---

## ✅ GOOD USERS

### 🌟 Tier A — Top Performers (4 users)

*High output volume + high Suggestion Efficiency. Multi-signal strength.*

| # | User | LoC Added | ΔLoC (Apr 28) | Sugg Eff | % Accept | Code Accept | Int | Code Gen | Rationale | vs Apr 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Amol Salunkhe** | 17,155 | **+14,945** 🏆 | **35.96** | 2.9% | 14 | 191 | 477 | 🏆🏆 **BREAKOUT OF THE PERIOD.** 7.8× LoC growth since Apr 28. Agent-dominant workflow producing extraordinary output. Was Tier C. Biggest improvement in team history. | 📈📈📈 C→A |
| 2 | **Mikhail Shnayderman** | 22,268 | +1,317 | **72.06** | 0.3% | 1 | 162 | 309 | 🏆 Team MVP retained. Highest cumulative LoC and Sugg Eff. Pure Agent-First workflow. Modest increment this period — normal for high-baseline users. | ➡️ Stable A |
| 3 | **Prathmesh Ranadive** | 8,783 | **+6,935** | **14.52** | **77.9%** ✅✅ | **471** 🏆 | 55 | 605 | 🏆🏆 **COACHING SUCCESS STORY OF THE PERIOD.** Was Tier D in Apr 28 (2.1 Req Eff, 864 premium). Now: 6,935 new LoC, accept rate 35.8%→77.9%, count 38→471. Every metric exploded. | 📈📈📈 D→A |
| 4 | **Ritesh Pawar** | 8,640 | **0** ⚠️ | **75.13** | 6.1% | 7 | 50 | 115 | Cumulative LoC remains high (2nd best Sugg Eff). ZERO new activity this period — identical to Apr 28. Possible leave/absence. Retains A on cumulative basis but flagged for investigation. | ⚠️ No new activity |

**💡 Tier A: 4 users, ~56,846 LoC (53% of total), consuming 21 Int avg per user (lean engagement)**

---

### 👍 Tier B — Solid Contributors (9 users)

*Good output volume OR strong efficiency signal. Multi-signal strength.*

| # | User | LoC Added | ΔLoC | Sugg Eff | % Accept | Code Accept | Int | Rationale | vs Apr 28 |
|---|---|---|---|---|---|---|---|---|---|
| 5 | **Matt Field** | 8,566 | +2,929 | **14.45** | 5.1% | 30 | 489 | High output, solid efficiency. Highly engaged (489 int). Consistent Tier B. | ➡️ Stable B |
| 6 | **Nilesh Tonape** | 4,908 | +1,310 | **24.42** | 11.9% | 24 | 600 | 📈 **UPGRADED from Tier D.** Was worst ROI user Apr 28. Sugg Eff 24.42 is now solid. T1 at 11.9% below benchmark but improving. Highest interactions (600) = engaged. | 📈 D→B |
| 7 | **Shraddha Kale** | 4,706 | +153 | **11.10** | 5.2% | 22 | 445 | Stable solid output. Agent-dominant. Very lean budget user. Eff steady. | ➡️ Stable B |
| 8 | **Swapnil Zade** | 3,063 | +556 | **33.29** | 4.3% | 4 | 248 | 📈 **UPGRADED from Tier C.** Manager delivering strong output. LoC 2,507→3,063. Sugg Eff excellent (33.29). Engagement rising (81→248 int). | 📈 C→B |
| 9 | **Vyankatesh Khadakkar** | 2,795 | +445 | **41.10** | **66.2%** ✅✅ | 45 | 215 | 📈 **T1 BREAKOUT.** Accept rate 23.1%→66.2% (tripled). Count 6→45. Sugg Eff excellent at 41.10. LoC steady growth. | 📈 B→B T1 surge |
| 10 | **Abhishek Hole** | 2,722 | **+2,403** | **61.86** | 0.0% | 0 | 97 | 📈 **UPGRADED from Tier D.** Was 319 LoC (Apr 28). Now 2,722. Pure Agent-First (0% accept expected). Sugg Eff 61.86 — excellent. | 📈 D→B |
| 11 | **Moad Alzughul** | 2,655 | +35 | **15.80** | 3.0% | 5 | 90 | Steady Agent-First performer. Low interactions, solid Sugg Eff. Stable. | ➡️ Stable B |
| 12 | **Vitthal Devkar** | 2,472 | +1,292 | **14.21** | **44.8%** ✅ | **78** 🥈 | 101 | Strong T1 signal (44.8% accept, 78 count). +1,292 LoC this period. 2nd highest Code Accept count. Balanced workflow. | ➡️ Stable B |
| 13 | **Chris Haun** | 6,758 | **+88** ⚠️ | 8.68 | 15.9% | 124 | 814 | 📉 **FLAGGED: Near-zero activity this period (+88 LoC).** Cumulative remains high. Was Tier A. Retains B on cumulative. 814 interactions still show high engagement but not converting. **Investigate.** | 📉 A→B (activity concern) |

**💡 Tier B: 9 users, ~38,645 LoC (36% of total)**

---

### Summary: Good Users (Tier A + B = 13 users)

| Metric | May 11 | vs Apr 28 |
|---|---|---|
| **Users** | 13 (38% of team) | 📈 Was 12 (+1) |
| **Total LoC Produced** | ~95,491 (~88%) | 📈 Was ~84% |
| **Avg % Code Acceptance** | ~18.3% | 📈 Was 15.7% |
| **Total Code Accept Count** | ~851 (69% of team total) | 📈 Was 307 |

---

## ⚠️ NEEDS IMPROVEMENT

### 👌 Tier C — Moderate Users (6 users)

*Some output, mixed efficiency and T1 signals.*

| # | User | LoC Added | ΔLoC | Sugg Eff | % Accept | Code Accept | Int | Concern | vs Apr 28 |
|---|---|---|---|---|---|---|---|---|---|
| 14 | **Sourabh Kalaskar** | 2,056 | +539 | 29.80 | 15.9% | 11 | 153 | Improving. Sugg Eff excellent (29.80). T1 at 15.9% below benchmark. Engagement high (153). | 📈 Improving |
| 15 | **Pradnyesh Salunke** | 1,735 | +878 | 11.72 | **31.1%** ✅ | 46 | 203 | Good T1 (31.1%, above benchmark). Count up (46). Strong engagement (203 int). Sugg Eff solid. | 📈 Improving |
| 16 | **Tushar Patil** | 1,389 | +536 | **39.69** | 14.3% | 5 | 37 | High Sugg Eff (39.69) — very efficient when coding. LoC growing steadily. T1 at 14.3% — coach on completions. | 📈 Steady growth |
| 17 | **Luis Salvatierra** | 1,698 | +254 | 6.13 | 13.0% | 36 | 28 | Moderate output. T1 at 13% below benchmark. Low engagement (28 int). Steady but slow improvement. | ➡️ Stable |
| 18 | **Suhas Kakde** | 1,615 | +18 | 8.73 | 2.2% | 4 | 137 | Only +18 LoC this period — nearly stalled. High interactions (137) but low output. T1 terrible (2.2%). | 📉 Stalling |
| 19 | **Amulya Kale** | 1,133 | +354 | 3.62 | 19.5% | 61 | 147 | T1 at 19.5% (near benchmark). Count improving (61). But Sugg Eff low (3.62) — too many suggestions, low LoC per event. | 📈 Slowly improving |

**💡 Tier C: 6 users, ~9,626 LoC (9% of total)**

---

## 🔴 BAD USERS — Needs Urgent Attention

### 🟠 Tier D — Low Efficiency (11 users)

*Low output, inconsistent signals, high coaching potential for some.*

| # | User | LoC Added | ΔLoC | Sugg Eff | % Accept | Code Accept | Int | Problem | T1 Potential | vs Apr 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| 20 | **Jayesh Rai** | 777 | +776 | 7.69 | 3.0% | 3 | 61 | Huge LoC jump from near-zero (1→777) but T1 still terrible (3.0%). High engagement but not converting. | ❌ Low | 📈 Major improvement |
| 21 | **Suraj Dubey** | 491 | 0 | 16.37 | 0.0% | 0 | 11 | 0% accept all periods. Zero change this period. Agent-only mode but near-zero activity. | ❌ Low | ➡️ Stable |
| 22 | **Pratik Devle** | 370 | +2 | 6.07 | 6.6% | 4 | 21 | Near-zero growth (+2). Low engagement. Worsening trend. | ❌ Low | 📉 Declining |
| 23 | **Shubham Gite** | 268 | +189 | 1.10 | **57.2%** ✅✅ | **139** | 22 | 🏆 **Highest accept count in D.** 57.2% rate — ABOVE benchmark. Volume too low to promote. Needs more Copilot-suitable tasks. | ✅✅ HIGHEST — give more volume | 📈 Up |
| 24 | **Trunal Gawade** | 261 | +200 | 1.46 | **27.4%** ✅ | 49 | 86 | Good T1 (27.4%, IN benchmark). Count improving (10→20→49). Volume the only issue. | ✅ Improving | 📈 Up |
| 25 | **Abhijeet Kolhe** | 172 | ~stable | 10.75 | 18.8% | 3 | ~1 | Very low engagement (~1 int). T1 near-threshold. Very small sample size. | 🟡 Low volume | ➡️ Stable |
| 26 | **Prashasti Jain** | 203 | ~stable | 9.67 | 14.3% | 3 | 14 | 🔴 **P0 CONTINUES.** 4-period trend of near-zero output. Was P0 in Apr 28 — unresolved. | ❌ Low | 📉 STILL CRITICAL |
| 27 | **Pratik Pawar** | 166 | +166 | 1.66 | 5.0% | 5 | 63 | First LoC recorded this period. Engagement up (2→63). Early signals. | 🟡 Emerging | 📈 First output |
| 28 | **Shreedevi Patil** | 88 | stable | 8.80 | **30.0%** ✅ | 3 | 73 | T1 IN benchmark (30%). But only 88 LoC and 10 code gen events — tiny volume. Exploring but not producing. | ✅ T1 good, needs volume | ➡️ Stable |
| 29 | **Mohan Shivarkar** | 28 | stable | 1.22 | **69.6%** | 16 | 52 | Highest accept rate among D users (69.6%). But only 28 LoC. Accepting short snippets. | ✅ T1 excellent, volume critical | ➡️ Stable |
| 30 | **Shridhar Mishra** | 155 | **+155** | 6.74 | **69.6%** | 16 | 47 | 📈 **First LoC ever recorded.** Was Tier E (0 LoC, 0/4 periods). 155 LoC and 69.6% accept = quality signal. Breakthrough moment. | ✅ Strong T1 | 📈 E→D |

**💡 Tier D: 11 users, ~2,979 LoC (3% of total)**

---

### 🔴 Tier E — Zero Output (2 users)

| # | User | LoC Added | % Accept | Code Accept | Int | Problem | vs Apr 28 |
|---|---|---|---|---|---|---|---|
| 31 | **Nishtha Thakral** | 0 | 0.0% | 0 | 51 | 🔴 Zero across all periods. Active (51 int) but zero conversion. 5-period flat. Train or revoke. | ➡️ Unchanged |
| 32 | **Susovan Samal** | 38 | 8.3% | 1 | 26 | 🟡 Manager. Near-zero expected. | ➡️ Manager |

**Research (not tiered):**
| User | LoC Added | Int | Notes |
|---|---|---|---|
| **Rahul Walunj** | 0 | 21 | Research/Management. 0 LoC expected. |

---

## 📊 Executive Scorecard

| Tier | Users | % Team | LoC Produced | % LoC | Avg Sugg Eff | Avg % Accept |
|---|---|---|---|---|---|---|
| 🌟 **A** | 4 | 12% | 56,846 | 53% | 48.9 | 21.6% |
| 👍 **B** | 9 | 27% | 38,645 | 36% | 22.2 | 18.6% |
| 👌 **C** | 6 | 18% | 9,626 | 9% | 16.8 | 15.9% |
| 🟠 **D** | 11 | 33% | 2,979 | 3% | 5.6 | 30.0% |
| 🔴 **E** | 2 | 6% | 38 | <1% | 1.6 | 4.2% |
| **Research** | 1 | 3% | 0 | 0 | — | — |
| **Total** | **33** | | **~108,134** | | | |

**The Story (significantly improved from Apr 28):**
> **39% of team (Tier A+B)** produces **89% of code.**
> **39% of team (Tier D+E)** produces **3% of code.**
> **The gap is narrowing** — Tier C grew to 18% of team (was 13%), absorbing users promoted from D.
>
> **⭐ Two extraordinary breakouts this period:**
> - Prathmesh Ranadive (D→A): Coached to success — 77.9% accept rate, 471 count.
> - Amol Salunkhe (C→A): 7.8× LoC increase.

---

## 📈 Five-Period Comparison

| Metric | Apr 14 | Apr 20 | Apr 23 | Apr 28 | May 11 | Trend |
|---|---|---|---|---|---|---|
| **Total LoC** | ~55,000 | ~60,400 | ~64,076 | ~76,288 | **~108,134** | 📈📈 |
| **Tier A+B Users** | 10 | 11 | 12 | 13 | **13** | 📈 |
| **Tier C Users** | — | — | 3 | 5 | **6** | 📈 |
| **Tier D+E Users** | 22 | 22 | 23 | 20 | **13** | 📈📈 Improving |
| **Team Avg % Accept** | — | — | 8.9% | 12.1% | **20.8%** | 📈📈 |
| **Biggest Breakout** | — | Sourabh | Sourabh | Amol (C→A) | **Prathmesh (D→A)** | 📈🏆 |
| **Biggest Concern** | — | — | Prashasti | Rahul prem surge | **Chris Haun (+88 only)** | ⚠️ |

---

## 📋 Action Plan

### 🔴 P0 — Immediate

| # | Action | Target | Owner | Impact |
|---|---|---|---|---|
| 1 | **Investigate Chris Haun stall** — Only +88 LoC since Apr 28. Was #1 team engagement (814 int). Determine if on leave, task change, or blocker. | Chris Haun | Swapnil Zade | Recover ~2,000 LoC/period |
| 2 | **Final decision on Prashasti Jain** — 5 periods, near-zero output. P0 from Apr 28 unresolved. Train or revoke. | Prashasti Jain | Swapnil Zade | Save premium spend |
| 3 | **Final decision on Nishtha Thakral** — 5 periods, zero LoC, zero accept. No improvement signal. | Nishtha Thakral | Susovan Samal | Save premium spend |

### 🟠 P1 — This Sprint

| # | Action | Target | Owner | Impact |
|---|---|---|---|---|
| 4 | **Celebrate Prathmesh Ranadive** — D→A in one period. 77.9% accept, 471 count. Share coaching playbook. | Prathmesh | Swapnil Zade | Team motivation + replicate |
| 5 | **Celebrate Amol Salunkhe** — C→A. 7.8× LoC growth. Document what changed. | Amol | Swapnil Zade | Team motivation |
| 6 | **Verify Ritesh Pawar** — Zero activity, exact same numbers as Apr 28. Check leave/absence. | Ritesh | Susovan Samal | Clarify A-tier status |

### 🟡 P2 — Next Sprint

| # | Action | Target | Owner | Impact |
|---|---|---|---|---|
| 7 | **Give Shubham Gite + Trunal Gawade more volume** — 57.2% and 27.4% accept rates are excellent. Output limited by task assignment. | Both | Susovan Samal | Potential C promotion |
| 8 | **Coach Suhas Kakde on workflow** — 137 int, only +18 LoC this period. High activity, near-zero conversion. | Suhas | Swapnil Zade | Unblock productivity |
| 9 | **Capture missing users** — Kranti Kaple, Jyoti Kumbhar, Vishal Tiwari, Kaushal Bajaj not in this report. Pull from Power BI USER METRICS individually. | 4 users | Rahul | Complete picture |

---

## Appendix: Susovan Samal's Team

| User | Tier | LoC Added | ΔLoC | % Accept | Code Accept | Sugg Eff | Status |
|---|---|---|---|---|---|---|---|
| Ritesh Pawar | 🌟 A | 8,640 | 0 ⚠️ | 6.1% | 7 | 75.13 | ⚠️ No new activity |
| Vitthal Devkar | 👍 B | 2,472 | +1,292 | 44.8% | 78 🥈 | 14.21 | ✅ Solid |
| Amulya Kale | 👌 C | 1,133 | +354 | 19.5% | 61 | 3.62 | 🟡 Slow improvement |
| Tushar Patil | 👌 C | 1,389 | +536 | 14.3% | 5 | 39.69 | ✅ Growing |
| Suraj Dubey | 🟠 D | 491 | 0 | 0.0% | 0 | 16.37 | 🟠 No change |
| Pratik Devle | 🟠 D | 370 | +2 | 6.6% | 4 | 6.07 | 📉 Stalling |
| Shubham Gite | 🟠 D | 268 | +189 | 57.2% | 139 | 1.10 | ✅ Needs volume |
| Trunal Gawade | 🟠 D | 261 | +200 | 27.4% | 49 | 1.46 | ✅ Improving |
| Susovan Samal (self) | 🔴 E | 38 | — | 8.3% | 1 | 3.17 | 🟡 Manager |
| Nishtha Thakral | 🔴 E | 0 | 0 | 0.0% | 0 | 0.00 | 🔴 Final warning |
| Kaushal Bajaj | — | — | — | — | — | — | ⚠️ Not captured |
| Sanket Nikam | — | — | — | — | — | — | 🆕 New |
| Mohit Baghel | — | — | — | — | — | — | 🆕 New |

## Appendix: Rahul Walunj's Direct Reports

| User | Tier | LoC Added | ΔLoC | % Accept | Sugg Eff | Status |
|---|---|---|---|---|---|---|
| Swapnil Zade | 👍 B | 3,063 | +556 | 4.3% | 33.29 | ✅ Upgraded C→B |
| Susovan Samal | 🔴 E | 38 | — | 8.3% | 3.17 | 🟡 Manager |
| Shridhar Mishra | 🟠 D | 155 | +155 | 69.6% | 6.74 | ✅ E→D, first LoC! |

---

*Document generated 2026-05-11 from Power BI GitHub 360 AI Usage dashboard (WFM Integrations, data through 5/10/2026). Based on Github Quick Benchmark v1 methodology. Note: Suggestion Efficiency substituted for Request Efficiency this period — Premium Requests data not available in current dashboard view.*
