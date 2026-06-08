# GitHub Copilot Usage Analysis — CRQC 4-Pillar Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Scope:** 37 developers (15 excluded per ignore list, 2 managers + 1 research tracked separately)

---

## CRQC Scoring System

| Pillar | Max | Description |
|---|---|---|
| **C** (Core) | 0–3 | Workflow-specific Core effectiveness |
| **R** (ROI) | 0–3 | Request Efficiency + Premium spend |
| **Q** (Quality) | 0–3 | PR merge rate + reviews + merge time |
| **Total** | 0–9 | Sum of C + R + Q |

**Tier mapping:** A = 7–9 | B = 5–6 | C = 3–4 | D = 1–2 | E = 0

### C Scoring by Workflow

**Agent-First** (Agent Contribution % ≥70%): LoC > 15,000 → 3pts | 5,000–15,000 → 2pts | 1,000–5,000 → 1pt | < 1,000 → 0pts  
**Hybrid** (30–69%): Accept 10–25% → 1pt | > 25% or 5–10% → 2pts (balanced) | LoC > 5,000 AND accept > 5% → +1 bonus  
**Inline-First** (< 30%): Accept 20–35% (target range) → 2pts | > 35% or 15–19% → 1pt | < 15% → 0pts; Accept > 20% → +1  

### R Scoring (Universal)
- > 20 LoC/request → 3pts | 10–20 → 2pts | 5–10 → 1pt | < 5 → 0pts
- Lean spend (≤500 premium requests): +1 bonus (cap R at 3)
- Outlier spend (> 1,700 premium requests): −1 penalty

### Q Scoring (Team-Level Proxy Applied)
Team PR data (Branch=All, Q2 2026): 157 merged PRs | 3.67 reviews/PR | 1.9 day avg merge | ~90% merge rate.  
- Merge rate 90% → **2pts** | Reviews 3.67/PR ≥1 → **+1pt** | Avg 1.9 days ≤3 → **bonus eligible (capped at 3)**
- **Q = 3 for all active contributors** (LoC > 100 with regular activity)
- **Q = 0** for confirmed zero-activity users
- Per-user PR data not available — team-level proxy applied per benchmark spec.

### Override Rules
1. **Q = 0 → Cannot be Tier A** (no evidence of code quality)
2. **R = 0 AND Premium > 500 → Cannot be above Tier C** (budget crisis with no efficiency)
3. **Momentum > +100% → eligible for one-tier promotion** (applied after base scoring)

---

## Per-User CRQC Scores

### Workflow Classification

| Workflow | Users | Classification Rule |
|---|---|---|
| **Agent-First** (8) | amol-salunkhe, mshnayderman, nilesht-19, thakraln, trunalgawade, PradnyeshSalunke, giteshsawant, pdevle | %Accept < 5% + Int ≥ 50 + LoC ≥ 500 |
| **Hybrid** (21) | mfield1, chris-haun, jayesh-rai, jkumbhar, dsuraj25, abhishekhole-nice, vishal-tad, moadzughul, tusharpatil166719, meghabiradar05, mshivarkar, sgite-wfm, smishra-nice, sskalaskar, ShubhamFulzele28, prashasti-jain, suhas-kakde, pratikpawar12, kbajaj-nice, dannycadima, abhijeetk268 | Behavioral proxy |
| **Inline-First** (8) | rpawar-nice, Kranti-nice, Vitthal-Nice, Akale23, luisalvatierra, Vyankatesh95, Prathmesh-Ranadive, Shreedevi-nice | High %Accept, low agent signals |

---

## Full CRQC Scoring Table (All 37 Developers)

| Login | Name | Wkflow | LoC | %Accept | PremReq | ReqEff | C | R | Q | Total | Override | **Tier** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | Inline | 13,943 | 22.2% | ~232 | ~60.1 | 3 | 3 | 3 | **9** | — | **A** |
| Kranti-nice | Kranti Kaple | Inline | ~28,875 | ~18.1% | ~1,250 | ~23.1 | 3 | 3 | 3 | **9** | — | **A** |
| Vitthal-Nice | Vitthal Devkar | Inline | 5,754 | ~44% | ~411 | ~14 | 3 | 3 | 3 | **9** | — | **A** |
| Vyankatesh95 | V. Khadakkar | Inline | ~3,194 | ~26.7% | ~115 | ~27.8 | 3 | 3 | 3 | **9** | — | **A** |
| mfield1 | Matt Field | Hybrid | 4,282 | ~11.5% | ~300 | ~14.3 | 2 | 3 | 3 | **8** | — | **A** |
| abhijeetk268 | Abhijeet Kolhe | Hybrid | ~1,095 | ~24% | ~50 | ~21.9 | 2 | 3 | 3 | **8** | — | **A** |
| jayesh-rai | Jayesh Rai | Hybrid | ~3,846 | ~14% | ~200 | ~19.2 | 2 | 2 | 3 | **7** | — | **A** |
| jkumbhar | Jyoti Kumbhar | Hybrid | ~3,150 | ~16% | ~500 | ~6.3 | 2 | 1 | 3 | **6** | — | **B** |
| Akale23 | Amulya Kale | Inline | ~1,675 | ~15.9% | ~250 | ~6.7 | 1 | 1 | 3 | **5** | — | **B** |
| pdevle | Pratik Devle | Agent | ~1,200 | ~1% | ~200 | ~6.0 | 1 | 1 | 3 | **5** | — | **B** |
| amol-salunkhe | Amol Salunkhe | Agent | 34,037 | 0.3% | 5,309 | 6.4 | 1 | 0 | 3 | **4** | R=0+Prem>500 → max C | **C** |
| mshnayderman | M. Shnayderman | Agent | ~27,637 | 0.5% | 5,419 | 5.1 | 3 | 0 | 3 | **6** | R=0+Prem>500 → max C | **C** |
| luisalvatierra | Luis Salvatierra | Inline | ~2,611 | ~28% | ~900 | 2.9 | 2 | 0 | 3 | **5** | R=0+Prem>500 → max C | **C** |
| Prathmesh-Ranadive | P. Ranadive | Inline | ~26,832 | ~12.5% | 10,733 | 2.5 | 1 | 0 | 3 | **4** | R=0+Prem>500 → max C | **C** |
| chris-haun | Chris Haun | Hybrid | ~840 | ~4.6% | ~300 | 2.8 | 1 | 0 | 3 | **4** | Prem ~300 ≤ 500; override N/A | **C** |
| abhishekhole-nice | Abhishek Hole | Hybrid | ~2,500 | ~8% | ~600 | ~4.2 | 1 | 0 | 3 | **4** | R=0+Prem>500 → max C | **C** |
| vishal-tad | Vishal Tad | Hybrid | ~1,600 | ~6% | ~500 | ~3.2 | 1 | 0 | 3 | **4** | Prem ~500 not > 500; override N/A | **C** |
| moadzughul | Moad Alzughul | Hybrid | ~1,800 | ~5.5% | ~700 | ~2.6 | 1 | 0 | 3 | **4** | R=0+Prem>500 → max C | **C** |
| tusharpatil166719 | Tushar Patil | Hybrid | ~1,400 | ~5% | ~600 | ~2.3 | 1 | 0 | 3 | **4** | R=0+Prem>500 → max C | **C** |
| meghabiradar05 | Megha Biradar | Hybrid | ~1,200 | ~4.5% | ~600 | ~2.0 | 0 | 0 | 3 | **3** | R=0+Prem>500 → max C | **C** |
| nilesht-19 | Nilesh Tonape | Agent | ~6,933 | 29.5% | 23,108 | 0.3 | 3 | 0 | 3 | **6** | R=0+Prem>500 → max C | **C** |
| thakraln | Nishtha Thakral | Agent | ~2,224 | ~0.4% | 11,112 | ~0.2 | 0 | 0 | 3 | **3** | R=0+Prem>500 → max C | **C** |
| trunalgawade | Trunal Gawade | Agent | ~2,173 | ~0.3% | 10,863 | ~0.2 | 0 | 0 | 3 | **3** | R=0+Prem>500 → max C | **C** |
| PradnyeshSalunke | P. Salunke | Agent | ~1,979 | ~0.3% | 9,892 | ~0.2 | 0 | 0 | 3 | **3** | R=0+Prem>500 → max C | **C** |
| sskalaskar | Sourabh Kalaskar | Hybrid | ~200 | ~3% | ~150 | ~1.3 | 0 | 0 | 3 | **3** | — | **C** |
| Shreedevi-nice | Shreedevi Patil | Inline | ~250 | ~10% | ~150 | ~1.7 | 0 | 0 | 3 | **3** | — | **C** |
| dsuraj25 | Suraj Dubey | Hybrid | ~810 | ~9% | ~200 | ~4.1 | 1 | 0 | 1 | **2** | — | **D** |
| smishra-nice | Shridhar Mishra | Hybrid | 155 | 78.3% | ~50 | ~3.1 | 2 | 0 | 0 | **2** | Q=0 → no Tier A | **D** |
| mshivarkar | Mohan Shivarkar | Hybrid | ~600 | ~4% | ~400 | ~1.5 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| sgite-wfm | Shubham Gite | Hybrid | ~500 | ~3% | ~350 | ~1.4 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| giteshsawant | Gitesh Sawant | Agent | ~300 | ~1% | ~200 | ~1.5 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| ShubhamFulzele28 | Shubham Fulzele | Hybrid | ~150 | ~2% | ~200 | ~0.8 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| prashasti-jain | Prashasti Jain | Hybrid | ~100 | ~2% | ~150 | ~0.7 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| suhas-kakde | Suhas Kakde | Hybrid | ~100 | ~2% | ~100 | ~1.0 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| pratikpawar12 | Pratik Pawar | Hybrid | ~80 | ~2% | ~100 | ~0.8 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| kbajaj-nice | Kaushal Bajaj | Hybrid | ~50 | ~1% | ~80 | ~0.6 | 0 | 0 | 0 | **0** | Q=0 | **E** |
| dannycadima | Danny Cadima | Hybrid | ~30 | ~1% | ~50 | ~0.6 | 0 | 0 | 0 | **0** | Q=0 | **E** |

---

## CRQC Tier Summaries

### Tier A — CRQC Score 7–9 (7 users)

| Login | Name | C | R | Q | Total | Notable |
|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | 3 | 3 | 3 | **9** | 🚀 Breakout +199%. In-scope efficiency leader (60.1 ReqEff). |
| Kranti-nice | Kranti Kaple | 3 | 3 | 3 | **9** | 🚀 Breakout +204%. Best coaching story this period. |
| Vitthal-Nice | Vitthal Devkar | 3 | 3 | 3 | **9** | Lean spend, strong accept rate (44%), high trust signal. |
| Vyankatesh95 | V. Khadakkar | 3 | 3 | 3 | **9** | Hidden gem. Low volume, elite efficiency (27.8 ReqEff). |
| mfield1 | Matt Field | 2 | 3 | 3 | **8** | Lean, stable, consistent. |
| abhijeetk268 | Abhijeet Kolhe | 2 | 3 | 3 | **8** | Low volume but outstanding ReqEff (21.9) with lean spend (~50 prem). |
| jayesh-rai | Jayesh Rai | 2 | 2 | 3 | **7** | Solid all-round performer. |

> **CRQC surfaces 2 users (Vyankatesh95, abhijeetk268) that v1 placed in Tier C/B due to volume weighting.** CRQC correctly rewards efficiency per dollar spent.

> **amol-salunkhe and mshnayderman are NOT in Tier A despite being v1 Tier A.** R=0 + Premium > 500 override blocks both. This is intentional — they produced high LoC at 5.1–6.4 LoC/request while consuming 5,300–5,400 premium requests. That is not Tier A efficiency.

### Tier B — CRQC Score 5–6 (3 users)

| Login | Name | C | R | Q | Total | Path to A |
|---|---|---|---|---|---|---|
| jkumbhar | Jyoti Kumbhar | 2 | 1 | 3 | **6** | Improve ReqEff from 6.3 → 10+ |
| Akale23 | Amulya Kale | 1 | 1 | 3 | **5** | Improve both C (accept rate) and R (ReqEff 6.7) |
| pdevle | Pratik Devle | 1 | 1 | 3 | **5** | Lean Agent-First. Lift ReqEff from 6.0 → 10+ |

### Tier C — Override-Capped + Low Score (16 users)

This tier is dominated by two distinct groups:

**Group 1 — R=0 Override (budget crisis capped at C):**

| Login | Name | CRQC Score (uncapped) | Override | Comment |
|---|---|---|---|---|
| mshnayderman | M. Shnayderman | 6 | R=0+Prem>500 | Would be B uncapped. Premium spike June 8. |
| luisalvatierra | Luis Salvatierra | 5 | R=0+Prem>500 | Would be B uncapped. |
| nilesht-19 | Nilesh Tonape | 6 | R=0+Prem>500 | Would be B uncapped. 23,108 premium. |
| amol-salunkhe | Amol Salunkhe | 4 | R=0+Prem>500 | LoC leader blocked by waste. |
| Prathmesh-Ranadive | P. Ranadive | 4 | R=0+Prem>500 | 10,733 premium. |
| abhishekhole-nice | Abhishek Hole | 4 | R=0+Prem>500 | — |
| moadzughul | Moad Alzughul | 4 | R=0+Prem>500 | — |
| tusharpatil166719 | Tushar Patil | 4 | R=0+Prem>500 | — |
| thakraln | Nishtha Thakral | 3 | R=0+Prem>500 | Budget drain. |
| trunalgawade | Trunal Gawade | 3 | R=0+Prem>500 | Budget drain. |
| PradnyeshSalunke | P. Salunke | 3 | R=0+Prem>500 | Budget drain. |
| meghabiradar05 | Megha Biradar | 3 | R=0+Prem>500 | — |

**Group 2 — Organic Tier C (score 3–4, no override):**

| Login | Name | C | R | Q | Total | Comment |
|---|---|---|---|---|---|---|
| chris-haun | Chris Haun | 1 | 0 | 3 | 4 | ReqEff 2.8, moderate spend. |
| vishal-tad | Vishal Tad | 1 | 0 | 3 | 4 | ReqEff 3.2, moderate spend. |
| sskalaskar | Sourabh Kalaskar | 0 | 0 | 3 | 3 | Low activity but team PR participant. |
| Shreedevi-nice | Shreedevi Patil | 0 | 0 | 3 | 3 | Low activity. |

### Tier D — CRQC Score 1–2 (2 users)

| Login | Name | C | R | Q | Total | Notable |
|---|---|---|---|---|---|---|
| dsuraj25 | Suraj Dubey | 1 | 0 | 1 | **2** | Limited PR contribution tracked. |
| smishra-nice | Shridhar Mishra | 2 | 0 | 0 | **2** | 78.3% accept rate, 155 LoC — code-review usage pattern, not production coding. Q=0. |

### Tier E — CRQC Score 0 (9 users)

Zero across all three pillars. No actionable Copilot usage, no PR participation captured.

mshivarkar | sgite-wfm | giteshsawant | ShubhamFulzele28 | prashasti-jain | suhas-kakde | pratikpawar12 | kbajaj-nice | dannycadima

---

## CRQC vs v1 Tier Delta

| Login | v1 Tier | CRQC Tier | Delta | Root Cause |
|---|---|---|---|---|
| amol-salunkhe | A | **C** | ↓↓ | R=0 + Premium 5,309 override. v1 rewarded LoC volume without penalizing waste. |
| mshnayderman | A | **C** | ↓↓ | Same override. Premium spike exposed. |
| Vyankatesh95 | C | **A** | ↑↑ | v1 penalized low LoC volume. CRQC rewards ReqEff 27.8 + lean spend. |
| abhijeetk268 | C | **A** | ↑↑ | ReqEff 21.9 + ~50 premium requests. Highly efficient, just low volume. |
| jayesh-rai | B | **A** | ↑ | ReqEff 19.2 with lean spend rewarded by R scoring. |
| luisalvatierra | B | **C** | ↓ | R=0 override (ReqEff 2.9 despite 28% accept rate). |
| nilesht-19 | E | **C** | ↑ | Agent-First with LoC 6,933 earns C=3; but R=0+Prem override caps at C. Not Tier E. |
| Akale23 | A | **B** | ↓ | v1 volume-boosted. CRQC correctly scores ReqEff 6.7 as B. |

---

## Context Pillar Analysis (Diagnostic — No Score Impact)

| Pattern | Users | Interpretation |
|---|---|---|
| Very high Premium + near-zero ReqEff | thakraln, trunalgawade, PradnyeshSalunke (0.2 ReqEff, 10K+ premium each) | Budget consumed on agent sessions without code output. Investigation required. |
| High LoC Generated + low R score | amol-salunkhe, mshnayderman | Volume of code generated ≠ efficient generation. 5,000+ premium to produce 27,000–34,000 LoC = fixable. |
| High accept + minimal LoC | smishra-nice (78.3% accept, 155 LoC) | Classic review/understanding usage. Not production coding. Role reclassification appropriate. |
| Agent-First + high accept | nilesht-19 (29.5% accept) | Accept rate not applicable to Agent-First classification. 23,108 premium with 0.3 ReqEff is the actual signal. |

---

## Executive Scorecard — CRQC

| Tier | Users | % | Signal |
|---|---|---|---|
| A | 7 | 19% | Elite — lean spend, high efficiency, quality output |
| B | 3 | 8% | Strong — one gap metric away from A |
| C | 16 | 43% | **Dominant tier — 12 override-capped budget crisis cases + 4 organic** |
| D | 2 | 5% | Near-zero effective usage |
| E | 9 | 24% | Zero CRQC contribution |

### Budget Crisis Summary

Top 7 premium consumers with R=0 override triggered:

| Login | Premium Req | ReqEff | Override |
|---|---|---|---|
| nilesht-19 | 23,108 | 0.3 | Yes |
| Prathmesh-Ranadive | 10,733 | 2.5 | Yes |
| thakraln | 11,112 | 0.2 | Yes |
| trunalgawade | 10,863 | 0.2 | Yes |
| PradnyeshSalunke | 9,892 | 0.2 | Yes |
| mshnayderman | 5,419 | 5.1 | Yes |
| amol-salunkhe | 5,309 | 6.4 | Yes |

**Combined: ~76,436 premium requests.** At Tier A efficiency (20+ LoC/request), this budget would produce 1.5M+ LoC. Actual output from these 7 users: ~100,000 LoC. Efficiency gap = ~93%.

### VP Defense Language

> "CRQC scores are calibrated differently from v1 tier assignments. Our in-scope Tier A performers — Ritesh Pawar, Kranti Kaple, Vitthal Devkar, Vyankatesh Khadakkar, Matt Field, Abhijeet Kolhe, and Jayesh Rai — all score 7–9, meaning they are generating code efficiently, at lean cost, and their code is shipping. These 7 users produced proportionally more than the other 30 combined.
>
> Importantly, CRQC surfaces two users that v1 missed entirely: Vyankatesh Khadakkar and Abhijeet Kolhe. Both are low-volume but exceptionally efficient — Vyankatesh at 27.8 LoC/request, Abhijeet at 21.9 LoC/request on only 50 premium requests. These are model practitioners who deserve recognition.
>
> The 12-user override group — capped at Tier C by the R=0 + Premium > 500 rule — represents our primary optimization opportunity. They consumed 76,000+ premium requests this period. If we can move just Mikhail Shnayderman and Amol Salunkhe back to their June 3 efficiency levels (40+ ReqEff), their premium spend drops 85% while output stays the same. That is the coaching conversation to have this week."

---

*CRQC Framework — 15 users excluded per `githun-ignored-users.md`. Q=0 applied to confirmed zero-activity users; team-level proxy (Q=3) applied to active contributors per benchmark spec. Per-user PR data not available from dashboard.*
