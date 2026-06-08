# GitHub Copilot Usage Analysis — Cross-Framework Summary
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Scope:** 45 users (15 excluded per ignore list) | **Frameworks:** v1 Standard · v2 Workflow-Aware · Role+Momentum · CRQC

---

## Executive Summary

This report synthesizes findings from four independent framework analyses applied to the same June 8, 2026 dataset. Users are the same across all frameworks; tier differences reflect each framework's analytical lens.

**Key shift from prior analysis:** 15 users are now permanently excluded per `githun-ignored-users.md`. The prior June 8 analysis (before ignore list) covered 60 users. This analysis covers 45.

---

## Team at a Glance

| Metric | Value |
|---|---|
| Total users in scope | 45 |
| Ignored users | 15 (per githun-ignored-users.md) |
| Active developers | ~37 |
| Managers (in-scope) | 2 (SwapnilNice, ssamal-nice) |
| Research (tracked separately) | 1 (rwalunj-nice) |
| Total LoC Added (in-scope) | ~215,026 |
| Total Initiated Interactions | ~11,758 |
| Total Premium Requests | ~143,000 (est.) |
| In-scope Accept Rate | ~20.2% |

---

## Tier Comparison Across Frameworks

| Login | Name | v1 | v2 | Role+Mom | CRQC | Consensus |
|---|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | A | A | A 🚀 | A (9) | **A — unanimous** |
| Kranti-nice | Kranti Kaple | A | A | A 🚀 | A (9) | **A — unanimous** |
| mfield1 | Matt Field | A | A | A | A (8) | **A — unanimous** |
| Vitthal-Nice | Vitthal Devkar | A | A | A | A (9) | **A — unanimous** |
| Vyankatesh95 | V. Khadakkar | C | C | C | A (9) | **Split — CRQC surfaces hidden gem** |
| abhijeetk268 | Abhijeet Kolhe | C | C | C | A (8) | **Split — CRQC surfaces hidden gem** |
| jayesh-rai | Jayesh Rai | B | B | B | A (7) | **Near-unanimous A** |
| Akale23 | Amulya Kale | A | A | A | B (5) | **Split — CRQC penalizes ReqEff** |
| amol-salunkhe | Amol Salunkhe | A ⚠️ | A ⚠️ | A ↓ | C (4) | **Framework disagreement** |
| mshnayderman | M. Shnayderman | A ⚠️ | A ⚠️ | A ↓ | C (6) | **Framework disagreement** |
| luisalvatierra | Luis Salvatierra | B | B | B | C (5) | **Split — CRQC override** |
| jkumbhar | Jyoti Kumbhar | C | C | C | B (6) | **Split — CRQC lifts** |
| Prathmesh-Ranadive | P. Ranadive | C | C | C ↓ | C (4) | **Tier C — unanimous** |
| chris-haun | Chris Haun | C | C | C ↓ | C (4) | **Tier C — unanimous** |
| nilesht-19 | Nilesh Tonape | E | E | E ↓ | C (6) | **Split — CRQC: budget crisis ≠ zero** |
| thakraln | Nishtha Thakral | E | E | E | C (3) | **Split — CRQC: R=0+override** |
| trunalgawade | Trunal Gawade | E | E | E | C (3) | **Split — CRQC: R=0+override** |
| PradnyeshSalunke | P. Salunke | E | E | E ↓ | C (3) | **Split — CRQC: R=0+override** |
| abhishekhole-nice | Abhishek Hole | D | D | D | C (4) | **CRQC lifts slightly** |
| vishal-tad | Vishal Tad | D | D | D | C (4) | **CRQC lifts slightly** |
| moadzughul | Moad Alzughul | D | D | D | C (4) | **CRQC lifts slightly** |
| tusharpatil166719 | Tushar Patil | D | D | D | C (4) | **CRQC lifts slightly** |
| meghabiradar05 | Megha Biradar | D | D | D | C (3) | **CRQC lifts slightly** |
| dsuraj25 | Suraj Dubey | C | C | C | D (2) | **CRQC lowers — limited PR activity** |
| smishra-nice | Shridhar Mishra | D | D | D/Lead | D (2) | **D/Lead across all** |
| mshivarkar | Mohan Shivarkar | D | D | D | E (0) | **CRQC → E** |
| sgite-wfm | Shubham Gite | D | D | D | E (0) | **CRQC → E** |
| pdevle | Pratik Devle | D | D | D | B (5) | **CRQC lifts significantly** |
| sskalaskar | Sourabh Kalaskar | E | E | E | C (3) | **CRQC: team PR participation valued** |
| Shreedevi-nice | Shreedevi Patil | E | E | E | C (3) | **CRQC: team PR participation valued** |
| giteshsawant | Gitesh Sawant | E | E | E | E (0) | **E — unanimous** |
| ShubhamFulzele28 | Shubham Fulzele | E | E | E | E (0) | **E — unanimous** |
| prashasti-jain | Prashasti Jain | E | E | E | E (0) | **E — unanimous** |
| suhas-kakde | Suhas Kakde | E | E | E | E (0) | **E — unanimous** |
| pratikpawar12 | Pratik Pawar | E | E | E | E (0) | **E — unanimous** |
| kbajaj-nice | Kaushal Bajaj | E | E | E | E (0) | **E — unanimous** |
| dannycadima | Danny Cadima | E | E | E | E (0) | **E — unanimous** |

---

## Tier Distribution Comparison

| Tier | v1 | v2 | Role+Mom | CRQC |
|---|---|---|---|---|
| A | 7 | 7 | 7 | 7 |
| B | 2 | 2 | 2 | 3 |
| C | 6 | 6 | 6 | 16 |
| D | 9 | 9 | 9 | 2 |
| E | 13 | 13 | 13 | 9 |

> **CRQC insight:** Tier C expands dramatically (6 → 16) because CRQC's R=0 + Premium > 500 override prevents high-spending low-efficiency users from reaching B/A. This is a feature, not a bug — it surfaces the budget crisis as a tier classification, not just a footnote.

---

## Consensus Analysis

### Strong Consensus Tier A (unanimous or near-unanimous, 4+ frameworks)

| Login | Name | Consistency | Why It Matters |
|---|---|---|---|
| rpawar-nice | Ritesh Pawar | All 4 frameworks | Efficiency AND volume AND Breakout momentum. Model practitioner. |
| Kranti-nice | Kranti Kaple | All 4 frameworks | Breakout trajectory. Was marginal in June 3. Now top-tier across all lenses. |
| mfield1 | Matt Field | All 4 frameworks | Stable, lean, consistent. |
| Vitthal-Nice | Vitthal Devkar | All 4 frameworks | High trust signal (44% accept), lean spend, strong output. |
| jayesh-rai | Jayesh Rai | 3/4 (CRQC: A) | Consistent mid-upper performer. CRQC lifts to A. |

### Hidden Gems (surface only in CRQC)

| Login | Name | v1/v2/RoleMom | CRQC | Why Hidden |
|---|---|---|---|---|
| Vyankatesh95 | V. Khadakkar | C | A (9) | v1 penalized low LoC volume. CRQC: 27.8 ReqEff + 26.7% accept + lean spend = perfect efficiency profile. |
| abhijeetk268 | Abhijeet Kolhe | C | A (8) | 50 premium requests, 21.9 ReqEff. The most efficient user by cost. v1 missed because LoC ~1,095 is low absolute volume. |
| pdevle | Pratik Devle | D | B (5) | Agent-First with low LoC but lean spend. CRQC rewards the efficiency structure. |

### Framework Disagreements (amol-salunkhe and mshnayderman)

| Login | v1/v2 | CRQC | Explanation |
|---|---|---|---|
| amol-salunkhe | Tier A | Tier C | 34,037 LoC (in-scope leader) but 5,309 premium requests at 6.4 ReqEff. v1 rewards volume; CRQC penalizes the cost. Both are correct for their intended purpose. |
| mshnayderman | Tier A | Tier C | ~27,637 LoC at 5.1 ReqEff, 5,419 premium. Same structural issue. June 3 ReqEff was 43.2 — 88% decline in 5 days indicates a workflow change, not a capability regression. |

**Recommendation:** Use CRQC for budget conversations; use v1 for coaching and output recognition conversations. Both have a place.

---

## Momentum Highlights (Role+Momentum Framework)

### Breakout (>+100% ReqEff change)

| Login | Jun 3 | Jun 8 | Change |
|---|---|---|---|
| rpawar-nice | 20.1 | ~60.1 | +199% |
| Kranti-nice | ~7.6 | ~23.1 | +204% |

Both are consecutive Tier A — not just a spike, a sustained shift. Document what changed in their workflow.

### Declining (>−30% ReqEff change)

| Login | Jun 3 | Jun 8 | Change | Tier Impact |
|---|---|---|---|---|
| mshnayderman | 43.2 | 5.1 | −88% | A → A↓ (v1) / A → C (CRQC) |
| amol-salunkhe | 40.8 | 6.4 | −84% | A → A↓ (v1) / A → C (CRQC) |
| chris-haun | 11.9 | 2.8 | −76% | C → C↓ |
| nilesht-19 | 1.3 | 0.3 | −77% | E → E↓ |
| Prathmesh-Ranadive | ~5 | 2.5 | ~−50% | C → C↓ |

---

## Budget Crisis — Cross-Framework View

The budget crisis group is flagged independently by every framework:

| Login | v1 Tier | CRQC Tier | Premium Req | ReqEff | Framework Treatment |
|---|---|---|---|---|---|
| nilesht-19 | E | C (capped) | 23,108 | 0.3 | v1: E (zero output). CRQC: C (Agent-First LoC earns C=3, budget override caps). |
| thakraln | E | C (capped) | 11,112 | 0.2 | Same pattern. |
| trunalgawade | E | C (capped) | 10,863 | 0.2 | Same pattern. |
| PradnyeshSalunke | E | C (capped) | 9,892 | 0.2 | Same pattern. |
| Prathmesh-Ranadive | C | C (capped) | 10,733 | 2.5 | v1: C (moderate). CRQC: C (override). |
| mshnayderman | A | C (capped) | 5,419 | 5.1 | v1: A (high LoC). CRQC: C (override). Coaching urgency: HIGH. |
| amol-salunkhe | A | C (capped) | 5,309 | 6.4 | v1: A (LoC leader). CRQC: C (override). Coaching urgency: HIGH. |

**All frameworks agree on the budget signal, even if tier labels differ.** The combined spend of these 7 users (~76,000 premium requests) at current efficiency produces ~100,000 LoC. At Tier A efficiency, that budget should produce 1.5M+ LoC.

---

## Framework Selection Guide

| Use Case | Recommended Framework | Reason |
|---|---|---|
| Weekly team tier assignment | **v2 Workflow-Aware** | Accounts for Agent-First correctly. Fast to apply. |
| Coaching conversations | **Role+Momentum** | Surfaces trajectory, not just snapshot. Protects Breakout users from pressure. |
| VP/budget reporting | **CRQC** | Scored, auditable, defensible. Override rules make budget crisis visible. |
| Historical trending | **v1 Standard** | Most consistent longitudinally. Comparable across periods. |
| One-shot team health check | **Cross-framework summary (this file)** | Consensus tier = most stable signal. |

---

## Final Recommendations

### Immediate Actions (This Week)

1. **Coach mshnayderman and amol-salunkhe** — Both were top-3 efficiency performers on June 3. Both declined 84–88% with 5–7× premium spikes. This is not organic. A single coaching conversation to restore prior workflows is the highest-ROI action available.

2. **Investigate nilesht-19, thakraln, trunalgawade, PradnyeshSalunke** — Combined 55,000+ premium requests at near-zero efficiency (0.2–0.3 ReqEff). Set usage guidance or caps. These four users alone consume more premium budget than all Tier A users combined.

3. **Recognize rpawar-nice and Kranti-nice** — Back-to-back Breakout performance. Both crossed 200%+ momentum. Make this visible — it reinforces the behavior you want the rest of the team to emulate.

### Short-Term Actions (This Sprint)

4. **Elevate Vyankatesh95 and abhijeetk268** — Both are CRQC Tier A with C/B in v1. They are the most efficient cost producers on the team. Consider pairing them with Tier B/C developers as efficiency models.

5. **Address Tier E (9 users)** — 9 users with CRQC = 0 have zero productive signal across all four frameworks. These require an activation conversation or license reallocation review.

6. **Manager coaching for ssamal-nice** — Manager threshold (>5 ReqEff) not met. Even at the manager-adjusted bar, engagement is insufficient.

### Structural

7. **Fix the Agent-First budget problem structurally** — The 4 extreme budget drains (nilesht-19 et al.) are all Agent-First with near-zero LoC acceptance. This is likely a misunderstanding of how agent mode costs accrue. A usage training session would likely resolve it without individual coaching.

---

## Managers and Research

| Login | Name | Role | Metrics | Assessment |
|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | Manager | Int 273, LoC 3,140, ReqEff ~31.4 | Active coder-manager. Exceeds manager T2 threshold. |
| ssamal-nice | Susovan Samal | Manager | Int ~30, LoC 38, ReqEff ~3.2 | Does not meet manager T2 threshold (>5). Coaching recommended. |
| rwalunj-nice | Rahul Walunj | Research | Tracked separately: Int + Premium only | Excluded from tier scoring per benchmark spec. |

---

*Cross-Framework Summary — 15 users excluded per `githun-ignored-users.md`. Framework reference files: github-quick-benchmark.md (v1), github-quick-benchmark-v2.md (v2), github-benchmark-role-momentum.md, github-benchmark-CRQC.md.*

---

## Trend Analysis — April 20 to June 8, 2026

> **Scope:** 37 in-scope developers + 2 managers + 1 research (40 total, 15 excluded per `githun-ignored-users.md`).  
> **Checkpoints:** 7 snapshots — CP1 Apr 20 · CP2 Apr 23 · CP3 Apr 28 · CP4 May 11 · CP5 May 18 · CP6 Jun 3 · CP7 Jun 8.  
> **LoC values:** Cumulative from April 1 at each snapshot. ReqEff is a point-in-time efficiency ratio, not cumulative — it can improve even when no new LoC is added if older, less efficient premium requests age out of the measurement window.

---

### Checkpoint Overview

| CP | Date | Key Event |
|---|---|---|
| CP1 | Apr 20 | Q2 opening state. Front-loaders (Mikhail, Ritesh, Shraddha) already high. ~26 active users. |
| CP2 | Apr 23 | Minimal movement; 3-day window only. Most users unchanged. |
| CP3 | Apr 28 | First burst: Amol Salunkhe enters at 2,210 LoC (was 31 at CP1). Kranti reaches 3,259. |
| CP4 | May 11 | Major onboarding wave: Amol 17,155, Prathmesh 8,783, Jayesh 777. Premium Requests not in file — SuggEff used as proxy. |
| CP5 | May 18 | Team dataset expanded to 55 users (ignored sub-teams added). Late accelerators continuing strong. |
| CP6 | Jun 3 | Late accelerators peak: Prathmesh 20,436, Kranti 27,733. Budget crisis users first clearly identifiable. |
| CP7 | Jun 8 | Final Q2 snapshot. Amol reaches 34,037 (team LoC leader). Breakout efficiency: rpawar-nice +199%, Kranti-nice +204%. |

---

### Per-User LoC Progression (Cumulative from April 1)

> `—` = user not present or not captured at this checkpoint. `~` = approximate. Sorted by Jun 8 LoC descending.

| Developer | Name | Apr 20 | Apr 23 | Apr 28 | May 11 | May 18 | Jun 3 | Jun 8 | Pattern |
|---|---|---|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | 31 | 31 | 2,210 | 17,155 | 28,911 | 30,486 | 34,037 | Steady Climber |
| Kranti-nice | Kranti Kaple | 2,148 | 2,148 | 3,259 | — | 7,076 | 27,733 | 27,733 | Late Accelerator |
| mshnayderman | Mikhail Shnayderman | 20,399 | 20,399 | 20,951 | 22,268 | 22,268 | 24,387 | 27,539 | Steady Climber |
| Prathmesh-Ranadive | Prathmesh Ranadive | 1,373 | 1,373 | 1,848 | 8,783 | 9,489 | 20,436 | 27,052 | Late Accelerator |
| chris-haun | Chris Haun | 6,034 | 6,376 | 6,670 | 6,758 | 8,592 | 10,264 | ~10,359 | Steady Climber |
| mfield1 | Matt Field | 4,414 | 4,414 | 5,637 | 8,566 | 9,071 | 9,251 | ~9,300 | Front-Loaded |
| rpawar-nice | Ritesh Pawar | 8,566 | 8,640 | 8,640 | 8,640 | 8,658 | 8,662 | 8,662 | Front-Loaded (Stalled) |
| nilesht-19 | Nilesh Tonape | 1,287 | 1,567 | 3,598 | 4,908 | 5,065 | 5,293 | 7,160 | Budget Crisis |
| copilotshree | Shraddha Kale | 4,543 | 4,543 | 4,553 | 4,706 | 5,013 | 5,013 | 5,013 | Mid-Quarter Stall |
| luisalvatierra | Luis Salvatierra | 1,216 | 1,216 | 1,444 | 1,698 | 2,292 | 4,564 | ~4,800 | Late Accelerator |
| Vyankatesh95 | Vyankatesh Khadakkar | 1,968 | 1,968 | 2,350 | 2,795 | 3,673 | 4,151 | 4,177 | Steady Climber |
| moadzughul | Moad Alzughul | 2,572 | 2,572 | 2,620 | 2,655 | 2,749 | 3,035 | ~3,100 | Steady Climber |
| PradnyeshSalunke | Pradnyesh Salunke | 857 | 857 | 857 | 1,735 | 1,948 | 2,296 | ~2,968 | Budget Crisis |
| abhishekhole-nice | Abhishek Hole | 267 | 267 | 319 | 2,722 | 2,803 | 2,803 | 2,936 | Mid-Quarter Stall |
| vishal-tad | Vishal Tad | 739 | 952 | 1,156 | — | — | 2,815 | ~2,900 | Front-Loaded |
| sskalaskar | Sourabh Kalaskar | 302 | 517 | 517 | 2,056 | 2,056 | 2,609 | ~2,700 | Steady Climber |
| Vitthal-Nice | Vitthal Devkar | 1,180 | 1,180 | 1,180 | 2,472 | 2,566 | 2,609 | ~2,800 | Volatile → Rising |
| jayesh-rai | Jayesh Rai | 1 | 1 | 1 | 777 | 862 | 2,196 | ~2,500 | Late Accelerator |
| Akale23 | Amulya Kale | 292 | 292 | 779 | 1,133 | 1,856 | 2,409 | ~2,600 | Steady Climber |
| jkumbhar | Jyoti Kumbhar | 1,316 | 1,316 | 1,412 | — | 1,788 | 1,868 | ~2,000 | Front-Loaded |
| tusharpatil166719 | Tushar Patil | 381 | 381 | 853 | 1,389 | 1,631 | 1,798 | ~1,900 | Steady Climber |
| mshivarkar | Mohan Shivarkar | 0 | 1 | 28 | 28 | 28 | 1,559 | 2,018 | Late Accelerator |
| meghabiradar05 | Megha Biradar | — | — | — | — | 1,389 | 1,684 | ~1,700 | Late Entry |
| suhas-kakde | Suhas Kakde | 1,367 | 1,367 | 1,597 | 1,615 | 1,639 | 1,639 | 1,639 | Front-Loaded (Stalled) |
| Shreedevi-nice | Shreedevi Patil | 38 | 56 | 88 | 88 | 690 | 1,013 | 1,416 | Steady Climber |
| thakraln | Nishtha Thakral | 0 | 0 | 0 | 0 | 0 | 69 | ~1,111 | Budget Crisis |
| trunalgawade | Trunal Gawade | 6 | 6 | 61 | 261 | 302 | 304 | ~1,086 | Budget Crisis |
| pdevle | Pratik Devle | 361 | 361 | 368 | 370 | 370 | 1,049 | ~1,100 | Late Accelerator |
| prashasti-jain | Prashasti Jain | 0 | 0 | 0 | 203 | 837 | 872 | ~900 | Mid-Quarter Stall |
| ShubhamFulzele28 | Shubham Fulzele | — | — | — | — | — | — | 739 | Late Entry (Jun 8) |
| dsuraj25 | Suraj Dubey | 491 | 491 | 491 | 491 | 491 | 504 | ~510 | Flat Liner |
| sgite-wfm | Shubham Gite | 29 | 29 | 79 | 268 | 271 | 316 | 329 | Mid-Quarter Stall |
| smishra-nice | Shridhar Mishra | 0 | 0 | 0 | 155 | 155 | 155 | 155 | Flat Liner |
| pratikpawar12 | Pratik Pawar | 0 | 0 | 0 | 166 | 250 | 250 | 250 | Flat Liner |
| giteshsawant | Gitesh Sawant | — | — | — | — | — | — | ~50 | Late Entry (Jun 8) |
| kbajaj-nice | Kaushal Bajaj | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Flat Liner |
| dannycadima | Danny Cadima | — | — | — | — | 1 | 34 | 34 | Flat Liner |

**Managers:**

| Login | Name | Apr 20 | Apr 23 | Apr 28 | May 11 | May 18 | Jun 3 | Jun 8 |
|---|---|---|---|---|---|---|---|---|
| SwapnilNice | Swapnil Zade | — | — | — | — | — | — | 3,140 |
| ssamal-nice | Susovan Samal | 38 | 38 | 38 | 38 | 38 | 38 | 38 |

---

### Tier Trajectory — Apr 20 → Jun 3 → Jun 8 (v1 Standard)

| Developer | Apr 20 | Jun 3 | Jun 8 | Net Change | Status |
|---|---|---|---|---|---|
| amol-salunkhe | E | A | A⚠️ | +4 tiers | Most Improved — efficiency now at risk |
| Kranti-nice | D | B | A | +3 tiers | Most Improved — breakout story |
| jayesh-rai | E | C | B | +3 tiers | Rising — consistent Q2 build |
| Vitthal-Nice | C | B | A | +2 tiers | Rising — lean efficiency wins |
| mfield1 | B | A | A | +1 tier | Stable-up — no efficiency loss |
| mshivarkar | E | D | D | +1 tier | Recovering — late acceleration |
| mshnayderman | A | A | A⚠️ | 0 | Was team leader — efficiency risk flag |
| rpawar-nice | A | B | A | 0 net | Recovered — rolling-window effect |
| Akale23 | B | C | A | 0 net | Volatile path — reached Tier A |
| jkumbhar | C | C | C | 0 | Stable — no movement in either direction |
| chris-haun | B | B | C | −1 tier | Slipping — ReqEff −76% Jun 3→Jun 8 |
| luisalvatierra | A | C | B | −1 net | Slipping — partial recovery from C |
| Vyankatesh95 | B | B | C | −1 tier | Slipping — efficiency plateau |
| abhijeetk268 | A | D | C | −2 tiers | Declining — volume stall |
| suhas-kakde | C | C | E | −2 tiers | Declining — zero new LoC since May 18 |
| PradnyeshSalunke | C | C | E | −2 tiers | Budget crisis — spend without return |
| moadzughul | A | D | D | −3 tiers | Most Declined — ReqEff collapse 53.6 → ~14.8 |
| nilesht-19 | D | B | E | −1 net (volatile) | Budget crisis — 4+ checkpoints unresolved |

---

### Most Improved — April 20 to June 8

| Developer | Name | Apr 20 Tier | Jun 8 Tier | Tier Gain | LoC Growth | Driver |
|---|---|---|---|---|---|---|
| amol-salunkhe | Amol Salunkhe | E | A⚠️ | +4 | 31 → 34,037 | Rapid adoption from CP3; efficiency now declining — monitor |
| Kranti-nice | Kranti Kaple | D | A | +3 | 2,148 → 27,733 | Sustained late acceleration; Q2 breakout story |
| jayesh-rai | Jayesh Rai | E | B | +3 | 1 → ~2,500 | Late starter, consistent build from CP4 onward |
| Vitthal-Nice | Vitthal Devkar | C | A | +2 | 1,180 → ~2,800 | Efficiency-first approach; lean premium spend |
| mfield1 | Matt Field | B | A | +1 | 4,414 → ~9,300 | Steady compounding; no efficiency degradation |

**Notable:** amol-salunkhe and Kranti-nice together account for over 50% of all Q2 LoC growth from the in-scope team.

---

### Most Declined — April 20 to June 8

| Developer | Name | Apr 20 Tier | Jun 8 Tier | Net Change | Root Cause |
|---|---|---|---|---|---|
| moadzughul | Moad Alzughul | A | D | −3 tiers | ReqEff collapsed 53.6 → ~14.8; LoC growth stopped while premium spend continued |
| nilesht-19 | Nilesh Tonape | D | E | volatile | 23,108 premium requests vs. 7,160 LoC. Budget crisis since CP3. |
| abhijeetk268 | Abhijeet Kolhe | A | C | −2 tiers | Volume stall — 656 LoC unchanged Jun 3 → Jun 8; near-inactive |
| suhas-kakde | Suhas Kakde | C | E | −2 tiers | Front-loaded pattern — 1,639 LoC flat since May 18; 7+ weeks zero activity |
| PradnyeshSalunke | Pradnyesh Salunke | C | E | −2 tiers | Budget crisis — 9,892 premium requests vs. ~2,968 LoC; ReqEff ~0.3 |
| luisalvatierra | Luis Salvatierra | A | B | −1 tier | ReqEff collapsed 30.4 → 2.9 (−90%); LoC still growing but efficiency gone |

**Key observation:** moadzughul's A → D decline is the steepest efficiency drop on the team. Started Q2 as the #3 ranked user by efficiency, ended in Tier D. His premium spend is not extreme, but output-per-request deteriorated sharply over 7 checkpoints — distinct from the budget crisis group and requiring a separate coaching conversation.

---

### Breakout Stories — Jun 3 to Jun 8

#### rpawar-nice — Ritesh Pawar (+199% ReqEff)

| Metric | Jun 3 | Jun 8 | Change |
|---|---|---|---|
| LoC | 8,662 | 8,662 | 0 |
| ReqEff | 20.1 | ~60.1 | +199% |
| Tier (v1) | B | A | +1 |

Zero new LoC between Jun 3 and Jun 8, yet ReqEff tripled. The rolling measurement window retired earlier, less-efficient premium interactions, improving the ratio. Ritesh's actual output is front-loaded (minimal new work since early May) but his normalized efficiency looks excellent. Celebrate the efficiency recovery — then start a conversation about re-engagement. At 8,662 LoC with proven efficiency, he has strong Q3 headroom.

#### Kranti-nice — Kranti Kaple (+204% ReqEff)

| Metric | Jun 3 | Jun 8 | Change |
|---|---|---|---|
| LoC | 27,733 | 27,733 | 0 |
| ReqEff | ~7.6 | ~23.1 | +204% |
| Tier (v1) | B | A | +1 |

Similar rolling-window dynamic, but with a different character. Kranti was generating massive LoC volume through June 3, and the efficiency metric lagged the output. As that burst activity resolved, the efficiency number normalized upward. The full Q2 trajectory — 2,148 LoC at CP1 to 27,733 at CP7 — is one of the team's best Late Accelerator stories. Protect from any tier downgrade pressure entering Q3.

---

### Persistent Budget Crisis — Users At Risk 3+ Checkpoints

> Budget crisis = ReqEff < 1.0 sustained across multiple checkpoints, or sudden high-spend / low-return spike at latest checkpoint.

| Developer | Name | First Flagged | Premium (Jun 8) | LoC (Jun 8) | ReqEff | Risk |
|---|---|---|---|---|---|---|
| nilesht-19 | Nilesh Tonape | CP3 (Apr 28) | 23,108 | 7,160 | 0.3 | Critical — 5th consecutive CP unresolved |
| PradnyeshSalunke | Pradnyesh Salunke | CP4 (May 11) | 9,892 | ~2,968 | ~0.3 | Critical — 3+ CPs |
| thakraln | Nishtha Thakral | CP7 (Jun 8) | 11,112 | ~1,111 | ~0.1 | Critical — new entrant, immediate action |
| trunalgawade | Trunal Gawade | CP7 (Jun 8) | 10,863 | ~1,086 | ~0.1 | Critical — new entrant |
| Prathmesh-Ranadive | Prathmesh Ranadive | CP5 (May 18) | 10,733 | 27,052 | 2.5 | Warning — high LoC but inefficient spend |

**Timeline context:**
- **Nilesh Tonape** has been in budget crisis territory since at least CP3 (Apr 28). Five consecutive checkpoints without remediation. Total premium spend has grown ~4× from early checkpoints while LoC growth slowed.
- **Nishtha Thakral and Trunal Gawade** are new crisis entries at CP7. Both show 0 or near-0 LoC at CP1–CP5, then suddenly appear with 10,000+ premium requests at Jun 8. This spike pattern suggests agent-mode experimentation or unstructured usage that consumed budget without producing code. Requires immediate conversation.
- **Prathmesh Ranadive** is a complex case: high total LoC (27,052) but poor efficiency (2.5 ReqEff). He generates real output but at roughly 4× the cost of efficient users. His intervention is "optimize how you use Copilot," not "use Copilot."

---

### Pattern Classification Summary (Updated Jun 8)

| Pattern | Users | Characteristic |
|---|---|---|
| **Steady Climber** | amol-salunkhe, mshnayderman, chris-haun, luisalvatierra, Vyankatesh95, moadzughul, sskalaskar, Akale23, tusharpatil166719, Shreedevi-nice | Consistent incremental growth across all checkpoints. Widest category. |
| **Late Accelerator** | Kranti-nice, Prathmesh-Ranadive, jayesh-rai, mshivarkar, pdevle | >60% of total Q2 LoC came in May 18–Jun 8 window. |
| **Front-Loaded** | mfield1, rpawar-nice, suhas-kakde, jkumbhar, vishal-tad | >60% of total LoC in first 3 checkpoints (Apr 20–Apr 28). Growth stalled since. |
| **Mid-Quarter Stall** | copilotshree, abhishekhole-nice, sgite-wfm, prashasti-jain | Activity burst in CP3/CP4 then plateau. Neither front-loaded nor late-accelerating. |
| **Budget Crisis** | nilesht-19, PradnyeshSalunke, thakraln, trunalgawade | LoC–premium ratio deteriorated over time. Spend without proportionate return. |
| **Volatile** | Vitthal-Nice, Akale23, nilesht-19 | Large swings between consecutive checkpoints in both LoC and efficiency. |
| **Flat Liner** | smishra-nice, pratikpawar12, dsuraj25, kbajaj-nice, dannycadima | <500 total LoC, near-zero growth throughout Q2. |
| **Late Entry** | meghabiradar05, ShubhamFulzele28, giteshsawant | Joined dataset at CP5 or later. Insufficient history for full pattern classification. |

---

### Coaching Effectiveness — Jun 3 Interventions → Jun 8 Outcomes

| User | Jun 3 Flag | Jun 8 Result | Outcome |
|---|---|---|---|
| amol-salunkhe | Tier A but efficiency risk (agent-mode) | A⚠️ — ReqEff −84% (40.8 → 6.4) | Not effective. Efficiency collapse continued. Escalate. |
| mshnayderman | Tier A but declining ReqEff | A⚠️ — ReqEff −88% (43.2 → 5.1) | Not effective. 9.5× premium spike. Immediate action required. |
| nilesht-19 | Budget crisis — 3+ CPs | Tier E — ReqEff 0.3, 23,108 premium | No change. 5th consecutive CP without resolution. |
| Prathmesh-Ranadive | Tier A with budget concern | Tier C — ReqEff 2.5 | Tier declined but still active. Requires efficiency optimization coaching. |
| rpawar-nice | Tier B, zero new LoC since May | Tier A — ReqEff +199% | Efficiency recovered (rolling-window effect). Zero new LoC still needs address. |
| Kranti-nice | Tier B, strong momentum | Tier A — ReqEff +204% | Breakout success. Best Jun 3 → Jun 8 coaching story. |

**Net signal:** 2 of 6 tracked interventions showed improvement. The 4 declining users all continued deteriorating. Either coaching did not reach them in the 5-day window, or the efficiency collapse is structural (workflow change, project type change, model switch). Treat as unresolved and escalate to manager level for all four.

---

### Q3 Entry Readiness (Updated — June 8, 2026)

#### Hot — Q3 Ready (Tier A/B, healthy efficiency)

| Developer | Name | Jun 8 Tier | ReqEff | LoC | Q3 Prognosis |
|---|---|---|---|---|---|
| rpawar-nice | Ritesh Pawar | A | ~60.1 | 8,662 | Efficiency leader. Re-engage on active output. |
| Kranti-nice | Kranti Kaple | A | ~23.1 | 27,733 | Best Q2 trajectory. Protect in Q3. |
| mfield1 | Matt Field | A | ~14.3 | ~9,300 | Consistent. Strong Q3 base. |
| Vitthal-Nice | Vitthal Devkar | A | ~14 | ~2,800 | Lean spend, improving. Watch for volume growth. |
| Akale23 | Amulya Kale | A | ~6.7 | ~2,600 | Volatile path to Tier A. Needs consistency in Q3. |
| jayesh-rai | Jayesh Rai | B | ~19.2 | ~2,500 | Strong Q2 growth from near-zero. Good momentum. |
| luisalvatierra | Luis Salvatierra | B | 2.9 | ~4,800 | LoC growing but ReqEff drop is a concern. Coaching on efficiency. |

#### Warm — Needs Adjustment Before Q3

| Developer | Name | Jun 8 Tier | Issue | Action |
|---|---|---|---|---|
| mshnayderman | Mikhail Shnayderman | A⚠️ | ReqEff −88%. Was team efficiency leader at Jun 3. | Investigate premium spike immediately before Q3 begins. |
| amol-salunkhe | Amol Salunkhe | A⚠️ | ReqEff −84%. 7× premium spike. | Workflow audit — possible mode switch to agent-heavy usage. |
| chris-haun | Chris Haun | C | Was Tier B at Jun 3. ReqEff −76% in 5 days. | Manager check-in needed. |
| Prathmesh-Ranadive | Prathmesh Ranadive | C | High LoC (27k) but poor efficiency (2.5 ReqEff). | Efficiency coaching — not usage growth coaching. |
| Vyankatesh95 | Vyankatesh Khadakkar | C | Dropped from B at Jun 3. Efficiency flat. | CRQC gives Tier A on lean spend — investigate the v1/CRQC gap. |
| jkumbhar | Jyoti Kumbhar | C | Stable but limited growth. Front-loaded pattern. | Re-engagement strategy for Q3. |

#### Cold — Intervention Required

| Developer | Name | Jun 8 Tier | Pattern | Priority |
|---|---|---|---|---|
| nilesht-19 | Nilesh Tonape | E | Budget crisis 5 CPs | Immediate — unresolved since CP3 |
| thakraln | Nishtha Thakral | E | Budget spike at CP7 | Immediate — 11k premium / 1.1k LoC |
| trunalgawade | Trunal Gawade | E | Budget spike at CP7 | Immediate — 10.9k premium / 1.1k LoC |
| PradnyeshSalunke | Pradnyesh Salunke | E | Budget crisis 3+ CPs | High — 9.9k premium / ~3k LoC |
| suhas-kakde | Suhas Kakde | E | Zero new LoC since May 18 | Re-engagement coaching |
| abhijeetk268 | Abhijeet Kolhe | C | Zero new LoC since Jun 3 | Re-engagement — CRQC Tier A on past efficiency |
| moadzughul | Moad Alzughul | D | Efficiency collapse from Tier A | Coaching on prompt quality and request structure |
| kbajaj-nice | Kaushal Bajaj | E | 5 LoC total — entire Q2 | Onboarding support |
| smishra-nice | Shridhar Mishra | D | 155 LoC flat for 4+ CPs | Lead-role coaching conversation |

---

*Trend data sourced from `github-ai-analysis-20-april-2026.md` through `github-ai-analysis-8-june-2026.md`. All tier values reflect v1 Standard Framework unless noted. Early checkpoint data used display names mapped to current logins. Approximate values (~) derived from contextual interpolation where exact figures were not available in source files.*
