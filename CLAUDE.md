# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **documentation-only repository** — no build system, tests, or runnable code. It contains:

- A reusable metric framework for evaluating GitHub Copilot adoption across an organization
- Weekly AI usage analysis reports comparing individual and team-level Copilot performance

## Key Files

| File | Role |
|---|---|
| `github-quick-benchmark.md` | The canonical 3-tier metric framework — start here to understand the scoring system |
| `githubaianalysis/` | Weekly analysis reports (naming pattern: `github-ai-analysis-<date>.md`) |
| `README.md` | Navigation and onboarding overview |

## Metric Framework (3-Tier System)

Analysis reports classify users using this framework from `github-quick-benchmark.md`:

- **Tier 1 — Core Signals**: % Code Acceptance (target 20–35%), Code Acceptance Count, Agent Adoption
- **Tier 2 — ROI Signals**: Request Efficiency (LoC per premium request; >10 is good), Premium Requests Count (outlier threshold: 1,700+)
- **Tier 3 — Context Signals**: Initiated Interactions, Suggestion Efficiency, LoC Suggested/Added, Code Generation Count — always paired with Tier 1/2, never used standalone

## Analysis Report Structure

Each weekly report in `githubaianalysis/` follows this structure:
1. Header: team size, exclusions, new users, analysis period
2. What Changed (re-tiered users vs. prior week)
3. Team Overview (aggregated metrics)
4. Excluded / New Users tables
5. Combined Dataset (user-level metric table)
6. User tiers: **A** (top), **B** (solid), **C** (moderate), **D** (low efficiency), **E** (zero/near-zero output)
7. Executive Scorecard + 80/20 analysis + Top budget drains
8. Multi-period trend comparison
9. Appendix: team-specific breakdowns

## Columns in the Per-User Dataset

| Column | Meaning |
|---|---|
| Int | Initiated Interactions |
| LoC Added | Lines of code that landed in the editor |
| LoC Sugg | Lines Copilot suggested (accepted or not) |
| Code Accept | Count of accepted suggestions |
| Code Gen | Total Copilot output events |
| % Accept | Code acceptance rate |
| Sugg Eff | Suggestion Efficiency (LoC Added / Code Gen) |
| Prem Req | Premium Requests consumed |
| Req Eff | Request Efficiency (LoC Added / Prem Req) |

## Adding a New Analysis Report

1. Name the file `githubaianalysis/github-ai-analysis-<DD>-<month>-<year>.md`
2. Follow the section structure described above
3. Update `README.md` to add the new report to the AI Analysis Reports table
4. Compare against the previous week's report for the "What Changed" section
