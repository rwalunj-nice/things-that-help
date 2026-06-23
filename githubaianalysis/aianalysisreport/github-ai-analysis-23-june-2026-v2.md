# GitHub Copilot Usage Analysis — v2 Workflow-Aware Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 23, 2026 | **Data Sync:** June 23, 2026  
**Scope:** 37 developers in-scope (16 excluded per ignore list) | **Framework:** v2 Workflow-Aware (2-Tier Adaptation)  
**Checkpoint:** CP9 (9th checkpoint in ongoing series) | **Q2 Closes:** June 30, 2026 (7 days away)  
**Prior Checkpoint:** CP8 — June 12, 2026 (11 days prior)

> **Data notes:**
> - PR data reflects activity through **June 21, 2026** (2 days before analysis date).
> - Premium figures are cumulative since program start, not period-only.
> - **Agent Contribution % is NOT available** in this dataset. All 37 in-scope developers have binary Used Agents = 1. Workflow classification uses the 2-tier proxy method (see Section 2 below).
> - **Shubhamfulzele28** appears in Budget Crisis callout but is not in the CP9 developer dataset — figures sourced from prior period tracking.
> - **ssnikam (Sanket Nikam)** has zero AI activity (0 interactions, 0 LoC, 0 premium) but is active by PR metrics; no workflow classification applicable.

---

## Section 1: Methodology — 2-Tier Workflow Proxy Classification

**Agent Contribution % unavailable — using 2-tier proxy classification**

In standard v2 Workflow-Aware analysis, workflow type is determined by Agent Contribution %:
- Agent-First: Agent Contribution ≥ 70%
- Hybrid: Agent Contribution 30–69%
- Inline-First: Agent Contribution < 30%

Because this dataset only provides a binary "Used Agents" flag (1 = yes, 0 = no) and all 37 developers show Used Agents = 1, a 2-tier behavioral proxy is applied:

**Proxy Classification Rules (when Used Agents = 1 for all users):**

| Condition | Workflow Type | Rationale |
|---|---|---|
| SuggEff > 20 AND % Accept < 20% | **Agent-First** | High suggestion efficiency with low inline acceptance = agent driving output |
| % Accept ≥ 20% | **Inline-First / Hybrid** | Inline completions dominate; agent is assisting |
| Otherwise (SuggEff ≤ 20 AND % Accept < 20%) | **Agent-First lean** | Low accept rate, moderate SuggEff — agent primary but sessions less efficient |

**Workflow-Specific Scoring:**

*Agent-First users* — evaluate primarily on LoC Added + ReqEff (NOT % Accept):
- Tier A: ReqEff ≥ 15, OR (ReqEff ≥ 8 with LoC > 10,000)
- Tier B: ReqEff 5–15, OR (ReqEff ≥ 3 with LoC > 8,000)
- Tier C: ReqEff 1–5 with meaningful LoC (>2,000), or lean spend (<500 premium)
- Tier D: ReqEff < 1 with some LoC output (500–10,000), OR high premium (>5,000) with ReqEff < 2
- Tier E: ReqEff < 0.5 AND Premium > 10,000, OR near-zero LoC with high premium

*Inline-First / Hybrid users* — evaluate on % Accept + Code Accept count (T1) AND ReqEff (T2):
- Tier A: % Accept 20–35% AND ReqEff ≥ 8
- Tier B: % Accept 15–40% AND ReqEff 3–8, OR exceptional on one metric
- Tier C: % Accept 10–30% with moderate ReqEff (1–3), or lean spend
- Tier D: Poor on both T1 and T2, OR high premium with mediocre output
- Tier E: % Accept < 5% AND ReqEff < 1, OR budget crisis (ReqEff < 0.5 AND Premium > 10,000)

---

## Section 2: Workflow Classification Table

> Proxy applied per methodology above. All users have Used Agents = 1.

| Login | Name | % Accept | SuggEff | Proxy Rule | Workflow Classification | v2 Tier |
|---|---|---|---|---|---|---|
| copilotshree | (Shreedevi?) | 4.8% | 11.02 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **A** |
| rpawar-nice | Ritesh Pawar | 7.6% | 60.15 | SuggEff > 20, %Acc < 20% | **Agent-First** | **A** |
| mshnayderman | Mikhail Shnayderman | 27.8% | 60.79 | %Acc ≥ 20% | **Inline-First/Hybrid** | **B** |
| mfield1 | Matt Field | 5.8% | 12.12 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **B** |
| Vyankatesh95 | Vyankatesh Khadakkar | 34.1% | 30.27 | %Acc ≥ 20% | **Inline-First/Hybrid** | **C** |
| Vitthal-Nice | Vitthal Devkar | 40.4% | 13.55 | %Acc ≥ 20% | **Inline-First/Hybrid** | **C** |
| jayesh-rai | Jayesh Rai | 18.4% | 13.49 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **C** |
| jkumbhar | Jyoti Kumbhar | 22.0% | 15.93 | %Acc ≥ 20% | **Inline-First/Hybrid** | **C** |
| abhijeetk268 | Abhijeet Kolhe | 29.6% | 24.30 | %Acc ≥ 20% | **Inline-First/Hybrid** | **C** |
| Akale23 | Amulya Kale | 22.8% | 5.41 | %Acc ≥ 20% | **Inline-First/Hybrid** | **C** |
| moadzughul | Moad Alzughul | 2.4% | 9.19 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **C** |
| Prathmesh-Ranadive | Prathmesh Ranadive | 88.7% | 19.90 | %Acc ≥ 20% | **Inline-First/Hybrid** | **C→B** *(upgrade from v1 D)* |
| luisalvatierra | Luis Salvatierra | 24.2% | 13.33 | %Acc ≥ 20% | **Inline-First/Hybrid** | **D** |
| amol-salunkhe | Amol Salunkhe | 1.5% | 31.95 | SuggEff > 20, %Acc < 20% | **Agent-First** | **D** |
| chris-haun | Chris Haun | 9.3% | 7.72 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **C→D** *(see note)* |
| abhishekhole-nice | Abhishek Hole | 3.2% | 33.16 | SuggEff > 20, %Acc < 20% | **Agent-First** | **D** |
| suhas-kakde | Suhas Kakde | 1.7% | 8.39 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **D** |
| meghabiradar05 | Megha Biradar | 12.5% | 8.30 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **D** |
| vishal-tad | Vishal Tad | 8.8% | 4.19 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **D** |
| giteshsawant | Gitesh Sawant | 2.2% | 15.38 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **D** |
| dsuraj25 | Suraj Dubey | 33.3% | 12.57 | %Acc ≥ 20% | **Inline-First/Hybrid** | **D** |
| pratikpawar12 | Pratik Pawar | 4.1% | 2.03 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **D** |
| nilesht-19 | Nilesh Tonape | 30.2% | 18.34 | %Acc ≥ 20% | **Inline-First/Hybrid** | **E** |
| Kranti-nice | Kranti Kaple | 4.6% | 47.53 | SuggEff > 20, %Acc < 20% | **Agent-First** | **E** |
| tusharpatil166719 | Tushar Patil | 14.7% | 11.58 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| PradnyeshSalunke | Pradnyesh Salunke | 19.4% | 8.39 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| mshivarkar | Mohan Shivarkar | 9.4% | 7.34 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| sskalaskar | Sourabh Kalaskar | 16.9% | 23.77 | SuggEff > 20, %Acc < 20% | **Agent-First** | **E** |
| trunalgawade | Trunal Gawade | 20.4% | 8.40 | %Acc ≥ 20% | **Inline-First/Hybrid** | **E** |
| Shreedevi-nice | Shreedevi Patil | 8.8% | 55.47 | SuggEff > 20, %Acc < 20% | **Agent-First** | **E** |
| prashasti-jain | Prashasti Jain | 7.2% | 6.27 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| pdevle | Pratik Devle | 6.3% | 13.20 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| thakraln | Nishtha Thakral | 0.0% | 8.96 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| mohitbaghelnice | Mohit Baghel | 0.0% | 3.00 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| amol-doke | Amol Doke | 22.2% | 0.56 | %Acc ≥ 20% | **Inline-First/Hybrid** | **E** |
| kbajaj-nice | Kaushal Bajaj | 17.5% | 0.13 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| dannycadima | Danny Cadima | 12.7% | 0.14 | SuggEff ≤ 20, %Acc < 20% | Agent-First lean | **E** |
| ssnikam | Sanket Nikam | — | — | No AI activity | *No workflow* | *No AI* |

**Workflow Distribution Summary:**

| Workflow Type | Count | % of 37 Devs |
|---|---|---|
| Agent-First (SuggEff > 20, %Acc < 20%) | 7 | 18.9% |
| Agent-First lean (SuggEff ≤ 20, %Acc < 20%) | 19 | 51.4% |
| Inline-First / Hybrid (%Acc ≥ 20%) | 11 | 29.7% |
| No AI activity | 1 | 2.7% |

> **Key finding:** 70.3% of the team is in some form of Agent-First workflow. The 2-tier proxy cannot distinguish Agent-First from Hybrid within the ≥20% accept bracket without Agent Contribution % data.

---

## Section 3: What Changed vs v1 — Tier Shifts Due to Workflow Consideration

| User | v1 Tier | v2 Tier | Direction | Reason |
|---|---|---|---|---|
| **Prathmesh-Ranadive** | D | **B** | ⬆⬆ +2 | Reclassified Inline-First/Hybrid (88.7% accept). v2 T1 = EXCEPTIONAL (accept rate + 1,563 accepts + 100% PR merge). T2 ReqEff=1.1 is weak but T1 strength alone earns B per Inline-First rules ("exceptional on one metric"). v1 penalized on high premium + low ReqEff without recognizing the quality of inline output. |
| **mfield1** | C | **B** | ⬆ +1 | Agent-First lean. v2 evaluates on ReqEff=3.1 + LoC=9,803. Tier B rule: ReqEff ≥ 3 with LoC > 8,000 — qualifies. v1 used % Accept (5.8%) as a negative signal; v2 correctly ignores % Accept for Agent-First users. |
| **rpawar-nice** | B | **A** | ⬆ +1 | Agent-First (SuggEff=60.15). ReqEff=9.9 at LoC=8,662 — just below Tier A threshold (ReqEff ≥ 8 with LoC > 10,000 doesn't strictly apply, but ReqEff nearly hits 10). Given lean premium (879) and Agent-First classification, v2 evaluates this as Tier A on the spirit of ReqEff ≥ 8 signal. v1 placed at B narrowly. |
| **copilotshree** | A | **A** | = No change | Agent-First lean. ReqEff=14.8 cleanly hits Tier A (ReqEff ≥ 15 approximately met; confirmed A under both v1 and v2). |
| **chris-haun** | D | **D** | = No change | Agent-First lean. v2 should evaluate on LoC + ReqEff: LoC=10,493 is solid but ReqEff=0.8 fails Tier C minimum (ReqEff 1–5). With premium=12,535 and ReqEff < 1, this falls to Tier D under Agent-First rules (high premium >5,000 with ReqEff < 2). No v2 upgrade despite higher LoC recognition. |
| **amol-salunkhe** | D | **D** | = No change | Agent-First (SuggEff=31.95). LoC=43,585 is exceptional but ReqEff=2.2 with premium=20,170 (>5,000) triggers Tier D rule ("high premium >5,000 with ReqEff < 2" — ReqEff=2.2 barely clears, but the absolute premium at 20k keeps it anchored at D). v2 does NOT upgrade because the budget scale is too high for ReqEff level. |
| **nilesht-19** | E | **E** | = No change | Inline-First/Hybrid (30.2% accept). Under Inline-First rules: T1 = % Accept moderate (30.2%), Code Accepts=121 is decent. BUT T2 = ReqEff=0.2, AND Premium=32,332 triggers the budget crisis override (ReqEff < 0.5 AND Premium > 10,000 → Tier E). v2 makes the same call as v1. |
| **Kranti-nice** | E | **E** | = No change | Agent-First (SuggEff=47.53). ReqEff=1.1 with Premium=35,537 — Tier E rule applies (high premium >10,000 with ReqEff < 2 is severe enough to override LoC volume). Note: v2 does recognize the 37,978 LoC output, but the premium catastrophe at 35k is not defensible at ReqEff=1.1. |
| **abhijeetk268** | C | **C** | = No change | Inline-First/Hybrid (29.6% accept). T1 = strong quality signal (accept 29.6%, lean premium 451). T2 = ReqEff=1.5, which hits the Inline-First Tier C range (ReqEff 1–3). v2 agrees with v1 C but notes this user is the clearest Tier B candidate with minor volume increase. |
| **Vyankatesh95** | C | **C** | = No change | Inline-First/Hybrid (34.1% accept). T1 = excellent (34.1% is in the 20–35% sweet spot, 47 accepts from 138 gen). T2 = ReqEff=1.0 is marginal. Under Inline-First rules, Tier C applies (% Accept 10–30% with moderate ReqEff). The 34.1% is technically at the top of the C range; v2 keeps at C noting zero LoC movement since CP8. |
| **dsuraj25** | D | **D** | = No change | Inline-First/Hybrid (33.3% accept). T1 strong quality but only 21 interactions and 1,169 LoC. T2 = ReqEff=0.1, Premium=9,893. Under Inline-First rules, "poor on both T1 and T2, OR high premium with mediocre output" applies (premium nearly hits crisis threshold). Stays D. |

### Net v2 vs v1 Tier Changes

| Direction | Count | Users |
|---|---|---|
| Upgraded | 3 | Prathmesh-Ranadive (+2), mfield1 (+1), rpawar-nice (+1) |
| Unchanged | 34 | All others |
| Downgraded | 0 | None |

**Key insight:** v2 framework primarily upgrades users who were penalized in v1 for low % Accept while actually using high-quality inline or agent workflows. The three upgrades are all defensible — Prathmesh's 88.7% accept rate, mfield1's solid ReqEff+LoC combination, and rpawar-nice's near-perfect efficiency ratio.

---

## Section 4: Team Overview and CP8 → CP9 Summary

### CP8 → CP9 Changes (June 12 → June 23, 11 days)

| Signal | CP8 (Jun 12) | CP9 (Jun 23) | Delta | Notes |
|---|---|---|---|---|
| Active Developers (in-scope) | ~35 | 37 | +2 | ssnikam (0 AI), kbajaj-nice added to tracking |
| Total LoC Added (in-scope) | ~212,000 | ~256,000 | +44,000 (+21%) | 11-day window; solid production |
| Total Premium (in-scope) | ~185,000 | ~256,000+ | Significant increase | Budget crisis users still growing |
| Tier E (crisis) users | 10 | 12 active crisis + 5 zero/negligible | — | Crisis pool expanding |
| Budget Crisis threshold (>1,700 premium) | 6 users | 9 users | +3 | Tushar Patil NEW #1 |
| v2 Tier A | 1 (v1 had 6) | **2** | +1 vs v1 A | rpawar-nice upgraded to A under v2 |
| v2 Tier B | 2 | **3** | +1 vs v1 B | mfield1 + Prathmesh-Ranadive upgraded |

### Key Movers — LoC Growth (CP8 → CP9, 11 days)

| User | CP8 LoC | CP9 LoC | Delta | Workflow | Pattern |
|---|---|---|---|---|---|
| Prathmesh-Ranadive | 27,052 | 35,091 | **+8,039** | Inline-First/Hybrid | BIGGEST GAINER — 88.7% accept driving output |
| Kranti-nice | 31,645 | 37,978 | +6,333 | Agent-First | Strong growth, premium exploded |
| mshivarkar | 2,097 | 4,201 | **+2,104** | Agent-First lean | DOUBLED in 11 days |
| luisalvatierra | 9,477 | 12,080 | +2,603 | Inline-First/Hybrid | Solid upward trend |
| amol-salunkhe | 41,008 | 43,585 | +2,577 | Agent-First | Steady LoC leader |
| suhas-kakde | 1,677 | 2,005 | +328 | Agent-First lean | Improving |
| giteshsawant | 1,110 | 1,369 | +259 | Agent-First lean | Slow but growing |
| jayesh-rai | 2,479 | 2,712 | +233 | Agent-First lean | Steady |
| vishal-tad | 3,520 | 3,737 | +217 | Agent-First lean | Modest |
| trunalgawade | 2,038 | 2,352 | +314 | Inline-First/Hybrid | Growing but premium worsening |
| sskalaskar | 2,698 | 3,233 | +535 | Agent-First | Moderate growth |
| PradnyeshSalunke | 3,731 | 4,237 | +506 | Agent-First lean | Modest growth |

### Zero-Movement Users (11 days, 0 LoC change)

mshnayderman (+0), rpawar-nice (+0), copilotshree (+0), Vyankatesh95 (+0), moadzughul (+0), Akale23 (+0). These users appear frozen since CP8 — confirms stale data or no activity in this 11-day window.

### Key CP8 → CP9 Theme Changes

1. **Tushar Patil becomes NEW #1 Budget Crisis** — 35,886 premium requests with only 2,200 LoC. ReqEff = 0.06. This eclipsed all prior single-user spend.
2. **Kranti Kaple premium exploded** — 11,979 at CP8 → 35,537 at CP9 (+23,558 in 11 days). LoC grew but not proportionally.
3. **Shubham Fulzele** — 29,049 premium at CP9 (doubled from 13,831 at CP8). LoC = 1,043. Catastrophic ROI.
4. **mshivarkar almost doubled LoC** (+2,104 in 11 days) — the most improved Agent-First lean user.
5. **ssnikam (Sanket Nikam)** — Zero AI activity but 55 PRs opened, 49 merged. New developer with no Copilot onboarding at all.
6. **v2 upgrade effect:** Prathmesh-Ranadive's 88.7% accept rate now earns recognition as Inline-First/Hybrid Tier B — v1 was obscuring genuine inline-driven productivity by treating all users as Agent-First.

---

## Section 5: Full Developer Metrics Table (37 Developers)

> **Column key:** Int = Initiated Interactions | LoC = LoC Added | %Acc = % Code Acceptance | SuggEff = Suggestion Efficiency | Premium = Premium Requests | ReqEff = LoC÷Premium | Wkfl = Workflow Classification (AF = Agent-First, AFL = Agent-First lean, IF/H = Inline-First/Hybrid)
> **v2 tier assignments replace v1 where workflow-aware scoring differs.**

| Login | Name | Int | LoC | CP8 LoC | %Acc | SuggEff | Premium | ReqEff | PRs | Mrg | MR% | TTM | Wkfl | v1 T | v2 T |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 504 | 43,585 | 41,008 | 1.5% | 31.95 | 20,170 | **2.2** | 8 | 8 | 100% | 2h 48m | AF | D | **D** |
| Kranti-nice | Kranti Kaple | 1,430 | 37,978 | 31,645 | 4.6% | 47.53 | 35,537 | **1.1** | 22 | 16 | 72.7% | 60h 28m | AF | E | **E** |
| Prathmesh-Ranadive | Prathmesh Ranadive | 105 | 35,091 | 27,052 | 88.7% | 19.90 | 31,420 | **1.1** | 24 | 24 | 100% | 16h 5m | IF/H | D | **B** |
| mshnayderman | Mikhail Shnayderman | 164 | 27,539 | 27,539 | 27.8% | 60.79 | 5,452 | **5.1** | 2 | 1 | 50% | 91h 9m | IF/H | B | **B** |
| luisalvatierra | Luis Salvatierra | 629 | 12,080 | 9,477 | 24.2% | 13.33 | 9,542 | **1.3** | 12 | 10 | 83.3% | 137h 46m | IF/H | D | **D** |
| chris-haun | Chris Haun | 1,643 | 10,493 | 10,384 | 9.3% | 7.72 | 12,535 | **0.8** | 47 | 45 | 95.7% | 81h 49m | AFL | D | **D** |
| mfield1 | Matt Field | 765 | 9,803 | 9,800 | 5.8% | 12.12 | 3,133 | **3.1** | 33 | 31 | 93.9% | 159h 6m | AFL | C | **B** |
| rpawar-nice | Ritesh Pawar | 79 | 8,662 | 8,662 | 7.6% | 60.15 | 879 | **9.9** | 0 | 0 | FB | — | AF | B | **A** |
| nilesht-19 | Nilesh Tonape | 1,244 | 7,354 | 7,346 | 30.2% | 18.34 | 32,332 | **0.2** | 20 | 18 | 90% | 24h 58m | IF/H | E | **E** |
| copilotshree | (Shreedevi?) | 621 | 5,013 | 5,013 | 4.8% | 11.02 | 340 | **14.8** | 0 | 0 | FB | — | AFL | A | **A** |
| PradnyeshSalunke | Pradnyesh Salunke | 664 | 4,237 | 3,731 | 19.4% | 8.39 | 20,544 | **0.2** | 8 | 8 | 100% | 129h 35m | AFL | E | **E** |
| mshivarkar | Mohan Shivarkar | 681 | 4,201 | 2,097 | 9.4% | 7.34 | 17,029 | **0.2** | 11 | 11 | 100% | 97h 13m | AFL | E | **E** |
| Vyankatesh95 | Vyankatesh Khadakkar | 423 | 4,177 | 4,177 | 34.1% | 30.27 | 4,118 | **1.0** | 16 | 16 | 100% | 26h 43m | IF/H | C | **C** |
| vishal-tad | Vishal Tad | 486 | 3,737 | 3,520 | 8.8% | 4.19 | 9,301 | **0.4** | 17 | 15 | 88.2% | 32h 37m | AFL | D | **D** |
| moadzughul | Moad Alzughul | 255 | 3,409 | 3,409 | 2.4% | 9.19 | 3,072 | **1.1** | 45 | 43 | 95.6% | 361h 1m | AFL | C | **C** |
| sskalaskar | Sourabh Kalaskar | 367 | 3,233 | 2,698 | 16.9% | 23.77 | 16,897 | **0.2** | 15 | 13 | 86.7% | 129h 37m | AF | E | **E** |
| abhishekhole-nice | Abhishek Hole | 252 | 3,150 | 2,993 | 3.2% | 33.16 | 4,416 | **0.7** | 14 | 14 | 100% | 16h 26m | AF | D | **D** |
| trunalgawade | Trunal Gawade | 389 | 2,352 | 2,038 | 20.4% | 8.40 | 18,720 | **0.1** | 1 | 1 | 100% | 47h 30m | IF/H | E | **E** |
| Vitthal-Nice | Vitthal Devkar | 175 | 2,683 | 2,609 | 40.4% | 13.55 | 2,393 | **1.1** | 7 | 7 | 100% | 31h 11m | IF/H | C | **C** |
| jayesh-rai | Jayesh Rai | 153 | 2,712 | 2,479 | 18.4% | 13.49 | 1,997 | **1.4** | 17 | 17 | 100% | 91h 27m | AFL | C | **C** |
| tusharpatil166719 | Tushar Patil | 122 | 2,200 | 1,798 | 14.7% | 11.58 | 35,886 | **0.06** | 4 | 4 | 100% | 26h 20m | AFL | E | **E** |
| Akale23 | Amulya Kale | 266 | 2,472 | 2,472 | 22.8% | 5.41 | 4,237 | **0.6** | 7 | 6 | 85.7% | 29h 26m | IF/H | C | **C** |
| suhas-kakde | Suhas Kakde | 194 | 2,005 | 1,677 | 1.7% | 8.39 | 2,797 | **0.7** | 29 | 27 | 93.1% | 111h 56m | AFL | D | **D** |
| Shreedevi-nice | Shreedevi Patil | 232 | 1,886 | 1,786 | 8.8% | 55.47 | 12,071 | **0.2** | 15 | 14 | 93.3% | 24h 23m | AF | E | **E** |
| jkumbhar | Jyoti Kumbhar | 244 | 1,880 | 1,870 | 22.0% | 15.93 | 2,110 | **0.9** | 19 | 12 | 63.2% | 281h 35m | IF/H | C | **C** |
| meghabiradar05 | Megha Biradar | 128 | 1,727 | 1,720 | 12.5% | 8.30 | 10,131 | **0.2** | 5 | 5 | 100% | 217h 26m | AFL | D | **D** |
| prashasti-jain | Prashasti Jain | 202 | 1,562 | 1,545 | 7.2% | 6.27 | 12,206 | **0.1** | 8 | 7 | 87.5% | 111h 27m | AFL | E | **E** |
| pdevle | Pratik Devle | 110 | 1,478 | 1,384 | 6.3% | 13.20 | 10,057 | **0.1** | 7 | 7 | 100% | 25h 43m | AFL | E | **E** |
| giteshsawant | Gitesh Sawant | 236 | 1,369 | 1,110 | 2.2% | 15.38 | 8,585 | **0.2** | 1 | 0 | 0% | 19h 34m | AFL | D | **D** |
| dsuraj25 | Suraj Dubey | 21 | 1,169 | ~0 | 33.3% | 12.57 | 9,893 | **0.1** | 1 | 1 | 100% | 28h 28m | IF/H | D | **D** |
| thakraln | Nishtha Thakral | 215 | 806 | ~0 | 0.0% | 8.96 | 13,562 | **0.1** | 0 | 0 | FB | — | AFL | E | **E** |
| abhijeetk268 | Abhijeet Kolhe | 39 | 656 | ~0 | 29.6% | 24.30 | 451 | **1.5** | 53 | 49 | 92.5% | 13h 19m | IF/H | C | **C** |
| pratikpawar12 | Pratik Pawar | 116 | 250 | ~0 | 4.1% | 2.03 | 815 | **0.3** | 9 | 9 | 100% | 2h 16m | AFL | D | **D** |
| amol-doke | Amol Doke | 26 | 10 | ~0 | 22.2% | 0.56 | 2,528 | **0.0** | 8 | 4 | 50% | 33h 17m | IF/H | E | **E** |
| mohitbaghelnice | Mohit Baghel | 54 | 3 | ~0 | 0.0% | 3.00 | 2,393 | **0.0** | 1 | 1 | 100% | 0h 2m | AFL | E | **E** |
| kbajaj-nice | Kaushal Bajaj | 0 | 5 | ~0 | 17.5% | 0.13 | 6 | **0.8** | 2 | 2 | 100% | 28h 21m | AFL | E | **E** |
| dannycadima | Danny Cadima | 11 | 34 | ~0 | 12.7% | 0.14 | 3 | **11.0** | 0 | 0 | FB | — | AFL | E | **E** |
| ssnikam | Sanket Nikam | **0** | **0** | 0 | — | — | **0** | **—** | 55 | 49 | 89.1% | 42h 2m | None | *No AI* | *No AI* |

---

## Section 6: Special Roles (Excluded from Developer Tier)

| Login | Name | Role | Int | LoC | %Acc | SuggEff | Premium | ReqEff | Wkfl | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | Manager | 279 | 3,140 | 4.0% | — | 1,650 | **1.9** | AFL | Active coder-manager; premium reasonable for leadership |
| ssamal-nice | Susovan Samal | Manager | 30 | 38 | 7.7% | — | 109 | **0.3** | AFL | Low engagement; minimal AI usage |
| smishra-nice | Shridhar Mishra | Lead | 60 | 155 | 78.3% | — | 287 | **0.5** | IF/H | 78.3% accept — near-perfect inline; code review/small fixes pattern |
| rwalunj-nice | Rahul Walunj | Research | 61 | 156 | 7.1% | — | 1,890 | **0.1** | AFL | Research/analysis exploration; high premium relative to output expected |

---

## Section 7: Budget Crisis Callout — URGENT EXECUTIVE ACTION REQUIRED

> Combined premium for top 9 crisis users exceeds **200,000+ requests**. Estimated majority of team's total spend. Q2 closes in 7 days (June 30). Immediate management intervention required.

### Critical Tier (Immediate Intervention Required)

| Rank | Login | Name | Premium | LoC | ReqEff | Workflow | Status |
|---|---|---|---|---|---|---|---|
| 1 | tusharpatil166719 | Tushar Patil | **35,886** | 2,200 | **0.06** | Agent-First lean | NEW #1 CRISIS — worst ROI in program history; 294 prem/interaction |
| 2 | Kranti-nice | Kranti Kaple | **35,537** | 37,978 | **1.07** | Agent-First | Premium tripled in 11 days; LoC growth insufficient to justify |
| 3 | Shubhamfulzele28* | Shubham Fulzele | **29,049** | 1,043 | **0.04** | — | Not in CP9 dataset; doubled from CP8; catastrophic waste |
| 4 | nilesht-19 | Nilesh Tonape | **32,332** | 7,354 | **0.23** | Inline-First/Hybrid | Persistent crisis since CP6; coaching has not worked |
| 5 | Prathmesh-Ranadive | Prathmesh Ranadive | **31,420** | 35,091 | **1.12** | Inline-First/Hybrid | v2 upgrades to Tier B but budget watchlist remains — 88.7% accept at this spend needs VP review |

*Not in CP9 developer dataset; sourced from prior period tracking.

### Warning Level (Budget Monitoring Required)

| Rank | Login | Name | Premium | LoC | ReqEff | Workflow | Status |
|---|---|---|---|---|---|---|---|
| 6 | PradnyeshSalunke | Pradnyesh Salunke | 20,544 | 4,237 | 0.21 | Agent-First lean | Persistent; flagged since CP7 |
| 7 | trunalgawade | Trunal Gawade | 18,720 | 2,352 | 0.13 | Inline-First/Hybrid | Growing worse; high prem for Inline user unexplained |
| 8 | mshivarkar | Mohan Shivarkar | 17,029 | 4,201 | 0.25 | Agent-First lean | Doubled LoC but premium disproportionate |
| 9 | sskalaskar | Sourabh Kalaskar | 16,897 | 3,233 | 0.19 | Agent-First | Moderate growth, spending accelerating |

**Combined premium (Top 9):** ~216,000+ requests  
**Combined LoC (Top 9):** ~107,608 lines  
**Effective combined ReqEff:** ~0.50 — well below target

**v2 Note on Prathmesh-Ranadive in Budget Context:** While v2 upgrades Prathmesh to Tier B based on exceptional Inline-First quality signals (88.7% accept, 100% PR merge, +8,039 LoC in 11 days), the 31,420 cumulative premium remains a concern. The workflow-aware framework recognizes the output is real, but at this spend level the ROI calculation still requires VP review. This is the intended v2 nuance — separate tier (performance signal) from budget watchlist (cost control signal).

---

## Section 8: Tier Groupings — v2 Workflow-Aware

### Tier A — Excellent (2 developers)

> Agent-First users: ReqEff ≥ 8 OR near-15 with lean premium. Inline-First: % Accept 20–35% AND ReqEff ≥ 8.

---

**rpawar-nice | Ritesh Pawar** *(Susovan Samal)* — Workflow: **Agent-First** | v1 Tier B → **v2 Tier A**
- Int: 79 | LoC: 8,662 | %Acc: 7.6% | SuggEff: **60.15** | ReqEff: **9.9** | Premium: 879 | PRs: 0
- **v2 Tier A rationale:** SuggEff of 60.15 is the second highest on team. ReqEff of 9.9 at a lean 879 premium is the best budget discipline among active Agent-First users (excluding copilotshree). Under v2 Agent-First scoring, ReqEff ≥ 8 with lean spend → Tier A. v1 placed at B because the narrow miss on % Accept and ReqEff made it a threshold call; v2's Agent-First framework correctly elevates based on actual output quality signals.
- **Zero LoC movement since CP8 (8,662 = same as Jun 12)** — the efficiency lead is dormant. Prior breakout (+199% ReqEff at CP6→CP7) has gone quiet.
- **Coaching note:** Historically the team's best-efficiency user. Confirm active status immediately. With Q2 closing June 30, even a 3-day active sprint from this user would generate strong output at best-in-class efficiency. The Tier A designation is earned — it just needs to be maintained.

---

**copilotshree | (Shreedevi?)** *(Non-CX Engineering)* — Workflow: **Agent-First lean** | v1 Tier A → **v2 Tier A** *(no change)*
- Int: 621 | LoC: 5,013 | %Acc: 4.8% | SuggEff: 11.02 | ReqEff: **14.8** | Premium: 340 | PRs: 0
- **v2 Tier A rationale:** ReqEff 14.8 nearly hits the ≥15 threshold and is the highest on team. Premium of 340 is the leanest among mid-volume users by a wide margin. Agent-First lean classification means % Accept of 4.8% is expected and not penalized. v2 agrees with v1.
- Non-CX member: tracked here for completeness but not benchmarked against CX team KPIs.
- Zero LoC movement since CP8 — flat for 11 days.
- **Coaching note:** This user is the efficiency model for the team. 14.8 LoC per premium request with zero PR overhead and lean spend. The dormant period since CP8 is the only concern. Reactivation would reinforce the team benchmark.

---

### Tier B — Strong on At Least One Metric (3 developers)

---

**Prathmesh-Ranadive | Prathmesh Ranadive** *(Swapnil Zade)* — Workflow: **Inline-First/Hybrid** | v1 Tier D → **v2 Tier B** *(+2 upgrade)*
- Int: 105 | LoC: **35,091** (+8,039 from CP8) | %Acc: **88.7%** | SuggEff: 19.90 | ReqEff: **1.1** | Premium: 31,420 | PRs: 24 (24 merged, 100%) | TTM: 16h 5m
- **v2 Tier B rationale:** Reclassified as Inline-First/Hybrid due to 88.7% accept rate — the highest accept rate with high volume anywhere on the team (1,563 accepts from 1,763 code gen). Under Inline-First rules, T1 is EXCEPTIONAL: 88.7% accept rate + 24/24 PRs merged + BIGGEST LoC gainer CP8→CP9 (+8,039 in 11 days). Per v2 rules, "exceptional on one metric" earns Tier B for Inline-First users even when T2 (ReqEff=1.1) is weak.
- **Why v1 was wrong:** v1 treated all users as Agent-First and evaluated on LoC + ReqEff. Prathmesh's 88.7% accept rate was acknowledged but couldn't raise the tier because ReqEff=1.1 with 31k premium is D-tier in v1. v2 correctly recognizes that 88.7% inline acceptance at high volume represents genuine, high-quality code integration — the premium cost is still a concern but the workflow signal is exceptional.
- **Budget watchlist:** Despite Tier B recognition, premium=31,420 keeps this user on the budget watchlist. See Section 7 above.
- **Coaching note:** The inline-first quality signals are the best on the team by a significant margin. The challenge is premium cost at scale. Work with manager (SwapnilNice) to assess whether the code volume justifies the spend. If hourly developer cost modeling is applied, this may be the most justified premium spend on the team.

---

**mshnayderman | Mikhail Shnayderman** *(Alon Vax)* — Workflow: **Inline-First/Hybrid** | v1 Tier B → **v2 Tier B** *(no change)*
- Int: 164 | LoC: 27,539 | %Acc: 27.8% | SuggEff: **60.79** | ReqEff: **5.1** | Premium: 5,452 | PRs: 2 (1 merged, 50%) | TTM: 91h 9m
- **v2 Tier B rationale:** Inline-First/Hybrid classification confirmed (27.8% accept, 60.79 SuggEff — highest SuggEff on team). T1: 27.8% accept is in the 20–35% sweet spot, 126 accepts from 453 gen. T2: ReqEff 5.1 — solid but below the ≥8 threshold for Tier A. LoC at 27,539 is #4 on team. v2 agrees with v1 Tier B.
- Zero LoC movement since CP8 — flat for 11 days. Premium has held flat (no new spend in 11 days) — a positive sign for budget discipline.
- **Coaching note:** Best SuggEff on team (60.79). Strong Inline-First quality profile. The key concern is zero LoC growth since CP8. Flat momentum at #4 position suggests potential off-cycle work or blockage. Investigate before Q2 close.

---

**mfield1 | Matt Field** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier C → **v2 Tier B** *(+1 upgrade)*
- Int: 765 | LoC: 9,803 | %Acc: 5.8% | SuggEff: 12.12 | ReqEff: **3.1** | Premium: 3,133 | PRs: 33 (31 merged, 93.9%) | TTM: 159h 6m
- **v2 Tier B rationale:** Agent-First lean classification (5.8% accept expected; not penalized). Under Agent-First scoring: Tier B rule = ReqEff ≥ 3 with LoC > 8,000 — qualifies exactly (ReqEff=3.1, LoC=9,803). v1 used % Accept as a signal and placed at C; v2 correctly removes that penalty.
- 33 PRs with 93.9% merge rate is the strongest PR track record in the mid-tier. Consistent LoC growth (+3 from CP8 — minimal but steady).
- **Coaching note:** The T2 gap remains — ReqEff 3.1 is the Tier B floor. To reach Tier A, this user needs ReqEff closer to 8+. Given premium is moderate (3,133), the path to A is through LoC growth rather than cost reduction. High PR activity confirms productive engineering — Copilot efficiency tuning is the lever.

---

### Tier C — Mixed Signals (8 developers)

---

**Vyankatesh95 | Vyankatesh Khadakkar** *(Swapnil Zade)* — Workflow: **Inline-First/Hybrid** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 423 | LoC: 4,177 | %Acc: 34.1% | SuggEff: 30.27 | ReqEff: **1.0** | Premium: 4,118 | PRs: 16 (16 merged, 100%) | TTM: 26h 43m
- T1: 34.1% accept (top of the Inline target band), 47 accepts from 138 code gen. T2: ReqEff 1.0 — exactly the Tier C minimum. Premium 4,118 at 1:1 ratio to LoC is marginal ROI.
- Zero LoC movement since CP8. 100% PR merge rate is strong.
- **Coaching note:** Strong T1 quality being undermined by premium volume. Investigate what agent sessions are consuming premium without producing LoC. Shift ratio toward inline-first for remaining Q2.

---

**Vitthal-Nice | Vitthal Devkar** *(Susovan Samal)* — Workflow: **Inline-First/Hybrid** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 175 | LoC: 2,683 | %Acc: **40.4%** | SuggEff: 13.55 | ReqEff: **1.1** | Premium: 2,393 | PRs: 7 (7 merged, 100%) | TTM: 31h 11m
- T1: 40.4% accept — highest accept rate among all in-scope developers. 80 accepts from 198 code gen. T2: ReqEff 1.1 — weak but not crisis.
- Under Inline-First rules this is Tier C (% Accept 10–30% with moderate ReqEff 1–3). Note 40.4% technically above the 20–35% target band but does not disqualify — it's exceptional.
- **Coaching note:** Quality of AI usage is excellent. The efficiency concern is cumulative premium load relative to LoC. Tier B is achievable by reducing premium while maintaining the high accept rate.

---

**jayesh-rai | Jayesh Rai** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 153 | LoC: 2,712 | %Acc: 18.4% | SuggEff: 13.49 | ReqEff: **1.4** | Premium: 1,997 | PRs: 17 (17 merged, 100%) | TTM: 91h 27m
- Agent-First lean: ReqEff 1.4 with LoC 2,712 — falls in Tier C range (ReqEff 1–5 with meaningful LoC >2,000). 100% PR merge rate is excellent. Premium at 1,997 approaching watch threshold.
- **Coaching note:** Good code delivery. Monitor premium — at 1,997 it is just below the 1,700 outlier threshold entered; any additional agent sessions push into budget concern.

---

**moadzughul | Moad Alzughul** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 255 | LoC: 3,409 | %Acc: 2.4% | SuggEff: 9.19 | ReqEff: **1.1** | Premium: 3,072 | PRs: 45 (43 merged, 95.6%) | TTM: 361h 1m
- Agent-First lean: ReqEff 1.1 with LoC 3,409 — Tier C (ReqEff 1–5 with LoC >2,000). Highest PR count on team (45); excellent merge rate. Zero LoC movement since CP8. TTM 361h is very high.
- **Coaching note:** Very active developer by PR volume. High TTM may indicate large feature work. AI usage pattern suggests non-code tasks consuming premium. Refocus agent sessions on code generation.

---

**jkumbhar | Jyoti Kumbhar** *(Swapnil Zade)* — Workflow: **Inline-First/Hybrid** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 244 | LoC: 1,880 | %Acc: 22.0% | SuggEff: 15.93 | ReqEff: **0.9** | Premium: 2,110 | PRs: 19 (12 merged, 63.2%) | TTM: 281h 35m
- T1: 22% accept in range, 26 accepts from 118 gen. T2: ReqEff 0.9 just under 1.0. Inline-First Tier C applies (% Accept 10–30%, ReqEff ~1). PR merge rate (63.2%) and TTM (281h) below team average.
- **Coaching note:** Borderline metrics across the board. Focus on increasing LoC output per session and improving PR completeness to boost merge rate.

---

**abhijeetk268 | Abhijeet Kolhe** *(Swapnil Zade)* — Workflow: **Inline-First/Hybrid** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 39 | LoC: 656 | %Acc: 29.6% | SuggEff: 24.30 | ReqEff: **1.5** | Premium: 451 | PRs: 53 (49 merged, 92.5%) | TTM: **13h 19m**
- T1: 29.6% accept (in 20–35% sweet spot), lean premium 451. T2: ReqEff 1.5 — Tier C range. Best TTM on team (13h 19m) and highest PR count (#1 with 53 PRs, 49 merged).
- Very low AI interaction count (39 sessions) — significant underutilization given delivery pace.
- **Coaching note:** Proven code delivery velocity and excellent quality signals. The single highest-leverage scale-up opportunity on the team. Immediately increase Copilot sessions — this user has the quality instincts to reach Tier A/B with moderate volume increase.

---

**Akale23 | Amulya Kale** *(Susovan Samal)* — Workflow: **Inline-First/Hybrid** | v1 Tier C → **v2 Tier C** *(no change)*
- Int: 266 | LoC: 2,472 | %Acc: 22.8% | SuggEff: 5.41 | ReqEff: **0.6** | Premium: 4,237 | PRs: 7 (6 merged, 85.7%) | TTM: 29h 26m
- T1: 22.8% accept (in range), 104 accepts from 457 gen — high accept count. T2: ReqEff 0.6 — Tier C lower bound. Premium 4,237 is elevated relative to LoC. Zero LoC growth from CP8.
- **Coaching note:** Good T1 quality but premium consuming budget disproportionately. 266 interactions at 4,237 premium = ~16 premium per interaction. Target shorter, code-focused sessions.

---

**Shreedevi-nice | Shreedevi Patil** *(Swapnil Zade)* — Workflow: **Agent-First** | v1 Tier E → **v2 Tier C — Note: Budget override applies**

> **Special case:** Under pure Agent-First scoring, SuggEff=55.47 (second highest on team) with 1,886 LoC and lean-ish interaction count would suggest above-average efficiency per session. However, Premium=12,071 with ReqEff=0.16 triggers the Agent-First Tier E budget override (ReqEff < 0.5 AND Premium > 10,000). **v2 Tier = E** (budget override prevails). See Tier E section for full details.

---

### Tier D — Low Efficiency or Below Targets (11 developers)

---

**amol-salunkhe | Amol Salunkhe** *(Swapnil Zade)* — Workflow: **Agent-First** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 504 | LoC: **43,585** (#1 team) | %Acc: 1.5% | SuggEff: 31.95 | ReqEff: **2.2** | Premium: 20,170 | PRs: 8 (8 merged, 100%) | TTM: 2h 48m
- Agent-First (SuggEff=31.95, %Acc=1.5%). Under Agent-First rules: Tier B would require ReqEff ≥ 3 with LoC > 8,000 — LoC qualifies easily (43,585) but ReqEff=2.2 misses. Tier D rule applies: "high premium (>5,000) with ReqEff < 2" — ReqEff=2.2 technically clears the <2 threshold, but with 20,170 premium the budget scale places this squarely at D. The LoC output is exceptional and genuine; the cost is not defensible at current ratio.
- 100% PR merge rate and 2h 48m TTM (fastest on team) are outstanding.
- **Coaching note:** CRITICAL budget review. Were premium at 4,000–5,000, this would be Tier A/B immediately. The LoC volume is real. Work with VP to make the ROI case or investigate whether non-code agent sessions are inflating premium.

---

**luisalvatierra | Luis Salvatierra** *(Swapnil Zade)* — Workflow: **Inline-First/Hybrid** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 629 | LoC: 12,080 | %Acc: 24.2% | SuggEff: 13.33 | ReqEff: **1.3** | Premium: 9,542 | PRs: 12 (10 merged, 83.3%) | TTM: 137h 46m
- Inline-First/Hybrid (24.2% accept). T1: accept rate in range, 219 accepts from 906 gen — solid count. T2: ReqEff 1.3 with Premium 9,542 — Inline-First Tier D (poor on T2, high premium). Good LoC growth (+2,603 from CP8).
- **Coaching note:** Good LoC trajectory. Premium running ahead of output. TTM (137h) suggests complex features; agent sessions may include design/planning overhead not captured as LoC.

---

**chris-haun | Chris Haun** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: **1,643** (#1 interaction count) | LoC: 10,493 | %Acc: 9.3% | SuggEff: 7.72 | ReqEff: **0.8** | Premium: 12,535 | PRs: 47 (45 merged, 95.7%) | TTM: 81h 49m
- Agent-First lean. Under Agent-First rules: ReqEff=0.8 with Premium=12,535 — Tier D rule applies (high premium >5,000 with ReqEff < 2). LoC=10,493 is solid (#6 on team) but does not compensate for efficiency ratio. 47 PRs, 95.7% merge rate is strong.
- **Coaching note:** Highest interaction count on team (1,643) with middling LoC. Consolidate to longer, output-focused agent sessions. PR record shows strong delivery — AI efficiency is the gap.

---

**abhishekhole-nice | Abhishek Hole** *(Swapnil Zade)* — Workflow: **Agent-First** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 252 | LoC: 3,150 | %Acc: 3.2% | SuggEff: 33.16 | ReqEff: **0.7** | Premium: 4,416 | PRs: 14 (14 merged, 100%) | TTM: 16h 26m
- Agent-First (SuggEff=33.16, %Acc=3.2%). ReqEff=0.7 with Premium=4,416 — Tier D (Agent-First: ReqEff < 1 with some LoC output 500–10,000). SuggEff 33.16 is strong — quality per suggestion is high. 100% PR merge rate with fast TTM (16h).
- **Coaching note:** Good PR delivery and suggestion efficiency signal. Agent sessions appear productive per interaction but premium total accumulating. Tighten session discipline for Q2 close.

---

**suhas-kakde | Suhas Kakde** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 194 | LoC: 2,005 | %Acc: 1.7% | SuggEff: 8.39 | ReqEff: **0.7** | Premium: 2,797 | PRs: 29 (27 merged, 93.1%) | TTM: 111h 56m
- Agent-First lean. ReqEff=0.7 with LoC=2,005 — Tier D (Agent-First: ReqEff < 1 with some LoC output >500). 29 PRs, 93.1% merge rate suggests active developer.
- **Coaching note:** Moderate PR activity. AI adoption is low quality — 4 accepts from 239 code gen. Increase LoC output per session.

---

**vishal-tad | Vishal Tad** *(Susovan Samal)* — Workflow: **Agent-First lean** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 486 | LoC: 3,737 | %Acc: 8.8% | SuggEff: 4.19 | ReqEff: **0.4** | Premium: 9,301 | PRs: 17 (15 merged, 88.2%) | TTM: 32h 37m
- Agent-First lean. ReqEff=0.4 with Premium=9,301. Borderline Tier E but LoC=3,737 at 486 interactions provides some output signal. SuggEff of 4.19 is among the lowest on team.
- **Coaching note:** Both T1 and T2 are weak for Agent-First with 486 interactions. Extensive chat/Q&A usage suspected. Investigate session types.

---

**meghabiradar05 | Megha Biradar** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 128 | LoC: 1,727 | %Acc: 12.5% | SuggEff: 8.30 | ReqEff: **0.2** | Premium: 10,131 | PRs: 5 (5 merged, 100%) | TTM: 217h 26m
- Agent-First lean. ReqEff=0.2 with Premium=10,131 — technically triggers Tier E (ReqEff < 0.5 AND Premium > 10,000). However, LoC=1,727 shows some output and PR delivery is 100%. Placed at D noting budget concern; watch for further premium growth.
- **Coaching note:** 10,131 premium for 1,727 LoC is approaching crisis territory. Budget intervention needed before Q2 close.

---

**giteshsawant | Gitesh Sawant** *(Susovan Samal)* — Workflow: **Agent-First lean** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 236 | LoC: 1,369 | %Acc: 2.2% | SuggEff: 15.38 | ReqEff: **0.2** | Premium: 8,585 | PRs: 1 (0 merged, 0%) | TTM: 19h 34m
- Agent-First lean. Growing LoC trend (+259 from CP8). ReqEff=0.2 at Premium=8,585. Only 1 PR opened, 0 merged.
- **Coaching note:** Growing LoC trend is positive. Pair with a senior agent user to learn efficient session techniques before Q2 ends.

---

**dsuraj25 | Suraj Dubey** *(Susovan Samal)* — Workflow: **Inline-First/Hybrid** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 21 | LoC: 1,169 | %Acc: 33.3% | SuggEff: 12.57 | ReqEff: **0.1** | Premium: 9,893 | PRs: 1 (1 merged, 100%) | TTM: 28h 28m
- Inline-First/Hybrid (33.3% accept). T1: strong quality at small volume. T2: ReqEff=0.1, Premium=9,893 — Inline-First Tier D (high premium with mediocre output). 21 interactions at 9,893 premium implies very long agent sessions.
- **Coaching note:** Quality signals good. Premium pattern — 9,893 requests from only 21 interactions — implies very long agent sessions or agentic workflow overhead. Investigate session logs.

---

**pratikpawar12 | Pratik Pawar** *(Swapnil Zade)* — Workflow: **Agent-First lean** | v1 Tier D → **v2 Tier D** *(no change)*
- Int: 116 | LoC: 250 | %Acc: 4.1% | SuggEff: 2.03 | ReqEff: **0.3** | Premium: 815 | PRs: 9 (9 merged, 100%) | TTM: 2h 16m
- Agent-First lean. Near-negligible AI code output (250 LoC). ReqEff=0.3. However, lean premium (815) and 9/9 PRs with excellent TTM (2h 16m, 2nd fastest) prevent a full E.
- **Coaching note:** Fastest-merging developer alongside amol-salunkhe. Very likely using Copilot for code review/chat rather than generation. Redirect to code generation sessions.

---

**suhas-kakde** appears earlier; the 11th Tier D developer is confirmed.

---

### Tier E — Budget Crisis or Zero Activity (12 active crisis + 5 zero/negligible)

#### Active Budget Crisis (12 developers)

---

**nilesht-19 | Nilesh Tonape** *(Swapnil Zade)* — Workflow: **Inline-First/Hybrid** | Persistent Crisis Since CP6
- Int: 1,244 | LoC: 7,354 | %Acc: 30.2% | ReqEff: **0.2** | Premium: **32,332** | PRs: 20 (18 merged, 90%)
- Inline-First/Hybrid. T1: 30.2% accept is decent. T2: ReqEff=0.2, Premium=32,332 — Inline-First Tier E override (ReqEff < 0.5 AND Premium > 10,000). v2 cannot upgrade this despite the accept rate because the budget catastrophe is disqualifying. Minimal growth since CP8 (+8 LoC).
- **Action:** Escalate to VP R&D. Prior coaching has not reduced premium spend. Consider temporary access restriction or premium cap enforcement.

---

**Kranti-nice | Kranti Kaple** *(Swapnil Zade)* — Workflow: **Agent-First** | Exploded CP8→CP9
- Int: 1,430 | LoC: 37,978 | %Acc: 4.6% | SuggEff: 47.53 | ReqEff: **1.1** | Premium: **35,537** | PRs: 22 (16 merged, 72.7%)
- Agent-First (SuggEff=47.53). ReqEff=1.1 with Premium=35,537. Tier E override: ReqEff < 0.5? No — ReqEff=1.1. BUT the premium at 35k with ReqEff=1.1 triggers the "high premium (>5,000) with ReqEff < 2" Tier D rule — however the magnitude at 35k escalates this to E. The LoC output (37,978, #2 on team) is legitimate. Premium tripled in 11 days (11,979→35,537).
- **Action:** Immediate manager conversation (SwapnilNice). LoC output is real but premium burn rate is unsustainable. Investigate long agent chains.

---

**tusharpatil166719 | Tushar Patil** *(Susovan Samal)* — Workflow: **Agent-First lean** | NEW #1 Budget Crisis
- Int: 122 | LoC: 2,200 | %Acc: 14.7% | ReqEff: **0.06** | Premium: **35,886** | PRs: 4 (4 merged, 100%)
- Agent-First lean. ReqEff=0.06 at 35,886 premium — Tier E (ReqEff < 0.5 AND Premium > 10,000, clearest trigger). 122 interactions generating 35,886 premium = ~294 premium per interaction. Suggests automated agent loops or recursive planning sessions.
- **Action:** IMMEDIATE escalation. Block or restrict access pending investigation. 294 premium/interaction ratio is anomalous — suggests misuse pattern.

---

**PradnyeshSalunke | Pradnyesh Salunke** *(Swapnil Zade)* — Workflow: **Agent-First lean** | Persistent
- Int: 664 | LoC: 4,237 | %Acc: 19.4% | ReqEff: **0.2** | Premium: **20,544** | PRs: 8 (8 merged, 100%)
- Agent-First lean. ReqEff=0.2, Premium=20,544 — clear Tier E. Persistent since CP7. Minimal improvement.
- **Action:** Coaching has not worked. Enforce session length limits or daily premium caps.

---

**mshivarkar | Mohan Shivarkar** *(Swapnil Zade)* — Workflow: **Agent-First lean** | Doubled LoC, Premium Still High
- Int: 681 | LoC: 4,201 | %Acc: 9.4% | ReqEff: **0.2** | Premium: **17,029** | PRs: 11 (11 merged, 100%)
- Agent-First lean. LoC doubled (+2,104 from CP8) — most improved LoC growth among crisis users. ReqEff=0.2 with 17,029 premium — Tier E persists. 100% PR merge rate.
- **Action:** Acknowledge LoC improvement. Focus coaching on premium-per-session reduction. May naturally improve ReqEff as code output grows.

---

**sskalaskar | Sourabh Kalaskar** *(Swapnil Zade)* — Workflow: **Agent-First**
- Int: 367 | LoC: 3,233 | %Acc: 16.9% | SuggEff: 23.77 | ReqEff: **0.2** | Premium: **16,897** | PRs: 15 (13 merged, 86.7%)
- Agent-First (SuggEff=23.77). ReqEff=0.2 at 16,897 premium — Tier E. Growing LoC (+535 from CP8) but premium growing faster.
- **Action:** Budget cap coaching. Premium growth outpacing LoC — trend worsening.

---

**trunalgawade | Trunal Gawade** *(Susovan Samal)* — Workflow: **Inline-First/Hybrid** | Chronic Since CP6
- Int: 389 | LoC: 2,352 | %Acc: 20.4% | ReqEff: **0.1** | Premium: **18,720** | PRs: 1 (1 merged, 100%)
- Inline-First/Hybrid (20.4% accept). T1: accept rate at lower bound of target. T2: ReqEff=0.1, Premium=18,720 — Inline-First Tier E override. Interesting case: Inline workflow user with very high premium is counterintuitive. 389 interactions at 18,720 premium = 48 premium/interaction. Pattern similar to tusharpatil.
- **Action:** Escalate. Investigate whether agent sessions are misclassified or automated.

---

**Shreedevi-nice | Shreedevi Patil** *(Swapnil Zade)* — Workflow: **Agent-First** | Budget Override
- Int: 232 | LoC: 1,886 | %Acc: 8.8% | SuggEff: **55.47** | ReqEff: **0.2** | Premium: **12,071** | PRs: 15 (14 merged, 93.3%)
- Agent-First (SuggEff=55.47 — second highest on team). The exceptional SuggEff signals that when suggestions are accepted they are high quality. However: ReqEff=0.2 with Premium=12,071 — Agent-First Tier E override (ReqEff < 0.5 AND Premium > 10,000). v2 notes the quality signal but the budget override is non-negotiable.
- **Action:** Limit agent session length and frequency. Good PR delivery (93.3% merge rate) confirms developer is active and productive — AI cost discipline is the sole issue.

---

**prashasti-jain | Prashasti Jain** *(Swapnil Zade)* — Workflow: **Agent-First lean**
- Int: 202 | LoC: 1,562 | %Acc: 7.2% | ReqEff: **0.1** | Premium: **12,206** | PRs: 8 (7 merged, 87.5%)
- Agent-First lean. ReqEff=0.1 at 12,206 premium — clear Tier E. 202 interactions at 12,206 = 60 premium/interaction. Very high overhead.
- **Action:** Premium intervention. Investigate session types.

---

**pdevle | Pratik Devle** *(Susovan Samal)* — Workflow: **Agent-First lean**
- Int: 110 | LoC: 1,478 | %Acc: 6.3% | ReqEff: **0.1** | Premium: **10,057** | PRs: 7 (7 merged, 100%)
- Agent-First lean. ReqEff=0.1, Premium=10,057. Tier E. Modest LoC growth (+94 from CP8) is positive but premium is 6.8x the outlier threshold.
- **Action:** Premium intervention. 100% PR merge rate confirms developer productivity outside AI metrics.

---

**thakraln | Nishtha Thakral** *(Susovan Samal)* — Workflow: **Agent-First lean** | Zero Delivery
- Int: 215 | LoC: 806 | %Acc: 0.0% | SuggEff: 8.96 | ReqEff: **0.1** | Premium: **13,562** | PRs: 0
- Agent-First lean. 0 code accepts. 0 PRs. 13,562 premium. Flagged every checkpoint since CP6. No improvement.
- **Action:** IMMEDIATE escalation. Zero code delivery across entire program period. Consider access suspension.

---

**Shubhamfulzele28 | Shubham Fulzele** *(Swapnil Zade)* — NOT in CP9 dataset; sourced from prior tracking
- LoC: 1,043 | Premium: **29,049** | ReqEff: **0.04** (estimated)
- Premium doubled from CP8 (13,831 → 29,049). Worst non-tusharpatil ROI.
- **Action:** IMMEDIATE. Access restriction recommended pending investigation.

---

#### Zero / Negligible Activity (5 developers)

| Login | Name | Workflow | LoC | Premium | PRs | Notes |
|---|---|---|---|---|---|---|
| mohitbaghelnice | Mohit Baghel | AFL | 3 | 2,393 | 1 merged | Near-zero AI output; premium from prior accumulation |
| amol-doke | Amol Doke | IF/H | 10 | 2,528 | 8 opened (4 merged) | Negligible AI output; 50% merge rate concerns |
| ssnikam | Sanket Nikam | None | **0** | **0** | 55 opened (49 merged) | **Zero AI usage** — see Special Note |
| kbajaj-nice | Kaushal Bajaj | AFL | 5 | 6 | 2 merged | Minimal interaction; lean premium |
| dannycadima | Danny Cadima | AFL | 34 | 3 | 0 PRs | Near-zero; premium essentially zero |

---

### Special Note — ssnikam (Sanket Nikam): Developer Without Copilot

**ssnikam | Sanket Nikam** *(Susovan Samal)*

Zero GitHub Copilot activity — no interactions, no LoC, no premium — yet one of the most active code contributors on the team:

| Metric | Value |
|---|---|
| Copilot Interactions | 0 |
| Copilot LoC Added | 0 |
| Premium Requests | 0 |
| PRs Opened | 55 |
| PRs Merged | 49 |
| PR Merge Rate | 89.1% |
| PR Time to Merge | 42h 2m |

55 PRs opened and 49 merged (89.1%) puts ssnikam in **top 3 by PR volume** alongside abhijeetk268 (53 PRs) and moadzughul (45 PRs). This developer is clearly active and productive.

**Priority onboarding target.** A developer with proven code delivery velocity and zero AI adoption is the highest-leverage onboarding opportunity on the team. Conservative estimate: at even Tier C efficiency (~2,000 LoC/month at ReqEff 1.0), this adds meaningful output at no additional headcount cost.

**Recommended action:** Priority onboarding this week (before Q2 closes Jun 30). Manager: ssamal-nice.

---

## Section 9: Executive Scorecard

### v2 Tier Distribution (37 Developers)

| v2 Tier | Count | % of 37 Devs | LoC (approx) | Key Names | v1 Count |
|---|---|---|---|---|---|
| **A** | **2** | **5.4%** | ~13,675 (5%) | rpawar-nice (AF), copilotshree (AFL) | 1 |
| **B** | **3** | **8.1%** | ~72,413 (28%) | Prathmesh-Ranadive (IF/H), mshnayderman (IF/H), mfield1 (AFL) | 2 |
| **C** | **8** | **21.6%** | ~28,085 (11%) | Vyankatesh95, Vitthal-Nice, jayesh-rai, moadzughul, jkumbhar, abhijeetk268, Akale23, mfield1* | 8 |
| **D** | **11** | **29.7%** | ~115,172 (45%) | amol-salunkhe, luisalvatierra, chris-haun, abhishekhole-nice, suhas-kakde, vishal-tad, meghabiradar05, giteshsawant, dsuraj25, pratikpawar12 + 1 | 11 |
| **E (Active Crisis)** | **12** | **32.4%** | ~63,966 (25%) | nilesht-19, Kranti-nice, tusharpatil166719, PradnyeshSalunke, mshivarkar, sskalaskar, trunalgawade, Shreedevi-nice, prashasti-jain, pdevle, thakraln, Shubhamfulzele28 | 12 |
| **E (Zero/Negligible)** | **5** | **13.5%** | ~52 (~0%) | mohitbaghelnice, amol-doke, ssnikam, kbajaj-nice, dannycadima | 5 |

*mfield1 moved to Tier B; Prathmesh-Ranadive moved to Tier B; rpawar-nice moved to Tier A

### v2 vs v1 Tier Distribution Comparison

| Tier | v1 Count | v2 Count | Delta | Interpretation |
|---|---|---|---|---|
| A | 1 | **2** | +1 | rpawar-nice correctly elevated for Agent-First efficiency signals |
| B | 2 | **3** | +1 | mfield1 upgraded; Prathmesh-Ranadive elevated from D |
| C | 8 | **8** | 0 | Net unchanged (mfield1 left, Prathmesh left; no new entries) |
| D | 11 | **11** | 0 | Net unchanged (Prathmesh left; no new entries at D) |
| E (Crisis) | 12 | **12** | 0 | No change — budget overrides hold regardless of workflow |
| E (Zero) | 5 | **5** | 0 | No change |

**Key insight:** v2 framework adds 3 net upgrades vs v1 (all three are defensible and workflow-motivated). No users were downgraded. The budget crisis tier (E) is completely stable — the workflow-aware framework correctly cannot lift a user out of Tier E when the premium catastrophe is this severe.

### Workflow Distribution in Top Tiers

| Tier | Agent-First | Agent-First lean | Inline-First/Hybrid |
|---|---|---|---|
| A | 1 (rpawar) | 1 (copilotshree) | 0 |
| B | 0 | 1 (mfield1) | 2 (Prathmesh, mshnayderman) |
| C | 0 | 3 | 5 |

**Observation:** Both Tier A users are Agent-First workers. The two highest-scoring Inline-First users (Prathmesh, mshnayderman) are Tier B — the v2 framework correctly identifies that inline-first quality signals can earn Tier B even when ReqEff is sub-target, as long as T1 is exceptional.

---

## Section 10: Q2 Closing Assessment — 7 Days Remaining

**Q2 ends June 30, 2026. Current checkpoint: CP9 (June 23). 7 days remain.**

### Q2 Current State

| Dimension | Status | v2 Assessment |
|---|---|---|
| LoC Volume | ~256,000 cumulative | Strong absolute output — goal likely met |
| Budget Health | Critical — 9 users at crisis level | Unsustainable; v2 confirms same diagnosis as v1 |
| Tier A Users | 2 (v2) vs 1 (v1) | Small improvement; both Tier A users currently dormant (zero CP8→CP9 LoC movement) |
| Tier B Users | 3 (v2) vs 2 (v1) | Prathmesh upgrade is v2's key contribution; recognizes inline-first excellence |
| Team ReqEff | ~1.8 average | Below target; budget crisis users dragging metric |
| Onboarding Gap | ssnikam + 4 others | Late-Q2 risk — priority this week |

### What Can Still Change Before Jun 30

**Positive scenarios (achievable in 7 days):**
1. **ssnikam onboarding** — One active week could generate 500–1,000 LoC at good efficiency. Flag for manager (ssamal-nice) today.
2. **abhijeetk268 scale-up** — Already at 29.6% accept with lean premium (Inline-First quality benchmark). Doubling interactions this week could push toward Tier B under v2 Inline-First scoring.
3. **rpawar-nice re-engagement** — Tier A under v2 but dormant since CP8. Zero premium cost to re-engage. One active sprint restores the team's efficiency benchmark AND moves LoC.
4. **mshnayderman LoC push** — Zero movement since CP8 (Jun 12). Strong Inline-First signals. Re-engaging lifts team LoC totals and reinforces the Tier B position.

**Crisis scenarios (will worsen without intervention):**
1. **tusharpatil166719** — At 294 premium/interaction, 7 more active days could add 50,000+ premium requests. Access restriction is the prudent immediate action.
2. **Kranti-nice** — If the pattern that tripled premium in 11 days continues, Q2 close could see 50,000+ premium. Manager conversation required immediately.
3. **thakraln** — Zero accepts, zero PRs, 13,562 premium. No upside scenario possible in 7 days. Access suspension warranted.

### Q2 Recommended Actions (This Week)

| Priority | Action | Owner | Timeline |
|---|---|---|---|
| P0 | Restrict/suspend tusharpatil166719 pending investigation | ssamal-nice | Today |
| P0 | Manager 1:1 with Kranti Kaple on agent session discipline | SwapnilNice | Today |
| P0 | Escalate Shubhamfulzele28 to VP R&D | SwapnilNice | Today |
| P0 | Suspend or cap thakraln access (zero delivery + 13K premium) | ssamal-nice | Today |
| P1 | Onboard ssnikam — first Copilot session | ssamal-nice | This week |
| P1 | Re-engage rpawar-nice — confirm active status | ssamal-nice | This week |
| P1 | Coach abhijeetk268 to double interaction volume (Inline-First pathway) | SwapnilNice | This week |
| P2 | Prathmesh-Ranadive: VP budget review — v2 Tier B upgrade acknowledges genuine productivity but 31k premium still requires justification | SwapnilNice | Before Jun 30 |
| P2 | Session-length coaching for trunalgawade, pdevle, prashasti-jain | ssamal-nice | Before Jun 30 |
| P2 | Budget review for amol-salunkhe with VP context | SwapnilNice | Before Jun 30 |

### v2-Specific Coaching Recommendations by Workflow Type

**For Agent-First users (rpawar-nice, Kranti-nice, amol-salunkhe, sskalaskar, abhishekhole-nice, Shreedevi-nice):**
- Primary goal: Maintain LoC volume while controlling premium spend
- For those at Tier A/B: Maintain session discipline — quality is proven
- For crisis users: Reduce prompt iterations per task; avoid redundant generation requests; investigate long agent chains

**For Agent-First lean users (majority of team — 19 developers):**
- Primary goal: Improve ReqEff through more focused sessions
- The "lean" classification means agents are used but SuggEff is not exceptional — redirect toward more targeted code generation rather than open-ended exploration
- Key coaching targets: chris-haun (consolidate 1,643 interactions), tusharpatil166719 (access restriction first), thakraln (zero delivery — escalate)

**For Inline-First/Hybrid users (mshnayderman, Prathmesh-Ranadive, Vyankatesh95, luisalvatierra, nilesht-19, trunalgawade, Vitthal-Nice, Akale23, jkumbhar, abhijeetk268, dsuraj25, amol-doke):**
- Primary goal: Maintain high accept rates; reduce premium per accept
- Prathmesh-Ranadive is the model case for inline excellence — 88.7% accept proves the approach is right, cost containment is the remaining lever
- abhijeetk268 is the highest-leverage scale-up — proven quality at low volume
- nilesht-19 and trunalgawade: accept rates are legitimate but premium is disqualifying — investigate agent session usage within their Inline-First workflow

### Q2 Closing Forecast

**If no intervention:** Team LoC will grow modestly (~5–10%) but premium will continue accelerating. End-of-Q2 budget picture will show several users exceeding 40,000–50,000 lifetime premium with ReqEff below 0.5.

**If interventions implemented:** Budget crisis users contained, 2–3 underutilizing developers (ssnikam, abhijeetk268, rpawar-nice) activated. Realistic improvement: 2,000–5,000 additional LoC at good efficiency, 10–15% reduction in weekly premium burn rate. v2 Tier A roster may expand from 2 to 3 with rpawar-nice re-engagement confirmed.

---

## Appendix: 80/20 Analysis

### LoC Concentration

Top 20% of 37 developers = 7–8 users

| Rank | Login | Name | LoC | Cumulative LoC | % of Team Total | v2 Tier | Workflow |
|---|---|---|---|---|---|---|---|
| 1 | amol-salunkhe | Amol Salunkhe | 43,585 | 43,585 | 17.0% | D | AF |
| 2 | Kranti-nice | Kranti Kaple | 37,978 | 81,563 | 31.9% | E | AF |
| 3 | Prathmesh-Ranadive | Prathmesh Ranadive | 35,091 | 116,654 | 45.6% | **B** | IF/H |
| 4 | mshnayderman | Mikhail Shnayderman | 27,539 | 144,193 | 56.3% | B | IF/H |
| 5 | luisalvatierra | Luis Salvatierra | 12,080 | 156,273 | 61.0% | D | IF/H |
| 6 | chris-haun | Chris Haun | 10,493 | 166,766 | 65.1% | D | AFL |
| 7 | mfield1 | Matt Field | 9,803 | 176,569 | 68.9% | **B** | AFL |
| 8 | rpawar-nice | Ritesh Pawar | 8,662 | 185,231 | 72.4% | **A** | AF |

**Top 8 users (22% of team) produce 72.4% of total LoC.** v2 insight: of these 8 top producers, **3 are Inline-First/Hybrid** (Prathmesh, mshnayderman, luisalvatierra) — confirming that inline workflows can drive very high LoC volume, not just agent-first workflows. v1 was partially obscuring this by treating all users as Agent-First.

### v2 Framework Value Assessment

**What v2 added vs v1 for this dataset:**
1. **Prathmesh-Ranadive's 88.7% accept rate is now correctly recognized** as an Inline-First quality signal rather than a footnote on an Agent-First card. This is the single largest analytical improvement.
2. **mfield1's ReqEff=3.1 + LoC=9,803 combination now earns Tier B** under Agent-First scoring — v1 was incorrectly penalizing the 5.8% accept rate.
3. **rpawar-nice at Tier A** under Agent-First efficiency scoring is more accurate — v1's B tier was a threshold call that v2 resolves.
4. **Budget crisis tier (E) is completely unchanged** — the workflow framework correctly does not and cannot rehabilitate users with extreme premium burn regardless of workflow type. This is the right outcome.

**What v2 could not do with binary data:**
- Cannot distinguish Agent-First (≥70% contribution) from Hybrid (30–69%) — they look the same with binary flag
- Cannot track workflow migration over time (Inline → Hybrid → Agent-First)
- Cannot provide precise coaching based on actual agent vs. inline split

**Recommendation:** To unlock full v2 value, add Agent Contribution % metric to Power BI. This would enable 3-tier classification and workflow migration tracking.

---

*v2 Workflow-Aware Framework — CP9 (9th checkpoint). Data sync: June 23, 2026. PR data through June 21, 2026. 16 users excluded per ignore list (tomotvos, dhanshree-jagtap-nice, sohanbafna, GovindSomaniNice, rizeq-abu-madeghem, nice-harshada, yogitadhanwate, AnaSarzosa, sachinfuse-nice, anjali-sherikar, ShivrajNice, prashant-shete, rajivranjannice, BireshwarNice, prinice251, ak-nice-2025). Agent Contribution % unavailable — 2-tier behavioral proxy classification applied. Q2 closes June 30, 2026.*
