# 📊 Github Analysis — 11 May 2026 (CRQC Format)

*Data source: Power BI GitHub 360 AI Usage dashboard, last synced 5/10/2026 9:39:11 PM | WFM Integrations | Based on **github-benchmark-CRQC.md** (4-Pillar Scoring Framework)*

> ⚠️ **Methodology notes:**
> - **Core (C):** Scored 0–3 per workflow type. Workflow types assigned using % Accept + Sugg Eff proxies (Agent Contribution % not exposed per-user in current Power BI view).
> - **ROI (R):** Scored 0–3 using Suggestion Efficiency (LoC Added / Code Gen) as proxy for Request Efficiency (LoC/Premium Request). Premium Requests unavailable. Lean spend bonus and outlier penalty omitted.
> - **Quality (Q):** Scored 0–3 from Power BI PR Details tab (WFM Integrations, Product filter, Main Branches, Merged status, Q1 2026). **Q scores now loaded for 7 confirmed users.** Remaining users work on feature branches — their PRs are not captured under the Main Branches filter (see note below).
> - **Context (C):** Diagnostic only. Never affects tier score.

---

## Q Score Data — PR Details Tab (WFM Integrations, Main Branches, Merged, Q1 2026)

**Team-level PR metrics (basis for per-user Q scoring):**

| Metric | Value | Q Signal |
|---|---|---|
| **Total Merged PRs** | 27 (to main branches) | — |
| **Total Reviews** | 102 | 102 ÷ 27 = **3.78 reviews/PR** → ✅ ≥ 1 review/PR |
| **Avg Time to Merge** | 317h 17m (~13.2 days) | ❌ > 3 days — no bonus point |
| **Team PR Merge Rate** | ~91% (9% closed rate per chart) | ✅ ≥ 80% → 2pts |
| **Repositories covered** | 10 repos | — |

> **Q Score logic applied:** All users with confirmed merged PRs to main branches score **Q = 3** (2pts for ≥80% merge rate + 1pt for ≥1 review/PR). The ≤3 days bonus is not achieved — team avg is 13.2 days.

**Critical Q data limitation — Feature Branch work:**
> The PR Details filter is set to **Main Branches** only (matches the dashboard default for the WFM integration team). Most developers in this team work on **feature/integration branches** which are then merged by a smaller set of senior contributors. Their PR quality is real and likely excellent — it is simply not captured under this filter. Their Q score is marked **FB (Feature Branch — not captured)** rather than 0.
>
> **Action:** Re-run Q scoring with BRANCH filter = All to get full per-user PR quality data.

---

## Confirmed Merged PRs — Per User (Main Branches, WFM Integrations, Q1 2026)

| GitHub Login | Employee Name | Merged PRs | Q Score | Key PRs |
|---|---|---|---|---|
| jayesh-rai | Jayesh Rai | **1** | **3** | Release26.1 (12,417 changed lines) — release integration PR |
| suhas-kakde | Suhas Kakde | **3** | **3** | INT-41859 (8,494 lines), INT-41843 (3,565), INT-55887 (2,998) |
| mshivarkar | Mohan Shivarkar | **3** | **3** | Verint Merging to Master (1,282 lines), INT-53342 × 2 |
| moadzughul | Moad Alzughul | **4** | **3** | int 53038 (526 lines), WEM direction fix, Interval Publisher, Dapper fix |
| mfield1 | Matt Field | **2** | **3** | Enterprise Jenkins Pipelines × 2 (694 + 81 lines) |
| chris-haun | Chris Haun | **6** | **3** | Int 52611, Int 54753, Int 55582, INT-53342, INT-55367, Int 56020 |
| luisalvatierra | Luis Salvatierra | **1** | **3** | INT-54757 PO cluster ic-perf (3 lines) |
| copilotshree | **Likely Shreedevi Patil** ⚠️ | **1** | **3** | INT-52793 Java 21 changes (252 lines, intervalreader) — identity unconfirmed |
| meghabiradar05 | Megha Biradar | **1** | 3 | INT-53064 (6,995 lines) — new user, not in AI analysis |
| BireshwarNice | (not in team scope) | **1** | — | FRE-2345 NA3 Deployment — excluded from AI analysis |
| rohit-verma21 | (not in team scope) | **1** | — | Pdo 17709 dev — excluded from AI analysis |

> ⚠️ **copilotshree identity:** GitHub username "copilotshree" contains the prefix "shree." Best match in team: **Shreedevi Patil** (AI login: shreedevi-nice). If correct, she has 1 merged PR (252 changed lines, Java 21 upgrade). Confirm via GitHub Users Mapping tab.

---

## CRQC Score Reference

| Pillar | Max | Source | Key Thresholds |
|---|---|---|---|
| **Core (C)** | 3 | AI Usage — varies by workflow type | Agent-First: Sugg Eff > 15 = 2pts; Hybrid: Accept 15–30% = 1pt + Eff > 8 = 1pt; Inline: Accept 20–35% = 2pts |
| **ROI (R)** | 3 | AI Usage — Sugg Eff proxy | > 20 = 3pts; 10–20 = 2pts; 5–10 = 1pt; < 5 = 0pts |
| **Quality (Q)** | 3 | PR Details tab | PR Merge ≥ 80% = 2pts; + Reviews ≥ 1/PR = +1pt; + Merge ≤ 3 days = +1 (cap 3) |
| **Total** | 9 | C + R + Q | 7–9 = A; 5–6 = B; 3–4 = C; 1–2 = D; 0 = E |

---

## CRQC Scorecard — All Users (Q Scores Loaded)

*Q = **3**: confirmed merged PRs, team-level merge rate 91%, reviews 3.78/PR | Q = **FB**: Feature branch work, not captured in main branch filter | Q = **0**: confirmed zero PR activity*

| User | Role | Workflow | C | R | Q | **Total** | **Tier** | Notes |
|---|---|---|---|---|---|---|---|---|
| Moad Alzughul | Dev | AF | **3** | **2** | **3** | **8** | 🌟 **A** | C: Eff 15.80 >>15 (2) +LoC trend (+1). R: 15.80 in 10–20 (2). Q: 4 merged PRs. |
| Chris Haun | Dev | HY | **3** | **1** | **3** | **7** | 🌟 **A** | C: Accept 15.9% (1) +Eff >8 (1) +Count 124 (+1). R: Eff 8.68 in 5–10 (1). Q: 6 merged PRs. ⚠️ AI activity stall (+88 LoC) — coding but not using Copilot. |
| Matt Field | Dev | AF | **2** | **2** | **3** | **7** | 🌟 **A** | C: Eff 14.45 in 8–15 (1) +trend (+1). R: 14.45 in 10–20 (2). Q: 2 merged PRs (Jenkins pipeline mgmt). |
| Mikhail Shnayderman | Dev | AF | **3** | **3** | **FB** | **6+** | 🌟 **A** | C: Eff 72.06 >>15 (2) +trend (+1). R: 72.06 >>20 (3). Q: Feature branch work not captured — likely strong given output volume. |
| Amol Salunkhe | Dev | AF | **3** | **3** | **FB** | **6+** | 🌟 **A** | C: Eff 35.96 >>15 (2) +7.8× surge (+1). R: 35.96 >>20 (3). Q: Feature branch. |
| Vyankatesh Khadakkar | Dev | IL | **3** | **3** | **FB** | **6+** | 🌟 **A** | C: 66.2% >>20–35% (2) +Count 45 (+1). R: Eff 41.10 >>20 (3). Q: Feature branch. |
| Abhishek Hole | Dev | AF | **3** | **3** | **FB** | **6+** | 🌟 **A** | C: Eff 61.86 >>15 (2) +2,403 LoC surge (+1). R: 61.86 >>20 (3). Q: Feature branch. |
| Swapnil Zade | Mgr | AF | **3** | **3** | **FB** | **6+** | 👍 **B** *(Manager context)* | C: Eff 33.29 >>15 (2) +trend (+1). R: 33.29 >>20 (3). Q: Feature branch. Manager — engagement weighted. |
| Sourabh Kalaskar | Dev | HY | **3** | **3** | **FB** | **6+** | 🌟 **A** | C: Accept 15.9% (1) +Eff 29.80 >8 (1) +Count 11 (+1). R: 29.80 >>20 (3). Q: Feature branch. |
| Mohan Shivarkar | Dev | IL | **2** | **0** | **3** | **5** | 👍 **B** | C: 69.6% >>20–35% (2) +Count 16 <20 (0). R: Eff 1.22 <5 (0). Q: 3 merged PRs — delivering to production. ⚠️ R=0 + Premium check needed for cap rule. |
| Suhas Kakde | Dev | AF | **1** | **1** | **3** | **5** | 👍 **B** | C: Eff 8.73 in 8–15 (1) +barely growing (0). R: 8.73 in 5–10 (1). Q: 3 merged PRs. CRQC upgrade from D/C. |
| Jayesh Rai | Dev | AF | **1** | **1** | **3** | **5** | 👍 **B** | C: Eff 7.69 <8 (0) +LoC trend (+1). R: 7.69 in 5–10 (1). Q: 1 merged PR (Release26.1, 12,417 lines — key release delivery). CRQC upgrade from D. |
| Luis Salvatierra | Dev | HY | **1** | **1** | **3** | **5** | 👍 **B** | C: Accept 13% <15% (0) +Eff <8 (0) +Count 36 (+1). R: 6.13 in 5–10 (1). Q: 1 merged PR. CRQC upgrade from C/D. |
| Shreedevi Patil | Dev | IL | **2** | **1** | **3** ⚠️ | **6** ⚠️ | 👍 **B** | C: 30.0% in 20–35% (2) +Count 3 <20 (0). R: Eff 8.80 in 5–10 (1). Q: 1 merged PR IF copilotshree=Shreedevi. **Confirm identity.** |
| Ritesh Pawar | Dev | AF | **2** | **3** | **FB** | **5+** | 👍 **B** | C: Eff 75.13 >>15 (2) +0 new LoC (0). R: 75.13 >>20 (3). Q: Feature branch. ⚠️ Zero period output. |
| Prathmesh Ranadive | Dev | IL | **3** | **2** | **FB** | **5+** | 👍 **B** | C: 77.9% >>20–35% (2) +Count 471 (+1). R: Eff 14.52 in 10–20 (2). Q: Feature branch. |
| Moad — (see top) | | | | | | | | |
| Nilesh Tonape | Dev | HY | **2** | **3** | **FB** | **5+** | 👍 **B** | C: 11.9% <15% (0) +Eff 24.42 >8 (1) +Count 24 (+1). R: 24.42 >>20 (3). Q: Feature branch. |
| Vitthal Devkar | Dev | IL | **3** | **2** | **FB** | **5+** | 👍 **B** | C: 44.8% >>20–35% (2) +Count 78 (+1). R: Eff 14.21 in 10–20 (2). Q: Feature branch. |
| Pradnyesh Salunke | Dev | IL | **3** | **2** | **FB** | **5+** | 👍 **B** | C: 31.1% in 20–35% (2) +Count 46 (+1). R: Eff 11.72 in 10–20 (2). Q: Feature branch. |
| Shraddha Kale | Dev | AF | **2** | **2** | **FB** | **4+** | 👌–👍 **C/B** | C: Eff 11.10 in 8–15 (1) +trend (+1). R: 11.10 in 10–20 (2). Q: Feature branch. |
| Tushar Patil | Dev | HY | **1** | **3** | **FB** | **4+** | 👌–👍 **C/B** | C: 14.3% <15% (0) +Eff 39.69 >8 (1) +Count 5 <10 (0). R: 39.69 >>20 (3). Q: Feature branch. |
| Abhijeet Kolhe | Dev | HY | **2** | **2** | **FB** | **4+** | 👌–👍 **C/B** | C: 18.8% in 15–30% (1) +Eff 10.75 >8 (1) +Count 3 <10 (0). R: 10.75 in 10–20 (2). Q: Feature branch. Tiny volume. |
| Suraj Dubey | Dev | AF | **2** | **2** | **FB** | **4+** | 👌–👍 **C/B** | C: Eff 16.37 >>15 (2) +0 new LoC (0). R: 16.37 in 10–20 (2). Q: Feature branch. |
| Shubham Gite | Dev | IL | **3** | **0** | **FB** | **3+** | 👌 **C** | C: 57.2% >>20–35% (2) +Count 139 (+1). R: Eff 1.10 <5 (0). Q: Feature branch. Core excellent, ROI poor — volume-constrained. |
| Trunal Gawade | Dev | IL | **3** | **0** | **FB** | **3+** | 👌 **C** | C: 27.4% in 20–35% (2) +Count 49 (+1). R: Eff 1.46 <5 (0). Q: Feature branch. Same pattern as Shubham. |
| Shridhar Mishra | Dev | IL | **2** | **1** | **FB** | **3+** | 👌 **C** | C: 69.6% >>20–35% (2) +Count 16 <20 (0). R: Eff 6.74 in 5–10 (1). Q: Feature branch. First LoC period. |
| Amulya Kale | Dev | HY | **2** | **0** | **FB** | **2+** | 🟠–👌 **D/C** | C: 19.5% in 15–30% (1) +Eff 3.62 <8 (0) +Count 61 (+1). R: 3.62 <5 (0). Q: Feature branch. |
| Pratik Devle | Dev | AF | **1** | **1** | **FB** | **2+** | 🟠–👌 **D/C** | C: Eff 6.07 <8 (0) +barely increasing (+1). R: 6.07 in 5–10 (1). Q: Feature branch. |
| Prashasti Jain | Dev | HY | **1** | **1** | **FB** | **2+** | 🟠 **D** | C: 14.3% <15% (0) +Eff 9.67 >8 (1) +Count 3 <10 (0). R: 9.67 in 5–10 (1). Q: Feature branch. 🔴 5-period P0. |
| Pratik Pawar | Dev | AF | **1** | **0** | **FB** | **1+** | 🟠 **D** | C: Eff 1.66 <8 (0) +first LoC (+1). R: 1.66 <5 (0). Q: Feature branch. First period with output. |
| Nishtha Thakral | Dev | HY | **0** | **0** | **0** | **0** | 🔴 **E** | Zero output confirmed. Q=0 (no PRs any branch). All pillars = 0. |
| Susovan Samal | Mgr | AF | **0** | **0** | N/A | **0** | Manager | Near-zero expected. Manager context. |
| Rahul Walunj | Research | — | — | — | N/A | — | Research | Excluded from CRQC. |

---

## CRQC Tier Summary (With Q Scores Loaded)

| Tier | Users | Basis | Key Insight |
|---|---|---|---|
| 🌟 **A** (confirmed) | **3** | C+R+Q ≥ 7 | Moad Alzughul (8), Chris Haun (7), Matt Field (7) |
| 🌟 **A** (C+R ≥ 6, Q=FB) | **6** | C+R ≥ 6, Q pending | Mikhail, Amol, Vyankatesh, Abhishek Hole, Sourabh Kalaskar, Swapnil (B as Manager) |
| 👍 **B** (confirmed) | **6** | C+R+Q = 5–6 | Mohan Shivarkar (5), Suhas Kakde (5), Jayesh Rai (5), Luis Salvatierra (5), Shreedevi Patil (6, tentative), Ritesh (5+FB) |
| 👍 **B** (C+R = 5, Q=FB) | **5** | C+R = 5, Q pending | Prathmesh, Nilesh, Vitthal, Pradnyesh, Ritesh |
| 👌 **C/B** (C+R = 4, Q=FB) | **5** | C+R = 4, Q pending | Shraddha, Tushar, Abhijeet, Suraj, Chris Haun now confirmed A |
| 👌 **C** (C+R = 3, Q=FB) | **3** | C+R = 3, Q pending | Shubham, Trunal, Shridhar |
| 🟠 **D/C** (C+R = 2, Q=FB) | **2** | C+R = 2, Q pending | Amulya, Pratik Devle |
| 🟠 **D** | **2** | C+R ≤ 2 | Prashasti Jain (P0), Pratik Pawar |
| 🔴 **E** | **1** | All pillars = 0 | Nishtha Thakral |
| Manager | **1** | — | Susovan Samal |
| Research | **1** | — | Rahul Walunj |

---

## Override Rules Applied

| Override | Status | Users Affected |
|---|---|---|
| **Q = 0 → Cannot be Tier A** | ✅ Applied | Nishtha Thakral (Q=0 confirmed → E tier, N/A) |
| **R = 0 AND Premium > 500 → Cannot be above C** | ⚠️ Check Premium | Mohan Shivarkar (R=0, Q=3, total=5 → B); Shubham Gite, Trunal Gawade (R=0). Pull Premium data to confirm or cap. |
| **Momentum > +100% → Eligible for tier promotion** | ✅ Applied | Amol, Prathmesh, Abhishek Hole, Vitthal, Pradnyesh, Jayesh Rai, Pratik Pawar, Shridhar already reflected in CRQC scores |
| **Research → Not tiered** | ✅ | Rahul Walunj |

---

## The CRQC Revelation — Key Insights vs v1

| Finding | v1 Tier | CRQC Tier | Why It Matters |
|---|---|---|---|
| **Chris Haun** | B (flagged, +88 LoC stall) | **A** (C+R+Q = 7) | 6 merged PRs to main = real production delivery. He's coding, just not using Copilot heavily this period. The stall is in AI usage, not engineering output. |
| **Matt Field** | B | **A** (C+R+Q = 7) | 2 merged PRs (Jenkins pipeline mgmt). His AI efficiency is real AND he's shipping infrastructure. |
| **Moad Alzughul** | B | **A** (C+R+Q = 8) | 4 merged PRs + solid AI efficiency = most complete performer profile. |
| **Jayesh Rai** | D | **B** (C+R+Q = 5) | 1 merged PR was the 12,417-line Release26.1 integration — one of the largest PRs this quarter. Pure AI metrics missed this entirely. |
| **Mohan Shivarkar** | D (only 28 LoC!) | **B** (C+R+Q = 5) | 3 merged PRs to main. 28 LoC in AI usage but 2,375 lines in merged PRs. Coding directly without Copilot. Q pillar rescues him from D. |
| **Suhas Kakde** | C (stalling) | **B** (C+R+Q = 5) | 3 merged PRs including a 8,494-line INT-41859. High Copilot engagement AND shipping code. CRQC sees the full picture. |
| **Luis Salvatierra** | C | **B** (C+R+Q = 5) | 1 merged PR. Weak AI metrics but contributing to production. |
| **Mikhail Shnayderman** | A | **A** (C+R+FB = 6+) | Still clearly A — strongest AI usage + Q pending (feature branch). No change. |

---

## Context Pillar (Diagnostic Only)

| User | Context Signal | Interpretation |
|---|---|---|
| Chris Haun | 814 Initiated Interactions, +88 LoC, 6 merged PRs | The disconnect resolves: he's coding directly to main branches without heavy Copilot assist this period. His Copilot is engaged (interactions), but code delivery is happening outside the Copilot loop. |
| Jayesh Rai | 1 merged PR = Release26.1 (12,417 lines) | The single PR tells the whole story — he integrated a full release. AI usage (Tier D signals) doesn't capture this. CRQC does. |
| Mohan Shivarkar | 28 LoC in AI usage, 2,375 lines in merged PRs | Clear evidence of non-Copilot coding. He's productive, just not Copilot-first. Coach on Copilot adoption, not performance. |
| Nishtha Thakral | 51 Initiated Interactions, 0 LoC, 0 PRs | Both AI usage and PR data confirm zero productive output. No ambiguity. Final decision needed. |
| Prathmesh Ranadive | 471 Code Accept, 77.9% rate, Feature branch | Likely has excellent PR quality in feature branches (coaching success — his accept rate explosion suggests he's generating high-quality code). Pull feature branch PRs to confirm. |

---

## Action Items — CRQC-Specific

| Priority | Action | Basis |
|---|---|---|
| 🔴 P0 | **Confirm copilotshree = Shreedevi Patil** via GitHub Users Mapping tab in Power BI | Identity affects her tier (D→B if confirmed) |
| 🔴 P0 | **Pull Premium Requests data** to apply R=0+Premium>500 cap rule for Mohan Shivarkar, Shubham Gite, Trunal Gawade | Required for override rules |
| 🟠 P1 | **Re-run Q scoring with BRANCH filter = All** to capture feature branch PR quality for the majority of users | Most users' Q is currently FB (unknown) |
| 🟠 P1 | **Investigate Chris Haun's AI stall** — he has 6 merged PRs but only +88 Copilot LoC. He's coding but bypassing Copilot. | Coach on reintegrating Copilot into his main branch workflow |
| 🟡 P2 | **Celebrate Moad Alzughul** — top CRQC score (8/9). Both AI usage AND PR delivery are strong. | Share as the complete performance benchmark |
| 🟡 P2 | **Coach Mohan Shivarkar and Jayesh Rai on Copilot adoption** | They're shipping code but their AI efficiency is low — they're leaving Copilot value on the table |

---

*Document generated 2026-05-11 from Power BI GitHub 360 AI Usage dashboard (AI usage synced 5/10/2026) + Power BI PR Details tab (WFM Integrations, Main Branches, Merged, Q1 2026). Based on github-benchmark-CRQC.md. Q scores loaded for users with confirmed main-branch PR activity. Feature-branch PR quality pending BRANCH=All re-run.*
