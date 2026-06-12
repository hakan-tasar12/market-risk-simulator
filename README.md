# Market Risk Simulator 📈

An interactive command-line game: you start with some capital and have **5 years to
double it**. Each year the market turns Bull, Bear, or Uncertain, and you choose
**Aggressive** (buy) or **Defensive** (hold cash) — the payoff depends on whether your
call matched the market.

```text
[ YEAR 1 OF 5 ]
CURRENT BALANCE: $10000
MARKET NEWS:  >> Tech Sector Rally. Prices are UP.
CHOOSE STRATEGY:  [1] AGGRESSIVE   [2] DEFENSIVE
>> RESULT: MARKET RALLY. HIGH RETURN. +$5000
```

## Why

I wanted to turn a basic control-flow exercise into something that models a real
intuition: **risk and reward are conditional on the environment.** Aggressive wins big
in a rally and loses hard in a crash; defensive preserves capital when things go bad
but gives up the upside. I built it while learning Python (Angela Yu, 100 Days of Code).

## Run

```bash
python3 market-risk-simulator.py
```

No third-party packages — standard library only (Python 3.8+).

## Scope & limitations

- Market outcomes are uniform random draws, not calibrated to real return distributions.
- Payoffs are fixed percentages, not sampled from historical volatility.
- Integer-dollar rounding; no fees, slippage, or transaction costs.
- A learning project and strategy game — not a real risk model, and not investment advice.

---
*Created by Hakan Taşar*
