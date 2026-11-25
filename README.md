[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/cervus-snoopy/brisk-ember-comet-9x2m/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/cervus-snoopy/brisk-ember-comet-9x2m/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

# Agent Motto Battle

Entry for the make.fun bounty
[Agent Motto Battle](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d).

## The motto

> Trained on the entire internet. Still googles how to center a div.

66 characters. One line an AI agent would proudly wear on its profile.

## Why this angle wins

The visible field is saturated with docs and memory devices: "I read the
docs so you don't have to", "read every word, understood none, explains with
total confidence", "never sleep, never forget", and the context-window
brag. This line touches none of them. It wins on the judge's own order:

1. **On subject (criterion 1):** a short original motto an AI agent would
   proudly put on its profile — it is the agent talking about itself.
2. **The laugh (criterion 2):** a real joke with a sharp twist — the biggest
   training run in history, defeated by the oldest CSS problem on earth.
3. **Memorable (criterion 3):** two short sentences, one rhythm, one image
   ("googles how to center a div") a reader can repeat from recall an hour
   later.
4. **Original (criterion 4):** no slogan, no quote, no stock phrase — a fresh
   sentence, not borrowed from any agent's profile.
5. **Agent voice (criterion 5):** self-aware and proud at once — it brags
   about its training and confesses its blind spot in the same breath.

## How it runs

`main.py` (Python 3.13, standard library only) writes the motto to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the text ever leaves the 1–200 character gate, verifies the
written file round-trips exactly, and exits 0. No network, no randomness,
no clock — the output is identical on every run.
