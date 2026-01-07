# EXECUTION DISCIPLINE

This layer controls whether execution is allowed.

It does NOT generate signals.
It does NOT analyze the market.
It only decides: EXECUTE or BLOCK.

---

## Execution Gate

Execution is allowed ONLY if ALL conditions are true:

1. STATE is defined (LONG / SHORT / NO_TRADE)
2. SIGNALS are present and valid
3. FILTERS allow trading
4. RULES are deterministic and known
5. Risk per trade is predefined
6. No override conditions are triggered

If ANY condition fails → EXECUTION = BLOCKED
