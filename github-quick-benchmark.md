# 📊 Github Quick Benchmark — Selected Metrics

## 🥇 TIER 1 — Core Signals

| Metric | What It Tells You | Good Looks Like |
|---|---|---|
| **% Code Acceptance** | Are Copilot's suggestions relevant and trusted? | 20–35% |
| **Code Acceptance Count** | Volume of accepted suggestions (pairs with rate for full picture). | Higher = more value. Compare within team. |
| **Agent Adoption** | Are devs advancing beyond basic completions to agent workflows? | Trending upward month-over-month |

## 🥈 TIER 2 — ROI Signals

| Metric | What It Tells You | Good Looks Like |
|---|---|---|
| **Request Efficiency** | Lines of code produced per paid model request. | Higher = better ROI. Set your own baseline. |
| **Premium Requests Count** | Budget consumption of paid model calls. | Watch outliers (1,700+). Always pair with efficiency. |

## 🥉 TIER 3 — Context Signals (Never Standalone)

| Metric | What It Tells You | ⚠️ Caveat |
|---|---|---|
| **Initiated Interactions** | How many prompts did a dev send? | High count may = struggling, not productive |
| **Suggestion Efficiency** | Lines added per generation event. | Custom metric; inflated by agent mode |
| **LoC Suggested** | Lines Copilot offered (accepted or not). | Directional only; varies by IDE |
| **LoC Added** | Lines that actually landed in the editor. | Agent mode can add 2,000+ from one prompt |
| **Code Generation Count** | Total Copilot output events (including rejected). | High generation + low acceptance = poor fit |

## ⚡ Quick Decision Map

| Question | Look At | What Good Looks Like |
|---|---|---|
| Is Copilot useful? | **T1:** % Acceptance + Count | Acceptance 20–35%, Count trending up |
| Are devs advancing? | **T1:** Agent Adoption | Increasing month-over-month |
| Is the spend justified? | **T2:** Request Efficiency + Premium Requests | High efficiency (>10 LoC/request), no outlier spend (watch 1,700+) |
| Why are numbers off? | **T3:** Interactions, LoC, Generation Count | Interactions not excessively high, LoC Added close to LoC Suggested, Generation Count paired with healthy acceptance rate |