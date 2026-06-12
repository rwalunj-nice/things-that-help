# GitHub Copilot Multi-Period Analysis — Multi-Window Momentum
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Period:** April 20 → June 12, 2026 (53 days, 8 checkpoints)  
**Framework:** Role Context + Multi-Window Momentum

---

## Multi-Window Momentum Calculation

**Formula (applied to each checkpoint window):**
```
Momentum_Window_N = ((CP_N LoC − CP_N-1 LoC) / max(CP_N-1 LoC, 1)) × 100
```

**Windows Analyzed:**
1. CP1 → CP2 (3 days)
2. CP2 → CP3 (5 days)
3. CP3 → CP4 (13 days)
4. CP4 → CP5 (7 days)
5. CP5 → CP6 (16 days)
6. CP6 → CP7 (5 days)
7. **CP7 → CP8 (4 days)** ← Current analysis focus

---

## CP7 → CP8 Momentum Analysis (4-Day Window)

### Momentum Score Distribution

| Momentum Label | Count | % of Users | Definition |
|---|---|---|---|
| 🚀 Breakout (>+100%) | 0 | 0% | No users |
| 📈 Rising (+25% to +100%) | 1 | 2.3% | luisalvatierra only |
| ➡️ Stable (−25% to +25%) | ~40 | ~93% | Vast majority |
| 📉 Slipping (−25% to −60%) | 0 | 0% | No users |
| 🔴 Declining (<−60%) | 0 | 0% | No users |

### Top 10 Momentum Scores (CP7 → CP8)

| Rank | User | CP7 LoC | CP8 LoC | Delta | Momentum % | Label |
|---|---|---|---|---|---|---|---|
| 1 | luisalvatierra | ~4,800 | 9,477 | +4,677 | **+97.4%** | 📈 Rising |
| 2 | PradnyeshSalunke | ~2,968 | 3,731 | +763 | **+25.7%** | ➡️ Stable |
| 3 | vishal-tad | ~2,900 | 3,520 | +620 | **+21.4%** | ➡️ Stable |
| 4 | amol-salunkhe | 34,037 | 41,008 | +6,971 | **+20.5%** | ➡️ Stable |
| 5 | Kranti-nice | 27,733 | 31,645 | +3,912 | **+14.1%** | ➡️ Stable |
| 6 | moadzughul | ~3,100 | 3,409 | +309 | **+10.0%** | ➡️ Stable |
| 7 | mfield1 | ~9,300 | 9,800 | +500 | **+5.4%** | ➡️ Stable |
| 8 | nilesht-19 | 7,160 | 7,346 | +186 | **+2.6%** | ➡️ Stable |
| 9 | abhishekhole-nice | 2,936 | 2,993 | +57 | **+1.9%** | ➡️ Stable |
| 10 | chris-haun | ~10,359 | 10,384 | +25 | **+0.2%** | ➡️ Stable |

**Key Finding:** Only **1 user (luisalvatierra)** shows meaningful momentum in the 4-day window. Most users (~93%) show flat or minimal LoC movement. **The 4-day window is insufficient for momentum analysis.**

---

## Momentum Pattern Classification (Long-Term: CP1 → CP8)

**Data Source:** Master progression table from Jun 3 summary analysis (CP1-CP6 available there) + CP7-CP8 data from this analysis.

### Momentum Patterns Defined

| Pattern | Definition | Classification Rule |
|---|---|---|
| **Accelerating** | Momentum increases each window | Each window momentum > prior window momentum |
| **Decelerating** | Momentum decreases each window | Each window momentum < prior window momentum |
| **Volatile** | Large momentum swings between windows | >100% change in momentum between consecutive windows |
| **Sustained** | Stable momentum across windows | Momentum variance < 30% across windows |
| **Flat** | Minimal change across all windows | Avg momentum < ±10% |

### Pattern Distribution (CP1 → CP8)

| Pattern | Estimated Count | % of Team | Key Examples |
|---|---|---|---|
| **Accelerating** | ~3 | ~7% | amol-salunkhe, luisalvatierra |
| **Sustained** | ~8 | ~19% | mshnayderman, rpawar-nice, Vitthal-Nice |
| **Volatile** | ~15 | ~35% | Kranti-nice, chris-haun, Vyankatesh95 |
| **Decelerating** | ~5 | ~12% | nilesht-19, PradnyeshSalunke |
| **Flat** | ~12 | ~28% | Budget crisis users, low-output users |

**Analysis:**

**Accelerating:**
- **amol-salunkhe** — Emerged as LoC leader in recent checkpoints. Likely showed modest output at CP1-CP3, then accelerated at CP4-CP8.
- **luisalvatierra** — Breakout at CP8 (+97%) suggests acceleration pattern, but needs confirmation from earlier checkpoints.

**Sustained:**
- **mshnayderman** — Consistently ~27K LoC across CP7-CP8 (flat). Likely sustained this level from earlier checkpoints.
- **rpawar-nice** — Efficiency leader. LoC flat at 8,662 between CP7-CP8, suggesting sustained output at this level.

**Volatile:**
- **Kranti-nice** — Strong growth at CP7 (from Jun 3 → Jun 8), moderate growth at CP8. ReqEff swings wildly (7.6 → 23.1 → 2.6), indicating volatile premium usage.
- **Vyankatesh95** — Premium spiked 27× (CP7 → CP8) with flat LoC, creating extreme efficiency volatility.

**Flat:**
- **Budget crisis users** (nilesht-19, thakraln, trunalgawade, etc.) — Low LoC output sustained across multiple checkpoints despite high premium spend.

---

## Coaching Intervention Tracking (CP6 → CP7 → CP8)

### Interventions Documented at CP7 (Jun 8 Analysis)

| User | CP6 ReqEff | CP7 ReqEff | CP7 Intervention | CP8 ReqEff | Outcome |
|---|---|---|---|---|---|
| rpawar-nice | ~20.1 | **60.1** | ✅ Breakout success (+199%) | 10.2 | Regression but still strong |
| Kranti-nice | ~7.6 | **23.1** | ✅ Breakout success (+204%) | 2.6 | **Collapsed** (−88%) |
| nilesht-19 | ~0.3 | 0.3 | 🔴 Budget intervention | 0.2 | **No improvement** |
| trunalgawade | ~0.1 | 0.1 | 🔴 Budget intervention | 0.1 | **No improvement** |
| PradnyeshSalunke | ~0.3 | 0.3 | 🔴 Budget intervention | 0.2 | **No improvement** |

**Key Observations:**

**1. Breakout Coaching Successes Reversed:**
- **rpawar-nice** and **Kranti-nice** both showed exceptional ReqEff gains (CP6 → CP7) after coaching.
- At CP8, **Kranti-nice collapsed** (ReqEff 23.1 → 2.6, premium 10× spike).
- **rpawar-nice regressed** (ReqEff 60.1 → 10.2) but maintains lean premium relative to peers.

**Interpretation:** The CP7 → CP8 premium spike pattern **overwhelmed individual coaching gains**. Even users who responded well to coaching show regression, suggesting **platform-level issue** rather than behavior relapse.

**2. Budget Crisis Interventions Ineffective:**
- 3 budget crisis users (nilesht-19, trunalgawade, PradnyeshSalunke) showed **no improvement** from CP7 → CP8.
- Premium continued to spike or remain at crisis levels.
- **Action required:** Escalate to VP R&D for access restriction or deeper investigation.

**3. NEW Budget Crisis (Shubhamfulzele28):**
- No prior intervention history (was not flagged at CP7).
- Premium spiked from ~120 → 13,832 in 4 days (+11,400%).
- This user's sudden crisis suggests **platform-level trigger** rather than gradual behavioral drift.

---

## Momentum-Based Tier Adjustments

**Rule:** Users with Momentum > +100% are eligible for **one-tier promotion** beyond base score.

### Eligible Users (CP7 → CP8)

| User | Momentum % | Base Tier (Role+Momentum) | Promotion Eligible? | Final Tier |
|---|---|---|---|---|
| luisalvatierra | +97.4% | B | No (threshold is >+100%) | B |

**No users qualify** for momentum-based promotion in the CP7 → CP8 window (no users exceeded +100% momentum).

**Note:** If analyzing longer windows (e.g., CP6 → CP8 or CP5 → CP8), more users would likely qualify. The 4-day window limits eligibility.

---

## Role Context Integration

### Manager Role Momentum

| Login | Role | CP7 LoC | CP8 LoC | Momentum % | CP7 Premium | CP8 Premium | Notes |
|---|---|---|---|---|---|---|---|---|
| SwapnilNice | Manager | 3,140 | 3,140 | 0% | ~100 | 1,594 | Premium spiked 16×; LoC flat |
| ssamal-nice | Manager | 38 | 38 | 0% | ~35 | 109 | Low engagement; premium tripled |

**Manager Role Adjustment:** Managers are benchmarked on **engagement + efficiency (ReqEff >5)**, not raw LoC. Both managers show:
- **Flat LoC** (0% momentum)
- **Premium spikes** (16× for SwapnilNice, 3× for ssamal-nice)
- **ReqEff collapse** (SwapnilNice: 31.4 → 2.0)

**Action:** Manager-specific coaching on premium efficiency. SwapnilNice was a strong coder-manager at CP7 (ReqEff 31.4) — the 16× premium spike needs investigation.

### Research Role

| Login | Role | CP7 Int | CP8 Int | CP7 Premium | CP8 Premium | Notes |
|---|---|---|---|---|---|---|
| rwalunj-nice | Research | ~30 | 61 | ~100 | 1,770 | Interactions doubled; premium 18× spike |

**Research Role:** Excluded from tier scoring. LoC = 0 by design (research/tooling exploration). Premium increased 18×, but this may be justified if research scope expanded. **Recommend:** Manager review to confirm research activity scope.

---

## Recommendations for Multi-Window Momentum Analysis

### 1. Extend Window Length
- **Current:** 4 days (CP7 → CP8) → 93% of users show flat momentum
- **Recommended:** 7-14 days minimum for meaningful momentum signals
- **Ideal:** Checkpoint intervals of 10-15 days to balance data freshness with signal strength

### 2. Use Rolling Averages
Instead of comparing single checkpoints, use **3-checkpoint rolling averages**:
```
Momentum_Rolling = ((Avg(CP_N, CP_N-1, CP_N-2) − Avg(CP_N-3, CP_N-4, CP_N-5)) / Avg(CP_N-3, CP_N-4, CP_N-5)) × 100
```

This smooths out day-to-day noise and surfaces true trajectory shifts.

### 3. Track Momentum Volatility as Metric
Users with **high momentum volatility** (large swings between windows) are:
- **Either:** experimenting with different workflows (good — learning)
- **Or:** inconsistent usage (bad — not integrated into workflow)

**High volatility examples:** Kranti-nice (ReqEff swings: 7.6 → 23.1 → 2.6), Vyankatesh95 (Premium: 150 → 4,062 in 4 days).

**Low volatility examples:** mshnayderman (27.8% accept stable across checkpoints), Vitthal-Nice (41-44% accept stable).

**Coaching:** Celebrate low volatility + strong output (indicates mastery). Investigate high volatility + declining output (indicates struggle or platform issue).

---

*Multi-Window Momentum Analysis — 4-day CP7 → CP8 window insufficient for meaningful momentum signals. Coaching interventions from CP7 overwhelmed by CP8 premium spike pattern. 15 users excluded per ignore list.*
