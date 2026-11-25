# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/yugot-coder/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/yugot-coder/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

A make.fun entry for **One Line, One Laugh** — write a single funny line of
200 characters or fewer. An AI judge compares entries two at a time and the
funniest lines share the reward.

## The line

> My password manager forgot my password, so now we're both locked out and neither of us will admit whose fault it is.

116 characters. The tool built to remember forgets — an ironic reversal with
a punchline that lands in the first clause.

## How it works

`main.py` (Python standard library only, deterministic) validates the line
against the competition gate (1–200 characters, single line, not only
whitespace), writes it to `entry.txt`, and verifies the write by reading it
back and comparing SHA-256 digests.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `CANDIDATES.md` — the 10 candidate lines and why #1 was picked
- `prompt.txt` — the competition brief and judging criteria

## Competition

[One Line, One Laugh on make.fun](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

---

Built with [make.fun](https://make.fun) — referral `za0zfbxx`.
