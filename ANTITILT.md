# ANTI-TILT — Execution Discipline Guard

This block exists to protect the account from the trader (emotion, revenge, FOMO).
It does NOT analyze the market.
It only decides: ALLOW or BLOCK execution based on discipline rules.

---

## Output (one value)

- ALLOW
- BLOCK

---

## Hard Rules (no exceptions)

If ANY rule below is violated → output = BLOCK.

1) **No revenge trading**
   - After a loss, you must NOT open a new trade immediately.
   - Minimum cooldown: **30 minutes** (or **10 candles** on your working timeframe).
   - If you feel urgency / anger → BLOCK.

2) **Max losses per day**
   - If you hit **2 losses in a day** → STOP for the day.
   - Output = BLOCK until next day.

3) **Max trades per day**
   - Maximum **3 trades per day**.
   - After 3 trades → BLOCK.

4) **No trading while emotionally unstable**
   - If you feel: anger, fear, urgency, “I must win back”, shaking, obsession → BLOCK.
   - If you cannot calmly explain the setup in one sentence → BLOCK.

5) **No entries after impulse**
   - If price moved fast (impulse candle / spike) and you missed the move → NO chase.
   - Wait for structure + confirmation. Otherwise → BLOCK.

6) **No entry without full checklist**
   - If the required checklist is not 100% satisfied → BLOCK.
   - “Almost” counts as NO.

7) **No doubling risk**
   - You may NOT increase risk after a loss.
   - Risk per trade must stay constant by the Capital & Risk Governance block.

8) **No trading outside allowed session**
   - If session rules say NO TRADE (sleepy, distracted, rushed, tired) → BLOCK.
   - If you cannot focus for the next 30–60 minutes → BLOCK.

---

## Soft Rules (recommendations that can become hard later)

These do not automatically BLOCK, but require extra caution:

- If you already took **one loss today** → reduce activity, be selective.
- If volatility is extreme → prefer NO TRADE unless system explicitly allows.

---

## Self-Check (fast questions)

Answer YES/NO. If any is NO → BLOCK.

1) I am calm and not trying to win back money.
2) I can explain the setup in one sentence.
3) I accept the stop-loss emotionally.
4) I am not chasing an impulse.
5) I have time to manage the trade properly.

---

## Notes

- This block has priority over entry logic.
- Market can be perfect — you still do NOT trade if you are not.
