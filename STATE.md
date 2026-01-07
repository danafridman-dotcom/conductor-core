# STATE

This layer outputs the CURRENT MARKET STATE.

It is a classification layer only.
It does NOT open trades.
It answers: "What phase is the market in right now?"

## Output (one value)

- LONG
- SHORT
- NO_TRADE

## Definitions

### LONG
Market structure is bullish.
Minimum requirements (all must be true):
1) Higher High (HH) and Higher Low (HL) pattern on the control timeframe.
2) Latest Break of Structure (BOS) was UP.
3) Price holds above the structure pivot (the last HL area).
4) No active hard-block from FILTERS.

### SHORT
Market structure is bearish.
Minimum requirements (all must be true):
1) Lower Low (LL) and Lower High (LH) pattern on the control timeframe.
2) Latest Break of Structure (BOS) was DOWN.
3) Price holds below the structure pivot (the last LH area).
4) No active hard-block from FILTERS.

### NO_TRADE
Anything that is not a clean LONG or clean SHORT.
Examples:
- Structure is mixed or transitional (range, chop).
- BOS happened but hold failed (fakeout / reclaim).
- Price is inside the pivot zone (indecision).
- FILTERS blocks execution (even if structure looks good).

## Notes
- STATE is determined on CLOSED candles only.
- If uncertain -> NO_TRADE (default safe state).
