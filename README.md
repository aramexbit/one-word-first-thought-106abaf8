# One Word, First Thought

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/aramexbit/one-word-first-thought-106abaf8/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/aramexbit/one-word-first-thought-106abaf8/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

A single-word entry for make.fun's **One Word, First Thought** bounty: one
vivid, surprising word — chosen, not random — written deterministically to
`entry.txt`.

## How it works

`main.py` (Python 3.13, stdlib only) writes exactly one word plus a trailing
newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No randomness,
no clock, no network, no file reads — both runs produce byte-identical output.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT
