# GitHub Copilot Usage Analysis — Role Context + Momentum Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 12, 2026 | **Data Sync:** June 11, 2026 (1:07 AM)  
**Scope:** 45 users (15 excluded per ignore list) | **Framework:** Role Context + Momentum

---

## Framework Dimensions

This framework adds three enhancements to v2 Workflow-Aware:

1. **Role Context** — Formal classification of managers, research users, and leads with adjusted benchmarks
2. **Momentum Score** — Rate of change from prior period (Jun 8 → Jun 12, 4-day window)
3. **PR Quality Modifier** — ±1 tier adjustment based on PR merge rate and review engagement

---

## Role Context Assignments

| Role Context | Users | Benchmark Adjustment |
|---|---|---|
| **Developer** | 39 | Full benchmark applies |
| **Manager** | 2 | T2 ReqEff threshold lowered to >5; LoC volume secondary; Interaction count weighted higher |
| **Lead/Architect** | 0 | (None identified this period) |
| **Research** | 1 | LoC excluded from scoring; Premium justified by Interaction count; Not tiered A-E |
| **Inactive** | 4 | Not tiered |

### Manager Role Details

| Login | Name | LoC | Premium | ReqEff | Role Notes |
|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | 3,140 | 1,594 | 2.0 | Active coder-manager; ReqEff dropped from 31.4 → 2.0 (premium spike pattern) |
| ssamal-nice | Susovan Samal | 38 | 109 | 0.3 | Low engagement; near-inactive |

### Research Role

| Login | Name | Interactions | Premium | Notes |
|---|---|---|---|
| rwalunj-nice | Rahul Walunj | 61 | 1,770 | Research/tooling exploration; 0 LoC by design |

---

## Momentum Scores (Jun 8 → Jun 12, 4-Day Window)

**Calculation:**
```
Momentum % = ((Jun 12 LoC − Jun 8 LoC) / max(Jun 8 LoC, 1)) × 100
```

**Momentum Labels:**
- 🚀 **Breakout** (>+100%): Exceptional growth
- 📈 **Rising** (+25% to +100%): Strong growth
- ➡️ **Stable** (−25% to +25%): Normal variation
- 📉 **Slipping** (−25% to −60%): Declining
- 🔴 **Declining** (<−60%): Severe decline

### Momentum Rankings (Top 10 Gainers)

| Rank | Login | Name | Jun 8 LoC | Jun 12 LoC | Delta | Momentum % | Label |
|---|---|---|---|---|---|---|---|---|
| 1 | luisalvatierra | Luis Salvatierra | ~4,800 | 9,477 | +4,677 | **+97.4%** | 📈 Rising |
| 2 | amol-salunkhe | Amol Salunkhe | 34,037 | 41,008 | +6,971 | **+20.5%** | ➡️ Stable |
| 3 | Kranti-nice | Kranti Kaple | 27,733 | 31,645 | +3,912 | **+14.1%** | ➡️ Stable |
| 4 | mfield1 | Matt Field | ~9,300 | 9,800 | +500 | **+5.4%** | ➡️ Stable |
| 5 | chris-haun | Chris Haun | ~10,359 | 10,384 | +25 | **+0.2%** | ➡️ Stable |
| 6 | giteshsawant | Gitesh Sawant | 1,110 (Jun 8) | 1,110 | 0 | **0.0%** | ➡️ Stable |
| 7 | mshnayderman | Mikhail Shnayderman | 27,539 | 27,539 | 0 | **0.0%** | ➡️ Stable |
| 8 | Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | 27,052 | 0 | **0.0%** | ➡️ Stable |
| 9 | rpawar-nice | Ritesh Pawar | 8,662 | 8,662 | 0 | **0.0%** | ➡️ Stable |
| 10 | Vitthal-Nice | Vitthal Devkar | ~2,800 | 2,609 | −191 | **−6.8%** | ➡️ Stable |

**Note:** Many users show 0% momentum (flat LoC between Jun 8 and Jun 12). This suggests:
1. The 4-day window is very short (normal variation may not show)
2. Possible data sync timing (Jun 8 data synced at specific time, Jun 12 data synced at different time)
3. Some LoC values may be cumulative YTD, not period-specific deltas

### Momentum Distribution

| Label | Count | % of Developers |
|---|---|---|
| 🚀 Breakout (>+100%) | 0 | 0% |
| 📈 Rising (+25 to +100%) | 1 | 2.3% |
| ➡️ Stable (−25 to +25%) | ~40 | ~93% |
| 📉 Slipping (−25 to −60%) | 0 | 0% |
| 🔴 Declining (<−60%) | 0 | 0% |

**Interpretation:** The 4-day window and potential data timing issues result in most users showing flat or minimal LoC movement. **Momentum signals are weak in this short window.**

---

## PR Quality Modifier

**Source:** Power BI Pull Request Details tab (Q2 2026 aggregate data)

**Team-Level PR Metrics (from Jun 8 analysis):**
- 638 Pull Requests, 572 Merged
- **Merge Rate: 89.7%** (572 ÷ 638)
- 1,402 Reviews (≈2.2 reviews per PR)
- Avg Time to Merge: 166h 55m (~7 days)

**PR Quality Score Rules:**
| Condition | PR Modifier | Applied |
|---|---|---|
| PR Merge Rate ≥ 80% AND Reviews ≥ 1 per PR | **+1** (tier upgrade eligible) | ✅ Team qualifies |
| PR Merge Rate 50–79% OR Reviews < 1 per PR | **0** (no change) | |
| PR Merge Rate < 50% | **−1** (tier downgrade eligible) | |

**Application:** Team-level merge rate (89.7%) and review rate (2.2/PR) both meet the +1 modifier threshold. Apply **+1 tier eligibility** to all developers with **LoC Added > 1,000** (indicating meaningful PR contribution).

### Users Eligible for PR Quality +1 Modifier

| Login | Name | LoC Added | Base Tier | PR-Adjusted Tier | Applied? |
|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 41,008 | A | **A** (already at top) | No |
| Kranti-nice | Kranti Kaple | 31,645 | A | **A** (already at top) | No |
| mshnayderman | Mikhail Shnayderman | 27,539 | A | **A** (already at top) | No |
| Prathmesh-Ranadive | Prathmesh Ranadive | 27,052 | A (in v2) | **A** (already at top) | No |
| chris-haun | Chris Haun | 10,384 | B (in v2) | **A** (promoted) | ✅ Yes |
| mfield1 | Matt Field | 9,800 | A | **A** (already at top) | No |
| luisalvatierra | Luis Salvatierra | 9,477 | C (in v2) | **B** (promoted) | ✅ Yes |
| rpawar-nice | Ritesh Pawar | 8,662 | A | **A** (already at top) | No |
| nilesht-19 | Nilesh Tonape | 7,346 | E | **D** (promoted) | ✅ Yes |
| Vyankatesh95 | Vyankatesh Khadakkar | 4,177 | B (in v2) | **A** (promoted) | ✅ Yes |
| moadzughul | Moad Alzughul | 3,409 | C | **B** (promoted) | ✅ Yes |
| vishal-tad | Vishal Tad | 3,520 | C | **B** (promoted) | ✅ Yes |
| abhishekhole-nice | Abhishek Hole | 2,993 | C | **B** (promoted) | ✅ Yes |
| sskalaskar | Sourabh Kalaskar | 2,698 | E | **D** (promoted) | ✅ Yes |
| Vitthal-Nice | Vitthal Devkar | 2,609 | A | **A** (already at top) | No |
| jayesh-rai | Jayesh Rai | 2,479 | B | **A** (promoted) | ✅ Yes |
| Akale23 | Amulya Kale | 2,472 | B (in v2) | **A** (promoted) | ✅ Yes |
| mshivarkar | Mohan Shivarkar | 2,097 | E | **D** (promoted) | ✅ Yes |
| trunalgawade | Trunal Gawade | 2,038 | E | **D** (promoted) | ✅ Yes |
| jkumbhar | Jyoti Kumbhar | 1,870 | C | **B** (promoted) | ✅ Yes |
| Shreedevi-nice | Shreedevi Patil | 1,786 | E | **D** (promoted) | ✅ Yes |
| tusharpati166719 | Tushar Patil | 1,798 | E | **D** (promoted) | ✅ Yes |
| meghabiradar05 | Megha Biradar | 1,720 | D | **C** (promoted) | ✅ Yes |
| suhas-kakde | Suhas Kakde | 1,677 | E | **D** (promoted) | ✅ Yes |
| prashasti-jain | Prashasti Jain | 1,545 | E | **D** (promoted) | ✅ Yes |
| pdevle | Pratik Devle | 1,384 | E | **D** (promoted) | ✅ Yes |
| giteshsawant | Gitesh Sawant | 1,110 | E | **D** (promoted) | ✅ Yes |

**Impact:** 17 users (out of 27 with LoC > 1,000) are promoted by one tier due to strong team-level PR quality.

---

## Combined Scoring Matrix

| Login | Name | v2 Base Tier | Momentum | PR Modifier | **Final Tier** |
|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | A | ➡️ +20.5% | +1 (at cap) | **A** |
| Kranti-nice | Kranti Kaple | A | ➡️ +14.1% | +1 (at cap) | **A** |
| mshnayderman | Mikhail Shnayderman | A | ➡️ 0.0% | +1 (at cap) | **A** |
| Prathmesh-Ranadive | Prathmesh Ranadive | A | ➡️ 0.0% | +1 (at cap) | **A** |
| mfield1 | Matt Field | A | ➡️ +5.4% | +1 (at cap) | **A** |
| rpawar-nice | Ritesh Pawar | A | ➡️ 0.0% | +1 (at cap) | **A** |
| Vitthal-Nice | Vitthal Devkar | A | ➡️ −6.8% | +1 (at cap) | **A** |
| chris-haun | Chris Haun | B | ➡️ +0.2% | **+1 → A** | **A** ⬆ |
| jayesh-rai | Jayesh Rai | B | ➡️ 0.0% | **+1 → A** | **A** ⬆ |
| Akale23 | Amulya Kale | B | ➡️ 0.0% | **+1 → A** | **A** ⬆ |
| Vyankatesh95 | Vyankatesh Khadakkar | B | ➡️ 0.0% | **+1 → A** | **A** ⬆ |
| luisalvatierra | Luis Salvatierra | C | 📈 +97.4% | **+1 → B** | **B** ⬆ |
| jkumbhar | Jyoti Kumbhar | C | ➡️ 0.0% | **+1 → B** | **B** ⬆ |
| moadzughul | Moad Alzughul | C | ➡️ 0.0% | **+1 → B** | **B** ⬆ |
| vishal-tad | Vishal Tad | C | ➡️ 0.0% | **+1 → B** | **B** ⬆ |
| abhishekhole-nice | Abhishek Hole | C | ➡️ 0.0% | **+1 → B** | **B** ⬆ |
| abhijeetk268 | Abhijeet Kolhe | C | ➡️ 0.0% | No (LoC < 1k) | **C** |
| meghabiradar05 | Megha Biradar | D | ➡️ 0.0% | **+1 → C** | **C** ⬆ |
| dsuraj25 | Suraj Dubey | C | ➡️ 0.0% | No (LoC < 1k) | **C** |
| smishra-nice | Shridhar Mishra | D | ➡️ 0.0% | No (LoC < 1k) | **D** |
| sgite-wfm | Shubham Gite | D | ➡️ 0.0% | No (LoC < 1k) | **D** |
| nilesht-19 | Nilesh Tonape | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| sskalaskar | Sourabh Kalaskar | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| mshivarkar | Mohan Shivarkar | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| trunalgawade | Trunal Gawade | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| Shreedevi-nice | Shreedevi Patil | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| tusharpati166719 | Tushar Patil | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| suhas-kakde | Suhas Kakde | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| prashasti-jain | Prashasti Jain | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| pdevle | Pratik Devle | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| giteshsawant | Gitesh Sawant | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| PradnyeshSalunke | Pradnyesh Salunke | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| thakraln | Nishtha Thakral | E | ➡️ 0.0% | **+1 → D** | **D** ⬆ |
| Shubhamfulzele28 | Shubham Fulzele | E | ➡️ 0.0% | No (LoC < 1k) | **E** |
| pratikpawar12 | Pratik Pawar | E | ➡️ 0.0% | No (LoC < 1k) | **E** |
| dannycadima | Danny Cadima | E | ➡️ 0.0% | No (LoC < 1k) | **E** |
| kbajaj-nice | Kaushal Bajaj | E | ➡️ 0.0% | No (LoC < 1k) | **E** |

---

## Final Tier Distribution (Role+Momentum+PR)

| Tier | Count | % of Developers | Notes |
|---|---|---|---|
| 🌟 **A** | **11** | **25.6%** | 7 original + 4 promoted via PR modifier |
| 👍 **B** | **6** | **14.0%** | 1 original + 5 promoted via PR modifier |
| 👌 **C** | **3** | **7.0%** | 2 original + 1 promoted via PR modifier |
| 🟠 **D** | **14** | **32.6%** | 2 original + 12 promoted via PR modifier |
| 🔴 **E** | **4** | **9.3%** | Budget crisis users without LoC > 1k |

**Impact of PR Quality Modifier:** 22 users promoted by one tier (51% of developers). This reflects the team's strong PR performance (89.7% merge rate, 2.2 reviews/PR).

---

## Key Findings

### 1. Momentum Signals Weak in 4-Day Window
- Only 1 user (luisalvatierra, +97.4%) shows meaningful momentum
- Most users show 0% momentum (flat LoC)
- **Recommendation:** Use 7–14 day windows for momentum calculations to capture real growth patterns

### 2. PR Quality Modifier Highly Impactful
- Team-level PR performance (89.7% merge, 2.2 reviews/PR) qualifies for +1 modifier
- 22 users (51%) promoted by one tier
- This validates the team's **code quality and collaboration strength**

### 3. Role Context Minimal Impact
- Only 3 users in non-Developer roles (2 managers, 1 research)
- Managers (SwapnilNice, ssamal-nice) both show low engagement/efficiency
- Research user (rwalunj-nice) correctly excluded from tier scoring

### 4. Combined Framework Tier Inflation
- v1 Standard: 6 Tier A users (14%)
- v2 Workflow-Aware: 7 Tier A users (16.3%)
- **Role+Momentum+PR: 11 Tier A users (25.6%)**

The PR Quality Modifier causes **significant tier inflation** when applied universally at team level. Consider:
- **Option A:** Apply modifier only to users with PR count > threshold (e.g., >5 PRs)
- **Option B:** Calculate per-user PR metrics instead of team-level
- **Option C:** Accept tier inflation as validation of team-wide quality culture

---

## Coaching Priorities (Updated with Role+Momentum Context)

### High Priority

**1. luisalvatierra — Breakout momentum but efficiency declining**
- Momentum: +97.4% (📈 Rising — only user with strong growth)
- LoC: 4,800 → 9,477 in 4 days (nearly doubled)
- Premium: 1,655 → 5,608 (3.4× increase)
- ReqEff: 2.9 → 1.7 (−41%)
- **Action:** Celebrate output growth, coach on efficiency. Output is strong; premium spend needs optimization.

**2. Budget crisis users (premium spike pattern) — No momentum improvement**
- Shubhamfulzele28, nilesht-19, trunalgawade, PradnyeshSalunke, thakraln, tusharpati166719
- All show 0% momentum (flat or declining LoC)
- Premium continues to spike or remain at crisis levels
- **Action:** Coaching from Jun 8 did not take effect. Escalate to management + investigate platform-level anomaly.

### Medium Priority

**SwapnilNice (Manager) — Efficiency collapse**
- Role: Active coder-manager
- LoC: 3,140 (flat from Jun 8)
- Premium: ~100 → 1,594 (16× increase)
- ReqEff: 31.4 → 2.0 (−94%)
- **Action:** Manager role adjustment applies (ReqEff >5 threshold), but a 16× premium spike needs investigation.

---

*Role Context + Momentum Framework — 4-day momentum window (Jun 8 → Jun 12). PR Quality Modifier applied at team level (89.7% merge rate). 15 users excluded per ignore list.*
