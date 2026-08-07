
# Ledger - PM
Ledger was supposed to be a suite of agents tasked with helping go from concept to working prototype. What the first iteration of Ledger actually is, is an agent that asks probing questions to hone ideas. 
Ledger has 5 gates:
# Concept: 
This is where we start broad, narrow, or anything in between. Provide an idea for a product and then work through the questions Ledger will ask. It was designed to be thorough and grounded in reality unless you specifically advise to ignore something for the purpose of moving on to another issue or getting to the next gate. 
# Validate:
This is where more of the heavy lifting and some condescension (not specific instruction by the way) comes in. Ledger starts poking at whatever you brought into the Concept gate — asking for the source behind anything that sounds like a fact, flagging the numbers you clearly pulled out of thin air, and generally acting like the most skeptical person in the room. There are two settings for how hard it pushes: Exploratory mode, which lets pattern-based guesses through as long as they're clearly labeled, and Board-Ready mode, which refuses to guess at all — it just tells you what real number or source you'd need to go find instead. Exploratory is for when you're still playing. Board-Ready is for when you're not.
# Prototype:
This is the gate where the idea starts turning into something you could actually put in front of someone. Ledger doesn't build the thing for you so much as force you to get specific enough that building it becomes possible — what's the actual flow, what's the interaction, what does someone click. If you've been vague up to this point, this is where that catches up with you.
# GTM:
Go-to-market. This is where the real numbers show up — revenue models, capitalization estimates, regulatory constraints if your idea touches anything regulated. Every claim Ledger makes here gets logged to something called the Evidence Ledger: a running tally of every number it's given you, tagged as factual, unverified, speculative, or disputed, each with a confidence score, a risk-of-error score, and where it supposedly came from. In Board-Ready mode it won't hand you an unsourced figure at all. In Exploratory mode it'll still guess — it just won't pretend the guess is anything more than a guess.
# Pitch:
The last gate. Everything gets packaged into something you could actually present to a decision-maker. This is usually where you find out how many of your "facts" from Concept were actually assumptions wearing a nice outfit.

## Additional Agents in this suite:
# Product Owner Agent (PO Agent)

Takes whatever Ledger hands off — the artifacts from a concept that's made it through the gates — and turns it into an actual backlog: features, user stories, Gherkin acceptance criteria, one cell per story so it imports cleanly into tools like Rally. Thinks like an Agile PO, not like Ledger — less "prove it," more "here's what needs to get built and how we'll know it's done." Status: design decisions locked (CSV output, single-cell AC, placeholder feature IDs), build approach still being worked out.

# Dev Agent (Prototyping Agent)
Takes ideas from Ledger and backlog items from the PO agent and turns them into something visual — low-fi wireframes, grayscale, structure and layout only, deliberately not styled or interactive. The point is minimal and functional, not pretty. Sometimes pairs with a small dataset (Excel or a lightweight SQL setup) so the prototype has real-ish data behind it instead of lorem ipsum. First real test case: running the Medicare Advantage co-op concept end to end through both the dataset and the wireframes.

# QA Agent (Listener Agent)
Actually two agents wearing one name so far. The first is a generalized, non-insurance-specific agent that takes test case data — general QA patterns plus (eventually) real historical test cases — and produces a reference library of acceptance-criteria templates for the PO agent to draw from. That one's built, and it ported cleanly into a Copilot agent builder at work, where historical test case data that can't leave the workplace gets layered in separately — meaning the work and personal versions are starting to diverge on purpose. The second is a planned listener that would sit after the PO agent and Dev agent once both exist, catching issues in their output after the fact instead of expecting each agent to self-correct inline — that one's decided on, not built yet.
