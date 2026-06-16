# GitHub Copilot Multi-Period Analysis — C+R Score Evolution
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Period:** April 20 → June 12, 2026 (53 days, 8 checkpoints)  
**Framework:** CRQC (Core + ROI Score Evolution)

---

## C+R Score Evolution Tracking

**Methodology:** Track Core (C) and ROI (R) pillar scores across checkpoints. Quality (Q) pillar uses Q2 2026 aggregate PR data (not checkpoint-specific), so Q scores are constant across checkpoints. Focus on C+R evolution.

### CP7 (Jun 8) vs CP8 (Jun 12) Score Comparison

| User | CP7 C | CP8 C | CP7 R | CP8 R | CP7 Total (C+R+Q) | CP8 Total (C+R+Q) | Trend |
|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | 3 | 3 | 1 | 0 | 7 | 6 | ⬇ R score dropped (premium spike) |
| Kranti-nice | 3 | 3 | 2 | 0 | 8 | 6 | ⬇ R score dropped (premium spike) |
| mshnayderman | 3 | 3 | 0 | 0 | 6 | 6 | → Stable (already at R=0) |
| Prathmesh-Ranadive | 3 | 3 | 0 | 0 | 6 | 6 | → Stable |
| mfield1 | 3 | 3 | 2 | 0 | 8 | 6 | ⬇ R score dropped (premium spike) |
| rpawar-nice | 2 | 2 | 2 | 2 | 7 | 7 | → Stable (maintained R=2) |
| Vitthal-Nice | 1 | 1 | 2 | 1 | 6 | 5 | ⬇ R score dropped slightly |
| luisalvatierra | 2 | 3 | 0 | 0 | 5 | 6 | ⬆ C score improved (LoC growth) |
| jayesh-rai | 1 | 1 | 2 | 0 | 6 | 4 | ⬇ R score dropped (premium spike) |
| chris-haun | 3 | 3 | 0 | 0 | 6 | 6 | → Stable (already at R=0) |

**Key Patterns:**

**1. Widespread R Score Decline (CP7 → CP8)**
- **7 users** dropped from R=1 or R=2 to **R=0** in 4 days
- Cause: Premium spike pattern (5×-100× increases documented in v1 analysis)
- Even **elite efficiency users** affected: mfield1 (R=2 → R=0), jayesh-rai (R=2 → R=0)

**2. Only 1 User Maintained R=2**
- **rpawar-nice** — The only user with R=2 at both CP7 and CP8
- Premium increased (144 → 850), but ReqEff 10.2 still qualifies for R=2 (>10 LoC/request)
- **Model user** for premium efficiency

**3. C Score Mostly Stable**
- Core scores (LoC volume + trend) show **minimal movement** in 4-day window
- Only **luisalvatierra** improved C score (2 → 3) due to LoC doubling (4,800 → 9,477)

---

## Score Volatility Analysis

**Volatility Metric:** Change in C+R score between CP7 and CP8.

| Volatility Level | C+R Score Change | User Count | % of Team |
|---|---|---|---|
| **High Volatility** | ≥2 points | 8 | 19% |
| **Moderate Volatility** | 1 point | 5 | 12% |
| **Stable** | 0 points | 30 | 70% |

### High Volatility Users (C+R Change ≥2)

| User | CP7 C+R | CP8 C+R | Delta | Reason |
|---|---|---|---|---|
| amol-salunkhe | 4 | 3 | **−1** | R=1 → R=0 (premium spike from 5,309 → 11,150) |
| Kranti-nice | 5 | 3 | **−2** | R=2 → R=0 (premium spike from ~1,200 → 11,979) |
| mfield1 | 5 | 3 | **−2** | R=2 → R=0 (premium spike from ~650 → 1,813) |
| jayesh-rai | 3 | 1 | **−2** | R=2 → R=0 (premium spike from ~130 → 852) |
| Vitthal-Nice | 3 | 2 | **−1** | R=2 → R=1 (premium doubled from ~200 → 413) |
| luisalvatierra | 2 | 3 | **+1** | C=2 → C=3 (LoC doubled, but R stayed at 0) |

**Interpretation:**
- **All negative volatility** driven by **R score drops** (premium spikes)
- **Only positive volatility** from **luisalvatierra** (C score improvement from exceptional LoC growth)
- **High volatility is bad** in this period — indicates premium spike impact

---

## Premium Spend Timeline (CP1 → CP8)

**Tracking users who crossed premium thresholds:**

### Threshold Crossings

| Threshold | Definition | Users Who Crossed (CP7 → CP8) |
|---|---|---|
| **Lean Spend** | Premium ≤ 500 | **5 users dropped below** (no longer qualify for lean bonus) |
| **Moderate Spend** | Premium 500-1,700 | **Bandwidth shrinking** (most users now above 1,700) |
| **Outlier Spend** | Premium > 1,700 | **7 NEW users crossed** into outlier territory |

### NEW Outlier Spend Users (CP7 → CP8)

| User | CP7 Premium | CP8 Premium | Growth | Impact on R Score |
|---|---|---|---|---|
| Kranti-nice | ~1,200 | 11,979 | +898% | R=2 → R=0 (−1 penalty applied) |
| trunalgawade | 10,863 | 16,265 | +50% | Already outlier; penalty continues |
| PradnyeshSalunke | 9,892 | 15,719 | +59% | Already outlier; penalty continues |
| Shubhamfulzele28 | ~120 | 13,831 | +11,417% | NEW outlier; R score collapsed |
| tusharpati166719 | ~100 | 10,754 | +10,654% | NEW outlier; R score collapsed |
| amol-salunkhe | 5,309 | 11,150 | +110% | NEW outlier (crossed 1,700); R score dropped |
| sskalaskar | ~85 | 7,434 | +8,640% | NEW outlier; R score collapsed |

**Key Finding:** The Jun 8 → Jun 12 window shows **7 users crossing into outlier spend territory**. Combined with 6 users already in outlier status at CP7, this means **13 users (30% of team)** now have premium > 1,700.

---

## C+R Score Distribution (CP7 vs CP8)

### CP7 Distribution

| C+R Score | User Count | % of Team | Tier Mapping |
|---|---|---|---|
| 6 | 2 | 5% | A (with Q=3) |
| 5 | 6 | 14% | B (with Q=3) |
| 4 | 8 | 19% | C (with Q=3) |
| 3 | 10 | 23% | C (with Q=3) |
| 2 | 12 | 28% | D (with Q=3) or C (if Q=0) |
| 1 | 4 | 9% | D |
| 0 | 1 | 2% | E |

### CP8 Distribution

| C+R Score | User Count | % of Team | Tier Mapping | Change from CP7 |
|---|---|---|---|---|
| 4 | 2 | 5% | B (with Q=3) | ⬇ Down from 6 (no users scored 5-6 at CP8) |
| 3 | 18 | 42% | C (with Q=3) | ⬆ Massive increase (consolidation) |
| 2 | 10 | 23% | D (with Q=3) or C (if Q=0) | Stable |
| 1 | 11 | 26% | D | ⬆ Increase |
| 0 | 2 | 5% | E | Stable |

**C+R Score Compression:** The premium spike pattern caused **score consolidation** at C+R = 3:
- **CP7:** 10 users at C+R = 3 (23%)
- **CP8:** 18 users at C+R = 3 (42%)

**Interpretation:** With R=0 affecting 91% of users, **C score becomes the primary differentiator**. Users with C=3 (LoC > 10K or LoC 5-10K with growth) cluster at C+R=3, while users with C=2 or below spread across lower scores.

---

## Premium Efficiency Trend (Request Efficiency Over Time)

### Efficiency Leaders (CP7 vs CP8)

| Rank | User | CP7 ReqEff | CP8 ReqEff | Change | CP7 Premium | CP8 Premium |
|---|---|---|---|---|---|---|---|
| 1 | rpawar-nice | 60.1 | **10.2** | −83% | 144 | 850 |
| 2 | dannycadima | — | **11.0** | — | — | 3 |
| 3 | Vitthal-Nice | ~14 | **6.3** | −55% | ~200 | 413 |
| 4 | mfield1 | 14.3 | **5.4** | −62% | ~650 | 1,813 |
| 5 | mshnayderman | 5.1 | **5.1** | 0% | 5,419 | 5,419 |

**Observation:** Even **efficiency leaders show dramatic ReqEff declines** (except mshnayderman, who was already at R=0 and stays flat). rpawar-nice dropped from 60.1 → 10.2 (−83%) but **still maintains best-in-team efficiency**.

### Efficiency Laggards (ReqEff < 1.0)

| User | CP7 ReqEff | CP8 ReqEff | CP7 Premium | CP8 Premium | Status |
|---|---|---|---|---|---|
| nilesht-19 | 0.3 | 0.2 | 23,108 | 30,437 | Budget crisis worsening |
| trunalgawade | 0.1 | 0.1 | 10,863 | 16,265 | Budget crisis worsening |
| PradnyeshSalunke | 0.3 | 0.2 | 9,892 | 15,719 | Budget crisis worsening |
| Shubhamfulzele28 | ~6.2 | 0.1 | ~120 | 13,831 | NEW budget crisis |
| thakraln | 0.1 | 0.1 | 11,112 | 11,451 | Budget crisis stable |

**5 users** with ReqEff < 1.0 (producing less than 1 LoC per premium request). This is **unsustainable** at scale.

---

## Quality Score Trends (Q Pillar)

**Note:** Q scores are based on Q2 2026 aggregate PR data, **not checkpoint-specific**. All users maintain same Q score across CP7 and CP8.

### Q Score Distribution (Constant Across CP7-CP8)

| Q Score | User Count | % of Team | Criteria |
|---|---|---|---|
| **Q = 3** | 27 | 63% | LoC > 1,000; team merge rate 89.7%, reviews 2.2/PR |
| **Q = 0** | 16 | 37% | LoC < 1,000 (insufficient PR contribution) |

**Recommendation for Future Analyses:** Collect **checkpoint-specific PR data** to enable Q score evolution tracking. Current aggregate Q2 data cannot show:
- PR quality improvements/declines over time
- Correlation between LoC spikes and PR activity
- Whether Copilot-generated code is being merged or discarded

---

## CRQC Override Rule Impact Timeline

### "R=0 AND Premium >500 → Cap at Tier C" Rule

| Checkpoint | Users Affected | % of Team | Impact |
|---|---|---|---|
| CP7 | ~25 | ~58% | Moderate cap impact |
| **CP8** | **37** | **86%** | **Severe cap impact** |

**CP7 → CP8 Change:** 12 additional users fell under the R=0 override rule due to premium spikes. This includes:
- **7 users** who crossed into outlier spend (>1,700 premium)
- **5 users** who had moderate spend (500-1,700) but collapsed ReqEff below 5

**Result:** At CP8, only **6 users (14%)** are NOT capped by the R=0 override. The CRQC framework becomes **highly punitive** when a platform-level premium anomaly affects the entire team.

---

## Recommendations

### 1. Investigate R Score Collapse Root Cause
- **CP7:** 9% of users at R=0
- **CP8:** 91% of users at R=0
- This is **not normal behavior** — investigate platform-level premium calculation changes with GitHub Copilot support

### 2. Temporarily Suspend R=0 Override Rule
Until premium spike root cause is identified and resolved:
- **Option A:** Remove the "R=0 AND Premium >500 → Cap at Tier C" override for the CP8 period only
- **Option B:** Apply override only to users with **persistent** R=0 across 3+ checkpoints (not one-time spikes)

### 3. Track "Premium Efficiency Volatility" as Separate Metric
High ReqEff volatility (e.g., Kranti-nice: 7.6 → 23.1 → 2.6) indicates:
- **Either:** Platform instability (more likely in this case)
- **Or:** User behavior instability (less likely when affecting 37 users)

### 4. Add Premium Trend Alerts
Flag users who show:
- **5× premium spike** in a single window → Immediate investigation
- **>1,700 premium** crossed → Budget review
- **R score drop from 2 → 0** in one window → Efficiency intervention

---

*C+R Score Evolution — CP7 → CP8 window shows systematic R score collapse (91% of users at R=0). C scores stable. Q scores constant (Q2 aggregate data). Premium spike pattern dominates all score trends. 15 users excluded per ignore list.*
