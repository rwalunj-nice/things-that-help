# Analysis Report Structure

## Standard 9-Section Template

Every weekly analysis report follows this structure:

### 1. Header
- Team size (total users)
- Exclusions (service accounts, inactive users)
- New users (first-time in dataset)
- Analysis period (date range or checkpoint)

### 2. What Changed
- Re-tiered users vs. prior week
- Movement between tiers (A↑, B↓, etc.)
- New additions to tier system

### 3. Team Overview
- Aggregated metrics across all active users
- Trend comparison vs. previous period

### 4. Excluded / New Users Tables
- Excluded Users: list with exclusion reason
- New Users: list with initial metrics

### 5. Combined Dataset
User-level metric table with columns:
- **Int**: Initiated Interactions
- **LoC Added**: Lines of code that landed in editor
- **LoC Sugg**: Lines Copilot suggested (accepted or not)
- **Code Accept**: Count of accepted suggestions
- **Code Gen**: Total Copilot output events
- **% Accept**: Code acceptance rate
- **Sugg Eff**: Suggestion Efficiency (LoC Added / Code Gen)
- **Prem Req**: Premium Requests consumed
- **Req Eff**: Request Efficiency (LoC Added / Prem Req)

### 6. User Tiers
- **A (Top)**: Highest efficiency and acceptance
- **B (Solid)**: Strong performance
- **C (Moderate)**: Adequate performance
- **D (Low Efficiency)**: Below targets
- **E (Zero/Near-Zero)**: Minimal or no output

### 7. Executive Scorecard
- 80/20 analysis (top 20% of users generating 80% of value)
- Top budget drains (outlier premium request users)
- Tier distribution summary

### 8. Multi-Period Trend Comparison
- Week-over-week or checkpoint-to-checkpoint deltas
- Pattern classification (improving, stable, declining)

### 9. Appendix
- Team-specific breakdowns (if applicable)
- Methodology notes
- Data source references

## Report Naming Convention
`githubaianalysis/aianalysisreport/github-ai-analysis-<DD>-<month>-<year>.md`

Examples:
- `github-ai-analysis-3-june-2026.md`
- `github-ai-analysis-18-may-2026-v2.md` (v2 variant)
- `github-ai-analysis-11-may-2026-CRQC.md` (CRQC variant)

## Multi-Period Reports
Format: `github-ai-analysis-v2-<date>.md`
- Track checkpoint-to-checkpoint progression
- Include window deltas and daily rates
- Pattern classification across periods

## README Update Process
After creating a new report:
1. Add entry to appropriate month section in README.md
2. Include date and variant type (Standard, v2, Role+Momentum, CRQC)
3. Maintain chronological order within each month
