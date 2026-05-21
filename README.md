# Things That Help

A collection of resources, frameworks, and guides for measuring and maximizing the impact of **GitHub Copilot** across your organization.

---

## 📁 What's Inside

| File / Folder | Description |
|---|---|
| [GitHub Quick Benchmark (v1)](githubaianalysis/github-quick-benchmark.md) | The original 3-tier metric framework — Core, ROI, and Context signals for evaluating Copilot effectiveness. |
| [GitHub Quick Benchmark v2](githubaianalysis/github-quick-benchmark-v2.md) | Workflow-aware evolution of v1 — classifies users by Agent Contribution % before applying benchmarks. |
| [Role Context + Momentum](githubaianalysis/github-benchmark-role-momentum.md) | Adds Role Context (Developer/Manager/Lead/Research), Momentum Score (improvement velocity), and PR Quality Modifier on top of v2. |
| [CRQC Framework](githubaianalysis/github-benchmark-CRQC.md) | Full 4-pillar redesign — Core, ROI, Quality, Context — with explicit scoring (0–9) and maximum VP defensibility. |
| [Analysis Reports](githubaianalysis/aianalysisreport/) | Weekly GitHub AI usage analysis reports with detailed breakdowns of Copilot adoption, efficiency, and recommendations. |

---

### 📈 AI Analysis Reports

#### April 2026

| Report | Date | Variant |
|---|---|---|
| [github-ai-analysis-20-april-2026.md](githubaianalysis/aianalysisreport/github-ai-analysis-20-april-2026.md) | April 20, 2026 | Standard |
| [github-ai-analysis-23-april-2026.md](githubaianalysis/aianalysisreport/github-ai-analysis-23-april-2026.md) | April 23, 2026 | Standard |
| [github-ai-analysis-28-april-2026.md](githubaianalysis/aianalysisreport/github-ai-analysis-28-april-2026.md) | April 28, 2026 | Standard |

#### May 2026

| Report | Date | Variant |
|---|---|---|
| [github-ai-analysis-11-may-2026.md](githubaianalysis/aianalysisreport/github-ai-analysis-11-may-2026.md) | May 11, 2026 | Standard (v1) |
| [github-ai-analysis-11-may-2026-v2.md](githubaianalysis/aianalysisreport/github-ai-analysis-11-may-2026-v2.md) | May 11, 2026 | v2 (Workflow-Aware) |
| [github-ai-analysis-11-may-2026-role-momentum.md](githubaianalysis/aianalysisreport/github-ai-analysis-11-may-2026-role-momentum.md) | May 11, 2026 | Role + Momentum |
| [github-ai-analysis-11-may-2026-CRQC.md](githubaianalysis/aianalysisreport/github-ai-analysis-11-may-2026-CRQC.md) | May 11, 2026 | CRQC |
| [github-ai-analysis-18-may-2026.md](githubaianalysis/aianalysisreport/github-ai-analysis-18-may-2026.md) | May 18, 2026 | Standard (v1) |
| [github-ai-analysis-18-may-2026-v2.md](githubaianalysis/aianalysisreport/github-ai-analysis-18-may-2026-v2.md) | May 18, 2026 | v2 (Workflow-Aware) |
| [github-ai-analysis-18-may-2026-role-momentum.md](githubaianalysis/aianalysisreport/github-ai-analysis-18-may-2026-role-momentum.md) | May 18, 2026 | Role + Momentum |
| [github-ai-analysis-18-may-2026-CRQC.md](githubaianalysis/aianalysisreport/github-ai-analysis-18-may-2026-CRQC.md) | May 18, 2026 | CRQC |
| [github-ai-analysis-18may-lowusers.md](githubaianalysis/aianalysisreport/github-ai-analysis-18may-lowusers.md) | May 18, 2026 | Low Users Focus |

---

## 🚀 Getting Started

1. **Pick the right framework for your needs:**
   - *Quick start or small team?* → [`github-quick-benchmark.md`](githubaianalysis/github-quick-benchmark.md) (v1)
   - *Team uses agent mode heavily?* → [`github-quick-benchmark-v2.md`](githubaianalysis/github-quick-benchmark-v2.md) (workflow-aware)
   - *Need coaching plans & improvement tracking?* → [`github-benchmark-role-momentum.md`](githubaianalysis/github-benchmark-role-momentum.md)
   - *Presenting to VP R&D / need maximum defensibility?* → [`github-benchmark-CRQC.md`](githubaianalysis/github-benchmark-CRQC.md)
2. **Focus on Tier 1 first** — Regardless of framework version, start with Core Signals before diving into ROI or context metrics.
3. **Set baselines** — Use the "Good Looks Like" column to establish targets, then track trends over time within your team.
4. **Review the latest analysis** — Check the most recent report in [`githubaianalysis/aianalysisreport/`](githubaianalysis/aianalysisreport/) for current adoption trends and actionable recommendations.

---

## 📊 Framework Evolution

The benchmark system has evolved through four iterations, each adding capabilities:

```
v1 (Quick Benchmark)  →  v2 (Workflow-Aware)  →  Role + Momentum  →  CRQC
```

| Capability | v1 | v2 | Role+Momentum | CRQC |
|---|:---:|:---:|:---:|:---:|
| Agent-mode handling | ❌ | ✅ | ✅ | ✅ |
| Code quality signal (PR data) | ❌ | ❌ | ✅ | ✅ |
| Role-based exceptions | ❌ | ❌ | ✅ | ✅ |
| Improvement velocity tracking | ❌ | ❌ | ✅ | ✅ |
| VP defensibility | Medium | Medium-High | High | Highest |
| Weekly analysis effort | Low | Low | Medium | Medium-High |

> **Recommendation:** Start with **v1** to build familiarity. Graduate to **v2** once your team has agent-mode users. Adopt **CRQC** when you need scored, auditable tier assignments for leadership reporting.

---

## 📊 Metric Tiers at a Glance

All frameworks organize Copilot metrics into signal tiers:

- **🥇 Tier 1 — Core Signals**: % Code Acceptance, Code Acceptance Count, and Agent Adoption. These tell you whether Copilot is relevant, trusted, and evolving in usage.
- **🥈 Tier 2 — ROI Signals**: Request Efficiency (LoC per premium request; >10 is good) and Premium Requests Count (outlier threshold: 1,700+). These help justify spend and catch budget outliers.
- **🥉 Tier 3 — Context Signals**: Initiated Interactions, Suggestion Efficiency, Lines of Code metrics, and Code Generation Count. Use these to diagnose anomalies — never as standalone success metrics.

> **Tip:** Use the ⚡ Quick Decision Map in any benchmark file to jump straight to the metrics that answer your specific question.

---

## 📋 Analysis Report Structure

Each weekly report follows this structure:

1. Header — team size, exclusions, new users, analysis period
2. What Changed — re-tiered users vs. prior week
3. Team Overview — aggregated metrics
4. Excluded / New Users tables
5. Combined Dataset — user-level metric table
6. User tiers: **A** (top) → **B** (solid) → **C** (moderate) → **D** (low efficiency) → **E** (zero/near-zero output)
7. Executive Scorecard + 80/20 analysis + Top budget drains
8. Multi-period trend comparison
9. Appendix — team-specific breakdowns

---

## 🤝 Contributing

Have additional metrics, dashboards, or Copilot adoption playbooks? Contributions are welcome — open a PR or file an issue to start a discussion.

---

## 📄 License

This project is provided as-is for internal and community use. See individual files for any specific licensing details.
