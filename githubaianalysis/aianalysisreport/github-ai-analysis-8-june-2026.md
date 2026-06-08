# GitHub Copilot Usage Analysis — v1 Standard Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Scope:** 45 users (15 excluded per ignore list — see `githun-ignored-users.md`) | **Framework:** v1 Standard

---

## What Changed vs Prior Period (June 3, 2026)

| Signal | Jun 3 | Jun 8 (scoped) | Delta |
|---|---|---|---|
| Active Users (in scope) | ~38 | ~41 | +3 |
| LoC Added (in scope) | ~200,000 | ~215,026 | +8% |
| Accept Rate (in scope) | ~16% | ~20.2% | +4.2pp |
| mshnayderman ReqEff | 43.2 | 5.1 | 🔴 −88% |
| amol-salunkhe ReqEff | 40.8 | 6.4 | 🔴 −84% |
| rpawar-nice ReqEff | 20.1 | ~60.1 | 🚀 +199% |
| Kranti-nice ReqEff | ~7.6 | ~23.1 | 🚀 Breakout |

> **Scope note:** This analysis excludes 15 users per the permanent ignore list. Raw Power BI dashboard totals cover all 60 users; figures above are adjusted for in-scope users only.

**Key themes this period:**
1. **amol-salunkhe is new LoC leader** — 34,037 lines in scope (after dhanshree-jagtap-nice excluded). Tier A on volume despite efficiency collapse.
2. **Budget crisis — 5 accounts** — nilesht-19 (23,108 premium), thakraln (11,112), trunalgawade (10,863), Prathmesh-Ranadive (10,733), PradnyeshSalunke (9,892). Combined 65,708 premium requests generating low LoC.
3. **mshnayderman anomaly** — 9.5× premium spike (565 → 5,419) with only modest LoC gain. Tier A retained on accept rate strength; CRQC demotes to C.
4. **Two breakout coaching wins** — rpawar-nice (+199% ReqEff) and Kranti-nice (+204%).

---

## Team Overview (In-Scope Users Only)

| Metric | Value |
|---|---|
| Initiated Interactions | ~11,758 |
| LoC Added | ~215,026 |
| Code Acceptance Count | ~2,554 |
| Code Generation Count | ~12,609 |
| % Code Acceptance | ~20.2% |
| Suggestion Efficiency | ~17.1 |
| In-Scope Active Users | ~41 / 45 |
| Excluded (ignore list) | 15 |

---

## User Classification

### Special Groups (Excluded from A–E Tier)

**Inactive (0 activity this period — in scope):**
> ak-nice-2025, amoldoke051295, mohitbaghelnice, ssnikam

**Research (not tiered — tracked on Interactions + Premium only):**
| Login | Name | Manager | Interactions | LoC Added | Premium | Notes |
|---|---|---|---|---|---|---|
| rwalunj-nice | Rahul Walunj | Alon Vax | ~30 | 0 | ~100 | Research/tooling exploration |

**Managers (benchmarked on engagement + efficiency, not raw LoC):**
| Login | Name | Manager | Int | LoC Added | % Accept | ReqEff | Notes |
|---|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | Rahul Walunj | 273 | 3,140 | 4.0% | ~31.4 | Active coder-manager |
| ssamal-nice | Susovan Samal | Rahul Walunj | ~30 | 38 | ~8% | ~3.2 | Low engagement |

**Non-CX Engineering Members (tracked separately):**
| Login | Name | Manager | Int | LoC Added | % Accept | ReqEff | Notes |
|---|---|---|---|---|---|---|---|
| copilotshree | Shraddha Kale | Swapnil Zade | ~750 | 5,013 | ~4.8% | ~8.8 | Non-CX — not tiered with CX team |

---

## Full Developer Metrics Table (37 Developers)

> **Column key:** Int = Initiated Interactions | LoC = LoC Added | %Acc = % Code Acceptance | SuggEff = Suggestion Efficiency | Premium = Premium Requests | ReqEff = Request Efficiency (LoC/Premium)
> **Workflow inference:** Agent-First = %Acc < 5% + Int ≥ 50 + LoC ≥ 500 | Inline-First = %Acc ≥ 25% | Hybrid = others

| Login | Name | Manager | Int | LoC | %Acc | SuggEff | Premium | ReqEff | Workflow | v1 Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | Swapnil Zade | 423 | 34,037 | 1.6% | 29.42 | 5,309 | 6.4 | Agent-First | **A** ⚠️ |
| Kranti-nice | Kranti Kaple | Swapnil Zade | 1,182 | 27,733 | 1.3% | 39.01 | ~1,200 | ~23.1 | Agent-First | **A** |
| mshnayderman | Mikhail Shnayderman | Alon Vax | 164 | 27,539 | 27.8% | 60.79 | 5,419 | 5.1 | Inline-First | **A** ⚠️ |
| Prathmesh-Ranadive | Prathmesh Ranadive | Swapnil Zade | ~100 | 27,052 | 25.4% | ~25 | 10,733 | 2.5 | Inline-First | **C** |
| mfield1 | Matt Field | Swapnil Zade | ~600 | ~9,300 | ~5.5% | ~14.3 | ~650 | ~14.3 | Hybrid | **A** |
| chris-haun | Chris Haun | Swapnil Zade | ~1,000 | ~10,359 | ~11.7% | ~10.4 | ~3,700 | 2.8 | Hybrid | **C** |
| rpawar-nice | Ritesh Pawar | S. Samal | 77 | 8,662 | 7.7% | 60.57 | ~144 | ~60.1 | Hybrid | **A** |
| nilesht-19 | Nilesh Tonape | Swapnil Zade | 1,140 | 7,160 | 29.5% | ~18.2 | 23,108 | 0.3 | Inline-First | **E** |
| copilotshree* | Shraddha Kale | Swapnil Zade | ~750 | 5,013 | ~4.8% | ~8.8 | ~570 | ~8.8 | Agent-First | *Non-CX* |
| luisalvatierra | Luis Salvatierra | Swapnil Zade | ~480 | ~4,800 | ~17.6% | ~9.2 | ~1,655 | 2.9 | Hybrid | **B** |
| Vyankatesh95 | Vyankatesh Khadakkar | Swapnil Zade | 423 | 4,177 | 34.1% | 30.27 | ~150 | ~27.8 | Inline-First | **C** |
| SwapnilNice* | Swapnil Zade | Rahul Walunj | 273 | 3,140 | 4.0% | 31.40 | ~100 | ~31.4 | Agent-First | *Manager* |
| moadzughul | Moad Alzughul | Swapnil Zade | ~130 | ~3,100 | ~2.8% | ~14.8 | ~210 | ~14.8 | Agent-First | **D** |
| abhishekhole-nice | Abhishek Hole | Swapnil Zade | 167 | 2,936 | 0.0% | 53.38 | ~170 | ~17.3 | Agent-First | **D** |
| vishal-tad | Vishal Tad | Swapnil Zade | ~30 | ~2,900 | ~4.8% | ~23.2 | ~125 | ~23.2 | Hybrid | **D** |
| PradnyeshSalunke | Pradnyesh Salunke | Swapnil Zade | ~320 | ~2,968 | ~25.4% | ~16.5 | 9,892 | 0.3 | Inline-First | **E** |
| mshivarkar | Mohan Shivarkar | Swapnil Zade | ~100 | 2,018 | ~22% | ~40.4 | 3,480 | 0.6 | Hybrid | **D** |
| Vitthal-Nice | Vitthal Devkar | S. Samal | ~160 | ~2,800 | ~44% | ~14 | ~200 | ~14 | Inline-First | **A** |
| jkumbhar | Jyoti Kumbhar | Swapnil Zade | ~230 | ~2,000 | ~20% | ~20 | ~120 | ~16.7 | Hybrid | **C** |
| Akale23 | Amulya Kale | S. Samal | ~200 | ~2,600 | ~18.8% | ~6.7 | ~390 | ~6.7 | Hybrid | **A** |
| jayesh-rai | Jayesh Rai | Swapnil Zade | ~90 | ~2,500 | ~4% | ~19 | ~130 | ~19.2 | Agent-First | **B** |
| ~sskalaskar | Sourabh Kalaskar | Swapnil Zade | ~190 | ~2,700 | ~15% | ~33.8 | ~85 | ~31.8 | Hybrid | **E** |
| suhas-kakde | Suhas Kakde | Swapnil Zade | ~190 | 1,639 | ~1.8% | ~6.3 | ~265 | ~6.2 | Agent-First | **E** |
| Shreedevi-nice | Shreedevi Patil | Swapnil Zade | 195 | 1,416 | 11.1% | 52.44 | ~200 | ~7.1 | Hybrid | **E** |
| trunalgawade | Trunal Gawade | S. Samal | ~120 | ~1,086 | ~23% | ~3.9 | 10,863 | 0.1 | Hybrid | **E** |
| thakraln | Nishtha Thakral | S. Samal | ~80 | ~1,111 | 0.0% | ~55.6 | 11,112 | 0.1 | Agent-First | **E** |
| ~prashasti-jain | Prashasti Jain | Swapnil Zade | ~30 | ~900 | ~8% | ~25.7 | ~35 | ~25.7 | Hybrid | **E** |
| tusharpatil166719 | Tushar Patil | S. Samal | ~75 | ~1,900 | ~12% | ~19 | ~100 | ~19 | Hybrid | **D** |
| meghabiradar05 | Megha Biradar | Swapnil Zade | ~55 | ~1,700 | ~5.5% | ~15.5 | ~110 | ~15.5 | Hybrid | **D** |
| ShubhamFulzele28 | Shubham Fulzele | Swapnil Zade | 117 | 739 | 0.0% | 52.79 | ~120 | ~6.2 | Agent-First | **E** |
| abhijeetk268 | Abhijeet Kolhe | Swapnil Zade | 38 | 656 | 29.6% | 24.30 | ~30 | ~21.9 | Inline-First | **C** |
| smishra-nice | Shridhar Mishra | Rahul Walunj | ~80 | 155 | 78.3% | 6.74 | ~25 | ~6.2 | Inline-First | **D** |
| pdevle | Pratik Devle | S. Samal | ~35 | ~1,100 | ~7% | ~15.7 | ~70 | ~15.7 | Hybrid | **D** |
| dsuraj25 | Suraj Dubey | S. Samal | ~15 | ~510 | 0.0% | ~14.6 | ~35 | ~14.6 | Hybrid | **C** |
| sgite-wfm | Shubham Gite | S. Samal | ~35 | 329 | 53.5% | ~0.94 | 1,411 | 0.2 | Inline-First | **D** |
| pratikpawar12 | Pratik Pawar | Swapnil Zade | ~115 | 250 | ~4.2% | ~1.8 | ~140 | ~1.8 | Hybrid | **E** |
| kbajaj-nice | Kaushal Bajaj | S. Samal | ~5 | 5 | ~15.5% | ~0.11 | ~45 | ~0.11 | Hybrid | **E** |
| giteshsawant | Gitesh Sawant | Swapnil Zade | ~20 | ~50 | ~10% | ~2.5 | ~20 | ~2.5 | Hybrid | **E** |
| dannycadima | Danny Cadima | Swapnil Zade | ~5 | 34 | ~3.8% | ~1.1 | ~30 | ~1.1 | Hybrid | **E** |

*copilotshree and SwapnilNice shown for reference; excluded from developer tier table.*

---

## Tier Groupings

### 🌟 Tier A — Top Performers (7 developers)

> Agent-First exception applied: % Accept benchmark skipped. Evaluate on LoC + ReqEff instead.

---

**amol-salunkhe | Amol Salunkhe** *(Swapnil Zade)* ⚠️ Budget Flag — New LoC Leader
- Int: 423 | LoC: 34,037 | %Acc: 1.6% | ReqEff: 6.4 | Premium: 5,309 | Workflow: Agent-First
- **In-scope LoC leader** this period — 34,037 lines (15.8% of adjusted team total). However, premium consumption spiked from 747 → 5,309 (7×); ReqEff collapsed from 40.8 → 6.4 (−84%). Tier A retained on exceptional volume, but this is a mandatory budget review. Both T1 and T2 fail under strict framework — classification is a volume-based exception.
- **Signal:** #1 by output; efficiency collapse is the top coaching priority.

---

**Kranti-nice | Kranti Kaple** *(Swapnil Zade)* 🚀 Breakout
- Int: 1,182 | LoC: 27,733 | %Acc: 1.3% | ReqEff: ~23.1 | Premium: ~1,200 | Workflow: Agent-First
- Highest interaction count in scope (1,182). ReqEff improved from ~7.6 → ~23.1 (+204% — Breakout). Strong Agent-First with lean premium spend. This is the standout coaching success story in the current analysis scope.
- **Signal:** Best momentum. Clean Tier A. Breakout story to share with team.

---

**mshnayderman | Mikhail Shnayderman** *(Alon Vax)* ⚠️ Efficiency Collapse
- Int: 164 | LoC: 27,539 | %Acc: 27.8% | ReqEff: 5.1 | Premium: 5,419 | Workflow: Inline-First
- Strong T1 (27.8% accept) holds Tier A. But ReqEff collapsed from 43.2 → 5.1 (−88%); premium spiked 9.5× in 5 days. T2 is a clear failure at scale. CRQC framework demotes this user to Tier C via the R=0 override. Next period: if ReqEff does not recover above 20, formal Tier B re-classification recommended.
- **Signal:** Accept rate saves tier; efficiency collapse is the #2 coaching priority.

---

**mfield1 | Matt Field** *(Swapnil Zade)*
- Int: ~600 | LoC: ~9,300 | %Acc: ~5.5% | ReqEff: ~14.3 | Premium: ~650 | Workflow: Hybrid
- Consistent Hybrid performer. ReqEff ~14.3 approaching the ≥15 preferred threshold. Lean spend (~650 premium). Low accept % (5.5%) is below Hybrid T1 target but T2 compensates. Steady Tier A contributor.
- **Signal:** Reliable mid-volume performer with good efficiency.

---

**rpawar-nice | Ritesh Pawar** *(Susovan Samal)* 🚀 Best Efficiency in Scope
- Int: 77 | LoC: 8,662 | %Acc: 7.7% | ReqEff: ~60.1 | Premium: ~144 | Workflow: Hybrid
- **Best Request Efficiency in scope** — ~60.1 LoC per premium request (was 20.1 in Jun 3, +199%). Lean spend (144 premium). With tomotvos excluded from analysis, rpawar-nice is now the efficiency benchmark for the team. T2 is exceptional; accept rate (7.7%) is below Hybrid T1 target but T2 more than compensates.
- **Signal:** Team efficiency leader this period. Breakout momentum.

---

**Vitthal-Nice | Vitthal Devkar** *(Susovan Samal)*
- Int: ~160 | LoC: ~2,800 | %Acc: ~44% | ReqEff: ~14 | Premium: ~200 | Workflow: Inline-First
- High accept rate (44%) indicates very relevant inline suggestions. ReqEff ~14 above 10. Lean spend. Modest LoC volume but strong quality signals.
- **Signal:** Quality Inline-First user. High relevance of suggestions.

---

**Akale23 | Amulya Kale** *(Susovan Samal)*
- Int: ~200 | LoC: ~2,600 | %Acc: ~18.8% | ReqEff: ~6.7 | Premium: ~390 | Workflow: Hybrid
- Accept rate (18.8%) slightly below the 20-35% T1 target. ReqEff (~6.7) below 10. Tier A classification reflects consistent engagement and rising trajectory (📈 Rising momentum). If T1/T2 don't improve next period, Tier B re-evaluation warranted.
- **Signal:** Borderline Tier A — needs improvement in both T1 and T2 to hold tier.

---

### 👍 Tier B — Solid Contributors (2 developers)

---

**luisalvatierra | Luis Salvatierra** *(Swapnil Zade)*
- Int: ~480 | LoC: ~4,800 | %Acc: ~17.6% | ReqEff: 2.9 | Premium: ~1,655 | Workflow: Hybrid
- % Accept (17.6%) approaching the 15-30% Hybrid T1 range. However, ReqEff at 2.9 is a clear T2 failure. Premium spend (~1,655) is at the outlier boundary. Tier B reflects the T1 signal; T2 improvement is the coaching target.
- **Coaching focus:** Reduce premium consumption or switch to more output-productive sessions. ReqEff needs to reach > 8.

---

**jayesh-rai | Jayesh Rai** *(Swapnil Zade)*
- Int: ~90 | LoC: ~2,500 | %Acc: ~4% | ReqEff: ~19.2 | Premium: ~130 | Workflow: Agent-First
- Agent-First with good ReqEff (~19.2, above 15 threshold) and lean premium (130). LoC output (~2,500) is modest given interaction count. T2 passes; T1 (ReqEff above 15) passes. Tier B reflects modest absolute volume — scale up to reach A.
- **Coaching focus:** Increase LoC output volume while maintaining efficiency.

---

### 👌 Tier C — Needs Improvement (6 developers)

**Prathmesh-Ranadive | Prathmesh Ranadive** *(Swapnil Zade)* ⚠️ Budget Alert
- Int: ~100 | LoC: 27,052 | %Acc: 25.4% | ReqEff: 2.5 | Premium: 10,733 | Workflow: Inline-First
- Good T1 (25.4% accept, 690 accept count). But 10,733 premium for 27,052 LoC is an extreme T2 failure. With dhanshree-jagtap-nice excluded, this user's LoC total (27,052) stands out — but the 10,733 premium cost is unsustainable. Second-highest premium consumer in scope.
- **Action:** Critical budget intervention. 10,733 premium requests require investigation.

**chris-haun | Chris Haun** *(Swapnil Zade)*
- Int: ~1,000 | LoC: ~10,359 | %Acc: ~11.7% | ReqEff: 2.8 | Premium: ~3,700 | Workflow: Hybrid
- 🔴 Declining (−76% ReqEff from Jun 3). Both T1 (11.7%, below 15%) and T2 (2.8, below 8) fail for Hybrid. High interaction count (~1,000) with poor premium ROI.
- **Action:** Investigate what ~3,700 premium calls are generating. Agent sessions may need refocusing on code output.

**jkumbhar | Jyoti Kumbhar** *(Swapnil Zade)*
- Int: ~230 | LoC: ~2,000 | %Acc: ~20% | ReqEff: ~16.7 | Workflow: Hybrid
- At 20% accept (T1 lower bound) and 16.7 ReqEff (above 10). Tier C due to low absolute LoC volume despite healthy rates. Scale up usage.

**Vyankatesh95 | Vyankatesh Khadakkar** *(Swapnil Zade)*
- Int: 423 | LoC: 4,177 | %Acc: 34.1% | ReqEff: ~27.8 | Workflow: Inline-First
- Good T1 (34.1% accept) and T2 (27.8 ReqEff). Tier C due to low absolute LoC (4,177) given 423 interactions. High interaction count suggests many short sessions. Needs larger per-session output.

**dsuraj25 | Suraj Dubey** *(Susovan Samal)*
- Int: ~15 | LoC: ~510 | %Acc: 0.0% | ReqEff: ~14.6 | Workflow: Hybrid
- Near-inactive. 0 code accepts. Very low engagement.

**abhijeetk268 | Abhijeet Kolhe** *(Swapnil Zade)*
- Int: 38 | LoC: 656 | %Acc: 29.6% | ReqEff: ~21.9 | Workflow: Inline-First
- Good T1 (29.6%) and T2 (~21.9) at very small volume. Tier C — scale up to Tier B immediately.

---

### 🟠 Tier D — Low Efficiency (9 developers)

| Login | Name | LoC | %Acc | ReqEff | Primary Issue |
|---|---|---|---|---|---|
| abhishekhole-nice | Abhishek Hole | 2,936 | 0.0% | ~17.3 | 0 accepts in 167 sessions; otherwise decent ReqEff |
| vishal-tad | Vishal Tad | ~2,900 | ~4.8% | ~23.2 | Irregular engagement; good efficiency when used |
| moadzughul | Moad Alzughul | ~3,100 | ~2.8% | ~14.8 | Agent-First just below ReqEff 15 threshold |
| tusharpatil166719 | Tushar Patil | ~1,900 | ~12% | ~19 | Low volume despite decent efficiency |
| meghabiradar05 | Megha Biradar | ~1,700 | ~5.5% | ~15.5 | Low volume |
| mshivarkar | Mohan Shivarkar | 2,018 | ~22% | 0.6 | ⚠️ 3,480 premium for 2,018 LoC — severe budget drain |
| sgite-wfm | Shubham Gite | 329 | 53.5% | 0.2 | ⚠️ 1,411 premium for 329 LoC |
| smishra-nice | Shridhar Mishra | 155 | 78.3% | ~6.2 | Near-zero LoC despite 80 Int; likely code-review usage |
| pdevle | Pratik Devle | ~1,100 | ~7% | ~15.7 | Low volume |

> **mshivarkar note:** 3,480 premium requests with only 2,018 LoC output is the most anomalous D-tier pattern. The 22% accept rate shows inline work is happening, but the premium budget is disproportionate. Immediate manager conversation needed.

---

### 🔴 Tier E — Urgent Attention (13 developers)

**Budget crisis group:**

| Login | Name | LoC | Premium | ReqEff | Action |
|---|---|---|---|---|---|
| nilesht-19 | Nilesh Tonape | 7,160 | 23,108 | 0.3 | 🔴 Highest premium in scope — immediate intervention |
| thakraln | Nishtha Thakral | ~1,111 | 11,112 | 0.1 | 🔴 Worst ROI in scope |
| trunalgawade | Trunal Gawade | ~1,086 | 10,863 | 0.1 | 🔴 Same pattern as thakraln |
| PradnyeshSalunke | Pradnyesh Salunke | ~2,968 | 9,892 | 0.3 | 🔴 Budget drain |

**Low-output group:**

| Login | Name | LoC | %Acc | ReqEff | Issue |
|---|---|---|---|---|---|
| sskalaskar | Sourabh Kalaskar | ~2,700 | ~15% | ~31.8 | Good efficiency but very low absolute LoC value |
| ShubhamFulzele28 | Shubham Fulzele | 739 | 0.0% | ~6.2 | 0 accepts in 117 interactions |
| Shreedevi-nice | Shreedevi Patil | 1,416 | 11.1% | ~7.1 | Below T1 and T2; low volume |
| prashasti-jain | Prashasti Jain | ~900 | ~8% | ~25.7 | Good efficiency, low absolute volume |
| suhas-kakde | Suhas Kakde | 1,639 | ~1.8% | ~6.2 | Agent-First below ReqEff threshold |
| pratikpawar12 | Pratik Pawar | 250 | ~4.2% | ~1.8 | Near-inactive |
| kbajaj-nice | Kaushal Bajaj | 5 | ~15.5% | ~0.11 | Essentially inactive |
| giteshsawant | Gitesh Sawant | ~50 | ~10% | ~2.5 | Near-inactive |
| dannycadima | Danny Cadima | 34 | ~3.8% | ~1.1 | Near-inactive |

---

## Executive Scorecard

| Tier | Count | % of In-Scope Devs | Est. LoC | Notes |
|---|---|---|---|---|
| 🌟 A | 7 | 18.9% | ~107,871 (~50%) | amol, Kranti, mshnayderman, mfield1, rpawar, Vitthal, Akale23 |
| 👍 B | 2 | 5.4% | ~7,300 (~3%) | luisalvatierra, jayesh-rai |
| 👌 C | 6 | 16.2% | ~45,154 (~21%) | Dominated by Prathmesh-Ranadive (27,052 LoC) |
| 🟠 D | 9 | 24.3% | ~14,058 (~7%) | Mixed efficiency; mshivarkar/sgite-wfm budget flags |
| 🔴 E | 13 | 35.1% | ~22,644 (~11%) | Budget crisis (4 users) + low-output (9 users) |

### 80/20 Analysis (in-scope)
Top 20% of 37 developers = ~7 users. Top 7 by LoC: amol-salunkhe, Kranti-nice, mshnayderman, Prathmesh-Ranadive, chris-haun, mfield1, rpawar-nice.
- Estimated contribution: ~145,000 LoC ≈ 67% of in-scope total
- 80/20 holds: top ~20% of users producing ~67% of output

### Premium Budget Analysis — Top 10 (In-Scope)

| Rank | Login | Name | Premium | LoC | ReqEff | Action |
|---|---|---|---|---|---|---|
| 1 | nilesht-19 | Nilesh Tonape | 23,108 | 7,160 | 0.3 | 🔴 Immediate |
| 2 | thakraln | Nishtha Thakral | 11,112 | ~1,111 | 0.1 | 🔴 Immediate |
| 3 | trunalgawade | Trunal Gawade | 10,863 | ~1,086 | 0.1 | 🔴 Immediate |
| 4 | Prathmesh-Ranadive | Prathmesh Ranadive | 10,733 | 27,052 | 2.5 | 🟡 Budget review |
| 5 | PradnyeshSalunke | Pradnyesh Salunke | 9,892 | ~2,968 | 0.3 | 🔴 Immediate |
| 6 | mshnayderman | Mikhail Shnayderman | 5,419 | 27,539 | 5.1 | 🟡 Monitor (was 43.2) |
| 7 | amol-salunkhe | Amol Salunkhe | 5,309 | 34,037 | 6.4 | 🟡 Monitor (was 40.8) |
| 8 | mshivarkar | Mohan Shivarkar | 3,480 | 2,018 | 0.6 | 🔴 Immediate |
| 9 | chris-haun | Chris Haun | ~3,700 | ~10,359 | 2.8 | 🟡 Coaching |
| 10 | luisalvatierra | Luis Salvatierra | ~1,655 | ~4,800 | 2.9 | 🟡 Coaching |

---

## Coaching Priorities

### Immediate
1. **nilesht-19, thakraln, trunalgawade, PradnyeshSalunke, mshivarkar** — Budget intervention. Collectively 55,000+ premium for ~13,000 LoC.
2. **mshnayderman, amol-salunkhe** — Investigate cause of 7–9× premium spikes since Jun 3. Both were top performers.

### Next Period Targets
- **Akale23** — Hold Tier A only if T1 reaches 20% and T2 reaches 10.
- **luisalvatierra** — T2 (ReqEff 2.9) is blocking Tier A. Premium reduction is the lever.
- **Prathmesh-Ranadive** — Strong T1 signal; premium spend must come down from 10,733.

### Coaching Wins to Document
- **rpawar-nice** (+199% ReqEff, Jun 3 → Jun 8) — New efficiency benchmark for in-scope team.
- **Kranti-nice** (+204% ReqEff) — Breakout. Highest interaction count + strong output. Replicate the approach.

---

*v1 Standard — 15 users excluded per `githun-ignored-users.md`. Agent-First exception applied for users with %Accept < 5% + Int ≥ 50 + LoC ≥ 500. Adjusted team totals computed by subtracting ignored users' estimated contributions from dashboard totals.*
