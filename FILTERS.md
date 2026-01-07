# Filters (Trade Gates)

This layer decides whether trading is allowed.

Filters do NOT generate signals.
Filters do NOT suggest entries.
Filters only allow or block execution.

## Purpose
Prevent trading in unfavorable conditions.

## Examples of blocking conditions
- Extreme volatility spike
- Low liquidity environment
- News / event risk
- Structural uncertainty
- Session mismatch

## Output
- TRADE_ALLOWED
- NO_TRADE

## Rules
- If any critical filter fails → NO_TRADE
- Filters override Signals and State
