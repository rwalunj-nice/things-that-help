# GitHub Copilot Usage — WFM Integrations
## v2 Workflow-Aware Multi-Period Progression Analysis
**Product:** WFM Integrations
**VP:** (WFM Integrations VP)
**Analysis Date:** June 23, 2026
**Period Covered:** April 20, 2026 → June 23, 2026 (64 days)
**Checkpoints:** 9 (CP1–CP9)
**Methodology Note:** Agent Contribution % is not available in the current data export. This report uses a **2-tier proxy classification** (Agent-First vs Inline-First) based on CP9 Suggestion Efficiency (SuggEff) and % Accept patterns. Users with SuggEff > ~8–12 and %Accept < 20% are classified Agent-First; users with %Accept ≥ 20% or clear inline patterns are classified Inline-First. A third bucket — **Agent-First lean** — captures users whose signals lean Agent-First but fall below high-confidence thresholds. This classification informs workflow-sensitive interpretation of LoC velocity, plateau analysis, and budget pressure.

---

## Table of Contents
1. [Workflow Classification Summary](#1-workflow-classification-summary)
2. [Checkpoint Timeline](#2-checkpoint-timeline)
3. [Master LoC Progression Table](#3-master-loc-progression-table)
4. [Agent-First vs Inline-First Performance Comparison](#4-agent-first-vs-inline-first-performance-comparison)
5. [Pattern-Grouped Sections](#5-pattern-grouped-sections)
   - 5.1 Late Accelerators
   - 5.2 Steady Climbers
   - 5.3 Front-Loaders
   - 5.4 Mid-Period Stalls
   - 5.5 Volatile
   - 5.6 Flat Liners
6. [Per-User Cards — Top 20 Producers](#6-per-user-cards--top-20-producers)
7. [What Changed vs v1 Progression](#7-what-changed-vs-v1-progression)
8. [Budget Crisis by Workflow Type](#8-budget-crisis-by-workflow-type)
9. [Q2 Closing Assessment by Workflow Type](#9-q2-closing-assessment-by-workflow-type)

---

## 1. Workflow Classification Summary

### Classification Criteria (2-Tier Proxy)

| Tier | Label | Criteria | Interpretation |
|---|---|---|---|
| 1 | **Agent-First** | SuggEff > ~10 AND %Accept < 20% | User primarily runs Copilot agents/chat; accepts small portions of large generated blocks |
| 1 | **Inline-First** | %Accept ≥ 20% OR clear inline pattern | User primarily uses inline suggestions; accepts a higher share of presented code |
| 2 | **Agent-First lean** | SuggEff > ~4, %Accept < 20%, below high-confidence threshold | Likely Agent-First but signals are weaker; treat cautiously |
| — | **Inline-First lean** | Low LoC + low engagement; pattern unclear | Defaulted to Inline-First due to insufficient signal |

### CP9 Workflow Classification Table

| User | SuggEff (CP9) | %Accept (CP9) | Workflow Class | Confidence |
|---|---|---|---|---|
| amol-salunkhe | 31.95 | 1.5% | Agent-First | High |
| Kranti-nice | 47.53 | 4.6% | Agent-First | High |
| rpawar-nice | 60.15 | 7.6% | Agent-First | High |
| Shreedevi-nice | 55.47 | 8.8% | Agent-First | High |
| abhishekhole-nice | 33.16 | 3.2% | Agent-First | High |
| copilotshree | 11.02 | 4.8% | Agent-First | High |
| mfield1 | 12.12 | 5.8% | Agent-First | High |
| giteshsawant | 15.38 | 2.2% | Agent-First | High |
| moadzughul | 9.19 | 2.4% | Agent-First | High |
| suhas-kakde | 8.39 | 1.7% | Agent-First | High |
| jayesh-rai | 13.49 | 18.4% | Agent-First | High |
| pdevle | 13.20 | 6.3% | Agent-First | High |
| Prathmesh-Ranadive | — | 88.7% | Inline-First | High |
| mshnayderman | — | 27.8% | Inline-First | High |
| nilesht-19 | — | 30.2% | Inline-First | High |
| Vyankatesh95 | 30.27 | 34.1% | Inline-First | High (overrides SuggEff signal) |
| Vitthal-Nice | — | 40.4% | Inline-First | High |
| trunalgawade | — | 20.4% | Inline-First | High |
| Akale23 | — | 22.8% | Inline-First | High |
| jkumbhar | — | 22.0% | Inline-First | High |
| luisalvatierra | — | 24.2% | Inline-First | High |
| abhijeetk268 | — | 29.6% | Inline-First | High |
| dsuraj25 | — | 33.3% | Inline-First | High |
| amol-doke | — | 22.2% | Inline-First | High |
| smishra-nice | — | 78.3% | Inline-First | High |
| Shubhamfulzele28 | — | unknown | Inline-First lean | Low (low LoC, default) |
| tusharpatil166719 | 11.58 | 14.7% | Agent-First lean | Medium |
| chris-haun | 7.72 | 9.3% | Agent-First lean | Medium |
| PradnyeshSalunke | 8.39 | 19.4% | Agent-First lean | Medium |
| mshivarkar | 7.34 | 9.4% | Agent-First lean | Medium |
| vishal-tad | 4.19 | 8.8% | Agent-First lean | Medium |
| sskalaskar | 23.77 | 16.9% | Agent-First lean | Medium |
| prashasti-jain | 6.27 | 7.2% | Agent-First lean | Medium |
| meghabiradar05 | 8.30 | 12.5% | Agent-First lean | Medium |

### Workflow Distribution Summary

| Workflow Class | User Count | % of Team |
|---|---|---|
| Agent-First | 12 | 35% |
| Inline-First | 14 | 41% |
| Agent-First lean | 8 | 24% |
| **Total** | **34** | **100%** |

**Key structural insight:** The team is nearly evenly split between Agent-First and Inline-First workflows. Neither workflow dominates headcount. The differentiation lies in how LoC velocity, accept patterns, and budget pressure diverge between the two groups — which the sections below quantify.

---

## 2. Checkpoint Timeline

| CP | Date | Days Since Prior CP | Days Since Start | Label |
|---|---|---|---|---|
| CP1 | Apr 20, 2026 | — | 0 | Baseline |
| CP2 | Apr 23, 2026 | +3 | 3 | Early snapshot |
| CP3 | Apr 28, 2026 | +5 | 8 | Week 1 close |
| CP4 | May 11, 2026 | +13 | 21 | Mid-April gap |
| CP5 | May 18, 2026 | +7 | 28 | Month 1 close |
| CP6 | Jun 3, 2026 | +16 | 44 | Q2 acceleration |
| CP7 | Jun 8, 2026 | +5 | 49 | June sprint open |
| CP8 | Jun 12, 2026 | +4 | 53 | Mid-June |
| CP9 | Jun 23, 2026 | +11 | 64 | Final / Q2 close |

**Notable gaps:** CP4 (13-day window, Apr 28–May 11) and CP6 (16-day window, May 18–Jun 3) are the two longest windows. Large LoC jumps in these windows are amplified by window length and should not be read as single-day bursts.

---

## 3. Master LoC Progression Table

Sorted by CP9 LoC descending. "Workflow" column reflects CP9 classification.

| # | User | CP1 Apr20 | CP2 Apr23 | CP3 Apr28 | CP4 May11 | CP5 May18 | CP6 Jun3 | CP7 Jun8 | CP8 Jun12 | CP9 Jun23 | Workflow |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | amol-salunkhe | 31 | 31 | 2,210 | 17,155 | 28,911 | 30,486 | 34,037 | 41,008 | **43,585** | Agent-First |
| 2 | Kranti-nice | 2,148 | 2,148 | 3,259 | 3,259 | 7,076 | 27,733 | 27,733 | 31,645 | **37,978** | Agent-First |
| 3 | Prathmesh-Ranadive | 1,373 | 1,373 | 1,848 | 8,783 | 9,489 | 20,436 | 27,052 | 27,052 | **35,091** | Inline-First |
| 4 | mshnayderman | 20,399 | 20,399 | 20,951 | 22,268 | 22,268 | 24,387 | 27,539 | 27,539 | **27,539** | Inline-First |
| 5 | luisalvatierra | 1,216 | 1,216 | 1,444 | 1,698 | 2,292 | 4,564 | 4,800 | 9,477 | **12,080** | Inline-First |
| 6 | chris-haun | 6,034 | 6,376 | 6,670 | 6,758 | 8,592 | 10,264 | 10,359 | 10,384 | **10,493** | Agent-First lean |
| 7 | mfield1 | 4,414 | 4,414 | 5,637 | 8,566 | 9,071 | 9,251 | 9,300 | 9,800 | **9,803** | Agent-First |
| 8 | rpawar-nice | 8,566 | 8,640 | 8,640 | 8,640 | 8,658 | 8,662 | 8,662 | 8,662 | **8,662** | Agent-First |
| 9 | nilesht-19 | 1,287 | 1,567 | 3,598 | 4,908 | 5,065 | 5,293 | 7,160 | 7,346 | **7,354** | Inline-First |
| 10 | copilotshree | 4,543 | 4,543 | 4,553 | 4,706 | 5,013 | 5,013 | 5,013 | 5,013 | **5,013** | Agent-First |
| 11 | PradnyeshSalunke | 857 | 857 | 857 | 1,735 | 1,948 | 2,296 | 2,968 | 3,731 | **4,237** | Agent-First lean |
| 12 | mshivarkar | 0 | 1 | 28 | 28 | 28 | 1,559 | 2,018 | 2,097 | **4,201** | Agent-First lean |
| 13 | Vyankatesh95 | 1,968 | 1,968 | 2,350 | 2,795 | 3,673 | 4,151 | 4,177 | 4,177 | **4,177** | Inline-First |
| 14 | vishal-tad | 739 | 952 | 1,156 | 1,156 | 1,156 | 2,815 | 2,900 | 3,520 | **3,737** | Agent-First lean |
| 15 | moadzughul | 2,572 | 2,572 | 2,620 | 2,655 | 2,749 | 3,035 | 3,100 | 3,409 | **3,409** | Agent-First |
| 16 | sskalaskar | 302 | 517 | 517 | 2,056 | 2,056 | 2,609 | 2,700 | 2,698 | **3,233** | Agent-First lean |
| 17 | abhishekhole-nice | 267 | 267 | 319 | 2,722 | 2,803 | 2,803 | 2,936 | 2,993 | **3,150** | Agent-First |
| 18 | trunalgawade | 6 | 6 | 61 | 261 | 302 | 304 | 1,086 | 2,038 | **2,352** | Inline-First |
| 19 | Vitthal-Nice | 1,180 | 1,180 | 1,180 | 2,472 | 2,566 | 2,609 | 2,609 | 2,609 | **2,683** | Inline-First |
| 20 | jayesh-rai | 1 | 1 | 1 | 777 | 862 | 2,196 | 2,479 | 2,479 | **2,712** | Agent-First |
| 21 | tusharpatil166719 | 381 | 381 | 853 | 1,389 | 1,631 | 1,798 | 1,798 | 1,798 | **2,200** | Agent-First lean |
| 22 | Akale23 | 292 | 292 | 779 | 1,133 | 1,856 | 2,409 | 2,472 | 2,472 | **2,472** | Inline-First |
| 23 | suhas-kakde | 1,367 | 1,367 | 1,597 | 1,615 | 1,639 | 1,639 | 1,639 | 1,677 | **2,005** | Agent-First |
| 24 | Shreedevi-nice | 38 | 56 | 88 | 88 | 690 | 1,013 | 1,416 | 1,786 | **1,886** | Agent-First |
| 25 | jkumbhar | 1,316 | 1,316 | 1,412 | 1,412 | 1,788 | 1,868 | 1,870 | 1,870 | **1,880** | Inline-First |
| 26 | meghabiradar05 | 0 | 0 | 1,389 | 1,389 | 1,389 | 1,684 | 1,700 | 1,720 | **1,727** | Agent-First lean |
| 27 | prashasti-jain | 0 | 0 | 0 | 203 | 837 | 872 | 900 | 1,545 | **1,562** | Agent-First lean |
| 28 | pdevle | 361 | 361 | 368 | 370 | 370 | 1,049 | 1,100 | 1,384 | **1,478** | Agent-First |
| 29 | Shubhamfulzele28 | 0 | 0 | 0 | 0 | 0 | 0 | 739 | 739 | **1,043** | Inline-First lean |
| 30 | dsuraj25 | 491 | 491 | 491 | 491 | 491 | 504 | 510 | 510 | **1,169** | Inline-First |
| 31 | giteshsawant | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 1,110 | **1,369** | Agent-First |
| 32 | thakraln | 0 | 0 | 0 | 0 | 0 | 69 | 69 | 750 | **806** | Agent-First lean |
| 33 | abhijeetk268 | 172 | 172 | 172 | 172 | 173 | 656 | 656 | 656 | **656** | Inline-First |
| 34 | pratikpawar12 | 0 | 0 | 0 | 166 | 250 | 250 | 250 | 250 | **250** | Agent-First lean |

**Team Total LoC by Checkpoint:**

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 64,290 | 65,435 | 77,810 | 116,394 | 133,643 | 183,181 | 208,846 | 229,207 | 247,625 |

**Net new LoC per window:**

| Window | Period | Days | Net New LoC | LoC/day |
|---|---|---|---|---|
| CP1→CP2 | Apr 20–23 | 3 | 1,145 | 382 |
| CP2→CP3 | Apr 23–28 | 5 | 12,375 | 2,475 |
| CP3→CP4 | Apr 28–May 11 | 13 | 38,584 | 2,968 |
| CP4→CP5 | May 11–18 | 7 | 17,249 | 2,464 |
| CP5→CP6 | May 18–Jun 3 | 16 | 49,538 | 3,096 |
| CP6→CP7 | Jun 3–8 | 5 | 25,665 | 5,133 |
| CP7→CP8 | Jun 8–12 | 4 | 20,361 | 5,090 |
| CP8→CP9 | Jun 12–23 | 11 | 18,418 | 1,674 |

**Observation:** The CP6→CP7 and CP7→CP8 windows (early–mid June) represent the highest LoC/day rates of the entire period. The final CP8→CP9 window shows a marked deceleration (1,674 LoC/day vs 5,000+ in the prior two windows), suggesting the Q2 acceleration phase is winding down heading into June 23.

---

## 4. Agent-First vs Inline-First Performance Comparison

### 4.1 Total and Average LoC by Workflow Class (CP9)

| Workflow Class | Users | Total LoC (CP9) | Avg LoC/User | Median LoC | Top Producer |
|---|---|---|---|---|---|
| Agent-First | 12 | 151,435 | 12,620 | 5,838 | amol-salunkhe (43,585) |
| Inline-First | 14 | 126,977 | 9,070 | 3,231 | Prathmesh-Ranadive (35,091) |
| Agent-First lean | 8 | 31,609 | 3,951 | 3,485 | chris-haun (10,493) |
| **All** | **34** | **~310,021** | **~9,118** | — | amol-salunkhe |

> Note: "All" total includes Inline-First lean (Shubhamfulzele28, 1,043 LoC). Agent-First + Agent-First lean combined = 183,044 LoC across 20 users (avg 9,152). Inline-First + Inline-First lean combined = 127,020 LoC across 14 users (avg 9,073). The two broad groups are nearly even in average LoC per user — a critical finding: **neither workflow dominates on productivity**.

### 4.2 LoC Velocity Comparison (CP1 → CP9)

| Workflow Class | Avg LoC at CP1 | Avg LoC at CP9 | Avg Growth | Avg LoC/Day (64d) |
|---|---|---|---|---|
| Agent-First | 2,193 | 12,620 | +10,427 | +163/day |
| Inline-First | 2,374 | 9,070 | +6,696 | +105/day |
| Agent-First lean | 1,024 | 3,951 | +2,927 | +46/day |

**Agent-First users grew faster in absolute LoC/day** — but this is partly explained by three extreme outliers (amol-salunkhe, Kranti-nice, Prathmesh-Ranadive). Strip those three out and the gap narrows considerably.

### 4.3 Workflow-Specific Patterns

**Agent-First:**
- High SuggEff (often 10–60+) means users are requesting large code generations and accepting only a fraction — but that fraction represents substantial lines
- Low %Accept is expected and should NOT be interpreted as poor adoption; it reflects workflow mechanics
- Top performers (amol-salunkhe, Kranti-nice) show exponential LoC curves consistent with autonomous agent runs
- Risk: budget overspend is concentrated here — high SuggEff means many tokens consumed per accepted line
- Pattern: often front-loads in specific windows (CP3, CP5, CP6) then plateaus between agent sessions

**Inline-First:**
- High %Accept (20–88%) means most suggested lines are being accepted — users are working in a tighter review loop with Copilot
- LoC curves tend to be steadier and more consistent across windows
- Top performers (Prathmesh-Ranadive, mshnayderman) show strong absolute LoC but without the explosive burst patterns of Agent-First users
- Risk: plateaus are harder to diagnose because they look like "normal steady work"; may actually be stalls
- mshnayderman at 27,539 with zero new LoC since CP7 (15+ days) is the clearest Inline-First plateau concern

**Agent-First lean:**
- Weaker SuggEff signals suggest occasional agent use rather than primary workflow
- Lower absolute LoC reflects less intensive usage overall
- chris-haun is the outlier exception here (10,493 LoC) — likely more active than the classification suggests

### 4.4 Q2 Acceleration by Workflow Type (CP5 → CP9)

| Workflow Class | Avg LoC at CP5 | Avg LoC at CP9 | Q2 Avg Growth | % Growth Q2 |
|---|---|---|---|---|
| Agent-First | 7,968 | 12,620 | +4,652 | +58% |
| Inline-First | 4,279 | 9,070 | +4,791 | +112% |
| Agent-First lean | 2,009 | 3,951 | +1,942 | +97% |

**Inline-First users showed stronger percentage Q2 growth** (+112% vs +58% for Agent-First). This is partly because several Agent-First users had already front-loaded large LoC by CP5, leaving less room for proportional gain. Inline-First users like Prathmesh-Ranadive, trunalgawade, and dsuraj25 showed the steepest Q2 acceleration curves.

---

## 5. Pattern-Grouped Sections

### 5.1 Late Accelerators
*Users who added the majority of their LoC in the second half of the period (post-CP5, May 18+).*

#### Agent-First Late Accelerators

**Kranti-nice** (Agent-First)
- CP5: 7,076 → CP6: 27,733 → CP9: 37,978
- Added 30,902 LoC in 39 days (post-CP5), including a massive 20,657-LoC burst in CP5→CP6 (16-day window)
- SuggEff of 47.53 and %Accept of 4.6% confirm autonomous agent runs generating large code blocks
- This late acceleration came with a documented budget crisis — the agent sessions that generated 37,978 total LoC were premium-intensive
- LoC/day in Q2 window: 1,291 (May 18–Jun 3 burst)

**Shreedevi-nice** (Agent-First)
- CP5: 690 → CP9: 1,886
- Late bloomer: essentially inactive through CP4, then 702 LoC in the CP5→CP6 window, followed by steady climbs
- SuggEff 55.47, %Accept 8.8% — strong Agent-First signal; late adoption of agent workflow explains the acceleration timing
- Still relatively low absolute LoC but trajectory is strongly positive

**jayesh-rai** (Agent-First)
- CP4: 777 → CP6: 2,196 → CP9: 2,712
- Near-zero through CP3 (1 LoC), then activated in CP4; major acceleration CP5→CP6 (+1,334 LoC in 16 days)
- %Accept 18.4% is the highest among Agent-First users — borderline Agent-First, possibly evolving toward hybrid

**pdevle** (Agent-First)
- CP5: 370 → CP6: 1,049 → CP8: 1,384 → CP9: 1,478
- Dormant through CP5, then consistent acceleration across CP6–CP9 windows
- SuggEff 13.20 and %Accept 6.3% confirm Agent-First workflow activation

**giteshsawant** (Agent-First)
- Zero LoC through CP6; then 50 at CP7, 1,110 at CP8, 1,369 at CP9
- Most extreme late activator on the team — 1,369 LoC all added in the last two windows (11 days post-CP7)
- SuggEff 15.38, %Accept 2.2% — high-confidence Agent-First; explosive late start

#### Inline-First Late Accelerators

**Prathmesh-Ranadive** (Inline-First)
- CP5: 9,489 → CP6: 20,436 → CP7: 27,052 → CP9: 35,091
- Inline-First's strongest performer and the most dramatic late accelerator in this group
- %Accept 88.7% is extraordinary — nearly 9 in 10 suggestions accepted, implying very high-quality inline suggestions aligned with developer intent
- Added 25,602 LoC in 39 days post-CP5, nearly tripling from CP5 to CP9
- The CP6→CP7 window alone (+6,616 LoC in 5 days = 1,323 LoC/day) rivals Agent-First burst rates while maintaining inline workflow

**trunalgawade** (Inline-First)
- CP6: 304 → CP7: 1,086 → CP8: 2,038 → CP9: 2,352
- Near-dormant through CP6 (304 total LoC in 44 days), then explosive: +782 in CP6→CP7, +952 in CP7→CP8, +314 in CP8→CP9
- %Accept 20.4% — at the floor of Inline-First threshold; the velocity increase suggests workflow intensification
- Most consistent CP7–CP9 growth curve of any late activator (no plateau visible)

**luisalvatierra** (Inline-First)
- CP7: 4,800 → CP8: 9,477 → CP9: 12,080
- Strong CP7→CP8 burst (+4,677 in 4 days = 1,169 LoC/day) followed by continued growth
- %Accept 24.2% — solid inline pattern; high LoC/Accept ratio suggests accepting substantive code blocks

**dsuraj25** (Inline-First)
- Near-flat through CP7 (510 LoC); then jump to 1,169 at CP9 (+659 in the CP8→CP9 window)
- %Accept 33.3% — high confidence Inline-First; late activation with strong acceptance efficiency

#### Agent-First Lean Late Accelerators

**mshivarkar** (Agent-First lean)
- Zero meaningful LoC through CP5 (28 total), then CP6: 1,559, CP7: 2,018, CP8: 2,097, CP9: 4,201
- Most dramatic Agent-First lean late accelerator — 4,173 of 4,201 total LoC added post-CP5
- SuggEff 7.34, %Accept 9.4% — just below Agent-First threshold, but the velocity jump confirms agentic activation

**prashasti-jain** (Agent-First lean)
- Zero through CP3, then: CP4: 203, CP5: 837 (+634 in 7 days), CP8: 1,545, CP9: 1,562
- Inconsistent windows but clear second-half acceleration

---

### 5.2 Steady Climbers
*Users who added LoC consistently across most windows without large gaps or stalls.*

**nilesht-19** (Inline-First)
- Consistent growth CP1→CP9: 1,287 → 1,567 → 3,598 → 4,908 → 5,065 → 5,293 → 7,160 → 7,346 → 7,354
- Growth slowed materially after CP7 (only +194 across CP7–CP9); near-plateau risk
- %Accept 30.2% — solid inline pattern throughout; consistency aligns with inline workflow mechanics

**abhishekhole-nice** (Agent-First)
- CP1: 267 → CP4: 2,722 (+2,455 in the CP3→CP4 window) → CP9: 3,150
- Strong early acceleration then settling into slow steady climb post-CP5
- SuggEff 33.16, %Accept 3.2% — Agent-First; the CP3→CP4 burst was likely a focused agent session

**PradnyeshSalunke** (Agent-First lean)
- Consistent growth across all windows: 857 → 857 → 857 → 1,735 → 1,948 → 2,296 → 2,968 → 3,731 → 4,237
- No single burst dominates; steady accumulation pattern despite Agent-First lean classification
- SuggEff 8.39, %Accept 19.4% — borderline; this is arguably the most hybrid-pattern user on the team

**vishal-tad** (Agent-First lean)
- CP1: 739 → CP5: 1,156 (slow early) → CP6: 2,815 (+1,659 in 16 days) → CP9: 3,737
- Mid-period dormancy then re-engagement; not a clean steady climber but consistent post-CP6

**Vyankatesh95** (Inline-First)
- CP1: 1,968 → CP9: 4,177 — steady, moderate growth throughout all windows
- %Accept 34.1% with SuggEff 30.27 — the highest SuggEff among Inline-First users, indicating a hybrid behavior where inline suggestions happen to be long blocks
- Plateau at CP7: no growth between CP7 and CP9 (stuck at 4,177)

---

### 5.3 Front-Loaders
*Users who contributed significant LoC early and have largely plateaued or slowed.*

**mshnayderman** (Inline-First)
- CP1: 20,399 — by far the highest baseline on the team; entered the analysis period already carrying large LoC
- Growth has been slow throughout: only +7,140 added over 64 days vs 20,399 at baseline
- Zero new LoC from CP7 onward (27,539 at CP7 through CP9): 15-day plateau as of Jun 23
- %Accept 27.8% — solid inline pattern; but the near-complete cessation since CP7 is a concern
- Classification note: "front-loading" here means pre-period accumulation, not in-period burst

**rpawar-nice** (Agent-First)
- CP1: 8,566 — third-highest baseline; spent most of the period nearly flat
- Added only 96 LoC over 64 days (8,566 → 8,662), with essentially all the increment in CP1→CP2
- SuggEff 60.15, %Accept 7.6% — highest SuggEff on the team; implies extremely large agent runs with very low acceptance
- Possible interpretation: rpawar-nice used Copilot intensively before CP1 to build large infrastructure/scaffolding, and shifted to manual work or review mode thereafter

**copilotshree** (Agent-First)
- CP1: 4,543 → CP9: 5,013 — added only 470 LoC over 64 days (all before CP5)
- Zero new LoC from CP5 through CP9 (37 days flat at 5,013)
- SuggEff 11.02, %Accept 4.8% — Agent-First; the plateau suggests agent sessions have stopped
- Name suggests a dedicated Copilot account; may reflect tooling/automation use rather than individual developer output

**moadzughul** (Agent-First)
- CP1: 2,572 → CP9: 3,409 — slow, modest growth throughout; no bursts
- SuggEff 9.19, %Accept 2.4% — Agent-First signal but very low absolute acceptance indicates minimal active use
- Most recent plateau: stuck at 3,409 since CP8 (11 days)

**jkumbhar** (Inline-First)
- CP1: 1,316 → CP9: 1,880 — low baseline with limited overall growth
- %Accept 22.0% — Inline-First; but LoC trajectory is nearly flat post-CP5 (1,788 at CP5, 1,880 at CP9)
- Despite active inline workflow, output velocity is very low

---

### 5.4 Mid-Period Stalls
*Users who showed growth early or mid-period but have plateaued or significantly slowed in recent windows.*

**mshnayderman** (Inline-First) — [also in Front-Loaders]
- Complete stall since CP7: 0 new LoC in 15 days
- Highest risk Inline-First stall: 27,539 is a strong absolute number but the cessation is total

**suhas-kakde** (Agent-First)
- CP1: 1,367 → CP6: 1,639 (slow growth) → CP7–CP8: flat → CP9: 2,005 (+328 late recovery)
- SuggEff 8.39, %Accept 1.7% — the lowest %Accept on the team; Agent-First but extremely passive
- Flat through CP6–CP7–CP8, then small CP8→CP9 jump suggests minor reactivation

**Akale23** (Inline-First)
- CP5: 1,856 → CP6: 2,409 → CP7: 2,472 → CP9: 2,472
- Flat since CP7: 0 new LoC in the last 15 days despite being an active Inline-First user
- %Accept 22.8% — consistent inline engagement, but output has stopped

**Vitthal-Nice** (Inline-First)
- CP4: 2,472 → CP6: 2,609 → CP9: 2,683 — very slow post-CP4 growth
- %Accept 40.4% — one of the highest on the team; yet LoC output is low and slowing
- Suggests the user is accepting a high fraction of small suggestions — inline completions rather than large block generation

**nilesht-19** (Inline-First)
- CP7: 7,160 → CP9: 7,354 (+194 in 15 days) — near-stall after a strong early run
- %Accept 30.2% and strong CP1–CP7 history makes this the most concerning recent stall for Inline-First users

**meghabiradar05** (Agent-First lean)
- CP3: 1,389 (burst) → CP9: 1,727 — minimal growth post-CP3; only +338 LoC in 56 days
- SuggEff 8.30, %Accept 12.5% — Agent-First lean; may have completed a one-time project and disengaged

---

### 5.5 Volatile
*Users with irregular, non-monotonic, or burst-heavy patterns with long flat gaps.*

**Kranti-nice** (Agent-First)
- Exemplar of Agent-First volatility: essentially flat from CP1–CP4 (2,148–3,259), then explosive CP5→CP6 (+20,657 in 16 days), then flat CP7, then +3,912 CP7→CP8, then +6,333 CP8→CP9
- Pattern is consistent with discrete agent session bursts separated by gaps
- SuggEff 47.53 — high; each agent session generates massive code blocks

**amol-salunkhe** (Agent-First)
- Similar burst pattern: near-zero CP1 (31), then +2,179 CP2→CP3, then +14,945 CP3→CP4, then +11,756 CP4→CP5, then varying rates thereafter
- The CP4→CP5 burst (+11,756 in 7 days = 1,679 LoC/day) is remarkable for Agent-First
- SuggEff 31.95 — agent-driven; velocity variation across windows reflects session timing

**trunalgawade** (Inline-First)
- Near-zero through CP6 (304), then three consecutive burst windows: +782, +952, +314
- Unusual for Inline-First: the activation pattern (dormant then sudden high output) is more typical of Agent-First
- %Accept 20.4% at the Inline-First floor; worth monitoring to see if this evolves toward Agent-First lean behavior

**sskalaskar** (Agent-First lean)
- CP1: 302 → CP3: 517 → CP4: 2,056 (burst) → flat CP4–CP5 → CP6: 2,609 → flat CP7 → CP8: 2,698 → CP9: 3,233
- Two distinct burst episodes (CP3→CP4 and CP8→CP9) separated by flat periods
- SuggEff 23.77 — relatively high for Agent-First lean; may belong in Agent-First proper

---

### 5.6 Flat Liners
*Users with very low growth or no meaningful progress.*

**rpawar-nice** (Agent-First)
- Only +96 LoC in 64 days; effectively inactive since CP2
- Despite highest SuggEff on the team (60.15), LoC output is negligible — the high SuggEff may reflect historical data from a prior period rather than active CP1–CP9 engagement

**copilotshree** (Agent-First)
- +470 LoC over 64 days, all before CP5; zero since CP5 (37 days)
- Likely a shared/automation account rather than an active individual developer

**abhijeetk268** (Inline-First)
- CP5: 173 → CP9: 656 — low absolute LoC, slow growth, flat since CP7
- %Accept 29.6% — genuine Inline-First user; simply low-volume

**pratikpawar12** (Agent-First lean)
- CP4: 166 → CP5: 250 → flat through CP9 (250 unchanged)
- 13 days of complete inactivity; may have disengaged entirely

**thakraln** (Agent-First lean)
- Zero through CP5; CP6: 69 → CP7: 69 (flat) → CP8: 750 (sudden jump) → CP9: 806
- Very low total (806) despite late activation; not yet a meaningful contributor

---

## 6. Per-User Cards — Top 20 Producers

---

### 1. amol-salunkhe
**Workflow: Agent-First** | SuggEff: 31.95 | %Accept: 1.5%
**CP9 LoC: 43,585** | Rank: #1

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 31 | 31 | 2,210 | 17,155 | 28,911 | 30,486 | 34,037 | 41,008 | 43,585 |

**Net additions per window:**
- CP2→CP3: +2,179 | CP3→CP4: +14,945 | CP4→CP5: +11,756 | CP5→CP6: +1,575 | CP6→CP7: +3,551 | CP7→CP8: +6,971 | CP8→CP9: +2,577

**Workflow-Aware Analysis:**
Agent-First classification fully explains the low 1.5% accept rate — this user is running autonomous agent sessions that generate large code blocks, accepting a small but substantial fraction. The CP3→CP4 burst (14,945 LoC in 13 days, 1,150 LoC/day) and the CP7→CP8 burst (6,971 in 4 days, 1,743 LoC/day) are signature Agent-First patterns. Do NOT judge by %Accept; judge by LoC/day velocity. At 43,585 total LoC in 64 days, this is the strongest Producer on the team by any metric. Recent trajectory positive but decelerating (CP8→CP9 at 234 LoC/day vs CP7→CP8 at 1,743 LoC/day).

**Status: Active, top performer. Monitor for next agent session activation.**

---

### 2. Kranti-nice
**Workflow: Agent-First** | SuggEff: 47.53 | %Accept: 4.6%
**CP9 LoC: 37,978** | Rank: #2

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 2,148 | 2,148 | 3,259 | 3,259 | 7,076 | 27,733 | 27,733 | 31,645 | 37,978 |

**Net additions per window:**
- CP3→CP4: +0 | CP4→CP5: +3,817 | CP5→CP6: +20,657 | CP6→CP7: +0 | CP7→CP8: +3,912 | CP8→CP9: +6,333

**Workflow-Aware Analysis:**
Extreme Agent-First volatility. The CP5→CP6 burst (+20,657 in 16 days = 1,291 LoC/day) is the largest single-window absolute gain on the team. SuggEff 47.53 is the second highest, confirming large agent-generated block requests. The zero-growth windows (CP3→CP4 and CP6→CP7) are not disengagement — they are inter-session gaps typical of Agent-First workflow. **Budget crisis note:** This user's premium consumption from the CP5→CP6 agent burst reportedly created a significant overspend (see Section 8). The high SuggEff means many tokens consumed per accepted line. Recent trajectory positive (CP8→CP9: +6,333 in 11 days = 576 LoC/day) but budget pressure likely continues.

**Status: Active, high output, HIGH budget risk.**

---

### 3. Prathmesh-Ranadive
**Workflow: Inline-First** | SuggEff: — | %Accept: 88.7%
**CP9 LoC: 35,091** | Rank: #3

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 1,373 | 1,373 | 1,848 | 8,783 | 9,489 | 20,436 | 27,052 | 27,052 | 35,091 |

**Net additions per window:**
- CP3→CP4: +6,935 | CP4→CP5: +706 | CP5→CP6: +10,947 | CP6→CP7: +6,616 | CP7→CP8: +0 | CP8→CP9: +8,039

**Workflow-Aware Analysis:**
Inline-First's standout performer and the proof point that inline workflow can compete with Agent-First on absolute LoC. The 88.7% accept rate is exceptional — nearly every suggestion is accepted, implying either very aligned inline completions or a developer accepting aggressively. The CP8→CP9 burst (+8,039 in 11 days = 731 LoC/day) is remarkable for an Inline-First user and is the strongest recent-window performance on the team. The CP7→CP8 zero-growth gap is unusual given this user's velocity — one anomalous flat period in an otherwise strong trend. Zero budget pressure: inline suggestions are token-efficient compared to Agent-First large-block generation.

**Status: Active, accelerating, best Inline-First performer.**

---

### 4. mshnayderman
**Workflow: Inline-First** | SuggEff: — | %Accept: 27.8%
**CP9 LoC: 27,539** | Rank: #4

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 20,399 | 20,399 | 20,951 | 22,268 | 22,268 | 24,387 | 27,539 | 27,539 | 27,539 |

**Workflow-Aware Analysis:**
Front-loader with a strong pre-period baseline. In-period growth is limited (+7,140 over 64 days). Complete plateau since CP7: zero new LoC in the last 15 days. For an Inline-First user with 27.8% accept rate, the expectation would be continued incremental growth — the flat line is anomalous and warrants follow-up. Possible explanations: project completion, vacation, shift to different tools, or work on non-tracked repositories.

**Status: PLATEAU since CP7. 15-day stall. Flag for follow-up.**

---

### 5. luisalvatierra
**Workflow: Inline-First** | SuggEff: — | %Accept: 24.2%
**CP9 LoC: 12,080** | Rank: #5

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 1,216 | 1,216 | 1,444 | 1,698 | 2,292 | 4,564 | 4,800 | 9,477 | 12,080 |

**Workflow-Aware Analysis:**
Late accelerator with the strongest CP7→CP8 burst among Inline-First users (+4,677 in 4 days = 1,169 LoC/day). This output rate at 24.2% accept suggests accepting meaningful-length inline completions. The CP8→CP9 continuation (+2,603 in 11 days = 237 LoC/day) shows deceleration but still positive trajectory. Inline-First users rarely maintain 1,000+ LoC/day rates sustained — the current deceleration is expected.

**Status: Active, strong late accelerator, normalizing velocity.**

---

### 6. chris-haun
**Workflow: Agent-First lean** | SuggEff: 7.72 | %Accept: 9.3%
**CP9 LoC: 10,493** | Rank: #6

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 6,034 | 6,376 | 6,670 | 6,758 | 8,592 | 10,264 | 10,359 | 10,384 | 10,493 |

**Workflow-Aware Analysis:**
The Agent-First lean category's top producer and an anomaly within it — 10,493 LoC rivals mid-tier Agent-First users. Consistent but slowing growth throughout the period. The CP4→CP5 burst (+1,834 in 7 days) was the peak window; post-CP5 growth has been minimal. SuggEff 7.72 is modest — this user is not running heavy agent sessions. More likely a consistent inline user whose %Accept just falls below the 20% threshold. The "lean" classification may understate this user's actual engagement.

**Status: Active, slowly decelerating. Reclassification to hybrid warranted.**

---

### 7. mfield1
**Workflow: Agent-First** | SuggEff: 12.12 | %Accept: 5.8%
**CP9 LoC: 9,803** | Rank: #7

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 4,414 | 4,414 | 5,637 | 8,566 | 9,071 | 9,251 | 9,300 | 9,800 | 9,803 |

**Workflow-Aware Analysis:**
Strong early output (CP2→CP4: +4,152 in 18 days) followed by deceleration. Growth has nearly flatlined since CP6: only +552 LoC in 35 days (CP6→CP9). SuggEff 12.12 and %Accept 5.8% confirm Agent-First; the deceleration suggests agent sessions have wound down. At 9,803 total LoC, this user built significant output but appears to be in maintenance/consolidation mode.

**Status: Near-plateau since CP6. Monitor for reactivation.**

---

### 8. rpawar-nice
**Workflow: Agent-First** | SuggEff: 60.15 | %Accept: 7.6%
**CP9 LoC: 8,662** | Rank: #8

**Workflow-Aware Analysis:**
Highest SuggEff on the team (60.15) but lowest in-period LoC growth (only +96 over 64 days). This paradox resolves under workflow-aware analysis: rpawar-nice likely used heavy agent sessions before CP1 to build the 8,566-LoC baseline, and is now largely inactive during the tracked period. The high SuggEff reading is a historical artifact. The current 8,662 total represents an essentially complete front-load with no Q2 momentum.

**Status: EFFECTIVELY INACTIVE in-period. Pre-period front-load.**

---

### 9. nilesht-19
**Workflow: Inline-First** | SuggEff: — | %Accept: 30.2%
**CP9 LoC: 7,354** | Rank: #9

| CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 | CP9 |
|---|---|---|---|---|---|---|---|---|
| 1,287 | 1,567 | 3,598 | 4,908 | 5,065 | 5,293 | 7,160 | 7,346 | 7,354 |

**Workflow-Aware Analysis:**
Strong consistent Inline-First performer through CP7, then near-stall: only +194 in the last 15 days (CP7→CP9). The CP6→CP7 burst (+1,867 in 5 days = 373 LoC/day) was peak velocity; it has sharply declined. %Accept 30.2% confirms genuine inline engagement throughout. The sudden deceleration post-CP7 mirrors mshnayderman's pattern and may reflect project-phase transitions.

**Status: Near-plateau since CP7. Monitor.**

---

### 10. copilotshree
**Workflow: Agent-First** | SuggEff: 11.02 | %Accept: 4.8%
**CP9 LoC: 5,013** | Rank: #10

**Workflow-Aware Analysis:**
Possible shared/automation account based on the username convention. All growth occurred before CP5; zero additions in 37 days. SuggEff 11.02 and %Accept 4.8% are consistent with Agent-First. If this is an automation account, LoC should be treated as tooling output, not developer productivity. Recommend clarifying account ownership before including in individual productivity metrics.

**Status: INACTIVE since CP5. Verify account type.**

---

### 11. PradnyeshSalunke
**Workflow: Agent-First lean** | SuggEff: 8.39 | %Accept: 19.4%
**CP9 LoC: 4,237** | Rank: #11

**Workflow-Aware Analysis:**
Most consistent steady-growth pattern on the team. Growth visible in every window post-CP3 with no flat gaps. %Accept 19.4% is at the border between Agent-First lean and Inline-First — this user exhibits hybrid behavior and may be the team's best example of balanced workflow. SuggEff 8.39 suggests moderate agent use; the high %Accept suggests inline acceptance on top of that. Despite the "lean" classification, 4,237 LoC with consistent velocity is a solid contribution.

**Status: Active, consistently growing. Potential hybrid reclassification.**

---

### 12. mshivarkar
**Workflow: Agent-First lean** | SuggEff: 7.34 | %Accept: 9.4%
**CP9 LoC: 4,201** | Rank: #12

**Workflow-Aware Analysis:**
Most dramatic late-activator in the Agent-First lean group. Near-zero through CP5 (28 LoC in 28 days), then 4,173 LoC added in the final 35 days. The activation timing in the CP5→CP6 window suggests project assignment change or tool adoption event. Current trajectory (CP6: 1,559 → CP7: 2,018 → CP8: 2,097 → CP9: 4,201) shows re-acceleration in the CP8→CP9 window (+2,104 in 11 days = 191 LoC/day) after a mid-period slowdown.

**Status: Active and accelerating. Watch CP9+ trajectory.**

---

### 13. Vyankatesh95
**Workflow: Inline-First** | SuggEff: 30.27 | %Accept: 34.1%
**CP9 LoC: 4,177** | Rank: #13

**Workflow-Aware Analysis:**
Classification note: SuggEff of 30.27 would normally indicate Agent-First, but %Accept of 34.1% overrides — this user accepts more than 1-in-3 suggestions, which is definitionally Inline-First behavior. The combination of high SuggEff + high %Accept suggests the user is receiving and accepting long inline completions (e.g., multi-line function completions via Copilot's extended suggestion feature) rather than running discrete agent sessions. Growth has plateaued since CP7 (4,177 unchanged for 15 days).

**Status: PLATEAU since CP7. Unusual hybrid SuggEff/Accept profile.**

---

### 14. vishal-tad
**Workflow: Agent-First lean** | SuggEff: 4.19 | %Accept: 8.8%
**CP9 LoC: 3,737** | Rank: #14

**Workflow-Aware Analysis:**
Dormant mid-period (CP3→CP5: zero growth), then re-engaged CP6 onward. The CP5→CP6 jump (+1,659 in 16 days = 104 LoC/day) and continued growth through CP8→CP9 (+217 in 11 days) indicate an active but moderate user. SuggEff 4.19 is the lowest among Agent-First lean users — barely above Inline-First territory. May be transitioning toward inline workflow over time.

**Status: Active, gradual growth, low-intensity usage.**

---

### 15. moadzughul
**Workflow: Agent-First** | SuggEff: 9.19 | %Accept: 2.4%
**CP9 LoC: 3,409** | Rank: #15

**Workflow-Aware Analysis:**
Agent-First with the second-lowest %Accept on the team (2.4%, above only suhas-kakde's 1.7%). Slow, consistent growth throughout with no major bursts. The SuggEff/Accept combination suggests accepting very small portions of large suggestions — possibly reviewing agent-generated code carefully and accepting fragments. Latest window: flat since CP8 (0 new LoC). Solid but low-ceiling contributor.

**Status: Minor plateau since CP8. Low velocity Agent-First.**

---

### 16. sskalaskar
**Workflow: Agent-First lean** | SuggEff: 23.77 | %Accept: 16.9%
**CP9 LoC: 3,233** | Rank: #16

**Workflow-Aware Analysis:**
SuggEff 23.77 is above many confirmed Agent-First users, making this "lean" classification potentially underconfident. %Accept 16.9% just misses the 20% Inline-First floor. Two burst episodes (CP3→CP4: +1,539; CP8→CP9: +535) separated by flat periods are consistent with episodic agent use. This user may warrant Agent-First reclassification on SuggEff signal alone.

**Status: Active. Potential reclassification to Agent-First.**

---

### 17. abhishekhole-nice
**Workflow: Agent-First** | SuggEff: 33.16 | %Accept: 3.2%
**CP9 LoC: 3,150** | Rank: #17

**Workflow-Aware Analysis:**
Strong CP3→CP4 burst (+2,403 in 13 days = 185 LoC/day) — a signature Agent-First activation event. Post-CP4 growth has been incremental: +428 in the final 40 days. SuggEff 33.16 and %Accept 3.2% are classic Agent-First signatures. The post-burst slowdown suggests the primary project workload that triggered agent use has concluded.

**Status: Slowing post-burst. Monitor for next project activation.**

---

### 18. trunalgawade
**Workflow: Inline-First** | SuggEff: — | %Accept: 20.4%
**CP9 LoC: 2,352** | Rank: #18

**Workflow-Aware Analysis:**
Most volatile Inline-First user. Near-zero through CP6 (304 in 44 days), then three consecutive active windows: +782, +952, +314. The activation timing and burst intensity (notably CP7→CP8: 952 in 4 days = 238 LoC/day) are more typical of Agent-First behavior, but the 20.4% accept rate anchors the classification. Possible interpretation: this user adopted Copilot late but intensively, using inline completion aggressively once they started. Continued monitoring needed.

**Status: Active and recent acceleration. Most-improved late activator.**

---

### 19. Vitthal-Nice
**Workflow: Inline-First** | SuggEff: — | %Accept: 40.4%
**CP9 LoC: 2,683** | Rank: #19

**Workflow-Aware Analysis:**
High accept rate (40.4%) but low LoC output — the classic Inline-First "accept-many-but-few-suggestions" pattern. The user is likely accepting short completions (auto-complete style) rather than long block suggestions. Growth was most active in CP3→CP4 (+1,292) and has been nearly flat since CP5 (+117 in 36 days). The high %Accept with low LoC growth suggests diminishing engagement rather than workflow efficiency.

**Status: Near-plateau. High accept rate, low volume.**

---

### 20. jayesh-rai
**Workflow: Agent-First** | SuggEff: 13.49 | %Accept: 18.4%
**CP9 LoC: 2,712** | Rank: #20

**Workflow-Aware Analysis:**
%Accept 18.4% is the highest among confirmed Agent-First users — a borderline classification. Near-zero through CP3 (1 LoC), then activation in CP4 (+776), acceleration in CP5→CP6 (+1,334 in 16 days = 83 LoC/day), and continued growth through CP9. SuggEff 13.49 suggests moderate agent use. This user may be running shorter agent sessions or using a blend of agent and inline — the relatively high %Accept for Agent-First is the key signal. Good recent velocity (+516 in CP8→CP9 = 47 LoC/day).

**Status: Active, gradual acceleration. Potential hybrid workflow.**

---

## 7. What Changed vs v1 Progression

The v1 progression file treated all users under a unified LoC velocity lens without workflow differentiation. Below is a summary of where the v2 workflow-aware analysis **changes the interpretation** of key findings:

### 7.1 Low %Accept is No Longer a Red Flag

**v1 reading:** Users with low %Accept (e.g., amol-salunkhe at 1.5%, Kranti-nice at 4.6%, rpawar-nice at 7.6%) might be flagged as underutilizing Copilot or being too selective.

**v2 correction:** These users are all Agent-First by proxy classification. Low %Accept is a *structural feature* of agentic workflow — accepting a small portion of a 200-line generated block still yields 3–20 lines of accepted code per interaction. Their LoC velocity (not %Accept) is the correct productivity lens. At 43,585 and 37,978 LoC respectively, amol-salunkhe and Kranti-nice are the team's top two producers.

### 7.2 High %Accept Does Not Guarantee High Output

**v1 reading:** Prathmesh-Ranadive (88.7% accept), Vitthal-Nice (40.4%), smishra-nice (78.3%) might all appear equally "engaged" on an accept-rate metric.

**v2 correction:** Prathmesh-Ranadive's 88.7% accept rate with 35,091 LoC is qualitatively different from Vitthal-Nice's 40.4% with only 2,683 LoC. The former is accepting long, substantive completions; the latter is likely accepting short auto-complete fragments. Inline-First users must be evaluated on both %Accept AND LoC output together.

### 7.3 Kranti-nice Budget Crisis is an Agent-First-Specific Risk

**v1 reading:** Kranti-nice is a top producer with anomalously high premium usage.

**v2 addition:** This is a predictable consequence of Agent-First workflow at high SuggEff (47.53). Every accepted line required ~47x more lines to be generated and presented, consuming tokens proportionally. Agent-First workflow is inherently token-expensive per accepted LoC. The budget crisis is not a Kranti-nice individual behavior issue — it is a systemic Agent-First cost pattern. Any Agent-First user with SuggEff > 30 running high-volume sessions is a budget risk.

### 7.4 mshnayderman's Plateau is More Concerning for Inline-First

**v1 reading:** mshnayderman's plateau since CP7 is a simple engagement drop.

**v2 addition:** For Inline-First users, plateaus are harder to explain away. Agent-First users naturally gap between sessions. Inline-First users (who work in continuous suggestion loops) should show steady incremental growth. A 15-day zero-LoC period for a 27.8%-accept Inline-First user suggests complete disengagement from Copilot-assisted work — not a session gap. This warrants a more direct follow-up than the same pattern in an Agent-First user.

### 7.5 rpawar-nice Inactivity Explanation

**v1 reading:** rpawar-nice is a low contributor with mysteriously high SuggEff.

**v2 addition:** The high SuggEff (60.15) with near-zero in-period LoC growth resolves cleanly: this is a pre-period front-loader whose high SuggEff reflects historical agent session intensity. The 8,566-LoC baseline represents work completed before CP1. During the tracked 64-day period, the user effectively stopped using Copilot. The SuggEff metric is not a current-period rate in this case — it is a cumulative artifact.

### 7.6 Acceleration Patterns Differ Structurally

**v1 reading:** All "late accelerators" are treated as a uniform cohort.

**v2 addition:** Agent-First late accelerators (Kranti-nice, giteshsawant, jayesh-rai) activate in discrete bursts tied to specific agent session events. Inline-First late accelerators (Prathmesh-Ranadive, trunalgawade, luisalvatierra) show more gradual ramp-up once engaged. The management action for each is different: Agent-First users need project/task alignment to trigger the next session; Inline-First users need habit reinforcement and suggestion quality feedback.

---

## 8. Budget Crisis by Workflow Type

### 8.1 Why Agent-First is Structurally Higher Budget Risk

The GitHub Copilot premium (overage) budget is consumed by:
- Agent/chat requests (high token consumption per request)
- Number of suggestions generated (high for high-SuggEff users)
- Length of generated blocks (higher for Agent-First by definition)

Inline suggestions (the Inline-First workflow) are lower per-token cost: they generate short completions in response to context, rather than autonomous large-block generation.

**Implication:** Holding all else equal, an Agent-First user generating 10,000 LoC will consume more premium budget than an Inline-First user generating the same 10,000 LoC. The ratio scales with SuggEff.

### 8.2 Budget Risk Ranking by Workflow Class

| Risk Tier | Users | Workflow | Risk Rationale |
|---|---|---|---|
| CRITICAL | Kranti-nice | Agent-First | SuggEff 47.53 + high absolute LoC = extreme token consumption; documented premium overspend |
| HIGH | amol-salunkhe | Agent-First | SuggEff 31.95 + 43,585 LoC = highest total token exposure on team |
| HIGH | rpawar-nice | Agent-First | SuggEff 60.15 (highest on team) — historical overspend risk even if current LoC is low |
| HIGH | abhishekhole-nice | Agent-First | SuggEff 33.16 — moderate LoC but high efficiency ratio |
| MEDIUM | Shreedevi-nice | Agent-First | SuggEff 55.47 — accelerating; budget risk grows with LoC growth |
| MEDIUM | sskalaskar | Agent-First lean | SuggEff 23.77 — high for "lean" classification |
| MEDIUM | jayesh-rai | Agent-First | SuggEff 13.49 — moderate; growing LoC increases total exposure |
| LOW | All Inline-First | Inline-First | %Accept-based workflow; lower token cost per accepted LoC |
| LOW | chris-haun, mshivarkar | Agent-First lean | Low SuggEff; token consumption is modest |

### 8.3 Kranti-nice Budget Crisis Deep Dive

Kranti-nice's documented premium crisis is the team's clearest Agent-First budget failure mode:
- SuggEff of 47.53 means for every 1 line accepted, ~47 lines were generated and presented to the user
- CP5→CP6 burst: 20,657 LoC added in 16 days
- Approximate generated lines during that burst: 20,657 × (47.53 / acceptance rate factor) — far exceeding the accepted count
- The premium overspend is not unexpected given the SuggEff; it was a structural consequence of the Agent-First workflow running at scale

**Recommendation:** Implement per-user Copilot Business vs Premium seat allocation based on workflow classification. Agent-First users with SuggEff > 20 should be on Premium seats with monitored budgets. Inline-First users can often operate on standard Business seats.

### 8.4 Inline-First Budget Efficiency

Inline-First users (Prathmesh-Ranadive, mshnayderman, nilesht-19, etc.) consume tokens at significantly lower rates relative to LoC output:
- Suggestions are short (typically 1–20 lines per suggestion)
- %Accept of 20–88% means fewer wasted generation cycles
- No autonomous long-running agent sessions generating thousands of lines per request

Prathmesh-Ranadive at 35,091 LoC with Inline-First workflow likely consumed far less premium budget than Kranti-nice at 37,978 LoC with Agent-First workflow.

---

## 9. Q2 Closing Assessment by Workflow Type

### 9.1 Team Summary as of Jun 23, 2026

**Total cumulative LoC: ~247,625** (CP9)
**Active users (any LoC added CP8→CP9): 19 of 34**
**Users with zero CP8→CP9 growth: 15 of 34 (44%)**
**64-day span | 9 checkpoints completed**

### 9.2 Agent-First Q2 Assessment

**Summary:** Agent-First workflow drove the team's highest absolute LoC numbers (amol-salunkhe: 43,585; Kranti-nice: 37,978) but came with high variance and budget risk. The pattern is: periods of intense agentic activity alternating with complete inactivity. Q2 closing velocity for the group is mixed — amol-salunkhe and Kranti-nice are still active; rpawar-nice and copilotshree are effectively inactive.

**Q2 closing signals:**
- Active Agent-First users: amol-salunkhe, Kranti-nice, Shreedevi-nice, jayesh-rai, giteshsawant, pdevle, mfield1 (slowing)
- Stalled Agent-First users: rpawar-nice, copilotshree, suhas-kakde (partial recovery), moadzughul
- Budget overspend alert: Kranti-nice (critical), amol-salunkhe (watch)

**Recommendation for Agent-First users:** Align agent session frequency with sprint cycle to prevent uncontrolled premium burst. Consider Copilot Business monthly budget caps for users with SuggEff > 20.

### 9.3 Inline-First Q2 Assessment

**Summary:** Inline-First workflow produced more consistent LoC accumulation curves with lower budget risk. The group's top performer (Prathmesh-Ranadive) is still accelerating at Q2 close, which is the most positive signal on the team. However, the Inline-First group has a notable plateau cluster: mshnayderman (15 days flat), Akale23 (15 days flat), Vyankatesh95 (15 days flat), nilesht-19 (near-flat).

**Q2 closing signals:**
- Active Inline-First users: Prathmesh-Ranadive (accelerating), luisalvatierra (active), trunalgawade (active), dsuraj25 (late burst)
- Stalled Inline-First users: mshnayderman (0 LoC since CP7), Akale23 (0 since CP7), Vyankatesh95 (0 since CP7), nilesht-19 (near-zero since CP7)
- Budget status: Low risk across the board; no Inline-First premium crisis

**Recommendation for Inline-First plateau cluster:** The simultaneous plateau of mshnayderman, Akale23, Vyankatesh95, and nilesht-19 after CP7 (Jun 8) suggests a possible team-wide event: sprint end, code freeze, or project completion. Investigate whether this is a coordinated pause rather than individual disengagement.

### 9.4 Agent-First Lean Q2 Assessment

**Summary:** The "lean" group showed the most mixed Q2 picture. chris-haun (top of the group at 10,493 LoC) is decelerating but still active. mshivarkar is accelerating from a late start. prashasti-jain shows strong CP8 burst then immediate slowdown. The group's overall contribution is modest relative to Agent-First proper users.

### 9.5 Final Q2 Workflow Verdict

| Dimension | Agent-First Winner | Inline-First Winner |
|---|---|---|
| Total LoC (absolute) | Agent-First (+20%) | — |
| Q2 % growth (May→Jun) | — | Inline-First (+112% vs +58%) |
| Budget efficiency | — | Inline-First (lower cost/LoC) |
| Consistency of growth | — | Inline-First (fewer flat gaps) |
| Top individual performer | amol-salunkhe (43,585) | Prathmesh-Ranadive (35,091) |
| Closing momentum (Jun) | Mixed | Inline-First (Prathmesh still accelerating) |
| Budget crisis risk | Agent-First (Kranti) | None |

**Overall Q2 assessment:** Both workflow types contributed substantially to the team's 247,625-LoC total. Agent-First drove the ceiling (top 2 spots) but Inline-First drove more consistent Q2 acceleration and closed stronger on a percentage basis. The simultaneous mid-June plateau in multiple Inline-First users is the key open question heading into Q3 — if the Jun 8 stall cluster is project-driven, expect reactivation; if it reflects disengagement, Inline-First Q3 output will disappoint.

**Team health rating: 7/10.** Strong absolute output, diverse active contributors, but ~44% of users contributing zero LoC in the final 11-day window is a yellow flag. The budget crisis on the Agent-First side needs structural remediation before Q3 agent sessions scale further.

---

*Report generated: June 23, 2026 | Analysis by: GitHub Copilot Usage Tracking System | v2 Workflow-Aware Edition*
*2-tier proxy classification based on SuggEff and %Accept at CP9. Classifications should be revisited when direct Agent Contribution % metrics become available in the Copilot data export.*
