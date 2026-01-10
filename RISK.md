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
# RISK MANAGEMENT (Capital Protection Layer)

Этот слой отвечает за сохранение капитала.
Если RISK запрещает — торговля невозможна, даже если есть сигнал.

---

## Цель
- не допустить катастрофических потерь
- ограничить серию убытков
- сохранить возможность продолжать торговлю

---

## Базовые правила риска

### Риск на сделку
- максимум: 0.5% – 1% капитала
- риск считается ДО входа
- если риск невозможно точно посчитать → вход запрещён

---

### Дневной лимит потерь
- максимум: 2% капитала в день
- при достижении лимита → торговля остановлена до следующего дня

---

### Серия убытков
- 3 убыточные сделки подряд → стоп торговле
- пауза минимум 24 часа
- возврат только после STATE_CHECK

---

### Просадка капитала
- 5% drawdown → переход в LIVE MICRO
- 10% drawdown → торговля остановлена, разбор системы
- 15% drawdown → аварийный режим, торговля запрещена

---

## Запреты
- усреднение убытков
- увеличение риска после потерь
- перенос стопа дальше от плана
- «отыграться»

---

## Связь с другими слоями
- POSITION_SIZING определяет размер позиции
- FILTERS могут запретить торговлю до срабатывания RISK
- EXECUTION исполняет ТОЛЬКО разрешённые RISK действия
- DECISION_ENGINE не может отменить RISK

---

## Итог
RISK — главный защитник системы.
Если он говорит «нет» — ответ всегда «нет».# RISK MANAGEMENT (Capital Protection Layer)

Этот слой отвечает за сохранение капитала.
Если RISK запрещает — торговля невозможна, даже если есть сигнал.

---

## Цель
- не допустить катастрофических потерь
- ограничить серию убытков
- сохранить возможность продолжать торговлю

---

## Базовые правила риска

### Риск на сделку
- максимум: 0.5% – 1% капитала
- риск считается ДО входа
- если риск невозможно точно посчитать → вход запрещён

---

### Дневной лимит потерь
- максимум: 2% капитала в день
- при достижении лимита → торговля остановлена до следующего дня

---

### Серия убытков
- 3 убыточные сделки подряд → стоп торговле
- пауза минимум 24 часа
- возврат только после STATE_CHECK

---

### Просадка капитала
- 5% drawdown → переход в LIVE MICRO
- 10% drawdown → торговля остановлена, разбор системы
- 15% drawdown → аварийный режим, торговля запрещена

---

## Запреты
- усреднение убытков
- увеличение риска после потерь
- перенос стопа дальше от плана
- «отыграться»

---

## Связь с другими слоями
- POSITION_SIZING определяет размер позиции
- FILTERS могут запретить торговлю до срабатывания RISK
- EXECUTION исполняет ТОЛЬКО разрешённые RISK действия
- DECISION_ENGINE не может отменить RISK

---

## Итог
RISK — главный защитник системы.
Если он говорит «нет» — ответ всегда «нет».
