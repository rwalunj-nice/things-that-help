# GitHub Copilot Usage Analysis — v1 Standard Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 23, 2026 | **Data Sync:** June 23, 2026  
**Scope:** 37 developers in-scope (16 excluded per ignore list + 1 excluded this session) | **Framework:** v1 Standard  
**Checkpoint:** CP9 (9th checkpoint in ongoing series) | **Q2 Closes:** June 30, 2026 (7 days away)

> **Data notes:**
> - PR data reflects activity through **June 21, 2026** (2 days before analysis date). Recent PRs may not be reflected.
> - Premium figures are cumulative since program start, not period-only.
> - All 37 in-scope developers have Used Agents = 1 (Agent-First mode applies universally). Low % Accept is expected; all users evaluated primarily on **LoC + ReqEff**.
> - **Shubhamfulzele28** appears in Budget Crisis callout but is not in the CP9 developer dataset — figures sourced from prior period tracking.

---

## CP8 → CP9 Changes (June 12 → June 23, 11 days)

| Signal | CP8 (Jun 12) | CP9 (Jun 23) | Delta | Notes |
|---|---|---|---|---|
| Active Developers (in-scope) | ~35 | 37 | +2 | ssnikam (0 AI), kbajaj-nice added to tracking |
| Total LoC Added (in-scope) | ~212,000 | ~256,000 | +44,000 (+21%) | 11-day window; solid production |
| Total Premium (in-scope) | ~185,000 | ~256,000+ | Significant increase | Budget crisis users still growing |
| Tier E (crisis) users | 10 | 12 active crisis + 5 zero | — | Crisis pool expanding |
| Budget Crisis threshold (>1,700 premium) | 6 users | 9 users | +3 | Tushar Patil NEW #1 |

### Key Movers — LoC Growth (CP8 → CP9, 11 days)

| User | CP8 LoC | CP9 LoC | Delta | Pattern |
|---|---|---|---|---|
| Prathmesh-Ranadive | 27,052 | 35,091 | **+8,039** | BIGGEST GAINER — surging |
| Kranti-nice | 31,645 | 37,978 | +6,333 | Strong growth, premium exploded |
| mshivarkar | 2,097 | 4,201 | **+2,104** | DOUBLED in 11 days |
| luisalvatierra | 9,477 | 12,080 | +2,603 | Solid upward trend |
| amol-salunkhe | 41,008 | 43,585 | +2,577 | Steady leader |
| sskalaskar | 2,698 | 3,233 | +535 | Moderate growth |
| PradnyeshSalunke | 3,731 | 4,237 | +506 | Modest growth |
| jayesh-rai | 2,479 | 2,712 | +233 | Steady |
| vishal-tad | 3,520 | 3,737 | +217 | Modest |
| giteshsawant | 1,110 | 1,369 | +259 | Coming up slowly |
| trunalgawade | 2,038 | 2,352 | +314 | Growing but premium worsening |
| suhas-kakde | 1,677 | 2,005 | +328 | Improving |

### Zero-Movement Users (11 days, 0 LoC change)

mshnayderman (+0), rpawar-nice (+0), copilotshree (+0), Vyankatesh95 (+0), moadzughul (+0), Akale23 (+0). These users appear frozen since CP8 — confirms stale data or no activity in this 11-day window.

### Key CP8 → CP9 Theme Changes

1. **Tushar Patil (tusharpatil166719) becomes NEW #1 Budget Crisis** — 35,886 premium requests with only 2,200 LoC. ReqEff = 0.06. This eclipsed all prior single-user spend.
2. **Kranti Kaple (Kranti-nice) premium exploded** — 11,979 at CP8 → 35,537 at CP9 (+23,558 in 11 days). LoC grew but not proportionally.
3. **Shubham Fulzele (Shubhamfulzele28)** — 29,049 premium at CP9 (doubled from 13,831 at CP8). LoC = 1,043. Catastrophic ROI.
4. **mshivarkar almost doubled LoC** (+2,104 in 11 days) but premium also grew — tier remains E due to cumulative budget.
5. **ssnikam (Sanket Nikam)** — Zero AI activity but 55 PRs opened, 49 merged. New developer with no Copilot onboarding at all.

---

## Team Overview (In-Scope Developers Only)

| Metric | Value | Notes |
|---|---|---|
| In-Scope Developers | 37 | Excludes 16 per ignore list |
| Total LoC Added | ~256,000 | Cumulative program total |
| Total Initiated Interactions | ~10,650 | Across all 37 devs |
| Total Code Acceptance Count | ~3,077 | Cumulative |
| Total Premium Requests | ~340,000+ | Dominated by 9 crisis users |
| PRs Opened (tracked) | 496 | From PR dataset (through Jun 21) |
| PRs Merged | 440 | Overall merge rate ~88.7% |
| Average ReqEff (in-scope, excl. zero) | ~1.8 | Dragged down by crisis users |
| Median ReqEff (excluding E-tier crisis) | ~1.2 | Most devs below efficiency target |
| Developers with ReqEff > 10 | 5 | mshnayderman, rpawar-nice, copilotshree, mfield1, abhijeetk268 |
| Developers with ReqEff < 1.0 | 18 | Majority of team; coaching priority |

> **Agent-First Context:** Since all 37 developers have Used Agents = 1, the standard % Code Acceptance T1 metric (20–35% target) is deprioritized. Tier assignments use **LoC output + ReqEff (T2)** as primary signals per the Agent-First exception.

---

## Budget Crisis — URGENT EXECUTIVE CALLOUT

> These users are consuming disproportionate premium budget relative to code output. Combined premium for the top 9 crisis users exceeds **200,000 requests** — estimated majority of team's total spend. Immediate management intervention required before Q2 closes (June 30).

### Critical (Immediate Intervention)

| Rank | User | Name | Premium | LoC | ReqEff | Status |
|---|---|---|---|---|---|---|
| 1 | tusharpatil166719 | Tushar Patil | **35,886** | 2,200 | **0.06** | NEW #1 CRISIS — worst ROI in program history |
| 2 | Kranti-nice | Kranti Kaple | **35,537** | 37,978 | **1.07** | Premium tripled in 11 days; LoC growth insufficient |
| 3 | Shubhamfulzele28 | Shubham Fulzele | **29,049** | 1,043 | **0.04** | Doubled from CP8; catastrophic waste |
| 4 | nilesht-19 | Nilesh Tonape | **32,332** | 7,354 | **0.23** | Persistent crisis; flagged since CP6 |
| 5 | Prathmesh-Ranadive | Prathmesh Ranadive | **31,420** | 35,091 | **1.12** | High LoC partially justifies; still watch-listed |

### Warning Level (Budget Monitoring Required)

| Rank | User | Name | Premium | LoC | ReqEff | Status |
|---|---|---|---|---|---|---|
| 6 | PradnyeshSalunke | Pradnyesh Salunke | 20,544 | 4,237 | 0.21 | Persistent; flagged since CP7 |
| 7 | trunalgawade | Trunal Gawade | 18,720 | 2,352 | 0.13 | Growing worse each checkpoint |
| 8 | mshivarkar | Mohan Shivarkar | 17,029 | 4,201 | 0.25 | Doubled LoC but premium disproportionate |
| 9 | sskalaskar | Sourabh Kalaskar | 16,897 | 3,233 | 0.19 | Moderate growth but spending accelerating |

**Combined premium (Top 9):** ~216,000+ requests  
**Combined LoC (Top 9):** ~107,608 lines  
**Effective combined ReqEff:** ~0.50 — well below target of >10

---

## Full Developer Metrics Table (37 Developers)

> **Column key:** Int = Initiated Interactions | LoC = LoC Added | %Acc = % Code Acceptance | SuggEff = Suggestion Efficiency | Premium = Premium Requests | ReqEff = Request Efficiency (LoC÷Premium) | PRs = Total PRs | Mrg = PRs Merged | MR% = Merge Rate
> **All users = Agent-First** (Used Agents = 1). %Acc is informational; tier driven by LoC + ReqEff.

| Login | Name | Manager | Int | LoC | %Acc | SuggEff | Premium | ReqEff | PRs | Mrg | MR% | v1 Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | SwapnilNice | 504 | 43,585 | 1.5% | 31.95 | 20,170 | **2.2** | 8 | 8 | 100% | **D** |
| Kranti-nice | Kranti Kaple | SwapnilNice | 1,430 | 37,978 | 4.6% | 47.53 | 35,537 | **1.1** | 22 | 16 | 72.7% | **E** |
| Prathmesh-Ranadive | Prathmesh Ranadive | SwapnilNice | 105 | 35,091 | 88.7% | 19.90 | 31,420 | **1.1** | 24 | 24 | 100% | **D** |
| mshnayderman | Mikhail Shnayderman | Alon Vax | 164 | 27,539 | 27.8% | 60.79 | 5,452 | **5.1** | 2 | 1 | 50% | **B** |
| luisalvatierra | Luis Salvatierra | SwapnilNice | 629 | 12,080 | 24.2% | 13.33 | 9,542 | **1.3** | 12 | 10 | 83.3% | **D** |
| chris-haun | Chris Haun | SwapnilNice | 1,643 | 10,493 | 9.3% | 7.72 | 12,535 | **0.8** | 47 | 45 | 95.7% | **D** |
| mfield1 | Matt Field | SwapnilNice | 765 | 9,803 | 5.8% | 12.12 | 3,133 | **3.1** | 33 | 31 | 93.9% | **C** |
| rpawar-nice | Ritesh Pawar | ssamal-nice | 79 | 8,662 | 7.6% | 60.15 | 879 | **9.9** | 0 | 0 | — | **B** |
| nilesht-19 | Nilesh Tonape | SwapnilNice | 1,244 | 7,354 | 30.2% | 18.34 | 32,332 | **0.2** | 20 | 18 | 90% | **E** |
| copilotshree | (Shreedevi?) | Non-CX Eng | 621 | 5,013 | 4.8% | 11.02 | 340 | **14.8** | 0 | 0 | — | **A** |
| PradnyeshSalunke | Pradnyesh Salunke | SwapnilNice | 664 | 4,237 | 19.4% | 8.39 | 20,544 | **0.2** | 8 | 8 | 100% | **E** |
| mshivarkar | Mohan Shivarkar | SwapnilNice | 681 | 4,201 | 9.4% | 7.34 | 17,029 | **0.2** | 11 | 11 | 100% | **E** |
| Vyankatesh95 | Vyankatesh Khadakkar | SwapnilNice | 423 | 4,177 | 34.1% | 30.27 | 4,118 | **1.0** | 16 | 16 | 100% | **C** |
| vishal-tad | Vishal Tad | ssamal-nice | 486 | 3,737 | 8.8% | 4.19 | 9,301 | **0.4** | 17 | 15 | 88.2% | **D** |
| moadzughul | Moad Alzughul | SwapnilNice | 255 | 3,409 | 2.4% | 9.19 | 3,072 | **1.1** | 45 | 43 | 95.6% | **D** |
| sskalaskar | Sourabh Kalaskar | SwapnilNice | 367 | 3,233 | 16.9% | 23.77 | 16,897 | **0.2** | 15 | 13 | 86.7% | **E** |
| abhishekhole-nice | Abhishek Hole | SwapnilNice | 252 | 3,150 | 3.2% | 33.16 | 4,416 | **0.7** | 14 | 14 | 100% | **D** |
| Vitthal-Nice | Vitthal Devkar | ssamal-nice | 175 | 2,683 | 40.4% | 13.55 | 2,393 | **1.1** | 7 | 7 | 100% | **C** |
| jayesh-rai | Jayesh Rai | SwapnilNice | 153 | 2,712 | 18.4% | 13.49 | 1,997 | **1.4** | 17 | 17 | 100% | **C** |
| trunalgawade | Trunal Gawade | ssamal-nice | 389 | 2,352 | 20.4% | 8.40 | 18,720 | **0.1** | 1 | 1 | 100% | **E** |
| Akale23 | Amulya Kale | ssamal-nice | 266 | 2,472 | 22.8% | 5.41 | 4,237 | **0.6** | 7 | 6 | 85.7% | **C** |
| suhas-kakde | Suhas Kakde | SwapnilNice | 194 | 2,005 | 1.7% | 8.39 | 2,797 | **0.7** | 29 | 27 | 93.1% | **D** |
| tusharpatil166719 | Tushar Patil | ssamal-nice | 122 | 2,200 | 14.7% | 11.58 | 35,886 | **0.06** | 4 | 4 | 100% | **E** |
| jkumbhar | Jyoti Kumbhar | SwapnilNice | 244 | 1,880 | 22.0% | 15.93 | 2,110 | **0.9** | 19 | 12 | 63.2% | **C** |
| Shreedevi-nice | Shreedevi Patil | SwapnilNice | 232 | 1,886 | 8.8% | 55.47 | 12,071 | **0.2** | 15 | 14 | 93.3% | **E** |
| meghabiradar05 | Megha Biradar | SwapnilNice | 128 | 1,727 | 12.5% | 8.30 | 10,131 | **0.2** | 5 | 5 | 100% | **D** |
| prashasti-jain | Prashasti Jain | SwapnilNice | 202 | 1,562 | 7.2% | 6.27 | 12,206 | **0.1** | 8 | 7 | 87.5% | **E** |
| pdevle | Pratik Devle | ssamal-nice | 110 | 1,478 | 6.3% | 13.20 | 10,057 | **0.1** | 7 | 7 | 100% | **E** |
| giteshsawant | Gitesh Sawant | ssamal-nice | 236 | 1,369 | 2.2% | 15.38 | 8,585 | **0.2** | 1 | 0 | 0% | **E** |
| dsuraj25 | Suraj Dubey | ssamal-nice | 21 | 1,169 | 33.3% | 12.57 | 9,893 | **0.1** | 1 | 1 | 100% | **D** |
| thakraln | Nishtha Thakral | ssamal-nice | 215 | 806 | 0.0% | 8.96 | 13,562 | **0.1** | 0 | 0 | — | **E** |
| abhijeetk268 | Abhijeet Kolhe | SwapnilNice | 39 | 656 | 29.6% | 24.30 | 451 | **1.5** | 53 | 49 | 92.5% | **C** |
| pratikpawar12 | Pratik Pawar | SwapnilNice | 116 | 250 | 4.1% | 2.03 | 815 | **0.3** | 9 | 9 | 100% | **D** |
| amol-doke | Amol Doke | SwapnilNice | 26 | 10 | 22.2% | 0.56 | 2,528 | **0.0** | 8 | 4 | 50% | **E** |
| mohitbaghelnice | Mohit Baghel | ssamal-nice | 54 | 3 | 0.0% | 3.00 | 2,393 | **0.0** | 1 | 1 | 100% | **E** |
| kbajaj-nice | Kaushal Bajaj | ssamal-nice | 0 | 5 | 17.5% | 0.13 | 6 | **0.8** | 2 | 2 | 100% | **E** |
| dannycadima | Danny Cadima Molina | SwapnilNice | 11 | 34 | 12.7% | 0.14 | 3 | **11.0** | 0 | 0 | — | **E** |
| ssnikam | Sanket Nikam | ssamal-nice | **0** | **0** | **—** | **—** | **0** | **—** | 55 | 49 | 89.1% | *No AI* |

---

## Special Roles (Excluded from Developer Tier)

| Login | Name | Role | Manager | Int | LoC | %Acc | Premium | ReqEff | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | Manager | rwalunj-nice | 279 | 3,140 | 4.0% | 1,650 | **1.9** | Active coder-manager; premium reasonable for leadership level |
| ssamal-nice | Susovan Samal | Manager | rwalunj-nice | 30 | 38 | 7.7% | 109 | **0.3** | Low engagement; minimal AI usage |
| smishra-nice | Shridhar Mishra | Lead | rwalunj-nice | 60 | 155 | 78.3% | 287 | **0.5** | 78.3% accept = near-perfect inline; likely code review/small fixes use pattern |
| rwalunj-nice | Rahul Walunj | Research | — | 61 | 156 | 7.1% | 1,890 | **0.1** | Research/analysis exploration; high premium relative to output expected |

---

## Tier Groupings

### Tier A — Excellent (1 developer)

> Users with Excellent performance on both T1 (Agent-First: LoC) + T2 (ReqEff > 10, lean premium spend).

---

**copilotshree | (Shreedevi?) — Non-CX Engineering**
- Int: 621 | LoC: 5,013 | %Acc: 4.8% | ReqEff: **14.8** | Premium: 340 | Workflow: Agent-First
- **Tier A on both metrics.** ReqEff of 14.8 clears the >10 threshold cleanly. Premium spend of 340 is the leanest among mid-volume users. LoC of 5,013 is solid for non-CX workload. While %Acc (4.8%) is low, this is expected for Agent-First — the ReqEff signal confirms productive agent sessions.
- Non-CX member: tracked here for completeness but not benchmarked against CX team KPIs.
- **Coaching note:** Maintain current usage discipline. This is the efficiency model for the team — 14.8 LoC per premium request with zero PR overhead suggests focused, output-oriented agent sessions.

---

### Tier B — Strong on at Least One Metric (2 developers)

---

**mshnayderman | Mikhail Shnayderman** *(Alon Vax)*
- Int: 164 | LoC: 27,539 | %Acc: 27.8% | SuggEff: 60.79 | ReqEff: **5.1** | Premium: 5,452 | PRs: 2 (1 merged, 50%)
- **T1 (Agent-First): Strong** — 27,539 LoC is #4 on team; exceptional output. %Acc of 27.8% is above the 20–35% inline target, suggesting mixed inline + agent workflow.
- **T2: Moderate** — ReqEff 5.1 is below the >10 target. Premium (5,452) has held flat since CP8 (was 5,452 at Jun 8 — no increase in 11 days). This is a positive sign.
- Zero LoC movement since CP8 is a concern. Flat momentum across 11 days at #4 position suggests potential off-cycle or blockage.
- **Coaching note:** Strong quality signals (SuggEff: 60.79 — highest on team). Focus on reducing premium per session. Premium flatness (no new spend since Jun 8) is encouraging. Investigate zero LoC movement since CP8.

---

**rpawar-nice | Ritesh Pawar** *(Susovan Samal)* — Historical Efficiency Benchmark
- Int: 79 | LoC: 8,662 | %Acc: 7.6% | SuggEff: 60.15 | ReqEff: **9.9** | Premium: 879 | PRs: 0
- **T1 (Agent-First): Good** — 8,662 LoC at 79 interactions indicates high-output sessions.
- **T2: Near-Pass** — ReqEff 9.9 is just below the >10 threshold. Premium (879) is lean for cumulative total. At CP7-CP8 this user was the team's efficiency benchmark at ~60.1 ReqEff.
- Zero LoC movement since CP8 (8,662 = same as Jun 12). No new activity in 11 days. Prior breakout (+199% ReqEff CP6→CP7) has gone dormant.
- **Coaching note:** Historically the best-efficiency user in scope. The flat LoC since CP8 needs attention — confirm active status. With Q2 closing June 30, re-engagement now would be impactful. ReqEff of 9.9 narrowly misses Tier A — one active sprint would likely push it over.

---

### Tier C — Mixed Signals (8 developers)

---

**mfield1 | Matt Field** *(Swapnil Zade)*
- Int: 765 | LoC: 9,803 | %Acc: 5.8% | SuggEff: 12.12 | ReqEff: **3.1** | Premium: 3,133 | PRs: 33 (31 merged, 93.9%)
- **T1 (Agent-First): Good** — 9,803 LoC is #7 on team. Consistent production.
- **T2: Below target** — ReqEff 3.1 is well below >10. However, premium (3,133) is moderate and LoC output has held steady (+3 from CP8).
- 33 PRs with 93.9% merge rate is the strongest PR track record in the mid-tier. Active code reviewer (127 reviews).
- **Coaching note:** The T2 gap (ReqEff 3.1) is the primary improvement lever. High PR activity suggests productive engineering; Copilot efficiency just needs tuning. Reduce agent session length or refocus on code generation over Q&A/analysis.

---

**Vyankatesh95 | Vyankatesh Khadakkar** *(Swapnil Zade)*
- Int: 423 | LoC: 4,177 | %Acc: 34.1% | SuggEff: 30.27 | ReqEff: **1.0** | Premium: 4,118 | PRs: 16 (16 merged, 100%)
- **T1 (Agent-First): Good signal** — 34.1% accept rate (highest among non-special-role users with meaningful accepts) indicates highly relevant inline suggestions. 47 accepts from 138 code generations.
- **T2: Fail** — ReqEff 1.0 at exactly the boundary. 4,118 premium for 4,177 LoC is a near 1:1 ratio — the minimum possible ROI above zero.
- Zero LoC movement since CP8 (4,177 = same as Jun 12). 100% PR merge rate is strong.
- **Coaching note:** Strong T1 quality signal being undermined by premium volume. Investigate what agent sessions are consuming premium without producing LoC. With 423 interactions and high accept rate, the pattern suggests many exploratory/chat sessions mixed with inline coding. Shift ratio toward inline-first for remaining Q2.

---

**Vitthal-Nice | Vitthal Devkar** *(Susovan Samal)*
- Int: 175 | LoC: 2,683 | %Acc: 40.4% | SuggEff: 13.55 | ReqEff: **1.1** | Premium: 2,393 | PRs: 7 (7 merged, 100%) — PR Added: 27,436 lines
- **T1 (Agent-First): Excellent quality** — 40.4% accept rate (80 accepts from 198 code gen). Highest accept rate among in-scope developers.
- **T2: Weak** — ReqEff 1.1 reflects cumulative premium drag.
- PR Added Lines (27,436) is exceptionally high for only 7 PRs — large, substantive contributions. 100% merge rate.
- **Coaching note:** The quality of AI usage is excellent (40.4% accept). The efficiency concern is the cumulative premium load relative to LoC. New code contributions (PR adds of 27,436 lines) suggest meaningful work outside the AI metrics window. Likely a candidate for Tier B if premium is tightened.

---

**jkumbhar | Jyoti Kumbhar** *(Swapnil Zade)*
- Int: 244 | LoC: 1,880 | %Acc: 22.0% | SuggEff: 15.93 | ReqEff: **0.9** | Premium: 2,110 | PRs: 19 (12 merged, 63.2%) — TTM: 281h 35m
- **T1: Moderate** — 22% accept in range, 26 accepts from 118 code gen.
- **T2: Below threshold** — ReqEff 0.9 just under 1.0.
- PR merge rate (63.2%) and time to merge (281h) are below team average — suggests review backlog or PR quality issues.
- **Coaching note:** Metrics are borderline across the board. Focus on increasing LoC output per session and improving PR completeness to boost merge rate. Minimal growth from CP8 (+10 LoC) suggests underutilization.

---

**jayesh-rai | Jayesh Rai** *(Swapnil Zade)*
- Int: 153 | LoC: 2,712 | %Acc: 18.4% | SuggEff: 13.49 | ReqEff: **1.4** | Premium: 1,997 | PRs: 17 (17 merged, 100%) — TTM: 91h 27m
- **T1: Near-pass** — 18.4% accept approaching target range. 37 accepts from 201 code gen.
- **T2: Weak** — ReqEff 1.4 below target. Premium at 1,997 is approaching the 1,700 outlier threshold.
- 100% PR merge rate is excellent. Steady growth (+233 LoC from CP8).
- **Coaching note:** Good code delivery (all PRs merged). AI efficiency needs improvement. Monitor premium — at 1,997 it's just below the watch threshold; any additional agent sessions will push it into budget concern territory.

---

**moadzughul | Moad Alzughul** *(Swapnil Zade)*
- Int: 255 | LoC: 3,409 | %Acc: 2.4% | SuggEff: 9.19 | ReqEff: **1.1** | Premium: 3,072 | PRs: 45 (43 merged, 95.6%) — TTM: 361h 1m
- **T1 (Agent-First): Low output** — 3,409 LoC at 255 interactions is below expectation for Agent-First.
- **T2: Weak** — ReqEff 1.1 below target. Premium 3,072 for minimal LoC is poor ROI.
- Highest PR count (45) and excellent merge rate (95.6%). TTM 361h is very high — work items sit open for a long time.
- Zero LoC movement from CP8 signals no new AI-assisted coding activity in 11 days.
- **Coaching note:** Very active developer by PR volume but AI metrics are weak. High TTM (361h) may indicate large feature work. The AI usage pattern suggests non-code tasks (chat, Q&A, analysis) consuming premium budget. Refocus agent sessions on code generation output.

---

**abhijeetk268 | Abhijeet Kolhe** *(Swapnil Zade)*
- Int: 39 | LoC: 656 | %Acc: 29.6% | SuggEff: 24.30 | ReqEff: **1.5** | Premium: 451 | PRs: 53 (49 merged, 92.5%) — TTM: 13h 19m
- **T1: Strong quality** — 29.6% accept (8 accepts from 27 gen) at very small volume.
- **T2: Weak** — ReqEff 1.5 below target, though premium (451) is quite lean.
- Best TTM on team (13h 19m) and highest PR count (53 PRs, 49 merged). This developer is extremely productive in code delivery.
- Very low AI interaction count (39 sessions) — significant underutilization of Copilot given delivery pace.
- **Coaching note:** This user shows excellent coding throughput (53 PRs, best TTM). The AI quality signals are strong (29.6% accept, 24.3 SuggEff) but volume is tiny. Immediately increase Copilot usage — this user has the quality instincts to become Tier A with moderate increase in AI sessions.

---

**Akale23 | Amulya Kale** *(Susovan Samal)*
- Int: 266 | LoC: 2,472 | %Acc: 22.8% | SuggEff: 5.41 | ReqEff: **0.6** | Premium: 4,237 | PRs: 7 (6 merged, 85.7%) — TTM: 29h 26m
- **T1: Moderate** — 22.8% accept (104 accepts from 457 code gen). High accept count.
- **T2: Fail** — ReqEff 0.6 well below target. 4,237 premium for 2,472 LoC is significantly over-budget.
- Zero LoC growth from CP8. The premium increase from prior periods with no LoC growth worsened the ratio.
- **Coaching note:** Good T1 quality, but premium is consuming budget disproportionately. Investigate agent session patterns — 266 interactions at 4,237 premium means ~16 premium requests per interaction, suggesting long/complex agent calls. Target shorter, code-focused sessions.

---

### Tier D — Low Efficiency or Below Targets (11 developers)

---

**amol-salunkhe | Amol Salunkhe** *(Swapnil Zade)* — LoC Leader
- Int: 504 | LoC: **43,585** | %Acc: 1.5% | ReqEff: **2.2** | Premium: 20,170 | PRs: 8 (8 merged, 100%) — TTM: 2h 48m
- **T1 (Agent-First): Exceptional** — #1 LoC producer on team. 43,585 lines of code is dominant.
- **T2: Fail** — ReqEff 2.2. Premium of 20,170 is massive for LoC output. Were premium at 4,000-5,000, this would be Tier A/B.
- 100% PR merge rate and 2h 48m TTM are outstanding — fastest merges on team.
- Steady growth (+2,577 from CP8) shows continued production.
- **Rationale for D over E:** LoC output (43,585) is genuine and substantial. Unlike true E-tier crisis users who produce minimal code, this user is producing but at extreme cost. D assigned because both T1 LoC is strong but T2 (budget) is not supportable at scale.
- **Coaching note:** CRITICAL budget review. 20,170 premium requests for 43,585 LoC = excellent absolute output but a 4.6x higher spend than the ideal budget for this volume. Investigate whether agent sessions include non-code tasks. If LoC is genuine, make the ROI case to VP — otherwise premium must be contained.

---

**Prathmesh-Ranadive | Prathmesh Ranadive** *(Swapnil Zade)* — Biggest CP9 Gainer
- Int: 105 | LoC: **35,091** | %Acc: 88.7% | SuggEff: 19.90 | ReqEff: **1.1** | Premium: 31,420 | PRs: 24 (24 merged, 100%) — TTM: 16h 5m
- **T1 (Agent-First): Exceptional** — 35,091 LoC, +8,039 from CP8 (BIGGEST gainer). 88.7% accept rate (1,563 accepts from 1,763 code gen) is extraordinary — highest accept rate with high volume anywhere on the team.
- **T2: Fail** — ReqEff 1.1. Premium (31,420) is the #5 highest spend on team.
- 24/24 PRs merged (100%) with 16h 5m TTM — excellent delivery cadence.
- **Rationale for D over E:** The 88.7% accept rate and 1,563 code accepts represent enormous genuine productivity. The premium concern is real but 35,091 LoC is meaningful offsetting output.
- **Coaching note:** Highest-quality AI output signals on team (88.7% accept). The budget concern is systemic, not a behavior problem — this user is clearly generating code at scale. Work with management to evaluate whether the 31,420 premium spend is justified by the code volume. If ROI calculation uses hourly dev rate, this may be justifiable.

---

**luisalvatierra | Luis Salvatierra** *(Swapnil Zade)*
- Int: 629 | LoC: 12,080 | %Acc: 24.2% | SuggEff: 13.33 | ReqEff: **1.3** | Premium: 9,542 | PRs: 12 (10 merged, 83.3%) — TTM: 137h 46m
- **T1 (Agent-First): Good** — 12,080 LoC, solid at #5 on team. +2,603 from CP8 is strong growth.
- **T2: Fail** — ReqEff 1.3. Premium (9,542) is above budget threshold.
- **Coaching note:** Good LoC trajectory but premium is running ahead of output. 24.2% accept rate is in target range. Need to reduce agent session cost — TTM (137h) suggests complex features being built; agent sessions may include design/planning overhead that isn't captured as LoC.

---

**chris-haun | Chris Haun** *(Swapnil Zade)* — Highest Interaction Count
- Int: **1,643** | LoC: 10,493 | %Acc: 9.3% | SuggEff: 7.72 | ReqEff: **0.8** | Premium: 12,535 | PRs: 47 (45 merged, 95.7%) — TTM: 81h 49m
- **T1 (Agent-First): Weak** — 1,643 interactions yielding only 10,493 LoC. 6.4 LoC per interaction is below expectation for Agent-First.
- **T2: Fail** — ReqEff 0.8 below 1.0. Premium (12,535) is 6th highest on team.
- 47 PRs, 45 merged (95.7%) — strong code delivery.
- **Coaching note:** Highest interaction count on team (1,643) with middling LoC output suggests many short/exploratory sessions. Consolidate to longer, output-focused agent sessions. The PR record shows strong delivery — AI efficiency is the gap, not code quality.

---

**vishal-tad | Vishal Tad** *(Susovan Samal)*
- Int: 486 | LoC: 3,737 | %Acc: 8.8% | SuggEff: 4.19 | ReqEff: **0.4** | Premium: 9,301 | PRs: 17 (15 merged, 88.2%) — TTM: 32h 37m
- **T1 (Agent-First): Low** — 3,737 LoC at 486 interactions is underperforming.
- **T2: Fail** — ReqEff 0.4. Premium (9,301) is significantly above outlier threshold.
- **Coaching note:** Both T1 and T2 are weak for an Agent-First user with 486 interactions. SuggEff of 4.19 is among the lowest on team. Investigate session types — high premium with low LoC/SuggEff suggests extensive chat/Q&A usage rather than code generation.

---

**abhishekhole-nice | Abhishek Hole** *(Swapnil Zade)*
- Int: 252 | LoC: 3,150 | %Acc: 3.2% | SuggEff: 33.16 | ReqEff: **0.7** | Premium: 4,416 | PRs: 14 (14 merged, 100%) — TTM: 16h 26m
- **T1 (Agent-First): Low-moderate** — 3,150 LoC, modest growth (+157 from CP8). SuggEff 33.16 is strong.
- **T2: Fail** — ReqEff 0.7. Premium (4,416) is running well ahead of LoC.
- 100% PR merge rate and fast TTM (16h) are positives.
- **Coaching note:** Good PR delivery and suggestion efficiency signal (33.16 SuggEff). Agent sessions appear productive per interaction but premium total is accumulating. Tighten session discipline for Q2 close.

---

**suhas-kakde | Suhas Kakde** *(Swapnil Zade)*
- Int: 194 | LoC: 2,005 | %Acc: 1.7% | SuggEff: 8.39 | ReqEff: **0.7** | Premium: 2,797 | PRs: 29 (27 merged, 93.1%) — TTM: 111h 56m
- **T1 (Agent-First): Low** — 2,005 LoC at 194 interactions. 1.7% accept is very low even for Agent-First.
- **T2: Fail** — ReqEff 0.7 below 1.0.
- **Coaching note:** Moderate PR activity (29 PRs, 93.1% merge rate) suggests active developer. AI adoption is low quality. Increase LoC output per session and review accept rate — 4 accepts from 239 code gen suggests many suggestions are off-target.

---

**meghabiradar05 | Megha Biradar** *(Swapnil Zade)*
- Int: 128 | LoC: 1,727 | %Acc: 12.5% | SuggEff: 8.30 | ReqEff: **0.2** | Premium: 10,131 | PRs: 5 (5 merged, 100%) — TTM: 217h 26m
- **T1 (Agent-First): Low** — 1,727 LoC at 128 interactions.
- **T2: Fail** — ReqEff 0.2. Premium (10,131) is critically high for this LoC volume.
- **Coaching note:** 10,131 premium for 1,727 LoC is approaching crisis territory. 5 PRs with 217h TTM suggests work on complex/long-cycle features. Budget intervention needed before Q2 close.

---

**giteshsawant | Gitesh Sawant** *(Susovan Samal)*
- Int: 236 | LoC: 1,369 | %Acc: 2.2% | SuggEff: 15.38 | ReqEff: **0.2** | Premium: 8,585 | PRs: 1 (0 merged, 0%) — TTM: 19h 34m
- **T1 (Agent-First): Low** — 1,369 LoC at 236 interactions. Growing (was 1,110 at CP8, +259).
- **T2: Fail** — ReqEff 0.2. Premium (8,585) is high for cumulative output.
- Only 1 PR opened, 0 merged. Low code delivery signal.
- **Coaching note:** Growing LoC trend is positive. Premium is the concern — 8,585 requests generating minimal code. Pair with a senior agent user to learn efficient session techniques before Q2 ends.

---

**dsuraj25 | Suraj Dubey** *(Susovan Samal)*
- Int: 21 | LoC: 1,169 | %Acc: 33.3% | SuggEff: 12.57 | ReqEff: **0.1** | Premium: 9,893 | PRs: 1 (1 merged, 100%)
- **T1 (Agent-First): Limited data** — 21 interactions is very low; 33.3% accept and 1,169 LoC suggest quality when used.
- **T2: Fail** — ReqEff 0.1 is near-zero. 9,893 premium for 1,169 LoC. Most of the premium appears from agent overhead, not code generation.
- **Coaching note:** Quality signals (33.3% accept) are good. The premium pattern — 9,893 requests from only 21 interactions — implies very long agent sessions or agentic workflow overhead. Investigate session logs.

---

**pratikpawar12 | Pratik Pawar** *(Swapnil Zade)*
- Int: 116 | LoC: 250 | %Acc: 4.1% | SuggEff: 2.03 | ReqEff: **0.3** | Premium: 815 | PRs: 9 (9 merged, 100%) — TTM: 2h 16m
- **T1 (Agent-First): Very low** — 250 LoC. Near-negligible AI code output.
- **T2: Fail** — ReqEff 0.3. 815 premium requests generating only 250 LoC.
- 9/9 PRs merged with excellent TTM (2h 16m, 2nd fastest on team). Active developer but Copilot largely unused for code.
- **Coaching note:** Fastest-merging developer alongside amol-salunkhe. Very likely using Copilot for code review/chat rather than generation. 116 interactions with only 250 LoC confirms this. Redirect to code generation sessions.

---

### Tier E — Budget Crisis or Zero Activity (12 active crisis + 5 zero/negligible)

#### Active Budget Crisis (12 developers)

---

**nilesht-19 | Nilesh Tonape** *(Swapnil Zade)* — Persistent Crisis Since CP6
- Int: 1,244 | LoC: 7,354 | %Acc: 30.2% | ReqEff: **0.2** | Premium: **32,332** | PRs: 20 (18 merged, 90%)
- **Crisis:** 32,332 premium requests for 7,354 LoC. ReqEff = 0.23. Flagged every checkpoint since CP6.
- Minimal growth since CP8 (+8 LoC). Premium continues accumulating.
- **Action:** Escalate to VP R&D. Prior coaching interventions have not reduced premium spend. Consider temporary access restriction or premium cap enforcement.

---

**Kranti-nice | Kranti Kaple** *(Swapnil Zade)* — Exploded CP8→CP9
- Int: 1,430 | LoC: 37,978 | %Acc: 4.6% | ReqEff: **1.1** | Premium: **35,537** | PRs: 22 (16 merged, 72.7%) — TTM: 60h 28m
- **Crisis:** Premium tripled in 11 days (11,979 at CP8 → 35,537). LoC grew +6,333 but not proportionally.
- Highest interaction count on team (1,430). LoC output is legitimate (#2 on team) but budget is spiraling.
- **Action:** Immediate manager conversation (SwapnilNice). The LoC output is real — this is not waste in the traditional sense, but the premium burn rate is unsustainable. Investigate whether long agent chains are multiplying premium counts.

---

**tusharpatil166719 | Tushar Patil** *(Susovan Samal)* — NEW #1 Budget Crisis
- Int: 122 | LoC: 2,200 | %Acc: 14.7% | ReqEff: **0.06** | Premium: **35,886** | PRs: 4 (4 merged, 100%)
- **Crisis:** 35,886 premium requests for 2,200 LoC. ReqEff = 0.06. WORST ratio in team history.
- 122 interactions generating 35,886 premium = ~294 premium requests per interaction. Suggests automated agent loops or recursive planning sessions.
- **Action:** IMMEDIATE escalation. Block or restrict access pending investigation. 294 premium/interaction ratio is anomalous and suggests misuse pattern (automated agents, infinite loops, or bulk processing sessions).

---

**PradnyeshSalunke | Pradnyesh Salunke** *(Swapnil Zade)*
- Int: 664 | LoC: 4,237 | %Acc: 19.4% | ReqEff: **0.2** | Premium: **20,544** | PRs: 8 (8 merged, 100%)
- **Crisis:** 20,544 premium for 4,237 LoC. Persistent since CP7. Minimal improvement.
- **Action:** Coaching has not worked. Enforce session length limits or daily premium caps.

---

**mshivarkar | Mohan Shivarkar** *(Swapnil Zade)* — Doubled LoC, Premium Still High
- Int: 681 | LoC: 4,201 | %Acc: 9.4% | ReqEff: **0.2** | Premium: **17,029** | PRs: 11 (11 merged, 100%)
- **Crisis:** LoC doubled (+2,104 from CP8) — the most improved LoC growth among crisis users. However, premium (17,029) is disproportionate.
- 100% PR merge rate. Active and productive developer.
- **Action:** Acknowledge LoC improvement. Focus coaching specifically on premium-per-session reduction. This user may naturally improve ReqEff as they produce more code.

---

**sskalaskar | Sourabh Kalaskar** *(Swapnil Zade)*
- Int: 367 | LoC: 3,233 | %Acc: 16.9% | ReqEff: **0.2** | Premium: **16,897** | PRs: 15 (13 merged, 86.7%)
- **Crisis:** 16,897 premium for 3,233 LoC. Growing (+535 LoC from CP8) but premium growing faster.
- **Action:** Budget cap coaching. Premium growth is outpacing LoC — trend is worsening.

---

**trunalgawade | Trunal Gawade** *(Susovan Samal)*
- Int: 389 | LoC: 2,352 | %Acc: 20.4% | ReqEff: **0.1** | Premium: **18,720** | PRs: 1 (1 merged, 100%)
- **Crisis:** 18,720 premium for 2,352 LoC. ReqEff = 0.13. Chronic — flagged every checkpoint since CP6.
- **Action:** Escalate. 389 interactions for 18,720 premium = 48 premium/interaction. Pattern similar to tusharpatil. Investigate session types.

---

**Shreedevi-nice | Shreedevi Patil** *(Swapnil Zade)*
- Int: 232 | LoC: 1,886 | %Acc: 8.8% | ReqEff: **0.2** | Premium: **12,071** | PRs: 15 (14 merged, 93.3%)
- **Crisis:** 12,071 premium for 1,886 LoC. No meaningful LoC growth from CP8 (+100 lines).
- SuggEff 55.47 is very high — when suggestions ARE accepted, they're high-quality.
- **Action:** Good PR delivery (93.3% merge rate). AI sessions are producing quality but at extreme cost. Limit agent session length and frequency.

---

**prashasti-jain | Prashasti Jain** *(Swapnil Zade)*
- Int: 202 | LoC: 1,562 | %Acc: 7.2% | ReqEff: **0.1** | Premium: **12,206** | PRs: 8 (7 merged, 87.5%) — TTM: 111h 27m
- **Crisis:** 12,206 premium for 1,562 LoC. ReqEff = 0.13.
- **Action:** Premium intervention. 202 interactions at 12,206 premium = 60 premium/interaction. Very high overhead.

---

**pdevle | Pratik Devle** *(Susovan Samal)*
- Int: 110 | LoC: 1,478 | %Acc: 6.3% | ReqEff: **0.1** | Premium: **10,057** | PRs: 7 (7 merged, 100%) — TTM: 25h 43m
- **Crisis:** 10,057 premium for 1,478 LoC. ReqEff = 0.15.
- 100% PR merge rate with reasonable TTM.
- **Action:** Premium intervention. Modest LoC growth (+94 from CP8) is positive but premium is 6.8x the outlier threshold.

---

**thakraln | Nishtha Thakral** *(Susovan Samal)*
- Int: 215 | LoC: 806 | %Acc: 0.0% | SuggEff: 8.96 | ReqEff: **0.1** | Premium: **13,562** | PRs: 0
- **Crisis:** 13,562 premium requests. 0 code accepts. 0 PRs. LoC 806.
- Flagged since CP6. No improvement across multiple checkpoints.
- **Action:** IMMEDIATE escalation. Zero code accepts + zero PRs across entire program period = no measurable code delivery. This is the most extreme waste case for non-code output. Consider access suspension.

---

**Shubhamfulzele28 | Shubham Fulzele** *(Swapnil Zade)* — NOT in CP9 dataset, tracked from prior period
- LoC: 1,043 | Premium: **29,049** | ReqEff: **0.04** (estimated from prior period tracking)
- **Crisis:** Premium doubled from CP8 (13,831 → 29,049). Worst non-tusharpatil ROI.
- **Action:** IMMEDIATE. Access restriction recommended pending investigation. 29,049 premium for 1,043 LoC is catastrophic by any measure.

---

#### Zero / Negligible Activity (5 developers)

| Login | Name | LoC | Premium | PRs | Notes |
|---|---|---|---|---|---|
| mohitbaghelnice | Mohit Baghel | 3 | 2,393 | 1 merged | Near-zero AI output; premium from prior period accumulation |
| amol-doke | Amol Doke | 10 | 2,528 | 8 opened (4 merged) | Negligible AI output; 50% PR merge rate concerns |
| ssnikam | Sanket Nikam | **0** | **0** | 55 opened (49 merged) | **Zero AI usage** — see special note below |
| kbajaj-nice | Kaushal Bajaj | 5 | 6 | 2 merged | Minimal interaction; lean premium |
| dannycadima | Danny Cadima Molina | 34 | 3 | 0 PRs | Near-zero; premium essentially zero — low concern |

---

## Special Note — ssnikam (Sanket Nikam): Developer Without Copilot

**ssnikam | Sanket Nikam** *(Susovan Samal)*

Sanket Nikam has ZERO GitHub Copilot activity — no interactions, no LoC, no premium consumption — yet is one of the most active code contributors on the team by raw delivery metrics:

| Metric | Value |
|---|---|
| Copilot Interactions | 0 |
| Copilot LoC Added | 0 |
| Premium Requests | 0 |
| PRs Opened | 55 |
| PRs Merged | 49 |
| PR Merge Rate | 89.1% |
| PR Added Lines | 933 |
| PR Time to Merge | 42h 2m |

55 PRs opened and 49 merged (89.1% merge rate) puts ssnikam in the **top 3 by PR volume** for the entire team, alongside abhijeetk268 (53 PRs) and moadzughul (45 PRs). He is clearly an active, productive developer.

**This is a critical coaching target.** A developer with proven code delivery velocity and zero AI adoption represents the highest-leverage onboarding opportunity on the team. Conservative estimate: if ssnikam adopts Copilot at even Tier C efficiency (ReqEff ~1.0, ~2,000 LoC/month), this adds ~2,000 LoC to team output monthly at no additional headcount cost.

**Recommended action:** Priority onboarding session with ssnikam. Schedule within this week (before Q2 closes Jun 30). Manager: ssamal-nice (Susovan Samal).

---

## Executive Scorecard

| Tier | Count | % of 37 Devs | LoC (approx) | Key Names |
|---|---|---|---|---|
| A | 1 | 2.7% | 5,013 (2%) | copilotshree (non-CX) |
| B | 2 | 5.4% | 36,201 (14%) | mshnayderman, rpawar-nice |
| C | 8 | 21.6% | 28,509 (11%) | mfield1, Vyankatesh95, Vitthal-Nice, jayesh-rai, moadzughul, jkumbhar, Akale23, abhijeetk268 |
| D | 11 | 29.7% | 116,734 (46%) | amol-salunkhe, Prathmesh-Ranadive, luisalvatierra, chris-haun, vishal-tad, abhishekhole-nice, suhas-kakde, meghabiradar05, giteshsawant, dsuraj25, pratikpawar12 |
| E (Active Crisis) | 12 | 32.4% | 63,966 (25%) | nilesht-19, Kranti-nice, tusharpatil166719, PradnyeshSalunke, mshivarkar, sskalaskar, trunalgawade, Shreedevi-nice, prashasti-jain, pdevle, thakraln, Shubhamfulzele28 |
| E (Zero/Negligible) | 5 | 13.5% | 52 (~0%) | mohitbaghelnice, amol-doke, ssnikam, kbajaj-nice, dannycadima |

**Summary:**
- Only **1 developer (2.7%)** is at Tier A — the team efficiency benchmark is critically low
- **35.1% (13 developers)** are at Tier E — the highest E-tier count in the program's history
- **46% of team LoC** comes from D-tier developers — high output at unsustainable cost
- Top 3 LoC producers (amol-salunkhe, Kranti-nice, Prathmesh-Ranadive) are all D or E tier — output is real but budget is crisis

### Tier Distribution vs. CP8

| Tier | CP8 | CP9 | Delta |
|---|---|---|---|
| A | 6 | 1 | −5 (Tier collapse) |
| B | 3 | 2 | −1 |
| C | 5 | 8 | +3 |
| D | 6 | 11 | +5 |
| E | 15 | 17 | +2 |

> **Interpretation:** The dramatic Tier A collapse (6 → 1) reflects the application of the Agent-First exception uniformly combined with cumulative premium growth. Users who were Tier A in CP8 on LoC volume but have accumulated high premium since program start have slid to D/E under the cumulative ReqEff calculation.

---

## 80/20 Analysis

### LoC Concentration

Top 20% of 37 developers = **7–8 users**

| Rank | Login | Name | LoC | Cumulative LoC | % of Team Total |
|---|---|---|---|---|---|
| 1 | amol-salunkhe | Amol Salunkhe | 43,585 | 43,585 | 17.0% |
| 2 | Kranti-nice | Kranti Kaple | 37,978 | 81,563 | 31.9% |
| 3 | Prathmesh-Ranadive | Prathmesh Ranadive | 35,091 | 116,654 | 45.6% |
| 4 | mshnayderman | Mikhail Shnayderman | 27,539 | 144,193 | 56.3% |
| 5 | luisalvatierra | Luis Salvatierra | 12,080 | 156,273 | 61.0% |
| 6 | chris-haun | Chris Haun | 10,493 | 166,766 | 65.1% |
| 7 | mfield1 | Matt Field | 9,803 | 176,569 | 68.9% |
| 8 | rpawar-nice | Ritesh Pawar | 8,662 | 185,231 | 72.4% |

**Top 8 users (22% of team) produce 72.4% of total LoC** — well exceeding the 80/20 rule threshold in the opposite direction. LoC production is highly concentrated.

**Remaining 29 users produce only 27.6% of total LoC** (~70,769 LoC across 29 developers).

### Premium Concentration

Top 5 premium consumers account for estimated **~164,000+ premium requests** out of the team total — representing potentially 60%+ of all premium spend.

### Implication

The 80/20 reality for WFM Integrations is that **8 developers are doing 72% of AI-assisted coding**, but **3 of those 8 are in Tier D/E** due to premium costs. Coaching the bottom 29 users to match even Tier C performance could nearly double effective team output at marginal incremental cost.

---

## Q2 Closing Assessment — 7 Days Remaining (Jun 23 → Jun 30)

**Q2 ends June 30, 2026. Current checkpoint: CP9 (June 23). 7 days remain.**

### Q2 Current State

| Dimension | Status | Assessment |
|---|---|---|
| LoC Volume | ~256,000 cumulative | Strong total output — LoC goal likely met |
| Budget Health | Critical — 9 users at crisis level | Unsustainable spend pattern |
| Tier A Users | 1 (copilotshree, non-CX) | Zero CX developers at Tier A |
| Team ReqEff | ~1.8 average | Well below the >10 target |
| Onboarding Gap | ssnikam + 4 others never started | Late-Q2 risk |

### What Can Still Change Before Jun 30

**Positive scenarios (achievable in 7 days):**
1. **ssnikam onboarding** — One active week could generate 500–1,000 LoC at good efficiency. Flag for manager (ssamal-nice) today.
2. **abhijeetk268 scale-up** — Already at 29.6% accept rate with lean premium. Doubling interactions this week could push to Tier B/A.
3. **rpawar-nice re-engagement** — Was the team's efficiency benchmark. Zero movement since CP8 but premium is lean. One active week would likely restore Tier A status.
4. **mshnayderman LoC push** — Zero movement since CP8 (Jun 12). Strong accept rate and SuggEff. Re-engaging would lift team LoC totals and tier picture.

**Crisis scenarios (will worsen without intervention):**
1. **tusharpatil166719** — At 294 premium/interaction, 7 more active days could add 50,000+ premium requests. Access restriction now is the prudent action.
2. **Kranti-nice** — If the pattern that tripled premium in 11 days continues, Q2 close could see 50,000+ premium. Manager conversation immediately.
3. **thakraln** — Zero accepts, zero PRs, 13,562 premium. No upside scenario possible in 7 days. Recommend access suspension.

### Q2 Recommended Actions (This Week)

| Priority | Action | Owner | Timeline |
|---|---|---|---|
| P0 | Restrict/suspend tusharpatil166719 pending investigation | ssamal-nice | Today |
| P0 | Manager 1:1 with Kranti Kaple on agent session discipline | SwapnilNice | Today |
| P0 | Escalate Shubhamfulzele28 to VP R&D | SwapnilNice | Today |
| P0 | Suspend or cap thakraln access (zero delivery + 13K premium) | ssamal-nice | Today |
| P1 | Onboard ssnikam — first Copilot session | ssamal-nice | This week |
| P1 | Re-engage rpawar-nice — confirm active status | ssamal-nice | This week |
| P1 | Coach abhijeetk268 to double interaction volume | SwapnilNice | This week |
| P2 | Session-length coaching for trunalgawade, pdevle, prashasti-jain | ssamal-nice | Before Jun 30 |
| P2 | Budget review for amol-salunkhe with VP context | SwapnilNice | Before Jun 30 |

### Q2 Closing Forecast

If no intervention occurs: Team LoC will grow modestly (~5–10%) but premium will continue accelerating. End-of-Q2 budget picture will show several users exceeding 40,000–50,000 lifetime premium with ReqEff below 0.5.

If interventions implemented: Budget crisis users contained, 2–3 underutilizing developers (ssnikam, abhijeetk268, rpawar-nice) activated. Realistic improvement: 2,000–5,000 additional LoC at good efficiency, 10–15% reduction in weekly premium burn rate.

---

## Coaching Priority Summary

### IMMEDIATE (Before End of Day)
1. **tusharpatil166719** — 294 premium/interaction. Anomalous pattern. Access restriction pending investigation.
2. **Kranti-nice** — Premium tripled in 11 days. Manager conversation required immediately.
3. **Shubhamfulzele28** — Doubled crisis spend. VP R&D escalation.
4. **thakraln** — Zero code delivery. Access suspension warranted.

### THIS WEEK
5. **ssnikam** — Onboard immediately. Highest-leverage untapped asset on team.
6. **rpawar-nice** — Re-engage. Was efficiency benchmark, now inactive 11 days.
7. **abhijeetk268** — Scale up interaction count. Quality signals are excellent.

### NEXT CHECKPOINT (CP10 — target ~Jul 3–7, post-Q2 close)
8. **mshivarkar** — Monitor LoC growth vs. premium. Doubled LoC is positive; if trend continues ReqEff improves naturally.
9. **amol-salunkhe** — Full budget-vs-output ROI review with management.
10. **luisalvatierra** — Premium growth trending concern. Will cross 10,000 threshold soon.

---

*v1 Standard Framework — CP9 (9th checkpoint). Data sync: June 23, 2026. PR data through June 21, 2026. 16 users excluded per ignore list (tomotvos, dhanshree-jagtap-nice, sohanbafna, GovindSomaniNice, rizeq-abu-madeghem, nice-harshada, yogitadhanwate, AnaSarzosa, sachinfuse-nice, anjali-sherikar, ShivrajNice, prashant-shete, rajivranjannice, BireshwarNice, prinice251, ak-nice-2025). All in-scope developers have Used Agents = 1; Agent-First exception applied universally. Q2 closes June 30, 2026.*
