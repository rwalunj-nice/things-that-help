# GitHub Copilot Usage Analysis — May 18, 2026 (CRQC Framework)

> **Framework**: CRQC — Core (C) + ROI (R) + Quality (Q) + Context (diagnostic)  
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM  
> **Analysis Date**: May 18, 2026 | **Data Synced**: May 17, 2026 10:30 PM

---

## CRQC Scoring Overview

| Pillar | Max Score | Source |
|---|---|---|
| **C — Core** | 0–3 | AI Usage tab: LoC Added, % Accept, Suggestion Efficiency (by Workflow Type) |
| **R — ROI** | 0–3 (+1 bonus, −1 penalty) | AI Usage tab: Suggestion Efficiency as Req Eff proxy (Premium Requests unavailable) |
| **Q — Quality** | 0–3 | PR Details tab: Merge Rate, Reviews/PR, Time to Merge |
| **Context** | Diagnostic | Interactions, Code Gen patterns — explains C/R anomalies |

> **Premium Requests not available** in current Power BI view. Suggestion Efficiency (LoC Added ÷ Code Generation) used as ROI proxy, consistent with May 11 methodology. Lean/Outlier spend bonuses cannot be applied without Premium data.
>
> **Q scores**: PR data from May 11 session (Q1 2026, WFM Integrations, All branches). Per-user Q scores confirmed for 8 users from that pull. All others: Q=FB (Feature Branch — not captured, not Q=0).

---

## Scoring Key

### C (Core) — by Workflow Type

**Agent-First** (% Accept < 5%, SuggEff > 10):
- LoC > 8,000 → C=3; LoC 3,000–8,000 → C=2; LoC 1,000–3,000 → C=1; LoC < 1,000 → C=0

**Hybrid** (% Accept 5–30%):
- LoC > 5,000 → C=3; LoC 2,000–5,000 → C=2; LoC 500–2,000 → C=1; LoC < 500 → C=0

**Inline-First** (% Accept > 30%):
- % Accept 20–35% AND LoC > 1,000 → C=2; % Accept > 35% with LoC > 1,000 → C=3; % Accept in range with LoC < 1,000 → C=1

### R (ROI) — Universal (using SuggEff proxy)
- SuggEff > 20 → R=3; SuggEff 10–20 → R=2; SuggEff 5–10 → R=1; SuggEff < 5 → R=0

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
| nice-harshada | Harshada Bagane | Agent-First | 3 | 2 | FB | TBD | TBD | 🆕 New |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | Agent-First | 3 | 3 | FB | TBD | TBD | 🆕 New |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 3 | 2 | FB | TBD | TBD | 📈 Rising |
| mfield1 | Matt Field | Hybrid | 3 | 2 | 3 | **8** | **🌟 A** | 📈 Rising |
| tomotvos | Tom Otvos | Agent-First | 3 | 3 | FB | TBD | TBD | 🆕 New |
| rpawar-nice | Ritesh Pawar | Agent-First | 2 | 3 | FB | TBD | TBD | 💥 Breakout |
| chris-haun | Chris Haun | Hybrid | 2 | 2 | 3 | **7** | **🌟 A** | 💥 Breakout |
| yogitadhanwate | Yogita Dhanwate | Hybrid | 2 | 2 | FB | TBD | TBD | 🆕 New |
| Kranti-nice | Kranti Kaple | Agent-First | 2 | 2 | FB | TBD | TBD | 🆕 New |
| nilesht-19 | Nilesh Tonape | Hybrid | 3 | 3 | FB | TBD | TBD | 📈 Rising |
| copilotshree | Shraddha Kale | Hybrid | 3 | 2 | FB | TBD | TBD | 📈 Rising |
| SwapnilNice | Swapnil Zade | Agent-First | — | — | — | — | Manager | 📈 Rising |
| Vyankatesh95 | Vyankatesh Khadakkar | Inline-First | 3 | 3 | FB | TBD | TBD | 📈 Rising |
| moadzughul | Moad Alzughul | Agent-First | 2 | 2 | 3 | **7** | **🌟 A** | 📈 Rising |
| Vitthal-Nice | Vitthal Devkar | Inline-First | 3 | 2 | FB | TBD | TBD | 📈 Rising |
| GovindSomaniNice | Govind Somani | Agent-First | 2 | 3 | FB | TBD | TBD | 🆕 New |
| luisalvatierra | Luis Salvatierra | Hybrid | 2 | 1 | 3 | **6** | **👍 B** | 📈 Rising |
| sskalaskar | Sourabh Kalaskar | Hybrid | 2 | 3 | 3 | **8** | **🌟 A** | 📈 Rising |
| AnaSarzosa | Ana Sarzosa | Hybrid | 2 | 1 | FB | TBD | TBD | 🆕 New |
| abhishekhole-nice | Abhishek Hole | Agent-First | 2 | 3 | FB | TBD | TBD | 💥 Breakout |
| PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 2 | 2 | FB | TBD | TBD | 📈 Rising |
| Akale23 | Amulya Kale | Inline-First | 1 | 1 | FB | TBD | TBD | 🟡 Stable |
| jkumbhar | Jyoti Kumbhar | Hybrid | 1 | 3 | FB | TBD | TBD | 🆕 New |
| anjali-sherikar | Anjali Sherikar | Hybrid | 1 | 1 | FB | TBD | TBD | 🆕 New |
| tusharpatil166719 | Tushar Patil | Hybrid | 1 | 2 | FB | TBD | TBD | 💥 Breakout |
| suhas-kakde | Suhas Kakde | Agent-First | 1 | 1 | 3 | **5** | **👍 B** | 📈 Rising |
| meghabirada05 | Megha Biradar | Hybrid | 1 | 2 | FB | TBD | TBD | 🆕 New |
| jayesh-rai | Jayesh Rai | Agent-First | 0 | 1 | 3 | **4** | **👌 C** | 💥 Breakout |
| prashasti-jain | Prashasti Jain | Hybrid | 1 | 3 | FB | TBD | TBD | 💥 Breakout |
| shreedevi-nice | Shreedevi Patil | Hybrid | 1 | 3 | 3 | **7** | **🌟 A** | 💥 Breakout |
| sohanbafna | Sohan Bafna | Agent-First | 0 | 3 | FB | TBD | TBD | 🆕 New |
| dsuraj25 | Suraj Dubey | Agent-First | 0 | 2 | FB | TBD | TBD | 💥 Breakout |
| pdevle | Pratik Devle | Hybrid | 0 | 1 | FB | TBD | TBD | 🟡 Stable |
| trunalgawade | Trunal Gawade | Inline-First | 1 | 0 | FB | TBD | TBD | 📈 Rising |
| pratikpawar12 | Pratik Pawar | Hybrid | 0 | 0 | FB | TBD | TBD | 💥 Breakout |
| smishra-nice | Shridhar Mishra | Inline-First | 1 | 1 | FB | TBD | TBD | 📈 Rising |
| abhijeetk268 | Abhijeet Kolhe | Inline-First | 1 | 1 | FB | TBD | TBD | 💥 Breakout |
| kbajaj-nice | Kaushal Bajaj | Inline-First | 0 | 0 | FB | TBD | TBD | 📈 Rising |
| mshivarkar | Mohan Shivarkar | Inline-First | 0 | 0 | 3 | **3** | **👌 C** | 📉 Declining |
| thakraln | Nishtha Thakral | Agent-First | 0 | 0 | 0 | **0** | **🔴 E** | 📉 Declining |
| ssamal-nice | Susovan Samal | Hybrid | — | — | — | — | Manager | — |
| dannycadima | Danny Cadima Molina | Agent-First | 0 | 0 | FB | **0** | **🔴 E** | — |

---

## Confirmed CRQC Scores (Full C+R+Q available)

| Name | C | R | Q | Total | Tier | Notes |
|---|---|---|---|---|---|---|
| Matt Field | 3 | 2 | 3 | **8** | 🌟 **A** | Top CRQC score. Hybrid, delivering code AND shipping PRs |
| Moad Alzughul | 2 | 2 | 3 | **7** | 🌟 **A** | Agent-First with confirmed PR quality |
| Chris Haun | 2 | 2 | 3 | **7** | 🌟 **A** | Breakout momentum + PR quality = elite profile |
| Sourabh Kalaskar | 2 | 3 | 3 | **8** | 🌟 **A** | Strong ROI + PR quality |
| Shreedevi Patil | 1 | 3 | 3 | **7** | 🌟 **A** | Breakout momentum elevates her; PR quality confirmed |
| Luis Salvatierra | 2 | 1 | 3 | **6** | 👍 **B** | PR quality saves her from C; volume is the gap |
| Suhas Kakde | 1 | 1 | 3 | **5** | 👍 **B** | PR quality elevates from C |
| Jayesh Rai | 0 | 1 | 3 | **4** | 👌 **C** | PR quality saves from D; core output still weak |
| Mohan Shivarkar | 0 | 0 | 3 | **3** | 👌 **C** | PR quality only saving grace; output = 28 LoC |
| Nishtha Thakral | 0 | 0 | 0 | **0** | 🔴 **E** | Zero across all pillars |

---

## Users Awaiting Full Q Score (Q=FB)

These users work on feature branches. Q score pending a fresh PR Details pull with "Branch = All" filter for May 2026:

| Name | C | R | C+R Subtotal | Max Possible Total | Estimated Tier Range |
|---|---|---|---|---|---|
| Dhanshree Jagtap | 3 | 3 | 6 | 9 | A (locked — C+R=6 already Tier B minimum) |
| Amol Salunkhe | 3 | 3 | 6 | 9 | A |
| Mikhail Shnayderman | 3 | 3 | 6 | 9 | A |
| Rizeq Abu Madeghem | 3 | 3 | 6 | 9 | A |
| Tom Otvos | 3 | 3 | 6 | 9 | A |
| Ritesh Pawar | 2 | 3 | 5 | 8 | A or B |
| Abhishek Hole | 2 | 3 | 5 | 8 | A or B |
| Nilesh Tonape | 3 | 3 | 6 | 9 | A |
| Shraddha Kale | 3 | 2 | 5 | 8 | A or B |
| Vyankatesh | 3 | 3 | 6 | 9 | A |
| Prathmesh Ranadive | 3 | 2 | 5 | 8 | A or B |
| Govind Somani | 2 | 3 | 5 | 8 | A or B |
| Yogita Dhanwate | 2 | 2 | 4 | 7 | B or A |
| Harshada Bagane | 3 | 2 | 5 | 8 | A or B |
| Kranti Kaple | 2 | 2 | 4 | 7 | B or A |
| Vitthal Devkar | 3 | 2 | 5 | 8 | A or B |

---

## Override Rules Applied

| Rule | Applied To |
|---|---|
| Q=0 → Cannot be Tier A | Nishtha Thakral (stays E) |
| Momentum >+100% → eligible for one-tier promotion | Ritesh Pawar, Chris Haun, Abhishek Hole (B→A eligible); Tushar Patil (C→B eligible); Jayesh Rai, Prashasti Jain, Shreedevi Patil, Suraj Dubey, Pratik Pawar, Abhijeet Kolhe (D→C eligible) |
| Research role → excluded from tier | Rahul Walunj (rwalunj) |
| Manager → excluded from tier | Swapnil Zade, Susovan Samal |

---

## Context Pillar — Diagnostic Notes

| User | Observation | Interpretation |
|---|---|---|
| Mohan Shivarkar | 73 Int, 28 LoC, 60% accept, SuggEff 0.93 | Accepting micro-suggestions (1-line completions). Needs to switch to agent mode for meaningful tasks |
| Nishtha Thakral | 65 Int, 0 LoC, 0% accept | Interactions happening but no acceptance at all. May be exploring/reading responses only |
| Trunal Gawade | 100 Int, 302 LoC, 54 Accept, 228 CodeGen | High acceptance count (54) but tiny LoC output — accepting tiny completions, not blocks |
| Pratik Pawar | 98 Int, 250 LoC, 2329 LoCSugg | 2,329 LoC suggested but only 250 accepted = 89% rejection rate. Poor fit between suggestion style and needs |
| Chris Haun | 887 Int, 8,592 LoC | Very high interactions (887) driving output — high-frequency Hybrid user |
| nice-harshada | 92 Int, 17,600 LoC, 1,480 CodeGen | Very high Code Gen count (1,480) with only 92 interactions = heavy automated generation per session |
| Sohan Bafna | 11 Int, 467 LoC, SuggEff 35.92 | Per-session quality excellent but critically low engagement frequency |

---

## Action Plan by CRQC Finding

| Finding | Users | Action |
|---|---|---|
| C=0 + R=0 + Q=confirmed | Mohan Shivarkar, Nishtha Thakral | Immediate coaching: specific agent task assignments |
| C=0 + Breakout momentum | Suraj Dubey, Jayesh Rai | Momentum shows intent — coach on increasing session depth |
| Q=FB (full Q pending) | All feature branch workers | Pull PR Details with Branch=All filter for May 2026 to complete scoring |
| High C+R, Q unknown | Amol, Mikhail, Dhanshree, Rizeq | Pull PR data — these users likely have A-level CRQC if PRs confirm |
| Breakout + full CRQC | Shreedevi Patil (7/9, A) | A-grade outcome — recognize and share as example |
