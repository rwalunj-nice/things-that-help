# GitHub Copilot Usage Analysis — May 18, 2026 (CRQC Framework)

> **Framework**: CRQC — Core (C) + ROI (R) + Quality (Q) + Context (diagnostic)  
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM  
> **Analysis Date**: May 18, 2026 | **Data Synced**: May 17, 2026 10:30 PM  
> **Revision**: v2 — Full scroll verification complete. 9 previously missing users added. Premium Requests per user now available (actual data, replaces SuggEff proxy). Two corrections applied: nice-harshada Int 92→927; ssamal-nice Int 2→26.

---

## CRQC Scoring Overview

| Pillar | Max Score | Source |
|---|---|---|
| **C — Core** | 0–3 | AI Usage tab: LoC Added, % Accept, Suggestion Efficiency (by Workflow Type) |
| **R — ROI** | 0–3 (+1 lean bonus, −1 outlier penalty) | AI Usage tab + Premium Requests by User: Req Eff = LoC Added ÷ Premium Requests |
| **Q — Quality** | 0–3 | PR Details tab: Merge Rate, Reviews/PR, Time to Merge |
| **Context** | Diagnostic | Interactions, Code Gen patterns — explains C/R anomalies |

> **Premium Requests now available** from PREMIUM REQUESTS BY USER section (49 users). Actual Request Efficiency (LoC ÷ Prem Req) used for all R scores. Lean/Outlier bonuses now applied. This supersedes the SuggEff proxy used in v1 of this file.
>
> **Q scores**: PR data from May 11 session (Q1 2026, WFM Integrations, All branches). Per-user Q scores confirmed for 8 users. All others: Q=FB (Feature Branch — not captured, not Q=0).
>
> **Total team**: 55 rows in User Metrics. 50 active Copilot users. 5 truly inactive (no data). Managers and Research role excluded from tier scoring.

---

## Scoring Key

### C (Core) — by Workflow Type

**Agent-First** (% Accept < 5%, SuggEff > 10):
- LoC > 8,000 → C=3; LoC 3,000–8,000 → C=2; LoC 1,000–3,000 → C=1; LoC < 1,000 → C=0

**Hybrid** (% Accept 5–30%):
- LoC > 5,000 → C=3; LoC 2,000–5,000 → C=2; LoC 500–2,000 → C=1; LoC < 500 → C=0

**Inline-First** (% Accept > 30%):
- % Accept > 35% with LoC > 1,000 → C=3; % Accept 20–35% AND LoC > 1,000 → C=2; % Accept in range with LoC < 1,000 → C=1; otherwise → C=0

### R (ROI) — Universal (using actual Req Eff = LoC ÷ Premium Requests)
- Req Eff > 20 → R=3; Req Eff 10–20 → R=2; Req Eff 5–10 → R=1; Req Eff < 5 → R=0
- **Lean spend** (Prem Req ≤ 500): +1 bonus (cap at 3)
- **Outlier spend** (Prem Req > 1,700): −1 penalty (floor at 0)

### Q (Quality)
- PR Merge Rate ≥80% + Reviews ≥1/PR → Q=3 (if avg time ≤3 days: +1 bonus, cap at 3)
- Q=FB: Feature Branch work (not captured in current PR filter)
- Q=0: Confirmed zero PR activity

---

## CRQC Scorecard

| User | Name | Workflow | C | R | Q | Total | Tier | Momentum |
|---|---|---|---|---|---|---|---|---|
| dhanshree-jagtap-nice | Dhanshree Jagtap | Agent-First | 3 | 3 | FB | TBD | TBD | 🆕 New |
| amol-salunkhe | Amol Salunkhe | Agent-First | 3 | 3 | FB | TBD | TBD | 📈 Rising |
| mshnayderman | Mikhail Shnayderman | Agent-First | 3 | 3 | FB | TBD | TBD | 📈 Rising |
| nice-harshada | Harshada Bagane | Agent-First | 3 | 3 | FB | TBD | TBD | 🆕 New |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | Agent-First | 3 | 2 | FB | TBD | TBD | 🆕 New |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 3 | 0 | FB | TBD | TBD | 📈 Rising |
| mfield1 | Matt Field | Hybrid | 3 | 2 | 3 | **8** | **🌟 A** | 📈 Rising |
| tomotvos | Tom Otvos | Agent-First | 3 | 3 | FB | TBD | TBD | 🆕 New |
| nilesht-19 | Nilesh Tonape | Hybrid | 3 | 0 | FB | TBD | TBD | 📈 Rising |
| copilotshree | Shraddha Kale | Hybrid | 3 | 3 | FB | TBD | TBD | 📈 Rising |
| rpawar-nice | Ritesh Pawar | Agent-First | 2 | 3 | FB | TBD | TBD | 💥 Breakout |
| chris-haun | Chris Haun | Hybrid | 2 | 2 | 3 | **7** | **🌟 A** | 💥 Breakout |
| yogitadhanwate | Yogita Dhanwate | Hybrid | 2 | 1 | FB | TBD | TBD | 🆕 New |
| Kranti-nice | Kranti Kaple | Agent-First | 2 | 0 | FB | TBD | TBD | 🆕 New |
| moadzughul | Moad Alzughul | Agent-First | 2 | 3 | 3 | **8** | **🌟 A** | 📈 Rising |
| Vitthal-Nice | Vitthal Devkar | Inline-First | 3 | 2 | FB | TBD | TBD | 📈 Rising |
| GovindSomaniNice | Govind Somani | Agent-First | 2 | 2 | FB | TBD | TBD | 🆕 New |
| luisalvatierra | Luis Salvatierra | Hybrid | 2 | 0 | 3 | **5** | **👍 B** | 📈 Rising |
| sskalaskar | Sourabh Kalaskar | Hybrid | 2 | 2 | 3 | **7** | **🌟 A** | 📈 Rising |
| AnaSarzosa | Ana Sarzosa | Hybrid | 2 | 3 | FB | TBD | TBD | 🆕 New |
| abhishekhole-nice | Abhishek Hole | Agent-First | 2 | 2 | FB | TBD | TBD | 💥 Breakout |
| sachinfuse-nice | Sachin Fuse | Agent-First | 1 | 2 | FB | TBD | TBD | 🆕 New |
| PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 2 | 0 | FB | TBD | TBD | 📈 Rising |
| Akale23 | Amulya Kale | Inline-First | 1 | 2 | FB | TBD | TBD | 🟡 Stable |
| jkumbhar | Jyoti Kumbhar | Hybrid | 1 | 1 | FB | TBD | TBD | 🆕 New |
| anjali-sherikar | Anjali Sherikar | Hybrid | 1 | 3 | FB | TBD | TBD | 🆕 New |
| tusharpatil166719 | Tushar Patil | Hybrid | 1 | 1 | FB | TBD | TBD | 💥 Breakout |
| suhas-kakde | Suhas Kakde | Agent-First | 1 | 1 | 3 | **5** | **👍 B** | 📈 Rising |
| meghabiradar05 | Megha Biradar | Hybrid | 1 | 3 | FB | TBD | TBD | 🆕 New |
| jayesh-rai | Jayesh Rai | Agent-First | 0 | 2 | 3 | **5** | **👍 B** | 💥 Breakout |
| prashasti-jain | Prashasti Jain | Hybrid | 1 | 0 | FB | TBD | TBD | 💥 Breakout |
| shreedevi-nice | Shreedevi Patil | Hybrid | 1 | 1 | 3 | **5** | **👍 B** | 💥 Breakout |
| sohanbafna | Sohan Bafna | Hybrid | 0 | 3 | FB | TBD | TBD | 🆕 New |
| dsuraj25 | Suraj Dubey | Agent-First | 0 | 2 | FB | TBD | TBD | 💥 Breakout |
| pdevle | Pratik Devle | Hybrid | 0 | 1 | FB | TBD | TBD | 🟡 Stable |
| trunalgawade | Trunal Gawade | Inline-First | 1 | 1 | FB | TBD | TBD | 📈 Rising |
| pratikpawar12 | Pratik Pawar | Hybrid | 0 | 1 | FB | TBD | TBD | 💥 Breakout |
| smishra-nice | Shridhar Mishra | Inline-First | 1 | 1 | FB | TBD | TBD | 📈 Rising |
| abhijeetk268 | Abhijeet Kolhe | Inline-First | 1 | 1 | FB | TBD | TBD | 💥 Breakout |
| kbajaj-nice | Kaushal Bajaj | Inline-First | 0 | 1 | FB | TBD | TBD | 📈 Rising |
| ShivrajNice | Shivraj Bahirat | Hybrid | 0 | 1 | FB | TBD | TBD | 🆕 New |
| sgite-wfm | Shubham Gite | Inline-First | 0 | 1 | FB | TBD | TBD | 🆕 New |
| mshivarkar | Mohan Shivarkar | Inline-First | 0 | 1 | 3 | **4** | **👌 C** | 📉 Declining |
| thakraln | Nishtha Thakral | Agent-First | 0 | 0 | 0 | **0** | **🔴 E** | 📉 Declining |
| dannycadima | Danny Cadima Molina | Agent-First | 0 | 0 | FB | **0** | **🔴 E** | — |
| SwapnilNice | Swapnil Zade | Agent-First | — | — | — | — | Manager | 📈 Rising |
| ssamal-nice | Susovan Samal | Hybrid | — | — | — | — | Manager | — |
| rwalunj-nice | Rahul Walunj | — | — | — | — | — | Research | — |

**Inactive (no Copilot engagement)**:

| User | Name | Manager | Status |
|---|---|---|---|
| ak-nice-2025 | Anand Krishnaswamy | Yoav Shulman | Inactive — zero data across all columns |
| mohitbaghelnice | Mohit Baghel | Susovan Samal | Inactive — zero data across all columns |
| prashant-shete | Non-CX Engineering Member | Non-CX Engineering | 83 Prem Req consumed, 0 LoC produced — interactions only |
| prinice251 | Priscila Torrico | Victoria Koroleva | Inactive — zero data across all columns |
| rajivranjannice | Non-CX Engineering Member | Non-CX Engineering | Inactive — zero data across all columns |
| ssnikam | Sanket Nikam | Susovan Samal | Inactive — zero data across all columns |

---

## Confirmed CRQC Scores (Full C+R+Q available)

| Name | C | R | Q | Total | Tier | Notes |
|---|---|---|---|---|---|---|
| Matt Field | 3 | 2 | 3 | **8** | 🌟 **A** | Top CRQC score. Hybrid; Req Eff 16.7 (544 prem req) |
| Moad Alzughul | 2 | 3 | 3 | **8** | 🌟 **A** | Lean bonus lifts R: 235 prem req, Req Eff 11.7 → R=3 |
| Chris Haun | 2 | 2 | 3 | **7** | 🌟 **A** | Breakout momentum + PR quality |
| Sourabh Kalaskar | 2 | 2 | 3 | **7** | 🌟 **A** | Lean bonus: 324 prem req, Req Eff 6.3 → R=2 |
| Luis Salvatierra | 2 | 0 | 3 | **5** | 👍 **B** | 546 prem req, Req Eff 4.2 → R=0; PR quality saves tier |
| Suhas Kakde | 1 | 1 | 3 | **5** | 👍 **B** | Lean bonus: 489 prem req, Req Eff 3.4 → R=1 |
| Jayesh Rai | 0 | 2 | 3 | **5** | 👍 **B** | Lean bonus: 138 prem req, Req Eff 6.2 → R=2; PR quality saves from C |
| Shreedevi Patil | 1 | 1 | 3 | **5** | 👍 **B** | Lean bonus: 311 prem req, Req Eff 2.2 → R=1; PR saves from C |
| Mohan Shivarkar | 0 | 1 | 3 | **4** | 👌 **C** | Lean bonus: 69 prem req, Req Eff 0.4 → R=1; PR only saving grace |
| Nishtha Thakral | 0 | 0 | 0 | **0** | 🔴 **E** | Zero across all pillars; 561 prem req consumed with 0 LoC |

### Key Changes vs Prior CRQC Version (SuggEff proxy → actual Req Eff)

| Name | Old R (SuggEff proxy) | New R (actual Req Eff) | Change | Reason |
|---|---|---|---|---|
| Moad Alzughul | 2 | 3 | +1 | Lean bonus applied (235 prem req) |
| Sourabh Kalaskar | 3 | 2 | −1 | Actual Req Eff 6.3 (not SuggEff 28.56) |
| Jayesh Rai | 1 | 2 | +1 | Lean bonus applied (138 prem req); total 4→5, C→B |
| Shreedevi Patil | 3 | 1 | −2 | Actual Req Eff 2.2 (not SuggEff 36.32); total 7→5, A→B |
| nice-harshada | 2 | 3 | +1 | Lean bonus applied (470 prem req), actual Req Eff 37.5 |
| Prathmesh Ranadive | 2 | 0 | −2 | 2,235 prem req (outlier penalty applied) |
| Nilesh Tonape | 3 | 0 | −3 | 3,038 prem req (outlier penalty); highest consumer in team |
| Kranti Kaple | 2 | 0 | −2 | 2,097 prem req (outlier penalty) |
| Vyankatesh Khadakkar | 3 | 1 | −2 | Actual Req Eff 7.1 (not SuggEff 44.25) |
| Pradnyesh Salunke | 2 | 0 | −2 | 2,238 prem req (outlier penalty) |
| Anjali Sherikar | 1 | 3 | +2 | Lean bonus: 162 prem req, actual Req Eff 10.4 → R=3 |
| Shraddha Kale | 2 | 3 | +1 | Lean bonus: 340 prem req, Req Eff 14.8 → R=3 |
| Ana Sarzosa | 1 | 3 | +2 | Lean bonus: 97 prem req, actual Req Eff 20.8 → R=3 |
| Megha Biradar | 2 | 3 | +1 | Lean bonus: 82 prem req, actual Req Eff 16.9 → R=3 |
| Jyoti Kumbhar | 3 | 1 | −2 | Actual Req Eff 3.8 (not SuggEff 21.80) |
| Prashasti Jain | 3 | 0 | −3 | Actual Req Eff 1.0 (not SuggEff 27.90) |
| Mohan Shivarkar | 0 | 1 | +1 | Lean bonus applied (69 prem req); total 3→4 |
| Trunal Gawade | 0 | 1 | +1 | Lean bonus applied (93 prem req) |
| Pratik Pawar | 0 | 1 | +1 | Lean bonus applied (339 prem req) |
| Kaushal Bajaj | 0 | 1 | +1 | Lean bonus applied (6 prem req) |

---

## Users Awaiting Full Q Score (Q=FB)

These users work on feature branches. Q score pending a fresh PR Details pull with "Branch = All" filter for May 2026:

| Name | C | R | C+R Subtotal | Max Possible Total | Estimated Tier Range |
|---|---|---|---|---|---|
| Dhanshree Jagtap | 3 | 3 | 6 | 9 | A (locked — C+R=6 already Tier B minimum) |
| Amol Salunkhe | 3 | 3 | 6 | 9 | A |
| Mikhail Shnayderman | 3 | 3 | 6 | 9 | A |
| Harshada Bagane | 3 | 3 | 6 | 9 | A |
| Tom Otvos | 3 | 3 | 6 | 9 | A |
| Shraddha Kale | 3 | 3 | 6 | 9 | A |
| Ritesh Pawar | 2 | 3 | 5 | 8 | A or B |
| Ana Sarzosa | 2 | 3 | 5 | 8 | A or B |
| Rizeq Abu Madeghem | 3 | 2 | 5 | 8 | A or B |
| Vitthal Devkar | 3 | 2 | 5 | 8 | A or B |
| Govind Somani | 2 | 2 | 4 | 7 | B or A |
| Abhishek Hole | 2 | 2 | 4 | 7 | B or A |
| Sachin Fuse | 1 | 2 | 3 | 6 | B |
| Yogita Dhanwate | 2 | 1 | 3 | 6 | B |
| Vyankatesh Khadakkar | 3 | 1 | 4 | 7 | B or A |
| Amulya Kale | 1 | 2 | 3 | 6 | B |
| Anjali Sherikar | 1 | 3 | 4 | 7 | B or A |
| Megha Biradar | 1 | 3 | 4 | 7 | B or A |
| Nilesh Tonape | 3 | 0 | 3 | 6 | B |
| Pradnyesh Salunke | 2 | 0 | 2 | 5 | B or C |
| Jyoti Kumbhar | 1 | 1 | 2 | 5 | B or C |
| Tushar Patil | 1 | 1 | 2 | 5 | B or C |
| Sohan Bafna | 0 | 3 | 3 | 6 | B |
| Suraj Dubey | 0 | 2 | 2 | 5 | B or C |
| Prashasti Jain | 1 | 0 | 1 | 4 | C or B |
| Kranti Kaple | 2 | 0 | 2 | 5 | B or C |
| Prathmesh Ranadive | 3 | 0 | 3 | 6 | B |

---

## Override Rules Applied

| Rule | Applied To |
|---|---|
| Q=0 → Cannot be Tier A | Nishtha Thakral (stays E) |
| Outlier spend (Prem Req >1,700) → −1 R penalty | Nilesh Tonape (3,038), Pradnyesh Salunke (2,238), Prathmesh Ranadive (2,235), Kranti Kaple (2,097) |
| Lean spend (Prem Req ≤500) → +1 R bonus | 34 users — most of the team is lean spenders |
| Momentum >+100% → eligible for one-tier promotion | Ritesh Pawar, Chris Haun, Abhishek Hole (B→A eligible); Tushar Patil (C→B eligible); Jayesh Rai, Prashasti Jain, Shreedevi Patil, Suraj Dubey, Pratik Pawar, Abhijeet Kolhe (D→C eligible) |
| Research role → excluded from tier | Rahul Walunj (rwalunj-nice) — 1,016.90 premium requests consumed, 0 LoC |
| Manager → excluded from tier | Swapnil Zade (1,422.65 prem req), Susovan Samal (50.33 prem req) |

---

## Context Pillar — Diagnostic Notes

| User | Observation | Interpretation |
|---|---|---|
| nilesht-19 | 3,038 Prem Req, 5,065 LoC, Req Eff 1.7 | Highest premium consumer in team; only 1.7 LoC per premium request. Outlier spend penalty applied. Needs agent session discipline |
| Prathmesh-Ranadive | 2,235 Prem Req, 9,489 LoC, 79.9% accept | 2nd highest consumer; excellent output but premium cost is high. Inline-First pattern consuming agent quota |
| PradnyeshSalunke | 2,238 Prem Req, 1,948 LoC, Req Eff 0.9 | High premium spend with low output — worst Req Eff among active users. Outlier penalty applied |
| Kranti-nice | 2,097 Prem Req, 7,076 LoC, Req Eff 3.4 | 4th highest consumer; output is solid but premium cost is very high |
| Mohan Shivarkar | 69 Int, 28 LoC, 60% accept, Req Eff 0.4 | Accepting micro-suggestions (1-line). Needs agent mode for meaningful tasks |
| Nishtha Thakral | 65 Int, 0 LoC, 0% accept, 561 Prem Req | Premium requests consumed but zero code produced. Active AI cost with zero output |
| Trunal Gawade | 100 Int, 302 LoC, 54 Code Accept, 228 CodeGen | High acceptance count but tiny LoC — accepting small completions, not blocks |
| Pratik Pawar | 98 Int, 250 LoC, 2,329 LoC Sugg | 2,329 LoC suggested but only 250 accepted = high rejection rate |
| Chris Haun | 887 Int, 8,592 LoC | Highest interaction count in team; high-frequency Hybrid user. Breakout from 88→8,592 LoC |
| nice-harshada | 927 Int, 17,600 LoC, 1,480 CodeGen | 927 interactions (corrected from 92). Very high session volume. Req Eff 37.5 is excellent |
| Sohan Bafna | 11 Int, 467 LoC, Req Eff 42.5 | Only 11 interactions but excellent Req Eff. High quality, low frequency |
| Sachin Fuse | 273 Int, 2,074 LoC, 1.8% accept | New user not in prior analysis. Agent-First, moderate output |
| Shubham Gite | 25 Int, 271 LoC, 140 Code Accept | 56.7% accept — very high acceptance rate on very few interactions. Inline-First, low volume |
| Shivraj Bahirat | 47 Int, 361 LoC, 2,092 LoC Sugg | Large suggestions (2,092 LoC) but only 361 accepted. Poor fit or exploratory usage |

---

## Action Plan by CRQC Finding

| Finding | Users | Action |
|---|---|---|
| Outlier spend (>1,700 Prem Req) | Nilesh Tonape (3,038), Pradnyesh Salunke (2,238), Prathmesh Ranadive (2,235), Kranti Kaple (2,097) | Coach on prompt efficiency — fewer, better-targeted requests |
| C=0 + R=0 | Nishtha Thakral | Immediate coaching: not accepting any suggestions. 561 prem req wasted |
| Prem Req with 0 LoC | Nishtha Thakral, prashant-shete | Consuming premium budget with zero code output |
| Q=FB (full Q pending) | All feature branch workers (27 users) | Pull PR Details with Branch=All filter for May 2026 to complete scoring |
| High C+R, Q unknown | Amol, Mikhail, Dhanshree, Harshada, Tom Otvos, Shraddha Kale | Pull PR data — C+R=6 locks Tier A regardless of Q |
| Breakout + full CRQC | Moad Alzughul (8/9, A), Jayesh Rai (5/9, B now) | Recognize Moad's consistency. Jayesh Rai promoted C→B from lean bonus |
| New active users | Sachin Fuse, Shivraj Bahirat, Shubham Gite | Onboard to CRQC tracking |
