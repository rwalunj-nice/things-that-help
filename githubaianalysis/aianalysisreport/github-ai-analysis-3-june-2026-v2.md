# GitHub Copilot Usage Analysis — June 3, 2026 (v2 Workflow-Aware)

> **Framework**: Workflow-Aware Benchmark (github-quick-benchmark-v2.md)
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM
> **Analysis Date**: June 3, 2026 | **Data Synced**: June 3, 2026
> **Active Analysis Users**: 37 | **Ignored/Excluded**: 15 ignored + 2 managers + 1 research + 6 inactive

> ⚠️ **Q2 Cumulative Data**: All metrics represent **running totals from April 1 through June 3, 2026** (~9 weeks). Not a single-week snapshot. **Win LoC** = LoC added in the final ~16 days (May 18 → Jun 3).

---

## ⚡ What Changed vs v1

> v2 applies workflow-type classification **before** benchmarking. % Code Acceptance is NOT applied to Agent-First users. Separate benchmarks for Agent-First (ReqEff > 15), Hybrid (% Accept 15–30% + ReqEff > 8), and Inline-First (% Accept 20–35%).

| v1 Issue Fixed in v2 | Impact |
|---|---|
| Kranti Kaple penalized for 1.3% accept | v2 recognises Agent-First — benchmarks on Q2 LoC + ReqEff |
| Abhishek Hole's 0% accept flagged as failure | v2: 0% accept correct for pure Agent-First |
| Prathmesh's 84.8% accept misread as "too high" | v2: Inline-First scored on accept rate appropriately |
| Nilesh Tonape: hybrid pattern missed | v2: 3,988 Q2 Prem + 16.1% accept = Hybrid budget concern |

---

## 🔄 Step 0 — Workflow Type Classification

> Agent Contribution % column not visible this period. Workflow type inferred from SuggEff pattern, % Accept, and prior period classifications.

| Workflow Type | Criteria Used | Users |
|---|---|---|
| **Agent-First** | SuggEff > 20 AND % Accept < 12% | mshnayderman, rpawar-nice, abhishekhole-nice, Kranti-nice, shreedevi-nice, amol-salunkhe, moadzughul, suhas-kakde, thakraln |
| **Hybrid** | Mixed SuggEff or % Accept 5–30% with agent spend | Vyankatesh95, abhijeetk268, sskalaskar, tusharpatil166719, jkumbhar, nilesht-19, mfield1, pdevle, jayesh-rai, meghabiradar05, copilotshree, prashasti-jain, chris-haun, dsuraj25, mshivarkar, luisalvatierra, vishal-tad, pratikpawar12 |
| **Inline-First** | % Accept > 20% as primary signal, low SuggEff | Prathmesh-Ranadive, PradnyeshSalunke, Vitthal-Nice, smishra-nice, Akale23, trunalgawade, sgite-wfm, dannycadima, kbajaj-nice |

---

## 📊 v2 Tier Table — Q2 Cumulative

> **Win LoC** = May 18 → Jun 3 window. **LoC/wk** = Q2 total ÷ 9 weeks.

| # | Login | Name | Workflow | Q2 LoC | Win LoC | LoC/wk | % Accept | SuggEff | Prem | ReqEff | v2 Tier | vs v1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | amol-salunkhe | Amol Salunkhe | Agent-First | 30,486 | +1,575 | 3,387 | 1.8% | 30.01 | 748 | 40.8 | 🌟 A | = |
| 2 | Kranti-nice | Kranti Kaple | Agent-First | 27,733 | +20,657 | 3,082 | 1.3% | 39.01 | 3,660 | 7.6 | 👍 B⚠️ | ↓ from A — outlier Q2 spend |
| 3 | mshnayderman | Mikhail Shnayderman | Agent-First | 24,387 | +2,119 | 2,710 | 11.0% | 70.48 | 565 | 43.2 | 🌟 A | = |
| 4 | Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 20,436 | +10,947 | 2,271 | 84.8% | 18.97 | 4,001 | 5.1 | 👍 B⚠️ | ↓ from A — outlier Q2 spend |
| 5 | chris-haun | Chris Haun | Hybrid | 10,264 | +1,672 | 1,140 | 12.8% | 10.31 | 860 | 11.9 | 🌟 A | = |
| 6 | mfield1 | Matt Field | Hybrid | 9,251 | +180 | 1,028 | 5.0% | 14.34 | 620 | 14.9 | 🌟 A | = |
| 7 | rpawar-nice | Ritesh Pawar | Agent-First | 8,662 | +4 | 962 | 8.1% | 64.16 | 431 | 20.1 | 🌟 A | = |
| 8 | nilesht-19 | Nilesh Tonape | Hybrid | 5,293 | +228 | 588 | 16.1% | 18.57 | 3,988 | 1.3 | 🟠 D⚠️ | ↓ — outlier Q2 spend, ReqEff 1.3 |
| 9 | copilotshree | Shraddha Kale | Hybrid | 5,013 | 0 | 557 | 4.8% | 11.02 | 340 | 14.8 | 🌟 A | ↑ from B — lean Q2 spend + ReqEff |
| 10 | luisalvatierra | Luis Salvatierra | Hybrid | 4,564 | +2,272 | 507 | 12.3% | 7.47 | 952 | 4.8 | 🟠 D | ↓ — fails Hybrid ReqEff > 8 |
| 11 | Vyankatesh95 | Vyankatesh Khadakkar | Hybrid | 4,151 | +478 | 461 | 35.9% | 31.69 | 931 | 4.5 | 👌 C | = |
| 12 | moadzughul | Moad Alzughul | Agent-First | 3,035 | +286 | 337 | 3.3% | 11.12 | 408 | 7.4 | 👌 C | = |
| 13 | vishal-tad | Vishal Tad | Hybrid | 2,815 | 2,815 | 313 | 6.5% | 6.73 | 368 | 7.6 | 👌 C | 🆕 New |
| 14 | abhishekhole-nice | Abhishek Hole | Agent-First | 2,803 | 0 | 311 | 0.0% | 56.06 | 379 | 7.4 | 👌 C | = |
| 15 | sskalaskar | Sourabh Kalaskar | Hybrid | 2,609 | +553 | 290 | 17.1% | 23.50 | 457 | 5.7 | 👌 C | = |
| 16 | Vitthal-Nice | Vitthal Devkar | Inline-First | 2,609 | +43 | 290 | 41.9% | 13.66 | 282 | 9.3 | 👍 B | = |
| 17 | jayesh-rai | Jayesh Rai | Hybrid | 2,196 | +1,334 | 244 | 21.5% | 12.77 | 250 | 8.8 | 👍 B | ↑ — meets Hybrid T1+T2, lean spend |
| 18 | Akale23 | Amulya Kale | Inline-First | 2,409 | +553 | 268 | 19.7% | 6.34 | 333 | 7.2 | 👌 C | ↑ from D — inline-first scored fairly |
| 19 | PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 2,296 | +348 | 255 | 37.7% | 14.91 | 3,754 | 0.6 | 🔴 E | ↓ — outlier Q2 spend + ReqEff 0.6 |
| 20 | meghabiradar05 | Megha Biradar | Hybrid | 1,684 | +295 | 187 | 6.6% | 11.15 | 435 | 3.9 | 🟠 D | = |
| 21 | tusharpatil166719 | Tushar Patil | Hybrid | 1,798 | +167 | 200 | 15.9% | 20.43 | 441 | 4.1 | 🟠 D | = |
| 22 | jkumbhar | Jyoti Kumbhar | Hybrid | 1,868 | +80 | 208 | 18.4% | 19.06 | 591 | 3.2 | 🟠 D | = |
| 23 | mshivarkar | Mohan Shivarkar | Hybrid | 1,559 | +1,531 | 173 | 14.7% | 8.81 | 285 | 5.5 | 👌 C | ↑ recovery — +1,531 in final window |
| 24 | suhas-kakde | Suhas Kakde | Agent-First | 1,639 | 0 | 182 | 1.8% | 7.38 | 525 | 3.1 | 🟠 D | = |
| 25 | shreedevi-nice | Shreedevi Patil | Agent-First | 1,013 | +323 | 113 | 11.5% | 38.96 | 433 | 2.3 | 🟠 D | = |
| 26 | pdevle | Pratik Devle | Hybrid | 1,049 | +679 | 117 | 5.4% | 14.18 | 261 | 4.0 | 🟠 D | 🚀 +679 in final window |
| 27 | abhijeetk268 | Abhijeet Kolhe | Hybrid | 656 | +483 | 73 | 32.0% | 26.24 | 344 | 1.9 | 🟠 D | 🚀 +483 in final window |
| 28 | prashasti-jain | Prashasti Jain | Hybrid | 872 | +35 | 97 | 8.4% | 10.51 | 1,267 | 0.7 | 🔴 E | ↓ — 1,267 Q2 Prem, near-zero ROI |
| 29 | dsuraj25 | Suraj Dubey | Hybrid | 504 | +13 | 56 | 9.3% | 9.33 | 98 | 5.1 | 👌 C | ↑ — lean Q2 spend redeems low volume |
| 30 | smishra-nice | Shridhar Mishra | Inline-First | 155 | 0 | 17 | 78.3% | 6.74 | 257 | 0.6 | 🟠 D | = |
| 31 | trunalgawade | Trunal Gawade | Inline-First | 304 | +2 | 34 | 23.0% | 1.23 | 134 | 2.3 | 🟠 D | = |
| 32 | sgite-wfm | Shubham Gite | Inline-First | 316 | +45 | 35 | 54.6% | 1.17 | 126 | 2.5 | 👌 C | ↑ — high accept rewarded for inline |
| 33 | thakraln | Nishtha Thakral | Agent-First | 69 | +69 | 8 | 0.0% | 3.45 | 1,042 | 0.1 | 🔴 E | = — 1,042 Q2 Prem for 69 LoC |
| 34 | pratikpawar12 | Pratik Pawar | Hybrid | 250 | 0 | 28 | 4.3% | 2.14 | 375 | 0.7 | 🔴 E | = |
| 35 | dannycadima | Danny Cadima Molina | Inline-First | 34 | +33 | 4 | 12.7% | 0.14 | 3 | 11.0 | 🟠 D | = — lean spend, near-zero Q2 output |
| 36 | kbajaj-nice | Kaushal Bajaj | Inline-First | 5 | 0 | 1 | 17.5% | 0.13 | 6 | 0.8 | 🔴 E | = — near-zero everything |
| 37 | Shubhamfulzele28 | Shubham Fulzele | — | 0 | 0 | 0 | 0.0% | 0.00 | 170 | 0.0 | 🆕 New | — |

---

## 🌟 Tier A (v2) — 6 Users

**Agent-First**: amol-salunkhe (ReqEff 40.8, 3,387 LoC/wk), mshnayderman (ReqEff 43.2, 2,710 LoC/wk), rpawar-nice (ReqEff 20.1, 962 LoC/wk)
**Hybrid**: mfield1 (ReqEff 14.9, 1,028 LoC/wk), chris-haun (ReqEff 11.9, 1,140 LoC/wk), copilotshree (ReqEff 14.8, 557 LoC/wk)

> **rpawar-nice note**: 962 LoC/wk Q2 average but only +4 in final window. Q2 effort was April–May concentrated. Tier A stands on cumulative basis.
> **copilotshree note**: 557 LoC/wk Q2 average but zero in final window. Lean spend and strong ReqEff throughout Q2 earns Tier A in v2.

---

## 👍 Tier B (v2) — 4 Users

| User | Workflow | Q2 LoC | Win LoC | LoC/wk | Reason for B |
|---|---|---|---|---|---|
| Kranti-nice | Agent-First | 27,733 | +20,657 | 3,082 | Exceptional output; ReqEff 7.6 weak; 3,660 Q2 Prem outlier |
| Prathmesh-Ranadive | Inline-First | 20,436 | +10,947 | 2,271 | Inline power user; 4,001 Q2 Prem outlier caps at B |
| Vitthal-Nice | Inline-First | 2,609 | +43 | 290 | 41.9% accept, lean Q2 spend — solid inline |
| jayesh-rai | Hybrid | 2,196 | +1,334 | 244 | In benchmark % Accept; ReqEff 8.8; lean spend; strong final window |

---

## 👌 Tier C (v2) — 9 Users

| User | Q2 LoC | Win LoC | Note |
|---|---|---|---|
| abhishekhole-nice | 2,803 | 0 | Good Q2 cumulative; zero in final window |
| Vyankatesh95 | 4,151 | +478 | Steady pacing |
| moadzughul | 3,035 | +286 | Steady agent output |
| sskalaskar | 2,609 | +553 | Consistent hybrid |
| vishal-tad | 2,815 | 2,815 | 🆕 New — strong debut |
| Akale23 | 2,409 | +553 | Steady inline-first |
| mshivarkar | 1,559 | +1,531 | 🚀 Recovery — +1,531 in final 16 days |
| dsuraj25 | 504 | +13 | Lean spend earns C; 504 LoC Q2 total is very low |
| sgite-wfm | 316 | +45 | 54.6% accept inline; low Q2 volume |

---

## 🟠 Tier D (v2) — 12 Users

nilesht-19 ⚠️ (3,988 Q2 Prem), luisalvatierra (fails ReqEff despite +2,272 final window), meghabiradar05, tusharpatil166719, jkumbhar (+80 final, slowing), shreedevi-nice, suhas-kakde (0 final window), pdevle 🚀 (+679 final), abhijeetk268 🚀 (+483 final), smishra-nice (0 final, 155 Q2 total), trunalgawade (+2 final), dannycadima

---

## 🔴 Tier E (v2) — 5 Users

| User | Q2 LoC | Q2 Prem | Win LoC | Core issue |
|---|---|---|---|---|
| PradnyeshSalunke | 2,296 | 3,754 | +348 | 3,754 Q2 Premium for 2,296 LoC |
| prashasti-jain | 872 | 1,267 | +35 | 1,267 Q2 Premium for 872 LoC — inverted ROI |
| thakraln | 69 | 1,042 | +69 | 1,042 Q2 Premium for 69 total LoC |
| pratikpawar12 | 250 | 375 | 0 | Zero in final window; 250 LoC entire Q2 |
| kbajaj-nice | 5 | 6 | 0 | 5 LoC entire Q2 |

---

## 📊 v2 Executive Scorecard — Q2 2026

| Tier | Count | Q2 LoC | LoC/wk avg | Key Change from v1 |
|---|---|---|---|---|
| 🌟 A | 6 | ~88,077 | ~1,630/wk | copilotshree promoted; Kranti/Prathmesh to B for ROI |
| 👍 B | 4 | ~52,874 | ~1,469/wk | Kranti/Prathmesh from A; Vitthal/Jayesh confirmed |
| 👌 C | 9 | ~22,152 | ~274/wk | sgite-wfm + dsuraj25 promoted; mshivarkar recovery |
| 🟠 D | 12 | ~17,695 | ~179/wk | nilesht-19 + luisalvatierra dropped |
| 🔴 E | 5 | ~1,230 | ~27/wk | PradnyeshSalunke dropped for outlier Q2 spend |

> **Key v2 Q2 finding**: Budget efficiency across 9 weeks drives tier placement. 4 users consumed 15,403 Q2 Premium Requests — capped at B or below regardless of LoC output. Across a full quarter this spend compounds significantly.

---

## 📈 Final Window Velocity — Entering Q3 Hot vs Cold

| Status | Users | Q3 Signal |
|---|---|---|
| 🚀 **Hot** (>500 Win LoC) | Kranti (+20,657), Prathmesh (+10,947), Luis (+2,272), Mikhail (+2,119), Vishal (2,815 new), Chris (+1,672), Amol (+1,575), Mohan (+1,531), Jayesh (+1,334), Pratik Devle (+679), Abhijeet (+483) | Strong momentum entering Q3 |
| ➡️ **Warm** (100–500 Win LoC) | Vyankatesh (+478), Sourabh (+553), Amulya (+553), Shreedevi (+323), Pradnyesh (+348), Megha (+295), Moad (+286), Nilesh (+228), Tushar (+167) | Moderate momentum |
| ❄️ **Cold** (1–99 Win LoC) | Matt (+180), Jyoti (+80), Shubham Gite (+45), Danny (+33), Nishtha (+69), Prashasti (+35), Trunal (+2), Suraj (+13) | Low momentum — risk of slow Q3 start |
| 🔴 **Stopped** (0 Win LoC) | Shraddha (0), Abhishek (0), Suhas (0), Shridhar (0), Pratik Pawar (0), Kaushal (0) | Zero output in final 16 days — needs immediate re-engagement in Q3 |
