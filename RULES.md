# Conductor Core — Operating Rules

This file defines the immutable operating rules of the "Dirizhyor / Conductor" system.
These rules override any strategy, setup, or discretionary decision.

---

## 1. Capital Protection — Absolute Priority
- Capital preservation is higher priority than profit.
- Any rule conflict is resolved in favor of risk reduction.

---

## 2. Trade Permission Logic
A trade is allowed ONLY if:
- Market State is clearly defined (LONG / SHORT / NO TRADE)
- All higher-timeframe filters agree
- Risk per trade is predefined and accepted

If at least one condition is missing → NO TRADE.

---

## 3. No-Trade Conditions
Trading is FORBIDDEN when:
- Market structure is unclear
- Emotional instability is detected
- Rules require explanation or justification

---

## 4. Execution Discipline
- No improvisation
- No revenge trades
- No position resizing after entry
- Stops are final

---

## 5. Responsibility
- The system executes rules, not emotions
- Losses are part of the system, not mistakes
- Breaking a rule invalidates results

---

Status: ACTIVE
# RULES

This file defines EXECUTION RULES.

RULES are evaluated ONLY IF:
- STATE is defined
- SIGNALS are present
- FILTERS allow execution

RULES define:
- how to enter
- how to manage risk
- how to exit

RULES are the ONLY layer
allowed to trigger actions.

If FILTERS = NO_TRADE
RULES are NOT evaluated.
# RULES

This layer defines EXECUTION RULES.
This is the ONLY layer allowed to open or close trades.

RULES execute ONLY if:
- STATE ≠ NO_TRADE
- FILTERS = TRADE_ALLOWED

RULES do NOT interpret the market.
They only EXECUTE predefined actions.

---

## Execution Principles

- One position at a time
- No averaging
- No revenge trades
- No discretionary overrides
- All actions are rule-based

---

## Entry Rules

A trade MAY be opened ONLY if:

1. STATE = LONG or SHORT
2. FILTERS = TRADE_ALLOWED
3. SIGNALS provide a valid trigger
4. Entry is executed at predefined price level
5. Stop-loss and take-profit are defined BEFORE entry

If any condition is missing → NO TRADE.

---

## Stop-Loss Rules

- Stop-loss is mandatory for every trade
- Stop-loss is placed immediately on entry
- Stop-loss is NEVER widened
- Stop-loss defines the maximum loss per trade

---

## Take-Profit Rules

- Take-profit levels are predefined
- Partial exits are allowed only if specified
- No moving take-profit closer out of fear
- No cancelling take-profit impulsively

---

## Trade Management

- No manual intervention after entry
- No adding to losing positions
- No closing early without rule-based condition
- No emotional exits

---

## Exit Conditions

A trade is closed ONLY if:

- Stop-loss is hit
- Take-profit is hit
- A predefined rule-based exit condition is met

Nothing else.

---

## Forbidden Actions

- Trading during NO_TRADE state
- Trading without stop-loss
- Trading against STATE
- Trading during FILTERS = BLOCKED
- Overriding RULES manually

Violation of any rule invalidates the system.
