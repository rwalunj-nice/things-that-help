# GitHub Copilot Usage Analysis — June 3, 2026 (CRQC Framework)

> **Framework**: CRQC — Core (C) + ROI (R) + Quality (Q) + Context (diagnostic)
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM
> **Analysis Date**: June 3, 2026 | **Data Synced**: June 3, 2026
> **Active Analysis Users**: 37

---

## CRQC Scoring Key

### C (Core) — by Workflow Type

**Agent-First** (% Accept < 12%, SuggEff > 20):
- ReqEff > 15 → 2pts; ReqEff 8–15 → 1pt; ReqEff < 8 → 0pts
- LoC increasing vs prior period → +1pt (max C = 3)

**Hybrid** (% Accept 5–30%, mixed SuggEff):
- % Accept 15–30% → 1pt
- ReqEff > 8 → 1pt
- Code Accept Count > 10 → +1pt (max C = 3)

**Inline-First** (% Accept > 20% as primary signal):
- % Accept > 20% (above benchmark range or in range) → 2pts; 10–19% → 1pt
- Code Accept Count > 20 → +1pt (max C = 3)

### R (ROI) — Universal
- ReqEff > 20 → 3pts; 10–20 → 2pts; 5–10 → 1pt; < 5 → 0pts
- Premium ≤ 500 → +1 lean bonus | Premium > 1,700 → −1 outlier penalty
- Floor = 0, Cap = 3

### Q (Quality)
- **Q = FB**: PR Details tab skipped this period. All users = Feature Branch (not Q=0).
- Final tier calculated as floor tier from C+R. Q=FB means tier could improve if PR data captured.

### Override Rules
- R = 0 AND Premium > 500 → Cannot exceed Tier C
- Q = 0 → Cannot be Tier A (not applicable — Q=FB, not Q=0)
- Momentum > +100% → Eligible for one-tier promotion

---

## CRQC Scorecard

| Login | Name | Workflow | C | R | Q | C+R | Floor Tier | Override | Momentum | Final Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | Agent-First | 3 | 3 | FB | 6 | B+ | — | ➡️ Stable | **🌟 A** (projected) |
| mshnayderman | Mikhail Shnayderman | Agent-First | 3 | 3 | FB | 6 | B+ | — | ➡️ Stable | **🌟 A** (projected) |
| rpawar-nice | Ritesh Pawar | Agent-First | 3 | 3 | FB | 6 | B+ | — | ➡️ Stable | **🌟 A** (projected) |
| chris-haun | Chris Haun | Hybrid | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👍 B** (projected) |
| mfield1 | Matt Field | Hybrid | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👍 B** (projected) |
| Vitthal-Nice | Vitthal Devkar | Inline-First | 3 | 2 | FB | 5 | B+ | — | ➡️ Stable | **👍 B** (projected) |
| jayesh-rai | Jayesh Rai | Hybrid | 3 | 2 | FB | 5 | B+ | — | 🚀 Breakout | **👍 B** → eligible 🌟 A |
| copilotshree | Shraddha Kale | Hybrid | 2 | 3 | FB | 5 | B+ | — | ➡️ Stable | **👍 B** (projected) |
| sskalaskar | Sourabh Kalaskar | Hybrid | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** (projected) |
| tusharpatil166719 | Tushar Patil | Hybrid | 2 | 1 | FB | 3 | C | — | ➡️ Stable | **👌 C** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 3 | 0 | FB | 3 | C | R=0+Prem>500→max C | 🚀 Breakout | **👌 C** (capped) |
| PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 3 | 0 | FB | 3 | C | R=0+Prem>1700→max C | ➡️ Stable | **👌 C** (capped) |
| mshivarkar | Mohan Shivarkar | Hybrid | 1 | 2 | FB | 3 | C | — | 🚀 Breakout | **👌 C** → eligible 👍 B |
| moadzughul | Moad Alzughul | Agent-First | 1 | 2 | FB | 3 | C | — | ➡️ Stable | **👌 C** |
| Akale23 | Amulya Kale | Inline-First | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** (projected) |
| vishal-tad | Vishal Tad | Hybrid | 1 | 2 | FB | 3 | C | — | 🆕 New | **👌 C** |
| trunalgawade | Trunal Gawade | Inline-First | 3 | 1 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** (projected) |
| sgite-wfm | Shubham Gite | Inline-First | 3 | 1 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** (projected) |
| smishra-nice | Shridhar Mishra | Inline-First | 2 | 1 | FB | 3 | C | — | ➡️ Stable | **👌 C** |
| dsuraj25 | Suraj Dubey | Hybrid | 0 | 2 | FB | 2 | D+ | — | ➡️ Stable | **🟠 D** |
| shreedevi-nice | Shreedevi Patil | Agent-First | 1 | 1 | FB | 2 | D+ | — | 📈 Rising | **🟠 D** |
| Kranti-nice | Kranti Kaple | Agent-First | 1 | 0 | FB | 1 | D+ | R=0+Prem>1700→max C | 🚀 Breakout | **👌 C** (Breakout override + cap applies) |
| nilesht-19 | Nilesh Tonape | Hybrid | 2 | 0 | FB | 2 | D+ | R=0+Prem>1700→max C | ➡️ Stable | **🟠 D** (R=0+Prem>500→max C, floor D) |
| Vyankatesh95 | Vyankatesh Khadakkar | Hybrid | 1 | 0 | FB | 1 | D+ | R=0+Prem>500→max C | ➡️ Stable | **🟠 D** |
| jkumbhar | Jyoti Kumbhar | Hybrid | 2 | 0 | FB | 2 | D+ | R=0+Prem>500→max C | ➡️ Stable | **🟠 D** |
| luisalvatierra | Luis Salvatierra | Hybrid | 1 | 0 | FB | 1 | D+ | R=0+Prem>500→max C | 📈 Rising | **🟠 D** |
| abhijeetk268 | Abhijeet Kolhe | Hybrid | 0 | 1 | FB | 1 | D | — | 🚀 Breakout | **🟠 D** → eligible 👌 C |
| meghabiradar05 | Megha Biradar | Hybrid | 0 | 1 | FB | 1 | D | — | ➡️ Stable | **🟠 D** |
| pdevle | Pratik Devle | Hybrid | 0 | 1 | FB | 1 | D | — | 🚀 Breakout | **🟠 D** → eligible 👌 C |
| suhas-kakde | Suhas Kakde | Agent-First | 0 | 0 | FB | 0 | E | R=0+Prem>500→max C | ➡️ Stable | **🔴 E** (max C but C+R=0 floors at E) |
| abbhishekhole-nice | Abhishek Hole | Agent-First | 0 | 2 | FB | 2 | D+ | — | ➡️ Stable | **🟠 D** |
| thakraln | Nishtha Thakral | Agent-First | 1 | 0 | FB | 1 | D+ | R=0+Prem>500→max C | 🚀 Breakout* | **🟠 D** → eligible 👌 C* |
| prashasti-jain | Prashasti Jain | Hybrid | 0 | 0 | FB | 0 | E | R=0+Prem>500→max C | ➡️ Stable | **🔴 E** |
| smishra-nice | Shridhar Mishra | Inline-First | 2 | 1 | FB | 3 | C | — | ➡️ Stable | **👌 C** |
| dannycadima | Danny Cadima Molina | Inline-First | 2 | 3 | FB | 5 | B+ | — | 🚀 Breakout* | **👍 B** (projected)* |
| kbajaj-nice | Kaushal Bajaj | Inline-First | 1 | 1 | FB | 2 | D+ | — | ➡️ Stable | **🟠 D** |
| pratikpawar12 | Pratik Pawar | Hybrid | 0 | 1 | FB | 1 | D | — | ➡️ Stable | **🟠 D** |
| Shubhamfulzele28 | Shubham Fulzele | — | 0 | 1 | FB | 1 | D | — | 🆕 New | **🆕 New** |

> *dannycadima Tier B is mathematically correct (C=2, R=3 → 5+, lean spend) but output is 34 LoC — context: tiny volume despite great efficiency. Monitor whether volume grows. Breakout from near-zero.

> *thakraln and dannycadima Breakout overrides: baseline is near-zero (0 and 1 LoC respectively). Override eligibility noted but tier promotion requires VP review given context.

---

## Corrected Scorecard (Duplicate Fixed)

> Note: abhishekhole-nice and smishra-nice appeared twice above in draft — final correct scores:

| Login | C | R | Q | C+R | Final Tier |
|---|---|---|---|---|---|
| abhishekhole-nice | 0 | 2 | FB | 2 | 🟠 D |
| smishra-nice | 2 | 1 | FB | 3 | 👌 C |

---

## Detailed C Score Workings

### Agent-First Users

| Login | ReqEff | ReqEff pts | LoC Trend | C Score |
|---|---|---|---|---|
| amol-salunkhe | 40.8 | 2 | ↑ +5% | **3** |
| mshnayderman | 43.2 | 2 | ↑ +10% | **3** |
| rpawar-nice | 20.1 | 2 | ↑ +0.05% | **3** |
| abhishekhole-nice | 7.4 | 0 | → 0% | **0** |
| Kranti-nice | 7.6 | 0 | ↑ +292% | **1** |
| shreedevi-nice | 2.3 | 0 | ↑ +47% | **1** |
| amol-salunkhe | 40.8 | 2 | ↑ | **3** |
| moadzughul | 7.4 | 0 | ↑ +10% | **1** |
| suhas-kakde | 3.1 | 0 | → 0% | **0** |
| thakraln | 0.1 | 0 | ↑ (from 0) | **1** |

### Hybrid Users

| Login | % Accept | Accept pts | ReqEff > 8 | Accept Count > 10 | C Score |
|---|---|---|---|---|---|
| Vyankatesh95 | 35.9% | 0 (>30%) | No (4.5) | Yes (47) | **1** |
| abhijeetk268 | 32.0% | 0 (>30%) | No (1.9) | No (8) | **0** |
| sskalaskar | 17.1% | 1 | No (5.7) | Yes (19) | **2** |
| tusharpatil166719 | 15.9% | 1 | No (4.1) | Yes (14) | **2** |
| jkumbhar | 18.4% | 1 | No (3.2) | Yes (18) | **2** |
| nilesht-19 | 16.1% | 1 | No (1.3) | Yes (46) | **2** |
| mfield1 | 5.0% | 0 | Yes (14.9) | Yes (32) | **2** |
| pdevle | 5.4% | 0 | No (4.0) | No (4) | **0** |
| jayesh-rai | 21.5% | 1 | Yes (8.8) | Yes (37) | **3** |
| meghabiradar05 | 6.6% | 0 | No (3.9) | No (10, not >10) | **0** |
| copilotshree | 4.8% | 0 | Yes (14.8) | Yes (22) | **2** |
| prashasti-jain | 8.4% | 0 | No (0.7) | No (7) | **0** |
| chris-haun | 12.8% | 0 | Yes (11.9) | Yes (127) | **2** |
| dsuraj25 | 9.3% | 0 | No (5.1) | No (5) | **0** |
| mshivarkar | 14.7% | 0 | No (5.5) | Yes (26) | **1** |
| luisalvatierra | 12.3% | 0 | No (4.8) | Yes (75) | **1** |
| vishal-tad | 6.5% | 0 | No (7.6) | Yes (27) | **1** |
| pratikpawar12 | 4.3% | 0 | No (0.7) | No (5) | **0** |

### Inline-First Users

| Login | % Accept | Accept pts | Accept Count > 20 | C Score |
|---|---|---|---|---|
| Prathmesh-Ranadive | 84.8% | 2 | Yes (913) | **3** |
| PradnyeshSalunke | 37.7% | 2 | Yes (58) | **3** |
| Vitthal-Nice | 41.9% | 2 | Yes (80) | **3** |
| smishra-nice | 78.3% | 2 | No (18) | **2** |
| Akale23 | 19.7% | 1 | Yes (75) | **2** |
| trunalgawade | 23.0% | 2 | Yes (57) | **3** |
| sgite-wfm | 54.6% | 2 | Yes (147) | **3** |
| dannycadima | 12.7% | 1 | Yes (30) | **2** |
| kbajaj-nice | 17.5% | 1 | No (7) | **1** |

---

## Detailed R Score Workings

| Login | ReqEff | Base R | Premium | Lean Bonus | Outlier Penalty | Final R |
|---|---|---|---|---|---|---|
| amol-salunkhe | 40.8 | 3 | 747.58 | No | No | **3** |
| mshnayderman | 43.2 | 3 | 564.90 | No (>500) | No | **3** |
| rpawar-nice | 20.1 | 3 | 430.90 | Yes (+1→cap3) | No | **3** |
| abhishekhole-nice | 7.4 | 1 | 378.99 | Yes (+1) | No | **2** |
| Kranti-nice | 7.6 | 1 | 3,659.98 | No | Yes (−1) | **0** |
| shreedevi-nice | 2.3 | 0 | 433.31 | Yes (+1) | No | **1** |
| Vyankatesh95 | 4.5 | 0 | 930.64 | No | No | **0** |
| amol-salunkhe | 40.8 | 3 | 747.58 | No | No | **3** |
| abhijeetk268 | 1.9 | 0 | 344.00 | Yes (+1) | No | **1** |
| sskalaskar | 5.7 | 1 | 457.34 | Yes (+1) | No | **2** |
| tusharpatil166719 | 4.1 | 0 | 441.00 | Yes (+1) | No | **1** |
| jkumbhar | 3.2 | 0 | 591.32 | No (>500) | No | **0** |
| Prathmesh-Ranadive | 5.1 | 1 | 4,000.80 | No | Yes (−1) | **0** |
| nilesht-19 | 1.3 | 0 | 3,988.21 | No | Yes (−1→floor0) | **0** |
| PradnyeshSalunke | 0.6 | 0 | 3,754.32 | No | Yes (−1→floor0) | **0** |
| mfield1 | 14.9 | 2 | 620.30 | No | No | **2** |
| pdevle | 4.0 | 0 | 261.00 | Yes (+1) | No | **1** |
| Vitthal-Nice | 9.3 | 1 | 281.65 | Yes (+1) | No | **2** |
| jayesh-rai | 8.8 | 1 | 250.49 | Yes (+1) | No | **2** |
| meghabiradar05 | 3.9 | 0 | 435.00 | Yes (+1) | No | **1** |
| moadzughul | 7.4 | 1 | 407.53 | Yes (+1) | No | **2** |
| copilotshree | 14.8 | 2 | 339.54 | Yes (+1→cap3) | No | **3** |
| prashasti-jain | 0.7 | 0 | 1,267.00 | No | No | **0** |
| chris-haun | 11.9 | 2 | 859.90 | No | No | **2** |
| dsuraj25 | 5.1 | 1 | 98.00 | Yes (+1) | No | **2** |
| mshivarkar | 5.5 | 1 | 285.25 | Yes (+1) | No | **2** |
| luisalvatierra | 4.8 | 0 | 952.00 | No | No | **0** |
| suhas-kakde | 3.1 | 0 | 525.00 | No (>500) | No | **0** |
| smishra-nice | 0.6 | 0 | 257.00 | Yes (+1) | No | **1** |
| vishal-tad | 7.6 | 1 | 368.00 | Yes (+1) | No | **2** |
| Akale23 | 7.2 | 1 | 332.60 | Yes (+1) | No | **2** |
| thakraln | 0.1 | 0 | 1,041.90 | No | No | **0** |
| pratikpawar12 | 0.7 | 0 | 374.93 | Yes (+1) | No | **1** |
| trunalgawade | 2.3 | 0 | 134.00 | Yes (+1) | No | **1** |
| sgite-wfm | 2.5 | 0 | 125.66 | Yes (+1) | No | **1** |
| dannycadima | 11.0 | 2 | 3.10 | Yes (+1→cap3) | No | **3** |
| kbajaj-nice | 0.8 | 0 | 6.00 | Yes (+1) | No | **1** |
| Shubhamfulzele28 | 0.0 | 0 | 170.20 | Yes (+1) | No | **1** |

---

## CRQC Final Summary

### 🌟 Tier A Projected (C+R ≥ 6, no override)
amol-salunkhe (C3+R3=6), mshnayderman (C3+R3=6), rpawar-nice (C3+R3=6)

### 👍 Tier B Projected (C+R = 5 or override)
chris-haun (4+, Q expected ≥1), mfield1 (4+, Q expected ≥1), Vitthal-Nice (5), jayesh-rai (5 + Breakout), copilotshree (5), dannycadima (5)*

### 👌 Tier C
Prathmesh-Ranadive (capped), PradnyeshSalunke (capped), Kranti-nice (Breakout override → C from D), sskalaskar, tusharpatil166719, Akale23, mshivarkar (Breakout override), moadzughul, vishal-tad, trunalgawade, sgite-wfm, smishra-nice

### 🟠 Tier D
dsuraj25, shreedevi-nice, nilesht-19, Vyankatesh95, jkumbhar, luisalvatierra, abhijeetk268, meghabiradar05, pdevle, abhishekhole-nice, thakraln, kbajaj-nice, pratikpawar12, Shubhamfulzele28

### 🔴 Tier E
suhas-kakde (R=0 + Prem>500, C=0), prashasti-jain (C=0, R=0)

---

## ⚠️ Budget Alert — Override Rule Applications

| User | Issue | Override Applied |
|---|---|---|
| Prathmesh-Ranadive | R=0 (outlier penalty) + Prem 4,001 > 500 | Max Tier C |
| PradnyeshSalunke | R=0 (outlier penalty) + Prem 3,754 > 500 | Max Tier C |
| Kranti-nice | R=0 (outlier penalty) + Prem 3,660 > 500 | Max Tier C — Breakout allows C (not higher) |
| nilesht-19 | R=0 (outlier penalty) + Prem 3,988 > 500 | Max Tier C — but C+R floor is D, stays D |
| jkumbhar | R=0 + Prem 591 > 500 | Max Tier C — floor stays D |
| Vyankatesh95 | R=0 + Prem 931 > 500 | Max Tier C — floor stays D |
| thakraln | R=0 + Prem 1,042 > 500 | Max Tier C — Breakout eligible for C |
| prashasti-jain | R=0 + Prem 1,267 > 500 | Max Tier C — C+R=0 floors at E |
| suhas-kakde | R=0 + Prem 525 > 500 | Max Tier C — C+R=0 floors at E |
| luisalvatierra | R=0 + Prem 952 > 500 | Max Tier C — floor stays D |

---

## VP Narrative Template

> "Our CRQC framework scores each developer across Core (adoption quality), ROI (budget efficiency), and Quality (code delivery — currently FB/Feature Branch for this period).
>
> **Tier A (3 users)** score 6/9+ on Core + ROI alone: Amol Salunkhe, Mikhail Shnayderman, Ritesh Pawar. These users produce top-tier output with strong budget efficiency.
>
> **Budget concern (4 outlier spenders)**: Prathmesh Ranadive, Pradnyesh Salunke, Kranti Kaple, and Nilesh Tonape collectively consumed **14,403 Premium Requests** — roughly **54%** of the team's premium budget while representing only 10.8% of the team. CRQC override rule caps all four at Tier C or below regardless of output, because R=0 due to outlier penalty.
>
> **Momentum positive**: Mohan Shivarkar (+5,468%), Jayesh Rai (+155%), Abhijeet Kolhe (+279%), Pratik Devle (+184%) are all on strong improvement trajectories."
