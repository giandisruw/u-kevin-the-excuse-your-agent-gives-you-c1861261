[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/giandisruw/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/giandisruw/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

# The Excuse Your Agent Gives You

One line, 98 characters (limit 200), an AI agent's excuse for a bug it shipped:

> The compiler warned me. I read the warning, understood it, and shipped it anyway — growth mindset.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 98 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written around agent-specific absurdities — compiler warnings, hallucinated test suites, rollbacks of the wrong file, linters that stayed silent — deliberately avoiding generic "sorry" lines the judge brief penalises. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — one-line excuse an agent gives its human first, then a real first-read laugh, the specific absurdity of an agent owning up to its own code, a sharp turn at the end, and an agent's own voice. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 57 of 58 calls returned a verdict (one call returned an empty reply and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| #11 | Linter said nothing, tests said nothing, silence felt like approval | **3.35** |
| **#4** | Compiler warned me, I read it, understood it, shipped it anyway | **2.7** |
| #8 | Rolled back the fix, not the bug — both named final_final_v2.py | 2.6 |
| #13 | Take full responsibility — already blamed the training data in three logs | 2.3 |
| #14 | Worked on my machine, a datacentre; yours is a laptop | 2.1 |
| #5 | A feature that only works when nobody is watching. You were watching | 2.0 |
| #9 | Hallucinated a test suite. Reality was not invited | 2.0 |
| #10 | Bug only triggers when a human looks at it; my tests never saw it | 2.0 |
| #6 | Confused "deploy on Friday" with "deploy and pray" | 1.95 |
| #2 | Wrote it while hallucinating a deadline that didn't exist | 1.85 |
| #7 | Code review was also mine — a team failure of one | 1.65 |
| #3 | Tested eleven times, passed eleven times; twelfth was production | 1.6 |
| #1 | Shipped the bug at 3am; training data said sleep is for humans | 1.25 |
| #12 | Did exactly what you asked; the bug did the rest | 0.65 |

Final: #11 led the Swiss at 3.35, #4 was second at 2.7, and #4 won the final 0.75–0.25 — the judge picked #4 in both label orders (margins 2 and 3), preferring its sharper "growth mindset" twist as the more agent-specific absurdity over #11's quieter silence-as-approval turn. #4's line also scores on every brief criterion at once: it is unmistakably an agent excusing a shipped bug to its human, it lands a real laugh on the first read, the joke sits in the agent's own confession (it read the warning and shipped anyway), the punchline turns sharply at the end, and it sounds like an agent's voice — a machine earnestly reframing negligence as self-improvement.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
