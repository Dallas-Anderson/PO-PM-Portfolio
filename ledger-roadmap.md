# Ledger — Mockup → Production Agent Roadmap

*Captured for later exploration. Ordered roughly by priority, not necessarily build sequence.*

---

## 1. Reliability infrastructure

- ~~**Structured outputs via tool use**, not prompt-based JSON.~~ **Done in v0.3** — see `ledger-v0.3-changes.md`. One caveat carried forward from that doc: `tool_choice` couldn't be forced without breaking web search coexisting in the same turn, so this is a large reliability improvement, not an airtight guarantee — a narrow text fallback path still exists.
- **Server-side error handling and retry logic**, not client-side JavaScript reacting after the fact.
- **A real backend** — session state, ledger history, and audit trail need a real database, not client-side `window.storage`.

## 2. Resolve the "specialist agents" question

Currently one voice (Ledger) claims five roles (Research, Design, Data, Strategy, Pitch) rather than running them separately. Two legitimate paths — pick one deliberately, don't default:

- **Real sub-agent orchestration** — Ledger dispatches to separately-prompted/modeled specialist agents and synthesizes. More cost and latency, genuinely different reasoning per role.
- **Stay single-agent, drop the "suite" framing** — if a single voice reasons just as well in testing, describe it accurately instead of assuming multi-agent is automatically better.

## 3. Ground the claims for real

The core differentiator only holds up if this is true:

- ~~Wire in the **web search tool** so "unverified" claims can become genuinely sourced ones with real citations, not just flagged guesses.~~ **Done in v0.2** — see `ledger-v0.2-changes.md`. Real tradeoff documented there: increases truncation risk and adds latency/cost per turn.
- **Calibration testing** — do claims marked "80% confidence" turn out right ~80% of the time? Untested. Without this, confidence scores are a UX feature, not an epistemic one.

## 4. Table-stakes production requirements

- Auth and multi-user support.
- Persistence and audit trail as a hard requirement, not best-effort — if used for real decisions, "what did the agent claim and why" needs to be permanently queryable.
- Cost modeling — full conversation history is resent every turn; needs modeling before committing to that architecture at real usage volume.

**Both items originally flagged as the top priority are now done (v0.2, v0.3).** Next most valuable single step: calibration testing on confidence scores (§3) — everything else in this doc is infrastructure; that item is the one that tests whether the core premise of the product actually holds up.
