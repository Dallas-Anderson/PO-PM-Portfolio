# Ledger — Spec Document (Current Iteration)

*Describes what's actually built, as of this iteration. For where this goes next, see `ledger-roadmap.md`. For the concept it's been validated against, see `coop-health-plan-concept-brief.md`.*

---

## 1. Purpose

Ledger is a single-agent PM copilot that carries a product idea through five stages — Concept, Validate, Prototype, GTM, Pitch — while logging every substantive claim it makes to a visible, running **Evidence Ledger** (type, confidence score, risk-of-error score, source). The core differentiator: it never lets a number pass as settled without flagging what backs it.

**Current form factor:** a single self-contained `.html` file. No build step, no backend, no dependencies beyond a browser and network access to the Anthropic API.

---

## 2. Architecture

| Layer | Implementation |
|---|---|
| UI | Vanilla HTML/CSS/JS, single file |
| Model calls | Direct `fetch` to `https://api.anthropic.com/v1/messages`, model `claude-sonnet-4-6` |
| Output format | Model instructed via system prompt to return minified JSON matching a fixed schema (see §4) — not enforced via tool-use/structured output at the API level |
| Persistence | Browser-side `window.storage` (personal-scoped, not shared), keyed to this artifact instance |
| State | Held in JS variables (`history`, `ledgerEntries`, `sessionLog`, `currentStage`, `currentMode`) — no server, no database |

**Known architectural limitation:** because output format is prompt-enforced rather than API-enforced, malformed responses are possible (see §6). This is the single biggest gap between this iteration and a production build — flagged in the roadmap as the top-priority fix.

---

## 3. Feature Inventory

**Chat interface** — free-text input, agent replies rendered as chat bubbles. One lead agent ("Ledger") voices all reasoning; no separately-running specialist agents (see §7).

**Stage rail** — five-stage horizontal progress indicator (Concept → Validate → Prototype → GTM → Pitch). Advances based on the model's own read of conversation progress each turn; moves forward only, never regresses or skips.

**Evidence Ledger panel** — right-hand column. Every claim the model logs renders as a card: claim text, a type badge (`factual` / `unverified` / `speculative` / `disputed`), a confidence percentage, a risk-of-error percentage, and a short source tag. Cards also carry a mode tag (see below) showing which rigor setting was active when logged.

**Rigor mode toggle** — two states, switchable mid-conversation without losing history:
- **Exploratory** (default): model may offer flagged, pattern-based estimates to keep ideation moving.
- **Board-Ready**: model is instructed to withhold any number it can't source, and to name the specific real source/calculation needed instead. Ledger entries above 60% confidence require the number to have come from the user, not the model.

A dashed divider is inserted into the chat transcript whenever the mode changes, so the switch is visible in the record.

**Session persistence** — the full conversation (messages, mode switches, system notes), the Evidence Ledger, current stage, and current mode are saved after every turn and restored automatically on reload. A two-click "Reset session" control clears saved state and starts fresh.

**Starter prompts** — three example idea chips shown before the first message, to demonstrate the flow without requiring the user to compose an opening prompt.

---

## 4. Response Data Contract

Every model turn is instructed to return exactly this JSON shape (no markdown fences, no prose outside the object):

```json
{
  "stage": "concept | validate | prototype | gtm | pitch",
  "reply": "2-4 short sentences, conversational",
  "ledger_entries": [
    {
      "claim": "under 15 words",
      "type": "factual | unverified | speculative | disputed",
      "confidence": 0,
      "risk": 0,
      "source": "under 8 words"
    }
  ],
  "assumptions": ["short phrase", "..."]
}
```

Constraints enforced via the system prompt (not the API): 0–2 `ledger_entries` per turn, reply capped at 2–4 sentences, claim/source length caps — all sized to reliably fit inside the fixed 1000-token output budget for this feature.

---

## 5. System Prompt Design

Two layers, concatenated per request:

- **Base prompt** — defines Ledger's role (orchestrator of a conceptual specialist-agent suite), voice (grounded, status-quo-challenging, concise), the JSON contract, and a hard honesty rule: never fabricate a specific statistic, citation, or source as if verified, since this demo has no live web access.
- **Mode-specific rules** — appended based on the active toggle state, described in §3.

---

## 6. Error Handling & Resilience

Three distinct failure modes were identified and handled through iterative real-world testing:

| Failure | Symptom | Handling |
|---|---|---|
| API-level error (auth, rate limit, overload) | Response body contains an `error` field instead of `content` | Detected explicitly; real error message surfaced to the user instead of a downstream crash |
| Prose contamination | Model responds in plain text instead of JSON (no `{`/`}` found, or found but unparseable) | Code first attempts to extract a `{...}` substring and parse it; if that fails too, it degrades gracefully — shows the model's actual text as the reply, logs nothing to the Evidence Ledger that turn, and posts a visible system note explaining why |
| Truncation | Response cut off mid-generation (hit the 1000-token output cap before finishing) | Detected via parse-error signature (`unterminated string`, `unexpected end of input`); user sees a plain explanation that the reply ran long, not a raw parse error |

A prior, since-fixed defect is also worth noting for the record: an early version of the Evidence Ledger's empty-state placeholder was destroyed on first render and never recreated, causing a null-reference crash on the second update. Fixed by generating the empty-state message in JS on every render rather than depending on a static DOM node.

---

## 7. Known Limitations (as of this iteration)

- **No real specialist agents.** Research/Design/Data/Strategy/Pitch are named conceptual roles one model voices, not independently running agents. (Architecture diagram elsewhere in this portfolio represents the *conceptual* framework, not the current implementation — noted explicitly there.)
- **No real grounding.** No web search or external data tool is wired in. "Unverified"/"speculative" claims are genuinely unverified — the labeling is honest, but nothing upgrades a claim to "factual" via live lookup.
- **Confidence/risk scores are unvalidated.** They're the model's self-reported estimates, not calibrated against outcomes. No testing has been done on whether "80% confidence" claims are right ~80% of the time.
- **No file upload.** Documents (like the concept brief) must be pasted as text; there's no drag-and-drop or attachment handling.
- **No multi-user support.** Session storage is personal and scoped to this artifact instance — there's no auth, and no concept of shared or team state.
- **Structured output isn't API-enforced.** JSON compliance depends on prompt instructions the model can occasionally deviate from — mitigated (see §6) but not eliminated.
- **Fixed output budget.** `max_tokens` is fixed at 1000 for this environment and can't be raised, which caps how much a single turn can say before running the truncation-recovery path.

---

## 8. Visual/Brand Identity

- **Palette:** near-black ink background (`#14181C`), amber accent for unverified/exploratory (`#D9A441`), teal accent for factual/board-ready (`#4FA98C`), muted rust for challenge/friction (`#C15B4A`).
- **Typography:** IBM Plex Mono for labels, data, and the ledger UI; IBM Plex Sans for chat body text.
- **Motif:** the claim card (rounded panel, colored type badge, confidence/risk stats, source line) is the repeated visual signature — it also carries into the marketing deck and diagram built from this iteration.
