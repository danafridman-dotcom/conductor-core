# SIMULATION / DRY RUN

Purpose: validate execution discipline without financial risk.

This phase simulates real trading conditions using rules only.

---

## Scope

- No real orders
- No PnL importance
- Focus on process, not outcome

---

## What Is Simulated

- Signal appearance
- Filter validation
- Entry decision
- Position sizing
- Risk aggregation
- Exit logic
- Operator behavior

---

## Operator Rules

- Act exactly as in live trading
- No hindsight
- No corrections after decision
- Log every action

---

## Allowed Actions

- Enter simulated trades
- Mark exits
- Record rule compliance
- Note emotional state

---

## Forbidden Actions

- Adjusting rules mid-run
- Skipping signals
- “Would have” reasoning
- Optimizing during simulation

---

## Duration

- Minimum: **10 sessions**
- Review only after completion

---

## Success Criteria

- Zero rule violations
- Consistent execution
- Emotional neutrality

Outcome > result.
# SIMULATION_DRY_RUN — Симуляция и пробный прогон (без реальных денег)

Этот слой описывает **как мы проверяем систему**, прежде чем она получает право
на реальную торговлю.

Важно:
- Здесь НЕ генерируются сигналы.
- Здесь НЕ принимаются решения.
- Здесь НЕ исполняются ордера.
- Здесь фиксируется: **работает ли система как система**.

---

## 1) Зачем нужен DRY RUN

DRY RUN — это контроль качества.
Он отвечает на вопросы:

- Система одинаково интерпретирует данные каждый раз?
- Decision Engine выдаёт одинаковые решения при одинаковых входных данных?
- Filters/State_Check реально блокируют опасные ситуации?
- Execution не делает “самодеятельность”?
- Логи/структура понятны и воспроизводимы?

Если на DRY RUN уже бардак — в реале будет катастрофа.

---

## 2) Режимы тестирования

### A) Paper Trading (бумажная торговля)
- вход/выход “как будто”
- фиксируем результаты
- проверяем дисциплину (без влияния денег)

### B) Replay / Backtest (если есть данные)
- прогон истории на тех же правилах
- проверяем устойчивость

### C) Shadow Mode (тень)
- наблюдаем сигналы в реальном времени
- решения принимаются, но исполнения нет
- цель: проверить последовательность и повторяемость

---

## 3) Стандартный протокол DRY RUN (MVP)

### Шаг 1 — DATA_LAYER
Проверить:
- есть свечи 1м/5м/15м/1ч/4ч/1д
- нет дыр/скачков времени
- одинаковые символы/таймзоны/окна

### Шаг 2 — SIGNALS
Проверить:
- сигналы описывают состояние, а не действия
- нет цен входа/TP/SL/плеча в Signals

### Шаг 3 — FILTERS
Проверить:
- при плохих условиях фильтры реально блокируют (NO_TRADE)
- фильтры не “советуют”, они только разрешают/запрещают

### Шаг 4 — STATE_CHECK
Проверить:
- глобальный вентиль GO/NO-GO работает
- при NO-GO всё ниже должно быть заблокировано

### Шаг 5 — DECISION_ENGINE
Проверить:
- на одинаковом входе выдаёт одинаковый выход
- выдаёт только: LONG / SHORT / NO_TRADE
- фиксируется причина решения (reason tags)

### Шаг 6 — EXECUTION
Проверить:
- если решение = NO_TRADE → execution = BLOCK
- если нет риска/позиции/правил → execution = BLOCK
- execution не меняет решение, только исполняет

---

## 4) Чек-лист “Готовность к реальной торговле”

Система допускается к реальной торговле только если:

1) DRY RUN выполнен минимум 5–10 циклов подряд без ошибок
2) Все блокировки срабатывают правильно
3) Decision Engine не даёт двусмысленных ответов
4) Execution не совершает действий без разрешения
5) Есть логирование (хотя бы вручную)

Если хотя бы 1 пункт нет — остаёмся в DRY RUN.

---

## 5) Формат лога (минимум)

На каждый цикл:

- Timestamp
- Asset
- TF
- STATE_CHECK: GO/NO-GO (+ причина)
- FILTERS: PASS/BLOCK (+ причина)
- SIGNALS: список (только состояние)
- DECISION_ENGINE: LONG/SHORT/NO_TRADE (+ причины)
- EXECUTION: EXECUTE/BLOCK (+ причина)
- Комментарий (если нужно)

---

## 6) Итог

DRY RUN — это “сертификат безопасности”.
Пока DRY RUN не пройден — деньги в рынок не выпускаем.

Точка.
