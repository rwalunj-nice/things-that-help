# GitHub Copilot Usage Analysis — May 18, 2026 (v2 Workflow-Aware)

> **Framework**: v2 Workflow-Aware (Agent-First / Hybrid / Inline-First)  
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM  
> **Analysis Date**: May 18, 2026 | **Data Synced**: May 17, 2026 10:30 PM  
> **Total Users**: 55 (50 active Copilot users)

---

## Workflow Type Assignment

> **Note**: Agent Contribution % column not visible in current Power BI view. Workflow type inferred from % Code Acceptance + Suggestion Efficiency pattern, consistent with prior period methodology.
>
> - **Agent-First**: % Accept < 5% AND SuggEff > 10 (or near-zero Accept with high SuggEff)
> - **Hybrid**: % Accept 5–30% (or mixed signals)
> - **Inline-First**: % Accept > 30% (consistent acceptance of inline suggestions)
> - **⚠ NEVER penalise Agent-First users for low % Accept — this is by design**

---

## Agent-First Users (17 active)

> These users generate code primarily via Copilot agents. % Code Acceptance is structurally near-zero and **must not** be used to evaluate them. Evaluate on LoC Added + Suggestion Efficiency.

| User Login | Name | Int | LoC Added | % Accept | SuggEff | Tier |
|---|---|---|---|---|---|---|
| dhanshree-jagtap-nice | Dhanshree Jagtap | 284 | 35,646 | 10.7% | 75.04 | 🌟 A |
| amol-salunkhe | Amol Salunkhe | 283 | 28,911 | 2.2% | 35.47 | 🌟 A |
| mshnayderman | Mikhail Shnayderman | 162 | 22,268 | 0.3% | 72.06 | 🌟 A |
| nice-harshada | Harshada Bagane | 92 | 17,600 | 2.0% | 11.89 | 🌟 A |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | 627 | 13,006 | 0.9% | 23.48 | 🌟 A |
| tomotvos | Tom Otvos | 68 | 5,061 | 0.0% | 51.12 | 🌟 A |
| rpawar-nice | Ritesh Pawar | 60 | 8,658 | 5.9% | 72.76 | 👍 B |
| abhishekhole-nice | Abhishek Hole | 132 | 2,803 | 0.0% | 56.06 | 👍 B |
| GovindSomaniNice | Govind Somani | 44 | 2,356 | 1.2% | 27.72 | 👍 B |
| moadzughul | Moad Alzughul | 109 | 2,749 | 2.8% | 15.27 | 👍 B |
| SwapnilNice | Swapnil Zade | 263 | 3,140 | 4.0% | 31.72 | Manager |
| Kranti-nice | Kranti Kaple | 323 | 7,076 | 1.8% | 13.87 | 👍 B |
| suhas-kakde | Suhas Kakde | 165 | 1,639 | 1.8% | 7.45 | 👌 C |
| jayesh-rai | Jayesh Rai | 73 | 862 | 2.7% | 7.77 | 🟠 D |
| dsuraj25 | Suraj Dubey | 11 | 491 | 0.0% | 16.37 | 🟠 D |
| thakraln | Nishtha Thakral | 65 | 0 | 0.0% | 0.00 | 🔴 E |
| dannycadima | Danny Cadima Molina | 3 | 1 | 3.8% | 0.04 | 🔴 E |

### Agent-First Tier Benchmarks
| Signal | Condition | Score |
|---|---|---|
| LoC Added | > 8,000 | Strong (Tier A) |
| LoC Added | 3,000–8,000 | Solid (Tier B) |
| LoC Added | 1,000–3,000 | Developing (Tier C) |
| LoC Added | < 1,000 | Low (Tier D/E) |
| SuggEff | > 30 | Elite agent usage |
| SuggEff | 10–30 | Healthy |
| SuggEff | < 10 | Agent sessions not producing |

---

## Hybrid Users (18 active)

> Mixed workflow. % Code Acceptance is a valid (but not sole) signal. Target: 15–30% acceptance with healthy LoC.

| User Login | Name | Int | LoC Added | % Accept | SuggEff | Tier |
|---|---|---|---|---|---|---|
| mfield1 | Matt Field | 503 | 9,071 | 5.1% | 14.87 | 🌟 A |
| chris-haun | Chris Haun | 887 | 8,592 | 14.9% | 10.22 | 👍 B |
| yogitadhanwate | Yogita Dhanwate | 338 | 7,221 | 10.7% | 14.24 | 👍 B |
| nilesht-19 | Nilesh Tonape | 694 | 5,065 | 13.2% | 24.83 | 👍 B |
| copilotshree | Shraddha Kale | 621 | 5,013 | 4.8% | 11.02 | 👍 B |
| sskalaskar | Sourabh Kalaskar | 168 | 2,056 | 15.3% | 28.56 | 👍 B |
| luisalvatierra | Luis Salvatierra | 399 | 2,292 | 9.7% | 5.58 | 👍 B |
| AnaSarzosa | Ana Sarzosa | 139 | 2,021 | 6.6% | 7.86 | 👌 C |
| anjali-sherikar | Anjali Sherikar | 99 | 1,689 | 12.8% | 6.76 | 👌 C |
| tusharpatil166719 | Tushar Patil | 65 | 1,631 | 13.4% | 19.89 | 👌 C |
| jkumbhar | Jyoti Kumbhar | 193 | 1,788 | 20.7% | 21.80 | 👌 C |
| meghabirada05 | Megha Biradar | 46 | 1,389 | 5.7% | 15.97 | 👌 C |
| shreedevi-nice | Shreedevi Patil | 104 | 690 | 15.8% | 36.32 | 🟠 D |
| sohanbafna | Sohan Bafna | 11 | 467 | 7.7% | 35.92 | 🟠 D |
| pdevle | Pratik Devle | 30 | 370 | 6.6% | 6.07 | 🟠 D |
| prashasti-jain | Prashasti Jain | 24 | 837 | 10.0% | 27.90 | 🟠 D |
| pratikpawar12 | Pratik Pawar | 98 | 250 | 4.3% | 2.14 | 🟠 D |
| ssamal-nice | Susovan Samal | 2 | 38 | 8.3% | 3.17 | Manager |

### Hybrid Tier Benchmarks
| Signal | Condition |
|---|---|
| % Accept | Target 15–30% |
| LoC Added | > 5,000 = Tier A; 2,000–5,000 = Tier B; 500–2,000 = Tier C; < 500 = Tier D |
| SuggEff | > 10 adds confidence |

---

## Inline-First Users (9 active)

> Primary workflow is inline suggestion acceptance. % Code Acceptance is the primary signal. Target: 20–35%.

| User Login | Name | Int | LoC Added | % Accept | SuggEff | Tier |
|---|---|---|---|---|---|---|
| Prathmesh-Ranadive | Prathmesh Ranadive | 61 | 9,489 | **79.9%** | 13.50 | 🌟 A |
| Vyankatesh95 | Vyankatesh Khadakkar | 251 | 3,673 | **55.4%** | 44.25 | 👍 B |
| Vitthal-Nice | Vitthal Devkar | 137 | 2,566 | **44.1%** | 14.50 | 👍 B |
| PradnyeshSalunke | Pradnyesh Salunke | 269 | 1,948 | **38.0%** | 12.99 | 👍 B |
| Akale23 | Amulya Kale | 176 | 1,856 | 18.8% | 5.44 | 👌 C |
| abhijeetk268 | Abhijeet Kolhe | 15 | 173 | 17.4% | 7.52 | 🟠 D |
| smishra-nice | Shridhar Mishra | 59 | 155 | **78.3%** | 6.74 | 🟠 D |
| trunalgawade | Trunal Gawade | 100 | 302 | 23.7% | 1.32 | 🟠 D |
| mshivarkar | Mohan Shivarkar | 73 | 28 | **60.0%** | 0.93 | 🔴 E |
| kbajaj-nice | Kaushal Bajaj | 0 | 5 | 17.5% | 0.13 | 🔴 E |

### Inline-First Tier Benchmarks
| Signal | Condition |
|---|---|
| % Accept (target) | 20–35% for healthy inline usage |
| % Accept > 60% | Overly selective but may indicate lead/review role |
| LoC Added | Volume is the output validator |
| SuggEff < 5 | Accepting very small suggestions — needs longer completions |

---

## What Changed vs. v1 (Standard Tier)

| User | v1 Tier | v2 Tier | Reason |
|---|---|---|---|
| Suhas Kakde | C | C | Agent-First classification clarifies: low SuggEff is the concern, not low accept |
| Mohan Shivarkar | E | E | Inline-First with critically low SuggEff confirms E regardless of 60% accept |
| Shridhar Mishra | D | D | Inline-First correctly — 78% accept is intentional for manager/reviewer role |
| Prathmesh Ranadive | A | A | Inline-First, 79.9% accept + 9,489 LoC = elite inline user |
| Vyankatesh | B | B | Inline-First, 55.4% accept confirmed as excellent disciplined usage |
| Tom Otvos | A | A | Agent-First, 0% accept with SuggEff 51 = perfect agent profile |

---

## Workflow Distribution Summary

| Workflow | Count | Total LoC | % of LoC |
|---|---|---|---|
| Agent-First | 17 | 121,661 | 53.9% |
| Hybrid | 18 | 45,821 | 20.3% |
| Inline-First | 10 | 20,195 | 9.0% |
| Managers | 3 | 6,318 | 2.8% |
| Inactive/Excluded | 7 | — | — |
| **Total Active** | **48** | **193,995** | **86%** |

> **Key insight**: This team is overwhelmingly Agent-First (53.9% of LoC from 17 users). The expansion to 55 users has brought in heavy agent users (Dhanshree Jagtap, Harshada Bagane, Rizeq, Tom Otvos). Classic inline acceptance rates (20–35%) are now a minority pattern.
