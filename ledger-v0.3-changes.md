# Ledger v0.3 — Structured Output via Tool Use

*Companion to `ledger-spec.md` (v0.1 architecture) and `ledger-v0.2-changes.md` (live search + tone). This is the fix for the failure class documented in `ledger-spec.md` §6.*

---

## What changed, and why it was the top roadmap priority

Every parsing failure hit during v0.1/v0.2 testing — the empty-response crash, the prose-contamination errors, the mid-generation truncation errors — shared one root cause: Ledger's structured data was being requested as **free text that happened to look like JSON**, asked for entirely through prompt instructions ("respond with ONLY minified JSON..."). The model was, in effect, competing against its own instinct to write conversational prose every single turn, and occasionally lost.

v0.3 replaces that with the Claude API's actual structured-output mechanism: **tool use.** Instead of asking for JSON in the reply text, Ledger now calls a defined tool — `log_ledger_turn` — whose schema is enforced by the API itself. The stage, reply, ledger entries, and assumptions arrive as an already-parsed object (`tool_use` block's `input` field), not a string that has to survive a `JSON.parse()`.

---

## What was removed

The entire multi-stage parsing cascade from v0.1/v0.2 is gone:

- Markdown code-fence stripping (` ```json ` handling)
- The `{...}` extraction fallback for prose-wrapped JSON
- The string-sniffing truncation detector (checking parse-error messages for "unterminated", "unexpected end of input")

None of it is needed anymore. The API either returns a valid tool call or it doesn't — there's no in-between state of "technically text, sort of shaped like JSON" to reverse-engineer.

## What replaced it

- **`LEDGER_TOOL`** — a JSON Schema definition for `log_ledger_turn`, with real constraints the API enforces: `enum` on `stage` and `type`, `minimum`/`maximum` on `confidence`/`risk`, `maxLength` on `claim`/`source`/`reply`, `maxItems` on `ledger_entries`. These were previously prose asks ("keep claims under 15 words") that the model could and did occasionally ignore. They're now schema constraints.
- **A definitive truncation signal.** The API reports `stop_reason: "max_tokens"` when generation is cut off. v0.1/v0.2 had to *guess* at truncation by pattern-matching a JSON parse error message. v0.3 checks the actual field the API provides — no guessing.
- **A much narrower fallback path.** If the model somehow doesn't call the tool, Ledger still degrades gracefully to showing any plain text present (same behavior as v0.1/v0.2's prose-contamination handling) — but this should now be rare, since tool use is a distinct generation mode the model doesn't have to fight its own conversational instincts to use correctly.

---

## The one thing this did NOT simplify: search coexisting with structured output

This was the real design tension in this build, worth documenting honestly rather than glossing over.

Anthropic's API lets you force a specific tool via `tool_choice`. The obvious move would have been to force `log_ledger_turn` on every call. **That would have broken web search** — a model forced to call one specific tool immediately can't also decide to search first. Since v0.2's live grounding is the whole point of a lot of this suite, that tradeoff wasn't acceptable.

v0.3 instead leaves `tool_choice` on its default (`auto`), makes both `web_search` and `log_ledger_turn` available every turn, and relies on the system prompt to instruct: search first if needed, then always finish by calling `log_ledger_turn`. This is a real, if small, step back from "guaranteed" structured output toward "reliably instructed" structured output — the fallback path exists precisely because this isn't airtight. In practice this is still a large reliability improvement over prompt-based JSON, because tool-calling is a much stickier behavior for the model to follow than "write text that looks like JSON," but it's honest to say this wasn't a clean 100%-guaranteed fix — it was the best available tradeoff given that search needed to stay working too.

---

## What's still open

Structured output was one item under Roadmap §1 ("Reliability infrastructure"). The other two items in that same section — server-side error handling/retry logic, and a real backend replacing client-side `window.storage` — are unchanged and still open, along with everything in Roadmap §2 (specialist agent question) and §4 (production table-stakes). See `ledger-roadmap.md` for the current state of all of it.
