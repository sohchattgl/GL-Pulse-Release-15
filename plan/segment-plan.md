# Segment plan: Every Cell Gets a Receipt

Release folder: `Release 15` (the working directory). Briefs read: `research/research-brief-claude.md`, `research/research-brief-gemini.md`, `research/research-brief-openai.md`. Reconciliation: `plan/reconciliation.md`.
Hook: Since late October 2026, every web-sourced cell that Fill with Gemini writes in Google Sheets carries the pages behind it, which makes each value checkable one cell at a time; a citation records where Gemini looked, so the open question is how much of the column we have to check. Status: partially supported. The title comes from the Claude and Gemini briefs; the hook's "30 October" is corrected to the 28 October announcement, and "none showed where it came from" is scoped to Google Sheets.
Value proposition: The learner can say what a cited cell proves, name the three ways it still fails, read what a small clean sample does and does not show, and set how much to check by how the column will be used. Status: partially supported (41% supported by computation in all three briefs; the four-step ladder is our own framework; the third failure mode has no documented Sheets case).
Audience: working engineer, non-technical manager, early-career learner.

## Shape sheet

| Signal | Reading from the briefs |
|---|---|
| Framework cardinality | Three failure modes (page does not say it, page out of date, credible pages disagree). Four steps in our checking ladder (read, sample, cross-check, sign off). Four checking tiers by how a column is used (Shukla, Jose S., UD). Two sampling numbers (catch rate, error ceiling). |
| Chronology | One thread, four dated steps: AI function June 2025 (200 cells), Search grounding October 2025, Fill with Gemini April 2026, per-cell sources and 3,000 cells October 2026. A single `timeline` is earned; no second rail. |
| Binaries | Where Gemini looked against what the page says. Top rows against random rows. Five clean cells against thirty clean cells. |
| Worked example | Jose S.'s 200-supplier headquarters list: 30 random rows, 29 matched, directory-sourced rows then checked one by one (Gemini brief). Liu et al.'s audit of four search engines (Claude, Gemini). Dixon's five-assistant test (Claude). |
| Tensions and costs | Speed of entry (55x, 3,000 cells) against time to check (under a minute a cell, about half an hour for 30). One slide's worth inside the sampling segment and the decision segment; no costs segment. |
| Reversal (click candidate) | Reconciliation 6.1 to 6.5. Strongest: five clean cells allow an error rate up to 45% (6.4), placed in the third segment. Others: the citation records where Gemini looked (6.1), the update made the run bigger (6.2), wrong answers look like right ones (6.3), the top tier should not be AI-filled (6.5). |
| Experience (opening) | A column of AI-filled company facts lands with us; we check the first few rows, they look fine, and we pass it on (Gemini "Teams routinely spot-check the top five rows of a column"). |
| Audience vocabulary ceiling | Spreadsheet, column, cell, source, sample, error rate, "one in ten". No binomial, hypergeometric, confidence interval, groundingMetadata or API. The engineer gets the exact figures and the named mechanism, told as consequence. |

## Spine

4 segments.

| # | Title (2 to 4 words) | Job | Why, from the shape sheet | Slides | Est. minutes |
|---|---|---|---|---|---|
| 1 | A Source in Every Cell | origin: what changed and how a value gets its source | orientation <- chronology (one thread) and the click 6.2 | 4 | 5 to 6 |
| 2 | Where Gemini Looked | single mechanism: what a citation proves, and three ways a cited cell fails | deep dive <- the three-part failure framework and click 6.1, 6.3 | 5 | 6 to 7 |
| 3 | Five Clean Cells | worked arithmetic: what a small clean sample shows | sampling <- binaries (top against random, five against thirty) and click 6.4 | 5 | 6 to 7 |
| 4 | How Much to Check | decision: a checking tier for each column, and the module close | decision <- the four-step ladder, the worked example, the four tiers and click 6.5 | 6 | 6 to 7 |

## Segment 1: A Source in Every Cell

Job: Show what Google changed in October 2026 and how a filled value comes to carry its sources. Opens on: the column we checked by its first few rows and passed on. Closes on: before trusting a column, count its cells; then hand off to what one of those sources actually proves.

| Slide | Beat | Content signal | Layout | On the slide | Narration draws from (brief, first words of passage) | Provenance |
|---|---|---|---|---|---|---|
| 1 | experience | the shared experience | `cover` | Title "A Source in Every Cell"; subtitle as the experience line: a column of AI-filled company facts arrives, we check the first few rows, and we pass it on. | Gemini "Teams routinely spot-check the top five rows of a column"; OpenAI "Before this update, Fill with Gemini could generate data but provided *no* provenance" | 2 briefs |
| 2 | mechanism | one thread, four dated steps | `timeline` | June 2025: AI function, first 200 cells. October 2025: answers grounded in Google Search, with no sources shown. April 2026: Fill with Gemini, drag or select and fill. October 2026: sources in every web-sourced cell, up to 3,000 cells. Note: MONITOR, rollout from 20 October 2026, web only, eligible plans. | Claude "Google introduced the AI function"; Claude "From 15 October 2025, Google began"; Claude "On 22 April 2026, Google introduced Fill with Gemini"; Claude "On 28 October 2026, Google's Workspace team published"; Gemini "Prior to October 20, 2026, any external web fact" | 28 Oct and 3,000: 3 briefs; Oct 2025: 1 (Claude); date contradicted (30 Oct recap), side taken 28 Oct; MONITOR |
| 3 | mechanism | a process of five steps | `flow` | We ask Sheets to fill empty cells; the function reads only the row we point it at; Google Search finds pages; Gemini writes one value; the pages it used attach to that cell. Footer: the value is fixed once inserted and does not refresh when the web changes. | Claude "Step 1: A user asks Sheets to fill empty cells" through "Step 6: The value is frozen"; Gemini "Everything starts in the spreadsheet grid"; OpenAI "In sequence, the process is" | 3 briefs (no-refresh: 2) |
| 4 | click (6.2) + landing beat | a measurable before and after | `two_number` | Before: 200 cells per run (June 2025). After: 3,000 cells per request (October 2026). Note: MONITOR, Google's help page still says 350 cells. | Claude "Step 7: Why citations create a sampling problem"; Claude "Speed claims. '9x faster"; Claude "Cells per run"; Gemini "First, batch size"; OpenAI "Performance claims" | 200: 2 briefs; 3,000: 3; 350 contradicted; MONITOR |

The click: the same update that made one cell cheap to check made a single run fifteen times bigger, and the 55x speed figure measures entry, never checking. Landing beat: count the cells before trusting the column. Hand-off: what one of those sources proves.

MONITOR flags in this segment: rollout from 20 October 2026 and web-only (slide 2); 3,000 cells per request against the 350-cell help page (slides 2 and 4); 55x claim if spoken (slide 4).
Pronunciations needed: Gemini (JEM-in-eye); Fill with Gemini; Google Sheets; "AI function" read A I function.

## Segment 2: Where Gemini Looked

Job: Establish what a cell's citation proves and the three ways a cited cell is still wrong. Opens on: we click Sources, a real page opens, and we move on. Closes on: when a cell passes, write down the sentence on the page that states it; hand off to how many cells we can afford to do that for.

| Slide | Beat | Content signal | Layout | On the slide | Narration draws from (brief, first words of passage) | Provenance |
|---|---|---|---|---|---|---|
| 1 | experience | the experience of opening a source | `cover` | Title "Where Gemini Looked"; subtitle: we open a cell's sources, a real company page appears, and we take the value as checked. | Claude "Google itself presents the change as an audit aid"; Gemini "a clickable Sources badge can paradoxically heighten automation bias" | 2 briefs |
| 2 | mechanism | a binary contrast on one dimension | `two_card` | "Where it looked": the citation records which pages Gemini used for the value. "What the page says": whether the page states that value is a separate question, and Google's post does not claim it. | Claude "A source in a cell shows where the AI looked"; Claude "Step 5: How a grounded answer is linked"; Gemini "A source shows where Gemini found the answer"; OpenAI "the mechanism does *not* guarantee correctness"; Claude "Its post does not claim the cited pages are right" | 3 briefs |
| 3 | mechanism | three items that must each read as memorable | `numbered_list` | 1 The page does not say it: misread table, wrong subsidiary, page names the company without the figure. 2 The page is out of date: an old directory still cited after headcount changed; the cell never refreshes. 3 Credible pages disagree: full-time staff in a filing against headcount with contractors; Google's own two pages say 350 and 3,000. Note: MONITOR on the 350 and 3,000 figures. | Gemini "At the grounding-link stage, the language model can misread"; Gemini "At the web-search stage, Google Search can return an outdated"; OpenAI "Dependence on search"; OpenAI "The AI also cannot resolve conflicts"; Claude "Failure mode C: credible sources disagree" | mode 1: 3 briefs; mode 2: 3 (illustrative); mode 3: 2, Claude finds no Sheets case, said plainly; MONITOR |
| 4 | mechanism | one number carries the slide | `stat_hero` | 74.5%. Caption: in a 2023 Stanford audit of four generative search engines, only 74.5% of citations supported the sentence they were attached to. Note: other products, 2023; no figure exists for Sheets. | Claude "Failure mode A: the source does not support the value"; Gemini "Nelson F. Liu, Tianyi Zhang, and Percy Liang (Stanford" | 2 briefs |
| 5 | click (6.1, 6.3) + landing beat | three peer findings read side by side | `three_column` | "Rated most helpful": Stanford 2023 found the answers people rated most useful carried more unsupported citations. "Wrong, not hesitant": the Tow Center found eight AI search tools more likely to answer wrongly than admit a limit. "No hedges": Dixon's test of five assistants found zero hedges on any failing answer. | Claude "Liu et al. found 'citation precision is inversely correlated"; Gemini "Klaudia Jaźwińska and Aisvarya Chandrasekar"; Claude "Every non-passing source answer on the board: 0 hedges"; Claude "It looks checked. I think that look is the risk" | 1 brief each (Stanford utility finding: 2) |

The click: the citation is what makes a wrong cell look checked; nothing in a wrong cell looks different. Landing beat: when a cell passes, copy the sentence from the page that states the value (Dixon "require the exact page, then find the claim on it"). Hand-off: with thousands of cells we cannot do that for every one, which brings us to counting.

MONITOR flags in this segment: 350 against 3,000 cells (slide 3).
Pronunciations needed: Gemini; Percy Liang (LEE-ahng); Tow Center (rhymes with "go"); Columbia Journalism Review.

## Segment 3: Five Clean Cells

Job: Work out what a small clean sample shows, and what a sample large enough to sign off costs. Opens on: five rows checked, five matched, the column signed off. Closes on: thirty random cells is about half an hour, and that half hour is what "under ten percent" costs; hand off to which columns deserve it.

| Slide | Beat | Content signal | Layout | On the slide | Narration draws from (brief, first words of passage) | Provenance |
|---|---|---|---|---|---|---|
| 1 | experience | the experience of a clean spot check | `cover` | Title "Five Clean Cells"; subtitle: we check five cells, all five match their sources, and we sign off on the whole column. | Gemini "Teams routinely spot-check the top five rows of a column, observe five matches" | 1 brief |
| 2 | mechanism | a binary contrast on one dimension | `two_card` | "The top five rows": the top of a curated list holds the larger, better-documented companies, so it passes more often. "Five rows at random": give every row a random number, freeze it, sort by it, and check the first five. | Gemini "Checking only the first five or ten rows of a list is a classic methodological error"; Gemini "To draw a true random sample directly inside Google Sheets" | 1 brief (Jose S.) |
| 3 | mechanism | one number carries the slide | `stat_hero` | 41%. Caption: if one cell in ten is wrong, a check of five random cells finds at least one error 41% of the time. Note: on a 20-row list the figure is about 45%. | Claude "When p = 0.1, the chance that a 5-cell sample"; Gemini "Plugging in p = 0.10 and n = 5"; OpenAI "Sampling result"; Claude "Correction for a short list" | 3 briefs (computed); short-list figure 2 |
| 4 | click (6.4) | a measurable before and after | `two_number` | Before: five clean cells, and the column could still be up to 45% wrong. After: thirty clean cells, and the ceiling falls under 10%. | Claude "What a clean sample proves"; Gemini "Second, consider the zero-error upper bound"; Gemini "Ten clean checks still leave room"; Claude "after 30 clean cells" | 2 briefs (computed) |
| 5 | mechanism (cost) + landing beat | a comparison of four sample sizes | `table` | Columns: cells checked at random; chance of catching a one-in-ten error rate; time at under a minute a cell. Rows: 5 (41%, about five minutes), 10 (65%, about ten), 20 (88%, about twenty), 30 (96%, about half an hour). | Gemini "Translated into an operational team policy"; Gemini "Reported checking an individual cited cell takes under a minute"; Claude "Sample size needed for a 95% chance" | 5 and 29/30: 2 briefs; 10 and 20: computed by the worker from the briefs' formula, recorded as computed; time: 1 brief |

The click: the five clean cells we signed off on are consistent with almost half the column being wrong. Landing beat: thirty random cells is about half an hour. Hand-off: which columns deserve that half hour.

MONITOR flags in this segment: none.
Pronunciations needed: Gemini; percentages read in full ("forty-one percent").

## Segment 4: How Much to Check

Job: Turn the arithmetic into a checking routine and a tier for each column, then close the module. Opens on: a manager asks how sure we are of the column going into the pricing deck. Closes on: the landing line below.

| Slide | Beat | Content signal | Layout | On the slide | Narration draws from (brief, first words of passage) | Provenance |
|---|---|---|---|---|---|---|
| 1 | experience | the experience of being asked to vouch for a column | `cover` | Title "How Much to Check"; subtitle: someone asks how sure we are of the filled column before it goes into a pricing decision. | Gemini "Yet raising single-request capacity to 3,000 cells amplifies operational risk"; Gemini "Managers now need a clear sampling rule" | 1 brief |
| 2 | mechanism | a process of four steps with a loop | `flow` | Read the citation; check a random sample; cross-check a second source; sign off with a note. Loop back: a failed sample sends that kind of row to a full check. Footer: no vendor names these four steps; they collect what careful practitioners already do. | Claude "the closest sourced practices are Dixon's 'require the exact page'"; OpenAI "Use Gemini's new cell citations as a route to the evidence"; Gemini "Click each sampled cell, hover over the value" | our own framework; parts from 3 briefs |
| 3 | mechanism (example) | one number carries the slide | `stat_hero` | 29 of 30. Caption: a 200-supplier headquarters list passed 29 of 30 random checks, and the audit note sent every directory-sourced row to a check of its own. | Gemini "Jose S. (Analytics Made Simple) | Worked 200-supplier headquarters-enrichment workflow" | 1 brief |
| 4 | click (6.5) | a comparison across four uses | `table` | Columns: how the column is used; what we check; what we can then say. Rows: a first look (five random cells, to catch a broken prompt); a list the team works from (thirty random cells; error under 10%); a figure that changes a decision (every source, or the sheet is too big for that use); a figure we must defend (a formula; Gemini only labels around it). | Gemini "Translated into an operational team policy"; Claude "Shukla's tiering for decision cells"; Gemini "Second, no auditable financial figures" | rows 1 to 2: 1 brief (Gemini) with 2-brief arithmetic; row 3: 1 (Claude); row 4: 1 (Gemini) |
| 5 | landing (beat), module close | three parallel points that need no explanation | `bullets` | Three lines: what an engineer, a manager and an early-career learner can now do (the module-close block below). | the module-close block; Claude "What a clean sample proves"; Gemini "Translated into an operational team policy" | derived |
| 6 | landing (beat and layout) | the last slide of the module | `landing` | The landing line. | Gemini "record the exact audit summary (rows checked, matches found, and failure pattern)"; Claude "McKelvey's advice" | 1 brief each |

The click: for the columns that matter most, the right amount of checking is every cell, or the column should not be filled by Gemini at all.

MONITOR flags in this segment: none.
Pronunciations needed: Gemini.

## Deferred to the hands-on

- Gemini fills a 20-company list with headquarters and headcount; learners audit five cited cells in a shared saved copy and log each as pass or fail. Claude "Hands-on (Gemini fills 20 companies with headquarters and headcount"; Gemini "Claim 3: 'In the hands-on, you watch Gemini fill".
- The sampling calculator. Gemini "Claim 4: 'Finally, a sampling calculator shows"; the video carries the 41% arithmetic, never the calculator.
- Production blocker for the hands-on, not the video: no source confirms Sources survive Make a copy, paste as values, or a viewer without an eligible plan. Claude "Production notes for the hands-on"; Gemini "A third technical gap directly affects auditability".

## Module close (final segment only)

- Big idea, stated once: A citation tells us where Gemini looked; how much of a column we check is set by what the column will be used for and by the arithmetic of a random sample.
- After this module, a working engineer can: read five clean cells as an error ceiling of 45%, and size a sample to the error rate a column can afford.
- After this module, a non-technical manager can: set a checking tier for each AI-filled column by how it will be used, and ask for the audit note that goes with it.
- After this module, an early-career learner can: check a cited cell by finding the sentence on the page that states the value, and pick the cells to check at random.
- Landing line: When we hand over a filled column, one line goes with it: how many cells we checked at random, how many matched, and what we did about the rest.

## Checks run before presenting this plan

- [x] every segment traces to a shape-sheet signal
- [x] every slide names a brief passage by its first words, not a heading
- [x] segment 1 slide 1 names an experience, not a product
- [x] one `landing` layout, on the module's last slide; every segment closes on a landing beat
- [x] every MONITOR claim on a slide is marked here
- [x] each segment between 3 and 8 minutes at 60 to 150 seconds per slide
- [x] no slide and no narration carries a hands-on; anything hands-on is listed under "Deferred to the hands-on"
