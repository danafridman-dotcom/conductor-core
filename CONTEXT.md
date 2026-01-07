# Context

This file defines MARKET CONTEXT.

Context describes the environment in which the market operates.
It provides background conditions that influence interpretation,
but do NOT generate signals or actions.

Context answers:
"What kind of market environment are we in?"

---

## Context Dimensions

- Session (Asia / London / New York / Overlap)
- Macro regime (risk-on / risk-off / neutral)
- Volatility regime (compressed / expanding)
- Liquidity conditions (thin / normal / high)
- News pressure (none / scheduled / active)
- Correlation environment (BTC-led / market-wide / fragmented)

---

## Rules

- Context may contain multiple active descriptors
- Context changes slower than signals
- Context must never contradict State
- Context refines interpretation, not execution

---

## Forbidden in Context

- Buy / Sell language
- Entry or exit logic
- Price targets
- Risk sizing
- Emotional bias

---

## Output Format

Context must be expressed as a list:

> Context:
> - Session: X
> - Volatility: Y
> - Liquidity: Z

Example:
> Context:
> - Session: New York
> - Volatility: Expanding
> - Liquidity: High
