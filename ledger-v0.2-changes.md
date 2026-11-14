# Ledger v0.2 — Live Grounding + Configurable Tone

*Companion to `ledger-spec.md` (v0.1 architecture) and `ledger-roadmap.md`. This doc covers what changed in v0.2 and, more importantly, why one part of it was deliberately *not* made configurable.*

---

## 1. Live web search

Ledger now has real internet access via the Claude API's server-side web search tool. This is the single most-requested item from the v0.1 roadmap ("ground the claims for real") — up to now, every "unverified" or "speculative" tag was honest but permanent; nothing in the tool could actually resolve a claim to real, factual, cited data.

**What actually changed:**

- The API request now includes `tools: [{ type: "web_search_20250305", name: "web_search" }]`. This is a server-side tool — Anthropic's infrastructure runs the search and returns results within the same API call. No client-side tool-use loop was needed.
- The system prompt's old "you have no live web access" honesty rule is gone, replaced with an instruction to search before asserting anything that would otherwise be a guess, and to log the real URL or publication name in `source` when a search succeeds.
- Claim cards now render `source` as a clickable link when it's a real URL, instead of always rendering it as plain text.
- The footer copy was corrected — it previously said "Demo has no live data access," which would now simply be false.

**A real tradeoff, not a footnote:** enabling search increases the risk of the exact truncation failure mode documented in `ledger-spec.md` §6. The output token budget for this environment is fixed at 1000 tokens regardless of tool use, and a model that narrates its search process ("Let me look that up...") burns part of that budget on visible text before it ever produces the JSON object. The system prompt now explicitly instructs Ledger to search silently and emit only the final JSON — but this is a mitigation, not a guarantee. If truncation errors become more frequent in practice, this is the first place to look.

**Latency and cost are also real considerations that didn't exist in v0.1.** Every turn that triggers a search now takes longer and costs more than a turn that doesn't, in a way v0.1 simply never had to account for.

---

## 2. Configurable tone

Users can now adjust how Ledger delivers pushback — without changing whether it pushes back. Two controls:

- **Three presets** (Direct / Balanced / Supportive) — a segmented toggle in the header, next to the existing rigor-mode toggle.
- **A custom tone note** — free text, e.g. "use more encouraging language when flagging gaps." Applied on top of whichever preset is active.

Both persist across reloads the same way mode and stage already did, and switching either logs a visible marker in the chat transcript, consistent with how mode switches were already handled in v0.1.

**Tone and rigor mode are deliberately separate axes.** Rigor mode (Exploratory / Board-Ready) controls *how much grounding is required* before a number is allowed through. Tone controls *how the pushback sounds*. Conflating these would have been a mistake — a user might reasonably want board-ready rigor delivered supportively, or exploratory looseness delivered bluntly. Keeping them independent lets both preferences be set honestly instead of forcing a false tradeoff between rigor and kindness.

---

## 3. The one thing that is NOT configurable, on purpose

This is worth its own section rather than a bullet point, because it's a real design decision with a real justification, not a default that happened to survive.

**Tone changes delivery. It never changes substance.** A "Supportive" Ledger still flags every unsourced claim, still logs every weak assumption to the Evidence Ledger, still refuses to let a bad number pass as settled — it just phrases the pushback more gently while doing it. This is enforced by a dedicated clause in the system prompt (`TONE_INTEGRITY_CLAUSE`), which is appended *after* the mode rules, the tone preset, and any custom user tone note — specifically so that no combination of settings can quietly instruct it away.

**Why this matters enough to hard-code:** the entire premise of this tool, since v0.1, is that a claim's confidence and risk score mean something — that "factual" is earned, not asserted. A tone setting that could suppress a flag in exchange for sounding nicer wouldn't be a friendlier version of Ledger. It would be a tool that lies more comfortably. That's a worse product, not a more pleasant one, and it defeats the entire reason this suite exists. So the feature was built with the constraint baked into the architecture rather than left as a prompting hope — delivery is genuinely configurable; the presence of the pushback itself is not, and isn't intended to become configurable in future versions either.

---

## 4. What's still open (unchanged from the v0.1 roadmap)

Live search and tone were the two items pulled forward for v0.2. Everything else in `ledger-roadmap.md` is still open — structured outputs via tool use, real sub-agent orchestration (or dropping the "suite" framing honestly), calibration testing on whether confidence scores are actually calibrated, and the table-stakes production requirements (auth, real backend, cost modeling at scale). Search and tone didn't reduce that list; they were just next.
