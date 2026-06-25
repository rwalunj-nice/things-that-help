---
description: "Run GitHub Copilot usage analysis — collects inputs (VP, Product, date, team) then produces v1, v2, Role+Momentum, and CRQC analysis files pushed to copilot-projects repo"
---

# GitHub Stats Analysis

## Overview

This skill runs a structured GitHub Copilot usage analysis for a given team and period. It guides you through data collection, then produces four analysis files covering every evaluation framework: standard tier, workflow-aware tier, role/momentum, and the CRQC 4-pillar scorecard.

**Output**: 4 markdown files committed and pushed to `https://github.com/rwalunj-nice/copilot-projects/tree/main/githubaianalysis`

**Working directory**: `C:\Users\rwalunj\OneDrive - Nice Systems Ltd\Rahul\INT\Notes\GH360 Review\copilot-projects`

**Framework reference files** (in the repo root):
- `github-quick-benchmark.md` — v1 standard
- `github-benchmark-v2.md` — v2 workflow-aware
- `github-benchmark-role-momentum.md` — Role Context + Momentum
- `github-benchmark-CRQC.md` — CRQC 4-pillar

---

## Phase 1 — Collect Inputs (One at a Time)

Ask these questions one at a time. Do NOT ask multiple at once. Wait for the user's answer before asking the next.

1. **R&D VP**: "Who is the R&D VP for this team? (e.g., Barak)"
2. **Product**: "What is the Product name as it appears in Power BI? (e.g., WFM Integrations)"
3. **Usage date**: "What is the analysis date? (e.g., May 11, 2026) — this becomes the file name and report header"
4. **Team** *(optional)*: "Which team should be included? Press Enter to include all teams under the product, or name a specific sub-team."

Once all inputs are collected, confirm the summary before proceeding:
> "Got it. Analysing: **[Product]** | Team: **[Team or All]** | Date: **[Usage date]** | VP: **[R&D VP]**. Ready to pull Power BI data — let's go."

---

## Phase 2 — Data Extraction from Power BI

### Step 1: AI Usage data for USER METRICS

In Power BI GitHub 360 dashboard → **AI Usage tab**:
- Filter: Product = `<product>`, Date = `<usage_date>`, Team = `<team or All>`
- Copy the full **USER METRICS table** with these columns:

| User | Employee name | Direct manager name | Int | LoC Added | LoC Sugg | Code Accept | Code Gen | % Accept | Sugg Eff | Prem Req | Req Eff | Agent Contribution % |

Ask the user to paste or screenshot the table. Capture all rows, including users with zero activity. Once all the data is captured, get it confirmed on screen before proceeding. 

### Step 2: AI Usage data for PREMIUM REQUESTS BY USER

In Power BI GitHub 360 dashboard → **AI Usage tab**:
- Filter: Product = `<product>`, Date = `<usage_date>`, Team = `<team or All>`
- Copy the full **PREMIUM REQUESTS BY USER table** with these columns:

| User | Employee name | Direct manager name | LoC Added | Premium requests | Req Eff |

Ask the user to paste or screenshot the table. Capture all rows, including users with zero activity. Once all the data is captured, get it confirmed on screen before proceeding. 

### Step 3: PR Details data

In Power BI GitHub 360 dashboard → **Pull Request Details tab**:
- Filter: Product = `<product>`, Branch = **All** (not just main), Status = Merged, Date range = same period
- Capture: User login, PRs merged count, Reviews count, Average time to merge

> **Note**: "Branch = All" captures feature branch PRs. "Branch = Main" only catches direct-to-main merges, which applies to only ~8 users. Always use All for Q scoring.

---

## Phase 3 — Run All 4 Analyses

Process all frameworks using the data collected. Read the framework reference files in the repo to apply exact scoring rules. Run frameworks in this order and write each file before moving to the next.

### Framework 1 — v1 Standard (`github-ai-analysis-<date>.md`)

Uses `github-quick-benchmark.md` rules. Classify each user Tier A–E using:
- **Tier 1 (Core)**: % Code Acceptance (target 20–35%) + Code Acceptance Count
- **Tier 2 (ROI)**: Request Efficiency (LoC Added ÷ Prem Req; >10 = good) + Premium Requests volume
- **Tier 3 (Context)**: Initiated Interactions, Suggestion Efficiency, LoC Suggested vs. Added, Code Generation Count — diagnostic only, never sole basis for tier

**⚠ Agent-First exception**: Do NOT use % Accept for users with Agent Contribution % ≥70%. Their accept rate is near-zero by design. Evaluate these users on LoC Added and Request Efficiency instead.

Include: team overview, tier tables, executive scorecard, 80/20 analysis (what % of output comes from top 20% users), top budget drains.

### Framework 2 — v2 Workflow-Aware (`github-ai-analysis-<date>-v2.md`)

Uses `github-benchmark-v2.md` rules. First classify each user:

| Agent Contribution % | Workflow Type |
|---|---|
| ≥ 70% | Agent-First |
| 30–69% | Hybrid |
| < 30% | Inline-First |

Then apply workflow-specific benchmarks (see benchmark file). Key tier changes vs v1 are worth calling out explicitly in a "What Changed vs v1" section.

### Framework 3 — Role + Momentum (`github-ai-analysis-<date>-role-momentum.md`)

Uses `github-benchmark-role-momentum.md` rules.

**Role assignment** (verify with user if unsure):
- Developer: default for all ICs
- Manager: Swapnil Zade, Susovan Samal (and any new managers identified)
- Lead: senior ICs with review responsibilities
- Research: Rahul Walunj (excluded from tier — tracked separately)

**Momentum Score** (requires prior period data):
```
Momentum = (Current LoC − Prior LoC) / max(Prior LoC, 1) × 100
```
Labels: Breakout (>+100%), Rising (+25–100%), Stable (−25 to +25%), Slipping (−25 to −60%), Declining (< −60%)

**PR Quality Modifier**: apply ±1 to tier based on PR merge rate:
- ≥80% merge rate: +1
- <50% merge rate: −1
- Between: 0

### Framework 4 — CRQC (`github-ai-analysis-<date>-CRQC.md`)

Uses `github-benchmark-CRQC.md` rules. Score each user across 3 pillars (0–3 each), total 0–9 → Tier A–E.

**C (Core)**: Assign Workflow Type first, then apply workflow-specific Core scoring rules from the benchmark file.

**R (ROI)**: Universal — same for all workflow types:
- >20 LoC/request → 3 pts
- 10–20 → 2 pts
- 5–10 → 1 pt
- <5 → 0 pts
- Lean spend (≤500 requests): +1 bonus
- Outlier spend (>1,700 requests): −1 penalty

**Q (Quality)**: Sourced from PR Details tab.
- PR Merge Rate ≥80% → 2 pts; 50–79% → 1 pt; <50% → 0 pts
- Reviews ≥1 per PR → +1 pt
- Avg time to merge ≤3 days → +1 bonus (cap Q at 3)
- Users with no main-branch PR data but working on feature branches: mark **Q=FB** (Feature Branch — not captured in filter, not Q=0)
- Users with confirmed zero PR activity: Q=0

**Override rules**:
- Q=0 → Cannot be Tier A
- R=0 AND Premium >500 → Cannot be above Tier C
- Momentum >+100% → eligible for one-tier promotion
- Research role → excluded, reported separately

**Context pillar** (diagnostic only, no score impact):
- Very high Initiated Interactions + low Core = user struggling
- Large LoC Suggested vs. LoC Added gap in Inline-First = low acceptance
- High Code Generation + low C score = volume without value

---

## Phase 4 — Write Output Files

### File naming convention
```
github-ai-analysis-<DD>-<month>-<year>.md           ← v1
github-ai-analysis-<DD>-<month>-<year>-v2.md
github-ai-analysis-<DD>-<month>-<year>-role-momentum.md
github-ai-analysis-<DD>-<month>-<year>-CRQC.md
```
Example for May 11, 2026: `github-ai-analysis-11-may-2026.md`

Write all 4 files to: `copilot-projects/githubaianalysis/`

### File structure (each file)
1. Header: product, team, R&D VP, analysis date, data sync date, total users, exclusions
2. What Changed (vs prior period, if known)
3. Team Overview (aggregated totals)
4. Excluded / New Users
5. Per-user metric table
6. Tier groupings with user cards (metrics + narrative per user)
7. Executive Scorecard + 80/20 analysis
8. Multi-period trend (if prior data available)

---

## Phase 5 — Commit and Push

```powershell
cd "C:\Users\rwalunj\OneDrive - Nice Systems Ltd\Rahul\INT\Notes\GH360 Review\copilot-projects"
git add githubaianalysis/github-ai-analysis-<date>.md
git add githubaianalysis/github-ai-analysis-<date>-v2.md
git add githubaianalysis/github-ai-analysis-<date>-role-momentum.md
git add githubaianalysis/github-ai-analysis-<date>-CRQC.md
git commit -m "Add GitHub Copilot analysis - <date> (<product>)"
git push origin main
```

Confirm push succeeded and share the GitHub URL for the analysis folder.

---

## Key Rules — Always Apply

| Rule | Detail |
|---|---|
| Agent-First users: ignore % Accept | Agent mode = ~0% accept by design. Use LoC Added + Req Eff instead |
| Q=FB notation | Feature branch users with no captured main-branch PRs → Q=FB, not Q=0 |
| Research role | Excluded from all tier scoring. Tracked separately: Interaction count + Premium only |
| Momentum formula | `(Current LoC − Prior LoC) / max(Prior LoC, 1) × 100` |
| Time to merge bonus | Only if avg ≤3 days. Most teams will NOT qualify — do not assume the bonus |
| copilotshree identity | Verify via GitHub Users Mapping tab in Power BI — likely Shreedevi Patil but unconfirmed |
| Branch = All for Q | Always use "Branch = All" in PR Details filter to capture feature branch work |
