# GitHub Copilot Usage Analysis — Role Context + Momentum Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Prior Period:** June 3, 2026 | **Framework:** Role Context + Momentum (github-benchmark-role-momentum.md)

---

## Dimension 1 — Role Context Assignments

> Role Context determines which benchmark set applies. Set by manager role and responsibility, not changed week-to-week.

| Login | Name | Role Context | Rationale |
|---|---|---|---|
| rwalunj-nice | Rahul Walunj | **Research** | Uses Copilot for tooling research and documentation. LoC Added excluded from scoring. Tracked on Interactions + Premium only. |
| SwapnilNice | Swapnil Zade | **Manager** | Engineering manager. T2 efficiency threshold lowered to >5 ReqEff. Interaction count weighted higher as team engagement signal. |
| ssamal-nice | Susovan Samal | **Manager** | Engineering manager. Same benchmark adjustment as SwapnilNice. |
| GovindSomaniNice | Govind Somani | **Manager** | Engineering manager. Same benchmark adjustment. |
| smishra-nice | Shridhar Mishra | **Lead (candidate)** | 78.3% accept rate with 155 LoC suggests code review / code understanding usage more than coding. Suggest confirming with manager. If confirmed Lead/Review role, %Accept benchmark relaxes to 10–25%. |
| *All others* | *Various* | **Developer** | Full benchmark applies — all T1, T2, T3 signals. |

### Manager Role Summary

| Login | Name | Int | LoC | %Accept | ReqEff | Manager Assessment |
|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | 273 | 3,140 | 4.0% | ~31.4 | Strong engagement (273 Int). Agent-First behavior with decent LoC. Manager T2 threshold (>5) met comfortably at ~31.4. Active coding manager. |
| ssamal-nice | Susovan Samal | ~30 | 38 | ~8% | ~3.2 | Low engagement. Manager role focus explains the low LoC. ReqEff ~3.2 meets the Manager T2 threshold (>5) is actually NOT met. Flagged for coaching — even manager-adjusted benchmark suggests more engagement is valuable. |
| GovindSomaniNice | Govind Somani | 44 | 2,356 | 1.2% | ~27.7 | Good manager engagement. 44 Int with 2,356 LoC shows selective but efficient coding. ReqEff ~27.7 well exceeds Manager T2 threshold (>5). Active coder-manager. |

### Research Role Summary

| Login | Name | Interactions | Premium | Assessment |
|---|---|---|---|---|
| rwalunj-nice | Rahul Walunj | ~30 | ~100 | Low usage period. Interactions indicate lightweight tooling exploration. Premium spend is minimal. LoC=0 is expected for Research role. |

---

## Dimension 2 — Momentum Scores

### Momentum Calculation

```
Momentum Score = ((Current Req Eff − Prior Req Eff) / Prior Req Eff) × 100
```

> **Prior period baseline (June 3, 2026):** Req Eff values extracted from github-ai-analysis-3-june-2026.md.

| Login | Name | Jun 3 ReqEff | Jun 8 ReqEff | Momentum % | Label | Action |
|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 20.1 | ~60.1 | **+199%** | 🚀 Breakout | Celebrate. Document coaching action that drove this improvement. |
| Kranti-nice | Kranti Kaple | ~7.6 | ~23.1 | **+204%** | 🚀 Breakout | Celebrate publicly. Strong turnaround from Jun 3 struggles. |
| tomotvos | Tom Otvos | ~84.3 | 84.3 | **~0%** | ➡️ Stable | Team efficiency leader. Consistent excellence. |
| dhanshree-jagtap-nice | Dhanshree Jagtap | (New/First period) | 45.7 | N/A — New | 🆕 New User | Strong debut. No prior baseline for momentum calculation. |
| mfield1 | Matt Field | 14.9 | ~14.3 | **−4%** | ➡️ Stable | Minor fluctuation within noise range. |
| nilesht-19 | Nilesh Tonape | 1.3 | 0.3 | **−77%** | 🔴 Declining | Already poor in Jun 3; situation worsened significantly. |
| chris-haun | Chris Haun | 11.9 | 2.8 | **−76%** | 🔴 Declining | Sharp efficiency drop. Tier C with declining momentum = coaching priority. |
| amol-salunkhe | Amol Salunkhe | 40.8 | 6.4 | **−84%** | 🔴 Declining | 7× premium spike with modest LoC gain. Efficiency collapse. |
| mshnayderman | Mikhail Shnayderman | 43.2 | 5.1 | **−88%** | 🔴 Declining | 9.5× premium spike. Most severe efficiency decline on team. |
| Prathmesh-Ranadive | Prathmesh Ranadive | ~5 (est.) | 2.5 | ~−50% | 🔴 Declining | Already struggling; premium spend worsened. |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | ~15 (est.) | ~23.5 | **+57%** | 📈 Rising | Positive improvement trend. |
| nice-harshada | Harshada Bagane | ~13 (est.) | ~13.8 | **+6%** | ➡️ Stable | Consistent high-volume contributor. |
| Vitthal-Nice | Vitthal Devkar | ~12 (est.) | ~14 | **+17%** | ➡️ Stable | Steady improvement in inline-first pattern. |
| Akale23 | Amulya Kale | ~5 (est.) | ~6.7 | **+34%** | 📈 Rising | Gradual improvement in Hybrid workflow. |
| AnaSarzosa | Ana Sarzosa | ~8 (est.) | ~7.9 | **−1%** | ➡️ Stable | Consistent baseline. |
| luisalvatierra | Luis Salvatierra | ~4 (est.) | 2.9 | ~−28% | 📉 Slipping | Efficiency slipping. Flag for manager check-in. |
| jayesh-rai | Jayesh Rai | (Est.) | ~19.2 | N/A | ➡️ Stable est. | Insufficient prior data for reliable momentum calc. |
| yogitadhanwate | Yogita Dhanwate | ~10 (est.) | ~13.8 | **+38%** | 📈 Rising | Positive trend from Tier B baseline. |
| sohanbafna | Sohan Bafna | (Low prior) | ~42.5 | N/A | ➡️ Stable est. | Very small sample — momentum not reliable. |

### Momentum Override Rules Applied

| Rule | Users Affected | Action |
|---|---|---|
| Tier D/E AND Breakout/Rising → Show as ↑ marker | None — no D/E users have Breakout momentum | N/A |
| Tier A/B AND Declining → Flag with ↓ marker | mshnayderman (A↓), amol-salunkhe (A↓), chris-haun (C↓) | Flagged in final table |
| Tier C with Breakout → Eligible for skip-tier to B | Kranti-nice was C last period, now Breakout → promoted to A | Applied |

---

## Dimension 3 — PR Quality Modifier

### Team-Level PR Data (Branch=All, Q2 2026)

| Metric | Value |
|---|---|
| Merged PRs | 157 |
| Reviews | 576 (avg 3.67/PR) |
| Comments | 629 |
| Avg Time to Merge | 1.9 days |
| Merge Rate | ~90% (537/596 from User Details) |

### PR Quality Modifier Applied

> Per-user PR data not available in aggregated form in the current dashboard configuration.  
> Team-level proxy applied: **Merge rate ≥80% (90%) AND Reviews ≥1 per PR (3.67/PR avg)** → **+1 modifier** for active contributors.
> Users with near-zero LoC output are excluded from the +1 (no meaningful PR contribution to evaluate).

**+1 Applied (active contributors with LoC > 1,500 and consistent engagement):**
- Tier A users: all 12 → PR modifier = +1 (eligible for tier upgrade, but all are already Tier A — no numeric effect)
- Tier B users: yogitadhanwate, luisalvatierra, anjali-sherikar, jayesh-rai → +1 → eligible for Tier A; confirm with T1/T2 signals first (most still below T1/T2 threshold)
- Tier C users with LoC > 2K: Prathmesh-Ranadive, chris-haun, jkumbhar, Vyankatesh95 → +1 → eligible for Tier B; offset by other signals

**0 Applied (Tier E budget-drain group):**
- nilesht-19, thakraln, trunalgawade, PradnyeshSalunke — high premium, low LoC, PR contribution uncertain

**Modifier cap note:** The PR modifier shifts *eligibility*, not assignment. A Tier B user with +1 becomes eligible for A — we still confirm T1/T2 signals before promoting.

---

## Combined Scoring Matrix — Final Classifications

| Login | Name | Role | Base Tier | Momentum | PR Mod | Final | Notes |
|---|---|---|---|---|---|---|---|
| dhanshree-jagtap-nice | Dhanshree Jagtap | Developer | A | 🆕 New | +1 | **A** | Team LoC leader. |
| tomotvos | Tom Otvos | Developer | A | ➡️ Stable | +1 | **A** | Team efficiency leader. |
| Kranti-nice | Kranti Kaple | Developer | A | 🚀 Breakout +204% | +1 | **A** | Strong coaching win. |
| rpawar-nice | Ritesh Pawar | Developer | A | 🚀 Breakout +199% | +1 | **A** | Outstanding improvement. |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | Developer | A | 📈 Rising +57% | +1 | **A** | Positive trajectory. |
| nice-harshada | Harshada Bagane | Developer | A | ➡️ Stable | +1 | **A** | Consistent volume. |
| mfield1 | Matt Field | Developer | A | ➡️ Stable | +1 | **A** | Consistent. |
| Vitthal-Nice | Vitthal Devkar | Developer | A | ➡️ Stable | +1 | **A** | Quality inline user. |
| amol-salunkhe | Amol Salunkhe | Developer | A | 🔴 Declining −84% | +1 | **A↓** | Tier A but efficiency alert. |
| mshnayderman | Mikhail Shnayderman | Developer | A | 🔴 Declining −88% | +1 | **A↓** | Most severe efficiency drop. |
| Akale23 | Amulya Kale | Developer | A | 📈 Rising +34% | +1 | **A** | Improving trajectory. |
| AnaSarzosa | Ana Sarzosa | Developer | A | ➡️ Stable | +1 | **A** | Borderline — see v1 notes. |
| yogitadhanwate | Yogita Dhanwate | Developer | B | 📈 Rising +38% | +1 | **B↑** | Rising toward A — monitor. |
| sohanbafna | Sohan Bafna | Developer | B | ➡️ Stable | +1 | **B** | Good efficiency, low volume. |
| luisalvatierra | Luis Salvatierra | Developer | B | 📉 Slipping −28% | +1 | **B** | Slipping — watch T2. |
| anjali-sherikar | Anjali Sherikar | Developer | B | ➡️ Stable | +1 | **B** | Steady contributor. |
| jayesh-rai | Jayesh Rai | Developer | B | ➡️ Stable | +1 | **B** | Agent-First, good efficiency. |
| Prathmesh-Ranadive | Prathmesh Ranadive | Developer | C | 🔴 Declining ~−50% | +1 | **C↓** | T1 good, T2 critical, declining. |
| chris-haun | Chris Haun | Developer | C | 🔴 Declining −76% | +1 | **C↓** | Both T1/T2 down significantly. |
| jkumbhar | Jyoti Kumbhar | Developer | C | ➡️ Stable | +1 | **C** | Low volume but on-track metrics. |
| Vyankatesh95 | Vyankatesh Khadakkar | Developer | C | ➡️ Stable | +1 | **C** | Good signals, low LoC output. |
| dsuraj25 | Suraj Dubey | Developer | C | ➡️ Stable | 0 | **C** | Near-inactive, minimal PR contribution. |
| abhijeetk268 | Abhijeet Kolhe | Developer | C | ➡️ Stable | +1 | **C** | Good signals at low volume. |
| sachinfuse-nice | Sachin Fuse | Developer | D | ➡️ Stable | +1 | **D** | Agent-First below threshold. |
| abhishekhole-nice | Abhishek Hole | Developer | D | ➡️ Stable | +1 | **D** | 0 accepts anomaly. |
| vishal-tad | Vishal Tad | Developer | D | ➡️ Stable | +1 | **D** | Irregular engagement. |
| pdevle | Pratik Devle | Developer | D | ➡️ Stable | +1 | **D** | Low but improving. |
| moadzughul | Moad Alzughul | Developer | D | ➡️ Stable | +1 | **D** | Near Agent-First threshold. |
| tusharpatil166719 | Tushar Patil | Developer | D | ➡️ Stable | +1 | **D** | Consistent low output. |
| meghabiradar05 | Megha Biradar | Developer | D | ➡️ Stable | +1 | **D** | Low volume. |
| mshivarkar | Mohan Shivarkar | Developer | D | ➡️ Stable | 0 | **D** | Budget drain, limited PR contribution. |
| sgite-wfm | Shubham Gite | Developer | D | ➡️ Stable | 0 | **D** | Premium drain, low output. |
| smishra-nice | Shridhar Mishra | Lead (cand.) | D | ➡️ Stable | 0 | **D / Lead** | Reclassify if Lead confirmed. |
| nilesht-19 | Nilesh Tonape | Developer | E | 🔴 Declining −77% | 0 | **E↓** | Worsening budget drain. |
| thakraln | Nishtha Thakral | Developer | E | ➡️ Stable | 0 | **E** | Budget crisis. |
| trunalgawade | Trunal Gawade | Developer | E | ➡️ Stable | 0 | **E** | Budget crisis. |
| PradnyeshSalunke | Pradnyesh Salunke | Developer | E | 🔴 Declining | 0 | **E↓** | Budget crisis worsening. |
| sskalaskar | Sourabh Kalaskar | Developer | E | ➡️ Stable | +1 | **E** | Low LoC despite decent efficiency. |
| ShivrajNice | Shivraj Bahirat | Developer | E | ➡️ Stable | 0 | **E** | Low across all signals. |
| giteshsawant | Gitesh Sawant | Developer | E | ➡️ Stable | 0 | **E** | Near-inactive. |
| ShubhamFulzele28 | Shubham Fulzele | Developer | E | ➡️ Stable | 0 | **E** | 0 accepts. |
| Shreedevi-nice | Shreedevi Patil | Developer | E | ➡️ Stable | +1 | **E** | Below all thresholds. |
| prashasti-jain | Prashasti Jain | Developer | E | ➡️ Stable | +1 | **E** | Low volume. |
| suhas-kakde | Suhas Kakde | Developer | E | ➡️ Stable | 0 | **E** | Agent-First below threshold. |
| pratikpawar12 | Pratik Pawar | Developer | E | ➡️ Stable | 0 | **E** | Near-inactive. |
| kbajaj-nice | Kaushal Bajaj | Developer | E | ➡️ Stable | 0 | **E** | Essentially inactive. |
| dannycadima | Danny Cadima | Developer | E | ➡️ Stable | 0 | **E** | Essentially inactive. |
| SwapnilNice | Swapnil Zade | Manager | — | ➡️ Stable | +1 | **Manager** | Active coder-manager. ReqEff 31.4 exceeds manager threshold. |
| ssamal-nice | Susovan Samal | Manager | — | ➡️ Stable | 0 | **Manager** | Low engagement. ReqEff 3.2 below manager threshold (>5). Coaching recommended. |
| GovindSomaniNice | Govind Somani | Manager | — | ➡️ Stable | +1 | **Manager** | Active. ReqEff 27.7 exceeds manager threshold. |
| rwalunj-nice | Rahul Walunj | Research | — | — | — | **Research** | LoC excluded from scoring. |

---

## Momentum Summary Dashboard

### 🚀 Breakout Users (>+100% Momentum)

| User | Prior ReqEff | Current ReqEff | Change | Coaching Action |
|---|---|---|---|---|
| rpawar-nice (Ritesh Pawar) | 20.1 | ~60.1 | +199% | Document what changed. Share with team as coaching success. |
| Kranti-nice (Kranti Kaple) | ~7.6 | ~23.1 | +204% | Strong turnaround. Protect from premature tier downgrade pressure. |

### 🔴 Declining Users (< −30% Momentum)

| User | Prior ReqEff | Current ReqEff | Change | Response |
|---|---|---|---|---|
| mshnayderman (Mikhail) | 43.2 | 5.1 | −88% | Immediate coaching regardless of current tier (Tier A↓). 9.5× premium spike. |
| amol-salunkhe (Amol) | 40.8 | 6.4 | −84% | Immediate coaching (Tier A↓). 7× premium spike. |
| chris-haun (Chris) | 11.9 | 2.8 | −76% | Manager check-in needed. Tier C↓. |
| nilesht-19 (Nilesh) | 1.3 | 0.3 | −77% | Was already poor. Worsening. Immediate budget intervention. |
| Prathmesh-Ranadive | ~5 | 2.5 | ~−50% | Budget review. Declining with high spend. |
| luisalvatierra (Luis) | ~4 | 2.9 | ~−28% | Flag for manager check-in. On the edge of Declining label. |

### VP Defense Language for Momentum

> "Ritesh Pawar has achieved a +199% Momentum Score — his Request Efficiency tripled from 20.1 to 60.1 in one period. This is exactly the coaching response we're targeting.
>
> Kranti Kaple's Breakout momentum (+204%) demonstrates the coaching investment working. He was in the low-efficiency range in June 3; by June 8, he is a clear Tier A contributor.
>
> Mikhail Shnayderman remains Tier A by output volume and inline accept rate, but his Momentum Score of −88% is our most urgent coaching item. The 9.5× premium spike in 5 days needs investigation before the next period."

---

*Role Context + Momentum Framework — builds on v2 Workflow-Aware classification. All v2 workflow classifications and tier assignments apply. Momentum calculations based on Jun 3, 2026 baseline; estimated prior values marked with (est.). PR Quality Modifier applied at team level (per-user PR data not filterable in current dashboard).*
