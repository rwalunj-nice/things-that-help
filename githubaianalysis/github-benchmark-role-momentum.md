# 📊 Github Benchmark — Role Context + Momentum (Option 2)

> **What this adds on top of v2:** Three enhancements that directly serve the four use cases (VP tier management, user segregation, coaching plans, defending low performers):
> 1. **Role Context** — formalizes the informal exceptions already being made (managers, research users) so they stop appearing as anomalies
> 2. **Momentum Score** — surfaces improvement velocity so coaching success is quantified and visible even when absolute tier hasn't changed yet
> 3. **PR Quality Modifier** — uses Power BI Pull Request data to validate that LoC Added actually shipped, strengthening the VP ROI story

---

## Dimension 1 — Role Context

Assign each user a Role Context at the start of analysis. This determines which benchmark set applies. Role Context is set by the manager — it does not change week-to-week unless the person's responsibilities change.

| Role Context | Who | Benchmark Adjustment |
|---|---|---|
| **Developer** | Hands-on engineers writing production code | Full benchmark applies — all T1, T2, T3 signals |
| **Manager** | Engineering managers who also code (e.g., Swapnil Zade) | T2 efficiency threshold lowered to > 5; LoC volume is secondary; Interaction count weighted higher as a team engagement signal |
| **Lead/Architect** | Senior ICs doing design, review, and selective coding | % Accept benchmark relaxed to 10–25%; T2 Req Eff > 8 |
| **Research/Exploration** | Users using Copilot for documentation, code understanding, non-shipping tasks (e.g., Rahul Walunj) | LoC Added excluded from scoring; Premium justified by Interaction count; Not tiered A–E — labeled **Research** |

> **Why this matters:** Shridhar Mishra (87.5% accept, 0 LoC), Susovan Samal (100% accept, 1/1 count, manager), and Rahul Walunj (751 premium, 0 LoC, research) are currently handled as ad hoc footnotes. Role Context makes their classification a framework output, not an exception that needs explaining to a VP.

### Role Context — VP Defense Language

| Role | If VP asks "Why is their LoC zero?" | Response |
|---|---|---|
| Research | "This user's role uses Copilot for [documentation / code understanding / tooling research]. LoC Added is not the right output metric. We track Premium Efficiency against Interaction value instead." | |
| Manager | "As an engineering manager, their primary Copilot value is in code review, architecture guidance, and selective implementation. We benchmark them on engagement + efficiency, not raw volume." | |

---

## Dimension 2 — Momentum Score

The Momentum Score measures **rate of change** between the current period and the prior period. It surfaces users who are improving rapidly (coaching is working) or declining (intervention needed), independent of their absolute tier position.

### Calculation

```
Momentum Score = ((Current Req Eff − Prior Req Eff) / Prior Req Eff) × 100
```

If Prior Req Eff = 0, use LoC Added change as a proxy:
```
Momentum Score (proxy) = ((Current LoC − Prior LoC) / max(Prior LoC, 1)) × 100
```

### Momentum Labels

| Momentum Score | Label | Action |
|---|---|---|
| > +100% | 🚀 **Breakout** | Celebrate publicly. Document the coaching action that drove it. Protect from premature tier downgrade. |
| +30% to +100% | 📈 **Rising** | Acknowledge in coaching review. On track — maintain current coaching plan. |
| -10% to +30% | ➡️ **Stable** | No special action. Monitor for sustained trend. |
| -10% to -30% | 📉 **Slipping** | Flag for manager check-in. Investigate cause before next period. |
| < -30% | 🔴 **Declining** | Immediate coaching intervention regardless of current tier. |

### Momentum Override Rules

| Scenario | Rule |
|---|---|
| User is Tier D/E **and** Momentum is Breakout/Rising | Do NOT downgrade. Show as "D↑" or "E↑" in tier table to signal trajectory. |
| User is Tier A/B **and** Momentum is Declining | Flag with "A↓" marker. Eligible for tier drop if decline continues next period. |
| Tier C user with Breakout momentum | Eligible for skip-tier promotion to B (bypass C→B→A ladder for exceptional improvement). |

### Momentum — VP Defense Language

> "Amol Salunkhe is classified as Tier C this period. His Momentum Score is +3,500% — a 71× increase in output in one week. The coaching investment is working. We expect Tier B classification next period if the trajectory holds."

---

## Dimension 3 — PR Quality Modifier

Sourced from the **Power BI Pull Request Details** tab. The PR Quality Modifier validates that LoC Added from Copilot is actually shipping — not just being generated and discarded.

### Available PR Signals (from Power BI PR tab)

| Signal | Power BI Field | What It Tells You |
|---|---|---|
| **PR Merge Rate** | PR Status filter: Merged / Total submitted | % of PRs that were approved and shipped |
| **Review Rate** | Reviews metric | Avg reviews per PR — code quality gate engagement |
| **Time to Merge** | Time to Merge metric | Faster = cleaner code requiring less rework |
| **Time to Code Review** | Time to Code Review metric | Review responsiveness — team collaboration signal |
| **Added Lines AVG** | Added Lines AVG | Avg lines per PR — correlates with Copilot-generated chunk size |

### PR Quality Score (Simple)

Apply a **+1 / 0 / −1 tier modifier** based on two signals:

| Condition | PR Modifier | Rationale |
|---|---|---|
| PR Merge Rate ≥ 80% AND Reviews ≥ 1 per PR | **+1** (tier upgrade eligible) | Code is shipping and being reviewed — Copilot output is production-quality |
| PR Merge Rate 50–79% OR Reviews < 1 per PR | **0** (no change) | Neutral — insufficient signal or mixed quality |
| PR Merge Rate < 50% | **−1** (tier downgrade eligible) | Code isn't shipping despite high LoC — Copilot output may not be production-ready |

> **Important:** The PR modifier shifts eligibility, not assignment. A Tier B user with +1 becomes *eligible* for Tier A — confirm with T1/T2 signals before promoting. A Tier A user with −1 is flagged for review, not auto-demoted.

### PR Quality — VP ROI Language

> "Of the 76,288 lines of code Copilot helped generate this period, [X]% made it into merged pull requests. Our top performers (Tier A) have a PR merge rate of [X]% — meaning their Copilot-assisted output is consistently shipping to production."

---

## Combined Scoring Matrix

| User | Role Context | Workflow Type (v2) | Tier (Base) | Momentum | PR Modifier | Final Classification |
|---|---|---|---|---|---|---|
| *Mikhail Shnayderman* | Developer | Agent-First | A | ➡️ Stable | +1 | **A** |
| *Amol Salunkhe* | Developer | Agent-First | C | 🚀 Breakout (+3,500%) | TBD | **C↑ → B eligible** |
| *Rahul Walunj* | Research | — | — | — | — | **Research** (not tiered) |
| *Prathmesh Ranadive* | Developer | Hybrid | D | 📈 Rising | TBD | **D↑ — coach on premium** |

---

## Weekly Analysis Checklist (with these enhancements)

1. ☐ Confirm Role Context for any new or changed-role users
2. ☐ Pull Agent Contribution % from Power BI → assign Workflow Type per v2
3. ☐ Calculate Momentum Score for each user (current vs. prior Req Eff)
4. ☐ Pull PR Merge Rate and Reviews from Power BI PR tab → apply PR modifier
5. ☐ Apply base tier (A–E) per v2 workflow-aware benchmarks
6. ☐ Apply Momentum override rules (↑/↓ markers)
7. ☐ Apply PR modifier (eligibility only)
8. ☐ Produce Executive Scorecard with final classifications

---

*This framework builds on github-quick-benchmark-v2.md. All v2 tier definitions and workflow classification rules apply. The Role Context, Momentum Score, and PR Quality Modifier are additive dimensions — they do not replace the base benchmark, they refine it.*
