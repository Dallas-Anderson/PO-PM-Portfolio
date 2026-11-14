# [Working name] — Co-op Medicare Advantage Concept Brief

*Synthesis of concept + grounded research to date. Confidence and source labels follow throughout — this is a validation working document, not a finished business case.*

> **Portfolio note:** This document is a demonstration of the Ledger PM Agent's capabilities — grounded research, explicit confidence/risk scoring, assumption-flagging, and regulatory synthesis applied to a product concept in real time. It is **not** a real business plan, and the co-op described here is not a venture being pursued. Every figure, source, and open question below is genuine — the research is real — but the exercise itself exists to show how a PM Agent reasons through ambiguity and ties research to product decisions, not to advance an actual company.

---

## 1. The thesis, as stated

A community-focused health plan, structured as a co-op, positioned as a **replacement for the "buy Original Medicare + Medigap" path** — one plan instead of two purchases. Two stated differentiators:

1. **Premiums fund more than ailment coverage** — some portion of member premium supports community/member benefit beyond paying claims.
2. **Premium transparency is the core differentiator**, not a compliance afterthought.

**Confirmed by you:** this is structured as a **Medicare Advantage plan** — CMS pays a per-member-per-month capitated rate, the plan bears risk, and MA's 85% MLR rule governs the split. This is *not* a Medigap-style supplement product, which would mean no CMS capitation, member-paid premiums instead, and state-level NAIC regulation with no federal MLR floor as strict as MA's. Everything financial in this brief assumes the MA path.

---

## 2. The tension your differentiator creates — resolved as a scenario (option (a) chosen)

**Factual, confidence: very high** — MA plans face a hard federal floor: at least 85% of capitation revenue must go to claims and CMS-recognized quality improvement activities; administration, taxes, and profit/reserves must fit inside the remaining ≤15% (42 CFR §422.2410).

**You've chosen to play out option (a): structuring "more than ailment coverage" as an MA supplemental benefit, spending inside the 85%, not competing with the 15%.** This is a real, CMS-recognized mechanism, not a workaround — it splits into two lanes:

**Lane 1 — Primarily health-related supplemental benefits (uniform, every member).** Since 2019, CMS has allowed nonmedical services such as adult daycare, in-home support, and caregiver support to count as primarily health-related benefits, offered equally to all enrollees — no eligibility test. For this co-op: dental/vision/hearing, a wellness stipend, transportation to appointments, telehealth. This is the baseline "your premium buys more than claims coverage" layer every one of the ~700 members feels.

**Lane 2 — Special Supplemental Benefits for the Chronically Ill (SSBCI), targeted only.** Added by the Bipartisan Budget Act of 2018, this lets MA plans offer benefits *not primarily health related* to enrollees who meet a real regulatory bar: one or more comorbid, medically complex chronic conditions that are life-threatening or significantly limit health or function, combined with high risk of hospitalization. CMS-approved real-world examples: meal delivery, non-medical transportation (e.g., grocery runs), pest control, and home environment modifications tied to a chronic condition. **Constraint that matters:** each SSBCI must have a documented "reasonable expectation of improving or maintaining the health or overall function" of that specific member, and CMS must approve the non-uniform benefit design before it's offered — this can't be open-ended community spending, it has to be individually justified and CMS-filed.

**The differentiator story this makes possible, my synthesis:** because Lane 2 has to be delivered as real local services — home modification, pest control, transportation, food — those services could be sourced from **local Morgan County vendors and nonprofits** rather than a national supplemental-benefits contractor. That would mean the same dollars satisfying the 85% MLR requirement also recirculate into the local economy, turning "community-focused" into a mechanism, not just a tagline.

**What's still unresolved, flagged honestly:**
- No sourced estimate yet of what share of ~700 Morgan County enrollees would actually meet the SSBCI "chronically ill" bar — needs real prevalence data or an actuary's estimate, not a guess.
- Lane 2 is funded by rebate dollars from bidding under the CMS benchmark; at 700 members that pool is real but modest, not deep.
- **Speculative, low confidence, needs verification:** new MA contracts likely lack an established Star Rating in their first year(s), which typically affects quality-bonus rebate dollars specifically (distinct from the base under-benchmark rebate) — if true, year-one Lane 2 funding likely leans on the base rebate alone. Confirm directly with CMS guidance before sizing this.
- CMS approval of the benefit design and eligibility criteria is a real filing step, not a unilateral marketing decision.

---

## 3. Transparency as differentiator — what we actually found

**Factual, confidence: high, from earlier research in this conversation.** Searching for major Medigap/MA carriers' voluntary premium transparency practices (beyond what NAIC/CMS legally requires) turned up **nothing** — no AARP/UHC, Cigna, Aetna, Humana, or Mutual of Omaha public commitment to disclosure beyond the standardized Outline of Coverage and state rate filings.

**What this means, my synthesis:** that's either a real whitespace opportunity or an unexplored one — the search wasn't exhaustive (we didn't check investor-relations archives or trade press systematically). But directionally, no major incumbent appears to be marketing transparency as a differentiator the way you're proposing. That's worth a deeper competitive pass before you build a positioning strategy on it.

**Speculative idea, not something you've asked for — flagging as an option, not a recommendation:** the Evidence Ledger mechanic built into your Ledger mockup (every claim stamped with confidence, source, risk) could become a literal *member-facing* product feature — e.g., an annual premium changes explained with the same rigor, rather than a compliance-mandated Outline of Coverage buried in fine print. That would make "transparency" a felt product experience, not just a claim in marketing copy.

---

## 4. Target market data pulled so far

**Factual, confidence: very high, source: U.S. Census Bureau, ACS 2020–2024 5-year estimates.** Morgan County, Colorado:

- Population: 30,306 (2025 estimate)
- Median household income: $73,278
- Per capita income: $32,280
- Persons in poverty: 14.0%
- Persons 65+: 17.8% of population

**Confirmed by you:** Morgan County is the actual pilot market. A rural county with income meaningfully below state median and a poverty rate half again the state average is a plausible fit for a co-op's "we're not extracting profit from you" positioning — but I still haven't validated MA competitive density, provider network availability, or existing plan options in that specific county, all of which materially affect viability. That's the natural next research step (see §6).

---

## 5. Financial architecture modeled so far — all speculative, none of it validated

| Element | Figure | Confidence | Status |
|---|---|---|---|
| CMS capitation benchmark | $900–$1,100 PMPM | Flagged illustrative, not sourced | Needs real CMS rural CO benchmark rate |
| Monthly revenue @ 700 members | $630K–$770K | Derived from above | Same caveat |
| Claims (value-based contracts) | ~86% of revenue | Low-moderate (~40%) | Regulatory floor is 85%; exact split above that is a guess |
| Administration (incl. transparency app) | ~10% of revenue | Low (~25%) | National MA average is ~8%, but that's carriers at massive scale — 700 members likely runs higher |
| Reserves/margin | ~4% of revenue | Low (~25%) | Whatever's left after claims + admin, not independently validated |
| Statutory minimum capital (CO) | $1.0M–$2.6M | High — Colorado DOI, cited directly | Real floor, confirmed |
| Risk-based capital cushion | ~$3M–$8M | Low (~30%) | Needs an actuary to run your actual RBC formula |
| Pre-revenue build/ramp cost | ~$2M–$5M | Low (~25%) | Needs real vendor/staffing quotes |
| **Total illustrative capitalization ask** | **~$8M–$10M** | **Low-moderate (~35%)** | Planning placeholder, not a number for a leadership deck yet |

---

## 6. What would move this from ideation to a real validated concept

1. Get real prevalence data (or an actuary's estimate) for how many of the ~700 Morgan County enrollees would meet the SSBCI "chronically ill" eligibility bar — needed to size Lane 2 funding — §2.
2. Confirm directly with CMS guidance whether a new MA contract's Star Rating status in year one limits quality-bonus rebate dollars, since that affects how much Lane 2 can rely on bonus vs. base rebate — §2.
3. Identify actual Morgan County vendors/nonprofits capable of delivering Lane 2 services (home modification, pest control, transportation, food) — this is what turns the CMS mechanism into the "community investment" story — §2.
4. A real actuary running your NAIC RBC formula, replacing the pattern-based $3–8M cushion estimate.
5. Real vendor/staffing quotes replacing the $2–5M build-cost pattern estimate.
6. Pull actual MA plan density, existing competitor plans, and provider network availability for Morgan County specifically — the pilot market is confirmed, this data isn't yet.
7. A deeper, systematic competitive scan on premium transparency — investor relations, trade press, state DOI bulletins — to confirm the whitespace claim in §3 before it becomes a marketing pillar.
