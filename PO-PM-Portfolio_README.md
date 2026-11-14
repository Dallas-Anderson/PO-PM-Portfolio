# PO/PM AI Agent Portfolio

I'm a Product Owner with a background in APIs, data integration, and Agile delivery. This repo holds the AI agents I've been building to answer one question: **how much of product ownership can AI speed up without taking the judgment away from the person accountable for the product?**

Each agent produces real output files (backlogs, wireframes, acceptance-criteria libraries) that you can open and judge for yourself. The proofs of concept in this repo use concept and general-purpose data only, so none of it contains employer or customer data. The agents themselves are designed to work with real data. The QA agent has been ported into my work environment and is in limited use there, and Ledger's approach informed a separate, heavily adapted agent built for my organization's own framework. All private data stays separate from this repo. That isn't the focus here. This repo is about the thinking and the proofs of concept.

---

## The problem

Backlog writing, acceptance criteria, and early prototyping are slow, and the quality varies from person to person. AI can draft all three in minutes, but it also states guesses as facts and fills gaps without telling you. The design problem was never "can AI write a user story?" It was **"how do I keep a human in the judgment seat while AI does the drafting?"**

Every decision below comes from that question.

---

## The suite at a glance

| Agent | What it does | Output | Status |
|---|---|---|---|
| **[Ledger](ledger-README.md)** | Takes an idea from concept to pitch through five gates (Concept, Validate, Prototype, GTM, Pitch), asking probing questions and logging every claim to a visible Evidence Ledger | A pressure-tested idea with its evidence trail | Built |
| **[Product Owner Agent](product-owner-agent-README.md)** | Turns Ledger's output into a backlog of features, user stories, and Gherkin acceptance criteria | CSV formatted for import into tools like Rally | Built; has produced a backlog |
| **Dev (Prototyping) Agent** | Takes Ledger ideas and backlog items and produces low-fidelity wireframes, with a small supporting dataset when useful | Grayscale layout-only wireframes | Built; has produced wireframes for one complete concept |
| **[QA Agent](qa-listener-agent-README.md)** | Two roles: (1) a general-purpose agent that builds a library of acceptance-criteria patterns, and (2) a planned listener that reviews other agents' output after the fact | AC pattern library (built); output reviews (planned) | Library built; listener planned |

---

## Design decisions, and why I made them

**1. Every claim gets an evidence tag.**
Ledger logs each claim with a type (factual, unverified, speculative, or disputed), a confidence score, a separate risk-of-error score, and a source. The point is that AI output can't quietly pass a guess off as a fact. A reader can see at a glance what is solid and what is not.

**2. Two rigor modes.**
*Exploratory* mode allows clearly labeled guesses, which is useful early on. *Board-Ready* mode refuses guesses and points you to the real data you need. Early thinking and decision-grade thinking need different standards, and the tool shouldn't blur them.

**3. Backlog output is a CSV built for import.**
Acceptance criteria are packed into a single cell per story so the file imports cleanly into Rally-style tools. The `feature_id` column is a fixed placeholder (`XXX`) instead of generated IDs, because I didn't want to assume any one tool's feature ID naming convention.

**4. Wireframes are low-fidelity and grayscale on purpose.**
Layout and structure only. That keeps the conversation on flow and function before anyone debates colors.

**5. The AC pattern library is a standalone document, reviewed by a human before it reaches the PO agent.**
I chose not to bake patterns into the agent's prompt or let it look them up live. A person reviews the patterns first, so they can't quietly shape output without oversight. The first version is built from general QA patterns, with my own test cases to be layered in later. The same library has since ported cleanly into a different agent platform (Microsoft Copilot) where separate, private data is layered in.

**6. QA is a separate agent that listens, not a self-check inside each agent.**
An agent grading its own work has the same blind spots that produced the work. A separate reviewer that sits after both the PO and Dev agents is a cleaner check.

---

## Where things stand

- **Built:** Ledger, the Product Owner agent, the Dev (prototyping) agent, and the AC pattern library (v1)
- **Proven end to end:** one complete concept, taken from Ledger through backlog to wireframes
- **Next:** running more concepts through to the prototype phase
- **Planned:** the listener QA agent, my own test cases layered into the pattern library

I'm being direct about status because I'd rather show honest work in progress than polished claims.

---

## Where to start

- **The thinking behind Ledger:** start with the [Ledger README](ledger-README.md), then the [spec](ledger-spec.md) for what's actually built and the [roadmap](ledger-roadmap.md) for where it goes next.
- **Ledger applied to a concept:** the [co-op health plan concept brief](coop-health-plan-concept-brief.md), along with its [pitch deck](morgan-county-pitch-deck.pptx) and [regulatory timeline](morgan-county-regulatory-timeline.xlsx).
- **The Dev agent's wireframes for that concept:** five low-fidelity pages, [member benefits](01_member_benefits_overview.html), [SSBCI case manager](02_ssbci_case_manager.html), [vendor network](03_vendor_network.html), [compliance dashboard](04_compliance_mlr_dashboard.html), and [premium transparency](05_premium_transparency.html). They are generated from a small dataset ([coop_health.db](coop_health.db)) by [build_dataset.py](build_dataset.py) and [generate_wireframes.py](generate_wireframes.py). The pages are HTML, so download them to view in a browser.
- **Ledger itself:** the [interactive mockup](ledger-pm-agent-mockup.html) (a single HTML file, so download it to open it), the [agent workflow diagram](ledger-agent-workflow.mermaid), and the [marketing mockup deck](ledger-marketing-mockup.pptx).
- **How it evolved:** the [v0.2 changes](ledger-v0.2-changes.md), the [v0.3 changes](ledger-v0.3-changes.md), and the [session export](ledger-session-export.md).
- **The other agents' design:** the [PO Agent README](product-owner-agent-README.md) and the [QA Agent README](qa-listener-agent-README.md).

---

## About

Product Owner with experience in API products, data integration, and enterprise Agile delivery, currently exploring how AI changes the way product teams work. Connect with me on [LinkedIn](https://www.linkedin.com/in/dallas-anderson-a8a59a8/).
