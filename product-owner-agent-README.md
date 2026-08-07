# Product Owner Agent

An agent that takes validated concept artifacts from [Ledger](../ledger/README.md) and turns them into a structured backlog — features, user stories, and Gherkin-style acceptance criteria — written from the perspective of an Agile Product Owner.

## What it does

- **Input:** markdown or plain-text artifacts handed off from Ledger (a validated concept summary, key requirements, constraints)
- **Output:** a CSV backlog, with one row per user story, including:
  - Feature grouping
  - User story (standard "As a... I want... so that..." format)
  - Acceptance criteria in Gherkin (Given/When/Then), packed into a single cell per story so it imports cleanly into backlog tools like Rally
- **Perspective:** the agent reasons about scope, story-splitting, and acceptance criteria the way an Agile PO would — not just summarizing the input, but making the judgment calls a PO makes when turning a concept into workable backlog items

## Why CSV, and why a single cell for AC

Backlog import tools (Rally, Jira, Azure DevOps) generally expect one row per story with acceptance criteria as a single field rather than split across rows — so the output is structured to be pasted straight into a real tool with minimal cleanup, rather than needing reformatting first.

## Design notes

- Feature IDs are currently a placeholder value across all rows rather than generated sequentially — ID assignment is intentionally deferred to whatever tool the backlog lands in, since that's usually where real ID governance happens anyway
- Built as a standalone agent for now (not yet wired to Ledger automatically) — the handoff today is manual: an artifact from Ledger is fed in as input

## Sample output

See `outputs/` for an example backlog CSV generated from a sample concept brief.

## Where this feeds

Backlog items from this agent are one of the two inputs (along with raw Ledger ideas) for the [Dev/Prototyping Agent](../dev-agent-prototyping/README.md), which turns them into low-fidelity UX wireframes.
