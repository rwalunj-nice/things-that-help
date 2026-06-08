# GitHub Copilot Usage Analysis — Role Context + Momentum Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Scope:** 45 users (15 excluded per ignore list) | **Prior Period:** June 3, 2026

---

## Dimension 1 — Role Context Assignments

| Login | Name | Role Context | Rationale |
|---|---|---|---|
| rwalunj-nice | Rahul Walunj | **Research** | Tooling/documentation usage. LoC not applicable. Tracked on Interactions + Premium. |
| SwapnilNice | Swapnil Zade | **Manager** | T2 threshold lowered to >5 ReqEff. Interaction count weighted higher. |
| ssamal-nice | Susovan Samal | **Manager** | Same adjustment as SwapnilNice. |
| smishra-nice | Shridhar Mishra | **Lead (candidate)** | 78.3% accept with 155 LoC = code-review/understanding usage. Confirm with manager. |
| *All others (37)* | *Various* | **Developer** | Full benchmark applies. |

> **Note:** GovindSomaniNice (Govind Somani) is on the ignore list — removed from analysis.

### Manager Summary (In-Scope)

| Login | Name | Int | LoC | %Accept | ReqEff | Assessment |
|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | 273 | 3,140 | 4.0% | ~31.4 | Active coder-manager. ReqEff ~31.4 well exceeds Manager T2 threshold (>5). |
| ssamal-nice | Susovan Samal | ~30 | 38 | ~8% | ~3.2 | Low engagement. ReqEff ~3.2 does NOT meet manager threshold (>5). Coaching recommended even at manager role level. |

---

## Dimension 2 — Momentum Scores

> Momentum = ((Current ReqEff − Prior ReqEff) / Prior ReqEff) × 100
> Prior period: June 3, 2026

| Login | Name | Jun 3 ReqEff | Jun 8 ReqEff | Momentum % | Label | Action |
|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 20.1 | ~60.1 | **+199%** | 🚀 Breakout | Celebrate. New efficiency benchmark for in-scope team. |
| Kranti-nice | Kranti Kaple | ~7.6 | ~23.1 | **+204%** | 🚀 Breakout | Celebrate. Protect from tier downgrade pressure. |
| mshnayderman | Mikhail Shnayderman | 43.2 | 5.1 | **−88%** | 🔴 Declining | Immediate coaching regardless of tier. |
| amol-salunkhe | Amol Salunkhe | 40.8 | 6.4 | **−84%** | 🔴 Declining | Immediate coaching. |
| chris-haun | Chris Haun | 11.9 | 2.8 | **−76%** | 🔴 Declining | Manager check-in needed. |
| nilesht-19 | Nilesh Tonape | 1.3 | 0.3 | **−77%** | 🔴 Declining | Was already critical; worsening. |
| mfield1 | Matt Field | 14.9 | ~14.3 | **−4%** | ➡️ Stable | Minor noise. |
| Akale23 | Amulya Kale | ~5 (est.) | ~6.7 | **+34%** | 📈 Rising | Positive trend. |
| Vitthal-Nice | Vitthal Devkar | ~12 (est.) | ~14 | **+17%** | ➡️ Stable | Steady. |
| luisalvatierra | Luis Salvatierra | ~4 (est.) | 2.9 | **~−28%** | 📉 Slipping | Flag for check-in. |
| Prathmesh-Ranadive | Prathmesh Ranadive | ~5 (est.) | 2.5 | **~−50%** | 🔴 Declining | Budget worsening. |
| jayesh-rai | Jayesh Rai | (est.) | ~19.2 | N/A | ➡️ Stable est. | Limited prior data. |
| abhijeetk268 | Abhijeet Kolhe | (est.) | ~21.9 | N/A | ➡️ Stable est. | Good signals at low volume. |
| Vyankatesh95 | Vyankatesh Khadakkar | (est.) | ~27.8 | N/A | ➡️ Stable est. | Consistent. |

### Momentum Override Rules Applied

| Rule | Users | Action |
|---|---|---|
| Tier A/B AND Declining → flag ↓ | mshnayderman (A↓), amol-salunkhe (A↓), chris-haun (C↓) | Flagged in final table |
| Tier C with Breakout → skip-tier to B | Kranti-nice was C in Jun 3 (low ReqEff ~7.6); now Breakout | Promoted to A — skip-tier applied |
| Tier D/E AND Breakout/Rising → show ↑ | None in Tier D/E with Breakout momentum | N/A |

---

## Dimension 3 — PR Quality Modifier

### Team PR Data (Branch=All, Q2 2026)

| Metric | Value |
|---|---|
| Merged PRs | 157 |
| Avg Reviews/PR | 3.67 |
| Avg Time to Merge | 1.9 days |
| Merge Rate | ~90% |

**PR Modifier:** +1 applied to active contributors (LoC > 1,000, consistent engagement). Conditions met: 90% merge rate AND 3.67 reviews/PR avg.
- All Tier A–C users with LoC > 1,000 → **+1 (eligible for tier upgrade)**
- Budget crisis + near-inactive users → **0** (no PR contribution to evaluate)

---

## Combined Scoring Matrix — Final Classifications (37 Developers)

| Login | Name | Role | Base Tier | Momentum | PR Mod | Final |
|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | Developer | A | 🔴 −84% | +1 | **A↓** |
| Kranti-nice | Kranti Kaple | Developer | A | 🚀 +204% | +1 | **A** |
| mshnayderman | Mikhail Shnayderman | Developer | A | 🔴 −88% | +1 | **A↓** |
| mfield1 | Matt Field | Developer | A | ➡️ Stable | +1 | **A** |
| rpawar-nice | Ritesh Pawar | Developer | A | 🚀 +199% | +1 | **A** |
| Vitthal-Nice | Vitthal Devkar | Developer | A | ➡️ Stable | +1 | **A** |
| Akale23 | Amulya Kale | Developer | A | 📈 +34% | +1 | **A** |
| luisalvatierra | Luis Salvatierra | Developer | B | 📉 −28% | +1 | **B** |
| jayesh-rai | Jayesh Rai | Developer | B | ➡️ Stable | +1 | **B** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Developer | C | 🔴 −50% | +1 | **C↓** |
| chris-haun | Chris Haun | Developer | C | 🔴 −76% | +1 | **C↓** |
| jkumbhar | Jyoti Kumbhar | Developer | C | ➡️ Stable | +1 | **C** |
| Vyankatesh95 | Vyankatesh Khadakkar | Developer | C | ➡️ Stable | +1 | **C** |
| dsuraj25 | Suraj Dubey | Developer | C | ➡️ Stable | 0 | **C** |
| abhijeetk268 | Abhijeet Kolhe | Developer | C | ➡️ Stable | +1 | **C** |
| abhishekhole-nice | Abhishek Hole | Developer | D | ➡️ Stable | +1 | **D** |
| vishal-tad | Vishal Tad | Developer | D | ➡️ Stable | +1 | **D** |
| moadzughul | Moad Alzughul | Developer | D | ➡️ Stable | +1 | **D** |
| tusharpatil166719 | Tushar Patil | Developer | D | ➡️ Stable | +1 | **D** |
| meghabiradar05 | Megha Biradar | Developer | D | ➡️ Stable | +1 | **D** |
| mshivarkar | Mohan Shivarkar | Developer | D | ➡️ Stable | 0 | **D** |
| sgite-wfm | Shubham Gite | Developer | D | ➡️ Stable | 0 | **D** |
| smishra-nice | Shridhar Mishra | Lead (cand.) | D | ➡️ Stable | 0 | **D / Lead** |
| pdevle | Pratik Devle | Developer | D | ➡️ Stable | +1 | **D** |
| nilesht-19 | Nilesh Tonape | Developer | E | 🔴 −77% | 0 | **E↓** |
| thakraln | Nishtha Thakral | Developer | E | ➡️ Stable | 0 | **E** |
| trunalgawade | Trunal Gawade | Developer | E | ➡️ Stable | 0 | **E** |
| PradnyeshSalunke | Pradnyesh Salunke | Developer | E | 🔴 Declining | 0 | **E↓** |
| sskalaskar | Sourabh Kalaskar | Developer | E | ➡️ Stable | +1 | **E** |
| giteshsawant | Gitesh Sawant | Developer | E | ➡️ Stable | 0 | **E** |
| ShubhamFulzele28 | Shubham Fulzele | Developer | E | ➡️ Stable | 0 | **E** |
| Shreedevi-nice | Shreedevi Patil | Developer | E | ➡️ Stable | +1 | **E** |
| prashasti-jain | Prashasti Jain | Developer | E | ➡️ Stable | +1 | **E** |
| suhas-kakde | Suhas Kakde | Developer | E | ➡️ Stable | 0 | **E** |
| pratikpawar12 | Pratik Pawar | Developer | E | ➡️ Stable | 0 | **E** |
| kbajaj-nice | Kaushal Bajaj | Developer | E | ➡️ Stable | 0 | **E** |
| dannycadima | Danny Cadima | Developer | E | ➡️ Stable | 0 | **E** |
| SwapnilNice | Swapnil Zade | Manager | — | ➡️ Stable | +1 | **Manager** |
| ssamal-nice | Susovan Samal | Manager | — | ➡️ Stable | 0 | **Manager** ⚠️ |
| rwalunj-nice | Rahul Walunj | Research | — | — | — | **Research** |

---

## Momentum Summary

### 🚀 Breakout (>+100%)

| User | Jun 3 | Jun 8 | Change | Coaching Action |
|---|---|---|---|---|
| rpawar-nice (Ritesh Pawar) | 20.1 | ~60.1 | +199% | **New in-scope efficiency benchmark.** Document what drove this. |
| Kranti-nice (Kranti Kaple) | ~7.6 | ~23.1 | +204% | **Best coaching story this period.** Protect from downgrade pressure. |

### 🔴 Declining (<−30%)

| User | Jun 3 | Jun 8 | Change | Response |
|---|---|---|---|---|
| mshnayderman | 43.2 | 5.1 | −88% | Immediate coaching. Was the team efficiency leader (Jun 3). 9.5× premium spike unexplained. |
| amol-salunkhe | 40.8 | 6.4 | −84% | Immediate coaching. Was #2 in efficiency (Jun 3). 7× premium spike. In-scope LoC leader now. |
| chris-haun | 11.9 | 2.8 | −76% | Manager check-in. Both T1 and T2 declining. |
| nilesht-19 | 1.3 | 0.3 | −77% | Was already at bottom. Budget drain worsening. |
| Prathmesh-Ranadive | ~5 | 2.5 | ~−50% | Budget intervention required. |

### VP Defense Language

> "In this analysis period — covering 45 in-scope users after 15 users were permanently excluded — our two standout coaching wins are Ritesh Pawar (+199% efficiency, Breakout) and Kranti Kaple (+204%, Breakout from near-inactive in June 3).
>
> The immediate concern is Mikhail Shnayderman and Amol Salunkhe: both were in the top 3 for efficiency on June 3, and both have declined 84-88% in five days with 7-9× premium spikes. These are not organic usage changes — they require investigation.
>
> The persistent budget crisis group (Nilesh Tonape 23,108 premium, Nishtha Thakral 11,112, Trunal Gawade 10,863, Prathmesh Ranadive 10,733, Pradnyesh Salunke 9,892) together consume over 65,000 premium requests generating less than 40,000 lines of code. This is our primary cost optimization target."

---

*Role Context + Momentum — 15 users excluded per `githun-ignored-users.md`. Momentum baseline from github-ai-analysis-3-june-2026.md. PR modifier applied at team level (per-user PR data not available). Estimated prior values marked (est.).*
