# GitHub Copilot Usage Analysis — v1 Standard Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Total Users:** 60 (54 active, 6 inactive) | **Framework:** v1 Standard (github-quick-benchmark.md)

---

## What Changed vs Prior Period (June 3, 2026)

| Signal | Jun 3 | Jun 8 | Delta |
|---|---|---|---|
| Active Users | ~50 | 54 | +4 |
| LoC Added (team) | ~270,000 | 344,967 | +28% |
| Accept Rate | ~16% | 15.6% | −0.4pp |
| Agent Adoption | ~96% | 98.1% | +2.1pp |
| Agent Contribution | ~85% | 86.4% | +1.4pp |
| mshnayderman ReqEff | 43.2 | 5.1 | 🔴 −88% |
| amol-salunkhe ReqEff | 40.8 | 6.4 | 🔴 −84% |
| rpawar-nice ReqEff | 20.1 | ~60.1 | 🚀 +199% |
| Kranti-nice ReqEff | ~7.6 | ~23.1 | 🚀 Breakout |

**Key themes this period:**
1. **dhanshree-jagtap-nice emerges as #1 by LoC** — 64,112 lines, 45.7 ReqEff. New leader.
2. **Budget crisis in 5 accounts** — nilesht-19 (23,108 premium), thakraln (11,112), trunalgawade (10,863), Prathmesh-Ranadive (10,733), PradnyeshSalunke (9,892). Combined 65,708 premium on low LoC output.
3. **mshnayderman anomaly** — 9.5× premium spike (565 → 5,419) with only modest LoC gain. Requires investigation.
4. **amol-salunkhe efficiency collapse** — 747 → 5,309 premium with ~3,000 LoC gain. Agent usage pattern changed dramatically.

---

## Team Overview

| Metric | Value |
|---|---|
| Initiated Interactions | 15,546 |
| LoC Added | 344,967 |
| LoC Suggested | ~83,161 |
| Code Acceptance Count | 2,787 |
| Code Generation Count | 17,877 |
| % Code Acceptance | 15.6% |
| Suggestion Efficiency | 19.30 |
| Active Users | 54 / 60 |
| Agent Adoption | 98.1% |
| Agent Contribution | 86.4% |

---

## User Classification

### Special Groups (Excluded from A–E Tier)

**Inactive (0 activity this period):**
> ak-nice-2025, amoldoke051295, BireshwarNice, mohitbaghelnice, prinice251, ssnikam

**Research (not tiered — tracked on Interactions + Premium only):**
| Login | Name | Manager | Interactions | LoC Added | Premium | Notes |
|---|---|---|---|---|---|---|
| rwalunj-nice | Rahul Walunj | Alon Vax | ~30 | 0 | ~100 | Research/tooling exploration — LoC not applicable metric |

**Managers (benchmarked on engagement + efficiency, not raw LoC):**
| Login | Name | Manager | Int | LoC Added | % Accept | ReqEff | Notes |
|---|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | Rahul Walunj | 273 | 3,140 | 4.0% | ~31.4 | Active coder-manager, high int count |
| ssamal-nice | Susovan Samal | Rahul Walunj | ~30 | 38 | ~8% | ~3.2 | Low engagement — manager role focus |
| GovindSomaniNice | Govind Somani | Piyush Shirke | 44 | 2,356 | 1.2% | ~27.7 | Active manager with agent usage |

**Non-CX Engineering Members (tracked separately):**
| Login | Name | Manager | Int | LoC Added | % Accept | ReqEff | Notes |
|---|---|---|---|---|---|---|---|
| copilotshree | Shraddha Kale | Swapnil Zade | ~750 | 5,013 | ~4.8% | ~8.8 | Non-CX — tracked but not tiered with CX team |
| rajivranjannice | Rajiv Ranjan | (Non-CX) | ~15 | ~50 | ~10% | ~5 | Non-CX |
| prashant-shete | Prashant Shete | (Non-CX) | ~5 | ~10 | 0.0% | ~2 | Non-CX |

---

## Full Developer Metrics Table (47 Developers)

> **Column key:** Int = Initiated Interactions | LoC = LoC Added | LoC Sugg = LoC Suggested | Accept = Code Acceptance Count | %Acc = % Code Acceptance | SuggEff = Suggestion Efficiency (LoC/CodeGen) | Premium = Premium Requests | ReqEff = Request Efficiency (LoC/Premium) | Workflow = inferred (no per-user Agent Contribution % in dashboard)

> **Workflow inference:** Agent-First = %Acc < 5% + Int ≥ 50 + LoC ≥ 500 | Inline-First = %Acc ≥ 25% | Hybrid = all others

| Login | Name | Manager | Int | LoC | %Acc | SuggEff | Premium | ReqEff | Workflow | v1 Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| dhanshree-jagtap-nice | Dhanshree Jagtap | G. Somani | 399 | 64,112 | 6.7% | 76.32 | ~1,403 | 45.7 | Hybrid | **A** |
| tomotvos | Tom Otvos | Bala Katta | 95 | 9,191 | 0.8% | 77.89 | ~109 | 84.3 | Agent-First | **A** |
| amol-salunkhe | Amol Salunkhe | Swapnil Zade | 423 | 34,037 | 1.6% | 29.42 | 5,309 | 6.4 | Agent-First | **A** ⚠️ |
| Kranti-nice | Kranti Kaple | Swapnil Zade | 1,182 | 27,733 | 1.3% | 39.01 | ~1,200 | ~23.1 | Agent-First | **A** |
| mshnayderman | Mikhail Shnayderman | Alon Vax | 164 | 27,539 | 27.8% | 60.79 | 5,419 | 5.1 | Inline-First | **A** ⚠️ |
| nice-harshada | Harshada Bagane | V. Mahore | ~1,400 | 23,408 | ~2.0% | ~11.7 | ~1,700 | ~13.8 | Agent-First | **A** |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | Tomer Daniel | ~800 | 15,876 | ~0.9% | ~23.5 | ~675 | ~23.5 | Agent-First | **A** |
| mfield1 | Matt Field | Swapnil Zade | ~600 | ~9,300 | ~5.5% | ~14.3 | ~650 | ~14.3 | Hybrid | **A** |
| rpawar-nice | Ritesh Pawar | S. Samal | 77 | 8,662 | 7.7% | 60.57 | ~144 | ~60.1 | Hybrid | **A** |
| Vitthal-Nice | Vitthal Devkar | S. Samal | ~160 | ~2,800 | ~44% | ~14 | ~200 | ~14 | Inline-First | **A** |
| Akale23 | Amulya Kale | S. Samal | ~200 | ~2,600 | ~18.8% | ~6.7 | ~390 | ~6.7 | Hybrid | **A** |
| AnaSarzosa | Ana Sarzosa | S. Dalence | 139 | 2,021 | 6.6% | 7.86 | ~257 | ~7.9 | Hybrid | **A** |
| yogitadhanwate | Yogita Dhanwate | G. Somani | ~400 | ~8,000 | ~10.7% | ~13.8 | ~580 | ~13.8 | Hybrid | **B** |
| sohanbafna | Sohan Bafna | P. Shirke | 11 | 467 | 7.7% | 35.92 | ~11 | ~42.5 | Hybrid | **B** |
| luisalvatierra | Luis Salvatierra | Swapnil Zade | ~480 | ~4,800 | ~17.6% | ~9.2 | ~1,655 | 2.9 | Hybrid | **B** |
| anjali-sherikar | Anjali Sherikar | G. Somani | ~120 | ~1,800 | ~12% | ~6 | ~250 | ~7.2 | Hybrid | **B** |
| jayesh-rai | Jayesh Rai | Swapnil Zade | ~90 | ~2,500 | ~4% | ~19 | ~130 | ~19.2 | Agent-First | **B** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Swapnil Zade | ~100 | 27,052 | 25.4% | ~25 | 10,733 | 2.5 | Inline-First | **C** |
| chris-haun | Chris Haun | Swapnil Zade | ~1,000 | ~10,359 | ~11.7% | ~10.4 | ~3,700 | 2.8 | Hybrid | **C** |
| jkumbhar | Jyoti Kumbhar | Swapnil Zade | ~230 | ~2,000 | ~20% | ~20 | ~120 | ~16.7 | Hybrid | **C** |
| Vyankatesh95 | Vyankatesh Khadakkar | Swapnil Zade | 423 | 4,177 | 34.1% | 30.27 | ~150 | ~27.8 | Inline-First | **C** |
| dsuraj25 | Suraj Dubey | S. Samal | ~15 | ~510 | 0.0% | ~14.6 | ~35 | ~14.6 | Hybrid | **C** |
| abhijeetk268 | Abhijeet Kolhe | Swapnil Zade | 38 | 656 | 29.6% | 24.30 | ~30 | ~21.9 | Inline-First | **C** |
| sachinfuse-nice | Sachin Fuse | G. Somani | ~300 | ~2,200 | ~1.8% | ~8.8 | ~250 | ~8.8 | Agent-First | **D** |
| abhishekhole-nice | Abhishek Hole | Swapnil Zade | 167 | 2,936 | 0.0% | 53.38 | ~170 | ~17.3 | Agent-First | **D** |
| vishal-tad | Vishal Tad | Swapnil Zade | ~30 | ~2,900 | ~4.8% | ~23.2 | ~125 | ~23.2 | Hybrid | **D** |
| pdevle | Pratik Devle | S. Samal | ~35 | ~1,100 | ~7% | ~15.7 | ~70 | ~15.7 | Hybrid | **D** |
| moadzughul | Moad Alzughul | Swapnil Zade | ~130 | ~3,100 | ~2.8% | ~14.8 | ~210 | ~14.8 | Agent-First | **D** |
| tusharpatil166719 | Tushar Patil | S. Samal | ~75 | ~1,900 | ~12% | ~19 | ~100 | ~19 | Hybrid | **D** |
| meghabiradar05 | Megha Biradar | Swapnil Zade | ~55 | ~1,700 | ~5.5% | ~15.5 | ~110 | ~15.5 | Hybrid | **D** |
| mshivarkar | Mohan Shivarkar | Swapnil Zade | ~100 | 2,018 | ~22% | ~40.4 | 3,480 | 0.6 | Hybrid | **D** |
| sgite-wfm | Shubham Gite | S. Samal | ~35 | 329 | 53.5% | ~0.94 | 1,411 | 0.2 | Inline-First | **D** |
| smishra-nice | Shridhar Mishra | Rahul Walunj | ~80 | 155 | 78.3% | 6.74 | ~25 | ~6.2 | Inline-First | **D** |
| nilesht-19 | Nilesh Tonape | Swapnil Zade | 1,140 | 7,160 | 29.5% | ~18.2 | 23,108 | 0.3 | Inline-First | **E** |
| thakraln | Nishtha Thakral | S. Samal | ~80 | ~1,111 | 0.0% | ~55.6 | 11,112 | 0.1 | Agent-First | **E** |
| trunalgawade | Trunal Gawade | S. Samal | ~120 | ~1,086 | ~23% | ~3.9 | 10,863 | 0.1 | Hybrid | **E** |
| PradnyeshSalunke | Pradnyesh Salunke | Swapnil Zade | ~320 | ~2,968 | ~25.4% | ~16.5 | 9,892 | 0.3 | Inline-First | **E** |
| sskalaskar | Sourabh Kalaskar | Swapnil Zade | ~190 | ~2,700 | ~15% | ~33.8 | ~85 | ~31.8 | Hybrid | **E** |
| ShivrajNice | Shivraj Bahirat | G. Somani | ~60 | ~450 | ~11% | ~3 | ~150 | ~3 | Hybrid | **E** |
| giteshsawant | Gitesh Sawant | Swapnil Zade | ~20 | ~50 | ~10% | ~2.5 | ~20 | ~2.5 | Hybrid | **E** |
| ShubhamFulzele28 | Shubham Fulzele | Swapnil Zade | 117 | 739 | 0.0% | 52.79 | ~120 | ~6.2 | Agent-First | **E** |
| Shreedevi-nice | Shreedevi Patil | Swapnil Zade | 195 | 1,416 | 11.1% | 52.44 | ~200 | ~7.1 | Hybrid | **E** |
| prashasti-jain | Prashasti Jain | Swapnil Zade | ~30 | ~900 | ~8% | ~25.7 | ~35 | ~25.7 | Hybrid | **E** |
| suhas-kakde | Suhas Kakde | Swapnil Zade | ~190 | 1,639 | ~1.8% | ~6.3 | ~265 | ~6.2 | Agent-First | **E** |
| pratikpawar12 | Pratik Pawar | Swapnil Zade | ~115 | 250 | ~4.2% | ~1.8 | ~140 | ~1.8 | Hybrid | **E** |
| kbajaj-nice | Kaushal Bajaj | S. Samal | ~5 | 5 | ~15.5% | ~0.11 | ~45 | ~0.11 | Hybrid | **E** |
| dannycadima | Danny Cadima | Swapnil Zade | ~5 | 34 | ~3.8% | ~1.1 | ~30 | ~1.1 | Hybrid | **E** |

---

## Tier Groupings

### 🌟 Tier A — Top Performers (12 developers)

> Criteria: (Agent-First: strong LoC + ReqEff > 10) OR (Inline-First/Hybrid: % Accept 20–35% + ReqEff > 10)
> Agent-First exception: % Accept benchmark skipped — evaluate on LoC volume + Request Efficiency instead.

---

**dhanshree-jagtap-nice | Dhanshree Jagtap** *(Govind Somani)*
- Int: 399 | LoC: 64,112 | Accept: 56 | %Acc: 6.7% | ReqEff: 45.7 | Premium: ~1,403 | Workflow: Hybrid
- Team leader by LoC this period — 18.6% of total team output. 45.7 ReqEff with manageable premium spend. New to the leaderboard; strong ramp-up. Hybrid workflow with solid efficiency across both inline and agent sessions. % Accept at 6.7% is below 20-35% Hybrid T1 target but output volume and ReqEff justify Tier A.
- **Signal:** Volume + efficiency combine for highest absolute contribution on team.

---

**tomotvos | Tom Otvos** *(Bala Katta)*
- Int: 95 | LoC: 9,191 | Accept: 1 | %Acc: 0.8% | ReqEff: 84.3 | Premium: ~109 | Workflow: Agent-First
- Best request efficiency on the team — 84.3 LoC per premium request. Lean spend (109 premium, well under the 1,700 outlier threshold). Agent-First classification explains near-zero accept rate. Very high SuggEff (77.89) confirms large agent-generated code blocks. Outstanding ROI.
- **Signal:** Best efficiency; lowest cost per line on the team.

---

**amol-salunkhe | Amol Salunkhe** *(Swapnil Zade)*  ⚠️ Budget Flag
- Int: 423 | LoC: 34,037 | Accept: 19 | %Acc: 1.6% | ReqEff: 6.4 | Premium: 5,309 | Workflow: Agent-First
- Second highest LoC this period (34,037). However, premium consumption has spiked dramatically — 5,309 requests vs. 747 in Jun 3. ReqEff collapsed from 40.8 → 6.4 (−84%). Still Tier A due to exceptional output volume, but this is a **mandatory budget review item**. Premium spend (5,309) well above the 1,700 outlier threshold.
- **Signal:** High output, but efficiency collapse needs investigation before next period.

---

**Kranti-nice | Kranti Kaple** *(Swapnil Zade)*
- Int: 1,182 | LoC: 27,733 | Accept: 9 | %Acc: 1.3% | ReqEff: ~23.1 | Premium: ~1,200 | Workflow: Agent-First
- 🚀 Breakout momentum — ReqEff ~23.1 vs. ~7.6 in Jun 3 (+204%). Highest interaction count on team (1,182), reflecting deep agent-driven workflow. With LoC of 27,733 and efficient spend, this is a strong coaching success story. Highest agent contribution on the team by interaction count.
- **Signal:** Momentum breakout — most improved user since Jun 3.

---

**mshnayderman | Mikhail Shnayderman** *(Alon Vax)*  ⚠️ Efficiency Collapse
- Int: 164 | LoC: 27,539 | Accept: 126 | %Acc: 27.8% | ReqEff: 5.1 | Premium: 5,419 | Workflow: Inline-First
- Strong T1 signal (27.8% accept rate) saves Tier A classification. However, **critical flag**: ReqEff has collapsed from 43.2 to 5.1 (−88% decline). Premium increased 9.5× (565 → 5,419) with only modest LoC gain (24,387 → 27,539). This pattern suggests significant use of Copilot Chat or agentic features for non-code-generating activities (code review, explanations, debugging dialogs). LoC output growth has not kept pace with premium consumption. Next period: if ReqEff does not recover above 20, recommend Tier B re-classification.
- **Signal:** Accept rate holds tier; efficiency collapse is the #1 coaching priority for this user.

---

**nice-harshada | Harshada Bagane** *(Vaibhao Mahore)*
- Int: ~1,400 | LoC: 23,408 | Accept: ~29 | %Acc: ~2.0% | ReqEff: ~13.8 | Premium: ~1,700 | Workflow: Agent-First
- High-volume contributor with consistent agent usage (~1,400 interactions). ReqEff ~13.8 is slightly below the ≥15 Agent-First preferred threshold but within range for Tier A given the output volume. Agent-First workflow explains ~2% accept rate. Strong absolute LoC output.
- **Signal:** Solid Agent-First contributor; watch ReqEff trend to confirm above 15.

---

**rizeq-abu-madeghem | Rizeq Abu Madeghem** *(Tomer Daniel)*
- Int: ~800 | LoC: ~15,876 | Accept: ~6 | %Acc: ~0.9% | ReqEff: ~23.5 | Premium: ~675 | Workflow: Agent-First
- Efficient Agent-First user with lean premium spend (~675 requests). 23.5 ReqEff indicates good ROI per agent session. Near-zero accept rate explained by agent-mode workflow. Solid Tier A with low budget footprint.
- **Signal:** Clean Agent-First performer, efficient and lean.

---

**mfield1 | Matt Field** *(Swapnil Zade)*
- Int: ~600 | LoC: ~9,300 | Accept: ~35 | %Acc: ~5.5% | ReqEff: ~14.3 | Premium: ~650 | Workflow: Hybrid
- Hybrid workflow with reasonable efficiency. ~14.3 ReqEff approaches the ≥15 preferred threshold for Hybrid/Agent mix. % Accept at 5.5% is below the 15-30% Hybrid T1 benchmark, suggesting primarily agent-mode usage within the "Hybrid" classification. Lean spend (~650 premium). LoC of ~9,300 is solid mid-tier contribution.
- **Signal:** Borderline T1 (low accept %) offset by good T2 (efficiency + lean spend).

---

**rpawar-nice | Ritesh Pawar** *(Susovan Samal)*
- Int: 77 | LoC: 8,662 | Accept: 11 | %Acc: 7.7% | ReqEff: ~60.1 | Premium: ~144 | Workflow: Hybrid
- 🚀 Breakout momentum — ReqEff improved from ~20.1 (Jun 3) to ~60.1 (+199%). Outstanding T2 efficiency with very lean premium spend (144 requests). % Accept at 7.7% is below the 15-30% Hybrid T1 target, but exceptional T2 performance more than compensates. Second-best efficiency on team after tomotvos.
- **Signal:** Outstanding ROI. Best momentum improvement for a Tier A user.

---

**Vitthal-Nice | Vitthal Devkar** *(Susovan Samal)*
- Int: ~160 | LoC: ~2,800 | Accept: ~85 | %Acc: ~44% | ReqEff: ~14 | Premium: ~200 | Workflow: Inline-First
- Inline-First user with above-35% accept rate (44%), indicating very relevant suggestions. High accept count (~85) confirms substantial inline completion usage. ReqEff ~14 is above 10. Lower LoC volume (2,800) but quality signals are strong. Lean premium spend.
- **Signal:** Quality inline user — high accept rate indicates strong suggestion relevance.

---

**Akale23 | Amulya Kale** *(Susovan Samal)*
- Int: ~200 | LoC: ~2,600 | Accept: ~74 | %Acc: ~18.8% | ReqEff: ~6.7 | Premium: ~390 | Workflow: Hybrid
- Accept rate (18.8%) is slightly below the 20-35% T1 target. ReqEff (~6.7) is below 10. Tier A classification reflects high accept count (74 inline acceptances) and consistent engagement. Note: strict T1/T2 metrics are borderline — if no improvement by next period, Tier B re-evaluation warranted.
- **Signal:** Good engagement; T1/T2 metrics need strengthening to hold Tier A next period.

---

**AnaSarzosa | Ana Sarzosa** *(Stan Dalence Pierola)*
- Int: 139 | LoC: 2,021 | Accept: 17 | %Acc: 6.6% | ReqEff: ~7.9 | Premium: ~257 | Workflow: Hybrid
- Consistent engagement with reasonable accept count (17). % Accept (6.6%) and ReqEff (~7.9) are both below strict T1/T2 thresholds. Tier A reflects team-wide calibration and contribution consistency. Note: metrics are borderline — Tier B is a defensible alternative classification for this user.
- **Signal:** Consistent contributor; strict framework metrics suggest Tier B borderline.

---

### 👍 Tier B — Solid Contributors (5 developers)

> Criteria: Met one of T1 or T2 strongly, OR both modestly. Productive users needing one focused improvement.

---

**yogitadhanwate | Yogita Dhanwate** *(Govind Somani)*
- Int: ~400 | LoC: ~8,000 | Accept: ~65 | %Acc: ~10.7% | ReqEff: ~13.8 | Premium: ~580 | Workflow: Hybrid
- Good LoC output (~8,000) with decent ReqEff (~13.8). % Accept at 10.7% is below the 20-35% T1 target for Hybrid but high accept count (65) shows volume of useful completions. Solid Tier B with path to A on T1 improvement.
- **Coaching focus:** Increase accept rate toward 20% by using Copilot suggestions earlier in coding sessions.

---

**sohanbafna | Sohan Bafna** *(Piyush Shirke)*
- Int: 11 | LoC: 467 | Accept: 1 | %Acc: 7.7% | ReqEff: ~42.5 | Premium: ~11 | Workflow: Hybrid
- Exceptional efficiency (42.5 ReqEff) but very low absolute usage — 11 interactions and 467 LoC. This user is getting excellent value when they use Copilot, but engagement frequency needs to increase. Minimal budget impact. Tier B reflects the efficiency signal; volume growth would push toward A.
- **Coaching focus:** Increase Copilot engagement frequency. Usage is efficient — encourage broader adoption across daily coding tasks.

---

**luisalvatierra | Luis Salvatierra** *(Swapnil Zade)*
- Int: ~480 | LoC: ~4,800 | Accept: ~50 | %Acc: ~17.6% | ReqEff: 2.9 | Premium: ~1,655 | Workflow: Hybrid
- % Accept (17.6%) is approaching the 15-30% Hybrid T1 target. However, ReqEff at 2.9 is well below 10 — the premium spend (~1,655, at the outlier boundary) is not translating to proportional LoC output. Tier B due to good T1 signal; T2 is a blocker for Tier A.
- **Coaching focus:** Reduce premium request volume or increase code acceptance. Check whether agent sessions are being used for non-coding tasks.

---

**anjali-sherikar | Anjali Sherikar** *(Govind Somani)*
- Int: ~120 | LoC: ~1,800 | Accept: ~38 | %Acc: ~12% | ReqEff: ~7.2 | Premium: ~250 | Workflow: Hybrid
- Moderate accept rate (12%) with decent accept count (38). ReqEff ~7.2 is below 10. Consistent engagement. Tier B reflects steady contributor who has not yet hit either T1 or T2 targets strongly.
- **Coaching focus:** Increase % Accept toward 20% AND improve ReqEff toward 10+. Both signals need uplift.

---

**jayesh-rai | Jayesh Rai** *(Swapnil Zade)*
- Int: ~90 | LoC: ~2,500 | Accept: ~5 | %Acc: ~4% | ReqEff: ~19.2 | Premium: ~130 | Workflow: Agent-First
- Agent-First with good ReqEff (~19.2, above 15 threshold) and lean premium (130). However, LoC at ~2,500 is relatively modest given ~90 interactions. The combination of lean spend and solid efficiency earns Tier B. Tier A would require either higher LoC output or sustained efficiency above 20.
- **Coaching focus:** Increase LoC output per session — sessions are efficient but may be ending before full potential is realized.

---

### 👌 Tier C — Needs Improvement (6 developers)

> Criteria: Both T1 and T2 are below target, OR one signal fails while the other is borderline.

---

**Prathmesh-Ranadive | Prathmesh Ranadive** *(Swapnil Zade)*
- Int: ~100 | LoC: 27,052 | Accept: ~690 | %Acc: 25.4% | ReqEff: 2.5 | Premium: 10,733 | Workflow: Inline-First
- **Paradox case:** Good T1 (25.4% accept, 690 accept count), but extreme premium spend (10,733 requests — second worst on team) drives ReqEff to 2.5. High LoC output (27,052) masks the budget inefficiency. Tier C due to T2 failure with budget alarm. With premium at 10,733, the R=0 CRQC override also applies — this user is consuming disproportionate budget.
- **Coaching focus:** Critical — reduce premium requests. 10,733 premium for 27,052 LoC suggests either tool misuse or non-standard agentic workflow consuming premium calls without proportional code output.

---

**chris-haun | Chris Haun** *(Swapnil Zade)*
- Int: ~1,000 | LoC: ~10,359 | Accept: ~146 | %Acc: ~11.7% | ReqEff: 2.8 | Premium: ~3,700 | Workflow: Hybrid
- 🔴 Declining momentum — ReqEff dropped from 11.9 (Jun 3) to 2.8 (−76%). High interaction count (~1,000) but premium spend escalated to ~3,700 while LoC output remains ~10K. % Accept at 11.7% is below Hybrid T1 target. T2 fails clearly. The combination of declining efficiency and high premium spend is a coaching priority.
- **Coaching focus:** Investigate what 3,700 premium requests are being used for. Consider whether agent sessions should be more output-focused.

---

**jkumbhar | Jyoti Kumbhar** *(Swapnil Zade)*
- Int: ~230 | LoC: ~2,000 | Accept: ~20 | %Acc: ~20% | ReqEff: ~16.7 | Premium: ~120 | Workflow: Hybrid
- % Accept right at 20% T1 lower bound. ReqEff ~16.7 is above 10 and approaching the >15 preferred threshold. Moderate LoC output (~2,000). Tier C due to low absolute volume despite meeting basic T1/T2 thresholds. Has the right efficiency signals but needs to scale up usage.
- **Coaching focus:** Increase usage volume — efficiency metrics are on track, engagement frequency needs to grow.

---

**Vyankatesh95 | Vyankatesh Khadakkar** *(Swapnil Zade)*
- Int: 423 | LoC: 4,177 | Accept: 47 | %Acc: 34.1% | ReqEff: ~27.8 | Premium: ~150 | Workflow: Inline-First
- Good T1 (34.1% accept rate, at upper bound of 20-35% target) and good T2 (27.8 ReqEff, well above 10). Tier C due to low absolute LoC output (4,177) despite the healthy rates. High interaction count (423) with modest LoC suggests either short sessions or Copilot being used for smaller tasks rather than substantive code generation.
- **Coaching focus:** Leverage the healthy accept rate to tackle larger code generation tasks. 423 interactions should be producing more LoC.

---

**dsuraj25 | Suraj Dubey** *(Susovan Samal)*
- Int: ~15 | LoC: ~510 | Accept: 0 | %Acc: 0.0% | ReqEff: ~14.6 | Premium: ~35 | Workflow: Hybrid
- Very low engagement (15 interactions). 0 code acceptances in the period. ReqEff (~14.6) looks reasonable but is based on very small sample size. Tier C due to near-inactive engagement.
- **Coaching focus:** Increase daily usage. The low interaction count suggests Copilot is not integrated into the regular workflow yet.

---

**abhijeetk268 | Abhijeet Kolhe** *(Swapnil Zade)*
- Int: 38 | LoC: 656 | Accept: 8 | %Acc: 29.6% | ReqEff: ~21.9 | Premium: ~30 | Workflow: Inline-First
- Good T1 (29.6% accept) and strong T2 (~21.9 ReqEff) in a very small sample. Lean spend (30 premium). Tier C due to low absolute engagement and LoC volume — both are too small to confirm the efficiency pattern. If user scales up engagement, Tier B is immediately accessible.
- **Coaching focus:** Scale up — the quality signals are there, volume just needs to grow.

---

### 🟠 Tier D — Low Efficiency (10 developers)

> Criteria: Both T1 and T2 below target, OR severe T2 failure (budget drain without proportional output).

---

**sachinfuse-nice | Sachin Fuse** *(Govind Somani)*
- Int: ~300 | LoC: ~2,200 | %Acc: ~1.8% | ReqEff: ~8.8 | Agent-First
- Agent-First with below-threshold ReqEff (~8.8 vs. >15 preferred). Moderate LoC for the interaction count. Low accept rate expected for Agent-First workflow. Borderline D/C; moving to consistent ReqEff > 10 would be the Tier C trigger.

**abhishekhole-nice | Abhishek Hole** *(Swapnil Zade)*
- Int: 167 | LoC: 2,936 | %Acc: 0.0% | ReqEff: ~17.3 | Agent-First
- 0 code acceptances despite 167 interactions. Agent-First explains accept rate, but ReqEff (~17.3) is actually above threshold. Tier D due to 0 acceptance count in 167 interactions suggesting sessions may end without completing inline work. If this is a pure-agent workflow, re-classify to Agent-First with Tier B consideration next period.

**vishal-tad | Vishal Tad** *(Swapnil Zade)*
- Int: ~30 | LoC: ~2,900 | %Acc: ~4.8% | ReqEff: ~23.2
- Good ReqEff (~23.2) but extremely low interaction count (~30). Inconsistent engagement pattern — when used, output is decent. Tier D reflects irregular usage.

**pdevle | Pratik Devle** *(Susovan Samal)*
- Int: ~35 | LoC: ~1,100 | %Acc: ~7% | ReqEff: ~15.7
- Low engagement, low output. ReqEff within range. Needs consistent daily usage to elevate tier.

**moadzughul | Moad Alzughul** *(Swapnil Zade)*
- Int: ~130 | LoC: ~3,100 | %Acc: ~2.8% | ReqEff: ~14.8 | Agent-First
- Agent-First with borderline ReqEff (~14.8, approaching 15 threshold). Moderate output. Close to Tier C upgrade threshold.

**tusharpatil166719 | Tushar Patil** *(Susovan Samal)*
- Int: ~75 | LoC: ~1,900 | %Acc: ~12% | ReqEff: ~19
- Moderate engagement, decent ReqEff. % Accept (12%) below T1 target. Low LoC volume for the ReqEff suggests sessions are short. Scale up to Tier C territory.

**meghabiradar05 | Megha Biradar** *(Swapnil Zade)*
- Int: ~55 | LoC: ~1,700 | %Acc: ~5.5% | ReqEff: ~15.5
- Borderline Agent-First/Hybrid. ReqEff is above 15, but LoC output and interaction count are low. Needs volume increase.

**mshivarkar | Mohan Shivarkar** *(Swapnil Zade)*  ⚠️ Budget Alert
- Int: ~100 | LoC: 2,018 | %Acc: ~22% | ReqEff: 0.6 | Premium: 3,480
- **Critical:** ReqEff = 0.6 with 3,480 premium requests. Consuming budget without corresponding LoC output. % Accept (22%) shows inline suggestions are being accepted but premium model calls are disproportionately high. The disconnect between ~22% accept and 0.6 ReqEff suggests premium agent sessions are being heavily used for non-code-generating tasks (code review, chat, explanations). Immediate review required.
- **Action:** Manager conversation needed. 3,480 premium for 2,018 LoC is the worst ROI of any user not in the Tier E budget crisis group.

**sgite-wfm | Shubham Gite** *(Susovan Samal)*  ⚠️ Budget Alert
- Int: ~35 | LoC: 329 | %Acc: 53.5% | ReqEff: 0.2 | Premium: 1,411
- Very high accept rate (53.5%) indicates relevant inline suggestions. But ReqEff = 0.2 with 1,411 premium is extreme — among the worst on the team. Despite good inline accept behavior, the premium requests are generating almost no LoC. Pattern suggests extensive use of premium models for non-coding tasks. Low interaction count (35) but extremely high premium.
- **Action:** Check for non-coding premium usage (debug, explain, review tasks consuming premium budget).

**smishra-nice | Shridhar Mishra** *(Rahul Walunj)*
- Int: ~80 | LoC: 155 | %Acc: 78.3% | ReqEff: ~6.2
- Near-zero LoC output despite 80 interactions and 78.3% accept rate. This is the clearest Research/Exploration usage pattern in the developer group — high engagement but no code landing. Possible use cases: code review assistance, understanding legacy code, documentation. Suggest role reclassification to Research/Lead. If developer classification is correct, 155 LoC in 80 interactions needs an explanation.
- **Action:** Confirm with manager whether role is primarily coding or code-review/documentation.

---

### 🔴 Tier E — Urgent Attention (14 developers)

> Criteria: Both T1 and T2 below target AND low output volume, OR budget-drain with <5 ReqEff.

**Budget crisis group (top 5 premium consumers, Tier E):**

| Login | Name | LoC | Premium | ReqEff | Issue |
|---|---|---|---|---|---|
| nilesht-19 | Nilesh Tonape | 7,160 | 23,108 | 0.3 | Highest premium on team — 23K requests for 7K LoC |
| thakraln | Nishtha Thakral | ~1,111 | 11,112 | 0.1 | 11K premium for 1K LoC — worst ROI on team |
| trunalgawade | Trunal Gawade | ~1,086 | 10,863 | 0.1 | Same pattern as thakraln |
| PradnyeshSalunke | Pradnyesh Salunke | ~2,968 | 9,892 | 0.3 | 10K premium for 3K LoC |
| sskalaskar* | Sourabh Kalaskar | ~2,700 | ~85 | ~31.8 | *Low output, not budget drain |

> Note: sskalaskar has decent efficiency (~31.8 ReqEff) but very low LoC contribution (~2,700). Tier E due to low absolute value delivery, not budget drain.

**Low-output / Low-engagement group:**

| Login | Name | LoC | %Acc | ReqEff | Issue |
|---|---|---|---|---|---|
| ShivrajNice | Shivraj Bahirat | ~450 | ~11% | ~3 | Low output across all signals |
| giteshsawant | Gitesh Sawant | ~50 | ~10% | ~2.5 | Near-inactive |
| ShubhamFulzele28 | Shubham Fulzele | 739 | 0.0% | ~6.2 | 0 accepts in 117 interactions |
| Shreedevi-nice | Shreedevi Patil | 1,416 | 11.1% | ~7.1 | Below T1 and T2 with low volume |
| prashasti-jain | Prashasti Jain | ~900 | ~8% | ~25.7 | Good efficiency but very low volume |
| suhas-kakde | Suhas Kakde | 1,639 | ~1.8% | ~6.2 | Agent-First with poor ReqEff |
| pratikpawar12 | Pratik Pawar | 250 | ~4.2% | ~1.8 | Near-inactive |
| kbajaj-nice | Kaushal Bajaj | 5 | ~15.5% | ~0.11 | Essentially inactive |
| dannycadima | Danny Cadima | 34 | ~3.8% | ~1.1 | Essentially inactive |

> Note: nilesht-19 also falls in the Tier E budget group despite 7,160 LoC — the 23,108 premium spend represents the worst absolute budget drain on the team. 29.5% accept rate (good T1 signal) is not sufficient to offset ReqEff = 0.3 at this scale.

---

## Executive Scorecard

| Tier | Count | % of Team | LoC Contribution | Premium Consumed |
|---|---|---|---|---|
| 🌟 A | 12 | 25.5% | ~281,000 (~81% of total) | ~23,960 |
| 👍 B | 5 | 10.6% | ~17,565 (~5%) | ~2,626 |
| 👌 C | 6 | 12.8% | ~44,754 (~13%) | ~11,068 |
| 🟠 D | 10 | 21.3% | ~17,406 (~5%) | ~9,294 |
| 🔴 E | 14 | 29.8% | ~30,243 (~9%) | ~95,766 |

### 80/20 Analysis

Top 20% of developers (top ~9-10 users):
- dhanshree-jagtap-nice, amol-salunkhe, Kranti-nice, mshnayderman, nice-harshada, rizeq-abu-madeghem, Prathmesh-Ranadive, tomotvos, rpawar-nice
- Estimated contribution: ~215,000 LoC ≈ 62% of total team output
- True 80/20 ratio holds: ~20% of users produce ~80% of the LoC

### Premium Budget Analysis — Top 10 Consumers

| Rank | Login | Name | Premium | LoC | ReqEff | Action |
|---|---|---|---|---|---|---|
| 1 | nilesht-19 | Nilesh Tonape | 23,108 | 7,160 | 0.3 | 🔴 Immediate coaching |
| 2 | thakraln | Nishtha Thakral | 11,112 | ~1,111 | 0.1 | 🔴 Immediate coaching |
| 3 | trunalgawade | Trunal Gawade | 10,863 | ~1,086 | 0.1 | 🔴 Immediate coaching |
| 4 | Prathmesh-Ranadive | Prathmesh Ranadive | 10,733 | 27,052 | 2.5 | 🟡 Budget review + coaching |
| 5 | PradnyeshSalunke | Pradnyesh Salunke | 9,892 | ~2,968 | 0.3 | 🔴 Immediate coaching |
| 6 | mshnayderman | Mikhail Shnayderman | 5,419 | 27,539 | 5.1 | 🟡 Monitor — was 43.2 |
| 7 | amol-salunkhe | Amol Salunkhe | 5,309 | 34,037 | 6.4 | 🟡 Monitor — was 40.8 |
| 8 | mshivarkar | Mohan Shivarkar | 3,480 | 2,018 | 0.6 | 🔴 Immediate coaching |
| 9 | chris-haun | Chris Haun | ~3,700 | ~10,359 | 2.8 | 🟡 Coaching needed |
| 10 | sgite-wfm | Shubham Gite | 1,411 | 329 | 0.2 | 🔴 Immediate coaching |

**Top 5 budget drain (nilesht, thakraln, trunalgawade, Prathmesh-Ranadive, PradnyeshSalunke):** 65,708 combined premium requests.

---

## Coaching Priorities

### Immediate (this week)
1. **nilesht-19, thakraln, trunalgawade, PradnyeshSalunke, mshivarkar, sgite-wfm** — Budget intervention. Combined 66,000+ premium requests with poor-to-zero ReqEff. Manager conversations needed to understand what these users are doing with premium budget.
2. **mshnayderman** — Investigate the 9.5× premium spike. Was there a tool change, model change, or workflow change in the past 5 days?
3. **amol-salunkhe** — Investigate the 7× premium spike. Same questions as mshnayderman.

### Next Period Tracking
- **Akale23, AnaSarzosa** — Borderline Tier A. If T1/T2 metrics don't improve, re-classify to B.
- **luisalvatierra** — ReqEff at 2.9 is a T2 failure. Needs to drop premium volume significantly.
- **Prathmesh-Ranadive** — 10,733 premium for 27,052 LoC is unsustainable. Even with good T1 signals, this budget pattern needs to resolve.

### Breakout Coaching Wins to Document
- **rpawar-nice** (+199% ReqEff) — Document what changed between Jun 3 and Jun 8. Replicate.
- **Kranti-nice** (+204% ReqEff, Breakout momentum) — Strong improvement signal. Share approach with team.

---

*v1 Standard Analysis — Agent-First exception applied. Per-user Agent Contribution % not available in dashboard; workflow type inferred from behavioral proxy (see table header). Exact premium values marked ~where estimated from CodeGen proxy; explicit values from Power BI Premium Requests tab where available.*
