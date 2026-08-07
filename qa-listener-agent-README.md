# QA Listener Agent

*Status: early design — scope and architecture still in progress. This README describes the direction, not a finished build.*

## The idea

Rather than having each agent in this suite try to self-correct its own output inline, the QA Listener sits **after** the [Product Owner Agent](../product-owner-agent/README.md) and [Dev/Prototyping Agent](../dev-agent-prototyping/README.md), reviewing what they produce and flagging issues — a dedicated quality pass instead of built-in self-checking.

## Two directions being explored

1. **Output listener** — reviews backlog items and prototypes after they're generated, checking for gaps, inconsistencies, or quality issues before they're treated as final.
2. **Acceptance criteria pattern library** — a related but distinct piece: an agent that analyzes test case data (general QA patterns, plus eventually real test cases) to build a reference library of AC templates and patterns the PO Agent can draw from. This is meant to be a standalone reference doc that gets reviewed and manually fed into the PO Agent's process, rather than something the PO Agent looks up live.

## Why split it this way

Keeping QA as a separate, after-the-fact listener (rather than baked into each agent) keeps each agent's core logic simpler, and makes it possible to swap in a better QA process later without touching the agents it's reviewing.

## Current state

The AC pattern library direction has an early working version, built from general QA testing patterns. It's since been adapted into a separate work-context version to layer in real test case data there. The output listener direction hasn't been built yet.
