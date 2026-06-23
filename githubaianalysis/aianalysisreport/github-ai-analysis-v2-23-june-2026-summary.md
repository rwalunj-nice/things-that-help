# WFM Integrations — GitHub Copilot Usage Analysis
## Cross-Framework Executive Summary | CP9 | June 23, 2026

**Product:** WFM Integrations
**R&D VP:** WFM
**Analysis Window:** April 20 → June 23, 2026 (64 days)
**Checkpoints Completed:** 9 of 9 (CP1 Apr 20 → CP9 Jun 23)
**Frameworks Applied:** v1 Standard · v2 Workflow-Aware · Role+Momentum · CRQC
**File:** 9 of 9 — Cross-Framework Synthesis
**Q2 Close:** June 30, 2026 — **7 days remaining**

---

## 1. Q2 Closing Status

Q2 ends in 7 days. This is the final checkpoint before the quarter closes. The program is 64 days mature — long enough to distinguish genuine adoption patterns from noise, and to make confident Q3 entry recommendations.

The headline story is a team split into two diverging halves:

- **One half** is producing well, accelerating into Q2 close, and ready for Q3.
- **The other half** is either stalled (zero new output in the final 11 days) or burning premium budget at a rate that has not translated into code output at any point in the quarter.

The single most urgent finding is that **five budget-crisis users were flagged at CP8 (June 12) and every one of them got worse, not better, in the 11 days that followed.** Coaching signals did not reach the team, or did not land. That is the primary action item before Q2 closes.

---

## 2. Team at a Glance (CP9 Totals)

| Metric | Value |
|---|---|
| In-scope developers | 37 |
| Managers / Lead / Research (excluded from LoC analysis) | 4 |
| Developer without Copilot license (ssnikam) | 1 |
| Ignored / inactive users | 16 |
| Frameworks applied per checkpoint | 4 |
| Total checkpoints | 9 |
| **Total LoC Added (team, CP9)** | **~256,000** |
| **Total Premium Requests (team, CP9)** | **~371,000+** |
| **Team-wide Request Efficiency (ReqEff)** | **~0.69** |
| Total PRs (team) | 496 |
| PR Merge Rate | 88.7% |
| Average Time to Merge | 166 hours |

**ReqEff benchmark:** Values above 1.0 indicate efficient use (more LoC per premium request). Values below 0.2 indicate spend with minimal code output. Three users are below 0.1.

---

## 3. Pattern Distribution — 9-Checkpoint Arc

Across 9 checkpoints from April 20 to June 23, each developer's LoC trajectory was classified into one of six patterns.

| Pattern | Count | What It Means |
|---|---|---|
| Late Accelerator | 12 | Minimal early activity; significant uptick in CP7–CP9 |
| Steady Climber | 7 | Consistent week-over-week LoC growth throughout Q2 |
| Front-Loaded | 2 | High early LoC; flat or declining since mid-quarter |
| Mid-Period Stall | 10 | Active early/mid quarter; production slowed or stopped |
| Volatile | 3 | Alternating high/low output; no stable pattern |
| Flat Liner | 9 | Minimal LoC across all 9 checkpoints |

**Late Accelerator (12 users) is the largest single pattern**, indicating the team is still finding its rhythm with Copilot. This is structurally healthy — adoption is not plateauing — but the 10 Mid-Period Stall and 9 Flat Liner users represent meaningful under-realized value.

---

## 4. Top 5 Late Accelerators

These users showed the strongest positive momentum in the final two windows (CP7 → CP9, ~15 days).

| Rank | User | CP7 LoC | CP9 LoC | Delta | % Gain | Note |
|---|---|---|---|---|---|---|
| 1 | luisalvatierra | 4,800 | 12,080 | +7,280 | +152% | Strongest late acceleration on team |
| 2 | Prathmesh-Ranadive | 27,052 | 35,091 | +8,039 | +30% | Absolute LoC leader; premium concern |
| 3 | mshivarkar | 2,018 | 4,201 | +2,183 | +108% | Breakout from near-zero CP1–CP5 |
| 4 | giteshsawant | 50 | 1,369 | +1,319 | +2,638% | Entire output in last 2 windows |
| 5 | dsuraj25 | 510 | 1,169 | +659 | +129% | Flat 6 windows, then burst |

**Q3 Implication:** Late accelerators entering Q3 with momentum are the team's strongest candidates for sustained high production. luisalvatierra and mshivarkar in particular have broken through after long dormant periods — their Q3 trajectory is worth watching closely. giteshsawant and dsuraj25 need one more checkpoint to confirm the burst is durable rather than a one-time spike.

---

## 5. Top 6 Plateau / Stall Users (Final Window)

These users produced zero or near-zero new LoC in the final 11-day window (CP8 → CP9).

| User | Last Active LoC | Days Flat | Prior Pattern |
|---|---|---|---|
| mshnayderman | 27,539 (CP7/8/9) | 15+ days | Front-Loaded — high early; zero new LoC since |
| copilotshree | 5,013 (since CP5) | 36 days | Flat since CP5 — longest current plateau |
| rpawar-nice | 8,662 (effectively flat from CP1) | 64 days | Minimal LoC growth across entire quarter |
| Vyankatesh95 | 4,177 (since CP7) | 15 days | Mid-Period Stall |
| moadzughul | 3,409 (since CP7) | 15 days | Mid-Period Stall |
| Akale23 | — | 11+ days | Limited output throughout |

**Note on copilotshree and rpawar-nice:** Both score Tier A/B across frameworks due to exceptional Request Efficiency (ReqEff=14.8 and 9.9 respectively), not LoC volume. Their lean spend and high efficiency make them strong in the frameworks even though absolute output is modest. The 36-day plateau for copilotshree should be flagged for Q3 engagement.

---

## 6. Most Improved Over Q2 (Apr 20 → Jun 23)

These users showed the largest positive arc across the full 64-day program.

| Rank | User | CP1 LoC | CP9 LoC | Growth | Arc |
|---|---|---|---|---|---|
| 1 | luisalvatierra | 1,216 | 12,080 | +893% | Tier D (CP1) → Tier B/C (CP9); late but sustained |
| 2 | mshivarkar | ~0 | 4,201 | Breakout | Near-zero CP1–CP5; significant producer by CP9 |
| 3 | jayesh-rai | 1 | 2,712 | +271,100% | Slow start; consistent growth across Q2 |
| 4 | trunalgawade | 6 | 2,352 | +39,100% | Volatile pattern but cumulative progress |
| 5 | Shreedevi-nice | 38 | 1,886 | +4,858% | Strong growth arc; premium budget concern remains |

---

## 7. Budget Crisis Summary

### Critical Tier (>25,000 premium requests)

These five users collectively account for a disproportionate share of team premium spend with poor-to-moderate LoC output.

| User | Premium Requests | LoC Added | ReqEff | Status |
|---|---|---|---|---|
| tusharpatil166719 | 35,886 | ~2,200 | 0.06 | All-time team worst ratio. No output justifying spend. |
| Kranti-nice | 35,537 | — | — | Tripled in 11 days (from 11,979 at CP8). Fastest escalation on team. |
| nilesht-19 | 32,332 | 7,354 | 0.23 | Persistent crisis; unchanged since CP8 flag. |
| Prathmesh-Ranadive | 31,420 | 35,091 | ~1.1 | Only Critical user with strong LoC output. Watch, not Cold. |
| Shubhamfulzele28 | 29,049 | 1,043 | 0.04 | Near-zero output for all spend. Doubled from CP8. |

### Severe Tier (15,000–25,000 premium requests)

| User | Premium Requests | Notes |
|---|---|---|
| PradnyeshSalunke | 20,544 | Accelerating spend; CP8 flag not acted on. |
| amol-salunkhe | 20,170 | Consistent high spend; moderate output. |
| trunalgawade | 18,720 | Some LoC growth but ReqEff low. |
| mshivarkar | 17,029 | Late Accelerator — spend justified by LoC breakout. |
| sskalaskar | 16,897 | Moderate spend; efficiency needs review. |

**Total premium consumed by top 10 budget-risk users: ~319,000+ requests combined.**
**Three users individually exceed 30,000 premium requests** — a threshold that signals tool misuse rather than intensive legitimate use.

**Distinction:** Prathmesh-Ranadive and mshivarkar are the only high-spend users whose LoC output provides partial justification. All others in the Critical tier are spending without producing.

---

## 8. Coaching Effectiveness: Jun 12 Flags → Jun 23 Outcomes

Budget concerns were flagged at CP8 (June 12). The 11-day window to Jun 23 is the measure of whether those signals reached the team.

| User Flagged at CP8 | CP8 Premium | CP9 Premium | Change | Outcome |
|---|---|---|---|---|
| nilesht-19 | 30,437 | 32,332 | +1,895 | Did not respond. ReqEff unchanged. |
| trunalgawade | 16,265 | 18,720 | +2,455 | Did not respond. Continued same behavior. |
| PradnyeshSalunke | 15,719 | 20,544 | +4,825 | Worse. Spending accelerated. |
| Shubhamfulzele28 | 13,831 | 29,049 | +15,218 | Critical escalation. Spend doubled in 11 days. |
| Kranti-nice | 11,979 | 35,537 | +23,558 | Most extreme escalation. Tripled. |

**Coaching effectiveness: 0 of 5 flagged users improved on budget metrics in the 11-day window.**

This is not a data anomaly — it is a process gap. Flags generated at CP8 either did not reach developers, did not reach team leads, or reached them without a clear directive to change behavior. Before Q2 closes, the mechanism for converting analysis flags into manager action needs to be addressed. Generating a 10th checkpoint without fixing this loop will produce the same result.

---

## 9. Cross-Framework Tier Alignment

Frameworks agree when they assign the same tier from different measurement angles — a strong convergence signal. Disagreements reveal users whose performance looks different depending on how you measure.

| User | v1 Tier | v2 Tier | CRQC Tier | R+M Tier | Consensus |
|---|---|---|---|---|---|
| copilotshree | A | A | B | A | **A — strong consensus** |
| rpawar-nice | B | A | C | B | **B** (v2 upgrades based on workflow) |
| mshnayderman | B | B | C | B | **B** (CRQC is outlier) |
| mfield1 | C | B | C | C | **C/B split** |
| Vyankatesh95 | C | C | C | C | **C — full consensus** |
| Vitthal-Nice | C | C | C | C | **C — full consensus** |
| jayesh-rai | C | C | C | C | **C — full consensus** |
| moadzughul | C | C | C | C | **C — full consensus** |
| abhijeetk268 | C | C | A | B | **B** (CRQC significantly promotes) |
| Prathmesh-Ranadive | D | B | C | C+ | **C/B split** (v2 strong on workflow) |
| amol-salunkhe | D | D | C | D | **D** (CRQC slight upgrade) |
| luisalvatierra | D | D | C | C | **C/D split** |
| chris-haun | D | D | C | C | **C/D split** |
| nilesht-19 | E | E | C | E | **E — crisis confirmed across 3/4 frameworks** |
| Kranti-nice | E | E | C | E | **E — crisis confirmed across 3/4 frameworks** |
| tusharpatil166719 | E | E | C | E | **E — crisis confirmed across 3/4 frameworks** |

**Framework disagreement signals worth noting:**
- CRQC consistently promotes users one tier relative to v1/v2/R+M. This reflects CRQC's emphasis on PR quality metrics (merge rate, review depth) where some low-output users have clean PR histories.
- abhijeetk268 is the most notable CRQC outlier — Tier A in CRQC vs. C elsewhere. Suggests strong PR quality behaviors even at moderate LoC volume.
- Prathmesh-Ranadive's v2 Tier B (vs. D in v1) reflects the workflow-aware framework crediting agent and complex completion patterns, not just raw LoC.

---

## 10. Q3 Entry Readiness

### HOT — Strong momentum, ready for Q3 without intervention

| User | Rationale |
|---|---|
| copilotshree | ReqEff=14.8. Leanest spender on team. Tier A consensus. Address 36-day plateau going into Q3. |
| rpawar-nice | ReqEff=9.9. Agent-first behavior. Low spend. High framework scores. |
| mshnayderman | ReqEff=5.1. Strong total LoC (27,539). Flag: zero new LoC for 15+ days entering Q3. |

### WARM — Decent output; specific coaching will accelerate Q3 performance

| User | Rationale |
|---|---|
| luisalvatierra | Strongest acceleration (+152% final window). Needs premium spend review (9.5K). |
| Prathmesh-Ranadive | Exceptional LoC velocity (35,091). Must address 31K premium spend in Q3 — only WATCH, not Cold, due to output. |
| mfield1 | Solid output, reasonable spend, but flat final 11 days. |
| mshivarkar | Late Accelerator breakout; 17K premium spend needs monitoring in Q3. |
| jayesh-rai | Consistent Tier C consensus; lean spend; reliable output. |
| Vitthal-Nice | Tier C consensus; moderate steady output. |
| abhijeetk268 | Strong PR quality (CRQC Tier A); moderate LoC. |
| moadzughul | Tier C consensus; flat final window needs engagement. |
| giteshsawant | Strong late burst; needs one more CP to confirm durability. |
| dsuraj25 | Late burst; same caveat as giteshsawant. |
| Shreedevi-nice | Strong growth arc; premium spend needs watch. |
| trunalgawade | Volatile but cumulative progress; premium intervention needed. |
| PradnyeshSalunke | Moderate LoC; premium spend escalating — borderline Warm/Cold. |

### COLD — Significant intervention required before or at Q3 start

| User | Rationale |
|---|---|
| tusharpatil166719 | ReqEff=0.06. All-time team worst. 35,886 premium, 2,200 LoC. Immediate review. |
| Kranti-nice | Tripled premium in 11 days to 35,537. No proportional output. Immediate review. |
| nilesht-19 | Persistent crisis. 0/5 coaching response. 32,332 premium. Escalate to manager. |
| Shubhamfulzele28 | ReqEff=0.04. Spend doubled at CP9. Near-zero output. |
| ssnikam | Zero Copilot usage (see Section 12). 55 PRs, 49 merged — highest-leverage unconverted user. |
| copilotshree | HOT on efficiency but 36-day zero-output plateau is a Q3 risk — borderline HOT/WARM. |
| amol-salunkhe | Low efficiency across all frameworks. D consensus. |
| Flat Liner cohort | 9 users with minimal LoC across all 9 checkpoints — evaluate whether Copilot is being used at all. |

---

## 11. ssnikam — Strategic Zero-AI Opportunity

ssnikam does not have a Copilot license and has produced **zero AI-assisted code** across the entire 64-day program.

Despite this, ssnikam has:
- **55 PRs submitted**, 49 merged (89% merge rate)
- One of the highest PR volumes on the team
- A demonstrated, high-cadence development workflow

**Why this matters:** ssnikam is the clearest single-user productivity multiplier available. A developer already operating at high PR velocity, given an AI tool that can accelerate code generation and review, is the profile most likely to produce outsized LoC gains.

**Action before Q2 close:** Assign Copilot license to ssnikam. Pair with a Late Accelerator (e.g., mshivarkar) for a single onboarding session. Measure impact at CP1 of Q3.

---

## 12. Top 3 Actions Before Q2 Close (by June 30)

### Action 1 — Emergency Budget Intervention for 3 Critical Users

**Who:** tusharpatil166719, Kranti-nice, Shubhamfulzele28 (nilesht-19 as secondary)
**What:** Direct manager conversation. Review Copilot usage logs to determine whether spend reflects repeated prompt retries, tool misconfiguration, or exploratory (non-production) usage patterns. Provide concrete guidance: premium requests should correlate with LoC output. If a user cannot connect their usage to code produced, their workflow needs to be reset before Q3.
**Why now:** All three doubled or tripled spend in the 11 days after CP8 flagged them. Q3 starts July 1. If no intervention happens before then, the same pattern continues with no quarterly reset signal.

### Action 2 — Close the Coaching Feedback Loop

**Who:** Team leads / engineering managers for the WFM Integrations team
**What:** Establish a direct path from analysis flag → manager inbox → developer conversation. The CP8 → CP9 data shows that analysis flags alone do not change behavior. At minimum, for Q3 CP1, confirm that CP9 budget findings were reviewed by the relevant managers before June 30.
**Why now:** 0 of 5 flagged users improved in 11 days. This is a process gap, not a data gap. Generating a Q3 analysis without fixing the feedback loop will produce the same zero-response result.

### Action 3 — Assign Copilot to ssnikam Before Q2 Closes

**Who:** ssnikam
**What:** Provision Copilot license. Brief onboarding session (1 hour). Pair with an experienced user for initial IDE setup.
**Why now:** 55 PRs in 64 days without AI assistance. Q3 Day 1 with Copilot active gives you a clean baseline measurement. Waiting until Q3 mid-quarter loses the clean start-of-quarter data point.

---

## 13. Q3 Watch List

These users warrant close attention at Q3 CP1 (target: ~2 weeks into Q3).

| User | Watch Reason | Signal to Look For |
|---|---|---|
| Kranti-nice | Tripled premium in 11 days; zero response to flag | Any deceleration in premium; any LoC output |
| Shubhamfulzele28 | Doubled spend at CP9; ReqEff=0.04 | Premium drop; LoC increase |
| tusharpatil166719 | All-time worst ReqEff; no output for spend | Manager confirmation of workflow review |
| luisalvatierra | Strongest accelerator — can it hold? | LoC growth continuing into Q3 |
| giteshsawant | Entire output in last 2 windows — durable or spike? | Continued production in first Q3 window |
| dsuraj25 | Same as giteshsawant | Continued production |
| mshivarkar | Breakout from near-zero; 17K premium | LoC continuing + premium stabilizing |
| ssnikam | Zero Copilot today; provisioning by Jul 1 | First LoC with Copilot |
| mshnayderman | Zero new LoC for 15+ days entering Q3 | Any resumed production |
| copilotshree | 36-day plateau entering Q3 | Any resumed production |
| PradnyeshSalunke | Spend accelerating with moderate output | Premium deceleration |
| Prathmesh-Ranadive | Only Critical-tier user with strong output | Premium/LoC ratio improving |

---

## Appendix — Framework Reference

| Framework | Primary Signal | Tier Logic |
|---|---|---|
| v1 Standard | LoC Added + Premium Efficiency | Raw output and spend efficiency |
| v2 Workflow-Aware | Agent usage, multi-file completions, PR workflow integration | Behavioral sophistication of Copilot use |
| Role+Momentum | Trajectory over checkpoints, rate of change | Is the user accelerating, stalling, or declining? |
| CRQC | Code Review Quality Contribution | PR merge rate, review participation, code quality signals |

All four frameworks were applied at each of the 9 checkpoints. This summary synthesizes consensus findings. Where frameworks disagree, the disagreement is noted and the most credible interpretation given context is used.

---

*Analysis generated: June 23, 2026 | CP9 of 9 | Q2 closes June 30, 2026*
*Next checkpoint recommended: Q3 CP1 — target July 7–10, 2026*
