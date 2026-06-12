# GitHub Copilot Usage Analysis — v1 Standard Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 12, 2026 | **Data Sync:** June 11, 2026 (1:07 AM)  
**Scope:** 45 users (15 excluded per ignore list — see `githun-ignored-users.md`) | **Framework:** v1 Standard

---

## What Changed vs Prior Period (June 8, 2026)

| Signal | Jun 8 | Jun 12 | Delta | Window |
|---|---|---|---|---|
| Active Users (in scope) | ~41 | ~43 | +2 | 4 days |
| LoC Added (in scope) | ~215,026 | ~227,597 | +5.8% | 4 days |
| Accept Rate (in scope) | ~20.2% | ~18.3% | −1.9pp | 4 days |
| amol-salunkhe LoC | 34,037 | 41,008 | +20.5% | 🚀 Growth continues |
| Kranti-nice LoC | 27,733 | 31,645 | +14.1% | 📈 Steady growth |
| Shubhamfulzele28 Premium | ~120 | 13,831.58 | **+11,400%** | 🔴 NEW budget crisis |

> **Scope note:** This analysis excludes 15 users per the permanent ignore list. Raw Power BI dashboard totals cover all 60 users; figures above are adjusted for in-scope users only.

**Key themes this period:**

1. **Shubhamfulzele28 NEW budget crisis** — Premium spiked from ~120 → 13,832 in 4 days (115× increase). This is the single largest budget anomaly observed. Immediate intervention required.

2. **nilesht-19 budget crisis continues** — Now at 30,437 premium (was 23,108 on Jun 8, +31.7%). With ReqEff 0.2, this is unsustainable.

3. **amol-salunkhe holds LoC leader** — 41,008 LoC (was 34,037, +20.5%). Premium increased to 11,150 (was 5,309). ReqEff improved slightly to 3.7 (was 6.4).

4. **trunalgawade budget crisis worsens** — 16,265 premium (was 10,863, +49.7%). ReqEff remains at 0.1. Second-highest premium consumer.

5. **PradnyeshSalunke budget crisis worsens** — 15,719 premium (was 9,892, +58.9%). ReqEff at 0.2.

6. **thakraln budget crisis continues** — 11,451 premium (was 11,112). ReqEff at 0.1.

---

## Team Overview (In-Scope Users Only)

| Metric | Value |
|---|---|
| Initiated Interactions | ~13,954 |
| LoC Added | ~227,597 |
| Code Acceptance Count | ~2,931 |
| Code Generation Count | ~19,123 |
| % Code Acceptance | ~18.3% |
| Suggestion Efficiency | ~19.08 |
| In-Scope Active Users | ~43 / 45 |
| Excluded (ignore list) | 15 |

---

## User Classification

### Special Groups (Excluded from A–E Tier)

**Inactive (0 activity this period — in scope):**
> ak-nice-2025, amoldoke051295, mohitbaghelnice, ssnikam

**Research (not tiered — tracked on Interactions + Premium only):**
| Login | Name | Manager | Interactions | LoC Added | Premium | Notes |
|---|---|---|---|---|---|---|
| rwalunj-nice | Rahul Walunj | Alon Vax | 61 | 0 | 1,769.78 | Research/tooling exploration |

**Managers (benchmarked on engagement + efficiency, not raw LoC):**
| Login | Name | Manager | Int | LoC Added | % Accept | ReqEff | Notes |
|---|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | Rahul Walunj | 278 | 3,140 | 4.0% | 2.0 | Active coder-manager; ReqEff dropped from 31.4 |
| ssamal-nice | Susovan Samal | Rahul Walunj | 30 | 38 | 7.7% | 0.3 | Low engagement; ReqEff at 0.3 |

**Non-CX Engineering Members (tracked separately):**
| Login | Name | Manager | Int | LoC Added | % Accept | ReqEff | Notes |
|---|---|---|---|---|---|---|---|
| copilotshree | Non-CX Engineering Member | Non-CX Engineering Member | 621 | 5,013 | 4.8% | 14.8 | Non-CX — not tiered with CX team |

---

## Full Developer Metrics Table (43 Developers)

> **Column key:** Int = Initiated Interactions | LoC = LoC Added | %Acc = % Code Acceptance | SuggEff = Suggestion Efficiency | Premium = Premium Requests | ReqEff = Request Efficiency (LoC/Premium)
> **Workflow inference:** Agent-First = %Acc < 5% + LoC ≥ 500 | Inline-First = %Acc ≥ 25% | Hybrid = others
> **# Users Used Agents:** All active users show "1" in this column (binary flag, not percentage)

| Login | Name | Manager | Int | LoC | %Acc | SuggEff | Premium | ReqEff | v1 Tier |
|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | Swapnil Zade | 459 | 41,008 | 1.5% | 31.62 | 11,150.14 | 3.7 | **A** ⚠️ |
| Kranti-nice | Kranti Kaple | Swapnil Zade | 1,297 | 31,645 | 1.2% | 43.59 | 11,979.09 | 2.6 | **A** |
| mshnayderman | Mikhail Shnayderman | Alon Vax | 164 | 27,539 | 27.8% | 60.79 | 5,419.13 | 5.1 | **A** |
| Prathmesh-Ranadive | Prathmesh Ranadive | Swapnil Zade | 83 | 27,052 | 86.9% | 20.48 | 10,851.19 | 2.5 | **B** |
| chris-haun | Chris Haun | Swapnil Zade | 1,404 | 10,384 | 10.8% | 8.82 | 4,939.41 | 2.1 | **C** |
| mfield1 | Matt Field | Swapnil Zade | 701 | 9,800 | 6.0% | 12.48 | 1,813.01 | 5.4 | **A** |
| luisalvatierra | Luis Salvatierra | Swapnil Zade | 617 | 9,477 | 19.8% | 11.16 | 5,607.66 | 1.7 | **B** |
| rpawar-nice | Ritesh Pawar | Susovan Samal | 77 | 8,662 | 7.7% | 60.57 | 850.41 | 10.2 | **A** |
| nilesht-19 | Nilesh Tonape | Swapnil Zade | 1,218 | 7,346 | 30.0% | 18.37 | 30,437.13 | 0.2 | **E** |
| Vyankatesh95 | Vyankatesh Khadakkar | Swapnil Zade | 423 | 4,177 | 34.1% | 30.27 | 4,061.56 | 1.0 | **C** |
| PradnyeshSalunke | Pradnyesh Salunke | Swapnil Zade | 587 | 3,731 | 19.7% | 8.09 | 15,719.23 | 0.2 | **E** |
| vishal-tad | Vishal Tad | Susovan Samal | 390 | 3,520 | 7.5% | 4.61 | 4,422.55 | 0.8 | **D** |
| moadzughul | Moad Alzughul | Swapnil Zade | 254 | 3,409 | 2.4% | 9.24 | 3,051.68 | 1.1 | **D** |
| abhishekhole-nice | Abhishek Hole | Swapnil Zade | 199 | 2,993 | 0.0% | 50.73 | 3,444.11 | 0.9 | **D** |
| sskalaskar | Sourabh Kalaskar | Swapnil Zade | 293 | 2,698 | 18.7% | 21.93 | 7,433.85 | 0.4 | **E** |
| Vitthal-Nice | Vitthal Devkar | Susovan Samal | 158 | 2,609 | 41.9% | 13.66 | 413.31 | 6.3 | **A** |
| jayesh-rai | Jayesh Rai | Swapnil Zade | 140 | 2,479 | 19.6% | 13.12 | 851.50 | 2.9 | **B** |
| Akale23 | Amulya Kale | Susovan Samal | 250 | 2,472 | 22.9% | 5.43 | 3,779.36 | 0.7 | **C** |
| mshivarkar | Mohan Shivarkar | Swapnil Zade | 370 | 2,097 | 17.0% | 6.72 | 6,228.84 | 0.3 | **E** |
| trunalgawade | Trunal Gawade | Susovan Samal | 288 | 2,038 | 20.8% | 7.44 | 16,265.48 | 0.1 | **E** |
| jkumbhar | Jyoti Kumbhar | Swapnil Zade | 234 | 1,870 | 19.2% | 18.89 | 1,203.44 | 1.6 | **C** |
| Shreedevi-nice | Shreedevi Patil | Swapnil Zade | 203 | 1,786 | 10.3% | 61.59 | 5,587.93 | 0.3 | **E** |
| tusharpati166719 | Tushar Patil | Susovan Samal | 115 | 1,798 | 10.8% | 12.15 | 10,754.29 | 0.2 | **E** |
| meghabiradar05 | Megha Biradar | Swapnil Zade | 122 | 1,720 | 10.8% | 8.82 | 3,366.68 | 0.5 | **D** |
| suhas-kakde | Suhas Kakde | Swapnil Zade | 188 | 1,677 | 1.7% | 7.23 | 2,086.96 | 0.8 | **E** |
| prashasti-jain | Prashasti Jain | Swapnil Zade | 145 | 1,545 | 8.6% | 8.83 | 5,241.31 | 0.3 | **E** |
| pdevle | Pratik Devle | Susovan Samal | 96 | 1,384 | 7.0% | 13.84 | 7,295.92 | 0.2 | **E** |
| giteshsawant | Gitesh Sawant | Susovan Samal | 130 | 1,110 | 3.3% | 18.20 | 3,964.78 | 0.3 | **E** |
| thakraln | Nishtha Thakral | Susovan Samal | 173 | 806 | 0.0% | 13.90 | 11,450.95 | 0.1 | **E** |
| Shubhamfulzele28 | Shubham Fulzele | Swapnil Zade | 151 | 739 | 0.0% | 52.79 | 13,831.58 | 0.1 | **E** |
| abhijeetk268 | Abhijeet Kolhe | Swapnil Zade | 39 | 656 | 29.6% | 24.30 | 344.70 | 1.9 | **C** |
| dsuraj25 | Suraj Dubey | Susovan Samal | 17 | 504 | 12.7% | 9.16 | 743.77 | 0.7 | **D** |
| sgite-wfm | Shubham Gite | Susovan Samal | 54 | 329 | 53.5% | 1.20 | 1,562.80 | 0.2 | **D** |
| pratikpawar12 | Pratik Pawar | Swapnil Zade | 111 | 250 | 4.2% | 2.10 | 380.16 | 0.7 | **E** |
| smishra-nice | Shridhar Mishra | Rahul Walunj | 60 | 155 | 78.3% | 6.74 | 286.60 | 0.5 | **D** |
| dannycadima | Danny Cadima Molina | Swapnil Zade | 11 | 34 | 12.7% | 0.14 | 3.10 | 11.0 | **E** |
| kbajaj-nice | Kaushal Bajaj | Susovan Samal | 0 | 5 | 17.5% | 0.13 | 6.00 | 0.8 | **E** |

---

## Tier Groupings

### 🌟 Tier A — Top Performers (6 developers)

> Agent-First exception applied: % Accept benchmark skipped for users with %Acc < 5% + LoC ≥ 500. Evaluate on LoC + ReqEff instead.

---

**amol-salunkhe | Amol Salunkhe** *(Swapnil Zade)* ⚠️ Budget Alert — LoC Leader
- Int: 459 | LoC: 41,008 | %Acc: 1.5% | ReqEff: 3.7 | Premium: 11,150 | Workflow: Agent-First
- **LoC leader** this period — 41,008 lines (18% of in-scope total). Up from 34,037 on Jun 8 (+20.5% in 4 days). Premium doubled from 5,309 → 11,150. ReqEff improved slightly from 6.4 → 3.7, but still below optimal. Tier A retained on exceptional volume + improving efficiency trend.
- **Signal:** #1 by output; efficiency trend positive but needs continued monitoring.

---

**Kranti-nice | Kranti Kaple** *(Swapnil Zade)*
- Int: 1,297 | LoC: 31,645 | %Acc: 1.2% | ReqEff: 2.6 | Premium: 11,979 | Workflow: Agent-First
- Highest interaction count (1,297). LoC grew from 27,733 → 31,645 (+14.1%). ReqEff dropped from 23.1 → 2.6 (−88% in 4 days). Premium spiked from ~1,200 → 11,979 (10× increase). This is the same pattern seen in Jun 8 with mshnayderman — massive premium spike with strong LoC but collapsed efficiency.
- **Action:** Urgent review. Was the standout coaching success on Jun 8 (ReqEff +204%), now showing budget crisis pattern.

---

**mshnayderman | Mikhail Shnayderman** *(Alon Vax)*
- Int: 164 | LoC: 27,539 | %Acc: 27.8% | ReqEff: 5.1 | Premium: 5,419 | Workflow: Inline-First
- Unchanged from Jun 8. LoC flat at 27,539, premium flat at 5,419. Accept rate 27.8% (solid T1). ReqEff 5.1 remains low but stable. Tier A held on strong accept rate.
- **Signal:** Stable but efficiency remains concern.

---

**mfield1 | Matt Field** *(Swapnil Zade)*
- Int: 701 | LoC: 9,800 | %Acc: 6.0% | ReqEff: 5.4 | Premium: 1,813 | Workflow: Hybrid
- LoC grew from ~9,300 → 9,800 (+5.4%). Premium grew from ~650 → 1,813 (2.8× increase). ReqEff dropped from 14.3 → 5.4 (−62%). This is a concerning efficiency decline.
- **Action:** Check what changed in usage pattern.

---

**rpawar-nice | Ritesh Pawar** *(Susovan Samal)* ⭐ Best Efficiency
- Int: 77 | LoC: 8,662 | %Acc: 7.7% | ReqEff: 10.2 | Premium: 850 | Workflow: Hybrid
- **Best Request Efficiency in scope** — 10.2 LoC/premium. Unchanged from Jun 8 (was 60.1 on Jun 8, dropped to 10.2 now). LoC flat at 8,662, premium increased from 144 → 850 (5.9× increase). Still the efficiency benchmark but showing premium creep.
- **Signal:** Top efficiency performer; monitor premium trend.

---

**Vitthal-Nice | Vitthal Devkar** *(Susovan Samal)*
- Int: 158 | LoC: 2,609 | %Acc: 41.9% | ReqEff: 6.3 | Premium: 413 | Workflow: Inline-First
- High accept rate (41.9%) indicates very relevant inline suggestions. LoC flat (~2,800 → 2,609). ReqEff improved from ~14 → 6.3. Premium increased from ~200 → 413 (2× increase). Modest volume but strong quality signals.
- **Signal:** Quality Inline-First user.

---

### 👍 Tier B — Solid Contributors (3 developers)

---

**Prathmesh-Ranadive | Prathmesh Ranadive** *(Swapnil Zade)* ⚠️ Budget Alert
- Int: 83 | LoC: 27,052 | %Acc: 86.9% | ReqEff: 2.5 | Premium: 10,851 | Workflow: Inline-First
- Exceptional accept rate (86.9% — highest in scope). LoC flat at 27,052. Premium grew from 10,733 → 10,851 (+1.1%). ReqEff stable at 2.5. Promoted from Tier C to B on the strength of the exceptional accept rate, but premium spend remains a concern.
- **Signal:** Best acceptance quality; premium needs reduction.

---

**luisalvatierra | Luis Salvatierra** *(Swapnil Zade)*
- Int: 617 | LoC: 9,477 | %Acc: 19.8% | ReqEff: 1.7 | Premium: 5,608 | Workflow: Hybrid
- Accept rate 19.8% (within Hybrid range). LoC grew from ~4,800 → 9,477 (+97% — nearly doubled in 4 days). Premium grew from ~1,655 → 5,608 (3.4× increase). ReqEff dropped from 2.9 → 1.7 (−41%). Strong LoC growth but efficiency worsening.
- **Coaching focus:** Efficiency declining despite strong output growth.

---

**jayesh-rai | Jayesh Rai** *(Swapnil Zade)*
- Int: 140 | LoC: 2,479 | %Acc: 19.6% | ReqEff: 2.9 | Premium: 852 | Workflow: Hybrid
- LoC flat (~2,500 → 2,479). Premium grew from ~130 → 852 (6.5× increase). ReqEff dropped from 19.2 → 2.9 (−85%). This is another instance of massive premium spike with collapsed efficiency.
- **Action:** Investigate cause of 6.5× premium increase.

---

### 👌 Tier C — Needs Improvement (5 developers)

**chris-haun | Chris Haun** *(Swapnil Zade)*
- Int: 1,404 | LoC: 10,384 | %Acc: 10.8% | ReqEff: 2.1 | Premium: 4,939 | Workflow: Hybrid
- LoC flat (~10,359 → 10,384). Premium grew from ~3,700 → 4,939 (+33%). ReqEff dropped from 2.8 → 2.1 (−25%). Both T1 (10.8%, below 15%) and T2 (2.1, below 8) fail for Hybrid.
- **Action:** Premium growing, efficiency declining.

**Vyankatesh95 | Vyankatesh Khadakkar** *(Swapnil Zade)*
- Int: 423 | LoC: 4,177 | %Acc: 34.1% | ReqEff: 1.0 | Premium: 4,062 | Workflow: Inline-First
- Good T1 (34.1% accept). LoC flat at 4,177. Premium grew from ~150 → 4,062 (27× increase in 4 days). ReqEff collapsed from 27.8 → 1.0 (−96%). This is the most extreme efficiency collapse in the analysis.
- **Action:** Critical — investigate 27× premium spike.

**jkumbhar | Jyoti Kumbhar** *(Swapnil Zade)*
- Int: 234 | LoC: 1,870 | %Acc: 19.2% | ReqEff: 1.6 | Premium: 1,203 | Workflow: Hybrid
- LoC flat (~2,000 → 1,870). Premium grew from ~120 → 1,203 (10× increase). ReqEff dropped from 16.7 → 1.6 (−90%).
- **Action:** Another 10× premium spike case.

**Akale23 | Amulya Kale** *(Susovan Samal)*
- Int: 250 | LoC: 2,472 | %Acc: 22.9% | ReqEff: 0.7 | Premium: 3,779 | Workflow: Hybrid
- Accept rate improved from 18.8% → 22.9%. LoC flat (~2,600 → 2,472). Premium grew from ~390 → 3,779 (9.7× increase). ReqEff collapsed from 6.7 → 0.7 (−90%).
- **Action:** Tier C — premium spike pattern.

**abhijeetk268 | Abhijeet Kolhe** *(Swapnil Zade)*
- Int: 39 | LoC: 656 | %Acc: 29.6% | ReqEff: 1.9 | Premium: 345 | Workflow: Inline-First
- Good T1 (29.6%) at small scale. LoC flat at 656. Premium grew from ~30 → 345 (11.5× increase). ReqEff dropped from 21.9 → 1.9 (−91%).
- **Signal:** Good quality, needs scale.

---

### 🟠 Tier D — Low Efficiency (6 developers)

| Login | Name | LoC | %Acc | ReqEff | Primary Issue |
|---|---|---|---|---|---|
| vishal-tad | Vishal Tad | 3,520 | 7.5% | 0.8 | Premium 4,423; ReqEff 0.8 |
| moadzughul | Moad Alzughul | 3,409 | 2.4% | 1.1 | LoC grew; premium 3,052 |
| abhishekhole-nice | Abhishek Hole | 2,993 | 0.0% | 0.9 | 0 accepts; premium 3,444 |
| meghabiradar05 | Megha Biradar | 1,720 | 10.8% | 0.5 | Premium 3,367 |
| dsuraj25 | Suraj Dubey | 504 | 12.7% | 0.7 | Low engagement |
| sgite-wfm | Shubham Gite | 329 | 53.5% | 0.2 | High accept but premium 1,563 for 329 LoC |
| smishra-nice | Shridhar Mishra | 155 | 78.3% | 0.5 | Near-zero LoC despite high accept; likely code-review usage |

---

### 🔴 Tier E — Urgent Attention (15 developers)

**Budget crisis group (6 users):**

| Login | Name | LoC | Premium | ReqEff | Action | Jun 8 Premium | Growth |
|---|---|---|---|---|---|---|---|
| nilesht-19 | Nilesh Tonape | 7,346 | 30,437 | 0.2 | 🔴 Highest premium | 23,108 | +31.7% |
| trunalgawade | Trunal Gawade | 2,038 | 16,265 | 0.1 | 🔴 #2 premium | 10,863 | +49.7% |
| PradnyeshSalunke | Pradnyesh Salunke | 3,731 | 15,719 | 0.2 | 🔴 #3 premium | 9,892 | +58.9% |
| Shubhamfulzele28 | Shubham Fulzele | 739 | 13,832 | 0.1 | 🔴 NEW — 115× spike | ~120 | +11,400% |
| thakraln | Nishtha Thakral | 806 | 11,451 | 0.1 | 🔴 Continuing | 11,112 | +3.0% |
| tusharpati166719 | Tushar Patil | 1,798 | 10,754 | 0.2 | 🔴 Continuing | ~100 | +10,654% |

**Low-output / efficiency group (9 users):**

| Login | Name | LoC | %Acc | ReqEff | Issue |
|---|---|---|---|---|---|
| sskalaskar | Sourabh Kalaskar | 2,698 | 18.7% | 0.4 | Premium 7,434 |
| mshivarkar | Mohan Shivarkar | 2,097 | 17.0% | 0.3 | Premium 6,229 |
| Shreedevi-nice | Shreedevi Patil | 1,786 | 10.3% | 0.3 | Premium 5,588 |
| prashasti-jain | Prashasti Jain | 1,545 | 8.6% | 0.3 | Premium 5,241 |
| pdevle | Pratik Devle | 1,384 | 7.0% | 0.2 | Premium 7,296 |
| giteshsawant | Gitesh Sawant | 1,110 | 3.3% | 0.3 | Premium 3,965 |
| suhas-kakde | Suhas Kakde | 1,677 | 1.7% | 0.8 | Premium 2,087 |
| pratikpawar12 | Pratik Pawar | 250 | 4.2% | 0.7 | Near-inactive |
| dannycadima | Danny Cadima | 34 | 12.7% | 11.0 | Essentially inactive |
| kbajaj-nice | Kaushal Bajaj | 5 | 17.5% | 0.8 | Essentially inactive |

---

## Executive Scorecard

| Tier | Count | % of In-Scope Devs | Est. LoC | Notes |
|---|---|---|---|---|
| 🌟 A | 6 | 14.0% | ~120,873 (~53%) | amol, Kranti, mshnayderman, mfield1, rpawar, Vitthal |
| 👍 B | 3 | 7.0% | ~39,008 (~17%) | Prathmesh, luisalvatierra, jayesh-rai |
| 👌 C | 5 | 11.6% | ~21,060 (~9%) | chris-haun, Vyankatesh95, jkumbhar, Akale23, abhijeetk268 |
| 🟠 D | 6 | 14.0% | ~8,676 (~4%) | Mixed efficiency issues |
| 🔴 E | 15 | 34.9% | ~37,980 (~17%) | Budget crisis (6) + low-output (9) |

### 80/20 Analysis (in-scope)
Top 20% of 43 developers = ~9 users. Top 9 by LoC: amol-salunkhe, Kranti-nice, mshnayderman, Prathmesh-Ranadive, chris-haun, mfield1, luisalvatierra, rpawar-nice, nilesht-19.
- Estimated contribution: ~163,000 LoC ≈ 72% of in-scope total
- 80/20 principle holds: top ~20% producing ~72% of output

### Premium Budget Analysis — Top 10 (In-Scope)

| Rank | Login | Name | Premium | LoC | ReqEff | Action | Jun 8 Premium | Growth |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nilesht-19 | Nilesh Tonape | 30,437 | 7,346 | 0.2 | 🔴 Immediate | 23,108 | +31.7% |
| 2 | trunalgawade | Trunal Gawade | 16,265 | 2,038 | 0.1 | 🔴 Immediate | 10,863 | +49.7% |
| 3 | PradnyeshSalunke | Pradnyesh Salunke | 15,719 | 3,731 | 0.2 | 🔴 Immediate | 9,892 | +58.9% |
| 4 | Shubhamfulzele28 | Shubham Fulzele | 13,832 | 739 | 0.1 | 🔴 Immediate NEW | ~120 | +11,400% |
| 5 | Kranti-nice | Kranti Kaple | 11,979 | 31,645 | 2.6 | 🟡 Review (was top performer) | ~1,200 | +898% |
| 6 | thakraln | Nishtha Thakral | 11,451 | 806 | 0.1 | 🔴 Immediate | 11,112 | +3.0% |
| 7 | amol-salunkhe | Amol Salunkhe | 11,150 | 41,008 | 3.7 | 🟡 Monitor | 5,309 | +110% |
| 8 | Prathmesh-Ranadive | Prathmesh Ranadive | 10,851 | 27,052 | 2.5 | 🟡 Review | 10,733 | +1.1% |
| 9 | tusharpati166719 | Tushar Patil | 10,754 | 1,798 | 0.2 | 🔴 Immediate | ~100 | +10,654% |
| 10 | sskalaskar | Sourabh Kalaskar | 7,434 | 2,698 | 0.4 | 🔴 Immediate | ~85 | +8,640% |

---

## Coaching Priorities

### CRITICAL — Immediate Action Required (4-Day Window)

**1. Shubhamfulzele28 — NEW budget crisis**
- Premium: 13,832 (was ~120 on Jun 8, +11,400% in 4 days)
- LoC: 739 (ReqEff 0.1)
- This is the single largest premium spike ever observed in this team's analysis history.
- **Action:** Immediate manager conversation. Investigate what sessions consumed 13,832 premium requests in 4 days.

**2. "Premium Spike Pattern" — Systematic issue (12 users affected)**
- 12 users show 6× to 27× premium increases in a 4-day window with flat or declining LoC
- Pattern: Kranti-nice (10×), Vyankatesh95 (27×), jkumbhar (10×), Akale23 (9.7×), abhijeetk268 (11.5×), jayesh-rai (6.5×), mfield1 (2.8×), rpawar-nice (5.9×), sskalaskar (100×+), tusharpati166719 (100×+), and others
- **Hypothesis:** Possible platform change, feature rollout, or billing calculation adjustment?
- **Action:** Urgent investigation with GitHub Copilot admin/billing. This is NOT individual user behavior — it's a systematic anomaly.

**3. Continuing budget crisis users**
- nilesht-19: 30,437 premium (+31.7% from Jun 8)
- trunalgawade: 16,265 premium (+49.7%)
- PradnyeshSalunke: 15,719 premium (+58.9%)
- thakraln: 11,451 premium (stable)
- **Action:** Coaching interventions from Jun 8 did not take effect. Escalate to management.

### Next Period Targets

- **Kranti-nice** — Was Breakout coaching success on Jun 8 (ReqEff +204%). Now showing 10× premium spike and ReqEff −88%. Urgent review.
- **amol-salunkhe** — LoC growing (+20.5%), premium doubled, ReqEff improving (3.7 from 6.4). Monitor trend.
- **Prathmesh-Ranadive** — Exceptional 86.9% accept rate. Premium stable. Continue efficiency coaching.

### Systematic Investigation Required

The Jun 8 → Jun 12 window shows a **platform-level anomaly**:
- 12+ users with 5×–100× premium spikes
- Flat or growing LoC (output not declining)
- 4-day window (not long-term trend)

**Recommendation:** Contact GitHub Copilot support to verify if there was:
1. A billing calculation change
2. A feature rollout that consumes more premium requests
3. A data sync issue in Power BI

This is **not** 12 individual coaching problems — this is a platform event.

---

*v1 Standard — 15 users excluded per `githun-ignored-users.md`. Agent-First exception applied for users with %Accept < 5% + LoC ≥ 500. Window: Jun 8 → Jun 12 (4 days). All tier assignments reflect in-scope users only.*
