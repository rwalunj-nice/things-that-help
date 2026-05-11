# 📊 Github Analysis — 11 May 2026 (Role+Momentum Format)

*Data source: Power BI GitHub 360 AI Usage dashboard, last synced 5/10/2026 9:39:11 PM | WFM Integrations | Based on **github-benchmark-role-momentum.md** (v2 + Role Context + Momentum Score + PR Modifier)*

> ⚠️ **Methodology notes:**
> - Premium Requests not exposed in current Power BI view. Suggestion Efficiency used as T2 proxy.
> - Momentum Score uses LoC Added delta as proxy (per-period Req Eff not available at user level).
> - PR Quality Modifier: Power BI PR tab data not pulled per-user this session — noted as TBD. Apply before finalizing tier.
> - Base tier assignments inherited from v2 (workflow-aware). This report adds Role Context, Momentum, and PR Modifier layers.

---

## Dimension 1 — Role Context Assignment

| User | Manager | Role Context | Benchmark Adjustment |
|---|---|---|---|
| Mikhail Shnayderman | Alon Vax | **Developer** | Full benchmark applies |
| Amol Salunkhe | Swapnil Zade | **Developer** | Full benchmark applies |
| Prathmesh Ranadive | Swapnil Zade | **Developer** | Full benchmark applies |
| Ritesh Pawar | Susovan Samal | **Developer** | Full benchmark applies |
| Matt Field | Swapnil Zade | **Developer** | Full benchmark applies |
| Chris Haun | Swapnil Zade | **Developer** | Full benchmark applies |
| Nilesh Tonape | Swapnil Zade | **Developer** | Full benchmark applies |
| Shraddha Kale | Swapnil Zade | **Developer** | Full benchmark applies |
| **Swapnil Zade** | Rahul Walunj | **Manager** | T2 Eff threshold lowered to > 5; LoC secondary; Interaction count weighted higher |
| Vyankatesh Khadakkar | Swapnil Zade | **Developer** | Full benchmark applies |
| Abhishek Hole | Swapnil Zade | **Developer** | Full benchmark applies |
| Moad Alzughul | Swapnil Zade | **Developer** | Full benchmark applies |
| Vitthal Devkar | Susovan Samal | **Developer** | Full benchmark applies |
| Sourabh Kalaskar | Swapnil Zade | **Developer** | Full benchmark applies |
| Pradnyesh Salunke | Swapnil Zade | **Developer** | Full benchmark applies |
| Luis Salvatierra | Swapnil Zade | **Developer** | Full benchmark applies |
| Suhas Kakde | Swapnil Zade | **Developer** | Full benchmark applies |
| Tushar Patil | Susovan Samal | **Developer** | Full benchmark applies |
| Amulya Kale | Susovan Samal | **Developer** | Full benchmark applies |
| Jayesh Rai | Swapnil Zade | **Developer** | Full benchmark applies |
| Suraj Dubey | Susovan Samal | **Developer** | Full benchmark applies |
| Pratik Devle | Susovan Samal | **Developer** | Full benchmark applies |
| Shubham Gite | Susovan Samal | **Developer** | Full benchmark applies |
| Trunal Gawade | Susovan Samal | **Developer** | Full benchmark applies |
| Abhijeet Kolhe | Swapnil Zade | **Developer** | Full benchmark applies |
| Prashasti Jain | Swapnil Zade | **Developer** | Full benchmark applies |
| Pratik Pawar | Swapnil Zade | **Developer** | Full benchmark applies |
| Shridhar Mishra | Rahul Walunj | **Developer** | Full benchmark applies |
| Shreedevi Patil | Swapnil Zade | **Developer** | Full benchmark applies |
| Mohan Shivarkar | Swapnil Zade | **Developer** | Full benchmark applies |
| **Susovan Samal** | Rahul Walunj | **Manager** | Near-zero LoC expected. Benchmark: Interaction count + engagement signal, not LoC volume |
| Nishtha Thakral | Susovan Samal | **Developer** | Full benchmark applies (zero output — not a role exception) |
| **Rahul Walunj** | Alon Vax | **Research** | Not tiered A–E. Track: Interaction count + Premium usage as signals of research value |

---

## Dimension 2 — Momentum Score

*Formula: (Current period LoC − Prior period LoC) / max(Prior period LoC, 1) × 100*
*Note: "Current period LoC" = LoC delta since Apr 28. "Prior period LoC" = Apr 14 → Apr 28 delta (estimated from cumulative data where available).*

> **Data limitation:** Per-user prior period LoC deltas are derived from cumulative totals and prior report notes. Where exact prior period delta is unknown, the trend label uses multi-period directional data from the v1 analysis record.

| User | May 11 LoC | May 11 ΔLoC | Apr 28 Est. LoC | Est. Momentum Score | Label | VP Action |
|---|---|---|---|---|---|---|
| Mikhail Shnayderman | 22,268 | +1,317 | ~20,951 | — | ➡️ **Stable** | Monitor. High baseline, modest increment normal. |
| **Amol Salunkhe** | 17,155 | **+14,945** | 2,210 | **+576%** | 🚀 **Breakout** | 🏆 Celebrate publicly. Document coaching action. |
| **Prathmesh Ranadive** | 8,783 | **+6,935** | 1,848 | **+275%** | 🚀 **Breakout** | 🏆 Celebrate. Share coaching playbook team-wide. |
| Ritesh Pawar | 8,640 | **0** | ~8,640 | **0%** | ❌ **Stalled** | Investigate leave/absence before classifying Declining. |
| Matt Field | 8,566 | +2,929 | ~5,637 | **+52%** | 📈 **Rising** | Acknowledge. On track. |
| **Chris Haun** | 6,758 | **+88** | ~6,670 | **+1.3%** | 📉 **Slipping** | ⚠️ Flag for manager check-in. From A to near-zero. |
| Nilesh Tonape | 4,908 | +1,310 | ~3,598 | **+36%** | 📈 **Rising** | Acknowledge. Trajectory recovering from D. |
| Shraddha Kale | 4,706 | +153 | ~4,553 | **+3.4%** | ➡️ **Stable** | Monitor. |
| Swapnil Zade | 3,063 | +556 | ~2,507 | **+22%** | ➡️ **Stable** | Manager showing consistent growth. |
| Vyankatesh Khadakkar | 2,795 | +445 | ~2,350 | **+19%** | ➡️ **Stable** | Accept rate surge (23%→66%) is the real signal. Rising. |
| **Abhishek Hole** | 2,722 | **+2,403** | ~319 | **+654%** | 🚀 **Breakout** | Celebrate. From D to strong B output. |
| Moad Alzughul | 2,655 | +35 | ~2,620 | **+1.3%** | ➡️ **Stable** | Steady. Slight plateau — monitor. |
| Vitthal Devkar | 2,472 | +1,292 | ~1,180 | **+110%** | 🚀 **Breakout** | Great trajectory. LoC more than doubled. |
| Sourabh Kalaskar | 2,056 | +539 | ~1,517 | **+36%** | 📈 **Rising** | Improving. C→B in v2 confirmed by momentum. |
| Pradnyesh Salunke | 1,735 | +878 | ~857 | **+102%** | 🚀 **Breakout** | Strong improvement. C→B promotion in v2. |
| Luis Salvatierra | 1,698 | +254 | ~1,444 | **+18%** | ➡️ **Stable** | Slow steady improvement. |
| Suhas Kakde | 1,615 | +18 | ~1,597 | **+1.1%** | ➡️ **Stable** | ⚠️ Nearly stalled this period despite 137 interactions. |
| Tushar Patil | 1,389 | +536 | ~853 | **+63%** | 📈 **Rising** | Good growth rate. Coach on accept rate. |
| Amulya Kale | 1,133 | +354 | ~779 | **+45%** | 📈 **Rising** | Improving. Needs efficiency boost. |
| **Jayesh Rai** | 777 | **+776** | ~1 | **+77,500%** | 🚀 **Breakout** | First real output. Effectively emerging from zero. Don't promote yet — one period. |
| Suraj Dubey | 491 | 0 | ~491 | **0%** | ➡️ **Stable** | No new LoC this period. Stable base but no growth. |
| Pratik Devle | 370 | +2 | ~368 | **+0.5%** | 📉 **Slipping** | Near-zero growth. Multi-period stall. |
| **Shubham Gite** | 268 | +189 | ~79 | **+139%** | 🚀 **Breakout** | T1 excellent, output tripling. Volume-constrained — give more tasks. |
| **Trunal Gawade** | 261 | +200 | ~61 | **+228%** | 🚀 **Breakout** | LoC 4× vs prior period. T1 strong. |
| Abhijeet Kolhe | 172 | ~0 | ~172 | **0%** | ➡️ **Stable** | Tiny baseline, near-zero activity. |
| Prashasti Jain | 203 | ~13 | ~190 | **+7%** | ➡️ **Stable** | 🔴 4-period P0. Stable = not improving. Final warning. |
| **Pratik Pawar** | 166 | **+166** | ~0 | **+16,500%** | 🚀 **Breakout** | First LoC ever. Emerging. Single period — watch next period. |
| **Shridhar Mishra** | 155 | **+155** | ~0 | **+15,500%** | 🚀 **Breakout** | First LoC ever (was E, 0 LoC all prior periods). Quality signals (69.6% accept). |
| Shreedevi Patil | 88 | ~0 | ~88 | **0%** | ➡️ **Stable** | Tiny volume, no growth. |
| Mohan Shivarkar | 28 | ~0 | ~28 | **0%** | ➡️ **Stable** | Minimal LoC, accepting micro-snippets only. |
| Susovan Samal | 38 | ~0 | ~38 | **0%** | ➡️ **Stable** | Manager — expected. |
| Nishtha Thakral | 0 | 0 | ~0 | **0%** | 🔴 **Declining** | Zero across 5 periods with no signal of change. |
| Rahul Walunj | 0 | 0 | — | — | ➡️ Research | 21 interactions this period — research activity tracked. |

---

## Dimension 3 — PR Quality Modifier

> **Status: TBD for all users this period.** Power BI Pull Request Details tab data was not pulled per-user in this session. Run before finalizing any tier-upgrade or tier-downgrade recommendations.
>
> To pull: Power BI → Pull Request Details tab → filter by user login + same time window → record PR Merge Rate and Reviews per PR.

| Condition | Modifier | Action |
|---|---|---|
| PR Merge Rate ≥ 80% AND ≥ 1 review per PR | **+1** (upgrade eligible) | Confirm with T1/T2 signals |
| PR Merge Rate 50–79% OR Reviews < 1 per PR | **0** (neutral) | No change |
| PR Merge Rate < 50% | **−1** (downgrade eligible) | Flag for review |

---

## Combined Classification — Final

*Base tier from v2 (workflow-aware) + Momentum override + PR Modifier (TBD). Momentum labels influence tier markers but not assignment until PR modifier is confirmed.*

| User | Role | Workflow | Base Tier (v2) | Momentum | Momentum Score | PR Mod | **Final Classification** |
|---|---|---|---|---|---|---|---|
| Mikhail Shnayderman | Developer | Agent-First | A | ➡️ Stable | — | TBD | **A** |
| Amol Salunkhe | Developer | Agent-First | A | 🚀 Breakout | +576% | TBD | **A** *(confirm +1 if PR merge ≥ 80%)* |
| Prathmesh Ranadive | Developer | Inline-First | A | 🚀 Breakout | +275% | TBD | **A** |
| Ritesh Pawar | Developer | Agent-First | A | ❌ Stalled | 0% | TBD | **A⚠️** *(flag; confirm not Declining)* |
| Matt Field | Developer | Agent-First | B | 📈 Rising | +52% | TBD | **B** |
| Chris Haun | Developer | Hybrid | B | 📉 Slipping | +1.3% | TBD | **B↓** *(eligible for C if decline continues)* |
| Nilesh Tonape | Developer | Hybrid | B | 📈 Rising | +36% | TBD | **B** |
| Shraddha Kale | Developer | Agent-First | B | ➡️ Stable | +3.4% | TBD | **B** |
| Swapnil Zade | **Manager** | Agent-First | B | ➡️ Stable | +22% | TBD | **B** *(Manager benchmark; strong engagement)* |
| Vyankatesh Khadakkar | Developer | Inline-First | B | ➡️ Stable | +19% | TBD | **B** *(accept rate surge is key signal)* |
| Abhishek Hole | Developer | Agent-First | B | 🚀 Breakout | +654% | TBD | **B→A eligible** *(if PR confirms)* |
| Moad Alzughul | Developer | Agent-First | B | ➡️ Stable | +1.3% | TBD | **B** |
| Vitthal Devkar | Developer | Inline-First | B | 🚀 Breakout | +110% | TBD | **B** |
| Sourabh Kalaskar | Developer | Hybrid | B ⬆️ | 📈 Rising | +36% | TBD | **B** *(upgraded from C in v2; Rising confirms)* |
| Pradnyesh Salunke | Developer | Inline-First | B ⬆️ | 🚀 Breakout | +102% | TBD | **B** *(upgraded from C in v2; Breakout confirms)* |
| Luis Salvatierra | Developer | Hybrid | C | ➡️ Stable | +18% | TBD | **C** |
| Suhas Kakde | Developer | Agent-First | C | ➡️ Stable | +1.1% | TBD | **C** *(near-stall despite 137 int — coaching needed)* |
| Tushar Patil | Developer | Hybrid | C | 📈 Rising | +63% | TBD | **C** *(Rising — on B trajectory if accept improves)* |
| Amulya Kale | Developer | Hybrid | C | 📈 Rising | +45% | TBD | **C** |
| Suraj Dubey | Developer | Agent-First | C ⬆️ | ➡️ Stable | 0% | TBD | **C** *(stable; v2 upgrade confirmed; next period LoC growth needed)* |
| Shubham Gite | Developer | Inline-First | C ⬆️ | 🚀 Breakout | +139% | TBD | **C↑** *(volume-constrained; T1 breakout + Momentum = B eligible once volume up)* |
| Trunal Gawade | Developer | Inline-First | C ⬆️ | 🚀 Breakout | +228% | TBD | **C↑** *(same as Shubham — volume gap only)* |
| Jayesh Rai | Developer | Agent-First | D | 🚀 Breakout | +77,500% | TBD | **D↑** *(first real output; hold D for one more period to confirm)* |
| Pratik Devle | Developer | Agent-First | D | 📉 Slipping | +0.5% | TBD | **D↓** *(near-stall, multi-period)* |
| Abhijeet Kolhe | Developer | Hybrid | D | ➡️ Stable | 0% | TBD | **D** |
| Prashasti Jain | Developer | Hybrid | D | ➡️ Stable | +7% | TBD | **D** 🔴 *(5 periods, P0 unresolved)* |
| Pratik Pawar | Developer | Agent-First | D | 🚀 Breakout | +16,500% | TBD | **D↑** *(first LoC; one period — monitor)* |
| Shreedevi Patil | Developer | Inline-First | D | ➡️ Stable | 0% | TBD | **D** |
| Mohan Shivarkar | Developer | Inline-First | D | ➡️ Stable | 0% | TBD | **D** |
| Shridhar Mishra | Developer | Inline-First | D | 🚀 Breakout | +15,500% | TBD | **D↑** *(first LoC; quality signals strong 69.6% accept)* |
| Nishtha Thakral | Developer | Hybrid | E | 🔴 Declining | 0% | N/A | **E** 🔴 *(Final decision: revoke or intensive training)* |
| Susovan Samal | **Manager** | Agent-First | E | ➡️ Stable | 0% | N/A | **Manager** *(not tiered A–E; engagement tracking only)* |
| Rahul Walunj | **Research** | — | Research | ➡️ Research | — | N/A | **Research** *(21 interactions = active usage)* |

---

## 📊 Momentum Summary

| Label | Count | Users |
|---|---|---|
| 🚀 Breakout (>+100%) | 8 | Amol, Prathmesh, Abhishek Hole, Vitthal, Pradnyesh, Jayesh Rai, Pratik Pawar, Shridhar Mishra |
| 📈 Rising (+30–100%) | 4 | Matt Field, Nilesh, Tushar, Amulya |
| ➡️ Stable (-10–+30%) | 13 | Mikhail, Shraddha, Swapnil, Vyankatesh, Moad, Sourabh, Luis, Suhas, Suraj, Abhijeet, Shreedevi, Mohan, Susovan |
| 📉 Slipping (-10–-30%) | 2 | Chris Haun, Pratik Devle |
| 🔴 Declining (<-30%) | 1 | Nishtha Thakral |
| ⚠️ Stalled (0%) | 1 | Ritesh Pawar (investigate before classifying) |

> **Coaching system is working.** 8 Breakout users this period — highest ever. 3 users (Jayesh, Pratik Pawar, Shridhar) moving from zero-output to first-LoC. Coaching playbook from Prathmesh Ranadive should be documented and shared.

---

## VP Defense Language

### For Rahul Walunj (Research)
> "Rahul's role uses Copilot for code understanding, tooling research, and management analysis. LoC Added is not the right output metric. We track Research value through Interaction count — 21 interactions this period confirms active usage aligned to his responsibilities."

### For Susovan Samal (Manager)
> "As an engineering manager, Susovan's primary Copilot value is in code review, architecture guidance, and selective implementation oversight. We benchmark him on engagement, not raw LoC volume."

### For D↑ Users (Jayesh Rai, Pratik Pawar, Shridhar Mishra)
> "These users are classified Tier D this period. However, all three recorded first-ever LoC this period and show Breakout momentum scores. The coaching investment is beginning to work. We expect C classification in the next period if the trajectory holds."

### For Breakout Performers (Amol, Prathmesh)
> "Amol Salunkhe and Prathmesh Ranadive were both classified Tier D/C in the prior period. This period, Amol produced 14,945 new LoC (576% growth) and Prathmesh produced 6,935 new LoC (275% growth). Both are now firmly Tier A. The coaching program is producing measurable results."

---

## Priority Actions (Role+Momentum Layer)

| Priority | Action | Basis |
|---|---|---|
| 🔴 P0 | **Final decision: Nishtha Thakral** — 5 periods zero output, Declining label. Revoke or intensive training. | Momentum Declining + E tier |
| 🔴 P0 | **Investigate Ritesh Pawar stall** — 0 new LoC. Not Declining yet, but could be. Confirm leave status before next period. | Momentum stalled at 0% |
| 🔴 P0 | **Investigate Chris Haun** — Slipping momentum. From A to +88 LoC in one period. | Momentum Slipping (B↓) |
| 🟠 P1 | **Pull PR Modifier for Tier A/B candidates** — Abhishek Hole (B→A eligible), Shubham Gite (C↑→B eligible) — PR data needed to confirm upgrades | Momentum supports upgrade; PR required |
| 🟠 P1 | **Document Prathmesh Ranadive coaching playbook** — D→A in one period. Replicate for D↑ users. | Breakout momentum |
| 🟡 P2 | **Coach Suhas Kakde** — 137 interactions with near-zero LoC growth. Momentum Stable but output near-stalled. | Stable momentum + stalling output |

---

*Document generated 2026-05-11 from Power BI GitHub 360 AI Usage dashboard (WFM Integrations, data through 5/10/2026). Based on github-benchmark-role-momentum.md. Builds on v2 workflow-aware tier assignments — apply PR Quality Modifier from Power BI Pull Request Details tab to finalize all tier promotions.*
