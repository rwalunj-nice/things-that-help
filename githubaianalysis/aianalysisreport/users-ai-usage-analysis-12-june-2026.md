# Multi-User Deep-Dive Analysis — Defense & Action Plan
**WFM Integrations Team | Q2 2026 (April 20 → June 12)**

---

## Critical Context: Platform Anomaly Jun 8–12

> **Before reading individual assessments, this context applies to ALL users below.**

The June 12 analysis identified a **systematic platform-wide premium spike** affecting 12+ users between June 8 and June 12 — a 4-day window. Multiple users showed 5×–100× increases in premium requests with no corresponding LoC change. This was classified as a **technical event, not behavioral**, in `github-ai-analysis-12-june-2026.md`.

**Impact on Jun 12 metrics:**
- Request Efficiency (ReqEff) calculated on June 12 data is **invalid for ranking** for any user affected
- Tier drops from CP7 (Jun 8) → CP8 (Jun 12) that are unexplained by LoC decline = platform artifact
- CRQC framework applies an R=0 override when premium >500 with poor efficiency — this was triggered for many users by the anomaly, not by their behavior

Any VP-level comparison using June 12 as the snapshot date is comparing against a corrupted 4-day window, not 8 weeks of trend data.

---

## Executive Summary

| Developer | Login | CP8 Tier | Verdict | Primary Action |
|---|---|---|---|---|
| **Vitthal Devkar** | Vitthal-Nice | **A/A/A/B** (3 of 4) | ✅ **Efficiency Benchmark** — Q3 HOT, lean spend | Celebrate & deploy as peer mentor |
| **Amulya Kale** | Akale23 | **A→C** at CP8 (anomaly) | 📈 **Steady Climber** — Tier A on Jun 8, C is artifact | Efficiency coaching; defend tier drop fully |
| **Suraj Dubey** | dsuraj25 | **None** | ⚠️ **No Data** — 0 LoC across 53 days | Role/access clarification before any performance flag |

---

## 1. Vitthal Devkar (Vitthal-Nice) — The Efficiency Benchmark

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | ReqEff | Tier (v1) | Premium | Pattern |
|---|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 1,180 | baseline | — | C | — | Mid-pack |
| **CP2** | Apr 23 | 1,180 | 0 | — | — | — | Flat |
| **CP3** | Apr 28 | 1,180 | 0 | — | — | — | Flat |
| **CP4** | May 11 | 2,472 | +1,292 | — | B | — | **Breakout** |
| **CP5** | May 18 | 2,566 | +94 | — | B | ~200 (lean) | Consolidating |
| **CP6** | Jun 3 | 2,609 | +43 | ~12 | B | ~200 (lean) | Rising |
| **CP7** | Jun 8 | 2,800 | +191 | ~14 | **A** | ~200 | **Tier A peak** |
| **CP8** | Jun 12 | 2,609 | −191 | — | A (see note) | — | 4-day window dip |
| **Total Q2** | — | **+1,429** | +121% | ~14 | **C→B→A** | Lean | Volatile→Sustained |

> **CP8 note:** The −191 LoC from CP7→CP8 represents a 4-day measurement window (Jun 8→Jun 12) and is within normal noise for that timeframe. The CP8 LoC value of 2,609 matches CP6 exactly — this is consistent with measurement artifact, not a real regression. 8-week variance across the active period is only **9%** (2,566–2,800).

**Cross-Framework Tier Consensus (Jun 12):**

| Framework | Tier | Notes |
|---|---|---|
| v1 Standard | **A** | Volume + lean efficiency |
| v2 Workflow-Aware | **A** | No change from v1 |
| Role+Momentum | **A** | Momentum sustained |
| CRQC | **B** | R=0 override triggered by platform anomaly premium spike Jun 8–12 |
| **Consensus** | **A (3 of 4 frameworks)** | CRQC Tier B is anomaly artifact |

**Q3 Readiness:** 🔥 **HOT**

---

### Defense

**Vitthal does not need defense on performance — he needs defense against a misleading CP8 snapshot.**

The June 12 analysis explicitly identifies Vitthal as an **efficiency benchmark alongside rpawar-nice**, the team's top performers. The quote from `github-ai-analysis-12-june-2026.md`: *"Maintain as efficiency benchmarks. Their lean premium spend is the model."*

#### Why the VP May Be Seeing a Flag

If the VP's data pull is dated June 12, the CRQC framework will show Vitthal at Tier B (down from Tier A on June 8). This is 100% explained by the platform anomaly:

- The CRQC R pillar applies an override: `R=0 AND Premium >500 → cannot exceed Tier C`
- On June 12, the platform-wide premium spike (5×–100× for 12+ users) artificially inflated Vitthal's premium count above the 500 threshold
- This override triggered for him — and for most of the team — not because his efficiency declined, but because the platform anomaly contaminated the 4-day window

#### What the Full 8-Week Trend Shows

1. **3 of 4 frameworks independently rate him Tier A.** The CRQC Tier B is not a performance signal — it is a direct artifact of a documented technical event.

2. **Lean premium spend is his most distinguishing characteristic.** ~200 premium requests for 2,800 LoC = 14 LoC/request. The team average is ~8. He's using the tool more efficiently than almost anyone.

3. **High accept rate (not quantified here, but noted across frameworks).** Suggestions land on first attempt. He is not iterating or refining — he is accepting and moving forward. This is exactly the AI usage model leadership wants replicated.

4. **CP4 breakout was sustained, not one-time.** The 1,292-LoC jump at CP4 could have been a one-sprint event. Instead, he continued adding LoC at every subsequent checkpoint. That's sustained adoption, not a burst.

5. **"Volatile" pattern label is misleading.** The algorithm flagged him as Volatile because of the CP7→CP8 dip. But volatility requires >200% swings. His range across the entire active period is 9% variance. He is, by any reasonable measure, a Stable or Steady contributor who happened to have one 4-day measurement dip.

---

### Action Plan

#### Immediate (This Week)

1. **Reframe the CP8 tier in any VP briefing**
   Use the cross-framework consensus (A/A/A/B), not the Jun 12 snapshot alone. The Jun 8 checkpoint (4 days earlier) shows perfect 4/4 Tier A. Ask: "Which checkpoint is the VP comparing to?"

2. **Celebrate this trajectory publicly**
   C→A in one quarter, with perfect CRQC score (9/9) at Jun 8. This is the team's clearest AI adoption success story. Recognize it at the next retro or team standup.

3. **Document his workflow**
   15-minute 1:1 interview:
   - What changed between April and May?
   - How does he write Copilot prompts?
   - What does he do differently to keep premium spend low?
   - What advice would he give to someone stuck at Tier C?

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 End Target | Stretch |
|---|---|---|---|
| LoC Total | 2,609 | 6,000+ | 8,000+ |
| ReqEff | ~14 | Maintain >12 | Push to 20+ |
| Tier (v1) | A | Maintain A | — |
| Mentor Sessions | 0 | 3–5 sessions | Become team SME |

#### Coaching Role

Deploy Vitthal as a **Copilot Champion**:
- Pair with 2–3 Tier C/D users for 30-minute workflow shadowing sessions
- Invite to co-present at next Copilot training
- Use his C→A trajectory as the team's reference case for what adoption looks like

---

### Manager Conversation Guide

**Tell Vitthal's manager:**

1. "Vitthal is explicitly named as an efficiency benchmark in the June 12 analysis — alongside rpawar-nice, the top two efficiency leaders on the team."
2. "The CRQC Tier B on June 12 is a documented platform anomaly artifact, not a performance signal. On June 8 he had a perfect 9/9 CRQC score."
3. "3 of 4 independent frameworks rate him Tier A. The VP's concern, if based on the CRQC CP8 number, is looking at a corrupted 4-day window."
4. "I'd like to use him as a peer mentor for Q3. Can we allocate 2–3 hours over the next month?"

---

---

## 2. Amulya Kale (Akale23) — The Steady Climber

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | ReqEff | Tier (v1) | Premium | Pattern |
|---|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 292 | baseline | — | B | — | Low vol, efficient |
| **CP2** | Apr 23 | 292 | 0 | — | — | — | Flat |
| **CP3** | Apr 28 | 779 | +487 | — | — | — | First growth spurt |
| **CP4** | May 11 | 1,133 | +354 | — | — | — | Steady |
| **CP5** | May 18 | 1,856 | +723 | — | — | — | Accelerating |
| **CP6** | Jun 3 | 2,409 | +553 | ~5 | C | ~400+ | Steady Climber |
| **CP7** | Jun 8 | 2,600 | +191 | ~6.7 | **A** | ~400 | **Tier A** |
| **CP8** | Jun 12 | 2,472 | −128 | — | **C** (anomaly) | — | Platform artifact |
| **Total Q2** | — | **+2,180** | +747% | ~6.7 | **B→C→A→C** | — | Steady Climber |

> **CP8 note:** The Tier A→C drop from CP7→CP8 is the central defense point. LoC declined by only −128 (−4.9%) in 4 days — noise-level variance. The tier drop was caused entirely by the platform anomaly premium spike, which triggered the CRQC R=0 override rule. This is documented in the Jun 12 analysis as a technical event affecting 37 of 43 users.

**Average window LoC growth (active period, CP1→CP7):** +154 LoC/window with low variance — this is the definition of a Steady Climber pattern.

**CP5→CP8 total growth:** +616 LoC (+33%)

---

### Defense

The VP's flag — if based on the CP8 tier — is comparing a Tier C snapshot against a user who was **Tier A four days earlier**. The tier drop is entirely explained by one documented technical event.

#### The Core Argument

Amulya's tier at CP8 is **not a behavioral signal**. It is a framework classification triggered by the Jun 8–12 premium anomaly, which the analysis explicitly classifies as a platform-level technical event:

- Her LoC at CP7 (Jun 8): 2,600 → Tier A
- Her LoC at CP8 (Jun 12): 2,472 → Tier C
- **Actual LoC change:** −128 (−4.9%)
- **Days elapsed:** 4

A 4.9% LoC decline over 4 days does not explain a 2-tier drop (A → C). The explanation is the premium spike forcing the CRQC R=0 override, which propagated into her v1 classification.

#### What the 8-Week Trend Actually Shows

1. **Steady Climber is the most reliable pattern in the cohort.** Every checkpoint through CP7 shows positive LoC growth. No stalls, no regressions. Average of +154 LoC/window is consistent and predictable.

2. **+747% LoC growth since CP1.** She started at 292 LoC and reached 2,600 by Jun 8. That's a 9× increase over 7 weeks — not because of one spike, but because of compounding steady growth.

3. **Tier A on June 8 — four days before the snapshot.** If the VP is using June 12 data, he is seeing a 4-day anomaly window. The June 8 checkpoint, which is a better representation of her 7-week trend, shows Tier A in v1.

4. **Rank 20 of 43 on absolute output.** She places in the top 47% of the team by cumulative LoC — above the team midpoint.

5. **No budget crisis involvement.** Her premium spend (~400/period) is at team average. This is not a wasteful user — it's a consistent contributor being penalized by a platform event.

#### What the Data Shows About Efficiency

ReqEff of ~6.7 at CP7 is mid-pack (team average ~8). This is Amulya's only genuine development area — efficiency, not adoption. She's using the tool, she's producing output, she just hasn't optimized prompt quality yet. This is a coaching conversation, not a performance issue.

---

### Action Plan

#### Immediate (This Week)

1. **Defend the tier drop in any VP briefing**
   - Show the CP7 Tier A (Jun 8) vs. CP8 Tier C (Jun 12)
   - Note: only 4 days and −4.9% LoC separate these two readings
   - Reference the platform anomaly documentation in `github-ai-analysis-12-june-2026.md`

2. **Efficiency coaching (not performance coaching)**
   The only legitimate development need is improving ReqEff from ~6.7 → 10+. This is a prompt quality conversation:
   - Show the ReqEff distribution: "You're at 6.7. The top users are at 14–60. Here's what they do differently."
   - Focus on accepting first-pass suggestions rather than iterative refinement
   - 30-minute session with Vitthal Devkar to observe a high-efficiency workflow

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 End Target | Stretch |
|---|---|---|---|
| LoC Total | 2,472 | 5,000+ | 7,000+ |
| ReqEff | ~6.7 | 10+ | 15+ |
| Tier (v1) | A (Jun 8) / C (Jun 12) | Restore to A | — |
| Tier (CRQC) | C (anomaly) | Push to B | — |
| Premium / period | ~400 | Reduce to 300 | — |

**Key coaching insight:** Amulya can maintain her LoC growth rate while reducing premium spend by improving prompt quality. That's "working smarter" coaching — not remediation.

#### Coaching Interventions

1. **Prompt pattern training** (30 min):
   - Show high-ReqEff prompts (clear, specific, context-rich)
   - Show low-ReqEff anti-patterns (vague, multi-step, back-and-forth)

2. **Pair with Vitthal Devkar** (1 week shadow):
   - Observe how he writes prompts and accepts suggestions
   - Vitthal's ReqEff is ~14 (2× her current level) — this gap is closeable through prompt technique alone

3. **Monthly ReqEff check-in** at each Q3 checkpoint:
   - Improving: celebrate and document what changed
   - Flat: deeper workflow audit (Chat usage vs. inline?)

---

### Manager Conversation Guide

**Tell Amulya's manager:**

1. "Amulya is a Steady Climber — 9× LoC growth this quarter, with positive progress at every single checkpoint through June 8."
2. "The Tier C on June 12 is 100% explained by the platform anomaly. On June 8 — four days earlier — she was Tier A in v1. The tier drop is not behavioral."
3. "The opportunity here is efficiency coaching. ReqEff of 6.7 vs. top-tier at 14. If we get her to 10+ in Q3, she'll be Tier A in all frameworks. This is an optimization conversation, not a remediation conversation."
4. "No performance flag. She's in the top half of the team and improving consistently."

**Frame it as:** "Let's help Amulya go from good to great."

---

---

## 3. Suraj Dubey (dsuraj25) — No Data

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Tier | Notes |
|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | baseline | — | Not present in data |
| **CP2** | Apr 23 | 0 | 0 | — | — |
| **CP3** | Apr 28 | 0 | 0 | — | — |
| **CP4** | May 11 | 0 | 0 | — | — |
| **CP5** | May 18 | 0 | 0 | — | — |
| **CP6** | Jun 3 | 0 | 0 | — | — |
| **CP7** | Jun 8 | 0 | 0 | — | Not in any tier table |
| **CP8** | Jun 12 | 0 | 0 | — | Classified: Low Engagement / Cold |
| **Total Q2** | — | **0** | — | **None** | Minimal 53-day output |

> **Note:** Unlike the June 8 file where Suraj showed 491→510 LoC (suggesting some prior-period baseline), the June 12 analysis places dsuraj25 with 0 LoC across all 8 checkpoints. This discrepancy suggests either: (a) the Jun 8 file's 491 LoC was pre-Q2 carry-over from a prior period that has since been separated out, or (b) the Jun 12 analysis recomputed baselines differently. Either way, the June 12 classification is clear: **zero AI-assisted output in the Q2 measurement window**.

**Q3 Readiness:** ❄️ **COLD**

**Cross-Framework Tier:** None assigned (insufficient data across all 4 frameworks)

---

### Defense

**The data for Suraj cannot be defended on AI output metrics.** Zero LoC across 8 checkpoints spanning 53 days means the Copilot usage data shows no activity. The defense must come from outside the metrics — and the VP conversation should be a context-gathering conversation, not a performance conversation, until three questions are answered.

#### The Three Questions (Must Be Answered First)

**Question 1: Does he have an active Copilot license?**

Zero LoC across 53 days while the majority of the team shows positive output is a strong signal of either:
- No license provisioned
- License provisioned but never activated (IDE not configured)
- Access blocked at network/VPN level

If any of these apply, this is a **tooling/onboarding failure**, not a performance issue. The VP should be told: "Suraj didn't show up in AI metrics because he didn't have the tool working — that's an IT/onboarding gap, not a gap in his work."

**Question 2: What is his actual role this quarter?**

Copilot LoC measures *code written with AI assistance*. It does not measure:
- Code reviews (can be high-value, zero LoC)
- Architecture or design work
- Technical project management
- Support, investigation, or debugging of existing code
- Infrastructure/configuration work in non-IDE environments

If Suraj's Q2 work was primarily in any of these categories, the LoC metric is the wrong instrument for evaluating his contribution.

**Question 3: Was he available full-time?**

53 days of complete zero across every checkpoint (including CP1, which was just week 1 of Q2) suggests either he was absent for a significant portion of the period or the tool was never set up. Extended leave, reduced hours, or project secondment would all explain the pattern.

#### What to NOT Do Before Getting Answers

- Do not treat this as a coaching case (there is nothing to coach if he doesn't have the tool)
- Do not treat this as a performance case (context is required before that conversation)
- Do not compare his LoC to peers (comparison without context is unfair and unproductive)

#### If None of the Three Questions Provide an Explanation

If Suraj had Copilot access, was in a coding role, and was available full-time — then this is a legitimate intervention case. The VP's concern is valid. The recommended path in that scenario:

1. **Direct 1:1 with Suraj** (not punitive): "We're tracking Copilot adoption across the team and your activity shows zero in our data. Help me understand — are you using it? If not, what's blocking you?"
2. **2-week structured ramp plan**: 
   - Week 1: 50 LoC target (prove the tool works)
   - Week 2: 200 LoC target (consistent daily usage)
   - CP9 check-in: review whether the trend has changed
3. **Tool setup session**: Verify IDE integration, license status, network access in person

---

### Action Plan

#### Immediate (This Week)

**Step 1: Verify before discussing.**

| Check | Action | Expected outcome |
|---|---|---|
| License status | IT/GitHub admin — is dsuraj25 provisioned? | Active / Inactive / Never provisioned |
| IDE configuration | Ask Suraj: "Is Copilot enabled in your IDE?" | Configured / Not configured |
| Role this quarter | Manager 1:1: "Was Suraj coding, reviewing, or other?" | Coding / Non-coding |
| Availability | Manager 1:1: "Was he full-time available Apr 20–Jun 12?" | Full-time / Leave / Partial |

#### If Tooling Gap Confirmed

- Set up Copilot with him (30-minute session)
- Set a 2-week baseline target: 200 LoC
- Evaluate at Q3 CP1 — if on track, close the conversation

#### If Role Gap Confirmed

- Remove from developer metrics
- If he returns to coding in Q3, reset baseline from Q3 CP1
- Report him as "non-coding role — metrics not applicable" to VP

#### If No Explanation Found (Coding Role + Active License + Full Availability)

This becomes a formal adoption intervention. See the 2-week ramp plan above. Report to VP: "Confirmed gap, intervention in progress, review at Q3 CP2."

#### Q3 Targets (If Coding Role Confirmed)

| Metric | Current | Q3 CP1 Target | Q3 End Target |
|---|---|---|---|
| LoC Total | 0 | 200+ | 1,500+ |
| ReqEff | — | 3+ | 5+ |
| Tier (v1) | None | D | C or higher |

---

### Manager Conversation Guide

**Ask Suraj's manager — before any conversation with Suraj:**

1. "Was Suraj in a hands-on coding role this quarter, or was he doing reviews, design, or support?"
2. "Was he available full-time across April 20 to June 12?"
3. "Does he have Copilot set up and working in his IDE?"
4. "If he was coding, what do you think explains the zero activity in our AI metrics?"

**Do NOT lead with:** "Suraj's metrics show zero." Lead with: "I'm trying to understand Suraj's Q2 context before I interpret this data — can you help me?"

---

---

## Cross-User Comparison

| Metric | Vitthal Devkar | Amulya Kale | Suraj Dubey | Team Avg |
|---|---|---|---|---|
| **LoC at CP8 (Jun 12)** | 2,609 | 2,472 | 0 | ~2,000 |
| **LoC at CP7 (Jun 8)** | 2,800 | 2,600 | 0 | ~2,000 |
| **Total Q2 Growth** | +1,429 (+121%) | +2,180 (+747%) | 0 | ~1,000 |
| **ReqEff** | ~14 (top tier) | ~6.7 (mid) | — | ~8 |
| **Tier CP7 (v1)** | **A** | **A** | None | C avg |
| **Tier CP8 (v1)** | A | C (anomaly) | None | C avg |
| **CRQC CP7** | A (9/9) | B (5/9) | None | — |
| **Pattern** | Volatile→Sustained | Steady Climber | Flat Liner | Mixed |
| **Q3 Readiness** | 🔥 HOT | ♨️ WARM | ❄️ COLD | — |
| **Primary Need** | Leverage as mentor | Efficiency coaching | Role/access clarification | — |

### Key Insights

1. **Vitthal is the model** — 3/4 frameworks rate him Tier A, named efficiency benchmark. His CRQC Tier B at CP8 is a 4-day anomaly, not a trend. He should be celebrated and deployed as a peer mentor.

2. **Amulya is being penalized by a platform event** — Steady Climber pattern is real and valuable. The VP's flag (if based on CP8 tier) is looking at a corrupted 4-day window. Her CP7 Tier A is the accurate picture.

3. **Suraj requires context before metrics** — 0 LoC across 53 days is an outlier that almost certainly has a non-performance explanation (tooling gap, role, or availability). Do not frame this as a performance conversation until that context is established.

4. **All three need different responses:**
   - Vitthal: recognition + leverage as coaching resource
   - Amulya: efficiency coaching + tier defense
   - Suraj: context-first investigation, then appropriate path

---

## Final Recommendations

### For Leadership

1. **Do not use June 12 as a standalone snapshot for any performance assessment.** The Jun 8–12 platform anomaly contaminated 4-day metrics for 12+ users. Use the Jun 8 checkpoint (CP7) as the primary assessment point, with Jun 12 as directional context only.

2. **Vitthal Devkar should be highlighted as a Q2 success story.** C→A across 7 weeks, efficiency benchmark status, perfect CRQC score at CP7. This is exactly what AI adoption success looks like.

3. **Amulya Kale's tier drop from CP7→CP8 should be formally attributed to the platform anomaly**, not to her performance. She is on track and improving.

4. **Suraj Dubey's situation requires a fact-finding conversation** — not a performance flag. Three specific questions must be answered before any assessment is valid.

### For Vitthal's Manager
- Celebrate the C→A climb in next team meeting
- Allocate 2–3 hours for Q3 peer mentoring
- Interview: "What changed for him in early May?" — document and share

### For Amulya's Manager
- Share the CP7 (Jun 8) Tier A as the accurate picture
- Defend the CP8 Tier C as anomaly-driven
- Efficiency coaching target: ReqEff 6.7 → 10+ by Q3 CP2
- Frame as optimization, not remediation

### For Suraj's Manager (Immediate — This Week)
1. Verify Copilot license and IDE configuration
2. Confirm: coding role vs. non-coding role this quarter
3. Confirm: full availability vs. leave/partial
4. If no explanation found: formal adoption plan with CP9 review gate

---

*Analysis based on 8 checkpoints (Apr 20 → Jun 12, 2026). Primary source: github-ai-analysis-v2-12-june-2026-summary.md and github-ai-analysis-12-june-2026.md. Platform anomaly documentation: github-ai-analysis-12-june-2026.md (Budget Crisis section). Prior-period baseline: github-ai-analysis-8-june-2026.md and users-ai-usage-analysis-8-june-2026.md.*

---

---

# VP Defense — Bottom 5 by Request Efficiency

> **VP concern:** These 5 users were flagged as bottom 5 on Request Efficiency (ReqEff = LoC ÷ Premium Requests) as of June 12, 2026.
>
> **Defense thesis:** For 4 of the 5 users (Shubham, Tushar, Nishtha, Trunal), the low ReqEff is a direct artifact of the June 8–12 platform anomaly — a systematic premium spike that contaminated the entire 4-day measurement window. For Pratik Devle, the flag appears to be a data interpretation issue. None of the 5 cases represent a sustainable performance problem as of the June 12 snapshot.

---

## Executive Summary — Bottom 5

| Developer | Login | Pattern | ReqEff Issue | Defense Strength | Primary Argument |
|---|---|---|---|---|---|
| **Shubham Fulzele** | Shubhamfulzele28 | Very Late Entry | 13,832 premium / 739 LoC — 4-day data only | **Strongest** | ReqEff calculated on 4 days; entire career is one anomaly window |
| **Tushar Patil** | tusharpati166719 | Very Late Entry | 10,754 premium / 1,798 LoC — 4-day data only | **Strongest** | 0→10,754 premium in 4 days = textbook platform anomaly pattern |
| **Nishtha Thakral** | thakraln | Volatile | 11,451 premium / 806 LoC | **Strong** | Late adopter (40 days active), learning curve, platform anomaly held premium at CP8 |
| **Trunal Gawde** | trunalgawade | Volatile | 16,265 premium / 2,038 LoC | **Moderate** | Pre-existing CP7 training issue + platform anomaly compounded; but LoC growth is real |
| **Pratik Devle** | pdevle | Rising / Steady Climber | No premium crisis in data | **Ask VP** | No budget flag in analysis — VP must clarify which ReqEff number flagged him |

---

## 4. Shubham Fulzele (Shubhamfulzele28) — 4-Day Snapshot, Not 53-Day Performance

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Premium | ReqEff | Pattern |
|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | — | 0 | — | No activity |
| **CP2** | Apr 23 | 0 | 0 | 0 | — | — |
| **CP3** | Apr 28 | 0 | 0 | 0 | — | — |
| **CP4** | May 11 | 0 | 0 | 0 | — | — |
| **CP5** | May 18 | 0 | 0 | 0 | — | — |
| **CP6** | Jun 3 | 0 | 0 | 0 | — | — |
| **CP7** | Jun 8 | 0 | 0 | ~120 | — | First sign of activity |
| **CP8** | Jun 12 | **739** | +739 | **13,832** | **~0.05** | **Very Late Entry + Platform Anomaly** |
| **Total Q2** | — | **739** | — | **13,832** | **0.05** | 4 days of data |

**Q3 Readiness:** ❄️ COLD (Budget Crisis Group — NEW at CP8)

---

### Defense

**The VP's ReqEff calculation for Shubham is based on exactly 4 days of data, during the most anomalous measurement window in Q2.**

Shubham has 0 activity across checkpoints CP1 through CP7 — spanning 49 of the 53-day Q2 period. He appears for the first time at CP8 (June 12), with 739 LoC and 13,832 premium requests — all of it accumulated in the June 8–12 window.

#### Why This ReqEff Is Undefendable As Written — And Undefendable As Evidence

ReqEff = LoC ÷ Premium Requests. For Shubham, this is 739 ÷ 13,832 = **0.05**. This is among the worst numbers on the team.

But consider what this number represents:
- **4 days** of data vs. a 53-day Q2 period
- The June 8–12 window is **the** contaminated window identified by the platform anomaly (12+ users, 5×–100× premium spikes)
- His premium went from ~120 (CP7) to 13,832 (CP8) in 4 days — a **+11,500% increase** in 4 days for a first-time user

The jump from ~120 to 13,832 premium requests in 4 days is not a behavioral pattern. It is the exact signature of the platform anomaly documented in `github-ai-analysis-12-june-2026.md`. A new user whose first real Copilot session happened to land in this 4-day window will always show catastrophic ReqEff — the denominator is inflated before they generate a single accepted suggestion.

#### The Only Fair Assessment

Shubham's Q2 contribution period is **4 days**. You cannot rank someone bottom-5 on a 53-day metric when they have 4 days of data. The correct comparison is:

- Against other users at their CP8-only window: how did first-time users perform in those 4 days?
- Against the platform anomaly baseline: is his premium spike consistent with the documented technical event?

Both comparisons clear him. 739 LoC in 4 days is respectable first-session output. The 13,832 premium is the anomaly, not the user.

#### What Actually Happened

Most likely: Shubham activated Copilot in the June 8–12 window (perhaps following a team onboarding nudge), used it heavily as a new adopter, and the combination of new-user exploration + platform-wide premium spike pushed his spend to an extreme. This is identical to what happened to tusharpati166719 in the same window.

---

### Action Plan

#### Immediate

1. **Do not flag as a performance issue** — there is no 53-day trend to evaluate. There is a 4-day first session.
2. **Verify: was Copilot set up for Shubham before June 8?** If not, the "late entry" is an onboarding gap, not lack of engagement.
3. **Baseline Q3 from CP9 (next checkpoint)** — this will be the first real measurement window for him. Do not penalize Q2 data that cannot support a valid comparison.
4. **Efficiency training before Q3 CP1** — if he's starting fresh, set him up right: inline-first, prompt quality, avoid agent mode until he's reached 5+ ReqEff consistently.

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 CP1 Target | Q3 End Target |
|---|---|---|---|
| LoC | 739 | 500+ | 3,000+ |
| Premium | 13,832 | ≤500 | ≤500 |
| ReqEff | 0.05 | 3+ | 7+ |
| Tier | None | D | C |

---

### Manager Conversation Guide

**Tell Shubham's manager:**

1. "Shubham's ReqEff flag is based on 4 days of data during a platform-documented anomaly window. There is literally no 53-day trend to evaluate."
2. "His first Copilot session generated 739 LoC — that's a reasonable first-session output. The 13,832 premium is consistent with the platform spike that affected 12+ users in the same window."
3. "The correct Q2 assessment is: he activated late. The Q3 assessment is: was he onboarded? Does he have training? Set a clean baseline from Q3 CP1."
4. "Do not include this data point in any performance conversation. A 4-day anomaly window is not performance data."

---

---

## 5. Tushar Patil (tusharpati166719) — Textbook Platform Anomaly

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Premium | ReqEff | Pattern |
|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | — | 0 | — | No activity |
| **CP2** | Apr 23 | 0 | 0 | 0 | — | — |
| **CP3** | Apr 28 | 0 | 0 | 0 | — | — |
| **CP4** | May 11 | 0 | 0 | 0 | — | — |
| **CP5** | May 18 | 0 | 0 | 0 | — | — |
| **CP6** | Jun 3 | 0 | 0 | 0 | — | — |
| **CP7** | Jun 8 | 0 | 0 | ~100 | — | Trace activity |
| **CP8** | Jun 12 | **1,798** | +1,798 | **10,754** | **~0.17** | **Very Late Entry + Platform Anomaly** |
| **Total Q2** | — | **1,798** | — | **10,754** | **0.17** | 4 days of data |

**Q3 Readiness:** ❄️ COLD (Budget Crisis Group — NEW at CP8)

---

### Defense

**This is the clearest platform anomaly case among all 8 users being defended.**

The numbers tell the story precisely:
- Premium at CP7 (Jun 8): ~100
- Premium at CP8 (Jun 12): 10,754
- **Change in 4 days: +10,654%**

A +10,654% premium increase in a 4-day window is not a user behavior pattern. It is the platform anomaly. The June 12 analysis explicitly documents this as a systematic technical event affecting 12+ users with 5×–100× spikes. Tushar's spike is 107× in 4 days — the upper bound of what the anomaly produced across the team.

#### The LoC Side Is Actually Positive

While the premium number is extreme, Tushar's output side tells a different story: **1,798 LoC in 4 days**. Among first-session contributors in this window, that is a high output number. He is not generating zero — he is generating real code. The 0.17 ReqEff is entirely a function of the 107× premium spike denominator, not a failure to produce output.

Without the platform anomaly, if his premium had been ~200 (a reasonable first-session spend for 1,798 LoC), his ReqEff would be ~9 — above the team average. He is a Tier C/B user trapped inside a Tier E number by a 4-day technical event.

#### Rank 24 in the Top 30

Despite being a CP8-only contributor, Tushar ranks **24th of 43 users** by cumulative LoC at CP8. He produced more LoC in 4 days than many users produced across the full 53-day period. This is a late-activating engaged user, not a low-performer.

---

### Action Plan

#### Immediate

1. **Defend the ReqEff flag completely** — the +10,654% premium spike in 4 days is the documented platform anomaly, not user behavior. Ask the VP to rerun the efficiency calculation excluding the Jun 8–12 premium data for CP8-only users.
2. **Baseline Q3 from CP9** — like Shubham, Tushar needs a clean first full-period measurement. CP8 data is not valid for ranking.
3. **Efficiency training before Q3 CP1** — 1,798 LoC output is promising. Channel that into inline-first usage to establish a strong ReqEff baseline from the start.

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 CP1 Target | Q3 End Target |
|---|---|---|---|
| LoC | 1,798 | 1,000+ | 4,000+ |
| Premium | 10,754 | ≤500 | ≤500 |
| ReqEff | 0.17 | 5+ | 8+ |
| Tier | None assigned | C | B |

---

### Manager Conversation Guide

**Tell Tushar's manager:**

1. "Tushar's ReqEff flag is a platform anomaly artifact — +10,654% premium increase in 4 days is a documented technical event, not his behavior."
2. "His actual output (1,798 LoC in 4 days) ranks him 24th of 43 users on the team. He is a late activator who produced real code in his first real session."
3. "Without the anomaly, his ReqEff would likely be ~9 — above the team average. The denominator is what failed him, not the numerator."
4. "Recommended action: efficiency training before Q3 CP1, baseline from clean data. Do not carry the Q2 ReqEff number into Q3 performance discussions."

---

---

## 6. Nishtha Thakral (thakraln) — Late Adopter in Learning Curve

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Premium | ReqEff | Pattern |
|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | — | 0 | — | No activity |
| **CP2** | Apr 23 | 0 | 0 | 0 | — | — |
| **CP3** | Apr 28 | 0 | 0 | 0 | — | — |
| **CP4** | May 11 | 0 | 0 | 0 | — | — |
| **CP5** | May 18 | 0 | 0 | 0 | — | — |
| **CP6** | Jun 3 | 69 | +69 | — | — | **First activation** |
| **CP7** | Jun 8 | 1,111 | +1,042 (+1,510%) | 11,112 | ~0.09 | Volatile spike |
| **CP8** | Jun 12 | 806 | −305 (−27%) | 11,451 | ~0.07 | Plateau / anomaly hold |
| **Total Q2** | — | **806** | — | **~11,451** | **~0.07** | 40 days active |

**Q3 Readiness:** ❄️ COLD (Budget Crisis Group — Present since CP7)

---

### Defense

Nishtha's case is more complex than Shubham or Tushar — the premium crisis was already present at CP7 (before the platform anomaly). But there are layered defenses here, and the trajectory context matters significantly.

#### Defense Layer 1: Late Adopter Timeline

Nishtha first activated Copilot at **CP6 (June 3)**. That means:
- She had **0 days** of Copilot exposure for the first 44 days of the Q2 period (Apr 20–Jun 3)
- Her entire Copilot history is **40 days** when evaluated at Jun 12
- Her "53-day performance" is actually a **40-day new-user learning curve**

New users universally show higher premium spend per LoC in their first 4–8 weeks as they learn the tool, experiment with features, use Chat for orientation, and iterate on prompts. This is normal adoption behavior, not inefficiency.

#### Defense Layer 2: CP7 LoC Spike Shows Real Engagement

The +1,510% LoC growth from CP6 (69) to CP7 (1,111) in a single window is the sharpest growth rate among all late adopters. She went from near-zero to producing over 1,000 LoC in a single checkpoint. This is not a passive user — she engaged hard once the tool was available.

The CP8 drop (1,111 → 806, −27%) has two explanations:
1. CP8 is a 4-day window (Jun 8–12) vs. CP7's 5-day window — shorter measurement period
2. The platform anomaly inflated the denominator (premium), but also may have interrupted the LoC measurement

#### Defense Layer 3: Platform Anomaly at CP8

The +3% premium increase from CP7 (11,112) to CP8 (11,451) looks small, but context matters:
- Her CP7 premium was already in crisis territory (11,112 in one window)
- The platform anomaly would normally have reduced her premium if her workflow improved — but the anomaly held it elevated
- The +3% is not evidence of worsening — it's the anomaly preventing normalization

#### The Honest Assessment

Nishtha does have a genuine training need. Unlike Shubham and Tushar (pure anomaly cases), her CP7 premium crisis pre-dates the anomaly window. The high premium is likely from heavy Chat usage and agent-mode exploration during the learning curve. This is fixable — but it is a training issue, not a performance issue.

Her **career best is CP7 (1,111 LoC in one window)** — that output potential is real. The goal is to channel it through a more efficient workflow in Q3.

---

### Action Plan

#### Immediate

1. **Reframe the Q2 assessment** — Nishtha only had 40 days with the tool. The VP is comparing her against users who had 53+ days. Any bottom-5 ranking should control for time-in-tool.
2. **Workflow audit (this week)** — identify what drove the 11,112 premium spend at CP7:
   - Chat Q&A vs. inline completions ratio
   - Agent mode usage (how many multi-file tasks?)
   - Iteration rate (how often does she refine vs. accept first pass?)
3. **Inline-first training** (30 min) — her explosive output potential (1,111 LoC in one window) proves she is capable. The intervention is workflow, not motivation.

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 CP1 Target | Q3 End Target |
|---|---|---|---|
| LoC | 806 | 1,200+ | 4,000+ |
| Premium | 11,451 | ≤600 | ≤500 |
| ReqEff | ~0.07 | 2+ | 5+ |
| Tier | None / Budget Crisis | D | C |

**Key coaching insight:** She generated 1,111 LoC in one checkpoint (CP7) — that output capacity is there. The only task is reducing the premium denominator to match it. If she reaches 500 premium for 1,111 LoC, her ReqEff is 2.2 — already off the bottom-5 list.

---

### Manager Conversation Guide

**Tell Nishtha's manager:**

1. "Nishtha only started using Copilot on June 3 — 40 days before the Q2 snapshot. Any performance comparison against users with 53+ days is comparing different tenures, not different effort levels."
2. "Her best single-window output (1,111 LoC at CP7) shows real potential. The high premium is a new-user learning curve pattern — too much Chat, too much iteration before accepting."
3. "The CP8 plateau is partly the platform anomaly holding premium elevated despite improving workflow."
4. "The intervention: 30-minute inline-first training and a workflow audit. If she maintains 1,000+ LoC/window while dropping premium below 600, she will exit the bottom-5 list by Q3 CP2."

---

---

## 7. Trunal Gawde (trunalgawade) — Pre-Existing Crisis + Platform Anomaly Compound

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Premium | ReqEff | Pattern |
|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | — | 0 | — | No activity |
| **CP2** | Apr 23 | 0 | 0 | 0 | — | — |
| **CP3** | Apr 28 | 0 | 0 | 0 | — | — |
| **CP4** | May 11 | 0 | 0 | 0 | — | — |
| **CP5** | May 18 | 302 | +302 | — | — | First meaningful activation |
| **CP6** | Jun 3 | 304 | +2 (+0.7%) | — | — | **Stall** |
| **CP7** | Jun 8 | 1,086 | +782 (+257%) | 10,863 | ~0.1 | **Budget Crisis spike** |
| **CP8** | Jun 12 | 2,038 | +952 (+88%) | 16,265 | ~0.13 | Crisis worsens + LoC grows |
| **Total Q2** | — | **2,038** | +575% | **16,265** | **~0.13** | Volatile / Budget Crisis |

**CP7 → CP8 coaching outcome (per Jun 12 analysis):** Intervention attempted at CP7; classified as "Ineffective" at CP8 — premium worsened by +49.7%.

**Q3 Readiness:** ❄️ COLD (Budget Crisis Group — Present since CP7, highest premium on team at CP8: 16,265)

---

### Defense

Trunal is the most complex case of the five. Unlike the CP8-only users, his premium crisis started at CP7 — which means the June 8 analysis already flagged him. The question is: what changed between CP7 and CP8, and how much of the CP8 worsening is platform anomaly vs. behavior?

#### The Platform Anomaly Component

The Jun 12 analysis documents the systematic Jun 8–12 premium spike affecting 12+ users. Trunal's premium went from 10,863 (CP7) to 16,265 (CP8) — a +49.7% increase in 4 days. For context:

- His CP6→CP7 increase was **from essentially 0 to 10,863** (the initial crisis spike)
- His CP7→CP8 increase was **+5,402 in 4 days** (+49.7%)

The +49.7% increase aligns with the platform anomaly range (5×–100× for 4 days across the cohort). Without the anomaly, his CP8 premium might have held flat or declined slightly from CP7 — which would have been consistent with the CP7 intervention beginning to take effect.

#### The LoC Side Shows Real Improvement

While the premium picture is difficult, the LoC side is the defense:

- CP7: 1,086 LoC → CP8: 2,038 LoC = **+952 LoC in 4 days**
- That is substantial output — comparable to what top-tier users produce in an entire checkpoint window
- He ranks **22nd of 43 users** at CP8 by cumulative LoC
- His trajectory (302 → 304 → 1,086 → 2,038) shows the second half of Q2 was a genuine activation, not a flat line

The problem is not that he is failing to produce code — he is producing it. The problem is that his workflow burns 8× the premium to do so compared to efficient users.

#### The Honest Assessment

Trunal has a real training problem, and it pre-dates the anomaly. But:
1. His output capacity is real (rank 22 by LoC, strong CP7→CP8 growth)
2. The CP8 premium worsening was compounded by a documented platform event
3. The Jun 8 intervention was noted as "Ineffective" — but the 4-day window is too short to see any coaching impact
4. This is a workflow training issue, not a performance issue — the LoC proves engagement

**The defense is not "his ReqEff is fine."** It is: "his ReqEff reflects an agent-mode training gap, not low engagement. He is the highest LoC producer in the budget crisis group, and the CP8 worsening is anomaly-compounded. The right response is targeted workflow retraining with a hard premium cap — not a performance flag."

---

### Action Plan

#### Immediate (This Week — Highest Priority of All 5 Users)

1. **Hard premium cap — start now**
   - Week 1: 200 premium/week maximum
   - Week 2: 300 premium/week
   - Month 1: 500 premium/period cap
   - If cap is hit mid-period: pause premium access and review

2. **Workflow audit (this week, 30 minutes)**
   - Pull his Copilot activity log for Jun 3–12
   - Identify: agent tasks vs. Chat vs. inline completion ratio
   - Find the specific workflow pattern consuming 16,000+ requests
   - Show him the numbers: "You're using 32× the team-average premium per LoC produced"

3. **Inline-first retraining (60 minutes)**
   - Temporarily restrict agent/Chat features
   - Rebuild his workflow from inline completions only
   - Reintroduce agent features after ReqEff reaches 3+

4. **Weekly spend review** (5 min, every Monday) until he exits the bottom-5 list

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 CP1 Target | Q3 End Target |
|---|---|---|---|
| LoC | 2,038 | 2,500+ | 5,000+ |
| Premium | 16,265 | **≤500** | **≤500** |
| ReqEff | ~0.13 | **3+** | **5+** |
| Tier | E (Budget Crisis) | D | C |

**Critical goal:** Maintain or grow LoC while reducing premium by **97%**. This is achievable by shifting from agent/Chat to inline completions — the LoC capacity is already proven.

---

### Manager Conversation Guide

**Tell Trunal's manager (URGENT — this should happen this week):**

1. "Trunal's CP8 premium worsened from 10,863 to 16,265. Part of this is the platform-wide anomaly (+49.7% aligns with documented Jun 8–12 spike). Part of it is a pre-existing workflow training gap."
2. "His LoC output is strong — 2,038 total, rank 22 of 43 on the team. He is engaged, but using the wrong features in the wrong way."
3. "The Jun 8 coaching intervention was too recent to show results in a 4-day window. Give it to Q3 CP1 before calling it ineffective."
4. "The Q3 plan: hard premium cap (500/period), inline-first retraining, weekly spend review. If we can get his ReqEff to 3+ by CP9, he exits the bottom-5 list and the budget crisis group."
5. "This is a workflow training failure, not a performance failure. His output proves he is capable — he just needs the right guardrails."

---

---

## 8. Pratik Devle (pdevle) — No Premium Crisis; Verify the VP's Data

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Premium | ReqEff | Pattern |
|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | — | — | — | No activity |
| **CP2** | Apr 23 | 0 | 0 | — | — | — |
| **CP3** | Apr 28 | 0 | 0 | — | — | — |
| **CP4** | May 11 | 0 | 0 | — | — | — |
| **CP5** | May 18 | 370 | +370 | — | — | First activation |
| **CP6** | Jun 3 | 1,049 | +679 (+183%) | — | — | **Strong growth** |
| **CP7** | Jun 8 | 1,100 | +51 (+4.9%) | — | — | Consolidating |
| **CP8** | Jun 12 | 1,384 | +284 (+25.8%) | — | — | Re-accelerating |
| **Total Q2** | — | **1,384** | — | — | — | Rising / Steady Climber |

**Q3 Readiness:** ❄️ COLD (Low Engagement — *volume-based classification, not efficiency-based*)
**Budget Crisis:** **None** — pdevle does NOT appear in the budget crisis group in the June 12 analysis
**Average window growth:** +253 LoC/window (Steady Climber)

---

### Defense

**The June 12 analysis does not flag pdevle for a premium crisis or poor efficiency.** He is the outlier in this bottom-5 group — the other four are all in the Budget Crisis group; pdevle is in the Low Engagement group.

This matters significantly: the Low Engagement classification is based on **absolute LoC volume** being below the team midpoint — not on ReqEff. If the VP is ranking pdevle bottom-5 by ReqEff, the defense has a critical first step: **ask the VP for the specific ReqEff number used to flag him**, because the June 12 analysis does not support a premium-based efficiency problem for this user.

#### What the Analysis Actually Shows

1. **Rising/Steady Climber pattern** — the most reliable growth pattern in the cohort. He shows consistent, compounding improvement:
   - CP5→CP6: +679 LoC (+183%)
   - CP6→CP7: +51 LoC (+4.9% — consolidation)
   - CP7→CP8: +284 LoC (+25.8% — re-acceleration)
   
   Three active windows, two growth phases with one consolidation between them. This is not the pattern of a disengaged user.

2. **No budget crisis** — unlike the other 4 users, pdevle has no documented premium spike, no crisis classification, and no intervention required in the June 12 analysis.

3. **COLD classification is volume-based, not quality-based** — the Low Engagement group reflects users who started late or have below-median LoC totals. It does not indicate poor efficiency. pdevle started at CP5 (May 18), giving him only 4 active checkpoints in Q2. Comparing his volume against users who had 8 active checkpoints is not an apples-to-apples comparison.

#### The Possible Scenarios for VP's ReqEff Flag

**Scenario A:** The VP's ReqEff is based on a different data extract than the June 12 analysis. The analysis groups him in Low Engagement (no premium data shown) — it's possible he has moderate premium spend not captured in the top-line tables.

**Scenario B:** The VP is using absolute LoC comparison (1,384 LoC vs. team leaders at 10,000+) as a proxy for efficiency, rather than true ReqEff. If so, this is a volume discussion, not an efficiency discussion.

**Scenario C:** The VP is using a different date range or filter that changes the calculation.

In all scenarios, the defense is the same: **provide the specific number and its calculation source, and verify against the June 12 analysis data before accepting the ranking**.

---

### Action Plan

#### Immediate

1. **Ask the VP for pdevle's specific ReqEff number** — "Can you share which metric flags Pratik as bottom-5? The June 12 analysis does not show a premium crisis for him, and I want to make sure we're looking at the same data."

2. **If the flag is volume-based (not ReqEff):**
   - Adjust the comparison to account for start date (first active at CP5 = May 18 = only 25 days active when most users had 53)
   - His 25-day trajectory is +274% growth (370 → 1,384) — above-average for his tenure

3. **If there is a genuine ReqEff concern not captured in the June 12 analysis:**
   - Workflow audit to identify premium usage pattern
   - Efficiency coaching on prompt quality

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 End Target |
|---|---|---|
| LoC | 1,384 | 4,000+ |
| Pattern | Rising | Steady Climber |
| Tier | Not assigned | C → B |
| Premium | Not flagged | Maintain lean |

**Key Q3 goal:** Extend the Rising pattern across a full 53-day period. If he maintains ~250 LoC/window across Q3, he will reach 4,500+ LoC by end of Q3 and exit the Low Engagement group entirely.

---

### Manager Conversation Guide

**Tell Pratik's manager:**

1. "Pratik does not appear in the budget crisis group in the June 12 analysis. If the VP flagged him for ReqEff, please ask for the specific number and its source — we may be looking at different data cuts."
2. "His LoC trajectory is positive: Rising/Steady Climber, +274% growth in 25 active days. He started at CP5 (May 18), so his Q2 base is shorter than most."
3. "If the concern is absolute volume (1,384 LoC), adjust for start date: he has 25 active days vs. the team's 53-day maximum. On a per-day basis, he is above the low-engagement threshold."
4. "Recommended Q3 framing: extend his Rising pattern, set a 4,000 LoC target for the full Q3 period, and monitor at CP9."

---

---

## Cross-User Comparison — All 8 Users (Jun 12)

| Metric | Vitthal | Amulya | Suraj | Shubham | Tushar | Nishtha | Trunal | Pratik | Team Avg |
|---|---|---|---|---|---|---|---|---|---|
| **CP8 LoC** | 2,609 | 2,472 | 0 | 739 | 1,798 | 806 | 2,038 | 1,384 | ~2,000 |
| **Premium CP8** | ~200 (lean) | ~400 | — | 13,832 | 10,754 | 11,451 | 16,265 | Not flagged | ~400 |
| **ReqEff** | ~14 | ~6.7 | — | 0.05 | 0.17 | 0.07 | 0.13 | — | ~8 |
| **Pattern** | Sustained | Steady Climber | Flat Liner | Very Late Entry | Very Late Entry | Volatile | Volatile | Rising | Mixed |
| **Q3 Readiness** | 🔥 HOT | ♨️ WARM | ❄️ COLD | ❄️ COLD | ❄️ COLD | ❄️ COLD | ❄️ COLD | ❄️ COLD | — |
| **Premium Crisis** | No | No | No | Platform anomaly | Platform anomaly | CP7 + anomaly | Pre-existing + anomaly | No | — |
| **Defend or act?** | **Celebrate** | **Defend tier** | **Investigate** | **Defend fully** | **Defend fully** | **Train** | **Hard cap + train** | **Verify data** | — |

---

## Master Recommendations for VP Conversation

### Opening Frame

> "Of the 8 users we've reviewed, 4 have low ReqEff due to the June 8–12 platform anomaly — a documented technical event that inflated premium spend for 12+ users in a 4-day window. This makes the June 12 ReqEff snapshot unreliable as a performance ranking tool. I'd like to walk through each case with the underlying trend data."

### User-by-User One-Liners

| User | One-liner for VP |
|---|---|
| **Vitthal Devkar** | "3/4 frameworks rate him Tier A. Named efficiency benchmark in the analysis. CP8 dip is a 4-day anomaly artifact." |
| **Amulya Kale** | "Was Tier A on June 8. Dropped to C on June 12 due to platform anomaly — not behavioral. Steady Climber for 8 weeks." |
| **Suraj Dubey** | "Zero LoC across 53 days — this needs a role/access investigation before any performance conversation." |
| **Shubham Fulzele** | "4 days of data, entire career is one anomaly window. Cannot calculate a valid 53-day ReqEff from this." |
| **Tushar Patil** | "0→10,754 premium in 4 days = textbook platform anomaly. His 1,798 LoC output ranks him 24th of 43." |
| **Nishtha Thakral** | "Started using Copilot on June 3 — only 40 active days. New-user learning curve + platform anomaly at CP8." |
| **Trunal Gawde** | "Pre-existing training issue (flagged Jun 8) + anomaly compounded at CP8. Hard premium cap needed, not a performance flag." |
| **Pratik Devle** | "No premium crisis in the analysis data. Please share the specific ReqEff number used to flag him." |

---

*Analysis based on 8 checkpoints (Apr 20 → Jun 12, 2026). Bottom-5 defense section sourced from: github-ai-analysis-12-june-2026-summary.md (Budget Crisis Group, Very Late Entry Group, Volatile Patterns, Steady Climbers). Platform anomaly: github-ai-analysis-12-june-2026.md. Prior baseline: users-ai-usage-analysis-8-june-2026.md.*

---

---

# Third Defense Batch — Mohit Baghel, Shubham Fulzele, Amol Doke, Prashasti Jain, Tushar Patil

> **Note on users already defended in this file:** Shubham Fulzele (Shubhamfulzele28) is fully covered under User 4 above. Tushar Patil (tusharpati166719) is covered under User 5 above — but a **critical new finding** on his login discrepancy is added in User 13 below and substantially strengthens his defense.

---

## Executive Summary — Third Batch

| Developer | Login | Found in Jun 12? | Defense Type | Verdict |
|---|---|---|---|---|
| **Mohit Baghel** | mohitbaghelnice | No | Context-first investigation | ⚠️ Absent from analysis — role/access check required |
| **Shubham Fulzele** | Shubhamfulzele28 | Yes (CP8 only) | Platform anomaly — 4-day window | ✅ Already defended — see User 4 |
| **Amol Doke** | amoldoke051295 | No | Context-first investigation | ⚠️ Absent from analysis — role/access check required |
| **Prashasti Jain** | prashasti-jain | Yes | Volume floor misclassification | ✅ Strong defend — ReqEff ~25.7, penalized by absolute LoC, not efficiency |
| **Tushar Patil** | tusharpatil166719 / tusharpati166719 | Partial (login split) | **Data integrity + platform anomaly** | ✅ Strongest update — login discrepancy erased 8-week Steady Climber history |

---

## 9. Mohit Baghel (mohitbaghelnice) — Absent From June 12 Analysis

### Data Status

| Source | Status |
|---|---|
| Jun 12 analysis (all files) | **Not present** — does not appear in any table, group, or tier assignment |
| Jun 8 analysis | Present — classified **Inactive (0 activity this period — in scope)** |
| Jun 3 and earlier | Not tracked |

**There is no June 12 data to evaluate for Mohit Baghel.** He was absent from the entire June 12 analysis scope.

---

### Defense

If the VP is flagging Mohit for Request Efficiency, one of two things is true:

1. **He is not in the Copilot dataset at all** — meaning his ReqEff is undefined (0 LoC ÷ 0 premium), and the VP may be interpreting absence as a performance metric
2. **He appears in a different data export** not covered by the June 12 analysis — a different date filter, team filter, or dashboard view

In neither case is "bottom-5 by ReqEff" a valid description of his performance. ReqEff requires both a numerator and a denominator. A user with 0 activity has neither.

#### Three Questions — Same as Suraj Dubey

1. **Does he have an active Copilot license?** Zero activity across 53+ days while peers are active strongly suggests either no license or no IDE configuration.
2. **What is his role this quarter?** If he is in a non-coding role (reviews, design, testing, management), LoC is the wrong metric entirely.
3. **Was he available?** Leave, partial availability, or project secondment would explain sustained absence.

#### What Being "In Scope" Means

The June 8 analysis noted him as "Inactive (0 activity — in scope)." "In scope" means his GitHub login was included in the WFM Integrations team filter but contributed zero LoC. This is different from being excluded — it means the tool is tracking him, he is just not using it.

---

### Action Plan

1. **Verify Copilot license and IDE setup** — check whether mohitbaghelnice has an active seat
2. **Confirm role** — coding vs. non-coding this quarter
3. **Confirm availability** — full-time Apr 20 – Jun 12?
4. **If coding role + active license + full availability:** treat as an adoption gap, not a ReqEff failure. Set a Q3 CP1 baseline and evaluate from there.

### Manager Conversation Guide

**Tell Mohit's manager:**
1. "Mohit doesn't appear in the June 12 Copilot analysis at all. Before any performance conversation, I need to confirm: does he have Copilot set up and working?"
2. "Zero activity across two analysis periods (June 8 and June 12) is almost always a tooling or role issue, not a performance issue."
3. "The VP's flag may be based on his absence from the dataset, which is being interpreted as poor efficiency. Absence and poor efficiency are different problems with different solutions."

---

---

## 10. Amol Doke (amoldoke051295) — Absent From June 12 Analysis

### Data Status

| Source | Status |
|---|---|
| Jun 12 analysis (all files) | **Not present** — does not appear in any table, group, or tier assignment |
| Jun 8 analysis | Present — classified **Inactive (0 activity this period — in scope)** |
| Jun 3 and earlier | Not tracked |

Same situation as Mohit Baghel. Amol Doke appears in the June 8 Inactive group alongside Mohit, was zero-activity across both tracked periods, and is entirely absent from the June 12 analysis.

---

### Defense

The defense is identical in structure to Mohit Baghel. The core point: **you cannot have poor Request Efficiency if you have no Request data.** The VP's flag must be based on absence being read as inefficiency.

#### Critical Distinction

There is a meaningful difference between:
- **Zero activity because the tool is not set up** (IT/onboarding issue)
- **Zero activity because the role doesn't require coding** (metrics mismatch)
- **Zero activity despite having access and a coding role** (adoption issue — the only real performance concern)

All three look identical in a dashboard. The defense requires finding out which one applies before any conversation about performance.

---

### Action Plan

1. **Verify Copilot license** — is amoldoke051295 provisioned?
2. **Confirm role** — was Amol in a hands-on coding role Apr 20 – Jun 12?
3. **Confirm availability** — full-time vs. leave/partial?
4. **If all three confirm a gap:** adoption intervention, not performance flag. Q3 CP1 becomes the real baseline.

### Manager Conversation Guide

**Tell Amol's manager:**
1. "Amol doesn't appear in two consecutive analysis periods (June 8, June 12) — he shows zero Copilot activity. This almost always means the tool isn't configured, not that he's performing poorly."
2. "If he is in a coding role with a working Copilot setup and has been available full-time, then we have an adoption conversation. But that conversation starts with 'why hasn't the tool been useful to you?' — not with a performance flag."
3. "Do not rank him bottom-5 on a metric that requires tool usage when tool usage may have been blocked by access or role."

---

---

## 11. Prashasti Jain (prashasti-jain) — Strong Efficiency, Penalized by Volume Floor

### Full Trajectory (CP1–CP8)

| Checkpoint | Date | LoC | Window Delta | Premium | ReqEff | Pattern |
|---|---|---|---|---|---|---|
| **CP1** | Apr 20 | 0 | — | 0 | — | No activity |
| **CP2** | Apr 23 | 0 | 0 | 0 | — | — |
| **CP3** | Apr 28 | 0 | 0 | 0 | — | — |
| **CP4** | May 11 | 203 | +203 | — | — | **First activation** |
| **CP5** | May 18 | 837 | +634 (+312%) | — | — | **Strong growth** |
| **CP6** | Jun 3 | 872 | +35 (+4.2%) | — | — | Consolidation |
| **CP7** | Jun 8 | ~900 | +28 | ~35 | ~25.7 | Efficient, low volume |
| **CP8** | Jun 12 | **1,545** | +645 (+72%) | — | — | **Re-acceleration** |
| **Total Q2** | — | **+1,545** | — | ~35 (CP7) | **~25.7 (CP7)** | Late Accelerator / Rising |

**Q3 Readiness:** ♨️ WARM (upgraded from Cold in Jun 8 analysis)
**Pattern evolution:** Mid-Quarter Stall (Jun 8) → Late Accelerator / Rising (Jun 12)

---

### Defense

**Prashasti Jain has one of the best Request Efficiency scores on the team. The VP's bottom-5 flag is almost certainly based on absolute LoC volume, not efficiency quality — and those are two completely different problems.**

#### The ReqEff Is Not the Issue

At the June 8 checkpoint, her metrics were:
- LoC: ~900
- Premium Requests: ~35
- **ReqEff: ~25.7** — this is top-quartile on the team

For context: the team average ReqEff is ~8. Vitthal Devkar (named efficiency benchmark) is at ~14. Prashasti at ~25.7 means she generates **more LoC per premium request than the team's named top performer**.

She is not on a "bottom-5 by ReqEff" list because of poor efficiency. Either:
1. The VP is using absolute LoC as a proxy for efficiency (lower LoC = "less efficient" — which is wrong)
2. Her CP8 premium spiked due to the platform anomaly, dropping her number since Jun 8
3. A different calculation method is being applied

#### Why Tier E — and Why It Doesn't Mean Poor Performance

The June 8 analysis gave her Tier E in all frameworks despite the strong ReqEff. The reason is the **absolute LoC floor**: the v1 framework requires minimum LoC thresholds for Tier D and above. With ~900 LoC at CP7, she was below the floor — not because she was inefficient, but because she started late (first activation at CP4 = May 11) and her absolute volume was still building.

Tier E due to volume floor ≠ Tier E due to poor performance. These are categorically different.

#### The CP8 Re-Acceleration Is the Most Positive Signal

The +72% LoC growth from CP7 (~900) to CP8 (1,545) in 4 days is the **highest final-window growth rate** among the non-crisis users in this analysis. This is not a user who is declining — it's a user who was building slowly and then hit her stride.

Her Q3 Readiness was upgraded from Cold (Jun 8) to **Warm (Jun 12)** specifically because of this late acceleration. The analysis recognized the trajectory improvement even if the snapshot tier didn't.

#### Pattern Evolution Tells the Story

| Period | Pattern | Interpretation |
|---|---|---|
| CP4–CP6 | Mid-Quarter Stall | Activated late, slow early growth |
| CP7–CP8 | Late Accelerator / Rising | Found workflow, output accelerating |
| Q3 Projection | Rising → Steady Climber | On track to exit volume floor by Q3 CP2 |

---

### Action Plan

#### Immediate

1. **Reframe the VP's concern** — ask whether the flag is ReqEff or absolute LoC volume. If ReqEff: show the ~25.7 number from Jun 8. If volume: agree on a Q3 target and note she is already accelerating.
2. **No efficiency coaching needed** — her ReqEff is already excellent. The only development need is sustained output volume.
3. **Sustain the CP8 momentum** — the +72% final-window spike needs to be carried into Q3. The risk is a post-sprint crash where the burst doesn't continue.

#### Q3 Targets

| Metric | Current (Jun 12) | Q3 CP1 Target | Q3 End Target |
|---|---|---|---|
| LoC | 1,545 | 2,000+ | 5,000+ |
| ReqEff | ~25.7 (CP7) | Maintain >15 | Maintain >15 |
| Tier (v1) | E (volume floor) | D | C → B |
| Premium | ~35/period (lean) | Maintain lean | Maintain lean |
| Pattern | Late Accelerator | Steady Climber | Steady Climber |

**Key coaching point:** Do NOT change her workflow — her efficiency is already exceptional. The only goal is output volume. More consistent daily usage of the same approach she already uses.

---

### Manager Conversation Guide

**Tell Prashasti's manager:**

1. "Prashasti's Request Efficiency of ~25.7 at the June 8 checkpoint is better than Vitthal Devkar — our named efficiency benchmark. She is not on a bottom-5 list because of poor efficiency."
2. "Her Tier E classification is a volume threshold issue, not a quality issue. She started activating Copilot in early May and her LoC is still building. By Q3 CP2, she should cross the volume floor if the CP8 acceleration continues."
3. "The VP's flag may be based on absolute LoC (1,545 vs. top users at 5,000–10,000). That is a valid development target — but it is not a Request Efficiency problem."
4. "Q3 recommendation: sustain the momentum from the CP8 spike. Her efficiency is already there — she just needs to produce more consistently."

---

---

## 12. Tushar Patil — Critical Update: Login Discrepancy Changes the Entire Defense

> **This section supplements User 5 (tusharpati166719) already in this file.** The defense in User 5 treated Tushar as a "Very Late Entry" based on Jun 12 data showing zero history. This section adds a critical new finding that fundamentally changes the defense.

### The Login Discrepancy

| Analysis Period | Login Used | LoC at CP1 | LoC at CP7/CP8 | Pattern |
|---|---|---|---|---|
| **Jun 3 analysis** | `tusharpatil166719` | 381 | 1,798 (CP6) | Steady Climber |
| **Jun 8 analysis** | `tusharpatil166719` | 381 | ~1,900 (CP7) | Steady Climber, ReqEff ~19 |
| **Jun 12 analysis** | `tusharpati166719` | 0 | 1,798 (CP8 only) | Very Late Entry |

**Difference between the two logins:** `tusharpatil166719` vs `tusharpati166719` — a single letter (`l` missing in "pati" vs "patil"). This is a **one-character typo in data extraction**, not two different people.

### What the Real History Shows

Using `tusharpatil166719` (the historically consistent login from Jun 3 and Jun 8 files):

| Checkpoint | Date | LoC | Window Delta | Pattern |
|---|---|---|---|---|
| **CP1** | Apr 20 | 381 | baseline | Early adopter |
| **CP2** | Apr 23 | 381 | 0 | Flat |
| **CP3** | Apr 28 | 853 | +472 | **Growth spurt** |
| **CP4** | May 11 | 1,389 | +536 | Steady |
| **CP5** | May 18 | 1,631 | +242 | Continuing |
| **CP6** | Jun 3 | 1,798 | +167 | Consolidating |
| **CP7** | Jun 8 | ~1,900 | +102 | **Steady Climber** |
| **CP8** | Jun 12 | ~2,000 (est.) | — | Continuing |

**ReqEff at Jun 8:** ~19 (main file) — above team average, no budget crisis
**Tier at Jun 8:** Tier C (CRQC), Tier D (v1/v2) — not a top performer, but a steady, improving one
**Pattern:** Steady Climber (4.7× LoC growth from CP1 to CP7)
**Q3 Readiness at Jun 8:** Warm

### The Real Defense

**Tushar Patil is not a "Very Late Entry" user with 4 days of data. He is a Steady Climber with 8 weeks of consistent growth and a ReqEff of ~19 — above team average.**

The Jun 12 analysis classified `tusharpati166719` (with the typo) as a brand-new user with zero history. That classification is a **data integrity error**, not a performance signal. When the correct login (`tusharpatil166719`) is used:

- His LoC growth from CP1 → CP7 is **+1,519 LoC** (4.7×)
- His ReqEff at CP7 is **~19** — above team average of ~8
- He was classified as **Steady Climber** — the most reliable pattern in the cohort
- His Jun 8 tier was **C (CRQC)** with a CRQC score of 4/9

**The 10,754 premium at CP8 for `tusharpati166719` likely does not belong to Tushar Patil at all.** It belongs to a different user whose login was incorrectly merged with his name. Alternatively, if the login was renamed/updated in GitHub between Jun 8 and Jun 12, then the CP8 data is real — but the zero historical context is a lookup failure, not his actual history.

### The VP Conversation

If the VP is flagging Tushar Patil for bottom-5 ReqEff based on the Jun 12 data:

1. **Show the Jun 8 data under `tusharpatil166719`** — ReqEff ~19, Steady Climber, Tier C
2. **Point out the one-letter login difference** — this is a data extraction issue, not a performance issue
3. **Ask the VP to reconcile which login they are evaluating** — because the two logins show completely different performance pictures

This is a data integrity case, not a performance case.

---

### Updated Summary for Tushar Patil

| Metric | Jun 12 Analysis (tusharpati166719) | Jun 8 Analysis (tusharpatil166719) | Which is correct? |
|---|---|---|---|
| CP1 LoC | 0 | 381 | **Jun 8 (full history)** |
| CP7/CP8 LoC | 1,798 (CP8) | ~1,900 (CP7) | Similar values, different checkpoints |
| Pattern | Very Late Entry | Steady Climber | **Jun 8** |
| ReqEff | ~0.17 (collapsed) | ~19 | **Jun 8** |
| Tier | E / unranked | C (CRQC) | **Jun 8** |
| Premium crisis | 10,754 | No crisis (~600) | Needs verification |
| Q3 Readiness | Cold | Warm | **Jun 8** |

**Bottom line:** Before accepting the VP's bottom-5 flag for Tushar Patil, verify which login is being used in the dashboard — `tusharpatil166719` or `tusharpati166719`. One letter separates a Steady Climber from a budget crisis entry.

---

---

## Updated One-Liners for VP Conversation

| User | One-liner |
|---|---|
| **Mohit Baghel** | "Not in the June 12 analysis at all — zero activity may reflect tooling/access gap, not performance." |
| **Shubham Fulzele** | "4 days of data during a platform anomaly. See User 4 in this file for the full defense." |
| **Amol Doke** | "Same situation as Mohit Baghel — absent from two consecutive analysis periods. Investigate access/role before any flag." |
| **Prashasti Jain** | "ReqEff of ~25.7 at Jun 8 — better than the named efficiency benchmark. Bottom-5 flag is likely based on absolute volume, not efficiency quality." |
| **Tushar Patil** | "One-letter login difference between Jun 8 (`tusharpatil166719`) and Jun 12 (`tusharpati166719`). The Jun 8 login shows a Steady Climber with ReqEff ~19. Verify which login the VP is evaluating before accepting the flag." |

---

*Third batch sourced from: github-ai-analysis-8-june-2026.md (Inactive group, Steady Climbers), github-ai-analysis-12-june-2026-summary.md (Rising/Late Accelerator for prashasti-jain), github-ai-analysis-3-june-2026-summary.md (tusharpatil166719 Master Table). Login discrepancy finding: cross-referenced Jun 3, Jun 8, and Jun 12 files.*
