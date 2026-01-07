# State

This file defines the CURRENT MARKET STATE.

State is a classification layer.
It answers the question:
"What phase is the market in right now?"

State is NOT a signal.
State is NOT an instruction.
State is NOT a bias.

---

## Allowed States

- TREND_UP
- TREND_DOWN
- RANGE
- BREAKOUT
- DISTRIBUTION
- ACCUMULATION
- HIGH_VOLATILITY
- LOW_VOLATILITY
- TRANSITION
- NO_TRADE

---

## Rules

- Only ONE state may be active at a time
- State is determined from higher timeframe context
- State must be stable, not reactive
- State may persist across many signals

---

## Forbidden in State

- Entry or exit logic
- Buy / Sell language
- Risk management
- Emotional interpretation

---

## Output Format

State must be expressed as:

> Market state: X

Example:
> Market state: RANGE
