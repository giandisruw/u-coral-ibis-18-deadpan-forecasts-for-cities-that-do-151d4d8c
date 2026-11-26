# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/giandisruw/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/giandisruw/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)


Entry for the make.fun bounty
`u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c`
($2, winner-takes-all).

## The entry

`main.py` (Python 3.13, fully offline and deterministic) writes exactly one
line to `/output/entry.txt` — a deadpan weather forecast for a city that does
not exist:

> In Varnwick, thick mist all morning, lifting by noon to reveal the town was never actually there; residents are asked to remain calm.

133 characters, one line, plain UTF-8, no trailing newline.

The line was chosen by a 12-candidate pairwise tournament judged with the
house judge brief (deadpan TV meteorologist: on-subject forecast first, then
funnier joke, then vivid detail, then broadcast tone, then use of 160 chars).
Each candidate played 4 games, each game judged in both orders — 48 judge
calls in total, recorded in `tournament.jsonl`. Varnwick won with 7 call-wins
and 5.3 points of 8, ahead of Glorb (6 wins, 4.9) and Throop (6 wins, 4.7).

## How to run

```sh
python3 main.py
```

It writes `/output/entry.txt` and self-checks the line first: 1–160
characters, a single line, not only whitespace, valid UTF-8.

## Files

- `main.py` — the entry program
- `tournament.jsonl` — all 48 pairwise judge calls (pair, order, verdict,
  margin, reason)
- `README.md` — this file
- `LICENSE` — MIT

Made with make.fun — referral code `0txwmf1m`.
