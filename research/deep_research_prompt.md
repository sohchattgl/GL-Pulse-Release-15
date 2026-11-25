
GOAL

Produce a research brief on the module described below. A curriculum team will turn the brief into a 20 to 30 minute video module for working professionals. Stop when every section is backed by retrieved sources and the source ledger is complete. If the hook or the value proposition cannot be supported by retrieved material, say so in the unverified claims appendix instead of estimating or softening the claim.

CONTEXT

Module under research (the only block that changes per release):

- **Title**: Every Cell Gets a Receipt: How Much AI-Filled Data Do You Need to Check?
- **Format**: Deep Dive
- **Hook** (the opening claim the module must earn): Until now, when AI filled a spreadsheet column, every value looked equally confident and none showed where it came from, so you either checked every cell or trusted none. On 30 October 2026, Google added cell-level citations to Fill with Gemini in Sheets, so each AI-generated cell now shows the web sources behind it. That makes AI-filled data checkable one cell at a time. But a citation shows where a number came from, not whether it's right: sources go out of date, get misread, and disagree with each other. The question has moved from "can we trust AI data?" to "how much of it do we have to check?"
- **Value proposition** (what a learner walks away with): Learn a four-step trust ladder for any AI tool that cites its sources: read the citation, spot-check a sample, cross-check a second source, then sign off. Learn the three ways a cited cell still fails: the source doesn't support the value, the source is out of date, or credible sources disagree. In the hands-on, you watch Gemini fill a 20-company list with headquarters and headcount. You then audit five of its cited cells in a saved copy that every learner shares, logging each as pass or fail. Finally, a sampling calculator shows why five clean cells prove less than they seem: if one cell in ten is wrong, a five-cell check catches it only 41% of the time. You leave with an audit tab for any AI-filled sheet and a sampling rule your team can adopt.
- **Target** publish date:08 Dec 2026
- **Today**: 25 Nov 2026

Audience, three segments of equal weight:

- Working engineer: wants concrete technical detail, architecture, trade-offs, and implementation specifics as an evaluative or build framework.
- Non-technical manager: needs a mental model to evaluate or act on this development without reading code.
- Early-career learner: needs the development to be reproducible as a portfolio project or a daily workflow.

Situation: three research tools run this prompt in parallel. A person reconciles the three briefs and audits every claim against your source ledger before anything reaches a learner. The module opens on the hook above and promises the value proposition above, so the brief must test both against evidence rather than assume them. Fast-moving AI products change weekly; a claim that was true last month may be false at publish date.

Role and voice: you are a production researcher. Retrieve and synthesise source material. Write in a practitioner register: named people saying specific things on specific dates. Do not contribute opinions of your own and do not use training-data knowledge about these products; it is unreliable for this subject and is out of scope.

References (source selection):

- First: official documentation, release notes, product pages, system cards, and posts by the people who built the thing.
- Second: named practitioners writing from direct experience, named researchers, and technical journalists with a record on the subject.
- Excluded: aggregators, SEO content farms, anonymous forum claims, and vendor marketing without deployment evidence.
- Any claim from a source older than 7 days that plausibly moves (pricing, limits, availability, benchmark figures) is re-verified before it is reported.

Outputs: one markdown document with the skeleton below. Headings are fixed. The structure under each heading follows the material, not a template.

1. What it is and what changed
   What the development is, who made it, when it shipped, what existed before, and what specifically changed. Concrete deltas, no "faster, better, easier" abstractions. Why it matters, stated separately for a technical and a non-technical reader.
2. How it works
   The mechanism. Cause and effect, one link at a time, in the order a careful reader would need to follow it. Name the concepts and show how they connect. Depth matters more than coverage here.
3. Evidence
   Documented use cases: who, what they built, the reported outcome, source and date. Practitioner voices: at least five named people, platform, date, exact quote, and whether each confirms or contradicts the official account. Contradictions kept side by side, never resolved.
4. Limits
   Failure modes with conditions, frequency, and magnitude. At least two technical limitations and one non-technical risk. What the development is explicitly not for, from documentation or practitioner evidence.
5. Where to try it today
   Every place one person can run the development today without writing code first, then with one setup command: the vendor's playground, console or dashboard; no-code platforms with a step, piece or connector for it (Activepieces, Zapier, n8n, Make and similar); hosted demos (Hugging Face Spaces, in-browser builds); and local runs. For each: what it runs, the access state (open, waitlist, paused), the account and price needed, what of the output it shows on screen, the URL, and the date checked. Mark every row [MONITOR].

Appendix A. Source ledger: every source used, as a table with URL, date accessed, and the claim or claims it supports.
Appendix B. Unverified claims: the hook and the value proposition, each marked supported or unsupported with the evidence found, plus any other claim in the module framing that retrieved sources do not support.
Appendix C. MONITOR flags: every time-sensitive claim, listed with its section, so it can be re-checked before the script is finalised.

SUCCESS CRITERIA

1. Every factual claim carries an inline citation of the form [source: URL, accessed YYYY-MM-DD], and every cited source appears in the ledger.
2. Every number and every date traces to a primary source with a date.
3. At least five named practitioners are quoted exactly, with paraphrases marked "(paraphrase)", and disagreements between sources are preserved side by side.
4. The hook and the value proposition are each marked supported or unsupported in Appendix B, with the evidence.
5. The "How it works" section explains cause and effect in an order a non-technical manager can follow without a glossary.
6. Every time-sensitive claim carries [MONITOR] inline and appears in Appendix C.
7. "Where to try it today" lists at least one surface per product or model the brief covers, each with its access state, account and price, and the date checked, or says plainly that none was found.
8. Delivery: markdown, the five numbered headings and three appendices, 4,000 to 6,500 words, no preamble and no closing remarks.

Before you finish, verify the brief against these eight criteria and fix what fails.
