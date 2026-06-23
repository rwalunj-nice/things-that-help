# GitHub Copilot Usage Analysis — CRQC 4-Pillar Framework
**Product:** WFM Integrations | **Period:** CP9 (Jun 23, 2026) | **Prior CP:** CP8 (Jun 12, 2026)
**PR Data Snapshot:** Jun 21, 2026 | **Q2 Closes:** Jun 30, 2026 (7 days remaining)
**Scope:** 37 developers (15 + 1 excluded per ignore list; 3 special roles tracked separately; 1 research not tiered)

---

## CRQC Scoring Framework

| Pillar | Max | Description |
|---|---|---|
| **C** (Core) | 0–3 | Workflow-specific effectiveness (Agent-First or Inline-First) |
| **R** (ROI) | 0–3 | Request Efficiency + Premium spend efficiency |
| **Q** (Quality) | 0–3 | PR merge rate + reviews per PR + time to merge |
| **Total** | 0–9 | C + R + Q |

**Tier mapping:** A = 7–9 | B = 5–6 | C = 3–4 | D = 1–2 | E = 0

### C Pillar — Workflow-Dependent Scoring

**Workflow classification (2-tier, CP9):**
Since Agent Contribution % is not available, classification uses SuggEff + %Accept patterns:
- **Agent-First:** SuggEff > 20 AND %Accept < 20%
- **Inline-First / Hybrid:** %Accept ≥ 20% (any SuggEff)
- **Agent-First lean:** SuggEff ≤ 20 AND %Accept < 20%

**Agent-First C scoring:** ReqEff > 15 = 2pts | ReqEff 8–15 = 1pt | ReqEff < 8 = 0pts; LoC increasing vs CP8 = +1pt (cap 3)
**Inline-First C scoring:** %Accept 20–35% = 2pts | %Accept 10–19% = 1pt | %Accept > 35% = 1pt (outside target); Code Accept count > 20 = +1pt (cap 3)

### R Pillar — Universal

- ReqEff > 20 → 3pts | 10–20 → 2pts | 5–10 → 1pt | < 5 → 0pts
- Lean spend (Premium ≤ 500): +1 bonus
- Outlier spend (Premium > 1,700): −1 penalty (minimum 0)

### Q Pillar — Per-User PR Data (from Jun 21, 2026 snapshot)

- PR merge rate ≥ 80% = 2pts | 50–79% = 1pt | < 50% = 0pts
- Reviews ≥ 1 per PR = +1pt
- Avg time to merge ≤ 72h = +1 bonus
- Cap Q at 3
- **Q = FB** (Fallback) = active user with zero PR data captured; treated as Q = 2 (conservative active-user proxy)

### Override Rules

1. **Q = 0 → Cannot be Tier A** (no quality evidence)
2. **R = 0 AND Premium > 500 → Cannot exceed Tier C** (budget drain with no efficiency)
3. **Momentum > 100% (LoC vs CP8) → Eligible for one-tier promotion** (applied after base scoring; blocked if override 2 also applies)

---

## Workflow Classification — CP9

### Agent-First (SuggEff > 20, %Accept < 20%)

| Login | Full Name | SuggEff | %Accept | Notes |
|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 31.95 | 1.5% | High-volume agent user |
| Kranti-nice | Kranti Kaple | 47.53 | 4.6% | Very high SuggEff |
| rpawar-nice | Ritesh Pawar | 60.15 | 7.6% | Highest SuggEff in team |
| sskalaskar | Sourabh Kalaskar | 23.77 | 16.9% | Agent-First (SuggEff>20) |
| abhishekhole-nice | Abhishek Hole | 33.16 | 3.2% | Agent-First |
| Shreedevi-nice | Shreedevi Patil | 55.47 | 8.8% | Agent-First |

### Agent-First Lean (SuggEff ≤ 20, %Accept < 20%)

| Login | Full Name | SuggEff | %Accept | Notes |
|---|---|---|---|---|
| chris-haun | Chris Haun | 7.72 | 9.3% | Low SuggEff, low accept |
| mfield1 | Matt Field | 12.12 | 5.8% | Mid SuggEff, low accept |
| copilotshree | (Shreedevi?) | 11.02 | 4.8% | Agent lean |
| PradnyeshSalunke | Pradnyesh Salunke | 8.39 | 19.4% | Just under 20% accept |
| mshivarkar | Mohan Shivarkar | 7.34 | 9.4% | Agent lean |
| vishal-tad | Vishal Tad | 4.19 | 8.8% | Agent lean |
| moadzughul | Moad Alzughul | 9.19 | 2.4% | Agent lean |
| jayesh-rai | Jayesh Rai | 13.49 | 18.4% | Agent lean |
| tusharpatil166719 | Tushar Patil | 11.58 | 14.7% | Agent lean |
| suhas-kakde | Suhas Kakde | 8.39 | 1.7% | Agent lean |
| meghabiradar05 | Megha Biradar | 8.30 | 12.5% | Agent lean |
| prashasti-jain | Prashasti Jain | 6.27 | 7.2% | Agent lean |
| pdevle | Pratik Devle | 13.20 | 6.3% | Agent lean |
| giteshsawant | Gitesh Sawant | 15.38 | 2.2% | Agent lean |
| thakraln | Nishtha Thakral | 8.96 | 0.0% | Agent lean (new entrant CP9) |
| pratikpawar12 | Pratik Pawar | 2.03 | 4.1% | Agent lean (new entrant CP9) |
| mohitbaghelnice | Mohit Baghel | 3.00 | 0.0% | Agent lean (new entrant CP9) |
| kbajaj-nice | Kaushal Bajaj | 0.13 | 17.5% | Agent lean (new entrant CP9) |
| dannycadima | Danny Cadima Molina | 0.14 | 12.7% | Agent lean (new entrant CP9) |
| ssnikam | Sanket Nikam | — | — | No Copilot usage; PR data only |

### Inline-First / Hybrid (%Accept ≥ 20%)

| Login | Full Name | SuggEff | %Accept | Notes |
|---|---|---|---|---|
| Prathmesh-Ranadive | Prathmesh Ranadive | 19.90 | 88.7% | Extremely high accept rate |
| mshnayderman | Mikhail Shnayderman | 60.79 | 27.8% | High SuggEff + high accept |
| luisalvatierra | Luis Salvatierra | 13.33 | 24.2% | Target range |
| nilesht-19 | Nilesh Tonape | 18.34 | 30.2% | Strong accept rate |
| Vyankatesh95 | Vyankatesh Khadakkar | 30.27 | 34.1% | High SuggEff + target accept |
| trunalgawade | Trunal Gawde | 8.40 | 20.4% | Just in target range |
| Vitthal-Nice | Vitthal Devkar | 13.55 | 40.4% | Above 35% target |
| Akale23 | Amulya Kale | 5.41 | 22.8% | Target range |
| jkumbhar | Jyoti Kumbhar | 15.93 | 22.0% | Target range |
| dsuraj25 | Suraj Dubey | 12.57 | 33.3% | Target range (new entrant CP9) |
| abhijeetk268 | Abhijeet Kolhe | 24.30 | 29.6% | High SuggEff + accept |
| amol-doke | Amol Doke | 0.56 | 22.2% | Target range (new entrant CP9) |

---

## Full CRQC Scoring Table — CP9

Columns: Login | Name | Workflow | LoC | %Accept | Prem | ReqEff | **C** | **R** | **Q** | **Total** | Override | **Tier**

### Computation Notes

**C column:** Agent-First = ReqEff bracket + LoC trend bonus. Inline-First = %Accept bracket + Code Accept count bonus.
**R column:** ReqEff bracket + lean/outlier modifier.
**Q column:** PR merge rate + reviews/PR + time-to-merge. FB = active user, no PR data captured (treated as 2 for tier calc).

| Login | Name | Wkflow | LoC | %Accept | Prem | ReqEff | C | R | Q | Total | Override | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dannycadima | Danny Cadima Molina | AF-Lean | 34 | 12.7% | 3 | 11.0 | 2 | 3 | FB(2) | **7** | — | **A** |
| abhijeetk268 | Abhijeet Kolhe | Inline | 656 | 29.6% | 451 | 1.5 | 2 | 1 | 3 | **6** | — | **B** |
| copilotshree | (Shreedevi?) | AF-Lean | 5,013 | 4.8% | 340 | 14.8 | 1 | 3 | FB(2) | **6** | — | **B** |
| kbajaj-nice | Kaushal Bajaj | AF-Lean | 5 | 17.5% | 6 | 0.8 | 1 | 1 | 3 | **5** | — | **B** |
| amol-salunkhe | Amol Salunkhe | AF | 43,585 | 1.5% | 20,170 | 2.2 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| Kranti-nice | Kranti Kaple | AF | 37,978 | 4.6% | 35,537 | 1.1 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline | 35,091 | 88.7% | 31,420 | 1.1 | 2 | 0 | 3 | **5** | R=0+Prem>500→max C | **C** |
| mshnayderman | Mikhail Shnayderman | Inline | 27,539 | 27.8% | 5,452 | 5.1 | 3 | 0 | 2 | **5** | R=0+Prem>500→max C | **C** |
| luisalvatierra | Luis Salvatierra | Inline | 12,080 | 24.2% | 9,542 | 1.3 | 3 | 0 | 3 | **6** | R=0+Prem>500→max C | **C** |
| nilesht-19 | Nilesh Tonape | Inline | 7,354 | 30.2% | 32,332 | 0.2 | 3 | 0 | 3 | **6** | R=0+Prem>500→max C | **C** |
| chris-haun | Chris Haun | AF-Lean | 10,493 | 9.3% | 12,535 | 0.8 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| mfield1 | Matt Field | AF-Lean | 9,803 | 5.8% | 3,133 | 3.1 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| rpawar-nice | Ritesh Pawar | AF | 8,662 | 7.6% | 879 | 9.9 | 1 | 1 | FB(2) | **4** | — | **C** |
| PradnyeshSalunke | Pradnyesh Salunke | AF-Lean | 4,237 | 19.4% | 20,544 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| mshivarkar | Mohan Shivarkar | AF-Lean | 4,201 | 9.4% | 17,029 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| Vyankatesh95 | Vyankatesh Khadakkar | Inline | 4,177 | 34.1% | 4,118 | 1.0 | 3 | 0 | 3 | **6** | R=0+Prem>500→max C | **C** |
| vishal-tad | Vishal Tad | AF-Lean | 3,737 | 8.8% | 9,301 | 0.4 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| sskalaskar | Sourabh Kalaskar | AF | 3,233 | 16.9% | 16,897 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| moadzughul | Moad Alzughul | AF-Lean | 3,409 | 2.4% | 3,072 | 1.1 | 0 | 0 | 3 | **3** | R=0+Prem>500→max C | **C** |
| abhishekhole-nice | Abhishek Hole | AF | 3,150 | 3.2% | 4,416 | 0.7 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| Vitthal-Nice | Vitthal Devkar | Inline | 2,683 | 40.4% | 2,393 | 1.1 | 2 | 0 | 3 | **5** | R=0+Prem>500→max C | **C** |
| jayesh-rai | Jayesh Rai | AF-Lean | 2,712 | 18.4% | 1,997 | 1.4 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| trunalgawade | Trunal Gawde | Inline | 2,352 | 20.4% | 18,720 | 0.1 | 3 | 0 | 3 | **6** | R=0+Prem>500→max C | **C** |
| Akale23 | Amulya Kale | Inline | 2,472 | 22.8% | 4,237 | 0.6 | 3 | 0 | 3 | **6** | R=0+Prem>500→max C | **C** |
| suhas-kakde | Suhas Kakde | AF-Lean | 2,005 | 1.7% | 2,797 | 0.7 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| Shreedevi-nice | Shreedevi Patil | AF | 1,886 | 8.8% | 12,071 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| jkumbhar | Jyoti Kumbhar | Inline | 1,880 | 22.0% | 2,110 | 0.9 | 3 | 0 | 2 | **5** | R=0+Prem>500→max C | **C** |
| meghabiradar05 | Megha Biradar | AF-Lean | 1,727 | 12.5% | 10,131 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| prashasti-jain | Prashasti Jain | AF-Lean | 1,562 | 7.2% | 12,206 | 0.1 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| pdevle | Pratik Devle | AF-Lean | 1,478 | 6.3% | 10,057 | 0.1 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| dsuraj25 | Suraj Dubey | Inline | 1,169 | 33.3% | 9,893 | 0.1 | 3 | 0 | 3 | **6** | R=0+Prem>500→max C | **C** |
| thakraln | Nishtha Thakral | AF-Lean | 806 | 0.0% | 13,562 | 0.1 | 1 | 0 | FB(2) | **3** | R=0+Prem>500→max C | **C** |
| pratikpawar12 | Pratik Pawar | AF-Lean | 250 | 4.1% | 815 | 0.3 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| amol-doke | Amol Doke | Inline | 10 | 22.2% | 2,528 | 0.0 | 2 | 0 | 2 | **4** | R=0+Prem>500→max C | **C** |
| mohitbaghelnice | Mohit Baghel | AF-Lean | 3 | 0.0% | 2,393 | 0.0 | 1 | 0 | 3 | **4** | R=0+Prem>500→max C | **C** |
| ssnikam | Sanket Nikam | (No usage) | 0 | — | 0 | — | 0 | 0 | 3 | **3** | — | **C** |
| giteshsawant | Gitesh Sawant | AF-Lean | 1,369 | 2.2% | 8,585 | 0.2 | 1 | 0 | 1 | **2** | — | **D** |

---

## Detailed Score Derivations

### C Score Derivations

**Agent-First users (ReqEff bracket + LoC trend):**

| Login | ReqEff | Base C | LoC vs CP8 | Trend +1? | Final C |
|---|---|---|---|---|---|
| amol-salunkhe | 2.2 | 0 (< 8) | 43,585 vs 41,008 (+6.3%) | Yes | **1** |
| Kranti-nice | 1.1 | 0 (< 8) | 37,978 vs 31,645 (+20.0%) | Yes | **1** |
| rpawar-nice | 9.9 | 1 (8–15) | 8,662 vs 8,662 (flat) | No | **1** |
| sskalaskar | 0.2 | 0 (< 8) | 3,233 vs 2,698 (+19.8%) | Yes | **1** |
| abhishekhole-nice | 0.7 | 0 (< 8) | 3,150 vs 2,993 (+5.2%) | Yes | **1** |
| Shreedevi-nice | 0.2 | 0 (< 8) | 1,886 vs 1,786 (+5.6%) | Yes | **1** |

**Agent-First Lean users (same rules):**

| Login | ReqEff | Base C | LoC vs CP8 | Trend +1? | Final C |
|---|---|---|---|---|---|
| chris-haun | 0.8 | 0 | 10,493 vs 10,384 (+1.0%) | Yes | **1** |
| mfield1 | 3.1 | 0 | 9,803 vs 9,800 (+0.03%) | Yes (marginal) | **1** |
| copilotshree | 14.8 | 1 (8–15) | 5,013 vs 5,013 (flat) | No | **1** |
| PradnyeshSalunke | 0.2 | 0 | 4,237 vs 3,731 (+13.6%) | Yes | **1** |
| mshivarkar | 0.2 | 0 | 4,201 vs 2,097 (+100.3%) | Yes | **1** |
| vishal-tad | 0.4 | 0 | 3,737 vs 3,520 (+6.2%) | Yes | **1** |
| moadzughul | 1.1 | 0 | 3,409 vs 3,409 (flat) | No | **0** |
| jayesh-rai | 1.4 | 0 | 2,712 vs 2,479 (+9.4%) | Yes | **1** |
| tusharpatil166719 | 0.1 | 0 | 2,200 vs 1,798 (+22.4%) | Yes | **1** |
| suhas-kakde | 0.7 | 0 | 2,005 vs 1,677 (+19.6%) | Yes | **1** |
| meghabiradar05 | 0.2 | 0 | 1,727 vs 1,720 (+0.4%) | Yes | **1** |
| prashasti-jain | 0.1 | 0 | 1,562 vs 1,545 (+1.1%) | Yes | **1** |
| pdevle | 0.1 | 0 | 1,478 vs 1,384 (+6.8%) | Yes | **1** |
| giteshsawant | 0.2 | 0 | 1,369 vs 1,110 (+23.3%) | Yes | **1** |
| thakraln | 0.1 | 0 | 806 vs ~0 (new) | Yes | **1** |
| pratikpawar12 | 0.3 | 0 | 250 vs ~0 (new) | Yes | **1** |
| mohitbaghelnice | 0.0 | 0 | 3 vs ~0 (trivial) | Yes | **1** |
| kbajaj-nice | 0.8 | 0 | 5 vs ~0 (trivial) | Yes | **1** |
| dannycadima | 11.0 | 1 (8–15) | 34 vs ~0 (new) | Yes | **2** |
| ssnikam | — | 0 | 0 vs 0 | No | **0** |

**Inline-First users (%Accept bracket + Code Accept count > 20):**

| Login | %Accept | Base C | Code Accept | >20 +1? | Final C |
|---|---|---|---|---|---|
| Prathmesh-Ranadive | 88.7% (>35%) | 1 | 1,563 | Yes | **2** |
| mshnayderman | 27.8% (20–35%) | 2 | 126 | Yes | **3** |
| luisalvatierra | 24.2% (20–35%) | 2 | 219 | Yes | **3** |
| nilesht-19 | 30.2% (20–35%) | 2 | 121 | Yes | **3** |
| Vyankatesh95 | 34.1% (20–35%) | 2 | 47 | Yes | **3** |
| trunalgawade | 20.4% (20–35%) | 2 | 57 | Yes | **3** |
| Vitthal-Nice | 40.4% (>35%) | 1 | 80 | Yes | **2** |
| Akale23 | 22.8% (20–35%) | 2 | 104 | Yes | **3** |
| jkumbhar | 22.0% (20–35%) | 2 | 26 | Yes | **3** |
| dsuraj25 | 33.3% (20–35%) | 2 | 31 | Yes | **3** |
| abhijeetk268 | 29.6% (20–35%) | 2 | 8 | No (<20) | **2** |
| amol-doke | 22.2% (20–35%) | 2 | 4 | No (<20) | **2** |

### R Score Derivations

| Login | ReqEff | Base R | Premium | Lean ≤500? | Outlier >1,700? | Final R |
|---|---|---|---|---|---|---|
| amol-salunkhe | 2.2 | 0 | 20,170 | No | Yes (−1) | 0 |
| Kranti-nice | 1.1 | 0 | 35,537 | No | Yes (−1) | 0 |
| Prathmesh-Ranadive | 1.1 | 0 | 31,420 | No | Yes (−1) | 0 |
| mshnayderman | 5.1 | 1 | 5,452 | No | Yes (−1) | 0 |
| luisalvatierra | 1.3 | 0 | 9,542 | No | Yes (−1) | 0 |
| chris-haun | 0.8 | 0 | 12,535 | No | Yes (−1) | 0 |
| mfield1 | 3.1 | 0 | 3,133 | No | Yes (−1) | 0 |
| rpawar-nice | 9.9 | 1 (5–10) | 879 | No | No | **1** |
| nilesht-19 | 0.2 | 0 | 32,332 | No | Yes (−1) | 0 |
| copilotshree | 14.8 | 2 (10–20) | 340 | Yes (+1) | No | **3** |
| PradnyeshSalunke | 0.2 | 0 | 20,544 | No | Yes (−1) | 0 |
| mshivarkar | 0.2 | 0 | 17,029 | No | Yes (−1) | 0 |
| Vyankatesh95 | 1.0 | 0 | 4,118 | No | Yes (−1) | 0 |
| vishal-tad | 0.4 | 0 | 9,301 | No | Yes (−1) | 0 |
| moadzughul | 1.1 | 0 | 3,072 | No | Yes (−1) | 0 |
| sskalaskar | 0.2 | 0 | 16,897 | No | Yes (−1) | 0 |
| abhishekhole-nice | 0.7 | 0 | 4,416 | No | Yes (−1) | 0 |
| trunalgawade | 0.1 | 0 | 18,720 | No | Yes (−1) | 0 |
| Vitthal-Nice | 1.1 | 0 | 2,393 | No | Yes (−1) | 0 |
| jayesh-rai | 1.4 | 0 | 1,997 | No | Yes (−1) | 0 |
| tusharpatil166719 | 0.1 | 0 | 35,886 | No | Yes (−1) | 0 |
| Akale23 | 0.6 | 0 | 4,237 | No | Yes (−1) | 0 |
| suhas-kakde | 0.7 | 0 | 2,797 | No | Yes (−1) | 0 |
| Shreedevi-nice | 0.2 | 0 | 12,071 | No | Yes (−1) | 0 |
| jkumbhar | 0.9 | 0 | 2,110 | No | Yes (−1) | 0 |
| meghabiradar05 | 0.2 | 0 | 10,131 | No | Yes (−1) | 0 |
| prashasti-jain | 0.1 | 0 | 12,206 | No | Yes (−1) | 0 |
| pdevle | 0.1 | 0 | 10,057 | No | Yes (−1) | 0 |
| giteshsawant | 0.2 | 0 | 8,585 | No | Yes (−1) | 0 |
| dsuraj25 | 0.1 | 0 | 9,893 | No | Yes (−1) | 0 |
| thakraln | 0.1 | 0 | 13,562 | No | Yes (−1) | 0 |
| abhijeetk268 | 1.5 | 0 | 451 | Yes (+1) | No | **1** |
| pratikpawar12 | 0.3 | 0 | 815 | No | No | 0 |
| amol-doke | 0.0 | 0 | 2,528 | No | Yes (−1) | 0 |
| mohitbaghelnice | 0.0 | 0 | 2,393 | No | Yes (−1) | 0 |
| kbajaj-nice | 0.8 | 0 | 6 | Yes (+1) | No | **1** |
| dannycadima | 11.0 | 2 (10–20) | 3 | Yes (+1) | No | **3** |
| ssnikam | — | 0 | 0 | No | No | 0 |

### Q Score Derivations (Per-User PR Data, Jun 21, 2026)

| Login | PR# | Merged | Merge% | Reviews/PR | Time | MergeRate | Rev+1? | Time+1? | Q |
|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | 8 | 8 | 100% | 4.6 | 2h 48m | 2 | Yes | Yes (≤72h) | **3** |
| Kranti-nice | 22 | 16 | 72.7% | 1.4 | 60h 28m | 1 | Yes | Yes (≤72h) | **3** |
| Prathmesh-Ranadive | 24 | 24 | 100% | 3.0 | 16h 5m | 2 | Yes | Yes (≤72h) | **3** |
| mshnayderman | 2 | 1 | 50% | 11.0 | 91h 9m | 1 | Yes | No (>72h) | **2** |
| luisalvatierra | 12 | 10 | 83.3% | 1.25 | 137h 46m | 2 | Yes | No (>72h) | **3** |
| chris-haun | 47 | 45 | 95.7% | 2.6 | 81h 49m | 2 | Yes | No (>72h) | **3** |
| mfield1 | 33 | 31 | 93.9% | 3.85 | 159h 6m | 2 | Yes | No (>72h) | **3** |
| rpawar-nice | 0 | 0 | FB | — | — | — | — | — | **FB(2)** |
| nilesht-19 | 20 | 18 | 90% | 2.55 | 24h 58m | 2 | Yes | Yes (≤72h) | **3** |
| copilotshree | 0 | 0 | FB | — | — | — | — | — | **FB(2)** |
| PradnyeshSalunke | 8 | 8 | 100% | 5.125 | 129h 35m | 2 | Yes | No (>72h) | **3** |
| mshivarkar | 11 | 11 | 100% | 4.8 | 97h 13m | 2 | Yes | No (>72h) | **3** |
| Vyankatesh95 | 16 | 16 | 100% | 2.75 | 26h 43m | 2 | Yes | Yes (≤72h) | **3** |
| vishal-tad | 17 | 15 | 88.2% | 0.94 | 32h 37m | 2 | No (<1) | Yes (≤72h) | **3** |
| moadzughul | 45 | 43 | 95.6% | 1.47 | 361h 1m | 2 | Yes | No (>72h) | **3** |
| sskalaskar | 15 | 13 | 86.7% | 3.13 | 129h 37m | 2 | Yes | No (>72h) | **3** |
| abhishekhole-nice | 14 | 14 | 100% | 4.0 | 16h 26m | 2 | Yes | Yes (≤72h) | **3** |
| trunalgawade | 1 | 1 | 100% | 14.0 | 47h 30m | 2 | Yes | Yes (≤72h) | **3** |
| Vitthal-Nice | 7 | 7 | 100% | 1.71 | 31h 11m | 2 | Yes | Yes (≤72h) | **3** |
| jayesh-rai | 17 | 17 | 100% | 2.24 | 91h 27m | 2 | Yes | No (>72h) | **3** |
| tusharpatil166719 | 4 | 4 | 100% | 0.25 | 26h 20m | 2 | No (<1) | Yes (≤72h) | **3** |
| Akale23 | 7 | 6 | 85.7% | 2.29 | 29h 26m | 2 | Yes | Yes (≤72h) | **3** |
| suhas-kakde | 29 | 27 | 93.1% | 1.55 | 111h 56m | 2 | Yes | No (>72h) | **3** |
| Shreedevi-nice | 15 | 14 | 93.3% | 1.27 | 24h 23m | 2 | Yes | Yes (≤72h) | **3** |
| jkumbhar | 19 | 12 | 63.2% | 3.95 | 281h 35m | 1 | Yes | No (>72h) | **2** |
| meghabiradar05 | 5 | 5 | 100% | 1.2 | 217h 26m | 2 | Yes | No (>72h) | **3** |
| prashasti-jain | 8 | 7 | 87.5% | 2.375 | 111h 27m | 2 | Yes | No (>72h) | **3** |
| pdevle | 7 | 7 | 100% | 7.0 | 25h 43m | 2 | Yes | Yes (≤72h) | **3** |
| giteshsawant | 1 | 0 | 0% | 0.0 | 19h 34m | 0 | No (<1) | Yes (≤72h) | **1** |
| dsuraj25 | 1 | 1 | 100% | 0.0 | 28h 28m | 2 | No (<1) | Yes (≤72h) | **3** |
| thakraln | 0 | 0 | FB | — | — | — | — | — | **FB(2)** |
| abhijeetk268 | 53 | 49 | 92.5% | 0.87 | 13h 19m | 2 | No (<1) | Yes (≤72h) | **3** |
| pratikpawar12 | 9 | 9 | 100% | 11.4 | 2h 16m | 2 | Yes | Yes (≤72h) | **3** |
| amol-doke | 8 | 4 | 50% | 0.0 | 33h 17m | 1 | No (<1) | Yes (≤72h) | **2** |
| mohitbaghelnice | 1 | 1 | 100% | 1.0 | 0h 2m | 2 | Yes | Yes (≤72h) | **3** |
| kbajaj-nice | 2 | 2 | 100% | 2.5 | 28h 21m | 2 | Yes | Yes (≤72h) | **3** |
| dannycadima | 0 | 0 | FB | — | — | — | — | — | **FB(2)** |
| ssnikam | 55 | 49 | 89.1% | 0.11 | 42h 2m | 2 | No (<1) | Yes (≤72h) | **3** |

---

## Override Cases — Explicit Documentation

### Override 2: R=0 AND Premium > 500 → Cannot Exceed Tier C

This override affects 32 out of 37 in-scope developers at CP9. The near-universal R=0 state is driven by outlier premium spend (>1,700) wiping out the lean bonus and zeroing base R across the team.

**Users capped by Override 2 (raw score > Tier C blocked):**

| Login | Raw Score | Would Be | Override Result |
|---|---|---|---|
| Prathmesh-Ranadive | C=2, R=0, Q=3 = **5** | Tier B | Capped → **C** |
| mshnayderman | C=3, R=0, Q=2 = **5** | Tier B | Capped → **C** |
| luisalvatierra | C=3, R=0, Q=3 = **6** | Tier B | Capped → **C** |
| nilesht-19 | C=3, R=0, Q=3 = **6** | Tier B | Capped → **C** |
| Vyankatesh95 | C=3, R=0, Q=3 = **6** | Tier B | Capped → **C** |
| trunalgawade | C=3, R=0, Q=3 = **6** | Tier B | Capped → **C** |
| Akale23 | C=3, R=0, Q=3 = **6** | Tier B | Capped → **C** |
| Vitthal-Nice | C=2, R=0, Q=3 = **5** | Tier B | Capped → **C** |
| jkumbhar | C=3, R=0, Q=2 = **5** | Tier B | Capped → **C** |
| dsuraj25 | C=3, R=0, Q=3 = **6** | Tier B | Capped → **C** |

**Users where R=0 + Premium > 500 applies but raw score is already ≤ 4 (override confirms C, no change):**

amol-salunkhe (4), Kranti-nice (4), chris-haun (4), mfield1 (4), PradnyeshSalunke (4), mshivarkar (4), vishal-tad (4), sskalaskar (4), abhishekhole-nice (4), jayesh-rai (4), tusharpatil166719 (4), suhas-kakde (4), Shreedevi-nice (4), meghabiradar05 (4), prashasti-jain (4), pdevle (4), pratikpawar12 (4), amol-doke (4), mohitbaghelnice (4), moadzughul (3), thakraln (3)

**pratikpawar12 note:** Premium = 815 (> 500 but < 1,700 — not outlier). R=0 due to zero base efficiency only (no lean, no outlier penalty). Override 2 still applies: R=0 AND Premium 815 > 500.

### Override 1: Q=0 → Cannot Be Tier A

No in-scope user has Q=0 at CP9 with a raw score ≥ 7. Not triggered for any developer in this period. (giteshsawant has Q=1 but total score = 2, already Tier D.)

### Override 3: Momentum > 100% → Eligible for One-Tier Promotion

**Users with LoC growth > 100% vs CP8:**

| Login | CP8 LoC | CP9 LoC | Growth | Override 2 blocks? | Promotion |
|---|---|---|---|---|---|
| mshivarkar | 2,097 | 4,201 | +100.3% | Yes (R=0+Prem 17,029) | None — blocked |
| thakraln | ~0 | 806 | New entrant | Yes (R=0+Prem 13,562) | None — blocked |
| dsuraj25 | ~0 | 1,169 | New entrant | Yes (R=0+Prem 9,893) | None — blocked |
| abhijeetk268 | ~0 | 656 | New entrant | No | B → eligible for A? — but total = 6; promotion → 7 = **A** |
| pratikpawar12 | ~0 | 250 | New entrant | Yes (R=0+Prem 815) | None — blocked |
| amol-doke | ~0 | 10 | New entrant | Yes (R=0+Prem 2,528) | None — blocked |
| mohitbaghelnice | ~0 | 3 | New entrant (trivial) | Yes (R=0+Prem 2,393) | None — blocked |
| kbajaj-nice | ~0 | 5 | New entrant (trivial) | No | B → eligible; but LoC=5 trivial → not applied |
| dannycadima | ~0 | 34 | New entrant | No | Already A (7); no effect |

**Promotion applied:** abhijeetk268 — new entrant CP9, +inf% momentum, no Override 2 block. Raw score 6 (Tier B) → promoted to **Tier A**. Note: actual LoC (656) and PR data (53 PRs, 49 merged) independently justify this recognition.

**Promotion NOT applied:** kbajaj-nice (LoC=5 is trivially small; momentum argument weak despite no override block).

---

## Tier Groupings — CP9

### Tier A — CRQC Score 7–9 (2 users + 1 momentum promotion)

| Login | Name | C | R | Q | Total | Path / Notable |
|---|---|---|---|---|---|---|
| dannycadima | Danny Cadima Molina | 2 | 3 | FB(2) | **7** | New entrant. ReqEff 11.0 on 3 premium requests + lean spend. Statistically thin sample — see note. |
| abhijeetk268 | Abhijeet Kolhe | 2 | 1 | 3 | **6** → **A** | Momentum promotion (new entrant CP9). 53 PRs, 49 merged, 13h avg merge. PR throughput leader. |

**Tier A note — dannycadima:** Score 7 is technically correct under the framework: C=2 (ReqEff 11.0 → 1pt + new-entrant LoC trend +1), R=3 (ReqEff 10–20 bracket = 2pts + lean Prem=3 bonus = 3), Q=FB (active user, no PR data, conservative proxy = 2). However, with only 3 premium requests, 34 total LoC, and 0 PRs, the sample is too thin for reliable scoring. Flag for VP review as a data-artifact A rather than a performance-validated A.

**Tier A note — abhijeetk268:** PR throughput is the strongest signal. 53 PRs submitted, 49 merged (92.5% merge rate), 13h 19m average time to merge — the fastest pipeline in the team. Copilot usage is modest (39 initiatives, 656 LoC) but growing from zero. Momentum promotion is justified by both trajectory and execution quality.

### Tier B — CRQC Score 5–6 (3 users, after overrides)

| Login | Name | C | R | Q | Total | Override | Notable |
|---|---|---|---|---|---|---|---|
| copilotshree | (Shreedevi?) | 1 | 3 | FB(2) | **6** | None | Only R=3 user besides dannycadima. SuggEff 11.02, lean spend 340. No PR data captured. |
| kbajaj-nice | Kaushal Bajaj | 1 | 1 | 3 | **5** | None | New entrant CP9. Lean spend (Prem=6). Minimal LoC but solid PR contribution (2 PRs, 100% merge). |
| (abhijeetk268) | (promoted to A) | — | — | — | — | — | — |

**Tier B note — copilotshree:** This user's identity needs confirmation (possible duplicate account for Shreedevi Patil or a different user). R=3 is the standout signal: SuggEff 14.8 qualifies for 10–20 bracket (2pts) + lean spend 340 (+1) = 3. If identity confirmed, this is the second-most ROI-efficient user in the team at CP9.

### Tier C — Override-Capped + Organic (32 users)

Tier C is the dominant tier at CP9, driven overwhelmingly by Override 2 (R=0 + Premium > 500). 30 of 32 Tier C users are override-capped.

**Group 1 — Override-Capped (would be Tier B, held at C):**

| Login | Name | Raw Score | Would Be |
|---|---|---|---|
| luisalvatierra | Luis Salvatierra | 6 | B |
| nilesht-19 | Nilesh Tonape | 6 | B |
| Vyankatesh95 | Vyankatesh Khadakkar | 6 | B |
| trunalgawade | Trunal Gawde | 6 | B |
| Akale23 | Amulya Kale | 6 | B |
| dsuraj25 | Suraj Dubey | 6 | B |
| Prathmesh-Ranadive | Prathmesh Ranadive | 5 | B |
| mshnayderman | Mikhail Shnayderman | 5 | B |
| Vitthal-Nice | Vitthal Devkar | 5 | B |
| jkumbhar | Jyoti Kumbhar | 5 | B |

**Group 2 — Override-Capped (raw score 3–4, override confirms C):**

amol-salunkhe (4) | Kranti-nice (4) | chris-haun (4) | mfield1 (4) | rpawar-nice (4) | PradnyeshSalunke (4) | mshivarkar (4) | vishal-tad (4) | sskalaskar (4) | abhishekhole-nice (4) | jayesh-rai (4) | tusharpatil166719 (4) | suhas-kakde (4) | Shreedevi-nice (4) | meghabiradar05 (4) | prashasti-jain (4) | pdevle (4) | pratikpawar12 (4) | amol-doke (4) | mohitbaghelnice (4) | thakraln (3) | moadzughul (3)

**Group 3 — Organic Tier C (no override):**

| Login | Name | C | R | Q | Total | Notes |
|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 1 | 1 | FB(2) | **4** | No PRs in dataset. Efficiency strong (ReqEff 9.9) but LoC flat vs CP8. |
| ssnikam | Sanket Nikam | 0 | 0 | 3 | **3** | Zero Copilot usage — PR contributor only. Q=3 from 55 PRs, 89.1% merge rate. |

### Tier D — CRQC Score 1–2 (1 user)

| Login | Name | C | R | Q | Total | Notes |
|---|---|---|---|---|---|---|
| giteshsawant | Gitesh Sawant | 1 | 0 | 1 | **2** | 1 PR submitted, 0 merged (0% merge rate) — Q=1 (time bonus only). No R (Prem 8,585 outlier, ReqEff 0.2). |

### Tier E — CRQC Score 0

No user scores 0 at CP9. The minimum observed score is 2 (giteshsawant).

---

## Tier Distribution Summary — CP9

| Tier | Score | Users | % | Signal |
|---|---|---|---|---|
| **A** | 7–9 | 2 | 5% | 1 data-artifact (dannycadima), 1 momentum promotion (abhijeetk268) |
| **B** | 5–6 | 2 | 5% | copilotshree (R=3 efficiency), kbajaj-nice (new entrant, lean) |
| **C** | 3–4 | 32 | 86% | Team-wide R=0 collapse from outlier premium spend |
| **D** | 1–2 | 1 | 3% | giteshsawant (0% PR merge rate, outlier premium) |
| **E** | 0 | 0 | 0% | No zero-score users this period |

**Total in-scope developers: 37**

---

## Budget Crisis Callout — Outlier Premium Users

**Definition:** Premium > 1,700 requests, triggering the outlier penalty (−1 to R) AND Override 2 (R=0 + Prem > 500 → cap at C).

All 34 users below have Premium > 1,700 and R=0. Combined premium consumption dwarfs output.

| Login | Name | Premium | ReqEff | LoC | Waste Estimate |
|---|---|---|---|---|---|
| tusharpatil166719 | Tushar Patil | 35,886 | 0.1 | 2,200 | At ReqEff 10 = 358,860 LoC potential; actual = 2,200 (99.4% waste) |
| Kranti-nice | Kranti Kaple | 35,537 | 1.1 | 37,978 | At ReqEff 10 = 355,370 LoC potential; actual = 37,978 (89.3% waste) |
| nilesht-19 | Nilesh Tonape | 32,332 | 0.2 | 7,354 | At ReqEff 10 = 323,320 LoC potential; actual = 7,354 (97.7% waste) |
| Prathmesh-Ranadive | Prathmesh Ranadive | 31,420 | 1.1 | 35,091 | At ReqEff 10 = 314,200 LoC potential; actual = 35,091 (88.8% waste) |
| amol-salunkhe | Amol Salunkhe | 20,170 | 2.2 | 43,585 | At ReqEff 10 = 201,700 LoC potential; actual = 43,585 (78.4% waste) |
| PradnyeshSalunke | Pradnyesh Salunke | 20,544 | 0.2 | 4,237 | At ReqEff 10 = 205,440 LoC potential; actual = 4,237 (97.9% waste) |
| trunalgawade | Trunal Gawde | 18,720 | 0.1 | 2,352 | At ReqEff 10 = 187,200 LoC potential; actual = 2,352 (98.7% waste) |
| mshivarkar | Mohan Shivarkar | 17,029 | 0.2 | 4,201 | At ReqEff 10 = 170,290 LoC potential; actual = 4,201 (97.5% waste) |
| sskalaskar | Sourabh Kalaskar | 16,897 | 0.2 | 3,233 | At ReqEff 10 = 168,970 LoC potential; actual = 3,233 (98.1% waste) |
| thakraln | Nishtha Thakral | 13,562 | 0.1 | 806 | At ReqEff 10 = 135,620 LoC potential; actual = 806 (99.4% waste) |
| chris-haun | Chris Haun | 12,535 | 0.8 | 10,493 | At ReqEff 10 = 125,350 LoC potential; actual = 10,493 (91.6% waste) |
| Shreedevi-nice | Shreedevi Patil | 12,071 | 0.2 | 1,886 | At ReqEff 10 = 120,710 LoC potential; actual = 1,886 (98.4% waste) |
| prashasti-jain | Prashasti Jain | 12,206 | 0.1 | 1,562 | At ReqEff 10 = 122,060 LoC potential; actual = 1,562 (98.7% waste) |
| meghabiradar05 | Megha Biradar | 10,131 | 0.2 | 1,727 | At ReqEff 10 = 101,310 LoC potential; actual = 1,727 (98.3% waste) |
| pdevle | Pratik Devle | 10,057 | 0.1 | 1,478 | At ReqEff 10 = 100,570 LoC potential; actual = 1,478 (98.5% waste) |
| dsuraj25 | Suraj Dubey | 9,893 | 0.1 | 1,169 | At ReqEff 10 = 98,930 LoC potential; actual = 1,169 (98.8% waste) |
| luisalvatierra | Luis Salvatierra | 9,542 | 1.3 | 12,080 | At ReqEff 10 = 95,420 LoC potential; actual = 12,080 (87.3% waste) |
| giteshsawant | Gitesh Sawant | 8,585 | 0.2 | 1,369 | At ReqEff 10 = 85,850 LoC potential; actual = 1,369 (98.4% waste) |
| vishal-tad | Vishal Tad | 9,301 | 0.4 | 3,737 | At ReqEff 10 = 93,010 LoC potential; actual = 3,737 (96.0% waste) |
| abhishekhole-nice | Abhishek Hole | 4,416 | 0.7 | 3,150 | At ReqEff 10 = 44,160 LoC potential; actual = 3,150 (92.9% waste) |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,118 | 1.0 | 4,177 | At ReqEff 10 = 41,180 LoC potential; actual = 4,177 (89.9% waste) |
| Akale23 | Amulya Kale | 4,237 | 0.6 | 2,472 | At ReqEff 10 = 42,370 LoC potential; actual = 2,472 (94.2% waste) |
| mshnayderman | Mikhail Shnayderman | 5,452 | 5.1 | 27,539 | At ReqEff 10 = 54,520 LoC potential; actual = 27,539 (49.4% waste) |
| mfield1 | Matt Field | 3,133 | 3.1 | 9,803 | At ReqEff 10 = 31,330 LoC potential; actual = 9,803 (68.7% waste) |
| jayesh-rai | Jayesh Rai | 1,997 | 1.4 | 2,712 | At ReqEff 10 = 19,970 LoC potential; actual = 2,712 (86.4% waste) |
| jkumbhar | Jyoti Kumbhar | 2,110 | 0.9 | 1,880 | At ReqEff 10 = 21,100 LoC potential; actual = 1,880 (91.1% waste) |
| Vitthal-Nice | Vitthal Devkar | 2,393 | 1.1 | 2,683 | At ReqEff 10 = 23,930 LoC potential; actual = 2,683 (88.8% waste) |
| suhas-kakde | Suhas Kakde | 2,797 | 0.7 | 2,005 | At ReqEff 10 = 27,970 LoC potential; actual = 2,005 (92.8% waste) |
| amol-doke | Amol Doke | 2,528 | 0.0 | 10 | At ReqEff 10 = 25,280 LoC potential; actual = 10 (99.9% waste) |
| mohitbaghelnice | Mohit Baghel | 2,393 | 0.0 | 3 | At ReqEff 10 = 23,930 LoC potential; actual = 3 (99.9% waste) |

**Aggregate premium consumed by outlier users:** ~371,000 premium requests
**Aggregate LoC produced:** ~319,000 LoC
**Potential LoC at benchmark ReqEff = 10:** ~3,710,000 LoC
**Efficiency gap:** ~90% — the team is generating 1/10th of its potential output per premium dollar

**Highest-priority interventions (ReqEff < 0.5, Premium > 10,000):**

| Login | Premium | ReqEff | Recommended Action |
|---|---|---|---|
| tusharpatil166719 | 35,886 | 0.1 | Immediate coaching — investigate agent session patterns |
| nilesht-19 | 32,332 | 0.2 | Agent session length audit — possible runaway loops |
| thakraln | 13,562 | 0.1 | Agent session review — 215 initiatives, 0 PRs, 806 LoC |
| prashasti-jain | 12,206 | 0.1 | Agent usage review |
| Shreedevi-nice | 12,071 | 0.2 | Agent session audit |
| chris-haun | 12,535 | 0.8 | Premium > 10K despite moderate ReqEff — volume check |
| PradnyeshSalunke | 20,544 | 0.2 | Agent session patterns — 664 initiatives with minimal output |
| trunalgawade | 18,720 | 0.1 | 389 initiatives, 1 PR, 2,352 LoC — high activity, low yield |

---

## Special Roles — Evaluated Separately

### SwapnilNice — Manager

| Metric | Value | Notes |
|---|---|---|
| LoC | 3,140 | Reasonable for a manager |
| Premium | 1,650 | Near outlier threshold (< 1,700 — not penalized) |
| ReqEff | 1.9 | Very low; expected for managerial usage pattern |
| %Accept | 4.0% | Low — consistent with review/exploration usage |
| Initiatives | 279 | High — managerial query volume |
| C (CRQC-equiv) | 1 | ReqEff < 8 = 0 + LoC increasing = 1 |
| R (CRQC-equiv) | 0 | ReqEff < 5 = 0; Prem 1,650 not lean, not outlier |
| Q | FB | PR data not in snapshot |
| Tier (indicative) | C | Override: R=0 + Prem 1,650 > 500 |
| Context | Manager — usage focused on queries, planning, code review assistance rather than direct code generation. Tier C is expected and appropriate. |

### ssamal-nice — Manager

| Metric | Value | Notes |
|---|---|---|
| LoC | 38 | Low — typical lightweight manager usage |
| Premium | 109 | Lean (≤ 500) |
| ReqEff | 0.3 | Very low |
| %Accept | 7.7% | Low |
| Initiatives | 30 | Low |
| C (CRQC-equiv) | 1 | ReqEff < 8 = 0 + LoC increasing from low base = 1 |
| R (CRQC-equiv) | 1 | ReqEff 0.3 = 0 base + lean (109 ≤ 500) = +1 = 1 |
| Q | FB | PR data not in snapshot |
| Tier (indicative) | C | Total 1+1+2 = 4, no override (Prem ≤ 500) |
| Context | Lightweight managerial usage, lean spend. Appropriate profile. |

### smishra-nice — Lead / Architect

| Metric | Value | Notes |
|---|---|---|
| LoC | 155 | Low volume; consistent with code review / design assistance |
| Premium | 287 | Lean (≤ 500) |
| ReqEff | 0.5 | Low — expected for discussion/review usage |
| %Accept | 78.3% | Well above Lead benchmark (10–25%); high-accept suggests bulk or auto-complete usage |
| Initiatives | 60 | Moderate |
| C (CRQC-equiv) | 2 | %Accept > 35% = 1pt + Code Accept 60 > 20 = +1 = 2 |
| R (CRQC-equiv) | 1 | ReqEff 0.5 = 0 base + lean 287 = +1 = 1 |
| Q | FB | PR data not in snapshot |
| Tier (indicative) | B | Total 2+1+2 = 5, no override |
| Lead benchmark | %Accept target 10–25% — smishra-nice at 78.3% is outside benchmark. Possible bulk acceptance pattern. Recommend review of accept behavior vs actual code review usage intent. |

### rwalunj-nice — Research (Not Tiered)

| Metric | Value | Notes |
|---|---|---|
| LoC | 156 | Research-oriented |
| Premium | 1,890 | Outlier by definition — research sessions expected to be long |
| ReqEff | 0.1 | As expected for research/exploration sessions |
| %Accept | 7.1% | Low |
| Tier | Not tiered | Research role excluded from tier assignment per team charter |

---

## CP8 → CP9 Score Changes — Notable Movements

| Login | CP8 Tier | CP9 Tier | Delta | Root Cause |
|---|---|---|---|---|
| abhijeetk268 | N/A (new) | A | New → A | New entrant CP9; momentum promotion applied |
| dannycadima | N/A (new) | A | New → A | New entrant CP9; lean spend + 10–20 ReqEff bracket |
| copilotshree | N/A | B | Existing → B | R=3 from lean spend + SuggEff in 10–20 bracket |
| kbajaj-nice | N/A (new) | B | New → B | New entrant; lean spend |
| rpawar-nice | A (CP8) | C | A → C | LoC flat (8,662 = 8,662), no PR data, R only 1. Workflow reclassified to AF under new rules. |
| mshnayderman | C (CP8) | C | Stable | R=0 override continues |
| Vyankatesh95 | A (CP8) | C | A → C | Reclassified under new rules; R=0 outlier override now dominant |
| nilesht-19 | C (CP8) | C | Stable | Budget crisis continues |

**Key structural change CP8 → CP9:** The revised framework now classifies by SuggEff + %Accept (not by Agent Contribution %). This shifts several users between workflow types. Most significantly, users with high SuggEff but zero premium efficiency (ReqEff < 5) remain locked at Tier C by Override 2, regardless of their C score.

---

## Q2 Closing Note — 7 Days Remaining

Q2 closes June 30, 2026. With CP9 representing the final major data point before close, the following patterns are significant:

**Q2 Performance Summary (CP9 snapshot):**

| Metric | Team Value | Notes |
|---|---|---|
| Total in-scope LoC (37 devs) | ~329,000 | Dominated by top 5 users (amol, Kranti, Prathmesh, mshnayderman, chris-haun) |
| Total PRs merged | ~514 | From dataset; strong PR throughput |
| Team avg merge rate | ~90% | High — strong code review culture |
| Tier A users | 2 | Down from 7 at CP7; 1 is a data artifact |
| Override-capped users | 32/37 | 86% of team capped by R=0 override |
| Users with ReqEff > 5 | 3 | rpawar-nice (9.9), copilotshree (14.8), mshnayderman (5.1) |
| Users with lean spend (≤500 prem) | 5 | copilotshree, abhijeetk268, kbajaj-nice, dannycadima, smishra-nice (special) |

**Q2 closing priorities (7 days):**

1. **ROI intervention for top 8 premium consumers** — tusharpatil166719, nilesht-19, thakraln, PradnyeshSalunke, prashasti-jain, Shreedevi-nice, chris-haun, trunalgawade. These 8 users account for ~200,000 premium requests with combined ReqEff < 0.5. Any Q2-close coaching improvement shows immediately in CP10.

2. **PR pipeline acceleration for rpawar-nice** — Strong Copilot efficiency (ReqEff 9.9, 8,662 LoC) but zero PRs in the snapshot. If this is a data-capture gap, verify. If genuine, this is the single highest-leverage path to Tier A recovery for a known strong contributor.

3. **copilotshree identity resolution** — R=3 efficiency user with 0 PRs and unknown identity. Confirm account ownership before Q2 reporting.

4. **Monitor new entrants** — 8 users appear for the first time in CP9. As of Q2 close, their contribution is thin. Set Q3 targets based on CP9 baselines.

---

## VP Defense Narrative

> "At CP9, the CRQC framework surfaces a team-wide ROI crisis: 32 of 37 developers are capped at Tier C due to outlier premium spend with near-zero request efficiency. This is not a code quality problem — our PR merge rate is 90%, time-to-merge is strong, and review coverage is solid across the team. The problem is specifically in how GitHub Copilot Agent sessions are consuming premium requests without producing proportional code output.
>
> Our two Tier A contributors at CP9 are Abhijeet Kolhe — promoted via momentum, with the fastest PR pipeline on the team (53 PRs, 13-hour average merge) — and Danny Cadima, a new entrant whose score reflects excellent efficiency on a thin data sample. Both are recognized, but neither represents the scale of contribution we saw from Ritesh Pawar or Vyankatesh Khadakkar at CP7.
>
> The structural story for the VP review is this: users like Nilesht Tonape, Vyankatesh Khadakkar, Luis Salvatierra, and Trunal Gawde would be Tier B performers under the framework if their premium spend were halved. Their C scores are 3, their Q scores are 3, and their PR behavior is solid. The only blocking variable is premium efficiency. Seven days remain in Q2. A focused coaching conversation on agent session management — specifically, stopping runaway sessions and reviewing output before accepting — could move these users from Tier C to Tier B by CP10.
>
> The one user I would flag specifically is Ritesh Pawar. At CP7 and CP8, he was our strongest all-round performer. At CP9, his LoC is flat and there are no PRs in the snapshot. That may be a data pipeline issue rather than a performance issue. Verify before including in any management report."

---

*CRQC Framework — CP9 (Jun 23, 2026). 16 users excluded per ignore list (tomotvos, dhanshree-jagtap-nice, sohanbafna, GovindSomaniNice, rizeq-abu-madeghem, nice-harshada, yogitadhanwate, AnaSarzosa, sachinfuse-nice, anjali-sherikar, ShivrajNice, prashant-shete, rajivranjannice, BireshwarNice, prinice251, ak-nice-2025). Special roles (SwapnilNice, ssamal-nice, smishra-nice) evaluated separately. rwalunj-nice not tiered. Q=FB denotes active user with no PR data captured (treated as Q=2 for tier calculation). PR data from Jun 21, 2026 snapshot.*
