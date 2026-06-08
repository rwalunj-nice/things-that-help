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
