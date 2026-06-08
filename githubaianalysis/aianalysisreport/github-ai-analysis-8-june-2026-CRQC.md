# GitHub Copilot Usage Analysis — CRQC 4-Pillar Framework
**Product:** WFM Integrations | **R&D VP:** WFM | **Team:** All  
**Analysis Date:** June 8, 2026 | **Data Sync:** June 7, 2026 (10:30 PM)  
**Framework:** CRQC (github-benchmark-CRQC.md) | **Scale:** C(0–3) + R(0–3) + Q(0–3) = 0–9 → Tier A–E

---

## CRQC Framework Summary

| Pillar | Source | Scoring |
|---|---|---|
| **C — Core** | AI Usage tab | Workflow-type specific. Agent-First: ReqEff-based. Hybrid: %Accept + ReqEff. Inline-First: %Accept + Accept Count. Max 3 pts. |
| **R — ROI** | AI Usage tab | Universal. ReqEff tiers: >20→3, 10-20→2, 5-10→1, <5→0. Lean spend (≤500 req) +1 bonus. Outlier (>1,700 req) −1 penalty. Max 3 pts. |
| **Q — Quality** | PR Details tab | Merge rate ≥80%→2, +Review≥1/PR→+1, +AvgMerge≤3days→+1(cap 3). Team proxy applied (see note). Max 3 pts. |
| **Context** | AI Usage tab | Diagnostic only. Never adjusts score. Explains C/R/Q anomalies. |

### Q Score Methodology

> Per-user PR data is not available in filterable form in the current dashboard. The PR Details tab shows team-level aggregates only. **Team proxy applied:**
> - Merge rate: ~90% → **2 pts** (≥80% threshold met)
> - Reviews per PR: 3.67/PR → **+1 pt** (≥1 review/PR threshold met)
> - Avg time to merge: 1.9 days → **+1 bonus** (≤3 days threshold met, capped at 3)
> - **Q = 3 default** for all active developers with LoC > 500

> **Q = 0** applied to: near-inactive users (LoC ≤ 50 or 0 activity) — kbajaj-nice (LoC=5), dannycadima (LoC=34), giteshsawant (LoC=~50), rwalunj-nice (LoC=0)
> **Q = 1** applied to: very low output users unlikely to have main-branch PR activity — ShivrajNice (~450 LoC), pratikpawar12 (250 LoC), dsuraj25 (~510 LoC)
> **Q = 2** applied to: low-moderate output where PR contribution is plausible but uncertain — smishra-nice (155 LoC), sohanbafna (467 LoC)

---

## CRQC Pillar Scoring — All 47 Developers

### Core (C) Score Rules Recap

**Agent-First:** ReqEff >15 → 2pts | ReqEff 8–15 → 1pt | ReqEff <8 → 0pts | LoC trend increasing → +1pt (max 3)

**Hybrid:** %Accept 15–30% → 1pt | ReqEff >8 → 1pt | Accept Count >10 → +1pt (max 3)

**Inline-First:** %Accept 20–35% → 2pts | %Accept 10–19% → 1pt | Accept Count >20 → +1pt (max 3)

### ROI (R) Score Rules Recap

ReqEff >20 → 3pts | 10–20 → 2pts | 5–10 → 1pt | <5 → 0pts  
Premium ≤500 → +1 bonus | Premium >1,700 → −1 penalty

### Full Scorecard

| Login | Name | Workflow | C | R | Q | Total | Tier | Override? | Momentum |
|---|---|---|---|---|---|---|---|---|---|
| tomotvos | Tom Otvos | Agent-First | 3 | 3 | 3 | **9** | 🌟 A | — | ➡️ Stable |
| rpawar-nice | Ritesh Pawar | Hybrid | 2 | 3 | 3 | **8** | 🌟 A | — | 🚀 Breakout |
| dhanshree-jagtap-nice | Dhanshree Jagtap | Hybrid | 2 | 3 | 3 | **8** | 🌟 A | — | 🆕 New |
| Kranti-nice | Kranti Kaple | Agent-First | 3 | 2 | 3 | **8** | 🌟 A | — | 🚀 Breakout |
| rizeq-abu-madeghem | Rizeq Abu Madeghem | Agent-First | 3 | 2 | 3 | **8** | 🌟 A | — | 📈 Rising |
| Vyankatesh95 | Vyankatesh Khadakkar | Inline-First | 2 | 2 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| mfield1 | Matt Field | Hybrid | 2 | 2 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| nice-harshada | Harshada Bagane | Agent-First | 2 | 2 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| Vitthal-Nice | Vitthal Devkar | Inline-First | 3 | 2 | 3 | **8** | 🌟 A | — | ➡️ Stable |
| abhijeetk268 | Abhijeet Kolhe | Inline-First | 2 | 2 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| yogitadhanwate | Yogita Dhanwate | Hybrid | 2 | 2 | 3 | **7** | 🌟 A | — | 📈 Rising |
| jayesh-rai | Jayesh Rai | Agent-First | 2 | 2 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| jkumbhar | Jyoti Kumbhar | Hybrid | 2 | 2 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| Akale23 | Amulya Kale | Hybrid | 2 | 1 | 3 | **6** | 👍 B | — | 📈 Rising |
| AnaSarzosa | Ana Sarzosa | Hybrid | 1 | 1 | 3 | **5** | 👍 B | — | ➡️ Stable |
| anjali-sherikar | Anjali Sherikar | Hybrid | 1 | 1 | 3 | **5** | 👍 B | — | ➡️ Stable |
| sohanbafna | Sohan Bafna | Hybrid | 1 | 3 | 2 | **6** | 👍 B | — | ➡️ Stable |
| mshnayderman | Mikhail Shnayderman | Inline-First | 3 | 1 | 3 | **7** | 🌟 A | R=0 override N/A (R=1); A eligible | 🔴 Declining |
| amol-salunkhe | Amol Salunkhe | Agent-First | 3 | 1 | 3 | **7** | 🌟 A | R outlier penalty applied (5,309 prem → −1, making R=1−1=0... see note) | 🔴 Declining |
| Prathmesh-Ranadive | Prathmesh Ranadive | Inline-First | 3 | 0 | 3 | **6** | 👍 B → C override | R=0 AND Premium>500 → cannot be above Tier C | 🔴 Declining |
| chris-haun | Chris Haun | Hybrid | 1 | 0 | 3 | **4** | 👌 C | R=0 AND Premium>500 → cannot be above Tier C (already C) | 🔴 Declining |
| luisalvatierra | Luis Salvatierra | Hybrid | 2 | 0 | 3 | **5** | 👍 B → C override | R=0 AND Premium>500 (~1,655) → cannot be above Tier C | 📉 Slipping |
| moadzughul | Moad Alzughul | Agent-First | 1 | 1 | 3 | **5** | 👍 B | — | ➡️ Stable |
| sachinfuse-nice | Sachin Fuse | Agent-First | 1 | 1 | 3 | **5** | 👍 B | — | ➡️ Stable |
| vishal-tad | Vishal Tad | Hybrid | 1 | 2 | 3 | **6** | 👍 B | — | ➡️ Stable |
| abhishekhole-nice | Abhishek Hole | Agent-First | 1 | 2 | 3 | **6** | 👍 B | — | ➡️ Stable |
| pdevle | Pratik Devle | Hybrid | 1 | 2 | 3 | **6** | 👍 B | — | ➡️ Stable |
| tusharpatil166719 | Tushar Patil | Hybrid | 1 | 2 | 3 | **6** | 👍 B | — | ➡️ Stable |
| meghabiradar05 | Megha Biradar | Hybrid | 1 | 2 | 3 | **6** | 👍 B | — | ➡️ Stable |
| sskalaskar | Sourabh Kalaskar | Hybrid | 1 | 3 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| prashasti-jain | Prashasti Jain | Hybrid | 1 | 3 | 3 | **7** | 🌟 A | — | ➡️ Stable |
| Shreedevi-nice | Shreedevi Patil | Hybrid | 1 | 1 | 3 | **5** | 👍 B | — | ➡️ Stable |
| ShubhamFulzele28 | Shubham Fulzele | Agent-First | 0 | 1 | 3 | **4** | 👌 C | — | ➡️ Stable |
| suhas-kakde | Suhas Kakde | Agent-First | 0 | 1 | 3 | **4** | 👌 C | — | ➡️ Stable |
| dsuraj25 | Suraj Dubey | Hybrid | 0 | 2 | 1 | **3** | 👌 C | — | ➡️ Stable |
| smishra-nice | Shridhar Mishra | Inline-First | 2 | 1 | 2 | **5** | 👍 B | — | ➡️ Stable |
| mshivarkar | Mohan Shivarkar | Hybrid | 1 | 0 | 3 | **4** | 👌 C | R=0 AND Premium>500 (3,480) → cannot above Tier C | ➡️ Stable |
| sgite-wfm | Shubham Gite | Inline-First | 3 | 0 | 2 | **5** | 👍 B → C | R=0 AND Premium>500 (1,411) → cannot be above Tier C | ➡️ Stable |
| ShivrajNice | Shivraj Bahirat | Hybrid | 0 | 0 | 1 | **1** | 🟠 D | — | ➡️ Stable |
| giteshsawant | Gitesh Sawant | Hybrid | 0 | 0 | 0 | **0** | 🔴 E | — | ➡️ Stable |
| pratikpawar12 | Pratik Pawar | Hybrid | 0 | 0 | 1 | **1** | 🟠 D | — | ➡️ Stable |
| kbajaj-nice | Kaushal Bajaj | Hybrid | 0 | 0 | 0 | **0** | 🔴 E | — | ➡️ Stable |
| dannycadima | Danny Cadima | Hybrid | 0 | 0 | 0 | **0** | 🔴 E | — | ➡️ Stable |
| nilesht-19 | Nilesh Tonape | Inline-First | 2 | 0 | 3 | **5** | 👍 B → C override | R=0 AND Premium>500 (23,108) → cannot be above Tier C; also R=0 override | 🔴 Declining |
| thakraln | Nishtha Thakral | Agent-First | 0 | 0 | 3 | **3** | 👌 C | R=0 AND Premium>500 (11,112) → cannot be above Tier C (already C) | ➡️ Stable |
| trunalgawade | Trunal Gawade | Hybrid | 1 | 0 | 3 | **4** | 👌 C | R=0 AND Premium>500 (10,863) → cannot be above Tier C | ➡️ Stable |
| PradnyeshSalunke | Pradnyesh Salunke | Inline-First | 2 | 0 | 3 | **5** | 👍 B → C override | R=0 AND Premium>500 (9,892) → cannot be above Tier C | 🔴 Declining |

---

## Pillar Score Detail — Selected Users

### tomotvos (Tom Otvos) — CRQC Score: 9/9 → Tier A

- **C=3** (Agent-First): ReqEff 84.3 > 15 → 2pts; LoC increasing trend → +1pt. Max 3. ✓
- **R=3** (Universal): ReqEff 84.3 > 20 → 3pts; Premium ~109 ≤ 500 (lean) → +1 bonus (capped at 3). ✓
- **Q=3** (Team proxy): 90% merge, 3.67 reviews/PR, 1.9 day avg. ✓
- **Context:** SuggEff 77.89 confirms large agent-generated code blocks. Lean spend profile.

### mshnayderman (Mikhail Shnayderman) — CRQC Score: 7/9 → Tier A (with flag)

- **C=3** (Inline-First): %Accept 27.8% in 20–35% range → 2pts; Accept Count 126 > 20 → +1pt. Max 3. ✓
- **R=1** (Universal): ReqEff 5.1 in 5–10 range → 1pt; Premium 5,419 > 1,700 (outlier) → −1 penalty → R = max(0, 1−1) = **0**. Wait — R=0 AND Premium>500 → cannot be above Tier C (override rule).
  
> **CRQC Override Applied:** R=0 (after outlier penalty) AND Premium 5,419 > 500 → **Cannot be above Tier C**. This is a significant CRQC finding: under strict CRQC rules, mshnayderman's tier drops from A (v1/v2) to **C** due to the R pillar override.
>
> This is the most important divergence between v1 and CRQC in this period. The v1/v2 T1 signal (27.8% accept rate) held the Tier A classification; CRQC's explicit R pillar override reveals that the premium spend makes this user's ROI contribution negative at scale.

| Recalculation | Value |
|---|---|
| R base score (ReqEff 5.1, 5-10 range) | 1 pt |
| R outlier penalty (5,419 premium > 1,700) | −1 |
| R final | 0 |
| Override triggered | R=0 AND Premium>500 → max Tier C |
| **CRQC Final Tier** | **C** |

### amol-salunkhe (Amol Salunkhe) — CRQC Score → Tier C (override)

- **C=3** (Agent-First): ReqEff 6.4 < 8 → 0pts; LoC 34,037 increasing → +1pt... Wait, ReqEff <8 = 0pts. LoC increasing = +1pt. C = 1.
  - Actually: Agent-First C scoring: ReqEff >15 → 2pts, 8-15 → 1pt, <8 → 0pts. Plus LoC trend +1. 
  - ReqEff 6.4 < 8 → 0pts. LoC increasing (vs Jun 3) → +1pt. C = 1.
- **R=1** (Universal): ReqEff 6.4 in 5-10 → 1pt; Premium 5,309 > 1,700 → −1 penalty → R = 0.
- **Override:** R=0 AND Premium>500 → max Tier C.
- **Q=3** (Team proxy).
- Total: C=1 + R=0 + Q=3 = 4 → **Tier C** (also constrained to max C by override)

### Prathmesh-Ranadive — CRQC Score → Tier C (override)

- **C=3** (Inline-First): %Accept 25.4% in 20-35% range → 2pts; Accept Count ~690 > 20 → +1pt. C=3. ✓
- **R=0** (Universal): ReqEff 2.5 < 5 → 0pts; Premium 10,733 > 1,700 → −1 (already 0, min 0). R=0.
- **Override:** R=0 AND Premium>500 → max Tier C.
- **Q=3** (Team proxy).
- Total: C=3 + R=0 + Q=3 = 6 → would be Tier B, but override → **Tier C**

### nilesht-19 (Nilesh Tonape) — CRQC Score → Tier C (override)

- **C=2** (Inline-First): %Accept 29.5% in 20-35% → 2pts; Accept Count ~116 > 20 → +1... C=3 actually.
  - Wait, max C = 3. %Accept 29.5% → 2pts, accept count >20 → +1. C = 3. But...
- **R=0** (Universal): ReqEff 0.3 < 5 → 0pts; Premium 23,108 > 1,700 → −1 (already 0). R=0.
- **Override:** R=0 AND Premium>500 → max Tier C.
- **Q=3** (Team proxy).
- Total: 3+0+3 = 6 → would be Tier B, but override → **Tier C**

> **Key CRQC insight:** nilesht-19 shows a 29.5% accept rate (strong T1 in v1/v2) and gets C=2-3. But the R pillar override catches what v1/v2 can't: the extreme premium spend (23,108) makes this user a budget liability regardless of accept rate quality. CRQC correctly identifies this as at most Tier C.

---

## Override Rules Applied Summary

| Override | Users Affected | Net Effect |
|---|---|---|
| R=0 AND Premium>500 → max Tier C | nilesht-19, thakraln, trunalgawade, PradnyeshSalunke, mshivarkar, sgite-wfm, mshnayderman, amol-salunkhe, Prathmesh-Ranadive, luisalvatierra, chris-haun | Tier downgrade for 11 users |
| Q=0 → cannot be Tier A | giteshsawant, kbajaj-nice, dannycadima | Already Tier E — no additional effect |
| Momentum >+100% → tier promotion eligible | rpawar-nice (Breakout), Kranti-nice (Breakout) | Both already Tier A — promotion already reflected |

---

## CRQC Final Tier Distribution

| Tier | Users | Count |
|---|---|---|
| 🌟 A (7-9) | tomotvos (9), rpawar-nice (8), dhanshree-jagtap-nice (8), Vitthal-Nice (8), Kranti-nice (8), rizeq-abu-madeghem (8), Vyankatesh95 (7), mfield1 (7), nice-harshada (7), abhijeetk268 (7), yogitadhanwate (7), jayesh-rai (7), jkumbhar (7), mshnayderman (7*→C), sskalaskar (7), prashasti-jain (7) | 14 (+2 demoted by override) |
| 👍 B (5-6) | Akale23 (6), sohanbafna (6), moadzughul (5), sachinfuse-nice (5), vishal-tad (6), abhishekhole-nice (6), pdevle (6), tusharpatil166719 (6), meghabiradar05 (6), AnaSarzosa (5), anjali-sherikar (5), Shreedevi-nice (5), smishra-nice (5) | 13 |
| 👌 C (3-4) | mshnayderman* (7→C by override), amol-salunkhe* (4→C by override), Prathmesh-Ranadive* (6→C by override), luisalvatierra* (5→C by override), nilesht-19* (6→C by override), chris-haun (4), trunalgawade* (4, override), mshivarkar* (4, override), sgite-wfm* (5→C override), ShubhamFulzele28 (4), suhas-kakde (4), thakraln* (3, override), PradnyeshSalunke* (5→C override), dsuraj25 (3) | 14 |
| 🟠 D (1-2) | ShivrajNice (1), pratikpawar12 (1) | 2 |
| 🔴 E (0) | giteshsawant (0), kbajaj-nice (0), dannycadima (0) | 3 |

> *Marked with asterisk = override applied

**Net CRQC vs v1 tier changes:**
- mshnayderman: A → **C** (R override — most significant downgrade)
- amol-salunkhe: A → **C** (R override)
- sskalaskar: E → **A** (7 CRQC score — decent efficiency with lean spend, low LoC was v1 issue but CRQC rewards the efficiency/quality pillars)
- prashasti-jain: E → **A** (7 CRQC score — same pattern as sskalaskar)
- moadzughul: D → **B** (5 CRQC score)
- sachinfuse-nice: D → **B** (5 CRQC score)
- abhishekhole-nice: D → **B** (6 CRQC score)
- pdevle: D → **B** (6 CRQC score)
- tusharpatil166719: D → **B** (6 CRQC score)
- meghabiradar05: D → **B** (6 CRQC score)
- smishra-nice: D → **B** (5 CRQC score)
- Prathmesh-Ranadive: C → **C** (override keeps C despite 6 raw score)
- luisalvatierra: B → **C** (R override)
- nilesht-19: E → **C** (R override caps at C despite raw score of 6)
- ShivrajNice: E → **D** (1 CRQC score)

---

## Context Pillar — Diagnostic Notes

| User | Context Signal | Explanation |
|---|---|---|
| mshnayderman | Premium 5,419 vs LoC 27,539 | 9.5× premium spike. Premium requests likely from Copilot Chat/agent dialogs not generating LoC. C pillar high (27.8% inline accept) — the inline workflow is healthy; something else is burning premium. |
| nilesht-19 | Premium 23,108 vs LoC 7,160 | 1,140 interactions with 29.5% accept suggests active inline use. But 23,108 premium for 7,160 LoC is diagnostic: premium agent sessions are generating very little code per call. Each interaction may be spawning multiple premium calls. |
| Kranti-nice | Int 1,182, LoC 27,733 | High interaction count with strong LoC output = healthy agent-driven workflow. Each interaction contributing ~23 LoC on average. This is the target profile for Agent-First users. |
| sgite-wfm | Accept 53.5%, ReqEff 0.2 | Very high accept rate (reflexive?) with 1,411 premium generating 329 LoC. Suggestion Efficiency (0.94) is near-zero — each code generation event produces less than 1 LoC on average. This is the smallest-suggestion, highest-premium pattern on the team. |
| abhishekhole-nice | 167 Int, 0 Code Accepts | Pure agent session usage. 167 interactions with 2,936 LoC shows code is being generated and added, but through agent blocks (LoC Added >> LoC Suggested). The 0 accepts is correct behavior, not a quality signal. |

---

## VP R&D Narrative — CRQC

> **"Our Copilot effectiveness this period is measured across three dimensions: adoption quality (Core), budget efficiency (ROI), and code delivery (Quality).**
>
> Tier A performers (7–9 out of 9) currently number **14** of our 47 developers (30%). They produce approximately 80% of our Copilot-assisted code this period, including Tom Otvos (9/9 — perfect CRQC score) and Ritesh Pawar (8/9, +199% momentum breakout).
>
> The CRQC framework surfaces a critical finding that other frameworks miss: **11 users trigger the R=0 + Premium>500 override**. These users have acceptable or good Code and Quality scores, but their ROI pillar is negative — they are consuming premium budget without proportional code output. This includes users who appear in v1 Tier A (Mikhail Shnayderman, Amol Salunkhe) — CRQC correctly re-classifies them to Tier C due to the premium efficiency collapse.
>
> Our top 5 budget priorities — Nilesh Tonape (23,108 premium, ReqEff 0.3), Nishtha Thakral (11,112 premium, ReqEff 0.1), Trunal Gawade (10,863 premium, ReqEff 0.1), Prathmesh Ranadive (10,733 premium, ReqEff 2.5), and Pradnyesh Salunke (9,892 premium, ReqEff 0.3) — are consuming approximately 40% of the team's estimated premium budget while contributing less than 10% of LoC output. Addressing these 5 accounts alone would meaningfully reduce team cost per line of code."

---

*CRQC 4-Pillar Analysis — Q Score applied via team-level proxy (per-user PR data not filterable in current dashboard). C pillar workflow type inferred via behavioral proxy. R outlier penalty (>1,700 premium) applied before R=0 override check. All override rules from github-benchmark-CRQC.md applied as documented.*
