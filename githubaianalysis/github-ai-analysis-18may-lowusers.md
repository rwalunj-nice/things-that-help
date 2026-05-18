# GitHub Copilot Low-Usage Pattern Analysis — May 18, 2026

> **Scope**: 4 users with low premium request consumption identified from the May 18, 2026 analysis  
> **Product**: WFM Integrations | **Team**: All | **R&D VP**: WFM  
> **Analysis Date**: May 18, 2026 | **Data Synced**: May 17, 2026 10:30 PM  
> **Periods Covered**: Apr 20, Apr 23, Apr 28, May 11, May 18 (5 data points)  
> **Purpose**: Deep-dive usage pattern analysis to understand why these users have low premium request consumption and what coaching actions are appropriate

---

## Users Analysed

| User Login | Name | May 18 Prem Req | May 18 LoC Added | May 18 Tier |
|---|---|---|---|---|
| dsuraj25 | Suraj Dubey | 92 | 491 | 🟠 D |
| pdevle | Pratik Devle | 168 | 370 | 🟠 D |
| trunalgawade | Trunal Gawade | 93 | 302 | 🟠 D |
| mshivarkar | Mohan Shivarkar | 69 | 28 | 🔴 E |

---

## User 1 — Suraj Dubey (`dsuraj25`)

### Pattern Type: **Ghost User — Frozen Dataset**

### Multi-Period Data

| Period | Int | LoC Added | % Accept | SuggEff | Prem Req | Req Eff |
|---|---|---|---|---|---|---|
| Apr 20 | 10 | 491 | 0.0% | 17.54 | 70 | 7.0 |
| Apr 23 | 10 | 491 | 0.0% | 17.54 | 70 | 7.0 |
| Apr 28 | 10 | 491 | 0.0% | 17.54 | 70 | 7.0 |
| May 11 | 11 | 491 | 0.0% | 16.37 | — | — |
| May 18 | 11 | 491 | 0.0% | 16.37 | 92 | 5.3 |

### Analysis

The most striking pattern across all 5 periods: **LoC Added is identically 491 from Apr 20 through May 18**. No user produces exactly the same LoC across 5 consecutive analysis periods unless they had one single session of activity and then stopped completely. The marginal change in Interactions (10 → 11) and slight Req Eff decline (7.0 → 5.3) confirm that a very small amount of new session activity occurred in May, but fundamentally **Suraj has not worked in Copilot since his first session in April**.

**Root Cause**: Suraj is not using Copilot in his active workflow. His one session produced 491 LoC (decent for a single session), but there has been no repeat engagement. This is a **non-adoption** case disguised by cumulative metrics — the dashboard shows all-time totals, and Suraj's total is entirely from one early session.

**Why Premium Requests Are Low**: 92 premium requests over ~4 weeks is roughly 2–3 sessions worth of agent queries. For a developer doing active daily work, typical consumption is 300–800+ requests/month. Suraj's figure confirms near-total absence from the platform.

### Coaching Recommendation

- **Priority**: High — this is a non-adoption case, not a skill gap
- Confirm with direct manager whether Suraj is actively assigned to development work
- If yes: schedule a 30-minute Copilot onboarding session focused on daily use patterns (not just showing features)
- Set a 2-week re-check milestone — target: >500 Prem Req and growing LoC trend
- If confirmed on non-development work (QA, process, documentation): re-evaluate licence allocation

---

## User 2 — Pratik Devle (`pdevle`)

### Pattern Type: **Slow Ramp — Chat-Only Usage**

### Multi-Period Data

| Period | Int | LoC Added | % Accept | SuggEff | Prem Req | Req Eff |
|---|---|---|---|---|---|---|
| Apr 20 | 2 | 361 | 4.5% | 8.20 | 84 | 4.3 |
| Apr 23 | 5 | 361 | 4.5% | 8.20 | 93 | 3.9 |
| Apr 28 | 7 | 368 | 5.4% | 6.57 | 99 | 3.7 |
| May 11 | 21 | 370 | 6.6% | 6.07 | — | — |
| May 18 | 30 | 370 | 6.6% | 6.07 | 168 | 2.2 |

### Analysis

Pratik shows the most consistent — and concerning — trend of the four users. Every metric moves in the **wrong direction**:

- **Interactions are climbing** (2 → 30 over 5 periods), which means he is increasingly engaging with Copilot
- **LoC Added is essentially flat** (361 → 370), meaning the increased engagement is producing almost no code output
- **Req Eff is falling sharply** (4.3 → 2.2), meaning each premium request is delivering less value over time
- **SuggEff is declining** (8.20 → 6.07), confirming that accepted suggestions are getting smaller or being discarded

**Root Cause**: Pratik is using Copilot extensively as a **chat/Q&A tool** — asking questions, getting explanations, having code reviewed — but is NOT accepting or using the generated code. This is evidenced by:
1. High and growing interaction count (30 is above-average engagement)
2. Near-flat LoC Added despite more sessions
3. Very low % Code Acceptance (6.6%) — Pratik is reading Copilot responses but not accepting suggestions into his editor
4. Declining Req Eff as conversation-heavy sessions consume more premium requests per unit of output

**Why Premium Requests Are Low in Absolute Terms**: 168 requests/month is below average but not negligible — Pratik IS using the tool, just ineffectively for code generation. He is consuming budget on questions that don't translate to committed code.

### Coaching Recommendation

- **Priority**: Medium-High — this is a workflow misalignment that is worsening over time
- Pratik understands the tool exists and engages with it; the issue is he has not learned to trust the output
- Coaching focus: accepting suggestions more liberally (try Accept + refine rather than Read + retype)
- Suggest using inline completions for boilerplate/repetitive tasks where he can verify quickly
- Key metric to watch: % Code Acceptance. Target: move from 6.6% toward 15%+ within 2 periods
- Do NOT tell Pratik to use Copilot less — the chat behaviour is understandable; redirect it to code output

---

## User 3 — Trunal Gawade (`trunalgawade`)

### Pattern Type: **Healthy Ramp — Early Stage, Progressing Well**

### Multi-Period Data

| Period | Int | LoC Added | % Accept | SuggEff | Prem Req | Req Eff |
|---|---|---|---|---|---|---|
| Apr 20 | 19 | 6 | 19.6% | 0.12 | 7 | 0.9 |
| Apr 23 | 20 | 6 | 19.6% | 0.12 | 8 | 0.8 |
| Apr 28 | 33 | 61 | 21.3% | 0.65 | 23 | 2.7 |
| May 11 | 86 | 261 | 27.4% | 1.46 | — | — |
| May 18 | 100 | 302 | 23.7% | 1.32 | 93 | 3.2 |

### Analysis

Trunal is the **standout positive story** among the four users. Every core metric is trending in the right direction:

- **LoC Added**: 6 → 302 (+4,933% over 5 periods) — genuine output growth
- **Interactions**: 19 → 100 (+426%) — dramatically more engagement
- **% Accept**: 19.6% → 23.7% — now within the healthy 20–35% inline-first target range
- **SuggEff**: 0.12 → 1.32 (+1,000%) — suggestions are now meaningfully contributing to committed code
- **Req Eff**: 0.9 → 3.2 — efficiency improving steadily as Trunal develops better prompting habits
- **Prem Req**: 7 → 93 — growing consumption reflecting genuine workflow integration

**Root Cause for Low Premium Requests**: Trunal is in an **early adoption curve**. He only started generating real code output from Apr 28 onwards. The low absolute premium count reflects the fact that he is a **recent starter**, not a disengaged user. His trajectory is the healthiest of all four users.

**Key Observation**: The April 20–23 period shows Trunal attempting many interactions (19–20) with almost zero LoC output (6 LoC). This is the "trying to figure it out" phase. The breakthrough happened in late April when his sessions started generating committed code. By May 18, his % Accept of 23.7% and SuggEff of 1.32 are both healthy Inline-First benchmarks.

**Why Premium Requests Are Low in Absolute Terms**: At 93 requests/month, Trunal is in the low-medium range. But the trend is strongly upward (+1,229% from 7 to 93). If the current trajectory continues, he should reach 300–400 requests/month within 2–3 periods.

### Coaching Recommendation

- **Priority**: Low — Trunal is progressing well and needs encouragement, not intervention
- Positive reinforcement: his % Accept and LoC trend are model behaviour for a new Copilot user
- Light nudge: try longer/more complex completions to push SuggEff higher (currently 1.32; target >5 for Inline-First)
- Optional: introduce Copilot Chat for planning and architecture tasks to boost Interactions with higher-value outputs
- Re-check in 2 periods — expect to see him move from Tier D to Tier C naturally

---

## User 4 — Mohan Shivarkar (`mshivarkar`)

### Pattern Type: **Token Autocomplete — Manager/Reviewer Behaviour**

### Multi-Period Data

| Period | Int | LoC Added | % Accept | SuggEff | Prem Req | Req Eff |
|---|---|---|---|---|---|---|
| Apr 20 | 4 | 0 | 40.0% | 0.00 | 16 | 0.0 |
| Apr 23 | 18 | 1 | 37.5% | 0.06 | 32 | 0.0 |
| Apr 28 | 29 | 28 | 66.7% | 1.33 | 43 | 0.7 |
| May 11 | 52 | 28 | 69.6% | 1.22 | — | — |
| May 18 | 73 | 28 | 60.0% | 0.93 | 69 | 0.4 |

### Analysis

Mohan presents the most puzzling profile: **consistently high % Accept (40–70%)** combined with **near-zero LoC output (0–28 LoC over 5 periods)**. This combination is statistically very unusual and points to a specific usage pattern.

**Root Cause**: Mohan is accepting Copilot suggestions at a high rate, but the suggestions are **micro-completions** — single tokens, short identifiers, one-word completions, minor syntax assists. This is evidenced by:
1. SuggEff of 0.00–1.33 means each accepted suggestion contributes less than 1–1.3 lines of actual code
2. % Accept of 60–70% is characteristic of someone accepting but only the smallest / most obvious completions
3. The interaction count growing (4 → 73) while LoC stays flat at 28 confirms that sessions are happening, but each session's total code output is minimal

**Two possible explanations**:
- **Manager/Reviewer role**: Mohan may be spending most of his Copilot sessions reviewing code, asking questions, or having Copilot explain PRs — tasks where accepted output doesn't result in committed lines of code
- **Exploratory/learning usage**: Mohan may be using Copilot for config files, comments, documentation, or very small edits that don't show up significantly in LoC metrics

**Note**: The May 18 analysis correctly classifies Mohan as Inline-First (Tier E). His 60% accept rate is NOT a sign of good inline usage — it reflects the very small size of what he's accepting, not disciplined selective acceptance.

**Why Premium Requests Are Low**: 69 requests/month is very low. Premium requests are consumed primarily by Copilot Chat and agent interactions. Mohan's low count confirms his usage is primarily passive inline suggestion acceptance rather than active chat or agent sessions.

### Coaching Recommendation

- **Priority**: Medium — determine role clarity first before prescribing changes
- **Clarify with manager**: Is Mohan primarily doing code reviews, architecture work, or mentoring rather than greenfield development? If yes, his metrics will always look like this and that's acceptable
- If he IS doing development work: the issue is that he's accepting very small suggestions rather than using Copilot for larger completions
  - Suggest: disable single-token accept shortcut and only accept when suggestion is 3+ lines
  - Suggest: start using Copilot Chat to generate boilerplate blocks, then paste and edit
- **Do not expect** Mohan to reach Tier B/C purely through inline completions — his pattern suggests he needs a workflow shift toward agent or chat modes

---

## Summary Comparison

| User | Archetype | Root Cause | Trajectory | Action |
|---|---|---|---|---|
| Suraj Dubey | Ghost User | Single session, then stopped | Flat — stagnant | High priority: re-onboard or review licence |
| Pratik Devle | Chat-Only | High engagement, low code output | Worsening (Req Eff declining) | Medium-High: redirect from chat to code acceptance |
| Trunal Gawade | Healthy Ramp | New starter, early adoption curve | Strong upward trend | Low: positive reinforcement + light nudge |
| Mohan Shivarkar | Token Autocomplete | Micro-completions only, possible review role | Flat-improving engagement | Medium: clarify role + shift to chat/agent mode |

---

## Team-Level Insight

Three of the four users (Dubey, Devle, Shivarkar) show patterns that will NOT self-correct without intervention. Trunal Gawade is the exception — he is progressing well without any coaching.

The common thread across the struggling three: **premium requests are low not because they are efficient users, but because they are either not using the tool (Dubey), using it in a way that doesn't produce code (Devle), or only accepting micro-completions (Shivarkar)**. None of these patterns are captured adequately by % Code Acceptance alone — which is why multi-period trend analysis and SuggEff × LoC correlation are essential for identifying real usage behaviour.

---

*Analysis generated: May 18, 2026 | Based on 5-period data: Apr 20, Apr 23, Apr 28, May 11, May 18*
