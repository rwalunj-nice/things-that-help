# Pearson r (Pearson Correlation Coefficient)

Measures **how linearly related two things are** — in our context, how consistently a team's AI adoption moves in one direction over time.

Range is always **−1 to +1**:
- **+1** = perfect straight line upward
- **0** = no pattern at all
- **−1** = perfect straight line downward

---

## Formula

```
r = Σ(x−x̄)(y−ȳ)
    ─────────────────────────
    √[Σ(x−x̄)²] × √[Σ(y−ȳ)²]
```

- **Numerator**: captures whether x and y move together — if both go up at the same time, you get a big positive number
- **Denominator**: normalises so the result always lands between −1 and +1 regardless of scale

---

## Worked Example — WFM Integrations (S189=74%, S190=77%, S191=78%)

We correlate **sprint number** (x) against **AI adoption %** (y).

### Step 1 — List the pairs

| Sprint | x (sprint index) | y (AI%) |
|---|---|---|
| S189 | 1 | 74 |
| S190 | 2 | 77 |
| S191 | 3 | 78 |

### Step 2 — Find the means

- x̄ = (1 + 2 + 3) / 3 = **2**
- ȳ = (74 + 77 + 78) / 3 = **76.33**

### Step 3 — Compute deviations and multiply

For each row, calculate how far each value is from its mean, then multiply the two deviations together.

| Sprint | x−x̄ | y−ȳ | (x−x̄)(y−ȳ) | (x−x̄)² | (y−ȳ)² |
|---|---|---|---|---|---|
| S189 | −1 | −2.33 | +2.33 | 1 | 5.43 |
| S190 | 0 | +0.67 | 0 | 0 | 0.45 |
| S191 | +1 | +1.67 | +1.67 | 1 | 2.79 |
| **Sum** | | | **+4.00** | **2** | **8.67** |

**Why multiply the deviations?**
- S189: both x and y were *below* average at the same time → product is positive (+2.33)
- S190: sprint index is exactly at the mean → contributes nothing (0)
- S191: both x and y were *above* average at the same time → product is positive (+1.67)

The sum is **positive** because whenever sprint number was high, AI% was also high — they moved together consistently.

### Step 4 — Apply the formula

```
r = 4.00 / (√2 × √8.67)
r = 4.00 / (1.414 × 2.944)
r = 4.00 / 4.163
r ≈ +0.96  ✓
```

---

## Why CIA Gets r = +0.06

CIA's sprints: S189=64%, S190=80%, S191=65%

It shot up then came straight back down. The up-move and the down-move cancel each other out in the numerator — the result is near zero because there is no consistent direction. That is why r=+0.06 reads as "no trend" even though the numbers look active.

---

## Quick Reference — r Values in AI Adoption Reports

| r value | Product | Interpretation |
|---|---|---|
| +0.96 | WFM Integrations | Near-perfect linear climb |
| +0.92 | Playvox | Very consistent rise |
| +0.91 | ESP | Strong and stable |
| +0.82 | EEM | Rising, stabilising |
| +0.40 | CXone WFM | Gentle rise |
| +0.38 | Shivneri (team) | Volatile, weak trend |
| +0.30 | Torna (team) | Peaked, slight pullback |
| +0.06 | CIA | Spike then reset, no net trend |
| −0.12 | Integrations (team) | Flat/volatile |
| −0.46 | Rajgad (team) | Declining trend |
| −0.50 | IEX WFM | Peaked then correcting |
| N/A | PM | Only 2 closed sprints — insufficient |
