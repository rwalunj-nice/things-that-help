# GitHub Copilot Usage Analysis — June 3, 2026 (v2 Workflow-Aware)

> **Framework**: Workflow-Aware Benchmark (github-quick-benchmark-v2.md)
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM
> **Analysis Date**: June 3, 2026 | **Data Synced**: June 3, 2026
> **Active Analysis Users**: 37 | **Ignored/Excluded**: 15 ignored + 2 managers + 1 research + 6 inactive

---

## ⚡ What Changed vs v1

> v2 applies workflow-type classification **before** benchmarking. % Code Acceptance is NOT applied to Agent-First users. Separate benchmarks for Agent-First (ReqEff > 15), Hybrid (% Accept 15–30% + ReqEff > 8), and Inline-First (% Accept 20–35%).

| v1 Issue Fixed in v2 | Impact |
|---|---|
| Kranti Kaple penalized for 1.3% accept | v2 recognizes Agent-First — benchmarks on LoC + ReqEff |
| Abhishek Hole's 0% accept flagged as failure | v2: 0% accept is correct for pure Agent-First |
| Prathmesh's 84.8% accept misread as "too high" | v2: Inline-First users scored on accept rate appropriately |
| Nilesh Tonape: hybrid pattern missed | v2: 3,988 Prem + 16.1% accept = Hybrid spending concern, not pure inline failure |

---

## 🔄 Step 0 — Workflow Type Classification

> **Note**: Agent Contribution % column was not visible in Power BI USER METRICS screenshots this period. Workflow type inferred from SuggEff pattern, % Accept, and prior period classifications.

| Workflow Type | Criteria Used | Users |
|---|---|---|
| **Agent-First** | SuggEff > 20 AND % Accept < 12% | mshnayderman, rpawar-nice, abhishekhole-nice, Kranti-nice, shreedevi-nice, amol-salunkhe, moadzughul, suhas-kakde, thakraln |
| **Hybrid** | Mixed SuggEff or % Accept 5–30% with agent spend | Vyankatesh95, abhijeetk268, sskalaskar, tusharpatil166719, jkumbhar, nilesht-19, mfield1, pdevle, jayesh-rai, meghabiradar05, copilotshree, prashasti-jain, chris-haun, dsuraj25, mshivarkar, luisalvatierra, vishal-tad, pratikpawar12 |
| **Inline-First** | % Accept > 20% as primary signal, low SuggEff | Prathmesh-Ranadive, PradnyeshSalunke, Vitthal-Nice, smishra-nice, Akale23, trunalgawade, sgite-wfm, dannycadima, kbajaj-nice |

---

## 📊 v2 Tier Table

| # | Login | Name | Workflow | LoC | % Accept | SuggEff | Prem | ReqEff | v2 Tier | vs v1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | amol-salunkhe | Amol Salunkhe | Agent-First | 30,486 | 1.8% | 30.01 | 748 | 40.8 | 🌟 A | = |
| 2 | Kranti-nice | Kranti Kaple | Agent-First | 27,733 | 1.3% | 39.01 | 3,660 | 7.6 | 👍 B⚠️ | ↓ from A — outlier spend |
| 3 | mshnayderman | Mikhail Shnayderman | Agent-First | 24,387 | 11.0% | 70.48 | 565 | 43.2 | 🌟 A | = |
| 4 | Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 20,436 | 84.8% | 18.97 | 4,001 | 5.1 | 👍 B⚠️ | ↓ from A — outlier spend |
| 5 | chris-haun | Chris Haun | Hybrid | 10,264 | 12.8% | 10.31 | 860 | 11.9 | 🌟 A | = |
| 6 | mfield1 | Matt Field | Hybrid | 9,251 | 5.0% | 14.34 | 620 | 14.9 | 🌟 A | = |
| 7 | rpawar-nice | Ritesh Pawar | Agent-First | 8,662 | 8.1% | 64.16 | 431 | 20.1 | 🌟 A | = |
| 8 | nilesht-19 | Nilesh Tonape | Hybrid | 5,293 | 16.1% | 18.57 | 3,988 | 1.3 | 🟠 D⚠️ | ↓ — outlier spend, ReqEff 1.3 fails Hybrid T2 |
| 9 | copilotshree | Shraddha Kale | Hybrid | 5,013 | 4.8% | 11.02 | 340 | 14.8 | 🌟 A | ↑ from B — v2 rewards lean spend + good ReqEff |
| 10 | luisalvatierra | Luis Salvatierra | Hybrid | 4,564 | 12.3% | 7.47 | 952 | 4.8 | 🟠 D | ↓ — fails Hybrid ReqEff > 8 benchmark |
| 11 | Vyankatesh95 | Vyankatesh Khadakkar | Hybrid | 4,151 | 35.9% | 31.69 | 931 | 4.5 | 👌 C | ↑ from C — accept rate near range |
| 12 | moadzughul | Moad Alzughul | Agent-First | 3,035 | 3.3% | 11.12 | 408 | 7.4 | 👌 C | = |
| 13 | vishal-tad | Vishal Tad | Hybrid | 2,815 | 6.5% | 6.73 | 368 | 7.6 | 👌 C | 🆕 New |
| 14 | abhishekhole-nice | Abhishek Hole | Agent-First | 2,803 | 0.0% | 56.06 | 379 | 7.4 | 👌 C | = |
| 15 | sskalaskar | Sourabh Kalaskar | Hybrid | 2,609 | 17.1% | 23.50 | 457 | 5.7 | 👌 C | = |
| 16 | Vitthal-Nice | Vitthal Devkar | Inline-First | 2,609 | 41.9% | 13.66 | 282 | 9.3 | 👍 B | = |
| 17 | jayesh-rai | Jayesh Rai | Hybrid | 2,196 | 21.5% | 12.77 | 250 | 8.8 | 👍 B | ↑ from B — barely meets Hybrid T1+T2 |
| 18 | Akale23 | Amulya Kale | Inline-First | 2,409 | 19.7% | 6.34 | 333 | 7.2 | 👌 C | ↑ from D — v2 scores inline-first more fairly |
| 19 | PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 2,296 | 37.7% | 14.91 | 3,754 | 0.6 | 🔴 E | ↓ — outlier spend + ReqEff 0.6 = critical |
| 20 | meghabiradar05 | Megha Biradar | Hybrid | 1,684 | 6.6% | 11.15 | 435 | 3.9 | 🟠 D | = |
| 21 | tusharpatil166719 | Tushar Patil | Hybrid | 1,798 | 15.9% | 20.43 | 441 | 4.1 | 🟠 D | = |
| 22 | jkumbhar | Jyoti Kumbhar | Hybrid | 1,868 | 18.4% | 19.06 | 591 | 3.2 | 🟠 D | = |
| 23 | mshivarkar | Mohan Shivarkar | Hybrid | 1,559 | 14.7% | 8.81 | 285 | 5.5 | 👌 C | ↑ +5,468% recovery |
| 24 | suhas-kakde | Suhas Kakde | Agent-First | 1,639 | 1.8% | 7.38 | 525 | 3.1 | 🟠 D | = |
| 25 | shreedevi-nice | Shreedevi Patil | Agent-First | 1,013 | 11.5% | 38.96 | 433 | 2.3 | 🟠 D | = |
| 26 | pdevle | Pratik Devle | Hybrid | 1,049 | 5.4% | 14.18 | 261 | 4.0 | 🟠 D | 🚀 Breakout +184% |
| 27 | abhijeetk268 | Abhijeet Kolhe | Hybrid | 656 | 32.0% | 26.24 | 344 | 1.9 | 🟠 D | 🚀 Breakout +279% |
| 28 | prashasti-jain | Prashasti Jain | Hybrid | 872 | 8.4% | 10.51 | 1,267 | 0.7 | 🔴 E | ↓ — high spend, near-zero ROI |
| 29 | dsuraj25 | Suraj Dubey | Hybrid | 504 | 9.3% | 9.33 | 98 | 5.1 | 👌 C | ↑ — lean spend redeems low volume |
| 30 | smishra-nice | Shridhar Mishra | Inline-First | 155 | 78.3% | 6.74 | 257 | 0.6 | 🟠 D | = — high accept, zero output |
| 31 | trunalgawade | Trunal Gawade | Inline-First | 304 | 23.0% | 1.23 | 134 | 2.3 | 🟠 D | = |
| 32 | sgite-wfm | Shubham Gite | Inline-First | 316 | 54.6% | 1.17 | 126 | 2.5 | 👌 C | ↑ — v2 rewards high accept for inline users |
| 33 | thakraln | Nishtha Thakral | Agent-First | 69 | 0.0% | 3.45 | 1,042 | 0.1 | 🔴 E | = — high spend, near-zero output |
| 34 | pratikpawar12 | Pratik Pawar | Hybrid | 250 | 4.3% | 2.14 | 375 | 0.7 | 🔴 E | = |
| 35 | dannycadima | Danny Cadima Molina | Inline-First | 34 | 12.7% | 0.14 | 3 | 11.0 | 🟠 D | = — lean spend, minimal output |
| 36 | kbajaj-nice | Kaushal Bajaj | Inline-First | 5 | 17.5% | 0.13 | 6 | 0.8 | 🔴 E | = — near-zero everything |
| 37 | Shubhamfulzele28 | Shubham Fulzele | — | 0 | 0.0% | 0.00 | 170 | 0.0 | 🆕 New | — |

---

## 🌟 Tier A (v2) — 6 Users

**Agent-First**: amol-salunkhe (ReqEff 40.8), mshnayderman (ReqEff 43.2), rpawar-nice (ReqEff 20.1)
**Hybrid**: mfield1 (ReqEff 14.9), chris-haun (ReqEff 11.9), copilotshree (ReqEff 14.8)

> copilotshree **promoted** from B in v1 to A in v2 — their lean Hybrid profile (4.8% accept + 14.8 ReqEff + 340 Prem) scores better under workflow-aware benchmarks than under v1's accept-rate-first lens.

---

## 👍 Tier B (v2) — 4 Users

| User | Workflow | Reason for B |
|---|---|---|
| Kranti-nice | Agent-First | 27,733 LoC but ReqEff 7.6 — output strong, ROI weak. Outlier spend caps at B. |
| Prathmesh-Ranadive | Inline-First | 84.8% accept + 20,436 LoC but 4,001 Prem Req. Inline power but budget concern. |
| Vitthal-Nice | Inline-First | 41.9% accept, 2,609 LoC, lean spend — solid Inline-First |
| jayesh-rai | Hybrid | 21.5% accept in range, ReqEff 8.8 meets Hybrid T2, lean spend |

---

## 👌 Tier C (v2) — 8 Users

abhishekhole-nice, Vyankatesh95, moadzughul, sskalaskar, vishal-tad, Akale23, mshivarkar (recovery), dsuraj25, sgite-wfm

---

## 🟠 Tier D (v2) — 11 Users

nilesht-19 ⚠️, luisalvatierra, meghabiradar05, tusharpatil166719, jkumbhar, shreedevi-nice, suhas-kakde, pdevle 🚀, abhijeetk268 🚀, smishra-nice, trunalgawade, dannycadima

---

## 🔴 Tier E (v2) — 5 Users

PradnyeshSalunke ⚠️, prashasti-jain ⚠️, thakraln ⚠️, pratikpawar12, kbajaj-nice

---

## 📊 v2 Executive Scorecard

| Tier | Count | Key Change from v1 |
|---|---|---|
| 🌟 A | 6 | −1: copilotshree promoted from B; Kranti/Prathmesh moved to B for ROI |
| 👍 B | 4 | +2 from A (Kranti, Prathmesh); copilotshree removed |
| 👌 C | 9 | sgite-wfm promoted from D; dsuraj25 promoted |
| 🟠 D | 11 | nilesht-19 dropped from C; luisalvatierra dropped |
| 🔴 E | 5 | PradnyeshSalunke dropped due to outlier spend + 0.6 ReqEff |

> **Key v2 finding**: Budget efficiency now drives tier placement. 4 users with outlier Premium spend (>1,700 Prem Req) — Prathmesh, Kranti, Nilesh, Pradnyesh — are all capped at B or below regardless of LoC output.
