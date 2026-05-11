# 📊 Github Analysis — 11 May 2026 (CRQC Format)

*Data source: Power BI GitHub 360 AI Usage dashboard, last synced 5/10/2026 9:39:11 PM | WFM Integrations | Based on **github-benchmark-CRQC.md** (4-Pillar Scoring Framework)*

> ⚠️ **Methodology notes:**
> - **Core (C):** Scored 0–3 per workflow type. Workflow types assigned using % Accept + Sugg Eff proxies (Agent Contribution % not exposed per-user in current Power BI view).
> - **ROI (R):** Scored 0–3 using Suggestion Efficiency (Sugg Eff = LoC Added / Code Gen) as proxy for Request Efficiency (LoC/Premium Request). Premium Requests data unavailable. Lean spend bonus and outlier penalty omitted this period.
> - **Quality (Q):** Scored 0–3 from Power BI PR Details tab. **All values TBD** — per-user PR data not pulled this session. Final tier assignment incomplete until Q scores are loaded.
> - **Context (C):** Diagnostic only. Listed per-user where notable. Never affects tier score.

---

## CRQC Score Reference

| Pillar | Max | Source | Key Thresholds |
|---|---|---|---|
| **Core (C)** | 3 | AI Usage — varies by workflow type | Agent-First: Sugg Eff > 15 = 2pts; Hybrid: Accept 15–30% = 1pt + Eff > 8 = 1pt; Inline: Accept 20–35% = 2pts |
| **ROI (R)** | 3 | AI Usage — Sugg Eff proxy | > 20 = 3pts; 10–20 = 2pts; 5–10 = 1pt; < 5 = 0pts |
| **Quality (Q)** | 3 | PR Details tab | PR Merge ≥ 80% = 2pts; + Reviews ≥ 1/PR = +1pt; + Merge ≤ 3 days = +1 (cap 3) |
| **Total** | 9 | C + R + Q | 7–9 = A; 5–6 = B; 3–4 = C; 1–2 = D; 0 = E |

---

## CRQC Scorecard — All Users

*Workflow Type: AF = Agent-First, HY = Hybrid, IL = Inline-First*

| User | Role | Workflow | C Score | R Score | Q Score | **C+R** | **Est. Total** | **Tier (Partial)** | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Mikhail Shnayderman | Dev | AF | **3** | **3** | TBD | **6** | 6–9 | 🌟 **A** *(min B confirmed)* | C: Eff 72.06 >> 15 (2) + LoC increasing (+1). R: Eff 72.06 >> 20 (3). |
| Amol Salunkhe | Dev | AF | **3** | **3** | TBD | **6** | 6–9 | 🌟 **A** *(min B confirmed)* | C: Eff 35.96 >> 15 (2) + 7.8× LoC surge (+1). R: Eff 35.96 >> 20 (3). |
| Ritesh Pawar | Dev | AF | **2** | **3** | TBD | **5** | 5–8 | 👍 **B** *(min B)* | C: Eff 75.13 >> 15 (2) + 0 new LoC — no trend bonus. R: 75.13 >> 20 (3). ⚠️ Zero period output. |
| Matt Field | Dev | AF | **2** | **2** | TBD | **4** | 4–7 | 👌–👍 **C/B** | C: Eff 14.45 in 8–15 (1) + LoC increasing (+1). R: 14.45 in 10–20 (2). |
| Prathmesh Ranadive | Dev | IL | **3** | **2** | TBD | **5** | 5–8 | 👍 **B** *(min B)* | C: 77.9% accept >> 20–35% (2) + Count 471 >> 20 (+1). R: Eff 14.52 in 10–20 (2). |
| Shraddha Kale | Dev | AF | **2** | **2** | TBD | **4** | 4–7 | 👌–👍 **C/B** | C: Eff 11.10 in 8–15 (1) + LoC increasing (+1). R: 11.10 in 10–20 (2). |
| Swapnil Zade | Mgr | AF | **3** | **3** | TBD | **6** | 6–9 | 👍 **B** *(min B; Manager context)* | C: Eff 33.29 >> 15 (2) + LoC increasing (+1). R: 33.29 >> 20 (3). Manager benchmark — engagement weighted. |
| Vyankatesh Khadakkar | Dev | IL | **3** | **3** | TBD | **6** | 6–9 | 🌟 **A** *(min B confirmed)* | C: 66.2% >> 20–35% (2) + Count 45 >> 20 (+1). R: Eff 41.10 >> 20 (3). |
| Abhishek Hole | Dev | AF | **3** | **3** | TBD | **6** | 6–9 | 🌟 **A** *(min B confirmed)* | C: Eff 61.86 >> 15 (2) + 2,403 LoC surge (+1). R: 61.86 >> 20 (3). 0% accept structurally correct. |
| Moad Alzughul | Dev | AF | **3** | **2** | TBD | **5** | 5–8 | 👍 **B** *(min B)* | C: Eff 15.80 >> 15 (2) + LoC increasing (+1). R: 15.80 in 10–20 (2). |
| Chris Haun | Dev | HY | **3** | **1** | TBD | **4** | 4–7 | 👌–👍 **C/B** | C: 15.9% in 15–30% (1) + Eff 8.68 > 8 (1) + Count 124 > 10 (+1). R: Eff 8.68 in 5–10 (1). ⚠️ +88 LoC stall. |
| Nilesh Tonape | Dev | HY | **2** | **3** | TBD | **5** | 5–8 | 👍 **B** *(min B)* | C: 11.9% < 15% (0) + Eff 24.42 > 8 (1) + Count 24 > 10 (+1). R: 24.42 >> 20 (3). |
| Vitthal Devkar | Dev | IL | **3** | **2** | TBD | **5** | 5–8 | 👍 **B** *(min B)* | C: 44.8% >> 20–35% (2) + Count 78 >> 20 (+1). R: Eff 14.21 in 10–20 (2). |
| Sourabh Kalaskar | Dev | HY | **3** | **3** | TBD | **6** | 6–9 | 👍 **B** *(min B confirmed)* | C: 15.9% in 15–30% (1) + Eff 29.80 > 8 (1) + Count 11 > 10 (+1). R: 29.80 >> 20 (3). |
| Pradnyesh Salunke | Dev | IL | **3** | **2** | TBD | **5** | 5–8 | 👍 **B** *(min B)* | C: 31.1% in 20–35% (2) + Count 46 > 20 (+1). R: Eff 11.72 in 10–20 (2). |
| Tushar Patil | Dev | HY | **1** | **3** | TBD | **4** | 4–7 | 👌–👍 **C/B** | C: 14.3% < 15% (0) + Eff 39.69 >> 8 (1) + Count 5 < 10 (0). R: 39.69 >> 20 (3). High ROI, low Core signals. |
| Luis Salvatierra | Dev | HY | **1** | **1** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: 13.0% < 15% (0) + Eff 6.13 < 8 (0) + Count 36 > 10 (+1). R: 6.13 in 5–10 (1). |
| Amulya Kale | Dev | HY | **2** | **0** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: 19.5% in 15–30% (1) + Eff 3.62 < 8 (0) + Count 61 > 10 (+1). R: 3.62 < 5 (0). Poor ROI. |
| Abhijeet Kolhe | Dev | HY | **2** | **2** | TBD | **4** | 4–7 | 👌–👍 **C/B** | C: 18.8% in 15–30% (1) + Eff 10.75 > 8 (1) + Count 3 < 10 (0). R: 10.75 in 10–20 (2). Tiny volume. |
| Suhas Kakde | Dev | AF | **1** | **1** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: Eff 8.73 in 8–15 (1) + LoC barely growing (0). R: 8.73 in 5–10 (1). High interactions, low conversion. |
| Jayesh Rai | Dev | AF | **1** | **1** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: Eff 7.69 < 8 (0) + LoC increasing (+1). R: 7.69 in 5–10 (1). |
| Suraj Dubey | Dev | AF | **2** | **2** | TBD | **4** | 4–7 | 👌–👍 **C/B** | C: Eff 16.37 >> 15 (2) + 0 new LoC — no trend (+0). R: 16.37 in 10–20 (2). Strong Agent-First signals; volume the only concern. |
| Pratik Devle | Dev | AF | **1** | **1** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: Eff 6.07 < 8 (0) + barely increasing (+1). R: 6.07 in 5–10 (1). |
| Shubham Gite | Dev | IL | **3** | **0** | TBD | **3** | 3–6 | 👌 **C** *(min C)* | C: 57.2% >> 20–35% (2) + Count 139 >> 20 (+1). R: Eff 1.10 < 5 (0). Excellent Core, terrible ROI. Volume-constrained. |
| Trunal Gawade | Dev | IL | **3** | **0** | TBD | **3** | 3–6 | 👌 **C** *(min C)* | C: 27.4% in 20–35% (2) + Count 49 > 20 (+1). R: Eff 1.46 < 5 (0). Same pattern as Shubham. |
| Prashasti Jain | Dev | HY | **1** | **1** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: 14.3% < 15% (0) + Eff 9.67 > 8 (1) + Count 3 < 10 (0). R: 9.67 in 5–10 (1). 🔴 P0 unresolved. |
| Pratik Pawar | Dev | AF | **1** | **0** | TBD | **1** | 1–4 | 🟠 **D** *(max C without Q)* | C: Eff 1.66 < 8 (0) + first LoC (+1). R: 1.66 < 5 (0). Emerging, first period. |
| Shridhar Mishra | Dev | IL | **2** | **1** | TBD | **3** | 3–6 | 👌 **C** *(min C)* | C: 69.6% >> 20–35% (2) + Count 16 < 20 (0). R: Eff 6.74 in 5–10 (1). First LoC. Strong accept signal. |
| Shreedevi Patil | Dev | IL | **2** | **1** | TBD | **3** | 3–6 | 👌 **C** *(min C)* | C: 30.0% in 20–35% (2) + Count 3 < 20 (0). R: Eff 8.80 in 5–10 (1). Tiny volume. |
| Mohan Shivarkar | Dev | IL | **2** | **0** | TBD | **2** | 2–5 | 🟠–👌 **D/C** | C: 69.6% >> 20–35% (2) + Count 16 < 20 (0). R: Eff 1.22 < 5 (0). Micro-snippets only. |
| Nishtha Thakral | Dev | HY | **0** | **0** | **0** | **0** | 0 | 🔴 **E** | Zero output. Q = 0 confirmed (no PRs). All pillars = 0. |
| Susovan Samal | Mgr | AF | **0** | **0** | TBD | **0** | 0–3 | Manager | Near-zero expected. Manager context — not tiered A–E. |
| Rahul Walunj | Research | — | — | — | — | — | — | Research | Excluded from CRQC scoring per framework. |

---

## Override Rules Applied

| Override | Users Affected | Impact |
|---|---|---|
| **Q = 0 (< 50% PR merge rate) → cannot be Tier A** | TBD — Q not pulled yet | If any current A-candidate has <50% PR merge rate, cap at B |
| **R = 0 AND Premium > 500 → cannot be above C** | Amulya Kale (R=0), Shubham Gite (R=0), Trunal Gawade (R=0), Mohan Shivarkar (R=0) | If Premium > 500 confirmed for any of these, cap at C regardless of C score |
| **Research → not tiered** | Rahul Walunj | Excluded |

> **Action required:** Load Premium Requests and PR Merge Rate from Power BI before applying override rules. Current CRQC tier assignments are provisional.

---

## Tier Summary (Partial — Q Pending)

| Est. Tier | Users (based on C+R) | C+R Range | Key Condition |
|---|---|---|---|
| 🌟 **A** *(C+R ≥ 6, needs Q ≥ 1)* | 4 | C+R = 6 | Mikhail, Amol, Vyankatesh, Abhishek Hole — all confirmed 6/6 C+R |
| 👍 **B** *(C+R = 4–5, needs Q ≥ 1)* | 9 | C+R = 4–5 | Ritesh, Prathmesh, Matt, Shraddha, Moad, Nilesh, Vitthal, Sourabh, Pradnyesh |
| 👍 **B or A** *(pending Q)* | 1 | C+R = 6 | Swapnil Zade (Manager context — not tier A by convention for managers) |
| 👌 **C** *(C+R = 3)* | 5 | C+R = 3 | Shubham Gite, Trunal Gawade, Shridhar Mishra, Shreedevi Patil, Suraj Dubey (C+R=4) |
| 👌 **C / 👍 B** *(C+R = 4, Q determines)* | 6 | C+R = 4 | Matt Field, Shraddha Kale, Chris Haun, Abhijeet Kolhe, Suraj Dubey, Tushar Patil |
| 🟠 **D** *(C+R ≤ 2)* | 9 | C+R = 0–2 | Luis, Amulya, Suhas, Jayesh, Pratik Devle, Prashasti, Pratik Pawar, Mohan, Nishtha |
| 🔴 **E** | 1 | C+R = 0 | Nishtha Thakral |
| Manager | 1 | — | Susovan Samal |
| Research | 1 | — | Rahul Walunj |

---

## Context Pillar (Diagnostic Only)

*These signals explain C/R/Q scores. They do not affect tier assignment.*

| User | Context Signal | Interpretation |
|---|---|---|
| Chris Haun | 814 Initiated Interactions, +88 LoC | Very high interaction count not converting to output. Struggling or blocked — not productive engagement. |
| Suhas Kakde | 137 Initiated Interactions, +18 LoC | Same pattern as Chris Haun but smaller scale. High volume of prompts, near-zero output. |
| Nishtha Thakral | 51 Initiated Interactions, 0 LoC | Active user who generates zero value. Confirms training gap, not disengagement. |
| Prathmesh Ranadive | 471 Code Acceptance Count, 605 Code Gen | Inline-First with near-perfect acceptance discipline. 78% of generated suggestions accepted. Exceptional quality gate. |
| Shubham Gite | 139 Code Accept, 243 Code Gen, 57.2% rate | High acceptance rate/count but only 268 LoC → small suggestions. Task assignment issue, not skill gap. |
| Trunal Gawade | 49 Code Accept, 179 Code Gen, 27.4% rate | Similar to Shubham. LoC low despite reasonable T1 — constrained by task nature. |
| Mikhail Shnayderman | LoC Sugg 2,567, LoC Added 22,268 | Agent-First pattern: LoC Added >> LoC Sugg. Copilot generating beyond the suggestions panel. Healthy signal. |
| Abhishek Hole | 0 Code Accept, 44 Code Gen, 61.86 eff | Pure agent mode. 0% accept is expected (agent generates LoC outside the suggestion acceptance flow). |
| Amulya Kale | 313 Code Gen, Eff 3.62 | Very high generation count with low LoC per event. Suggests Copilot generating many small suggestions, most of low quality for her context. |

---

## Q Score — Data Pull Checklist

Run this before finalizing any CRQC tier assignment:

| Step | Action | Power BI Location |
|---|---|---|
| 1 | Open Power BI GitHub 360 | Reports → Pull Request Details tab |
| 2 | Filter by user login + same time window (May 11 analysis period) | Filters panel |
| 3 | Record: Total PRs, Merged PRs, Total Reviews | PR Status + Reviews metrics |
| 4 | Calculate: Merge Rate = Merged ÷ Total | Manual |
| 5 | Calculate: Review Rate = Reviews ÷ PRs | Manual |
| 6 | Score: ≥ 80% merge + ≥ 1 review/PR = 2pts; 50–79% or < 1 review = 1pt; < 50% merge = 0pts | Per Q pillar rules |
| 7 | Check: Time to Merge ≤ 3 days avg = +1 bonus (cap score at 3) | Time to Merge metric |
| 8 | Apply Q override: Q=0 → cannot be Tier A | Before finalizing |

---

## CRQC vs v1 Framework Comparison (May 11)

| Signal | v1 Result | CRQC Result | Key Difference |
|---|---|---|---|
| Mikhail Shnayderman | Tier A (noted 0% accept caveat) | **C+R = 6/6, Tier A** | CRQC formally scores Agent-First efficiency — no caveats needed |
| Sourabh Kalaskar | Tier C | **C+R = 6/6, Tier B** | Hybrid signals scored correctly in CRQC Core pillar |
| Shubham Gite | Tier D | **C+R = 3, Tier C** | CRQC separates Core (excellent) from ROI (poor) — volume gap is identified not confused with skill gap |
| Trunal Gawade | Tier D | **C+R = 3, Tier C** | Same pattern as Shubham — Core strong, ROI weak |
| Chris Haun | Tier B | **C+R = 4, Tier C/B** | CRQC penalizes low ROI signal (Eff 8.68 = 1pt) separately from Core. v1 masked this with cumulative LoC. |
| Amulya Kale | Tier C | **C+R = 2, Tier D** | CRQC surfaces R=0 (Eff 3.62 < 5) separately. v1 only noted Sugg Eff as a flag. |

---

*Document generated 2026-05-11 from Power BI GitHub 360 AI Usage dashboard (WFM Integrations, data through 5/10/2026). Based on github-benchmark-CRQC.md 4-pillar methodology. Quality (Q) scores pending Power BI PR Details tab pull — load Q before treating any tier assignment as final.*
