# Ledger

A PM copilot that carries a product idea through five stages — **Concept → Validate → Prototype → GTM → Pitch** — while logging every substantive claim it makes to a visible, running **Evidence Ledger**. The core idea: it never lets a number pass as settled without flagging what backs it.

## What it does

Ledger acts as a thinking partner for early-stage product work. As you talk through an idea, it:

- Advances through the five stages based on how the conversation is progressing
- Logs claims it makes to an Evidence Ledger panel — each one tagged as `factual`, `unverified`, `speculative`, or `disputed`, with a confidence score, a risk-of-error score, and a source note
- Lets you toggle between two rigor modes mid-conversation:
  - **Exploratory** — flagged, pattern-based estimates are allowed, to keep ideation moving
  - **Board-Ready** — the model withholds any number it can't source, and names the specific real source or calculation needed instead
- Saves the full session (conversation, ledger, stage, mode) automatically, so you can pick up where you left off

## Why it's built this way

Most AI brainstorming tools blur the line between "the model's best guess" and "a verified fact." Ledger forces that distinction into the open — every claim gets a type, a confidence level, and a source tag, so you always know what you're actually standing on before you take an idea to a stakeholder.

## Current form

A single self-contained HTML file — no build step, no backend, calling the Anthropic API directly. This is a working prototype, not a production build. Known limitations (by design, at this stage):

- The "specialist agents" referenced conceptually (Research, Design, Data, Strategy, Pitch) are voiced by one model, not independently running agents
- No live web search or grounding — "unverified" and "speculative" labels are honest, but nothing upgrades a claim to "factual" via live lookup
- Confidence/risk scores are the model's self-reported estimates, not yet validated against real outcomes

## Sample output

See `outputs/` for an example session log and Evidence Ledger export from a validation run against a co-op health plan concept.

## Where this feeds

Ledger's artifacts (markdown/text summaries of validated concepts) are the intake source for the [Product Owner Agent](../product-owner-agent/README.md), which turns them into a structured backlog.
