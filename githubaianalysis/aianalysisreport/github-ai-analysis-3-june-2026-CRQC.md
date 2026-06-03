# GitHub Copilot Usage Analysis — June 3, 2026 (CRQC Framework)

> **Framework**: CRQC — Core (C) + ROI (R) + Quality (Q) + Context (diagnostic)
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM
> **Analysis Date**: June 3, 2026 | **Data Synced**: June 3, 2026
> **Active Analysis Users**: 37

> ⚠️ **Q2 Cumulative Data**: All metrics represent **running totals from April 1 through June 3, 2026** (~9 weeks). ReqEff, % Accept, SuggEff, and Prem Req figures are all Q2 cumulative. **Win LoC** = LoC added in the final ~16 days (May 18 → Jun 3). The CRQC scores reflect a full quarter of behaviour, not a single week.

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
- % Accept > 20% → 2pts; 10–19% → 1pt
- Code Accept Count > 20 → +1pt (max C = 3)

### R (ROI) — Universal
- Q2 ReqEff > 20 → 3pts; 10–20 → 2pts; 5–10 → 1pt; < 5 → 0pts
- Q2 Premium ≤ 500 → +1 lean bonus | Q2 Premium > 1,700 → −1 outlier penalty
- Floor = 0, Cap = 3

### Q (Quality)
- **Q = FB**: PR Details tab skipped this period. All users = Feature Branch (not Q=0).
- Final tier calculated as floor tier from C+R. Q=FB means tier could improve if PR data captured next quarter.

### Override Rules
- R = 0 AND Q2 Premium > 500 → Cannot exceed Tier C
- Q = 0 → Cannot be Tier A (not applicable — Q=FB this period)
- Momentum > +100% (final window) → Eligible for one-tier promotion

---

## CRQC Scorecard — Q2 2026

> **Win LoC** column added to show final-window activity alongside Q2 cumulative scores.

| Login | Name | Workflow | Q2 LoC | Win LoC | C | R | Q | C+R | Floor Tier | Override | Momentum | Final Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | Agent-First | 30,486 | +1,575 | 3 | 3 | FB | 6 | B+ | — | ➡️ Stable | **🌟 A** |
| mshnayderman | Mikhail Shnayderman | Agent-First | 24,387 | +2,119 | 3 | 3 | FB | 6 | B+ | — | ➡️ Stable | **🌟 A** |
| rpawar-nice | Ritesh Pawar | Agent-First | 8,662 | +4 | 3 | 3 | FB | 6 | B+ | — | ⚠️ Near-zero window | **🌟 A** |
| chris-haun | Chris Haun | Hybrid | 10,264 | +1,672 | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👍 B** |
| mfield1 | Matt Field | Hybrid | 9,251 | +180 | 2 | 2 | FB | 4 | C+ | — | ⚠️ Low window | **👍 B** |
| Vitthal-Nice | Vitthal Devkar | Inline-First | 2,609 | +43 | 3 | 2 | FB | 5 | B+ | — | ➡️ Stable | **👍 B** |
| jayesh-rai | Jayesh Rai | Hybrid | 2,196 | +1,334 | 3 | 2 | FB | 5 | B+ | — | 🚀 Breakout | **👍 B** → eligible 🌟 A |
| copilotshree | Shraddha Kale | Hybrid | 5,013 | 0 | 2 | 3 | FB | 5 | B+ | — | ⚠️ Zero window | **👍 B** |
| sskalaskar | Sourabh Kalaskar | Hybrid | 2,609 | +553 | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** |
| tusharpatil166719 | Tushar Patil | Hybrid | 1,798 | +167 | 2 | 1 | FB | 3 | C | — | ➡️ Stable | **👌 C** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 20,436 | +10,947 | 3 | 0 | FB | 3 | C | R=0+Prem>500→max C | 🚀 Breakout | **👌 C** (capped) |
| PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 2,296 | +348 | 3 | 0 | FB | 3 | C | R=0+Prem>1,700→max C | ➡️ Stable | **👌 C** (capped) |
| mshivarkar | Mohan Shivarkar | Hybrid | 1,559 | +1,531 | 1 | 2 | FB | 3 | C | — | 🚀 Breakout | **👌 C** → eligible 👍 B |
| moadzughul | Moad Alzughul | Agent-First | 3,035 | +286 | 1 | 2 | FB | 3 | C | — | ➡️ Stable | **👌 C** |
| Akale23 | Amulya Kale | Inline-First | 2,409 | +553 | 2 | 2 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** |
| vishal-tad | Vishal Tad | Hybrid | 2,815 | 2,815 | 1 | 2 | FB | 3 | C | — | 🆕 New | **👌 C** |
| trunalgawade | Trunal Gawade | Inline-First | 304 | +2 | 3 | 1 | FB | 4 | C+ | — | ⚠️ Near-zero window | **👌 C** |
| sgite-wfm | Shubham Gite | Inline-First | 316 | +45 | 3 | 1 | FB | 4 | C+ | — | ➡️ Stable | **👌 C** |
| smishra-nice | Shridhar Mishra | Inline-First | 155 | 0 | 2 | 1 | FB | 3 | C | — | ⚠️ Zero window | **👌 C** |
| dsuraj25 | Suraj Dubey | Hybrid | 504 | +13 | 0 | 2 | FB | 2 | D+ | — | ⚠️ Near-zero window | **🟠 D** |
| shreedevi-nice | Shreedevi Patil | Agent-First | 1,013 | +323 | 1 | 1 | FB | 2 | D+ | — | 📈 Rising | **🟠 D** |
| Kranti-nice | Kranti Kaple | Agent-First | 27,733 | +20,657 | 1 | 0 | FB | 1 | D+ | R=0+Prem>1,700→max C | 🚀 Breakout | **👌 C** (Breakout override + cap) |
| nilesht-19 | Nilesh Tonape | Hybrid | 5,293 | +228 | 2 | 0 | FB | 2 | D+ | R=0+Prem>1,700→max C | ➡️ Stable | **🟠 D** (R=0+Prem>500 → floor stays D) |
| Vyankatesh95 | Vyankatesh Khadakkar | Hybrid | 4,151 | +478 | 1 | 0 | FB | 1 | D+ | R=0+Prem>500→max C | ➡️ Stable | **🟠 D** |
| jkumbhar | Jyoti Kumbhar | Hybrid | 1,868 | +80 | 2 | 0 | FB | 2 | D+ | R=0+Prem>500→max C | ➡️ Stable | **🟠 D** |
| luisalvatierra | Luis Salvatierra | Hybrid | 4,564 | +2,272 | 1 | 0 | FB | 1 | D+ | R=0+Prem>500→max C | 📈 Rising | **🟠 D** |
| abhijeetk268 | Abhijeet Kolhe | Hybrid | 656 | +483 | 0 | 1 | FB | 1 | D | — | 🚀 Breakout | **🟠 D** → eligible 👌 C |
| meghabiradar05 | Megha Biradar | Hybrid | 1,684 | +295 | 0 | 1 | FB | 1 | D | — | ➡️ Stable | **🟠 D** |
| pdevle | Pratik Devle | Hybrid | 1,049 | +679 | 0 | 1 | FB | 1 | D | — | 🚀 Breakout | **🟠 D** → eligible 👌 C |
| abhishekhole-nice | Abhishek Hole | Agent-First | 2,803 | 0 | 0 | 2 | FB | 2 | D+ | — | ⚠️ Zero window | **🟠 D** |
| thakraln | Nishtha Thakral | Agent-First | 69 | +69 | 1 | 0 | FB | 1 | D+ | R=0+Prem>500→max C | 🚀 Breakout* | **🟠 D** → eligible 👌 C* |
| kbajaj-nice | Kaushal Bajaj | Inline-First | 5 | 0 | 1 | 1 | FB | 2 | D+ | — | ⚠️ Zero window | **🟠 D** |
| pratikpawar12 | Pratik Pawar | Hybrid | 250 | 0 | 0 | 1 | FB | 1 | D | — | ⚠️ Zero window | **🟠 D** |
| dannycadima | Danny Cadima Molina | Inline-First | 34 | +33 | 2 | 3 | FB | 5 | B+ | — | 🚀 Breakout* | **👍 B*** |
| suhas-kakde | Suhas Kakde | Agent-First | 1,639 | 0 | 0 | 0 | FB | 0 | E | R=0+Prem>500→max C | ⚠️ Zero window | **🔴 E** |
| prashasti-jain | Prashasti Jain | Hybrid | 872 | +35 | 0 | 0 | FB | 0 | E | R=0+Prem>500→max C | ➡️ Stable | **🔴 E** |
| Shubhamfulzele28 | Shubham Fulzele | — | 0 | 0 | 0 | 1 | FB | 1 | D | — | 🆕 New | **🆕 New** |

> *dannycadima Tier B is mathematically correct (C=2, R=3 → 5+, lean Q2 spend of 3 Prem) but Q2 output is only 34 LoC — context: minimal volume despite great efficiency. Monitor whether volume grows in Q3.
> *thakraln Breakout override eligible but Q2 output is 69 LoC total. Tier C promotion requires VP review given absolute volume.

---

## Detailed C Score Workings

### Agent-First Users — Q2

| Login | Q2 ReqEff | ReqEff pts | LoC Trend (vs May 18) | C Score |
|---|---|---|---|---|
| amol-salunkhe | 40.8 | 2 | ↑ +1,575 | **3** |
| mshnayderman | 43.2 | 2 | ↑ +2,119 | **3** |
| rpawar-nice | 20.1 | 2 | → +4 (near-zero window) | **3** |
| Kranti-nice | 7.6 | 0 | ↑ +20,657 | **1** |
| shreedevi-nice | 2.3 | 0 | ↑ +323 | **1** |
| moadzughul | 7.4 | 0 | ↑ +286 | **1** |
| thakraln | 0.1 | 0 | ↑ +69 (from 0) | **1** |
| abhishekhole-nice | 7.4 | 0 | → 0 (zero window) | **0** |
| suhas-kakde | 3.1 | 0 | → 0 (zero window) | **0** |

### Hybrid Users — Q2

| Login | % Accept | Accept pts | ReqEff > 8 | Accept Count > 10 | C Score |
|---|---|---|---|---|---|
| jayesh-rai | 21.5% | 1 | Yes (8.8) | Yes (37) | **3** |
| sskalaskar | 17.1% | 1 | No (5.7) | Yes (19) | **2** |
| tusharpatil166719 | 15.9% | 1 | No (4.1) | Yes (14) | **2** |
| jkumbhar | 18.4% | 1 | No (3.2) | Yes (18) | **2** |
| nilesht-19 | 16.1% | 1 | No (1.3) | Yes (46) | **2** |
| mfield1 | 5.0% | 0 | Yes (14.9) | Yes (32) | **2** |
| copilotshree | 4.8% | 0 | Yes (14.8) | Yes (22) | **2** |
| chris-haun | 12.8% | 0 | Yes (11.9) | Yes (127) | **2** |
| mshivarkar | 14.7% | 0 | No (5.5) | Yes (26) | **1** |
| Vyankatesh95 | 35.9% | 0 (>30%) | No (4.5) | Yes (47) | **1** |
| moadzughul | 3.3% | 0 | No | Yes | **1** |
| luisalvatierra | 12.3% | 0 | No (4.8) | Yes (75) | **1** |
| vishal-tad | 6.5% | 0 | No (7.6) | Yes (27) | **1** |
| shreedevi-nice | 11.5% | 0 | No (2.3) | No | **1** |
| pdevle | 5.4% | 0 | No (4.0) | No (4) | **0** |
| abhijeetk268 | 32.0% | 0 (>30%) | No (1.9) | No (8) | **0** |
| meghabiradar05 | 6.6% | 0 | No (3.9) | No (10) | **0** |
| prashasti-jain | 8.4% | 0 | No (0.7) | No (7) | **0** |
| dsuraj25 | 9.3% | 0 | No (5.1) | No (5) | **0** |
| pratikpawar12 | 4.3% | 0 | No (0.7) | No (5) | **0** |
| suhas-kakde | 1.8% | 0 | No (3.1) | No (4) | **0** |

### Inline-First Users — Q2

| Login | % Accept | Accept pts | Accept Count > 20 | C Score |
|---|---|---|---|---|
| Prathmesh-Ranadive | 84.8% | 2 | Yes (913) | **3** |
| PradnyeshSalunke | 37.7% | 2 | Yes (58) | **3** |
| Vitthal-Nice | 41.9% | 2 | Yes (80) | **3** |
| trunalgawade | 23.0% | 2 | Yes (57) | **3** |
| sgite-wfm | 54.6% | 2 | Yes (147) | **3** |
| smishra-nice | 78.3% | 2 | No (18) | **2** |
| dannycadima | 12.7% | 1 | Yes (30) | **2** |
| Akale23 | 19.7% | 1 | Yes (75) | **2** |
| kbajaj-nice | 17.5% | 1 | No (7) | **1** |

---

## Detailed R Score Workings — Q2 Cumulative

| Login | Q2 ReqEff | Base R | Q2 Prem | Lean Bonus | Outlier Penalty | Final R |
|---|---|---|---|---|---|---|
| amol-salunkhe | 40.8 | 3 | 747.58 | No | No | **3** |
| mshnayderman | 43.2 | 3 | 564.90 | No (>500) | No | **3** |
| rpawar-nice | 20.1 | 3 | 430.90 | Yes (+1→cap3) | No | **3** |
| copilotshree | 14.8 | 2 | 339.54 | Yes (+1→cap3) | No | **3** |
| abhishekhole-nice | 7.4 | 1 | 378.99 | Yes (+1) | No | **2** |
| mfield1 | 14.9 | 2 | 620.30 | No | No | **2** |
| Vitthal-Nice | 9.3 | 1 | 281.65 | Yes (+1) | No | **2** |
| jayesh-rai | 8.8 | 1 | 250.49 | Yes (+1) | No | **2** |
| moadzughul | 7.4 | 1 | 407.53 | Yes (+1) | No | **2** |
| chris-haun | 11.9 | 2 | 859.90 | No | No | **2** |
| dsuraj25 | 5.1 | 1 | 98.00 | Yes (+1) | No | **2** |
| mshivarkar | 5.5 | 1 | 285.25 | Yes (+1) | No | **2** |
| vishal-tad | 7.6 | 1 | 368.00 | Yes (+1) | No | **2** |
| Akale23 | 7.2 | 1 | 332.60 | Yes (+1) | No | **2** |
| dannycadima | 11.0 | 2 | 3.10 | Yes (+1→cap3) | No | **3** |
| sskalaskar | 5.7 | 1 | 457.34 | Yes (+1) | No | **2** |
| shreedevi-nice | 2.3 | 0 | 433.31 | Yes (+1) | No | **1** |
| tusharpatil166719 | 4.1 | 0 | 441.00 | Yes (+1) | No | **1** |
| pdevle | 4.0 | 0 | 261.00 | Yes (+1) | No | **1** |
| meghabiradar05 | 3.9 | 0 | 435.00 | Yes (+1) | No | **1** |
| abhijeetk268 | 1.9 | 0 | 344.00 | Yes (+1) | No | **1** |
| smishra-nice | 0.6 | 0 | 257.00 | Yes (+1) | No | **1** |
| trunalgawade | 2.3 | 0 | 134.00 | Yes (+1) | No | **1** |
| sgite-wfm | 2.5 | 0 | 125.66 | Yes (+1) | No | **1** |
| pratikpawar12 | 0.7 | 0 | 374.93 | Yes (+1) | No | **1** |
| kbajaj-nice | 0.8 | 0 | 6.00 | Yes (+1) | No | **1** |
| Shubhamfulzele28 | 0.0 | 0 | 170.20 | Yes (+1) | No | **1** |
| Kranti-nice | 7.6 | 1 | 3,659.98 | No | Yes (−1) | **0** |
| Prathmesh-Ranadive | 5.1 | 1 | 4,000.80 | No | Yes (−1) | **0** |
| nilesht-19 | 1.3 | 0 | 3,988.21 | No | Yes (−1→floor0) | **0** |
| PradnyeshSalunke | 0.6 | 0 | 3,754.32 | No | Yes (−1→floor0) | **0** |
| Vyankatesh95 | 4.5 | 0 | 930.64 | No | No | **0** |
| jkumbhar | 3.2 | 0 | 591.32 | No (>500) | No | **0** |
| luisalvatierra | 4.8 | 0 | 952.00 | No | No | **0** |
| thakraln | 0.1 | 0 | 1,041.90 | No | No | **0** |
| prashasti-jain | 0.7 | 0 | 1,267.00 | No | No | **0** |
| suhas-kakde | 3.1 | 0 | 525.00 | No (>500) | No | **0** |

---

## CRQC Final Summary — Q2 2026

### 🌟 Tier A (C+R ≥ 6, no override)
amol-salunkhe (C3+R3=6), mshnayderman (C3+R3=6), rpawar-nice (C3+R3=6)

### 👍 Tier B (C+R = 4–5 or override)
chris-haun (C2+R2=4, Q expected ≥1), mfield1 (C2+R2=4, Q expected ≥1), Vitthal-Nice (C3+R2=5), jayesh-rai (C3+R2=5 + Breakout), copilotshree (C2+R3=5), dannycadima (C2+R3=5)*

### 👌 Tier C
Prathmesh-Ranadive (capped — 4,001 Q2 Prem), PradnyeshSalunke (capped — 3,754 Q2 Prem), Kranti-nice (Breakout override → C from D), sskalaskar, tusharpatil166719, Akale23, mshivarkar (Breakout override), moadzughul, vishal-tad, trunalgawade, sgite-wfm, smishra-nice

### 🟠 Tier D
dsuraj25, shreedevi-nice, nilesht-19, Vyankatesh95, jkumbhar, luisalvatierra, abhijeetk268 (eligible C), meghabiradar05, pdevle (eligible C), abhishekhole-nice (zero window), thakraln (eligible C*), kbajaj-nice, pratikpawar12, Shubhamfulzele28 (new)

### 🔴 Tier E
suhas-kakde (R=0 + Q2 Prem>500, C=0), prashasti-jain (C=0, R=0)

---

## ⚠️ Q2 Budget Alert — Override Rule Applications

| User | Q2 Prem | Q2 LoC | Q2 ReqEff | Override Applied |
|---|---|---|---|---|
| Prathmesh-Ranadive | 4,001 | 20,436 | 5.1 | R=0 (outlier penalty) → Max Tier C |
| Nilesh Tonape | 3,988 | 5,293 | 1.3 | R=0 (outlier penalty) → Max Tier C — floor stays D |
| Pradnyesh Salunke | 3,754 | 2,296 | 0.6 | R=0 (outlier penalty) → Max Tier C |
| Kranti Kaple | 3,660 | 27,733 | 7.6 | R=0 (outlier penalty) → Max Tier C — Breakout allows C |
| Nishtha Thakral | 1,042 | 69 | 0.1 | R=0 + Prem>500 → Max Tier C — Breakout eligible for C |
| Prashasti Jain | 1,267 | 872 | 0.7 | R=0 + Prem>500 → Max Tier C — C+R=0 floors at E |
| Suhas Kakde | 525 | 1,639 | 3.1 | R=0 + Prem>500 → Max Tier C — C+R=0 floors at E |
| Luis Salvatierra | 952 | 4,564 | 4.8 | R=0 + Prem>500 → Max Tier C — floor stays D |
| Jyoti Kumbhar | 591 | 1,868 | 3.2 | R=0 + Prem>500 → Max Tier C — floor stays D |
| Vyankatesh Khadakkar | 931 | 4,151 | 4.5 | R=0 + Prem>500 → Max Tier C — floor stays D |

> **Q2 Budget concentration**: 4 outlier spenders (Prathmesh 4,001 + Nilesh 3,988 + Pradnyesh 3,754 + Kranti 3,660) consumed **15,403 Q2 Premium Requests** — approximately 54% of the 37-user analysis pool's premium budget across the full quarter, while representing only 10.8% of the team.

---

## VP Narrative Template — Q2 2026

> "Our CRQC framework scores each developer across Core (adoption quality), ROI (budget efficiency), and Quality (code delivery — Feature Branch this period) using cumulative Q2 data from April 1 through June 3.
>
> **Tier A (3 users)** score 6/9+ on Core + ROI alone using their full 9-week Q2 track record: Amol Salunkhe (3,387 LoC/week), Mikhail Shnayderman (2,710 LoC/week), Ritesh Pawar (962 LoC/week). These users produce top-tier output with strong budget efficiency sustained across the quarter.
>
> **Budget concern (4 outlier spenders)**: Prathmesh Ranadive, Pradnyesh Salunke, Kranti Kaple, and Nilesh Tonape collectively consumed **15,403 Q2 Premium Requests** — roughly 54% of the team's Q2 premium budget while representing only 10.8% of the team. CRQC override rule caps all four at Tier C or below. This is a Q3 budget governance priority.
>
> **Final window momentum (positive)**: Mohan Shivarkar (+1,531 LoC in final 16 days — recovery confirmed), Jayesh Rai (+1,334 LoC), Pratik Devle (+679 LoC), Abhijeet Kolhe (+483 LoC) are all entering Q3 with strong momentum.
>
> **Re-engagement needed**: Six users produced zero LoC in the final 16 days of Q2 — Shraddha Kale, Abhishek Hole, Suhas Kakde, Shridhar Mishra, Pratik Pawar, Kaushal Bajaj. Their Q2 numbers are front-loaded. Without early Q3 re-engagement, slow starts are likely."
