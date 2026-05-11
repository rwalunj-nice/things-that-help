# 📊 Github Benchmark — CRQC Framework (Option 3)

> **What this is:** A full redesign of the benchmark into four explicitly named pillars: **Core**, **ROI**, **Quality**, and **Context**. Unlike the v1 3-tier system (which mixes signal types and applies benchmarks inconsistently across workflow types), CRQC gives every signal a named home, clear scoring rules, and a defined role in the final tier calculation.
>
> Use this framework when you need the strongest possible defensibility with VP R&D — every tier assignment traces back to explicit, scored evidence across four dimensions.

---

## The Four Pillars

| Pillar | Letter | Source | Purpose |
|---|---|---|---|
| **Core** | C | Power BI AI Usage | Is the user actually using Copilot in a productive workflow? |
| **ROI** | R | Power BI AI Usage | Is the premium spend justified by output volume? |
| **Quality** | Q | Power BI Pull Request | Is the output shipping and meeting code review standards? |
| **Context** | C | Power BI AI Usage | What diagnostic signals explain the Core/ROI/Quality scores? |

> **CRQC principle:** A user's tier is determined by their **C + R + Q scores**. The fourth C (Context) is diagnostic only — it explains *why* scores look the way they do, never directly drives tier assignment.

---

## Pillar 1 — Core (C)

Measures whether the user is engaged in a productive Copilot workflow. **Workflow Type must be assigned first** (using Agent Contribution % from Power BI).

### Workflow Type Assignment

| Agent Contribution % | Workflow Type |
|---|---|
| ≥ 70% | Agent-First |
| 30–69% | Hybrid |
| < 30% | Inline-First |

### Core Score (0–3 points)

**Agent-First users:**

| Signal | Condition | Points |
|---|---|---|
| Request Efficiency | > 15 | 2 |
| Request Efficiency | 8–15 | 1 |
| Request Efficiency | < 8 | 0 |
| LoC Added trend | Increasing vs. prior period | +1 |

**Hybrid users:**

| Signal | Condition | Points |
|---|---|---|
| % Code Acceptance | 15–30% | 1 |
| Request Efficiency | > 8 | 1 |
| Code Acceptance Count | > 10 | +1 |

**Inline-First users:**

| Signal | Condition | Points |
|---|---|---|
| % Code Acceptance | 20–35% | 2 |
| % Code Acceptance | 10–19% | 1 |
| Code Acceptance Count | > 20 | +1 |

> **Maximum Core Score: 3 points**

---

## Pillar 2 — ROI (R)

Measures whether the premium budget consumed is producing proportional output. Universal — applies identically to all workflow types and role contexts (except Research, who are excluded from ROI scoring).

### ROI Score (0–3 points)

| Signal | Condition | Points |
|---|---|---|
| Request Efficiency | > 20 LoC/request | 3 |
| Request Efficiency | 10–20 LoC/request | 2 |
| Request Efficiency | 5–10 LoC/request | 1 |
| Request Efficiency | < 5 LoC/request | 0 |
| Premium Requests | ≤ 500 (lean spend) | +1 bonus |
| Premium Requests | > 1,700 (outlier spend) | −1 penalty |

> **Maximum ROI Score: 3 points (4 with lean spend bonus; minimum 0)**

---

## Pillar 3 — Quality (Q)

Sourced from Power BI **Pull Request Details** tab. Measures whether Copilot-assisted output is production-ready. This is the pillar that connects Copilot usage to actual engineering delivery.

### Quality Score (0–3 points)

| Signal | Power BI Metric | Condition | Points |
|---|---|---|---|
| PR Merge Rate | PR Status: Merged ÷ Total submitted | ≥ 80% | 2 |
| PR Merge Rate | 50–79% | 1 |
| PR Merge Rate | < 50% | 0 |
| Review Rate | Reviews ÷ Pull Requests | ≥ 1 review per PR | +1 |
| Time to Merge | Time to Merge | ≤ 3 days avg | +1 bonus (cap score at 3) |

> **Note:** Q Score is calculated at user level by filtering Power BI PR tab by user login and the same time window as the AI Usage analysis.
>
> **Maximum Quality Score: 3 points**

---

## Pillar 4 — Context (C)

Diagnostic signals only. These never add or subtract from the final tier score. They explain anomalies in C, R, and Q scores and inform the coaching narrative.

| Signal | What to Look For |
|---|---|
| Initiated Interactions | Very high with low C/R score → user is struggling, not productive |
| Suggestion Efficiency (LoC/Code Gen) | High in Agent-First = healthy; high in Inline-First with low accept rate = large suggestions being rejected |
| LoC Suggested vs. LoC Added | Large gap in Inline-First → low acceptance; expected gap in Agent-First |
| Code Generation Count | Very high with low C score → volume without value |

---

## CRQC Tier Assignment

Sum the Core + ROI + Quality scores (0–9 total) and map to a tier:

| Total Score (C + R + Q) | Tier | Label |
|---|---|---|
| 7–9 | 🌟 **Tier A** | Top Performer |
| 5–6 | 👍 **Tier B** | Solid Contributor |
| 3–4 | 👌 **Tier C** | Needs Improvement |
| 1–2 | 🟠 **Tier D** | Low Efficiency |
| 0 | 🔴 **Tier E** | Urgent Attention |

### Override Rules

| Condition | Override |
|---|---|
| Q Score = 0 (< 50% PR merge rate) | Cannot be Tier A regardless of C + R score |
| R Score = 0 AND Premium > 500 | Cannot be above Tier C regardless of C + Q score |
| Momentum Score > +100% (from github-benchmark-role-momentum.md) | Eligible for one tier promotion beyond score-based placement |
| Role Context = Research | Not tiered. Reported separately with Interaction count and Premium as the two tracked metrics. |

---

## CRQC Scorecard Template

| User | Workflow Type | Role | C Score | R Score | Q Score | Total | Tier | Momentum | Notes |
|---|---|---|---|---|---|---|---|---|---|
| *Mikhail Shnayderman* | Agent-First | Developer | 3 | 3 | TBD | TBD | TBD | Stable | 93.1 Req Eff |
| *Prathmesh Ranadive* | Hybrid | Developer | 2 | 0 | TBD | TBD | TBD | Rising | 35.8% accept, 864 premium |
| *Rahul Walunj* | Agent-First | Research | — | — | — | — | Research | — | Excluded from tier |
| *Shridhar Mishra* | Inline-First | Developer | 1* | 0 | TBD | TBD | TBD | — | *87.5% accept, 0 LoC — Q score critical |

---

## VP R&D Narrative Template

Use this structure when presenting CRQC results to VP R&D:

> **"Our Copilot effectiveness is measured across three dimensions: adoption quality (Core), budget efficiency (ROI), and code delivery (Quality).**
>
> Tier A performers score 7–9 out of 9 across all three dimensions. Currently, [X] of our [N] developers ([X]%) achieve this standard, producing [Y]% of our Copilot-assisted code on [Z]% of the premium budget.
>
> Tier D/E users score 0–2 out of 9. Our coaching program has moved [N] users out of these tiers over the past 4 weeks — [specific names] are on strong improvement trajectories with Momentum Scores of [X]%.
>
> [For specific low performer]: [Name] currently scores [C/R/Q]. Their [low signal] is explained by [Context signal]. The coaching plan targets [specific metric] improvement over [timeframe]."

---

## Framework Comparison

| Dimension | v1 (Original) | v2 (Workflow-Aware) | Role+Momentum | CRQC |
|---|---|---|---|---|
| Agent-mode handling | ❌ Not handled | ✅ Workflow type classifier | ✅ Inherited from v2 | ✅ Per-pillar workflow rules |
| Code quality signal | ❌ None | ❌ None | ✅ PR modifier (±1) | ✅ Full Q pillar (0–3 scored) |
| Role exceptions | ❌ Ad hoc | ❌ Ad hoc | ✅ Formal Role Context | ✅ Formal Role Context |
| Improvement velocity | ❌ None | ❌ None | ✅ Momentum Score | ✅ Momentum override |
| VP defensibility | Medium | Medium-High | High | Highest |
| Weekly effort | Low | Low | Medium | Medium-High |
| Backward compatibility | — | Full | Full | Partial (scores replace A–E direct mapping) |

---

*CRQC is designed as the long-term target state. For teams already using v1 or v2, migrate by running both frameworks in parallel for 2–3 periods to validate tier consistency before switching fully.*
