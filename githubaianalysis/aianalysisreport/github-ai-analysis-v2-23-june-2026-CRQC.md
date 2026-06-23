# GitHub Copilot CRQC Progression Analysis — Multi-Period Evolution
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Range:** CP1 (Apr 20, 2026) → CP9 (Jun 23, 2026) — 9 checkpoints, 64 days  
**Report Date:** Jun 23, 2026 | **Framework Version:** CRQC v2 (CP8–CP9 full; CP1–CP7 C+R estimated)  
**Scope:** 37 in-scope developers | 15 + 1 excluded per ignore list | 3 special roles tracked separately

---

## 1. CRQC Framework Brief

The CRQC framework scores every in-scope developer on three measurable pillars, summed to a 0–9 total that maps to a tier. Context (the fourth letter) is diagnostic only — it explains scores but never directly raises them.

| Pillar | Max | What It Measures |
|---|---|---|
| **C** (Core) | 0–3 | Workflow-specific Copilot productivity — how well the user leverages their workflow pattern |
| **R** (ROI) | 0–3 | Request Efficiency (LoC per premium request) plus premium spend discipline |
| **Q** (Quality) | 0–3 | PR merge rate, reviews per PR, and time-to-merge |
| **Total** | 0–9 | C + R + Q |

**Tier mapping:** A = 7–9 | B = 5–6 | C = 3–4 | D = 1–2 | E = 0

### C Pillar — Workflow-Dependent

**CP8–CP9 workflow classification** uses SuggEff + %Accept (Agent Contribution % unavailable):
- Agent-First: SuggEff > 20 AND %Accept < 20%
- Agent-First Lean: SuggEff ≤ 20 AND %Accept < 20%
- Inline-First / Hybrid: %Accept ≥ 20%

**Agent-First C:** ReqEff > 15 = 2pts | 8–15 = 1pt | < 8 = 0pts; LoC increasing vs prior CP = +1 (cap 3)  
**Inline-First C:** %Accept 20–35% = 2pts | >35% = 1pt | 10–19% = 1pt; Code Accept count > 20 = +1 (cap 3)

### R Pillar — Universal

- ReqEff > 20 = 3pts | 10–20 = 2pts | 5–10 = 1pt | < 5 = 0pts
- Lean spend (Premium ≤ 500): +1 bonus
- Outlier spend (Premium > 1,700): −1 penalty (floor 0)

### Q Pillar — PR-Based

- Merge rate ≥ 80% = 2pts | 50–79% = 1pt | < 50% = 0pts
- Reviews ≥ 1 per PR = +1pt
- Avg time to merge ≤ 72h = +1 bonus
- Cap Q at 3
- Q = FB (Fallback) = active user with zero PR data captured; treated as Q = 2

### Override Rules

1. **Q = 0 → Cannot be Tier A** (no quality signal)
2. **R = 0 AND Premium > 500 → Cannot exceed Tier C** (budget drain, no efficiency — cap enforced regardless of C+Q score)
3. **Momentum > 100% LoC vs prior CP → eligible for one-tier promotion** (blocked if Override 2 also applies)

### Data Availability by Period

| Checkpoint | Date | Premium Data | C Score | R Score | Q Score | Full CRQC |
|---|---|---|---|---|---|---|
| CP1 | Apr 20 | Not available | LoC-estimated | Not computable | Not available | No |
| CP2 | Apr 23 | Not available | LoC-estimated | Not computable | Not available | No |
| CP3 | Apr 28 | Not available | LoC-estimated | Not computable | Not available | No |
| CP4 | May 11 | Partial (estimated from ReqEff patterns) | Available | Estimated | Team proxy | Partial |
| CP5 | May 18 | Partial | Available | Estimated | Team proxy | Partial |
| CP6 | Jun 3 | Partial | Available | Estimated | Team proxy | Partial |
| CP7 | Jun 8 | Partial | Available | Estimated | Team proxy | Partial |
| **CP8** | **Jun 12** | **Full** | **Full** | **Full** | **Full** | **Yes** |
| **CP9** | **Jun 23** | **Full** | **Full** | **Full** | **Full** | **Yes** |

---

## 2. LoC Progression — All 9 Checkpoints

Cumulative LoC is the primary driver of C score potential across checkpoints. Users are sorted by CP9 total.

| User | CP1 Apr20 | CP2 Apr23 | CP3 Apr28 | CP4 May11 | CP5 May18 | CP6 Jun3 | CP7 Jun8 | CP8 Jun12 | CP9 Jun23 | Net Growth | CP1→CP9 CAGR (weekly) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | 31 | 31 | 2,210 | 17,155 | 28,911 | 30,486 | 34,037 | 41,008 | **43,585** | +43,554 | Dominant |
| Kranti-nice | 2,148 | 2,148 | 3,259 | 3,259 | 7,076 | 27,733 | 27,733 | 31,645 | **37,978** | +35,830 | Strong |
| Prathmesh-Ranadive | 1,373 | 1,373 | 1,848 | 8,783 | 9,489 | 20,436 | 27,052 | 27,052 | **35,091** | +33,718 | Strong |
| mshnayderman | 20,399 | 20,399 | 20,951 | 22,268 | 22,268 | 24,387 | 27,539 | 27,539 | **27,539** | +7,140 | Plateau |
| luisalvatierra | 1,216 | 1,216 | 1,444 | 1,698 | 2,292 | 4,564 | 4,800 | 9,477 | **12,080** | +10,864 | Late surge |
| chris-haun | 6,034 | 6,376 | 6,670 | 6,758 | 8,592 | 10,264 | 10,359 | 10,384 | **10,493** | +4,459 | Slowing |
| mfield1 | 4,414 | 4,414 | 5,637 | 8,566 | 9,071 | 9,251 | 9,300 | 9,800 | **9,803** | +5,389 | Slowing |
| rpawar-nice | 8,566 | 8,640 | 8,640 | 8,640 | 8,658 | 8,662 | 8,662 | 8,662 | **8,662** | +96 | Flat (CP3+) |
| nilesht-19 | 1,287 | 1,567 | 3,598 | 4,908 | 5,065 | 5,293 | 7,160 | 7,346 | **7,354** | +6,067 | Slowing |
| copilotshree | 4,543 | 4,543 | 4,553 | 4,706 | 5,013 | 5,013 | 5,013 | 5,013 | **5,013** | +470 | Near-flat |
| PradnyeshSalunke | 857 | 857 | 857 | 1,735 | 1,948 | 2,296 | 2,968 | 3,731 | **4,237** | +3,380 | Steady |
| Vyankatesh95 | 1,968 | 1,968 | 2,350 | 2,795 | 3,673 | 4,151 | 4,177 | 4,177 | **4,177** | +2,209 | Stagnating |
| mshivarkar | 0 | 1 | 28 | 28 | 28 | 1,559 | 2,018 | 2,097 | **4,201** | +4,201 | Late surge |
| vishal-tad | 739 | 952 | 1,156 | 1,156 | 1,156 | 2,815 | 2,900 | 3,520 | **3,737** | +2,998 | Mid surge |
| moadzughul | 2,572 | 2,572 | 2,620 | 2,655 | 2,749 | 3,035 | 3,100 | 3,409 | **3,409** | +837 | Slow |
| sskalaskar | 302 | 517 | 517 | 2,056 | 2,056 | 2,609 | 2,700 | 2,698 | **3,233** | +2,931 | Steady |
| abhishekhole-nice | 267 | 267 | 319 | 2,722 | 2,803 | 2,803 | 2,936 | 2,993 | **3,150** | +2,883 | Stagnating |
| Akale23 | 292 | 292 | 779 | 1,133 | 1,856 | 2,409 | 2,472 | 2,472 | **2,472** | +2,180 | Stagnating |
| jayesh-rai | 1 | 1 | 1 | 777 | 862 | 2,196 | 2,479 | 2,479 | **2,712** | +2,711 | Mid surge |
| Vitthal-Nice | 1,180 | 1,180 | 1,180 | 2,472 | 2,566 | 2,609 | 2,609 | 2,609 | **2,683** | +1,503 | Slowing |
| trunalgawade | 6 | 6 | 61 | 261 | 302 | 304 | 1,086 | 2,038 | **2,352** | +2,346 | Late surge |
| tusharpatil166719 | 381 | 381 | 853 | 1,389 | 1,631 | 1,798 | 1,798 | 1,798 | **2,200** | +1,819 | Stagnating mid |
| suhas-kakde | 1,367 | 1,367 | 1,597 | 1,615 | 1,639 | 1,639 | 1,639 | 1,677 | **2,005** | +638 | Near-flat |
| Shreedevi-nice | 38 | 56 | 88 | 88 | 690 | 1,013 | 1,416 | 1,786 | **1,886** | +1,848 | Steady |
| jkumbhar | 1,316 | 1,316 | 1,412 | 1,412 | 1,788 | 1,868 | 1,870 | 1,870 | **1,880** | +564 | Near-flat |
| meghabiradar05 | 0 | 0 | 1,389 | 1,389 | 1,389 | 1,684 | 1,700 | 1,720 | **1,727** | +1,727 | Stagnating |
| prashasti-jain | 0 | 0 | 0 | 203 | 837 | 872 | 900 | 1,545 | **1,562** | +1,562 | Steady |
| pdevle | 361 | 361 | 368 | 370 | 370 | 1,049 | 1,100 | 1,384 | **1,478** | +1,117 | Steady |
| dsuraj25 | 491 | 491 | 491 | 491 | 491 | 504 | 510 | 510 | **1,169** | +678 | Late surge |
| Shubhamfulzele28 | 0 | 0 | 0 | 0 | 0 | 0 | 739 | 739 | **1,043** | +1,043 | CP7 entrant |
| giteshsawant | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 1,110 | **1,369** | +1,369 | CP7 entrant |
| thakraln | 0 | 0 | 0 | 0 | 0 | 69 | 69 | 750 | **806** | +806 | CP6 entrant |
| abhijeetk268 | 172 | 172 | 172 | 172 | 173 | 656 | 656 | 656 | **656** | +484 | Slow then burst |
| pratikpawar12 | 0 | 0 | 0 | 166 | 250 | 250 | 250 | 250 | **250** | +250 | Minimal |

### LoC Growth Velocity Observations

**Breakout Users (CP1→CP9, trajectory changing upward):**
- amol-salunkhe: Flat through CP2, explosive burst CP2→CP4 (+15K), sustained through CP9
- Kranti-nice: Dormant through CP4, massive surge CP5→CP6 (+20K in 16 days), continued
- Prathmesh-Ranadive: Consistent growth with CP6→CP7 surge (+6.6K), plateaued CP8→CP9
- mshivarkar: Zero through CP5, full dormancy-to-growth pattern starting CP6

**Plateau Users (LoC growth decelerating or stopped):**
- mshnayderman: Grew steadily through CP7, FLAT at 27,539 across CP7→CP8→CP9
- rpawar-nice: Essentially flat since CP3 (8,640 → 8,662, +22 LoC in 8 weeks)
- copilotshree: Flat since CP5 (5,013 unchanged through CP9)
- Vyankatesh95: Flat since CP7 (4,177 unchanged through CP9)
- Akale23: Flat since CP7 (2,472 unchanged through CP9)

**Late Entrants (CP6–CP8 first meaningful LoC):**
- giteshsawant: Zero through CP6, 50 at CP7, 1,110 at CP8, 1,369 at CP9
- thakraln: Zero through CP5, 69 at CP6, 750 at CP8, 806 at CP9
- Shubhamfulzele28: Zero through CP6, 739 at CP7, 1,043 at CP9
- trunalgawade: Near-zero through CP6, surge to 1,086 at CP7, 2,352 at CP9

---

## 3. CP8 vs CP9 Full CRQC Scorecard Comparison

Full CRQC scores are available for both CP8 (Jun 12) and CP9 (Jun 23). The comparison shows score changes across the 11-day window.

### CP8 Score Table (Jun 12, 2026)

*Note: CP8 used a prior workflow classification scheme (Agent/Hybrid/Inline by Agent Contribution %). Scores are sourced from the Jun 12 CRQC analysis.*

| Login | Name | LoC CP8 | Prem CP8 | ReqEff CP8 | C8 | R8 | Q8 | Total8 | Tier8 |
|---|---|---|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 8,662 | ~850 | ~10.2 | 3 | 2 | 3 | **8** | **A** |
| Kranti-nice | Kranti Kaple | 31,645 | 11,979 | ~2.6 | 3 | 0 | 3 | **6** | **C** (Ovr2) |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,177 | ~450 | ~9.3 | 3 | 0 | 3 | **6** | **A** (prior rules) |
| mshnayderman | Mikhail Shnayderman | 27,539 | 5,419 | ~5.1 | 3 | 0 | 3 | **6** | **C** (Ovr2) |
| nilesht-19 | Nilesh Tonape | 7,346 | 30,437 | ~0.2 | 3 | 0 | 3 | **6** | **C** (Ovr2) |
| luisalvatierra | Luis Salvatierra | 9,477 | ~9,477/est | ~1.0 | 3 | 0 | 3 | **6** | **C** (Ovr2) |
| amol-salunkhe | Amol Salunkhe | 41,008 | 11,150 | ~3.7 | 3 | 0 | 3 | **6** | **C** (Ovr2) |
| mfield1 | Matt Field | 9,800 | ~1,813 | ~5.4 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| chris-haun | Chris Haun | 10,384 | ~12,000 | ~0.9 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| PradnyeshSalunke | Pradnyesh Salunke | 3,731 | 15,719 | ~0.2 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| mshivarkar | Mohan Shivarkar | 2,097 | ~8,000 | ~0.3 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| vishal-tad | Vishal Tad | 3,520 | ~9,000 | ~0.4 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| sskalaskar | Sourabh Kalaskar | 2,698 | ~11,000 | ~0.2 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| abhishekhole-nice | Abhishek Hole | 2,993 | ~10,000 | ~0.3 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| jayesh-rai | Jayesh Rai | 2,479 | ~852 | ~2.9 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| thakraln | Nishtha Thakral | 750 | ~12,000 | ~0.1 | 1 | 0 | 2 | **3** | **C** (Ovr2) |
| Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | ~10,733 | ~2.5 | 2 | 0 | 3 | **5** | **C** (Ovr2) |
| Vitthal-Nice | Vitthal Devkar | 2,609 | ~413 | ~6.3 | 2 | 1 | 3 | **6** | **A** (prior rules) |
| trunalgawade | Trunal Gawde | 2,038 | 16,265 | ~0.1 | 3 | 0 | 3 | **6** | **C** (Ovr2) |
| Akale23 | Amulya Kale | 2,472 | ~200 | ~12.4 | 3 | 0 | 3 | **6** | **A** (prior rules) |
| moadzughul | Moad Alzughul | 3,409 | ~3,000 | ~1.1 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| Shreedevi-nice | Shreedevi Patil | 1,786 | ~12,000 | ~0.1 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| jkumbhar | Jyoti Kumbhar | 1,870 | ~2,110 | ~0.9 | 2 | 0 | 3 | **5** | **C** (Ovr2) |
| meghabiradar05 | Megha Biradar | 1,720 | ~10,000 | ~0.2 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| prashasti-jain | Prashasti Jain | 1,545 | ~12,000 | ~0.1 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| pdevle | Pratik Devle | 1,384 | ~10,000 | ~0.1 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| dsuraj25 | Suraj Dubey | 510 | ~8,000 | ~0.1 | 2 | 0 | 3 | **5** | **C** (Ovr2) |
| suhas-kakde | Suhas Kakde | 1,677 | ~2,500 | ~0.7 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| tusharpatil166719 | Tushar Patil | 1,798 | 10,754 | ~0.2 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| Vyankatesh95 (restated) | — | — | — | — | — | — | — | — | See note |
| Shubhamfulzele28 | Shubham Fulzele | 739 | 13,831 | ~0.1 | 1 | 0 | 3 | **4** | **C** (Ovr2) |
| giteshsawant | Gitesh Sawant | 1,110 | ~8,500 | ~0.1 | 1 | 0 | 1 | **2** | **D** |
| copilotshree | (Shreedevi?) | 5,013 | 340 | ~14.7 | 1 | 3 | 2 | **6** | **B** |
| pratikpawar12 | Pratik Pawar | 250 | ~500 | ~0.5 | 0 | 0 | 3 | **3** | **C** |
| abhijeetk268 | Abhijeet Kolhe | 656 | ~50 | ~13.1 | 0 | 3 | 3 | **6** | **B** (est.) |

*CP8 tier assignments used prior workflow classification (Agent Contribution %). Several users (rpawar-nice, Vitthal-Nice, Vyankatesh95, Akale23) were Tier A under CP7–CP8 rules, then reclassified under CP9's SuggEff+%Accept method. The CP9 column below uses the new rules consistently.*

---

### CP9 Full CRQC Scorecard (Jun 23, 2026)

| Login | Name | Workflow | LoC | %Accept | Prem | ReqEff | C | R | Q | Total | Override | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dannycadima | Danny Cadima Molina | AF-Lean | 34 | 12.7% | 3 | 11.0 | 2 | 3 | FB(2) | **7** | — | **A** |
| abhijeetk268 | Abhijeet Kolhe | Inline | 656 | 29.6% | 451 | 1.5 | 2 | 1 | 3 | **6→7** | Momentum promo | **A** |
| copilotshree | (Shreedevi?) | AF-Lean | 5,013 | 4.8% | 340 | 14.8 | 1 | 3 | FB(2) | **6** | — | **B** |
| kbajaj-nice | Kaushal Bajaj | AF-Lean | 5 | 17.5% | 6 | 0.8 | 1 | 1 | 3 | **5** | — | **B** |
| amol-salunkhe | Amol Salunkhe | AF | 43,585 | 1.5% | 20,170 | 2.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| Kranti-nice | Kranti Kaple | AF | 37,978 | 4.6% | 35,537 | 1.1 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline | 35,091 | 88.7% | 31,420 | 1.1 | 2 | 0 | 3 | **5** | R=0+Prem>500 | **C** |
| mshnayderman | Mikhail Shnayderman | Inline | 27,539 | 27.8% | 5,452 | 5.1 | 3 | 0 | 2 | **5** | R=0+Prem>500 | **C** |
| luisalvatierra | Luis Salvatierra | Inline | 12,080 | 24.2% | 9,542 | 1.3 | 3 | 0 | 3 | **6** | R=0+Prem>500 | **C** |
| nilesht-19 | Nilesh Tonape | Inline | 7,354 | 30.2% | 32,332 | 0.2 | 3 | 0 | 3 | **6** | R=0+Prem>500 | **C** |
| Vyankatesh95 | Vyankatesh Khadakkar | Inline | 4,177 | 34.1% | 4,118 | 1.0 | 3 | 0 | 3 | **6** | R=0+Prem>500 | **C** |
| trunalgawade | Trunal Gawde | Inline | 2,352 | 20.4% | 18,720 | 0.1 | 3 | 0 | 3 | **6** | R=0+Prem>500 | **C** |
| Akale23 | Amulya Kale | Inline | 2,472 | 22.8% | 4,237 | 0.6 | 3 | 0 | 3 | **6** | R=0+Prem>500 | **C** |
| dsuraj25 | Suraj Dubey | Inline | 1,169 | 33.3% | 9,893 | 0.1 | 3 | 0 | 3 | **6** | R=0+Prem>500 | **C** |
| Vitthal-Nice | Vitthal Devkar | Inline | 2,683 | 40.4% | 2,393 | 1.1 | 2 | 0 | 3 | **5** | R=0+Prem>500 | **C** |
| jkumbhar | Jyoti Kumbhar | Inline | 1,880 | 22.0% | 2,110 | 0.9 | 3 | 0 | 2 | **5** | R=0+Prem>500 | **C** |
| chris-haun | Chris Haun | AF-Lean | 10,493 | 9.3% | 12,535 | 0.8 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| mfield1 | Matt Field | AF-Lean | 9,803 | 5.8% | 3,133 | 3.1 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| rpawar-nice | Ritesh Pawar | AF | 8,662 | 7.6% | 879 | 9.9 | 1 | 1 | FB(2) | **4** | — | **C** |
| PradnyeshSalunke | Pradnyesh Salunke | AF-Lean | 4,237 | 19.4% | 20,544 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| mshivarkar | Mohan Shivarkar | AF-Lean | 4,201 | 9.4% | 17,029 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| vishal-tad | Vishal Tad | AF-Lean | 3,737 | 8.8% | 9,301 | 0.4 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| sskalaskar | Sourabh Kalaskar | AF | 3,233 | 16.9% | 16,897 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| abhishekhole-nice | Abhishek Hole | AF | 3,150 | 3.2% | 4,416 | 0.7 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| jayesh-rai | Jayesh Rai | AF-Lean | 2,712 | 18.4% | 1,997 | 1.4 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| tusharpatil166719 | Tushar Patil | AF-Lean | 2,200 | 14.7% | 35,886 | 0.1 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| suhas-kakde | Suhas Kakde | AF-Lean | 2,005 | 1.7% | 2,797 | 0.7 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| Shreedevi-nice | Shreedevi Patil | AF | 1,886 | 8.8% | 12,071 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| meghabiradar05 | Megha Biradar | AF-Lean | 1,727 | 12.5% | 10,131 | 0.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| prashasti-jain | Prashasti Jain | AF-Lean | 1,562 | 7.2% | 12,206 | 0.1 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| pdevle | Pratik Devle | AF-Lean | 1,478 | 6.3% | 10,057 | 0.1 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| pratikpawar12 | Pratik Pawar | AF-Lean | 250 | 4.1% | 815 | 0.3 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| amol-doke | Amol Doke | Inline | 10 | 22.2% | 2,528 | 0.0 | 2 | 0 | 2 | **4** | R=0+Prem>500 | **C** |
| mohitbaghelnice | Mohit Baghel | AF-Lean | 3 | 0.0% | 2,393 | 0.0 | 1 | 0 | 3 | **4** | R=0+Prem>500 | **C** |
| thakraln | Nishtha Thakral | AF-Lean | 806 | 0.0% | 13,562 | 0.1 | 1 | 0 | FB(2) | **3** | R=0+Prem>500 | **C** |
| moadzughul | Moad Alzughul | AF-Lean | 3,409 | 2.4% | 3,072 | 1.1 | 0 | 0 | 3 | **3** | R=0+Prem>500 | **C** |
| ssnikam | Sanket Nikam | (no usage) | 0 | — | 0 | — | 0 | 0 | 3 | **3** | — | **C** |
| giteshsawant | Gitesh Sawant | AF-Lean | 1,369 | 2.2% | 8,585 | 0.2 | 1 | 0 | 1 | **2** | — | **D** |

---

## 4. Score Change Analysis — CP8 vs CP9

### Users Who Improved (CP8 → CP9)

| User | CP8 Tier | CP9 Tier | C Change | R Change | Q Change | Total Change | Driver |
|---|---|---|---|---|---|---|---|
| abhijeetk268 | B (est.) | **A** | 2→2 | 3→1 | 3→3 | +1 (via promo) | New entrant, momentum promotion applied |
| dannycadima | Not in CP8 | **A** | — | — | — | New | New entrant; lean spend + ReqEff 11.0 |
| mshivarkar | C (4) | **C (4)** | 1→1 | 0→0 | 3→3 | 0 | Stable at C; LoC doubled (+100%) but override blocks promo |
| dsuraj25 | C (5) | **C (6→C cap)** | 2→3 | 0→0 | 3→3 | 0 (cap) | C score improved; override still caps at C |
| trunalgawade | C (6) | **C (6→C cap)** | 3→3 | 0→0 | 3→3 | 0 | Stable; LoC still growing |
| luisalvatierra | C (6) | **C (6→C cap)** | 3→3 | 0→0 | 3→3 | 0 | Stable at cap; LoC doubled CP8→CP9 |

**Key observation:** No user genuinely moved to a higher tier under the same framework rules. abhijeetk268's Tier A is a momentum promotion from Tier B (new entrant, first appearing at CP9). The framework structure locks all outlier-premium users at Tier C regardless of C or Q score gains.

### Users Who Regressed (CP8 → CP9)

| User | CP8 Tier | CP9 Tier | C Change | R Change | Q Change | Net | Driver |
|---|---|---|---|---|---|---|---|
| rpawar-nice | **A** (CP8) | **C** (CP9) | 3→1 | 2→1 | 3→FB(2) | −3 | Reclassified to AF under CP9 rules; LoC flat; R penalty from premium growth 850→879 (minor); C drops under new AF-Lean rules |
| Vyankatesh95 | **A** (CP8/prior) | **C** (CP9) | 3→3 | 3→0 | 3→3 | −3 | R collapsed: premium grew from ~450 to 4,118 (>1,700 outlier threshold crossed) |
| Vitthal-Nice | **A** (CP8/prior) | **C** (CP9) | 2→2 | 1→0 | 3→3 | −1 | R fell: premium grew from ~413 to 2,393 (crossed outlier threshold) |
| Akale23 | **A** (CP8/prior) | **C** (CP9) | 3→3 | 0→0 | 3→3 | 0 (tier drop) | Same score; but prior CP8 used different rules that didn't apply Override 2 consistently |
| mshnayderman | C (6→C) | C (5→C) | 3→3 | 0→0 | 3→2 | −1 | Q dropped slightly (50% merge rate → 2pts only, lost time bonus) |

**Note on rpawar-nice:** The apparent regression from A to C is partly methodological. Under CP7–CP8 rules, rpawar-nice scored A using the Agent Contribution % classification + prior R rules. Under CP9 SuggEff+%Accept rules, ReqEff of 9.9 only qualifies for R=1 (5–10 bracket), and the AF classification gives C=1 (ReqEff < 15, no LoC growth). The user's actual output has not declined — 8,662 LoC remains the highest efficiency-adjusted output on the team. This is a classification reclassification artifact, not a performance regression.

### Users Who Remained Stable (CP8 → CP9)

The majority of the team — 30 of 37 users — scored identically or within ±1 point at the same tier. The Override 2 cap creates structural stability: once R=0 and Premium > 500, scores cannot rise above Tier C regardless of C or Q improvements. This makes most of the team "stuck" at Tier C not by performance stagnation but by the override mechanism.

---

## 5. Premium Spend Escalation Timeline

### When Users Crossed the 1,700 Outlier Threshold

The outlier threshold (Premium > 1,700) triggers the −1 R penalty AND activates Override 2 (R=0 + Prem > 500 → cap at Tier C). Understanding when users crossed this threshold explains when their tier collapsed.

| User | CP4 May11 Prem (est.) | CP5 May18 Prem (est.) | CP6 Jun3 Prem (est.) | CP7 Jun8 Prem (est.) | CP8 Jun12 Prem | CP9 Jun23 Prem | First Outlier CP | Peak Spend |
|---|---|---|---|---|---|---|---|---|
| nilesht-19 | ~3,988 | ~15,000 | ~22,000 | 23,108 | 30,437 | **32,332** | CP4 (May11) | CP9 |
| Prathmesh-Ranadive | ~4,001 | ~8,000 | ~10,000 | 10,733 | ~10,733 | **31,420** | CP4 (May11) | CP9 |
| PradnyeshSalunke | ~3,754 | ~8,000 | ~9,000 | 9,892 | 15,719 | **20,544** | CP4 (May11) | CP9 |
| mshnayderman | ~3,000 | ~3,500 | ~4,500 | 5,419 | 5,419 | **5,452** | CP4 (May11) | CP9 |
| Kranti-nice | ~1,800 | ~2,500 | ~3,000 | ~1,250 | 11,979 | **35,537** | CP4–CP5 est. | CP9 |
| amol-salunkhe | ~2,000 | ~4,000 | ~5,000 | 5,309 | 11,150 | **20,170** | CP4 est. | CP9 |
| thakraln | 0 | 0 | ~5,000 | 11,112 | ~12,000 | **13,562** | CP6 (Jun3) | CP9 |
| trunalgawade | ~200 | ~400 | ~800 | 10,863 | 16,265 | **18,720** | CP7 (Jun8) | CP9 |
| Shubhamfulzele28 | 0 | 0 | 0 | ~120 | 13,831 | ~13,831 | CP8 (Jun12) | CP8 |
| tusharpatil166719 | ~200 | ~300 | ~500 | ~100 | 10,754 | **35,886** | CP8 (Jun12) | CP9 |
| sskalaskar | ~100 | ~200 | ~500 | ~85 | ~11,000 | **16,897** | CP8 (Jun12) | CP9 |
| Vyankatesh95 | ~115 | ~200 | ~300 | ~115 | ~450 | **4,118** | CP9 (Jun23) | CP9 |
| Vitthal-Nice | ~200 | ~300 | ~400 | ~411 | ~413 | **2,393** | CP9 (Jun23) | CP9 |
| jayesh-rai | ~100 | ~150 | ~200 | ~130 | ~852 | **1,997** | CP9 (Jun23) | CP9 |
| luisalvatierra | ~500 | ~700 | ~800 | ~900 | ~9,477 | **9,542** | CP8 (Jun12) | CP9 |
| chris-haun | ~200 | ~300 | ~400 | ~300 | ~12,000 | **12,535** | CP8 (Jun12) | CP9 |
| mshivarkar | ~100 | ~100 | ~200 | ~400 | ~8,000 | **17,029** | CP8 (Jun12) | CP9 |
| vishal-tad | ~100 | ~200 | ~300 | ~500 | ~9,000 | **9,301** | CP8 (Jun12) | CP9 |
| mfield1 | ~300 | ~400 | ~500 | ~650 | ~1,813 | **3,133** | CP8 (Jun12) | CP9 |
| Shreedevi-nice | ~100 | ~200 | ~300 | ~150 | ~12,000 | **12,071** | CP8 (Jun12) | CP9 |
| abhishekhole-nice | ~100 | ~200 | ~300 | ~600 | ~10,000 | **4,416** | CP8 (Jun12) | CP9 |
| prashasti-jain | 0 | ~100 | ~200 | ~150 | ~12,000 | **12,206** | CP8 (Jun12) | CP9 |
| meghabiradar05 | ~100 | ~200 | ~300 | ~600 | ~10,000 | **10,131** | CP8 (Jun12) | CP9 |
| pdevle | ~100 | ~100 | ~200 | ~200 | ~10,000 | **10,057** | CP8 (Jun12) | CP9 |
| giteshsawant | 0 | 0 | 0 | ~200 | ~8,500 | **8,585** | CP8 (Jun12) | CP9 |
| dsuraj25 | ~50 | ~100 | ~200 | ~200 | ~8,000 | **9,893** | CP8 (Jun12) | CP9 |
| sskalaskar | ~85 | ~100 | ~200 | ~85 | ~7,434 | **16,897** | CP8 (Jun12) | CP9 |
| suhas-kakde | ~100 | ~100 | ~200 | ~100 | ~2,500 | **2,797** | CP8 (Jun12) | CP9 |
| moadzughul | ~300 | ~400 | ~700 | ~700 | ~3,000 | **3,072** | CP7–CP8 est. | CP9 |

### Threshold Crossing Wave Summary

| Wave | Checkpoint | New Outlier Users | Cumulative Outlier Count | R Collapse Event |
|---|---|---|---|---|
| Wave 1 (Early Adopters) | CP4 May 11 | nilesht-19, Prathmesh-Ranadive, PradnyeshSalunke, mshnayderman, amol-salunkhe | 5 | First R=0 wave — 5 major users |
| Wave 2 (Mid-Q2) | CP5–CP6 | Kranti-nice, thakraln | +2 → 7 | Kranti spike from ~1,250 to 11,979 |
| Wave 3 (Jun 8 Spike) | CP7 Jun8 | trunalgawade | +1 → 8 | trunalgawade: 800→10,863 in one window |
| Wave 4 (Jun 12 Explosion) | CP8 Jun12 | Shubhamfulzele28, tusharpatil166719, sskalaskar, luisalvatierra, chris-haun, mshivarkar, vishal-tad, mfield1, abhishekhole-nice, prashasti-jain, meghabiradar05, pdevle, giteshsawant, dsuraj25 | +14 → 22 | Largest single-window spike: 14 new outliers |
| Wave 5 (Jun 23) | CP9 Jun23 | Vyankatesh95, Vitthal-Nice, jayesh-rai, mohitbaghelnice, amol-doke, pratikpawar12, suhas-kakde, Shreedevi-nice, jkumbhar | +9 → 31 | Remaining mid-tier users cross outlier line |

**Critical finding:** The CP7→CP8 window (Jun 8–12, only 4 days) added 14 new outlier users. This represents the sharpest single escalation in the Q2 period — 14 users went from sub-1,700 premium to >1,700 in under one week.

---

## 6. R Score Degradation — Tracing When Premium Spikes Killed ROI

The R score is the most volatile pillar. A user can drop from R=3 to R=0 in a single checkpoint if premium crosses 1,700 and ReqEff drops below 5. This section traces each budget crisis user's R score trajectory.

### R Score Trajectory — Top Budget Crisis Users

| User | R at CP4 | R at CP5 | R at CP6 | R at CP7 | R at CP8 | R at CP9 | First R=0 CP | Net R Change |
|---|---|---|---|---|---|---|---|---|
| nilesht-19 | 0 | 0 | 0 | 0 | 0 | 0 | CP4 | Persistent crisis |
| Prathmesh-Ranadive | 0 | 0 | 0 | 0 | 0 | 0 | CP4 | Persistent crisis |
| PradnyeshSalunke | 0 | 0 | 0 | 0 | 0 | 0 | CP4 | Persistent crisis |
| mshnayderman | 0 | 0 | 0 | 0 | 0 | 0 | CP4 | Persistent crisis |
| amol-salunkhe | 3 | 3 | 1 | 0 | 0 | 0 | CP7 | Degraded from lean bonus |
| Kranti-nice | 2 | 0 | 0 | 2 | 0 | 0 | CP5 (then recovered CP7, recollapsed CP8) | Volatile |
| rpawar-nice | 3 | 3 | 3 | 3 | 2 | 1 | Never 0 | Progressive decline |
| trunalgawade | 1 | 1 | 1 | 0 | 0 | 0 | CP7 | Degraded |
| Vyankatesh95 | 3 | 2 | 0 | 3 | 0 | 0 | CP6 (recovered CP7, recollapsed CP8) | Volatile |
| Vitthal-Nice | 2 | 2 | 2 | 2 | 1 | 0 | CP9 | Slow degradation |
| jayesh-rai | 2 | 2 | 2 | 2 | 0 | 0 | CP8 | Degraded |
| mfield1 | 2 | 2 | 2 | 2 | 0 | 0 | CP8 | Degraded |
| jkumbhar | 2 | 1 | 1 | 1 | 0 | 0 | CP8 | Slow degradation |
| chris-haun | 1 | 0 | 0 | 0 | 0 | 0 | CP5 | Early loss |
| abhijeetk268 | 2 | 1 | 1 | 3 | 3 | 1 | Never 0 | Volatile but positive |
| suhas-kakde | 1 | 1 | 0 | 0 | 0 | 0 | CP6 | Degraded |
| meghabiradar05 | 2 | 3 | 1 | 0 | 0 | 0 | CP7 | Peak then collapse |
| moadzughul | 2 | 3 | 2 | 0 | 0 | 0 | CP7 | Volatile then 0 |

### R=0 User Count by Checkpoint

| Checkpoint | Users with R=0 | % of 37-person team | Threshold Event |
|---|---|---|---|
| CP4 May 11 | ~8 | 22% | First wave of outlier premium users |
| CP5 May 18 | ~10 | 27% | Kranti-nice and others joining R=0 |
| CP6 Jun 3 | ~14 | 38% | Continued spread |
| CP7 Jun 8 | ~16 | 43% | trunalgawade, jayesh-rai, amol-salunkhe crossing over |
| **CP8 Jun 12** | **~33** | **89%** | **Catastrophic: 14 new outlier crossings in 4 days** |
| **CP9 Jun 23** | **~34** | **92%** | **Near-universal R=0; only rpawar-nice, copilotshree, abhijeetk268, dannycadima, kbajaj-nice at R>0** |

### The CP7→CP8 Collapse — A Structural Break

The most dramatic R score degradation event in the Q2 period occurred between Jun 8 and Jun 12 (4 days). In this window:
- 17 users went from R > 0 to R = 0
- The team-wide R=0 rate jumped from 43% to 89%
- Combined premium spend by these 17 users crossed ~150,000 new requests in 4 days

This is not gradual adoption pressure. It represents a platform-level behavioral shift — likely triggered by the broader rollout of GitHub Copilot agent sessions (where each iteration of a long session can generate dozens of premium requests). The root cause investigation recommended in the CP8 report remains open at CP9.

---

## 7. Q Score Evolution

Quality score behavior across checkpoints reflects both PR data availability and actual merge performance.

### Q Score Data Availability Timeline

| CP | Q Measurement Method | Quality Signal | Reliability |
|---|---|---|---|
| CP1–CP3 | Not measured | None | N/A |
| CP4–CP7 | Team-level proxy: Q=3 for active contributors (LoC > 100), Q=0 for inactive | Approximate | Low |
| CP7–CP8 | Team-level proxy: same rules; individual PR data not yet per-user | Approximate | Low |
| **CP9** | **Per-user PR data (Jun 21, 2026 snapshot)** | **Actual** | **High** |

### CP9 Q Score Distribution — First Per-User Measurement

| Q Score | Users | % | PR Characteristic |
|---|---|---|---|
| **Q = 3** | 29 | 78% | ≥ 80% merge rate + reviews ≥1/PR (or time ≤72h) |
| **Q = FB(2)** | 4 | 11% | Active users with no PR data captured (rpawar-nice, copilotshree, thakraln, dannycadima) |
| **Q = 2** | 3 | 8% | mshnayderman (50% merge, long TTM), jkumbhar (63.2% merge), amol-doke (50% merge) |
| **Q = 1** | 1 | 3% | giteshsawant (0% merge rate, time bonus only) |
| **Q = 0** | 0 | 0% | No in-scope user has Q=0 at CP9 |

### PR Merge Rate Analysis — CP9 Snapshot

**Best-in-class (100% merge rate):**
amol-salunkhe (8/8), Prathmesh-Ranadive (24/24), luisalvatierra (10/10), PradnyeshSalunke (8/8), mshivarkar (11/11), Vyankatesh95 (16/16), abhishekhole-nice (14/14), trunalgawade (1/1), Vitthal-Nice (7/7), jayesh-rai (17/17), tusharpatil166719 (4/4), suhas-kakde (27/27, 93.1%), meghabiradar05 (5/5), pdevle (7/7), dsuraj25 (1/1), pratikpawar12 (9/9), mohitbaghelnice (1/1), kbajaj-nice (2/2)

**Below-benchmark (merge rate < 80%):**

| User | PR# | Merged | Merge% | Issue |
|---|---|---|---|---|
| giteshsawant | 1 | 0 | 0% | 1 PR opened, not merged — possible open or rejected |
| jkumbhar | 19 | 12 | 63.2% | 7 unmerged PRs out of 19 — review loop issues |
| mshnayderman | 2 | 1 | 50% | Very low PR volume; 1 unmerged |
| amol-doke | 8 | 4 | 50% | New entrant; 4 of 8 PRs not merged |

**Fastest pipelines (time-to-merge ≤ 24h):**

| User | Avg TTM | PRs | Merge% | Signal |
|---|---|---|---|---|
| pratikpawar12 | 2h 16m | 9 | 100% | Fastest pipeline on team |
| amol-salunkhe | 2h 48m | 8 | 100% | Second fastest; strong review throughput |
| mohitbaghelnice | 0h 2m | 1 | 100% | Single PR, trivial TTM (likely trivial change) |
| abhishekhole-nice | 16h 26m | 14 | 100% | Fast + high volume |
| Prathmesh-Ranadive | 16h 5m | 24 | 100% | Fast pipeline, highest PR volume in top-3 |
| Shreedevi-nice | 24h 23m | 15 | 93.3% | Fast + consistent |

**Longest pipelines (TTM > 150h):**

| User | Avg TTM | PRs | Merge% | Signal |
|---|---|---|---|---|
| moadzughul | 361h 1m | 45 | 95.6% | 15 days avg TTM — complex cross-team PRs likely |
| mfield1 | 159h 6m | 33 | 93.9% | 6.6 days — consistent with external review cycles |
| luisalvatierra | 137h 46m | 12 | 83.3% | 5.7 days — cross-timezone or review bottleneck |
| jkumbhar | 281h 35m | 19 | 63.2% | 11.7 days avg + poor merge rate = systemic issue |
| meghabiradar05 | 217h 26m | 5 | 100% | Long TTM but all merged — review queue delay |

### Q Score vs R Score Divergence Observation

The most significant Q2 pattern is the **Q-R divergence**: the team's PR quality is excellent (Q=3 for 78% of users) while the ROI score has collapsed (R=0 for 92% of users). This means the team is:
- Writing good code (high merge rates)
- Getting it reviewed (reviews ≥ 1/PR for most users)
- Shipping it quickly (many users < 72h TTM)

But consuming premium requests at rates 10–100× the benchmark efficiency. The quality of the output is not in question. The cost of producing it is.

---

## 8. Cap Override Cases — Full Inventory

### Override 2: R=0 AND Premium > 500 → Cannot Exceed Tier C

At CP9, this override affects **32 of 37** in-scope developers. These are the users where a higher raw score is suppressed by the cap:

**Users where Override 2 reduces a would-be Tier B to Tier C (raw score 5–6):**

| User | C | R | Q | Raw Score | Would Be | Override Cap | Prem | ReqEff |
|---|---|---|---|---|---|---|---|---|
| luisalvatierra | 3 | 0 | 3 | 6 | B | C | 9,542 | 1.3 |
| nilesht-19 | 3 | 0 | 3 | 6 | B | C | 32,332 | 0.2 |
| Vyankatesh95 | 3 | 0 | 3 | 6 | B | C | 4,118 | 1.0 |
| trunalgawade | 3 | 0 | 3 | 6 | B | C | 18,720 | 0.1 |
| Akale23 | 3 | 0 | 3 | 6 | B | C | 4,237 | 0.6 |
| dsuraj25 | 3 | 0 | 3 | 6 | B | C | 9,893 | 0.1 |
| Prathmesh-Ranadive | 2 | 0 | 3 | 5 | B | C | 31,420 | 1.1 |
| mshnayderman | 3 | 0 | 2 | 5 | B | C | 5,452 | 5.1 |
| Vitthal-Nice | 2 | 0 | 3 | 5 | B | C | 2,393 | 1.1 |
| jkumbhar | 3 | 0 | 2 | 5 | B | C | 2,110 | 0.9 |

**Total override-B-to-C suppression: 10 users.** If the Override 2 rule were relaxed for these 10, the team's Tier B count would jump from 2 to 12.

**Users where Override 2 confirms an already-4 score as Tier C (no change in outcome, but override still active):**

amol-salunkhe (4), Kranti-nice (4), chris-haun (4), mfield1 (4), PradnyeshSalunke (4), mshivarkar (4), vishal-tad (4), sskalaskar (4), abhishekhole-nice (4), jayesh-rai (4), tusharpatil166719 (4), suhas-kakde (4), Shreedevi-nice (4), meghabiradar05 (4), prashasti-jain (4), pdevle (4), pratikpawar12 (4), amol-doke (4), mohitbaghelnice (4), moadzughul (3), thakraln (3)

### Override 1: Q=0 → Cannot Be Tier A

Not triggered at CP9. No user has Q=0 with a raw score ≥ 7. giteshsawant has Q=1 but a total score of only 2 (Tier D) — Override 1 would not change the outcome even if triggered.

### Override 3: Momentum > 100% → One-Tier Promotion

Override 3 was applied to **abhijeetk268** (new entrant CP9, first appearance, infinite momentum) — raw score 6 (Tier B) promoted to Tier A. This is the only promotion granted at CP9.

Blocked promotions (momentum > 100% but Override 2 also applies):

| User | CP8 LoC | CP9 LoC | Growth | Override 2 Block | Outcome |
|---|---|---|---|---|---|
| mshivarkar | 2,097 | 4,201 | +100.3% | Yes (Prem 17,029) | Blocked |
| thakraln | ~0 | 806 | New entrant | Yes (Prem 13,562) | Blocked |
| dsuraj25 | ~0 | 1,169 | New entrant | Yes (Prem 9,893) | Blocked |
| pratikpawar12 | ~0 | 250 | New entrant | Yes (Prem 815) | Blocked |
| amol-doke | ~0 | 10 | New entrant | Yes (Prem 2,528) | Blocked |
| mohitbaghelnice | ~0 | 3 | Trivial | Yes (Prem 2,393) | Blocked |
| kbajaj-nice | ~0 | 5 | New entrant | No | Not applied (LoC trivially small) |
| dannycadima | ~0 | 34 | New entrant | No | Already A (7); no effect |

---

## 9. LoC vs Premium Trajectory — Budget Crisis Users

The following textual analysis tracks the divergence between LoC output and premium consumption for the six highest-spend users. A healthy user should show LoC and Premium growing at similar rates (ReqEff stable). Budget crisis users show Premium growing far faster than LoC.

### amol-salunkhe — Premium Overtook LoC (CP6 onwards)

```
CP1: LoC=31      Prem=~30      ReqEff=~1.0  [Early, very low activity]
CP2: LoC=31      Prem=~30      ReqEff=~1.0  [No change]
CP3: LoC=2,210   Prem=~500     ReqEff=~4.4  [LoC burst; premium low; R=1]
CP4: LoC=17,155  Prem=~2,000   ReqEff=~8.6  [Strong growth; premium rising; R=1]
CP5: LoC=28,911  Prem=~4,000   ReqEff=~7.2  [LoC leads; premium catching up; R=1]
CP6: LoC=30,486  Prem=~5,000   ReqEff=~6.1  [LoC slowing; premium continuing; R=1]
CP7: LoC=34,037  Prem=5,309    ReqEff=6.4   [Lean bonus still; R=1]
CP8: LoC=41,008  Prem=11,150   ReqEff=3.7   [DIVERGENCE: premium +110%; LoC +21%; R=0]
CP9: LoC=43,585  Prem=20,170   ReqEff=2.2   [Premium doubles again; LoC +6%; R=0]
```
**Diagnosis:** Until CP7, amol-salunkhe was a productive user (ReqEff 6–8). The CP7→CP8 and CP8→CP9 windows show premium growing 5× faster than LoC. Likely running long unproductive agent sessions. LoC is still the highest on the team — the user is producing output — but the cost per unit of output is exploding.

---

### Kranti-nice — Volatile and Worsening

```
CP1: LoC=2,148   Prem=~500     ReqEff=~4.3  [Moderate; R=1]
CP2: LoC=2,148   Prem=~500     ReqEff=~4.3  [No change]
CP3: LoC=3,259   Prem=~900     ReqEff=~3.6  [Slow growth; R=0]
CP4: LoC=3,259   Prem=~1,800   ReqEff=~1.8  [Flat LoC; premium crossing outlier; R=0]
CP5: LoC=7,076   Prem=~2,500   ReqEff=~2.8  [LoC burst; but R=0 continues]
CP6: LoC=27,733  Prem=~3,000   ReqEff=~9.2  [Major LoC burst; R still 0 due to prem>1700]
CP7: LoC=27,733  Prem=~1,250   ReqEff=~22.2 [Premium dropped?? Anomaly; R=2]
CP8: LoC=31,645  Prem=11,979   ReqEff=~2.6  [Premium exploded 858%; LoC +14%; R=0]
CP9: LoC=37,978  Prem=35,537   ReqEff=1.1   [Premium tripled; LoC +20%; R=0]
```
**Diagnosis:** Kranti-nice showed a brief efficiency window at CP7 (possible measurement period boundary effect). By CP8–CP9, premium is expanding far faster than LoC. The user's absolute LoC is second-highest on the team (37,978) — output quality is real — but premium cost is the highest on the team at 35,537. At ReqEff 1.1, every 1 LoC produced costs ~0.9 premium requests.

---

### nilesht-19 — Earliest and Most Persistent Crisis

```
CP1: LoC=1,287   Prem=~1,000   ReqEff=~1.3  [Already low efficiency]
CP2: LoC=1,567   Prem=~1,200   ReqEff=~1.3  [Slow LoC growth]
CP3: LoC=3,598   Prem=~2,000   ReqEff=~1.8  [LoC improving but prem already outlier]
CP4: LoC=4,908   Prem=~3,988   ReqEff=~1.2  [R=0; prem now well above 1700]
CP5: LoC=5,065   Prem=~15,000  ReqEff=~0.3  [Catastrophic: prem 4× LoC growth rate]
CP6: LoC=5,293   Prem=~22,000  ReqEff=~0.2  [Near-flat LoC; premium continuing]
CP7: LoC=7,160   Prem=23,108   ReqEff=0.3   [Small LoC burst; premium relentless]
CP8: LoC=7,346   Prem=30,437   ReqEff=0.2   [Essentially flat LoC; +32% premium]
CP9: LoC=7,354   Prem=32,332   ReqEff=0.2   [8 new LoC in 11 days; 1,895 new premium requests]
```
**Diagnosis:** nilesht-19 is the earliest and most severe case. Premium crossed 1,700 at CP3–CP4 and has never recovered. Since CP5, the user has generated only ~2,289 LoC against ~17,000 new premium requests — a 7:1 waste ratio. Immediate agent session audit required.

---

### tusharpatil166719 — Late Entrant, Extreme Spike

```
CP1-CP6: LoC=381→1,798  Prem=<500     [Modest user; lean spend throughout]
CP7: LoC=1,798   Prem=~100     ReqEff=~18   [Still lean; efficient]
CP8: LoC=1,798   Prem=10,754   ReqEff=0.2   [EXPLOSION: premium +10,654% in 4 days]
CP9: LoC=2,200   Prem=35,886   ReqEff=0.1   [Premium tripled again; LoC +22%; worst R in team]
```
**Diagnosis:** tusharpatil166719 is the most extreme single-window spike case. From <500 premium to 35,886 premium in 6 weeks (CP7→CP9). LoC grew only +402. The user was a lean, efficient user through CP7 — something fundamentally changed in their Copilot usage pattern at CP8. Likely switched from inline suggestions to intensive agent sessions without adjusting session management.

---

### Prathmesh-Ranadive — High LoC, Extreme Cost

```
CP1: LoC=1,373   Prem=~800     ReqEff=~1.7
CP2: LoC=1,373   Prem=~800     ReqEff=~1.7
CP3: LoC=1,848   Prem=~1,500   ReqEff=~1.2
CP4: LoC=8,783   Prem=~4,001   ReqEff=~2.2  [First outlier; R=0]
CP5: LoC=9,489   Prem=~8,000   ReqEff=~1.2  [Premium growing faster than LoC]
CP6: LoC=20,436  Prem=~10,000  ReqEff=~2.0  [LoC burst; efficiency marginally better]
CP7: LoC=27,052  Prem=10,733   ReqEff=~2.5  [Strong LoC; but still R=0]
CP8: LoC=27,052  Prem=~10,733  ReqEff=~2.5  [Flat LoC; same premium]
CP9: LoC=35,091  Prem=31,420   ReqEff=1.1   [Premium nearly tripled; LoC +30%]
```
**Diagnosis:** Prathmesh-Ranadive produces significant LoC (third highest on team at 35,091) and has strong PR quality (24/24 merged, 100% rate, 16h TTM). The cost problem is exclusively in premium consumption. At ReqEff 1.1, the user produces slightly more than 1 LoC per request — technically positive but 10× worse than the benchmark ReqEff of 10.

---

### mshnayderman — Moderate Crisis, Structural Plateau

```
CP1-CP3: LoC=~20,000  Prem=~500    [High LoC baseline; lean; R=3]
CP4: LoC=22,268  Prem=~3,000  ReqEff=~7.4  [Prem crossed outlier; R=0]
CP5: LoC=22,268  Prem=~3,500  ReqEff=~6.4  [Flat LoC; R=0]
CP6: LoC=24,387  Prem=~4,500  ReqEff=~5.4  [Modest LoC; R=0]
CP7: LoC=27,539  Prem=5,419   ReqEff=5.1   [LoC burst; still R=0]
CP8: LoC=27,539  Prem=5,419   ReqEff=5.1   [FLAT: zero LoC growth; same premium]
CP9: LoC=27,539  Prem=5,452   ReqEff=5.1   [Still zero new LoC; +33 premium requests]
```
**Diagnosis:** mshnayderman is structurally different from the others — this is a plateau case, not an explosive spend case. Premium stabilized at ~5,400. LoC stopped growing after CP7. The user was the highest LoC holder through CP3 (20,399 from the start) but has added only 7,140 LoC in 64 days. With 0 new LoC at CP8–CP9 and R=0 from outlier premium, this user needs a workflow refresh, not a cost audit.

---

## 10. Q2 CRQC Summary and Q3 Entry Readiness

### Q2 Closing State — CP9 Snapshot (Jun 23, 2026)

| Metric | Value | Context |
|---|---|---|
| In-scope developers | 37 | 15+1 excluded per ignore list |
| Total LoC produced (team) | ~329,000 | Dominated by top 5: amol (43K), Kranti (38K), Prathmesh (35K), mshnayderman (27K), luisalvatierra (12K) |
| Total premium consumed (team) | ~371,000 | Top 5 consumers: tusharpatil (35.9K), Kranti (35.5K), nilesht-19 (32.3K), Prathmesh (31.4K), amol (20.2K) |
| Team avg ReqEff | ~0.9 | Below break-even (1.0); the team produces less than 1 LoC per premium request on average |
| PR merge rate | ~90% | Strong code quality culture |
| Total PRs merged (dataset) | ~514 | Solid throughput |
| Tier A users | 2 | 1 data-artifact (dannycadima, thin sample), 1 momentum promo (abhijeetk268) |
| Tier B users | 2 | copilotshree (R=3 efficiency), kbajaj-nice (lean spend) |
| Tier C users | 32 | 86% of team; 30/32 are override-capped |
| Tier D users | 1 | giteshsawant (0% merge rate, outlier premium) |
| Tier E users | 0 | No zero-score users |
| R=0 users | 34 | 92% of team |
| Override 2 active | 32 | 86% of team |
| Users with ReqEff > 5 | 3 | rpawar-nice (9.9), copilotshree (14.8), mshnayderman (5.1) |
| Users with lean spend (Prem ≤ 500) | 5 | copilotshree (340), abhijeetk268 (451), kbajaj-nice (6), dannycadima (3), kbajaj-nice |

### Q2 CRQC Score Distribution Evolution

The following shows how the tier distribution evolved across all 9 checkpoints. CP1–CP7 tiers are estimated from C+R progression; CP8 and CP9 use full CRQC scores.

| Tier | CP4 (est.) | CP5 (est.) | CP6 (est.) | CP7 (est.) | CP8 | CP9 |
|---|---|---|---|---|---|---|
| A (7–9) | ~5 | ~4 | ~4 | ~7 | ~2 | 2 |
| B (5–6) | ~8 | ~7 | ~5 | ~5 | ~3 | 2 |
| C (3–4) | ~12 | ~14 | ~18 | ~18 | 29 | 32 |
| D (1–2) | ~7 | ~7 | ~6 | ~5 | 2 | 1 |
| E (0) | ~5 | ~5 | ~4 | ~2 | 1 | 0 |

**The structural story:** The team began Q2 with ~5 Tier A users and a relatively spread distribution. As premium spend escalated through Q2, the distribution compressed heavily into Tier C. By CP9, 86% of the team is in Tier C — not because output declined (LoC is generally growing) but because premium spend crossed the outlier threshold for nearly everyone.

### The Five Remaining R > 0 Users — Q3 Benchmarks

These are the only users who maintained positive R scores at CP9:

| User | R Score | ReqEff | Premium | LoC | What They Do Right |
|---|---|---|---|---|---|
| copilotshree | **3** | 14.8 | 340 | 5,013 | Lean spend (340), ReqEff in 10–20 bracket. Gold standard for budget discipline. |
| dannycadima | **3** | 11.0 | 3 | 34 | Ultra-lean (3 premium requests). Statistically trivial but framework-compliant. |
| rpawar-nice | **1** | 9.9 | 879 | 8,662 | ReqEff in 5–10 bracket; premium not yet outlier. Declining from peak R=3 at CP5. |
| abhijeetk268 | **1** | 1.5 | 451 | 656 | Lean spend (451 ≤ 500); poor ReqEff but lean bonus saves R=1. |
| kbajaj-nice | **1** | 0.8 | 6 | 5 | Ultra-lean (6 premium requests); poor ReqEff but lean bonus saves R=1. |

**Benchmark target for Q3:** Any user who wants to maintain or achieve R > 0 must either:
- Keep premium ≤ 500 (lean bonus path), OR
- Achieve ReqEff ≥ 5 with premium ≤ 1,700 (moderate efficiency path), OR
- Achieve ReqEff > 10 even if premium is above 500

The only path to R = 3 under the current team's usage patterns is the lean+efficiency combination: ReqEff in 10–20 bracket + Prem ≤ 500. copilotshree and dannycadima demonstrate this at CP9.

### Q3 Entry Readiness Assessment

**Definition:** A user is Q3-ready if they can plausibly achieve Tier B or above in Q3 given their CP9 trajectory and known behavioral changes.

**Tier A candidates for Q3:**

| User | Current Tier | Path to Tier A | Blocker | Likelihood |
|---|---|---|---|---|
| rpawar-nice | C | ReqEff 9.9 → push above 10, get PRs into dataset, maintain lean spend → R=2+, C=2+, Q=3 = 7 | No PR data captured; LoC flat | Medium — requires PR data fix and LoC restart |
| copilotshree | B | Identity confirmed + PR data added → Q=3 actual + existing R=3 + C=2 = 7–8 | Identity unconfirmed; no PR data | High if identity resolved |
| abhijeetk268 | A (momentum) | Maintain efficiency, grow LoC, stay lean | Premium growth — if crosses 500, R drops to 0 | Medium — must stay lean |

**Tier B candidates for Q3 (users who could escape Override 2):**

The following users have Q=3 and C=3 but are capped at Tier C by Override 2. If they reduce premium below 1,700 AND achieve ReqEff ≥ 5, they qualify for Tier B on raw score alone (3+1+3=7 → A; or 3+0+3=6 → B if R stays 0 but override lifted).

| User | Current | Raw Score (without override) | Required Change | Premium Gap |
|---|---|---|---|---|
| luisalvatierra | C (capped from B) | 6 | Premium 9,542 → ≤1,700; ReqEff ≥5 | Need −7,842 prem AND +3× ReqEff |
| nilesht-19 | C (capped from B) | 6 | Premium 32,332 → ≤1,700; ReqEff ≥5 | Extreme gap — structural issue |
| Vyankatesh95 | C (capped from B) | 6 | Premium 4,118 → ≤1,700 | Need −2,418 prem |
| trunalgawade | C (capped from B) | 6 | Premium 18,720 → ≤1,700 | Extreme gap |
| Akale23 | C (capped from B) | 6 | Premium 4,237 → ≤1,700 | Need −2,537 prem |
| dsuraj25 | C (capped from B) | 6 | Premium 9,893 → ≤1,700 | Need −8,193 prem |
| Prathmesh-Ranadive | C (capped from B) | 5 | Premium 31,420 → ≤1,700 | Extreme gap |
| mshnayderman | C (capped from B) | 5 | Premium 5,452 → ≤1,700 | Need −3,752 prem; also need Q fix |
| Vitthal-Nice | C (capped from B) | 5 | Premium 2,393 → ≤1,700 | Need −693 prem — most achievable gap |

**Observation:** Vitthal-Nice requires the smallest premium reduction to escape Override 2 — only 693 fewer premium requests would bring them below 1,700. At their current trajectory, this may be achievable by managing agent session count in Q3. Vyankatesh95 (2,418 gap) and Akale23 (2,537 gap) are the next most achievable.

---

## Appendix — Override 2 Cap Visualization (Textual)

**How the same C+Q score maps to different tiers depending on R and Override:**

```
C=3, Q=3 = 6 raw points

  R=3 (lean): Total 9 → Tier A   [copilotshree, dannycadima path]
  R=2:        Total 8 → Tier A
  R=1:        Total 7 → Tier A
  R=0, Prem ≤ 500: Total 6 → Tier B  [no override]
  R=0, Prem > 500: Total 6 → CAPPED at Tier C  [Override 2 active]
               ↑
           This is where 10 users are trapped at CP9
           (luisalvatierra, nilesht-19, Vyankatesh95, trunalgawade,
            Akale23, dsuraj25, Prathmesh-Ranadive, mshnayderman,
            Vitthal-Nice, jkumbhar)
```

**The premium spend number is the ONLY variable separating these users from Tier B.** Their C scores are maxed (C=3). Their Q scores are strong (Q=2 or Q=3). The sole mechanism suppressing their tier is premium consumption above the 1,700 threshold combined with insufficient ReqEff to generate R points.

---

*Multi-period CRQC analysis — CP1 (Apr 20, 2026) through CP9 (Jun 23, 2026). Full CRQC scores computable only at CP8 and CP9 (premium data fully available). CP1–CP7 use LoC-based C estimation and R trajectory reconstruction from available partial data. Q scores: CP4–CP7 use team-level proxy (Q=3 for active contributors); CP9 uses per-user PR data (Jun 21, 2026 snapshot). Q=FB denotes active user with no PR data captured, treated as Q=2. 15+1 users excluded per ignore list. Special roles (SwapnilNice, ssamal-nice, smishra-nice) tracked separately in CP9 CRQC. rwalunj-nice not tiered.*
