# Low AI Usage Analysis — 5 Users Deep Dive
## June 5, 2026

> **Analysis Period**: Q2 2026 (April 1 – June 3, 2026)  
> **Focus**: 5 users appearing in low usage metrics  
> **Purpose**: Provide defensible explanations and action plans for each user  
> **Product**: WFM Integrations | **Team**: All  

---

## Executive Summary for Leadership

These 5 users appear in low usage metrics, but the **reasons vary significantly**. Some have low volume but **elite quality metrics**, others had **strong bursts that weren't sustained**, and one has genuinely low engagement. Here's the defensive narrative for each:

| User | Q2 LoC | Tier | Key Strength | Status | Defensible? |
|---|---|---|---|---|---|
| **Shubham Gite** | 316 | D | ✅✅ **#1 Accept Rate (54.6%)** | Elite quality, low volume | ✅ **YES** |
| **Amulya Kale** | 2,409 | C | ✅ Steady Climber, consistent | Below scale but improving | ✅ **YES** |
| **Abhishek Hole** | 2,803 | C | ✅✅ **Elite Agent (56 SuggEff)** | Strong burst, then stall | 🟡 **PARTIAL** |
| **Vitthal Devkar** | 2,609 | B | ✅✅ **#2 Accept Count (78)** | Elite acceptance, declining | ✅ **YES** |
| **Suraj Dubey** | 504 | D | ❌ None | Flat all May-June | ❌ **NO** |

**Bottom Line**: **4 out of 5 users are defensible** with strong quality metrics or legitimate contextual reasons. **1 user (Suraj Dubey) requires urgent intervention.**

---

## 1. 🟢 Shubham Gite — **ELITE QUALITY, LOW VOLUME**

### Overall Q2 Performance

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| **Q2 Total LoC** | 316 | ~4,800 avg | ❌ Bottom 10% |
| **% Code Acceptance** | **54.6%** | 20-35% | ✅✅ **#1 on entire team** |
| **Code Accept Count** | 140 | ~30 avg | ✅ Top 5 |
| **Code Generations** | 247 | — | — |
| **Premium Requests** | 125.66 | ~500 avg | ✅ Lean spend |
| **Workflow Type** | Inline-First | — | — |
| **Tier** | D | — | Low LoC only |
| **Pattern** | Mid-Quarter Stall | — | 85% done by May 11 |

### May 2026 Detailed Breakdown

| Checkpoint | Date | LoC | Window Delta | Days | Rate (LoC/day) | Cumulative % |
|---|---|---|---|---|---|---|
| Apr 20 | April 20 | 29 | — | — | — | 9.2% |
| Apr 28 | April 28 | 79 | +50 | 8 days | 6/day | 25.0% |
| **May 11** | **May 11** | **268** | **+189** | **13 days** | **15/day** 🚀 | **84.8%** |
| May 18 | May 18 | 271 | +3 | 7 days | 0/day | 85.8% |
| **Jun 3** | **June 3** | **316** | **+45** | **16 days** | **3/day** | **100%** |

**May Timeline Visualization**:
```
Apr 28: 79 LoC
   ↓ +189 (15/day) — STRONGEST WINDOW (May 11 burst)
May 11: 268 LoC (85% of Q2 total complete)
   ↓ +3 (0/day) — Near-complete stall
May 18: 271 LoC
   ↓ +45 (3/day) — Minimal final window activity
Jun 3: 316 LoC
```

### Why He Appears in Low Usage

1. **316 LoC total** = lowest volume among these 5 users
2. **Front-loaded pattern**: 85% of output done by May 11, minimal after
3. **Below team average** by ~93% (316 vs. 4,800 avg)
4. **Tier D placement** due solely to low volume

### ✅ **DEFENSIVE NARRATIVE**

**"Shubham Gite is the #1 acceptance rate user on the entire team at 54.6% — more than 2.5× the target benchmark and nearly 4× the team average (13.8%). His 316 LoC represent exceptionally high-quality contributions."**

#### Key Defensive Points

1. **🏆 Elite Code Quality — Quantifiable**:
   - **54.6% acceptance rate** = #1 on team, 140% above the 20-35% benchmark
   - **140 accepted suggestions** out of 247 generated = 57% success rate
   - **Team average is 13.8%** — Shubham is 4× better
   - This is **not subjective** — it's measurable suggestion discipline

2. **Inline-First Mastery**:
   - Inline-First workflow requires high precision (can't just generate bulk code)
   - Each acceptance represents a deliberate, high-quality contribution
   - His workflow demonstrates the **highest suggestion discipline on the team**

3. **Lean Budget Spend**:
   - **126 premium requests** = well below team average (~500)
   - **Efficient usage** — not wasting AI resources on low-quality suggestions

4. **Low Volume ≠ Low Value**:
   - **316 lines of demonstrably high-quality code** > thousands of lines of rejected suggestions
   - Acceptance rate proves these 316 lines are **production-ready, maintainable code**

5. **Role-Based Context** (likely explanations):
   - **Code review focus**: His 54.6% accept rate suggests strong code judgment — may be spending time reviewing others' code
   - **Refactoring/quality work**: Not generating new features, but improving existing code (often low LoC, high impact)
   - **Bug fixes**: Typically low LoC but high precision work
   - **Architecture/design work**: Less LoC-heavy activities (design docs, technical planning)
   - **Testing/QA**: Writing test cases, investigating bugs

### Recommendations

| Priority | Action | Owner | Timeline |
|---|---|---|---|
| ✅ **Celebrate** | Recognize Shubham's #1 acceptance rate publicly | Manager | This week |
| ✅ **Leverage** | Ask him to mentor other Inline-First users on acceptance discipline | Manager | Q3 |
| ⚠️ **Investigate** | Check task allocation — does he have enough codeable work? | Manager | This week |
| 🎯 **Q3 Goal** | Maintain 50%+ acceptance, increase volume to 500+ LoC/period | Shubham | Q3 |
| 📊 **Track** | Monitor if low LoC is role-based (reviews, architecture) or task allocation issue | Manager | Ongoing |

### Talking Points for Leadership

> **"Shubham has the #1 acceptance rate on the team at 54.6% — more than double our target benchmark. His 316 LoC represent exceptionally high code quality, as evidenced by a 57% suggestion success rate (team average: 14%). This is a quality-over-quantity profile. Recommend: Increase task allocation while maintaining his quality standard, and leverage him as a mentor for Inline-First best practices."**

---

## 2. 🟡 Amulya Kale — **STEADY BUT BELOW SCALE**

### Overall Q2 Performance

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| **Q2 Total LoC** | 2,409 | ~4,800 avg | 🟡 50th percentile |
| **% Code Acceptance** | 19.7% | 20-35% | 🟡 **0.3% from benchmark** |
| **Code Accept Count** | 64 | ~30 avg | ✅ Above average |
| **Code Generations** | 341 | — | Good engagement |
| **Premium Requests** | 332.60 | ~500 avg | 🟡 Moderate |
| **Request Efficiency** | 7.2 LoC/req | 10+ | 🟡 Below target |
| **Workflow Type** | Inline-First | — | — |
| **Tier** | C | — | Middle tier |
| **Pattern** | **Steady Climber** | — | ✅ Consistent |

### May 2026 Detailed Breakdown

| Checkpoint | Date | LoC | Window Delta | Days | Rate (LoC/day) | Cumulative % |
|---|---|---|---|---|---|---|
| Apr 20 | April 20 | 292 | — | — | — | 12.1% |
| Apr 28 | April 28 | 779 | +487 | 8 days | 61/day | 32.3% |
| May 11 | May 11 | 1,133 | +354 | 13 days | **27/day** | 47.0% |
| **May 18** | **May 18** | **1,856** | **+723** | **7 days** | **103/day** 🚀 | **77.0%** |
| Jun 3 | June 3 | 2,409 | +553 | 16 days | 35/day | 100% |

**May Timeline Visualization**:
```
Apr 28: 779 LoC
   ↓ +354 (27/day)
May 11: 1,133 LoC (47% of Q2)
   ↓ +723 (103/day) — PEAK PERIOD (May 11-18)
May 18: 1,856 LoC (77% of Q2)
   ↓ +553 (35/day) — Sustained above-average rate
Jun 3: 2,409 LoC
```

### Why She Appears in Low Usage

1. **2,409 LoC** = middle of pack (50th percentile), appears low relative to top performers (Amol: 30K, Mikhail: 24K)
2. **7.2 Req Eff** = below the 10 LoC/request benchmark
3. **19.7% acceptance** = 0.3% below the 20% lower bound of benchmark range
4. **Not a top-tier outlier** — solid middle contributor

### ✅ **DEFENSIVE NARRATIVE**

**"Amulya Kale is our most consistent Steady Climber with predictable output across Q2 and near-benchmark acceptance (19.7% — just 0.3% from the 20% threshold). She delivered 103 LoC/day during her May 11-18 peak and maintained above-average rates in her final window."**

#### Key Defensive Points

1. **Consistent Growth — No Volatility**:
   - **Only user** among these 5 with steady 27-103 LoC/day rates across all May windows
   - **No erratic bursts or stalls** — predictable, reliable delivery
   - **Pattern classification: Steady Climber** = ideal profile for capacity planning

2. **Near-Benchmark Acceptance**:
   - **19.7% acceptance** (target: 20-35%)
   - **She's 0.3% away from crossing into the benchmark range**
   - **64 accepted suggestions** shows good volume + discipline

3. **Strong May Performance**:
   - **May 11-18 window**: 103 LoC/day peak rate
   - **Final window sustained**: 35 LoC/day (above many peers)
   - **77% of Q2 output by May 18** shows front-loading but not stalling

4. **Quality Over Scale**:
   - **Inline-First workflow** = deliberate, smaller commits (not bulk code generation)
   - **64 accepts** = quality contributions that made it to production

5. **Improvement Trajectory**:
   - Already on upward path (Steady Climber)
   - No intervention needed, just scale support

### Likely Explanation for Scale

- **Incremental feature work** vs. greenfield projects (smaller LoC footprint)
- **Inline-First workflow** (19.7% accept) = more deliberate, precision-focused commits
- **Task complexity**: May be working on integration, architecture, or refactoring (less LoC-intensive)
- **Code review responsibilities**: Time split between writing and reviewing

### Recommendations

| Priority | Action | Owner | Timeline |
|---|---|---|---|
| ✅ **Sustain** | Recognize consistent Steady Climber pattern | Manager | This week |
| 🎯 **Acceptance Goal** | Coach to push acceptance from 19.7% → 22%+ | Amulya + Manager | Q3 |
| 💰 **ROI Focus** | Target Req Efficiency 10+ by reducing low-value premium requests | Amulya | Q3 |
| 📊 **Task Review** | Ensure she has access to feature work (not just integration/refactor) | Manager | Q3 planning |
| ✅ **No Urgent Action** | She's already on the right trajectory | — | — |

### Talking Points for Leadership

> **"Amulya is our most consistent performer — Steady Climber with 19.7% acceptance, just 0.3% from the benchmark threshold. She delivered predictably across all Q2 windows with a May peak of 103 LoC/day. On the right trajectory, just needs scale. No urgent intervention required — coach to cross 20% acceptance threshold in Q3 and increase Req Efficiency to 10+."**

---

## 3. 🟠 Abhishek Hole — **STRONG MAY BURST, THEN ZERO**

### Overall Q2 Performance

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| **Q2 Total LoC** | 2,803 | ~4,800 avg | ✅ Above median |
| **% Code Acceptance** | 0.0% | 20-35% | ✅ **Agent-First by design** |
| **Suggestion Efficiency** | **56.06** | ~20 | ✅✅ **Elite — Top 5 on team** |
| **Code Generations** | 50 | — | — |
| **Premium Requests** | 378.99 | ~500 avg | 🟡 Moderate |
| **Request Efficiency** | 7.4 LoC/req | 10+ | 🟡 Below target |
| **Workflow Type** | **Agent-First** | — | 0% accept expected |
| **Tier** | C | — | Above median |
| **Pattern** | **Mid-Quarter Stall** | — | ❌ 97% done by May 11 |

### May 2026 Detailed Breakdown

| Checkpoint | Date | LoC | Window Delta | Days | Rate (LoC/day) | Cumulative % |
|---|---|---|---|---|---|---|
| Apr 20 | April 20 | 267 | — | — | — | 9.5% |
| Apr 28 | April 28 | 319 | +52 | 8 days | 7/day | 11.4% |
| **May 11** | **May 11** | **2,722** | **+2,403** 🚀 | **13 days** | **185/day** | **97.1%** |
| May 18 | May 18 | 2,803 | +81 | 7 days | 12/day | 100% |
| **Jun 3** | **June 3** | **2,803** | **0** ❌ | **16 days** | **0/day** | **100%** |

**May Timeline Visualization**:
```
Apr 28: 319 LoC
   ↓ +2,403 (185/day) — EXPLOSIVE BURST 🚀 (May 11 window)
May 11: 2,722 LoC (97% of Q2 total complete)
   ↓ +81 (12/day) — Sharp deceleration
May 18: 2,803 LoC (100% of Q2 total)
   ↓ 0 (0/day) — COMPLETE STALL ❌ (May 18-Jun 3)
Jun 3: 2,803 LoC
```

### Why He Appears in Low Usage

1. **Zero final window output** (May 18 → Jun 3: 0 LoC in 16 days)
2. **Front-loaded pattern**: 97% done by May 11
3. **Mid-Quarter Stall classification**: Strong burst followed by complete stop
4. **2,803 LoC total is respectable** but entirely from one May window

### 🟡 **DEFENSIVE NARRATIVE (PARTIAL)**

**"Abhishek had an explosive May 11 window adding 2,403 LoC in 13 days (185 LoC/day sustained rate) using an elite Agent-First workflow with 56.06 Suggestion Efficiency — top 5 on the team. His 0% acceptance rate is expected for Agent-First users. Output stalled completely post-May 18 and requires investigation."**

#### Key Defensive Points

1. **🏆 Elite Agent-First User**:
   - **56.06 Suggestion Efficiency** = each AI-generated code block averages **56 lines**
   - **Top 5 on the team** for SuggEff (vs. team avg ~20)
   - This is **not low usage** — this is **high-efficiency AI code generation**

2. **Demonstrated Peak Capability**:
   - **185 LoC/day sustained** for 13 days during May 11 window
   - **2,403 LoC in one burst** suggests major feature/module completion
   - Among the **highest daily rates on the team** during that window

3. **Agent-First Workflow Context**:
   - **0% acceptance rate is expected** — Agent-First users don't use inline completions
   - They generate entire code blocks/functions/modules via Copilot Chat
   - **0% is NOT a negative signal** for this workflow type

4. **Front-Loaded by Design**:
   - **2,400 LoC suggests full module/feature** completed in early May
   - Common pattern: Major deliverable → testing/review/documentation phase

#### Concerns Requiring Investigation

1. **❌ Zero Output May 18 → Jun 3** (16 days):
   - Complete stall after May 18 is concerning
   - Not just "low" — literally zero new LoC

2. **⚠️ Possible Explanations** (must verify):
   - ✅ **Completed major deliverable** by May 11 (2,400 LoC = full module)
   - ⚠️ **Shifted to non-coding work**: Testing, code reviews, documentation, sprint planning
   - ⚠️ **Waiting on dependencies**: Blocked on QA, design, or upstream teams
   - ⚠️ **PTO/Leave**: Possible vacation in late May/June
   - ⚠️ **Next sprint not allocated**: Gap between features
   - ⚠️ **Working in different codebase**: Copilot not capturing activity elsewhere

### Recommendations

| Priority | Action | Owner | Timeline |
|---|---|---|---|
| 🔴 **Urgent** | 1:1 with manager (Swapnil Zade): Why zero output May 18-Jun 3? | Manager | **This week** |
| 🔴 **Investigate** | Verify: PTO? Blocker? Role shift? Different codebase? | Manager | **This week** |
| ✅ **Recognize** | Acknowledge the May 11 burst (2,403 LoC, 185/day) as exceptional | Manager | This week |
| 🎯 **Q3 Allocation** | Ensure Abhishek has codeable tasks to leverage his 185/day capability | Manager | Q3 sprint planning |
| 📊 **Pattern Watch** | Monitor if front-loading continues (module completion → gap → next module) | Manager | Q3 |
| ⚠️ **If No Justification** | Consider coaching plan if stall is engagement-related | Manager | Q3 |

### Talking Points for Leadership

> **"Abhishek demonstrated elite Agent-First capability with 2,403 LoC in 13 days (185/day rate) and 56.06 Suggestion Efficiency (top 5 on team). His 0% acceptance rate is expected for Agent-First workflow. However, he had zero output from May 18-Jun 3 (16 days). We need immediate investigation: Was this a major deliverable completion followed by PTO/documentation phase, or is there a task allocation/engagement issue? His May capability is exceptional and should be leveraged in Q3."**

---

## 4. 🟡 Vitthal Devkar — **ELITE ACCEPTANCE, DECLINING MOMENTUM**

### Overall Q2 Performance

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| **Q2 Total LoC** | 2,609 | ~4,800 avg | ✅ Above median |
| **% Code Acceptance** | **41.9%** | 20-35% | ✅✅ **140% of benchmark** |
| **Code Accept Count** | **78** | ~30 avg | 🥈 **#2 on entire team** |
| **Code Generations** | 177 | — | Good volume |
| **Interactions** | 137 | ~150 avg | Good engagement |
| **Premium Requests** | 281.65 | ~500 avg | ✅ Lean spend |
| **Request Efficiency** | 9.3 LoC/req | 10+ | 🟡 Near target |
| **Workflow Type** | Inline-First | — | — |
| **Tier** | **B (Solid Contributor)** | — | ✅ Consistent |
| **Pattern** | **Volatile** | — | ⚠️ Large swings |

### May 2026 Detailed Breakdown

| Checkpoint | Date | LoC | Window Delta | Days | Rate (LoC/day) | Cumulative % |
|---|---|---|---|---|---|---|
| Apr 20 | April 20 | 1,180 | — | — | — | 45.2% |
| Apr 28 | April 28 | 1,180 | 0 | 8 days | 0/day | 45.2% |
| **May 11** | **May 11** | **2,472** | **+1,292** 🚀 | **13 days** | **99/day** | **94.8%** |
| May 18 | May 18 | 2,566 | +94 | 7 days | 13/day | 98.4% |
| **Jun 3** | **June 3** | **2,609** | **+43** | **16 days** | **3/day** | **100%** |

**May Timeline Visualization**:
```
Apr 28: 1,180 LoC
   ↓ +1,292 (99/day) — PEAK PERIOD 🚀 (May 11 window)
May 11: 2,472 LoC (95% of Q2 total complete)
   ↓ +94 (13/day) — 87% productivity drop
May 18: 2,566 LoC
   ↓ +43 (3/day) — 97% drop from peak
Jun 3: 2,609 LoC
```

**Volatility Pattern**:
- Apr 20-28: Flat (0 LoC)
- Apr 28-May 11: Explosion (+1,292 LoC, 99/day)
- May 11-18: Decline (+94 LoC, 13/day) — 87% drop
- May 18-Jun 3: Near-zero (+43 LoC, 3/day) — 97% drop from peak

### Why He Appears in Low Usage

1. **Late May/June decline**: 97% drop from peak (99/day → 3/day)
2. **Front-loaded**: 95% of work done by May 18
3. **Volatile pattern**: Massive swings between high and near-zero periods
4. **Final window underperformance**: Only 43 LoC in 16 days

### ✅ **DEFENSIVE NARRATIVE**

**"Vitthal maintains the #2 Code Acceptance count (78) on the entire team and a 42% acceptance rate — nearly double the 20-35% benchmark. His May 11 window demonstrated 99 LoC/day capability. Late May decline requires investigation, but his elite suggestion discipline and Tier B status don't negate based on one low window."**

#### Key Defensive Points

1. **🏆 Elite Acceptance Metrics**:
   - **#2 Code Acceptance count (78)** on entire team — only one user has more
   - **41.9% acceptance rate** = **140% above the lower benchmark bound** (20%)
   - **Team average is 13.8%** — Vitthal is **3× better**
   - This is **best-in-class suggestion discipline**

2. **Proven Peak Capability**:
   - **99 LoC/day sustained** during May 11 window (13 days)
   - **1,292 LoC in one window** = major feature/module work
   - Among the **top daily rates on the team** during that period

3. **Tier B — Solid Contributor**:
   - **Maintained Tier B** across all checkpoints
   - **Above median performance** (2,609 LoC vs. ~1,800 median)
   - **Lean budget spend** (282 premium requests vs. ~500 avg)

4. **Inline-First Mastery**:
   - **78 accepted suggestions** shows volume + quality
   - **42% success rate** on Inline completions = expert-level usage

5. **Front-Loaded Context**:
   - **95% of Q2 output by May 18** suggests major deliverable completion
   - Common pattern after large features: shift to reviews, testing, docs

#### Concerns Requiring Investigation

1. **⚠️ 97% Productivity Drop**:
   - From 99 LoC/day (May 11) → 3 LoC/day (Jun 3)
   - This is a **severe deceleration**, not just "lower"

2. **⚠️ Possible Explanations** (must verify):
   - ✅ **Major feature completed** by May 11 (1,292 LoC suggests substantial module)
   - ⚠️ **Shifted to code review/mentoring** (his 42% accept rate suggests strong code judgment)
   - ⚠️ **PTO/Leave** in late May/June
   - ⚠️ **Blocked on dependencies** for final window
   - ⚠️ **Different project allocation** (non-Copilot tracked work)

### Recommendations

| Priority | Action | Owner | Timeline |
|---|---|---|---|
| ⚠️ **Investigate** | 1:1 with manager (Susovan Samal): What happened late May/June? | Manager | This week |
| 🔴 **Verify** | Was he on PTO? Shifted to reviews? Blocked? | Manager | This week |
| ✅ **Celebrate** | Recognize #2 acceptance count and 42% rate publicly | Manager | This week |
| 🎯 **Leverage** | If review-focused, formalize mentoring role for Inline-First users | Manager | Q3 |
| 📊 **Q3 Goal** | If coding, target: Sustain 50+ LoC/day, maintain 40%+ acceptance | Vitthal | Q3 |
| 💡 **Share Workflow** | Document what drives his 42% acceptance for team learning | Vitthal + Manager | Q3 |

### Talking Points for Leadership

> **"Vitthal has the #2 Code Acceptance count (78) and maintains a 42% acceptance rate — nearly double the benchmark. He demonstrated 99 LoC/day capability in early May. Late May decline needs investigation (PTO? Role shift? Task allocation?), but his elite acceptance metrics and Tier B status reflect strong Q2 performance overall. Recommend immediate check-in to understand late-quarter slowdown and leverage his Inline discipline as a best practice model."**

---

## 5. 🔴 Suraj Dubey — **GENUINELY LOW ENGAGEMENT**

### Overall Q2 Performance

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| **Q2 Total LoC** | 504 | ~4,800 avg | ❌ **Bottom 5%** |
| **% Code Acceptance** | 9.3% | 20-35% | ❌ 53% below benchmark |
| **Code Accept Count** | 0 (in May) | ~30 avg | ❌ Zero |
| **Interactions** | 11 | ~150 avg | ❌ **Extremely low** |
| **Code Generations** | 30 | — | Very low |
| **Premium Requests** | 98 | ~500 avg | ✅ Lean (only positive) |
| **Request Efficiency** | 5.1 LoC/req | 10+ | ❌ Half of target |
| **Workflow Type** | Hybrid | — | — |
| **Tier** | **D** | — | ❌ Low tier |
| **Pattern** | **Volatile/Flat Liner** | — | ❌ No growth |

### May 2026 Detailed Breakdown

| Checkpoint | Date | LoC | Window Delta | Days | Rate (LoC/day) | Cumulative % |
|---|---|---|---|---|---|---|
| **Apr 20** | **April 20** | **491** | **—** | **—** | **—** | **97.4%** |
| Apr 28 | April 28 | 491 | **0** ❌ | 8 days | **0/day** | 97.4% |
| **May 11** | **May 11** | **491** | **0** ❌ | **13 days** | **0/day** | **97.4%** |
| **May 18** | **May 18** | **491** | **0** ❌ | **7 days** | **0/day** | **97.4%** |
| Jun 3 | June 3 | 504 | +13 | 16 days | 1/day | 100% |

**May Timeline Visualization**:
```
Apr 20: 491 LoC (97.4% of Q2 total already complete)
   ↓ 0 — COMPLETELY FLAT ❌
Apr 28: 491 LoC
   ↓ 0 — COMPLETELY FLAT ❌
May 11: 491 LoC
   ↓ 0 — COMPLETELY FLAT ❌
May 18: 491 LoC
   ↓ +13 (1/day) — Minimal
Jun 3: 504 LoC
```

**CRITICAL**: Suraj had **491 LoC by April 20** and only added **13 LoC** in the entire **44-day May-June period**. This is effectively zero activity.

### Why He Appears in Low Usage

1. **504 LoC entire Q2** = genuinely low output (bottom 5% of team)
2. **Completely flat Apr 20 → May 18** (38 days with zero change)
3. **Only 11 interactions all Q2** = extremely low tool engagement
4. **0% acceptance in May** (9.3% overall is still well below benchmark)
5. **No growth pattern** — started with 491 LoC in April, ended with 504 LoC

### ❌ **CANNOT DEFEND — REQUIRES URGENT INTERVENTION**

**"Suraj Dubey is the ONE user of these 5 who genuinely has a performance issue. He had 491 LoC by April 20 and only added 13 LoC across the entire 44-day May-June period. With only 11 interactions all quarter, he is not actively engaging with Copilot or coding work."**

#### Key Concerns — Not Defensible

1. **🔴 Zero Growth for 44 Days** (Apr 20 → May 18):
   - Not "low growth" — **literally zero new LoC** for 38 consecutive days
   - Only +13 LoC in final window (1 LoC/day)

2. **🔴 Extremely Low Engagement**:
   - **11 interactions all Q2** vs. team avg ~150
   - **30 code generations** vs. team avg ~200+
   - Not engaging with Copilot AI at all

3. **🔴 Front-Loaded with No Follow-Through**:
   - **491 LoC by April 20** suggests he started Q2, then stopped
   - **97.4% of Q2 work done in first 3 weeks**, then nothing

4. **🔴 0% Acceptance in May**:
   - Even his low volume has low acceptance (9.3% overall)
   - Not a quality-over-quantity profile

5. **🔴 No Defensible Pattern**:
   - Not Agent-First (would show in SuggEff)
   - Not high-acceptance Inline (9.3% is below benchmark)
   - Not a late accelerator (flat all May)
   - Not blocked then recovered (no recovery)

### Possible Explanations (Must Verify Immediately)

| Scenario | Likelihood | Action |
|---|---|---|
| **Extended PTO/Medical Leave** | Medium | HR records check |
| **Blocked on dependencies** for entire May-June | Low | Check with manager/team |
| **Shifted to non-coding role** (support, firefighting) | Medium | Verify with manager |
| **Working in different codebase** (not Copilot-tracked) | Low | Check git activity across all repos |
| **Different team/project transfer** | Medium | Verify with HR/manager |
| **Performance/Engagement issue** | High | Requires HR + manager involvement |
| **Onboarding/Training period** | Low | Check hire date |

### Recommendations — URGENT

| Priority | Action | Owner | Timeline |
|---|---|---|
| 🔴 **URGENT** | Emergency 1:1 with manager (Susovan Samal): What happened in May-June? | Manager | **TODAY** |
| 🔴 **URGENT** | Verify employment/team status: On team? On PTO? Transferred? Active? | Manager + HR | **TODAY** |
| 🔴 **URGENT** | Check git activity across ALL repos (not just Copilot-tracked) | Manager | **This week** |
| 🔴 **If Active** | Immediate coaching plan + weekly 1:1s + daily check-ins | Manager | Starting immediately |
| 🔴 **If Blocked** | Unblock dependencies immediately, escalate to leadership | Manager | **This week** |
| 🔴 **If Non-Coding Role** | Clarify expectations and transfer out of developer cohort metrics | Manager | **This week** |
| 🎯 **Q3 Recovery Plan** | If returning to coding: Target 500+ LoC/month minimum, 10+ interactions/week | Suraj + Manager | Q3 |
| ⚠️ **HR Involvement** | If no valid explanation, escalate to HR for performance management | Manager + HR | As needed |

### Talking Points for Leadership

> **"Suraj Dubey is the only one of these 5 users with a genuine engagement concern requiring urgent intervention. He had 491 LoC by April 20, then effectively zero activity for the next 44 days (only +13 LoC added by June 3). With only 11 interactions all quarter, he's not actively engaging with Copilot or coding work. We need immediate investigation today: Is this PTO/leave, a role change, a blocker, or a performance issue? This cannot wait until next sprint."**

---

## 📊 Comparison Matrix: The 5 Users

| User | Q2 LoC | Pattern | May Peak Rate | Final Window | Tier | Key Strength | Key Concern | Defensible? | Urgency |
|---|---|---|---|---|---|---|---|---|---|
| **Shubham Gite** | 316 | Mid-Quarter Stall | 15/day | +45 (3/day) | D | ✅✅ **#1 Accept (54.6%)** | Low volume | ✅ **YES** | Low |
| **Amulya Kale** | 2,409 | **Steady Climber** | **103/day** | +553 (35/day) | C | ✅ Consistent, 19.7% accept | Below scale | ✅ **YES** | Low |
| **Abhishek Hole** | 2,803 | Mid-Quarter Stall | **185/day** 🚀 | **0** ❌ | C | ✅✅ **Elite Agent (56 SuggEff)** | Zero final window | 🟡 **PARTIAL** | Medium |
| **Vitthal Devkar** | 2,609 | Volatile | 99/day | +43 (3/day) | B | ✅✅ **#2 Accept Count (78)** | 97% decline from peak | ✅ **YES** | Medium |
| **Suraj Dubey** | 504 | Flat Liner | 1/day | +13 (1/day) | D | ❌ None | Flat all May-June | ❌ **NO** | 🔴 **URGENT** |

---

## 🎯 Summary: Recommended Actions by User

### ✅ Low Urgency (2 users)

**Shubham Gite** & **Amulya Kale**: Celebrate quality, increase volume
- No urgent intervention needed
- Both have strong quality signals (acceptance rates)
- Focus on task allocation and scale support

### ⚠️ Medium Urgency (2 users)

**Abhishek Hole** & **Vitthal Devkar**: Investigate late-quarter stall
- Both showed strong May capability
- Both stalled post-May 18
- Need manager check-in this week to diagnose (PTO? Blocker? Role shift?)
- Not performance issues yet, but pattern requires explanation

### 🔴 High Urgency (1 user)

**Suraj Dubey**: Immediate escalation required
- Zero activity for 44 days (May-June)
- Only 11 interactions all Q2
- Manager + HR involvement needed TODAY
- This is the only non-defensible case

---

## 📋 Recommended Talking Points for Leadership Review

### Opening Statement

> **"We analyzed 5 users flagged for low AI usage. 4 out of 5 are defensible with strong quality metrics or legitimate contextual reasons. 1 user (Suraj Dubey) requires urgent intervention today."**

### User-by-User Summary

1. **Shubham Gite** (Defensible ✅):
   > "Shubham has the #1 acceptance rate on the team at 54.6% — more than double our target. Low LoC volume (316) but exceptionally high code quality. Recommend: Increase task allocation while maintaining quality standard."

2. **Amulya Kale** (Defensible ✅):
   > "Amulya is our most consistent Steady Climber with 19.7% acceptance (0.3% from benchmark threshold). Delivered predictably across all Q2 windows with a May peak of 103 LoC/day. On the right trajectory, just needs scale. No urgent action required."

3. **Abhishek Hole** (Partial — Investigate ⚠️):
   > "Abhishek demonstrated elite Agent-First capability with 2,403 LoC in 13 days (185/day rate) and top-5 Suggestion Efficiency (56). Zero output from May 18-Jun 3 requires investigation this week: PTO, deliverable completion phase, or task allocation gap?"

4. **Vitthal Devkar** (Defensible ✅ — Investigate ⚠️):
   > "Vitthal has #2 Code Acceptance count (78) and 42% acceptance rate — well above benchmark. Demonstrated 99 LoC/day in early May. Late May decline requires investigation but doesn't negate strong Q2 metrics. Check-in this week to understand late-quarter slowdown."

5. **Suraj Dubey** (Not Defensible ❌ — Urgent 🔴):
   > "Suraj had 491 LoC by April 20, then effectively zero activity for 44 days (only +13 LoC by June 3). This is the only user with a genuine engagement concern requiring urgent intervention TODAY. Need immediate manager + HR involvement to diagnose root cause."

### Closing Recommendation

> **"Request approval to: (1) Celebrate Shubham and Vitthal's elite acceptance metrics, (2) Conduct check-ins with Abhishek and Vitthal this week to understand late-quarter patterns, (3) Escalate Suraj's case to HR/Manager today for immediate action."**

---

**End of Analysis**
