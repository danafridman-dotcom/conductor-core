# RISK AGGREGATION & EXPOSURE CONTROL

This block defines how multiple risks interact across trades.

Goal: prevent hidden overexposure and risk stacking.

---

## Definitions

- Trade Risk = predefined % risk of a single position
- Total Risk = sum of all active trade risks
- Exposure = capital allocated to open positions

---

## Global Risk Cap

- Max total active risk: **3%**
- If total risk ≥ 2.5% → no new trades allowed
- If total risk ≥ 3% → immediate trading halt

---

## Risk Stacking Rules

- Same direction trades increase aggregate risk
- Correlated assets count as shared risk
- Scaling in increases total risk unless offset

---

## Exposure Control

- Max exposure per direction (long / short): **20%**
- Opposing positions do NOT cancel risk
- Hedging must be predefined, not reactive

---

## Forbidden Patterns

- “Small risks” stacking
- Ignoring correlation
- Adding positions to justify exposure

---

## Enforcement

- Violation = forced flat
- Flat until next session or review
