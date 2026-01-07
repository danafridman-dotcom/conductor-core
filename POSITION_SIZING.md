# POSITION SIZING

This block defines how position size is calculated.
Position size is derived ONLY from risk and stop-loss distance.

No discretion is allowed.

---

## Inputs

- Account Equity (E)
- Fixed Risk per Trade (R)
- Stop-Loss Distance (SL)

---

## Fixed Parameters

- Risk per trade (R): **1% of equity**
- Risk value = E × R

---

## Position Size Formula

Position Size = Risk Value / Stop-Loss Distance

Example:
- Equity = 10,000
- Risk per trade = 1% → 100
- Stop-Loss = 50 points
- Position Size = 100 / 50 = 2 units

---

## Rules

- Position size is calculated BEFORE entry
- Stop-loss must be defined BEFORE size calculation
- If stop-loss is undefined → NO TRADE
- If position size exceeds exchange limits → NO TRADE
- Position size is NOT rounded up aggressively

---

## Forbidden Actions

- Increasing size to recover losses
- Using intuition instead of calculation
- Changing size mid-trade
- “Feeling-based” sizing

---

## Enforcement

- If sizing rules are violated → trade is invalid
- Invalid trade = system breach
