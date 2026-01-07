# RISK GOVERNANCE

This block defines how much the system is allowed to lose.
Risk is fixed, predefined, and non-negotiable.

Risk rules have priority over SIGNALS, RULES, and EXECUTION.

---

## Core Principles

- Capital preservation comes first
- Risk is constant, not adaptive to emotions
- Losses are part of the system
- Survival > profit

---

## Risk Per Trade

- Fixed risk per trade: **1% of account equity**
- Risk is calculated BEFORE entry
- Position size is derived from stop-loss distance
- Risk may NOT be increased after losses

---

## Daily Risk Limits

- Maximum daily loss: **2%**
- If daily loss limit is reached → STOP trading for the day
- No exceptions, no “one more trade”

---

## Consecutive Loss Control

- After **2 consecutive losses**:
  - Trading is BLOCKED for the day
- After **3 consecutive losses**:
  - Mandatory review before next session

---

## Drawdown Protection

- If total drawdown reaches **5%**:
  - Reduce risk per trade by 50%
- If total drawdown reaches **8%**:
  - STOP trading
  - System review required

---

## Forbidden Actions

- Increasing risk to recover losses
- Changing risk mid-trade
- Ignoring stop-loss
- “Feeling-based” position sizing
- Trading to get back to breakeven

---

## Enforcement

- If any risk rule is violated → system integrity is broken
- Broken system = NO TRADE until review
