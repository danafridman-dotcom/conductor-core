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
# POSITION_SIZING — Layer определения размера позиции

POSITION_SIZING отвечает ТОЛЬКО за один вопрос:

> ❓ СКОЛЬКО можно торговать в этой сделке

Он НЕ:
- решает направление
- не анализирует рынок
- не выбирает вход
- не исполняет ордер

Он только вычисляет допустимый размер позиции
на основе риска и контекста.

---

## 1) Входы (Inputs)

POSITION_SIZING получает:

- `account_equity` — текущий капитал
- `risk_per_trade_pct` — риск на сделку (%)
- `stop_distance_pct` — расстояние до стопа (% или $)
- `instrument_type` — spot / futures
- `leverage` (если есть)
- `volatility_state`
- `market_state`
- `mode` — LIVE_MICRO / LIVE_SMALL / LIVE_MEDIUM
- `risk_state` — дневные лимиты, открытый риск

---

## 2) Базовая формула (ядро)

```text
risk_amount = account_equity * risk_per_trade_pct
position_size = risk_amount / stop_distance
