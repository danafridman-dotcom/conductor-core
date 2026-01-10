# RISK AGGREGATION & EXPOSURE CONTROL

This block defines how multiple risks interact across trades.

Goal: prevent hidden overexposure and risk stacking.

---

## Definitions

- Trade Risk = predefined % risk of a single position
- Total Risk = sum of all active trade risks
- Exposure = capital allocated to open positions

---

## Global Risk Cap

- Max total active risk: **3%**
- If total risk ≥ 2.5% → no new trades allowed
- If total risk ≥ 3% → immediate trading halt

---

## Risk Stacking Rules

- Same direction trades increase aggregate risk
- Correlated assets count as shared risk
- Scaling in increases total risk unless offset

---

## Exposure Control

- Max exposure per direction (long / short): **20%**
- Opposing positions do NOT cancel risk
- Hedging must be predefined, not reactive

---

## Forbidden Patterns

- “Small risks” stacking
- Ignoring correlation
- Adding positions to justify exposure

---

## Enforcement

- Violation = forced flat
- Flat until next session or review
=# RISK_AGGREGATION (Total Risk Control)

Этот слой отвечает за суммарный риск системы.
Он не про одну сделку, а про то, сколько риска уже “висит” в рынке.

Если суммарный риск превышает лимиты — новые входы запрещены.

---

## Зачем нужен слой
- ограничить перегрузку (слишком много открытых рисков)
- не допустить “случайного all-in”
- контролировать коррелированные активы (BTC + DOGE и т.п.)

---

## Определения

### Risk per Trade
Риск на одну сделку = (Entry - Stop) * Size  
В процентах от капитала = Risk / Equity * 100%

### Total Open Risk
Сумма рисков по всем открытым позициям (и ожидающим, если они могут активироваться).

---

## Базовые лимиты

### 1) Максимальный суммарный риск
- TOTAL_OPEN_RISK_MAX = 2% капитала
- если превышено → новые входы запрещены

### 2) Максимум одновременно открытых позиций
- MAX_OPEN_POSITIONS = 2 (в LIVE MICRO)
- MAX_OPEN_POSITIONS = 3 (в LIVE SMALL)
- если превышено → новые входы запрещены

### 3) Корреляция / “Один рынок”
Если активы движутся как один (например BTC и DOGE):
- они считаются одной группой риска
- лимит на группу: GROUP_RISK_MAX = 1.5%

Пример групп:
- GROUP: BTC -> (BTC, DOGE, TON, SOL)
- GROUP: MEME -> (DOGE, SHIB, PEPE)

---

## Правила запрета входа (BLOCK)

### BLOCK if:
1) Total Open Risk > TOTAL_OPEN_RISK_MAX
2) Open Positions count > MAX_OPEN_POSITIONS
3) Any group risk > GROUP_RISK_MAX
4) Account is in Drawdown mode (из RISK)

---

## Приоритеты
1) RISK (правила выживания) — выше всего
2) RISK_AGGREGATION — второй барьер
3) FILTERS — третий барьер
4) DECISION_ENGINE — принимает решение только если барьеры пропустили

---

## Итог
Этот слой не даёт системе “случайно перегрузиться”.
Если в рынке уже достаточно риска — система говорит:
**STOP. Не добавляй.**
