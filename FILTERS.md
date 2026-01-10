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
# FILTERS

This file defines EXECUTION PERMISSION.

FILTERS decide whether trading is allowed
based on current market conditions.

FILTERS do NOT define entries.
FILTERS do NOT define exits.

They only return:
- TRADE_ALLOWED
- NO_TRADE

Examples of blocking conditions:
- Extreme volatility
- Low liquidity
- News / event risk
- Structural uncertainty
- Session mismatch

FILTERS operate AFTER SIGNALS
and BEFORE RULES.
# FILTERS — Trade Permission Layer (разрешение на торговлю)

FILTERS — это слой «можно / нельзя торговать сейчас».
Он НЕ создаёт сигнал и НЕ выбирает направление.
Он только проверяет условия допуска и возвращает:

- ✅ ALLOW_TRADE
- ❌ BLOCK_TRADE + причина

Связи:
DATA_LAYER → DECISION_ENGINE (формирует intent: LONG/SHORT/NO_TRADE)
DECISION_ENGINE → FILTERS (проверка допуска)
FILTERS → EXECUTION (если ALLOW, тогда можно исполнять)

---

## 1) Что FILTERS НЕ делает
- не анализирует «куда пойдёт цена»
- не генерирует сигнал
- не управляет ордерами
- не изменяет риск-параметры

---

## 2) Входы (Inputs)
FILTERS получает на вход структурированный пакет:

- `intent`: LONG / SHORT / NO_TRADE
- `symbol`: например DOGE/USDT
- `tf_context`: 15m / 1h / 4h / 1d (статусы)
- `market_state`: режим рынка (trend / range / chaos)
- `volatility_state`: low / normal / high
- `liquidity_state`: ok / thin
- `risk_state`: risk_per_trade, max_loss_day, open_risk, cooldown
- `session_state`: timezone, торговое окно, запреты по времени
- `data_quality`: ok / degraded / stale
- `exchange_state`: ok / limited / error
- `news_state` (опционально): calm / risk_event

---

## 3) Выходы (Outputs)
- `ALLOW_TRADE`
- `BLOCK_TRADE` + `reason_code` + `human_message`

Пример reason_code:
- `DATA_STALE`
- `VOLATILITY_TOO_HIGH`
- `COOLDOWN_ACTIVE`
- `DAILY_LIMIT_HIT`
- `SPREAD_TOO_WIDE`
- `EXCHANGE_DEGRADED`
- `NO_CLEAR_STATE`
- `SIGNAL_NOT_CONFIRMED` (если подтверждения не выполнены)
- `CONFLICTING_TFS`

---

## 4) Приоритет правил (Hard → Soft)

### A) HARD BLOCKERS (жёсткий запрет)
Если срабатывает любой пункт — торговать нельзя.

1. **Intent = NO_TRADE**
2. **Data Quality не ok**
   - stale / gaps / задержка
3. **Exchange State не ok**
   - ошибки, ограничения, нет доступа к ордерам
4. **Risk Governance**
   - дневной лимит потерь достигнут
   - риск на сделку не определён
   - превышен общий открытый риск
5. **Cooldown / Anti-tilt активен**
6. **Спред/ликвидность**
   - спред слишком широкий
   - тонкий стакан (thin liquidity)
7. **Volatility = HIGH (если нет отдельного режима работы с высокой волатильностью)**
8. **Нарушено торговое окно / запрет по времени**
9. **Конфликт таймфреймов (если правило включено)**
   - например: 15m LONG, а 1h/4h жёстко медвежьи

---

### B) SOFT FILTERS (мягкий запрет / понижение допуска)
Эти правила могут:
- либо блокировать (если включено как строгое),
- либо переводить в режим “WAIT / NEED_CONFIRMATION”.

- слабое подтверждение (RSI/EMA/SAR не в порядке)
- объёмы не подтверждают
- рынок в «range/chaos», а стратегия сейчас только для тренда
- слишком поздно/слишком рано по сессии (если наблюдается шум)

---

## 5) Минимальный чек-лист допуска (MVP)
Для включения ALLOW_TRADE должны быть TRUE:

1) `intent != NO_TRADE`
2) `data_quality == ok`
3) `exchange_state == ok`
4) `risk_per_trade` задан и <= лимита
5) `daily_loss_limit` не нарушен
6) `cooldown == false`
7) `liquidity_state == ok`
8) `volatility_state != high` (в MVP)
9) подтверждения сигнала «выполнены» (см. ниже)

---

## 6) Подтверждения сигнала (Confirmation Gate)
FILTERS не создаёт сигнал, но проверяет, что подтверждения выполнены.
(настройка под вашу систему)

### LONG confirmation (пример)
- RSI(15m) > 45
- цена удерживает / возвращает EMA20 (15m или 1h — по выбранному правилу)
- SAR перевёрнут под цену (или другой маркер смены импульса)
- объёмы не падают на росте (нет явной слабости)

### SHORT confirmation (пример)
- RSI(15m) < 55 и падает
- цена ниже EMA20 и ретест снизу подтверждён
- SAR над ценой
- объёмы подтверждают продавца

Если confirmation не выполнен → `BLOCK_TRADE: SIGNAL_NOT_CONFIRMED`

---

## 7) Режимы (Modes)
FILTERS зависит от режима стратегии:

- **LIVE_MICRO**: самые жёсткие фильтры, меньше сделок
- **LIVE_SMALL / MEDIUM**: фильтры сохраняются, допускается больше инструментов/окон
- **SIM / DRY_RUN**: можно ослаблять риск-блокеры, но фиксировать причины

---

## 8) Логирование (обязательно)
Каждый вызов FILTERS логируется:

- timestamp
- symbol
- intent
- result: ALLOW/BLOCK
- reason_code
- ключевые состояния (volatility/liquidity/risk/data)

Цель: потом видеть статистику «почему система НЕ торговала» и «где мы теряем сделки».

---

## 9) Итог
FILTERS — это «охранник входа».
Даже идеальный сигнал не проходит, если:
- данные плохие,
- риск-режим нарушен,
- рынок в опасном состоянии,
- дисциплина/лимиты активны.

Decision = в DECISION_ENGINE  
Execution = в EXECUTION  
Permission = здесь, в FILTERS
