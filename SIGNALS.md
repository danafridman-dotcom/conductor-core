# Signals

## Definition
Signals describe the **state of the market**, not actions.
They answer the question: **WHAT is happening**, never **WHAT to do**.

## Nature of Signals
- Signals are descriptive, not prescriptive
- Signals are objective and observable
- Signals are timeframe-specific
- Signals do not contain entries, exits, or position size

## Examples of Valid Signals
- Trend direction (HH / HL, LH / LL)
- Break of Structure (BOS)
- Range expansion or compression
- Volatility increase / decrease
- Liquidity sweep occurred
- Momentum acceleration / decay

## Forbidden in Signals
- Buy / Sell instructions
- Entry prices
- Stop-loss or take-profit
- Risk or position sizing
- Emotional or interpretive language

## Signal Output Rule
A signal may only state:
> “The market is showing X”

Never:
> “We should do X”
# SIGNALS

This file defines MARKET OBSERVATIONS.

SIGNALS describe what the market is doing,
without deciding whether to trade or not.

SIGNALS do NOT execute trades.
SIGNALS do NOT allow or block execution.

They only report observable conditions.

Examples:
- Break of structure (BOS)
- Higher High / Lower Low
- Volume expansion
- Momentum shift
- Volatility spike
- Range compression

SIGNALS are inputs for FILTERS and RULES.
---

## Signal Taxonomy

All signals are classified into clear categories.
Each signal answers **WHAT is happening**, never **WHAT to do**.

### 1. Market Structure Signals
- Higher High (HH)
- Higher Low (HL)
- Lower High (LH)
- Lower Low (LL)
- Break of Structure (BOS)
- Change of Character (CHoCH)

### 2. Volatility Signals
- Volatility Expansion
- Volatility Compression
- Range Breakout
- Range Contraction

### 3. Liquidity Signals
- Liquidity Sweep (high / low)
- Equal Highs / Equal Lows taken
- Stop-run event
- Inefficient price movement (impulse imbalance)

### 4. Momentum Signals
- Momentum Acceleration
- Momentum Decay
- Impulse Exhaustion
- Failed Follow-through

### 5. Timeframe Context Signals
- HTF bias alignment
- HTF vs LTF conflict
- Session Open / Close influence
- Killzone presence (if applicable)

---

## Signal Validity Rules

A signal is considered **valid** only if:
- It is observable on the chart
- It is timeframe-defined
- It does NOT include execution logic
- It does NOT imply direction by itself
- It can be independently verified

Signals are **inputs**, not decisions.

---

## Signal → System Flow

Signals are consumed by:
- FILTERS → to allow or block trading
- DECISION_ENGINE → to evaluate scenarios
- STATE_CHECK → to confirm system readiness

Signals **never**:
- Trigger orders
- Define entries
- Define exits
- Define position size
- Override risk rules

---

## Core Principle

> Signals describe reality.  
> Decisions interpret signals.  
> Execution obeys decisions.

Any signal that violates this separation is **invalid by design**.---

## Signal Taxonomy

All signals are classified into clear categories.
Each signal answers **WHAT is happening**, never **WHAT to do**.

### 1. Market Structure Signals
- Higher High (HH)
- Higher Low (HL)
- Lower High (LH)
- Lower Low (LL)
- Break of Structure (BOS)
- Change of Character (CHoCH)

### 2. Volatility Signals
- Volatility Expansion
- Volatility Compression
- Range Breakout
- Range Contraction

### 3. Liquidity Signals
- Liquidity Sweep (high / low)
- Equal Highs / Equal Lows taken
- Stop-run event
- Inefficient price movement (impulse imbalance)

### 4. Momentum Signals
- Momentum Acceleration
- Momentum Decay
- Impulse Exhaustion
- Failed Follow-through

### 5. Timeframe Context Signals
- HTF bias alignment
- HTF vs LTF conflict
- Session Open / Close influence
- Killzone presence (if applicable)

---

## Signal Validity Rules

A signal is considered **valid** only if:
- It is observable on the chart
- It is timeframe-defined
- It does NOT include execution logic
- It does NOT imply direction by itself
- It can be independently verified

Signals are **inputs**, not decisions.

---

## Signal → System Flow

Signals are consumed by:
- FILTERS → to allow or block trading
- DECISION_ENGINE → to evaluate scenarios
- STATE_CHECK → to confirm system readiness

Signals **never**:
- Trigger orders
- Define entries
- Define exits
- Define position size
- Override risk rules

---

## Core Principle

> Signals describe reality.  
> Decisions interpret signals.  
> Execution obeys decisions.

Any signal that violates this separation is **invalid by design**.
