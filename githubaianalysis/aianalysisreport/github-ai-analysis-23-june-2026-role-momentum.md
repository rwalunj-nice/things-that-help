# GitHub Copilot Usage Analysis — Role Context + Momentum Framework
## WFM Integrations | CP9 | June 23, 2026

---

### Header

| Field | Value |
|---|---|
| Product | WFM Integrations |
| VP | (WFM VP) |
| Checkpoint | CP9 (Jun 23, 2026) |
| Baseline | CP8 (Jun 12, 2026) |
| Window | 11 days |
| Q2 Close | Jun 30, 2026 — **7 days remaining** |
| PR Data Snapshot | Jun 21, 2026 |
| Framework | Role Context + Momentum |
| Analysis By | rwalunj-nice (Research role — excluded from tier) |

**Data Notes:**
- "New" users have no CP8 baseline; they are treated as first-window entrants and are not assigned a momentum label — their entry delta is noted.
- `ssnikam` (Sanket Nikam) has zero AI LoC at both CP8 and CP9 — tracked separately as a non-AI user with high PR activity.
- `copilotshree` is associated with a non-CX Eng org; listed for completeness but flagged as out-of-team scope.
- PR merge rate field "FB" = First Baseline (no PRs submitted, so no rate calculable).
- `mshnayderman` is the only user reporting to a different manager (Alon Vax) — noted in scoring.
- Premium LoC = Copilot premium feature consumption (e.g., agent mode, multi-file edits). High premium relative to total LoC indicates expensive usage patterns.

---

## Section 1 — Role Assignments

| GitHub Handle | Full Name | Manager | Assigned Role | Notes |
|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | — | **Manager** | Team lead for majority of ICs |
| ssamal-nice | Susovan Samal | — | **Manager** | Team lead for ssamal sub-team |
| smishra-nice | Shridhar Mishra | — | **Lead** | Senior IC / Architect role |
| rwalunj-nice | Rahul Walunj | — | **Research** | Excluded from tier — tracked separately |
| amol-salunkhe | Amol Salunkhe | SwapnilNice | Developer | IC |
| Kranti-nice | Kranti Kaple | SwapnilNice | Developer | IC |
| Prathmesh-Ranadive | Prathmesh Ranadive | SwapnilNice | Developer | IC |
| mshnayderman | Mikhail Shnayderman | Alon Vax | Developer | IC — different org |
| luisalvatierra | Luis Salvatierra | SwapnilNice | Developer | IC |
| chris-haun | Chris Haun | SwapnilNice | Developer | IC |
| mfield1 | Matt Field | SwapnilNice | Developer | IC |
| rpawar-nice | Ritesh Pawar | ssamal-nice | Developer | IC |
| nilesht-19 | Nilesh Tonape | SwapnilNice | Developer | IC |
| copilotshree | (Shreedevi?) | Non-CX Eng | Developer | Out-of-team scope — flagged |
| PradnyeshSalunke | Pradnyesh Salunke | SwapnilNice | Developer | IC |
| mshivarkar | Mohan Shivarkar | SwapnilNice | Developer | IC |
| Vyankatesh95 | Vyankatesh Khadakkar | SwapnilNice | Developer | IC |
| vishal-tad | Vishal Tad | ssamal-nice | Developer | IC |
| moadzughul | Moad Alzughul | SwapnilNice | Developer | IC |
| sskalaskar | Sourabh Kalaskar | SwapnilNice | Developer | IC |
| abhishekhole-nice | Abhishek Hole | SwapnilNice | Developer | IC |
| Vitthal-Nice | Vitthal Devkar | ssamal-nice | Developer | IC |
| jayesh-rai | Jayesh Rai | SwapnilNice | Developer | IC |
| Akale23 | Amulya Kale | ssamal-nice | Developer | IC |
| trunalgawade | Trunal Gawde | ssamal-nice | Developer | IC |
| tusharpatil166719 | Tushar Patil | ssamal-nice | Developer | IC |
| suhas-kakde | Suhas Kakde | SwapnilNice | Developer | IC |
| jkumbhar | Jyoti Kumbhar | SwapnilNice | Developer | IC |
| Shreedevi-nice | Shreedevi Patil | SwapnilNice | Developer | IC |
| meghabiradar05 | Megha Biradar | SwapnilNice | Developer | IC |
| prashasti-jain | Prashasti Jain | SwapnilNice | Developer | IC |
| pdevle | Pratik Devle | ssamal-nice | Developer | IC |
| giteshsawant | Gitesh Sawant | ssamal-nice | Developer | IC |
| dsuraj25 | Suraj Dubey | ssamal-nice | Developer | New — first window |
| thakraln | Nishtha Thakral | ssamal-nice | Developer | New — first window |
| abhijeetk268 | Abhijeet Kolhe | SwapnilNice | Developer | New — first window |
| pratikpawar12 | Pratik Pawar | SwapnilNice | Developer | New — first window |
| amol-doke | Amol Doke | SwapnilNice | Developer | New — first window |
| mohitbaghelnice | Mohit Baghel | ssamal-nice | Developer | New — first window |
| kbajaj-nice | Kaushal Bajaj | ssamal-nice | Developer | New — first window |
| dannycadima | Danny Cadima | SwapnilNice | Developer | New — first window |
| ssnikam | Sanket Nikam | ssamal-nice | Developer | Zero AI — special note |

---

## Section 2 — Momentum Scores Table (Developers Only)

> Formula: `Momentum % = ((CP9 LoC − CP8 LoC) / max(CP8 LoC, 1)) × 100`
> Sorted by Momentum % descending. New entrants listed at bottom.

### Established Users (CP8 Baseline Exists)

| Handle | Full Name | CP8 LoC | CP9 LoC | Delta | Momentum % | Momentum Label |
|---|---|---|---|---|---|---|
| mshivarkar | Mohan Shivarkar | 2,097 | 4,201 | +2,104 | **+100.3%** | **BREAKOUT** |
| Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | 35,091 | +8,039 | **+29.7%** | Stable (near Rising) |
| luisalvatierra | Luis Salvatierra | 9,477 | 12,080 | +2,603 | **+27.5%** | Stable (near Rising) |
| Kranti-nice | Kranti Kaple | 31,645 | 37,978 | +6,333 | **+20.0%** | Stable |
| tusharpatil166719 | Tushar Patil | 1,798 | 2,200 | +402 | **+22.4%** | Stable |
| trunalgawade | Trunal Gawde | 2,038 | 2,352 | +314 | **+15.4%** | Stable |
| PradnyeshSalunke | Pradnyesh Salunke | 3,731 | 4,237 | +506 | **+13.6%** | Stable |
| jayesh-rai | Jayesh Rai | 2,479 | 2,712 | +233 | **+9.4%** | Stable |
| rpawar-nice | Ritesh Pawar | 8,662 | 8,662 | 0 | 0% (no LoC gain) | *see Zero Momentum* |
| pdevle | Pratik Devle | 1,384 | 1,478 | +94 | **+6.8%** | Stable |
| amol-salunkhe | Amol Salunkhe | 41,008 | 43,585 | +2,577 | **+6.3%** | Stable |
| vishal-tad | Vishal Tad | 3,520 | 3,737 | +217 | **+6.2%** | Stable |
| Shreedevi-nice | Shreedevi Patil | 1,786 | 1,886 | +100 | **+5.6%** | Stable |
| abhishekhole-nice | Abhishek Hole | 2,993 | 3,150 | +157 | **+5.2%** | Stable |
| sskalaskar | Sourabh Kalaskar | 2,698 | 3,233 | +535 | **+19.8%** | Stable |
| suhas-kakde | Suhas Kakde | 1,677 | 2,005 | +328 | **+19.6%** | Stable |
| giteshsawant | Gitesh Sawant | 1,110 | 1,369 | +259 | **+23.3%** | Stable |
| Vitthal-Nice | Vitthal Devkar | 2,609 | 2,683 | +74 | **+2.8%** | Stable |
| jkumbhar | Jyoti Kumbhar | 1,870 | 1,880 | +10 | **+0.5%** | Stable |
| prashasti-jain | Prashasti Jain | 1,545 | 1,562 | +17 | **+1.1%** | Stable |
| chris-haun | Chris Haun | 10,384 | 10,493 | +109 | **+1.1%** | Stable |
| meghabiradar05 | Megha Biradar | 1,720 | 1,727 | +7 | **+0.4%** | Stable |
| nilesht-19 | Nilesh Tonape | 7,346 | 7,354 | +8 | **+0.1%** | Stable |
| mfield1 | Matt Field | 9,800 | 9,803 | +3 | **~0%** | Stable |
| mshnayderman | Mikhail Shnayderman | 27,539 | 27,539 | 0 | **0%** | *see Zero Momentum* |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,177 | 4,177 | 0 | **0%** | *see Zero Momentum* |
| moadzughul | Moad Alzughul | 3,409 | 3,409 | 0 | **0%** | *see Zero Momentum* |
| Akale23 | Amulya Kale | 2,472 | 2,472 | 0 | **0%** | *see Zero Momentum* |
| copilotshree | (Shreedevi?) | 5,013 | 5,013 | 0 | **0%** | *Out-of-team / Zero* |

### New Entrants (No CP8 Baseline — First Window)

| Handle | Full Name | CP9 LoC | Entry Delta | Label |
|---|---|---|---|---|
| dsuraj25 | Suraj Dubey | 1,169 | +1,169 | New Entrant |
| thakraln | Nishtha Thakral | 806 | +806 | New Entrant |
| abhijeetk268 | Abhijeet Kolhe | 656 | +656 | New Entrant |
| pratikpawar12 | Pratik Pawar | 250 | +250 | New Entrant |
| amol-doke | Amol Doke | 10 | +10 | New Entrant — minimal signal |
| mohitbaghelnice | Mohit Baghel | 3 | +3 | New Entrant — minimal signal |
| kbajaj-nice | Kaushal Bajaj | 5 | +5 | New Entrant — minimal signal |
| dannycadima | Danny Cadima | 34 | +34 | New Entrant — minimal signal |

---

## Section 3 — PR Quality Modifier Table

> Rule: ≥80% merge rate → +1 tier | 50–79% → 0 | <50% → −1 tier | No PRs (FB) → No modifier applied

| Handle | Full Name | PRs | Merged | Merge Rate | Modifier | Notes |
|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 8 | 8 | 100% | **+1** | Perfect merge rate |
| Kranti-nice | Kranti Kaple | 22 | 16 | 72.7% | 0 | Within neutral band |
| Prathmesh-Ranadive | Prathmesh Ranadive | 24 | 24 | 100% | **+1** | Perfect merge rate |
| mshnayderman | Mikhail Shnayderman | 2 | 1 | 50% | 0 | Borderline — neutral applied |
| luisalvatierra | Luis Salvatierra | 12 | 10 | 83.3% | **+1** | |
| chris-haun | Chris Haun | 47 | 45 | 95.7% | **+1** | High volume, high quality |
| mfield1 | Matt Field | 33 | 31 | 93.9% | **+1** | |
| rpawar-nice | Ritesh Pawar | 0 | 0 | FB | — | No PRs submitted |
| nilesht-19 | Nilesh Tonape | 20 | 18 | 90% | **+1** | |
| copilotshree | (Shreedevi?) | 0 | 0 | FB | — | Out-of-team |
| PradnyeshSalunke | Pradnyesh Salunke | 8 | 8 | 100% | **+1** | |
| mshivarkar | Mohan Shivarkar | 11 | 11 | 100% | **+1** | |
| Vyankatesh95 | Vyankatesh Khadakkar | 16 | 16 | 100% | **+1** | |
| vishal-tad | Vishal Tad | 17 | 15 | 88.2% | **+1** | |
| moadzughul | Moad Alzughul | 45 | 43 | 95.6% | **+1** | High volume |
| sskalaskar | Sourabh Kalaskar | 15 | 13 | 86.7% | **+1** | |
| abhishekhole-nice | Abhishek Hole | 14 | 14 | 100% | **+1** | |
| Vitthal-Nice | Vitthal Devkar | 7 | 7 | 100% | **+1** | |
| jayesh-rai | Jayesh Rai | 17 | 17 | 100% | **+1** | |
| Akale23 | Amulya Kale | 7 | 6 | 85.7% | **+1** | |
| trunalgawade | Trunal Gawde | 1 | 1 | 100% | **+1** | Small sample |
| tusharpatil166719 | Tushar Patil | 4 | 4 | 100% | **+1** | Small sample |
| suhas-kakde | Suhas Kakde | 29 | 27 | 93.1% | **+1** | |
| jkumbhar | Jyoti Kumbhar | 19 | 12 | 63.2% | 0 | Elevated pending/reject rate |
| Shreedevi-nice | Shreedevi Patil | 15 | 14 | 93.3% | **+1** | |
| meghabiradar05 | Megha Biradar | 5 | 5 | 100% | **+1** | |
| prashasti-jain | Prashasti Jain | 8 | 7 | 87.5% | **+1** | |
| pdevle | Pratik Devle | 7 | 7 | 100% | **+1** | |
| giteshsawant | Gitesh Sawant | 1 | 0 | **0%** | **−1** | Only PR open/rejected |
| dsuraj25 | Suraj Dubey | 1 | 1 | 100% | **+1** | New entrant |
| thakraln | Nishtha Thakral | 0 | 0 | FB | — | New entrant, no PRs |
| abhijeetk268 | Abhijeet Kolhe | 53 | 49 | 92.5% | **+1** | Very high volume for new entrant |
| pratikpawar12 | Pratik Pawar | 9 | 9 | 100% | **+1** | |
| amol-doke | Amol Doke | 8 | 4 | 50% | 0 | Borderline — neutral applied |
| mohitbaghelnice | Mohit Baghel | 1 | 1 | 100% | **+1** | Small sample |
| kbajaj-nice | Kaushal Bajaj | 2 | 2 | 100% | **+1** | Small sample |
| dannycadima | Danny Cadima | 0 | 0 | FB | — | New entrant, no PRs |
| ssnikam | Sanket Nikam | 55 | 49 | 89.1% | **+1** | Zero AI — separate section |

---

## Section 4 — Combined Final Scoring Matrix

> Tier order: Breakout > Rising > Stable > Slipping > Declining
> +1 tier moves up one step; −1 tier moves down one step.
> New entrants: Base = "New" — modifier applied as context note only.

### Established Users

| Handle | Full Name | Momentum % | Base Tier | PR Modifier | Final Tier | Final Assessment |
|---|---|---|---|---|---|---|
| mshivarkar | Mohan Shivarkar | +100.3% | Breakout | +1 | **Breakout+** | Already at ceiling — budget tension flag (see Section 6) |
| Prathmesh-Ranadive | Prathmesh Ranadive | +29.7% | Stable | +1 | **Rising** | PR quality elevates to Rising |
| luisalvatierra | Luis Salvatierra | +27.5% | Stable | +1 | **Rising** | PR quality elevates to Rising |
| giteshsawant | Gitesh Sawant | +23.3% | Stable | −1 | **Stable** | PR failure drops back to Stable |
| tusharpatil166719 | Tushar Patil | +22.4% | Stable | +1 | **Rising** | Strong trajectory in 11-day window |
| Kranti-nice | Kranti Kaple | +20.0% | Stable | 0 | **Stable** | Solid — near Rising threshold |
| sskalaskar | Sourabh Kalaskar | +19.8% | Stable | +1 | **Rising** | Good output + quality delivery |
| suhas-kakde | Suhas Kakde | +19.6% | Stable | +1 | **Rising** | Consistent quality throughput |
| trunalgawade | Trunal Gawde | +15.4% | Stable | +1 | **Rising** | Small sample but clean |
| PradnyeshSalunke | Pradnyesh Salunke | +13.6% | Stable | +1 | **Rising** | Quality delivery lifts tier |
| jayesh-rai | Jayesh Rai | +9.4% | Stable | +1 | **Rising** | Strong merge rate elevates |
| pdevle | Pratik Devle | +6.8% | Stable | +1 | **Rising** | Clean delivery on small volume |
| amol-salunkhe | Amol Salunkhe | +6.3% | Stable | +1 | **Rising** | High absolute LoC, perfect PR quality |
| vishal-tad | Vishal Tad | +6.2% | Stable | +1 | **Rising** | |
| Shreedevi-nice | Shreedevi Patil | +5.6% | Stable | +1 | **Rising** | |
| abhishekhole-nice | Abhishek Hole | +5.2% | Stable | +1 | **Rising** | Fast merge turnaround (16h 26m) |
| Vitthal-Nice | Vitthal Devkar | +2.8% | Stable | +1 | **Rising** | |
| jkumbhar | Jyoti Kumbhar | +0.5% | Stable | 0 | **Stable** | Elevated pending rate (63.2%) — watch |
| prashasti-jain | Prashasti Jain | +1.1% | Stable | +1 | **Rising** | |
| chris-haun | Chris Haun | +1.1% | Stable | +1 | **Rising** | Exceptionally high PR volume (47) — unique IC pattern |
| meghabiradar05 | Megha Biradar | +0.4% | Stable | +1 | **Rising** | |
| nilesht-19 | Nilesh Tonape | +0.1% | Stable | +1 | **Rising** | High absolute LoC (7,354) even at near-zero delta |
| mfield1 | Matt Field | ~0% | Stable | +1 | **Rising** | Very high absolute LoC (9,803), strong PR quality |
| mshnayderman | Mikhail Shnayderman | 0% | Stable | 0 | **Stable** | Zero LoC growth — needs attention |
| Vyankatesh95 | Vyankatesh Khadakkar | 0% | Stable | +1 | **Rising** | Zero LoC delta but perfect PR quality — output may be via PR without new Copilot sessions |
| moadzughul | Moad Alzughul | 0% | Stable | +1 | **Rising** | Zero LoC delta but 45 PRs, 95.6% merge — high PR throughput without new AI LoC is notable |
| Akale23 | Amulya Kale | 0% | Stable | +1 | **Rising** | Zero LoC delta — PR quality saves tier |
| rpawar-nice | Ritesh Pawar | 0% | Stable | — | **Stable** | No PRs, no LoC growth — critical gap |

### New Entrants (First Window — No Tier Comparable to Established)

| Handle | Full Name | CP9 LoC | PR Quality | Entry Assessment |
|---|---|---|---|---|
| abhijeetk268 | Abhijeet Kolhe | 656 | 92.5% (+1) | Strong start — very high PR volume (53) for a new entrant |
| dsuraj25 | Suraj Dubey | 1,169 | 100% (+1) | Best LoC among new entrants |
| pratikpawar12 | Pratik Pawar | 250 | 100% (+1) | Clean entry |
| thakraln | Nishtha Thakral | 806 | FB (—) | LoC present but no PRs yet |
| amol-doke | Amol Doke | 10 | 50% (0) | Minimal AI activity — signal unclear |
| mohitbaghelnice | Mohit Baghel | 3 | 100% (+1) | Nominal activity |
| kbajaj-nice | Kaushal Bajaj | 5 | 100% (+1) | Nominal activity |
| dannycadima | Danny Cadima | 34 | FB (—) | Minimal AI activity, no PRs |

---

## Section 5 — Per-User Momentum Cards (Top Performers and Concern Cases)

---

### BREAKOUT — Mohan Shivarkar (`mshivarkar`)

```
CP8 LoC:        2,097
CP9 LoC:        4,201
Delta:          +2,104
Momentum:       +100.3%  ← exactly at Breakout threshold
Base Tier:      Breakout
PR Modifier:    +1 (11/11 merged, 100%)
Final Tier:     Breakout+ (ceiling)
Premium LoC:    17,029
Req Efficiency: 0.2
```

**Assessment:** Mohan has achieved the only Breakout-level momentum in the team this checkpoint, doubling his cumulative LoC in 11 days. PR quality is flawless — 11 of 11 merged with a reasonable turnaround (97h 13m).

**Budget Tension Flag:** The Breakout label is earned. However, premium LoC of 17,029 against total LoC of 4,201 means Mohan consumed approximately 4x more premium token budget than he produced in total LoC. The request efficiency of 0.2 confirms a high-cost, low-density usage pattern. This is not a problem in isolation, but at scale it warrants a conversation: is he using agent/multi-file modes heavily for complex refactors, or is there inefficient prompt cycling? The output quality (100% merge) supports the former — but this ratio should be monitored.

---

### Rising (via PR Modifier) — Prathmesh Ranadive (`Prathmesh-Ranadive`)

```
CP8 LoC:        27,052
CP9 LoC:        35,091
Delta:          +8,039  ← largest absolute gain this window
Momentum:       +29.7%  (just below Rising threshold of +30%)
Base Tier:      Stable (high end)
PR Modifier:    +1 (24/24 merged, 100%)
Final Tier:     Rising
Premium LoC:    31,420
Req Efficiency: 1.1
```

**Assessment:** Prathmesh delivered the highest absolute LoC increase this checkpoint (+8,039 lines in 11 days) and maintained a perfect PR merge record across 24 submissions. The PR quality modifier appropriately bumps him to Rising.

**Budget Tension Flag (Critical):** Premium LoC of 31,420 against total LoC of 35,091 is a near 1:1 ratio. A healthy ratio should be closer to 10:1 or better (premium features consume significantly more tokens per LoC unit). At this rate, Prathmesh is driving substantial budget consumption. The output quality justifies the usage, but the spend rate needs to be surfaced to the manager. Recommend reviewing whether multi-file agent sessions are being used for tasks that single-file completions would handle adequately.

---

### Rising (via PR Modifier) — Luis Salvatierra (`luisalvatierra`)

```
CP8 LoC:        9,477
CP9 LoC:        12,080
Delta:          +2,603
Momentum:       +27.5%  (near Rising threshold)
Base Tier:      Stable (high end)
PR Modifier:    +1 (10/12 merged, 83.3%)
Final Tier:     Rising
Avg Time to Merge: 137h 46m
```

**Assessment:** Luis is trending strongly in this 11-day window — +27.5% puts him just 2.5 points below the Rising threshold organically, and the PR quality modifier lifts him there. The 137h average merge time is elevated (nearly 6 days per PR on average) — this may indicate a review bottleneck or large PR size. Worth investigating whether PRs are being batched or if reviewer bandwidth is constrained.

---

### Rising (via PR Modifier) — Chris Haun (`chris-haun`)

```
CP8 LoC:        10,384
CP9 LoC:        10,493
Delta:          +109
Momentum:       +1.1%
Base Tier:      Stable (low end)
PR Modifier:    +1 (45/47 merged, 95.7%)
Final Tier:     Rising
PRs Submitted:  47  ← highest PR volume in team this window
Avg Time to Merge: 81h 49m
```

**Assessment:** Chris's profile is unique in the team — minimal AI LoC growth (+109 lines) but an extraordinary PR throughput of 47 submissions in 11 days (4.3 PRs/day), with a 95.7% merge rate. This strongly suggests he is working on high-churn, small-delta tasks (configuration, tests, documentation, small fixes) that don't generate large LoC but represent high delivery velocity. The PR quality modifier is well-earned. Final tier: Rising.

**Note:** Chris's LoC Req Efficiency of 0.8 and Premium/Total ratio (12,535 / 10,493 ≈ 1.2x) is within acceptable range. His usage pattern is PR-dominant rather than LoC-dominant — this is a legitimate working style.

---

### Concern Case — Zero LoC Growth, High PR Activity — Moad Alzughul (`moadzughul`)

```
CP8 LoC:        3,409
CP9 LoC:        3,409
Delta:          0
Momentum:       0%
PRs Submitted:  45  ← very high
PRs Merged:     43  (95.6%)
Avg Time to Merge: 361h 1m  ← extremely elevated (15 days avg)
```

**Assessment:** Moad submitted 45 PRs with excellent quality but added zero new Copilot LoC in 11 days. The 361-hour average time to merge (15 days per PR on average) is the longest in the team and warrants immediate investigation. Possible explanations: (a) PRs are large and require extensive review, (b) review chain is bottlenecked, (c) Moad is completing work that doesn't generate new AI-assisted lines (manual coding, config, or review). The zero LoC growth approaching Q2 close is a concern signal.

---

### Concern Case — Zero Momentum with No PRs — Ritesh Pawar (`rpawar-nice`)

```
CP8 LoC:        8,662
CP9 LoC:        8,662
Delta:          0
Momentum:       0%
PRs:            0
Premium LoC:    879
Req Efficiency: 9.9
```

**Assessment:** Ritesh has 8,662 cumulative LoC (a meaningful base) but added nothing in the last 11 days. No PRs submitted either. Req Efficiency of 9.9 (very high) means he is generating many Copilot requests that aren't converting to accepted LoC — this could indicate exploratory usage, repeated suggestion cycling, or a task context that isn't Copilot-amenable. With 7 days to Q2 close, this is a conversation for `ssamal-nice`.

---

### Concern Case — 0% PR Merge Rate — Gitesh Sawant (`giteshsawant`)

```
CP8 LoC:        1,110
CP9 LoC:        1,369
Delta:          +259
Momentum:       +23.3%
Base Tier:      Stable
PR Modifier:    −1 (0/1 merged, 0%)
Final Tier:     Stable (downgraded from upper-Stable)
```

**Assessment:** Gitesh's momentum is genuinely positive (+23.3%) but the single PR submitted this window was not merged (0% merge rate). The −1 PR modifier prevents an upgrade. Small sample size (n=1) means this is not yet a pattern — but it must be watched. If the next window also shows rejected PRs, Slipping is on the horizon despite decent LoC growth.

---

### Concern Case — Elevated Review Time — Matt Field (`mfield1`)

```
CP8 LoC:        9,800
CP9 LoC:        9,803
Delta:          +3
Momentum:       ~0%
PRs:            33 submitted, 31 merged (93.9%)
Avg Time to Merge: 159h 6m  ← ~6.6 days average
```

**Assessment:** Matt has high cumulative LoC and excellent PR quality, but almost no new LoC growth this window (delta +3). The 159-hour average time to merge is significantly above the team median. Matt appears to be in a "delivery" phase rather than a "generation" phase — clearing outstanding PRs rather than writing new code. Given his cumulative position (9,803 LoC, top 5 in team), this may be appropriate task-cycle behavior, not a concern. Worth a check-in.

---

## Section 6 — Manager Assessment

### SwapnilNice — Swapnil Zade

```
CP8 LoC:    3,140
CP9 LoC:    3,140
Delta:      0
Premium:    1,650
Req Eff:    1.9
Init Count: 279
Role:       Manager
```

**Assessment:** Swapnil's LoC is static this checkpoint, consistent with a manager-role usage pattern. His primary signal is the Initiation count (279) — the highest in the org — indicating active Copilot engagement for tasks not reflected in LoC acceptance (code review assist, planning queries, documentation drafting, answer synthesis). Request Efficiency of 1.9 is reasonable for a manager role.

**Team Coverage:** Swapnil manages the majority of the WFM Integrations IC population. His team accounts for the Breakout (mshivarkar), the top absolute LoC gain (Prathmesh-Ranadive), and most of the Rising-tier performers. The budget tension cases (mshivarkar, Prathmesh-Ranadive) both sit in his org and should be reviewed with him.

**Q2 Concern:** Within Swapnil's team, moadzughul (zero LoC delta, 361h merge time), mfield1 (near-zero delta), and Vyankatesh95 (zero delta) are Q2 trailing concerns. Given 7 days remain, Swapnil should prioritize awareness of these cases.

---

### ssamal-nice — Susovan Samal

```
CP8 LoC:    ~38
CP9 LoC:    38
Delta:      0
Premium:    109
Req Eff:    0.3
Init Count: 30
Role:       Manager
```

**Assessment:** Susovan's usage is minimal in both volume and initiation count, consistent with a less Copilot-active manager profile. Request Efficiency of 0.3 (very low — high cost per accepted LoC) combined with low initiation suggests either sporadic engagement or usage for non-LoC tasks (queries, analysis).

**Team Concerns:** Within ssamal's team: rpawar-nice (zero LoC, zero PRs, Q2 gap), thakraln (new entrant, no PRs), and copilotshree (zero delta, out-of-team scope) are the primary gaps. Several new entrants (dsuraj25, thakraln, mohitbaghelnice, kbajaj-nice, ssnikam) sit in Susovan's team — onboarding quality for these users will define Q3 trajectory.

---

## Section 7 — Lead Assessment

### smishra-nice — Shridhar Mishra

```
CP9 LoC:        155
Premium LoC:    287
Req Efficiency: 0.5
Accept Rate:    78.3%  ← near-high
Init Count:     60
Role:           Lead / Senior IC / Architect
```

**Assessment:** Shridhar's LoC numbers are low in absolute terms but his usage signature is consistent with an architect/tech-lead profile: moderate initiation (60), low LoC output (expected — leads often review and guide rather than write), reasonable request efficiency (0.5), and a notably high accept rate (78.3%). High accept rate in a low-volume context indicates Shridhar is using Copilot selectively and accepting what it suggests with high confidence — this is a quality-first pattern.

The Premium LoC (287) exceeding total LoC (155) may indicate some agent-mode usage for complex architectural tasks. This is acceptable and expected for a lead role.

**Benchmark Note:** Leads are not tiered under the momentum framework. Shridhar's contribution value is measured by team quality impact, code review throughput, and architectural guidance — not LoC count. His 78.3% accept rate is the highest signal-of-quality in the dataset.

---

## Section 8 — Research Role

### rwalunj-nice — Rahul Walunj

```
CP9 LoC:        156
Premium LoC:    1,890
Req Efficiency: 0.1
Accept Rate:    7.1%
Init Count:     61
Role:           Research — EXCLUDED FROM TIER
```

**Note:** Research role is excluded from momentum scoring and tier assignment. Rahul's usage profile (7.1% accept rate, very low LoC against very high premium consumption) is consistent with a research/exploration pattern: many Copilot sessions for investigation, analysis, and tooling work that does not produce production LoC. This is expected and appropriate for the role. The 1,890 premium LoC against 156 accepted LoC (12:1 ratio) reflects the cost of deep investigation work.

---

## Section 9 — Users with Zero Momentum (Critical Q2 Concern — 7 Days Remaining)

> Q2 closes June 30, 2026. These users have not added a single Copilot LoC in the 11-day CP8→CP9 window. With only 7 days left, any contribution they make will be captured in CP9→Q2-close.

| Handle | Full Name | Manager | Cumul LoC | PRs | Key Concern |
|---|---|---|---|---|---|
| mshnayderman | Mikhail Shnayderman | Alon Vax | 27,539 | 2 (1 merged) | High cumul LoC, zero delta — is Copilot still in workflow? |
| rpawar-nice | Ritesh Pawar | ssamal-nice | 8,662 | 0 | Zero PRs AND zero LoC — no delivery signal at all |
| Vyankatesh95 | Vyankatesh Khadakkar | SwapnilNice | 4,177 | 16 (all merged) | PR activity is healthy; LoC gap may be task-type-driven |
| moadzughul | Moad Alzughul | SwapnilNice | 3,409 | 45 (43 merged) | Delivery active but zero new AI LoC; 361h TTM is alarming |
| Akale23 | Amulya Kale | ssamal-nice | 2,472 | 7 (6 merged) | Moderate activity, LoC gap is notable but not critical |
| copilotshree | (Shreedevi?) | Non-CX Eng | 5,013 | 0 | Out-of-team scope — flagged for org review |

**Summary:** 5 in-scope users (excluding copilotshree) have contributed zero new Copilot LoC in the last 11 days. The most alarming case is `rpawar-nice` (no PRs, no LoC, no delivery signal) and `mshnayderman` (high cumulative base but complete stall). `moadzughul` is a paradox: extremely high PR throughput but zero new AI assistance. This pattern — high manual delivery without AI augmentation — warrants a check-in to understand whether Copilot has been disabled, is blocked in that workflow context, or is simply not being used on current tasks.

**Recommended Actions:**
- `ssamal-nice` to follow up with `rpawar-nice` before EOD Jun 24.
- `SwapnilNice` to surface `moadzughul` and `Vyankatesh95` cases in team standup.
- `mshnayderman`'s manager (Alon Vax) should be looped in given different org.

---

## Section 10 — Budget Tension: Breakout/Rising Users with High Premium Spend

> Premium LoC represents consumption of Copilot premium features (agent mode, multi-file edit, etc.), which cost significantly more per token than standard completions. A healthy ratio is typically 10:1 or better (total LoC to premium LoC). Ratios near or below 2:1 are budget concerns.

| Handle | Full Name | Total LoC | Premium LoC | Ratio | Concern Level | Notes |
|---|---|---|---|---|---|---|
| Prathmesh-Ranadive | Prathmesh Ranadive | 35,091 | 31,420 | 1.1:1 | **CRITICAL** | Near 1:1 — premium almost equals total output |
| tusharpatil166719 | Tushar Patil | 2,200 | 35,886 | 0.06:1 | **CRITICAL** | Premium EXCEEDS total LoC by 16x |
| nilesht-19 | Nilesh Tonape | 7,354 | 32,332 | 0.23:1 | **CRITICAL** | Premium exceeds total LoC by 4x |
| Kranti-nice | Kranti Kaple | 37,978 | 35,537 | 1.07:1 | **HIGH** | Near 1:1 ratio at high absolute volume |
| mshivarkar | Mohan Shivarkar | 4,201 | 17,029 | 0.25:1 | **HIGH** | Breakout flag earned, but 4x premium overspend |
| PradnyeshSalunke | Pradnyesh Salunke | 4,237 | 20,544 | 0.21:1 | **HIGH** | Premium 5x total output |
| sskalaskar | Sourabh Kalaskar | 3,233 | 16,897 | 0.19:1 | **HIGH** | Premium 5x total output |

**Budget Tension Summary:**

The team has a systemic premium overspend pattern. Multiple users — including top performers by LoC — are consuming premium budget at multiples of their output. The three most severe cases (Tushar Patil, Nilesh Tonape, Pradnyesh Salunke, Sourabh Kalaskar) all show premium LoC exceeding total LoC, meaning every line of accepted code is costing more in premium feature tokens alone than the line represents. This is a compound cost: standard tokens + premium multiplier.

**Recommended Actions:**
- Review whether agent mode (multi-file) is the default session start for these users.
- Consider enabling Copilot usage guidelines for premium feature triggers (agent mode should be for complex multi-file tasks only, not single-file completions).
- Introduce a per-user premium LoC budget or alert threshold in the next CP cycle.

---

## Section 11 — Q2 Readiness Assessment

**Q2 Close: June 30, 2026 — 7 days remaining**

### Overall Team Status

| Category | Count | % of Active Users |
|---|---|---|
| Breakout | 1 (mshivarkar) | 3% |
| Rising (Final Tier) | 18 | 49% |
| Stable (Final Tier) | 5 | 14% |
| Zero Momentum (in-scope) | 5 | 14% |
| New Entrants | 8 | 22% |

**Positive Signals:**
- 49% of established users are at Rising tier after PR Quality Modifier application — this is a strong team-level quality signal.
- New entrant cohort (8 users) is actively onboarding with strong PR quality from abhijeetk268 (53 PRs, 92.5%) and dsuraj25 (1,169 LoC, 100% merge).
- PR quality across the team is exceptional: the majority of users maintain ≥80% merge rates, indicating code review health and delivery discipline.
- Breakout achievement (mshivarkar) demonstrates Copilot's ceiling capability is attainable.

**Q2 Risks:**
1. **Premium budget overrun** is the top systemic risk. At least 7 users are operating at unsustainable premium ratios. If this pattern holds through Q2 close, actual cost-per-LoC will be significantly above plan.
2. **Zero-momentum users** represent 14% of the established team with 7 days left. Any Q2 target tied to team aggregate LoC will be impacted.
3. **moadzughul's 361-hour average TTM** suggests a review bottleneck that may be blocking Q2 delivery despite high PR volume.
4. **rpawar-nice**: No delivery signal at all (0 PRs, 0 new LoC). Q2 contribution from this user is currently nil.
5. **jkumbhar's 281h TTM and 63.2% merge rate**: Delivery is occurring but at low efficiency — 7 PRs remain unmerged, which may block Q2 completion metrics.

**Q2 Recommendation Summary:**
- Managers to triage Zero-Momentum users by Jun 24 EOD.
- Budget review for premium overspend users to be flagged to VP before Q2 close.
- abhijeetk268 (53 PRs as new entrant) should be recognized — this is exceptional onboarding velocity.
- Confirm moadzughul's TTM root cause (large PRs vs. reviewer backlog vs. workflow config).

---

## Section 12 — ssnikam Special Note (Zero AI, High PR Activity)

### ssnikam — Sanket Nikam

```
CP8 LoC:    0
CP9 LoC:    0
Delta:      0
Premium:    0
PRs:        55 (49 merged, 89.1%)
Merge Rate: 89.1%
Avg TTM:    42h 2m
Manager:    ssamal-nice
```

**Assessment:** Sanket Nikam has the second-highest PR volume in the team (55 PRs) with an 89.1% merge rate and a very healthy 42-hour average time to merge. However, he has zero Copilot LoC at both CP8 and CP9 — not a stall, but a never-started baseline.

Sanket is delivering at a high pace entirely without AI augmentation. This is notable for two reasons:

1. **Missed opportunity:** At 55 PRs across the window, Sanket is clearly one of the most active contributors in the team. Copilot adoption for even 20–30% of his tasks would likely produce significant LoC and efficiency gains — and given his 89.1% merge rate, he clearly produces quality code. His accept rate potential is unknown but the underlying quality is demonstrated.

2. **Q2 AI adoption gap:** From a GitHub Copilot adoption KPI standpoint, Sanket is an unconverted high-performer. This is not a performance concern — it is an adoption conversation. The ROI case for Copilot is strongest for exactly this profile: high-velocity developers who are already demonstrating delivery quality.

**Recommended Action:** `ssamal-nice` to schedule a Copilot onboarding conversation with Sanket. Suggested framing: start with code completion on a current task, not agent mode. His PR velocity suggests the habit loop is already strong — Copilot adoption should add LoC acceleration on top of existing momentum, not disrupt it.

---

*Analysis generated: June 23, 2026 | Framework: Role Context + Momentum | Analyst: rwalunj-nice (Research — excluded from tier)*
*Next checkpoint: CP10 (projected ~Jul 3, 2026 — first Q3 data point)*
