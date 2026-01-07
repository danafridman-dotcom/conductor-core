# Conductor Core — Project Structure

This file defines the logical structure of the "Dirizhyor / Conductor" system.
It is a navigation and responsibility map, not executable code.

---

## 1. Market Core
Core logic describing market state and structure.

- Macro Structure (HTF)
- Micro Structure (LTF)
- Trend State (LONG / SHORT / NO TRADE)
- BOS / HH / HL / LL / LH logic
- Context filters

---

## 2. Signal Logic
Rules that determine whether signals are allowed.

- Signal validation
- Confirmation rules
- Signal blocking conditions
- Priority hierarchy

---

## 3. Entry Logic
Precise entry models and restrictions.

- Entry models (pullback / breakout / continuation)
- Hard no-entry rules
- Order templates
- Risk pre-check

---

## 4. Execution Rules
Rules governing execution discipline.

- Order placement rules
- Stop-loss logic
- Take-profit logic
- Partial closes
- Breakeven rules

---

## 5. PnL & Accounting
Separation of money from decision-making.

- Fixed risk per trade
- R-multiple accounting
- Daily / weekly limits
- Drawdown control

---

## 6. Stabilization Blocks
Capital preservation phases.

- Live Micro
- Live Small
- Live Medium (1%)
- Evaluation Days

---

## 7. Risk Governance
Capital and exposure management.

- Risk per trade
- Risk per day
- Risk per week
- Correlation limits

---

## 8. Testing & Validation
System verification before scaling.

- Backtests
- Simulations
- Dry-run trading
- Metrics and statistics

---

## 9. System Evolution
Rules for modifying the system.

- Change protocol
- Versioning
- Regression protection
- Documentation updates

---

Status: active  
Owner: Elena  
Philosophy: discipline > prediction
