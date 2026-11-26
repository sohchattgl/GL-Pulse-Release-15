# Module digest: Every Cell Gets a Receipt

Release folder: `Release 15`. The slide blocks are written by `scripts/digest_module.py` from `segment*/segment*.yaml`; cite a slide as segment.slide, such as 2.4.

## Segment 1: A Source in Every Cell

What Google changed in Sheets in October 2026, and how a value filled by Gemini comes to carry the pages behind it.

### 1.1 A Source in Every Cell (`cover`)

- Narration opens: "A list of company facts lands in our shared folder, filled in by AI in a few seconds, and someone has to decide whether it is good enough to send on."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Teams routinely spot-check the first five values of an AI-filled list and sign off on the rest | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |
| Before the October 2026 update, values filled by Fill with Gemini carried no sources and looked like plain text | research-brief-openai, research-brief-gemini, research-brief-claude | https://www.ud.hk/resources/ai/2026-07-10-fill-with-gemini-sheets |  |
| Since late October 2026, each web-sourced value carries the pages Gemini used, inside that cell | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |
| A citation records where Gemini looked, which is different from showing the value is right | research-brief-claude, research-brief-gemini, research-brief-openai | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet |  |

- Contradiction: Claude brief: an undated Google help snippet says the Sources view was "currently available only to users in Workspace Experiments and Beta programs"; Gemini brief: Clay showed per-row sources in a spreadsheet grid since 2023. Side taken: Scoped to general Google Sheets users, for whom neither the April 2026 nor the October 2025 post mentions sources; testers and other products are left out of the narration..

### 1.2 How a filled value got its sources (`timeline`)

- Note: MONITOR: Rollout began on 20 October 2026, in Sheets on the web only and on eligible paid plans. Google's help page still says a run fills only the first 350 selected cells.
- Narration opens: "The receipts arrived at the end of a short history, and each step in it changed what a filled value could tell us."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| The AI function launched on 25 June 2025 and generated only the first 200 selected cells | research-brief-claude, research-brief-gemini | https://workspaceupdates.googleblog.com/2025/06/generate-data-with-gemini-in-google-sheets.html | 2025-06-25 |
| From 15 October 2025 the AI function was grounded in Google Search, and that post never mentions sources | research-brief-claude | https://workspaceupdates.googleblog.com/2025/10/enhanced-ai-function-sheets-google-search.html | 2025-10-15 |
| Fill with Gemini launched on 22 April 2026 as an entry point to the AI function, by drag or by selecting empty cells and clicking Fill | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/04/effortlessly-automate-data-entry-in-Google-Sheets-using-Fill-with-Gemini.html | 2026-04-22 |
| Google announced cell-level web sources on 28 October 2026, rollout from 20 October 2026, Sheets on the web only, eligible plans | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |
| The same update raised a single request to up to 3,000 cells | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |

- Contradiction: The module hook says "On 30 October 2026"; 30 October 2026 is the date of the Google Workspace Weekly Recap that relisted the item. Side taken: 28 October 2026 in narration and on the rail (as October 2026); rollout from 20 October on the MONITOR caption; 30 October not used..
- Contradiction: Google Help: "only the first 350 selected cells with AI functions will be generated" (Claude, Gemini briefs). Side taken: 3,000 as Google's announcement states it, in narration and on the rail; the 350-cell help page goes on the MONITOR caption..

### 1.3 From an empty cell to a cited value (`flow`)

- Narration opens: "Knowing when the receipts arrived, we can build the chain that produces one, a link at a time, because each link is a place where a value can go wrong."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Fill with Gemini is an entry point to the existing AI function, started by dragging or by selecting empty cells | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/04/effortlessly-automate-data-entry-in-Google-Sheets-using-Fill-with-Gemini.html |  |
| The function does not have access to the entire spreadsheet or other Drive files; it sees the prompt and the range it is pointed at | research-brief-claude, research-brief-gemini, research-brief-openai | https://support.google.com/docs/answer/15877199?hl=en |  |
| For factual questions the function is grounded in Google Search results | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2025/10/enhanced-ai-function-sheets-google-search.html |  |
| The pages used are attached to each cell and opened by clicking into the cell, hovering and clicking Sources | research-brief-claude, research-brief-gemini, research-brief-openai | https://support.google.com/docs/answer/15877199?hl=en |  |
| A generated value is inserted as an edit and does not refresh; prompts built by joining cells give no refresh prompt | research-brief-claude, research-brief-gemini | https://support.google.com/docs/answer/15877199?hl=en |  |
| A company's headcount can change after the fill while the cited page or value stays as it was (illustrative) | research-brief-gemini, research-brief-openai |  |  |

### 1.4 One value cheaper, one run bigger (`two_number`)

- Takeaway: Each value got cheaper to check, and each run got fifteen times bigger.
- Note: MONITOR: Google's help page still says a run fills only the first 350 selected cells. The 55 times speed figure comes from Google's own study of a 500-cell task.
- Narration opens: "The same announcement that made one value cheap to check also made each run much bigger, and those two changes pull in opposite directions."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| At launch in June 2025 the AI function generated only the first 200 selected cells | research-brief-claude, research-brief-gemini | https://workspaceupdates.googleblog.com/2025/06/generate-data-with-gemini-in-google-sheets.html | 2025-06-25 |
| Up to 3,000 cells per request from October 2026, fifteen times the 200-cell launch cap (computed) | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |
| Up to 55 times faster than manual entry for 500-cell tasks, from a 95-participant internal Google study | research-brief-claude, research-brief-gemini, research-brief-openai | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |
| Checking one cited cell takes under a minute (Jose S., Analytics Made Simple) | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| 3,000 values at just under a minute each is close to fifty hours (computed from the under-a-minute figure) | research-brief-gemini |  |  |
| Saurabh Shukla, EchoNerve newsletter, exact: "Nobody opens 3,000 sources."; paraphrase of "It looks checked. I think that look is the risk." | research-brief-claude | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet | 2026-11-04 |

- Contradiction: Google Help: "only the first 350 selected cells with AI functions will be generated"; McKelvey: "Google doesn't say." Side taken: 3,000 as Google's announcement states it; the 350-cell help page is on the MONITOR caption, never spoken..

## Segment 2: Where Gemini Looked

What a cell's citation proves in Fill with Gemini, and the three ways a cited value can still be wrong.

### 2.1 Where Gemini Looked (`cover`)

- Narration opens: "We left off with a long list of filled values, and every one of them now arrives with its pages attached."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Google's announcement presents cell-level citations as a way to audit and verify Gemini-generated data | research-brief-claude, research-brief-gemini | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |
| A clickable Sources badge can heighten automation bias if reviewers treat the receipt as proof without reading the page | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| A user opens a cell's sources by clicking into the cell, hovering and clicking Sources | research-brief-claude, research-brief-gemini, research-brief-openai | https://support.google.com/docs/answer/15877199?hl=en |  |

### 2.2 What a citation records (`two_card`)

- Takeaway: A citation tells us where Gemini looked, and reading the page tells us whether it is right.
- Narration opens: "Behind every filled value sits a short chain of events, and the citation comes from one link in that chain."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| A citation shows where the AI looked; it does not show that the page states the value (paraphrase of Saurabh Shukla, EchoNerve, "A source in a cell shows where the AI looked. It does not show that the page says what the cell says.") | research-brief-claude, research-brief-gemini, research-brief-openai | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet | 2026-11-04 |
| In Google's developer grounding, the link connects generated text to the pages used for it; documented for the developer tools, not for Sheets | research-brief-claude, research-brief-gemini | https://ai.google.dev/gemini-api/docs/generate-content/google-search |  |
| Google's post promises "full visibility to audit, verify, and cross-reference outputs" and does not claim the cited pages are right | research-brief-claude, research-brief-gemini | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-10-28 |
| The mechanism does not guarantee correctness | research-brief-openai |  |  |

- Contradiction: Google's post frames citations as giving "greater trust and accuracy"; Shukla reads it narrowly, "Its post does not claim the cited pages are right." Side taken: Shukla's narrow reading, since the post's wording promises visibility for auditing and contains no claim that cited pages are correct.

### 2.3 Three ways a cited cell is wrong (`numbered_list`)

- Note: MONITOR: Google's help page caps a run at the first 350 selected cells; its announcement of 28 October 2026 says up to 3,000 cells per request.
- Narration opens: "The chain behind a filled value has three places where it can go wrong, and each one leaves a perfectly normal citation behind."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| The model can misread a table, pull the wrong subsidiary's city, or attach a page that mentions the company without stating the figure | research-brief-gemini, research-brief-claude, research-brief-openai | https://cs.stanford.edu/~nfliu/papers/liu+zhang+liang.arxiv2023.pdf |  |
| Search can return an outdated directory or press release after headcount has changed (illustrative) | research-brief-gemini, research-brief-openai | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ |  |
| A generated value is inserted as an edit; when a prompt joins cells, "you don't get a prompt to refresh the data" | research-brief-claude, research-brief-gemini | https://support.google.com/docs/answer/15877199?hl=en |  |
| Two credible pages measuring different scopes (full-time staff in a filing against headcount with contractors) can disagree, and Gemini may cite one | research-brief-gemini, research-brief-openai |  |  |
| Google's help page caps a run at the first 350 selected cells; the 28 October 2026 announcement says up to 3,000 cells per request | research-brief-claude, research-brief-gemini | https://support.google.com/docs/answer/15877199?hl=en | 2026-10-28 |

- Contradiction: Claude finds this failure mode "plausible but has no evidence for Sheets"; OpenAI found no source naming it as a separate point. Side taken: taught as a failure mode that can happen, with the narration stating plainly that no Sheets case has been documented.
- Contradiction: Help page "only the first 350 selected cells with AI functions will be generated"; Workspace post "up to 3,000 cells per request" Side taken: both figures shown as an example of Google's own pages disagreeing; the caption carries both.

### 2.4 How often a citation holds (`stat_hero`)

- Note: Measured in 2023 on other AI search products. No published figure exists yet for Gemini in Google Sheets.
- Narration opens: "How often that first failure happens is something researchers at Stanford set out to measure."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Liu, Zhang and Liang (Stanford, EMNLP Findings 2023) found only 74.5% of citations supported their associated sentence, across four generative search engines | research-brief-claude, research-brief-gemini | https://arxiv.org/abs/2304.09848 | 2023-04-19 |
| 51.5% of generated sentences were fully supported by citations | research-brief-claude, research-brief-gemini | https://arxiv.org/abs/2304.09848 |  |
| No Sheets-specific citation accuracy rate has been published | research-brief-claude, research-brief-gemini |  |  |

### 2.5 Why wrong cells look checked (`three_column`)

- Takeaway: When a cell passes, we copy in the sentence from the page that states its value.
- Narration opens: "There's a pattern across the studies of cited answers, and it runs against our instincts."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Liu et al. found citation precision inversely correlated with perceived utility; responses that seem more helpful often carry more unsupported statements or inaccurate citations | research-brief-claude, research-brief-gemini | https://arxiv.org/pdf/2304.09848v1 | 2023-04-19 |
| Tow Center (Jaźwińska and Chandrasekar, March 2025) found eight AI search engines "consistently more likely to provide an incorrect answer than to acknowledge limitations"; "unearned confidence" | research-brief-gemini | https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php | 2025-03-06 |
| Ben Dixon (dixon.ai) tested five assistants including the Gemini app; "Every non-passing source answer on the board, 0 hedges." | research-brief-claude | https://dixon.ai/posts/ai-cites-wrong-source/ | 2026-10-22 |
| Dixon's advice, "require the exact page, then find the claim on it" | research-brief-claude | https://dixon.ai/posts/ai-cites-wrong-source/ |  |
| Shukla: "It looks checked. I think that look is the risk." (source of the slide title framing) | research-brief-claude | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet | 2026-11-04 |

## Segment 3: Five Clean Cells

What a small clean sample of cited cells shows, and what a sample large enough to sign off on costs in time.

### 3.1 Five Clean Cells (`cover`)

- Narration opens: "With thousands of values in a sheet, most teams settle the question the same way, and it feels responsible while we do it."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Teams routinely spot-check the first five rows of a column, see five matches and sign off on the rest | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |

### 3.2 Which five cells we open (`two_card`)

- Takeaway: A random draw costs a few clicks and gives every company the same chance of a check.
- Narration opens: "The convenient five are usually the first five, and the start of a list is rarely a fair picture of what comes after it."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Checking only the first five or ten rows is a classic error, because the start of a curated list holds larger, better-documented companies | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| A random sample is drawn by giving every row a random number, freezing it, sorting by it and checking the first rows | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |

### 3.3 How often five cells catch it (`stat_hero`)

- Note: On a 20-row list with two wrong values, the same check finds an error about 45% of the time.
- Narration opens: "Suppose one cell in ten across the whole list is wrong, and we open five at random."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| If one cell in ten is wrong, a five-cell random check catches at least one error 41% of the time (1 minus 0.9 to the fifth, 40.95%) | research-brief-claude, research-brief-gemini, research-brief-openai | https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm | 2026-11-25 |
| Five clean draws in a row happen about six times in ten (0.9 to the fifth, 59.05%) | research-brief-claude, research-brief-gemini |  |  |
| On a 20-row list with two wrong values, a five-cell check catches an error about 45% of the time (44.7%) | research-brief-claude, research-brief-gemini | https://www.itl.nist.gov/div898/handbook/glossary.htm | 2026-11-25 |

### 3.4 What a clean result rules out (`two_number`)

- Note: Each figure is the highest error rate that still gives a clean result at least one time in twenty.
- Narration opens: "Let's turn the question around, because the one a manager asks after a clean result is how bad the list could still be."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Five clean random checks still allow an error rate up to 45% (exact bound 45.07%, 1 minus 0.05 to the power one fifth) | research-brief-claude, research-brief-gemini |  |  |
| Ten clean checks leave a ceiling near 26% (exact bound 25.89%) | research-brief-gemini |  |  |
| Quote, exact: "Ten clean checks still leave room for up to about one wrong cell in three." Jose S., Analytics Made Simple, spoken as a tutorial writer who teaches spreadsheet analysis | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| Twenty clean checks leave a ceiling of about 14% (exact bound 13.91%) | research-brief-gemini |  |  |
| Thirty clean checks bring the ceiling under 10% (exact bound 9.50%; Shukla's rule of thumb gives about 10%) | research-brief-claude, research-brief-gemini | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet | 2026-11-25 |

- Contradiction: The rule of three (3 divided by n) gives 60% at five clean checks. Side taken: the exact bound of 45% on the slide and in narration; the rule of three is too rough at five cells.
- Contradiction: Jose S. (Analytics Made Simple) states "Ten clean checks still leave room for up to about one wrong cell in three", the rule-of-three figure of 30%. Side taken: quoted his line as his rule of thumb and stated the exact figure, about one in four, beside it.

### 3.5 What each extra cell buys (`table`)

- Takeaway: Thirty random cells take about half an hour and bring the ceiling on errors under 10%.
- Narration opens: "Every cited cell we open takes under a minute to read against its page, so a bigger sample costs us minutes and buys a better chance of catching a problem."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Five random cells catch a one-in-ten error rate 41% of the time | research-brief-claude, research-brief-gemini, research-brief-openai |  |  |
| Ten random cells catch a one-in-ten error rate 65% of the time (65.1%), computed from the formula in research-brief-claude and research-brief-gemini | research-brief-claude, research-brief-gemini |  |  |
| Twenty random cells catch a one-in-ten error rate 88% of the time (87.8%), computed from the formula in research-brief-claude and research-brief-gemini | research-brief-claude, research-brief-gemini |  |  |
| Thirty random cells catch a one-in-ten error rate 96% of the time (95.8%), computed from the formula in research-brief-claude and research-brief-gemini | research-brief-claude, research-brief-gemini |  |  |
| Twenty-nine random cells give a 95% chance of catching a one-in-ten error rate | research-brief-claude, research-brief-gemini |  |  |
| Checking one cited cell takes under a minute, so thirty cells take roughly half an hour (the brief gives 20 to 30 minutes) | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| Five cells serve as a prompt smoke test; sign-off on a large column needs at least 30 random cells | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |

## Segment 4: How Much to Check

Turns the sampling arithmetic into a four-step checking routine and a checking tier for each column by its use, then closes the module.

### 4.1 How Much to Check (`cover`)

- Narration opens: "Half an hour of checking is easy to agree to in principle, and harder when someone is waiting on the answer."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Treating a visible source as proof can push unverified numbers into pricing, supplier or headcount decisions | research-brief-gemini | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 2026-11-25 |
| Managers need a clear sampling rule and an audit note attached to every AI-filled deliverable | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |

### 4.2 A routine for one filled column (`flow`)

- Note: No vendor names these four steps; they gather what careful practitioners already do.
- Narration opens: "The routine we need can be built from the ways a single value goes wrong, one failure at a time."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| The four-step routine (read, sample, cross-check, sign off) is the module's own framework, not a named external standard | research-brief-claude, research-brief-gemini, research-brief-openai |  |  |
| Ben Dixon's advice to "require the exact page, then find the claim on it" (spoken by role, paraphrase of exact quote) | research-brief-claude | https://dixon.ai/posts/ai-cites-wrong-source/ | 2026-11-25 |
| Checking only the top rows is biased because larger firms are better documented | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |
| A source can be out of date, or two credible sources can measure different scopes (full-time staff against headcount with contractors) | research-brief-gemini, research-brief-openai |  |  |
| Gary Stanton (AIAdoptionTrends) on using cell citations as a route to the evidence, then checking each decision-changing fact (paraphrase; spoken by role) | research-brief-openai |  |  |
| Jose S.'s routine of opening each sampled cell's Sources and recording pass or fail, with a sign-off note | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |

- Contradiction: Claude: 'This failure mode is plausible but has no evidence for Sheets'; OpenAI: 'We did not find a source stating out of date or disagree as separate points.' Side taken: taught as a failure mode in plain terms with an illustrative example, as the reconciliation directs; no Sheets case is claimed.

### 4.3 One list, thirty random checks (`stat_hero`)

- Note: Jose S., who writes the Analytics Made Simple tutorials, published this worked example in November 2026.
- Narration opens: "That routine has been run end to end, in public, by a tutorial writer who teaches spreadsheet analysis."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Jose S. (Analytics Made Simple) filled a 200-supplier headquarters list, froze it as values, drew 30 random rows with a random-number column, and 29 matched | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| Audit note "30 random rows checked against sources, 29 matched; directory-sourced rows checked individually" (exact) | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| Checking one cited cell takes under a minute | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-10 |
| Several more wrong values in the unchecked rows if the one-in-thirty miss rate held (derived from 1/30 of 200) | research-brief-gemini |  |  |

### 4.4 How much each column needs (`table`)

- Takeaway: For the columns that matter most, we check every cell or Gemini does not fill them.
- Note: The two highest-stakes tiers follow Saurabh Shukla, who writes the EchoNerve newsletter, and the UD Technology Team at UDomain.
- Narration opens: "With that routine in hand, the remaining decision is how much of it each list deserves, and the answer rises with what the list will be used for."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Five cells serve as a prompt smoke test before spending usage quotas | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |
| Five clean random cells still allow an error rate up to 45% (95% upper bound) | research-brief-claude, research-brief-gemini |  |  |
| Thirty clean random cells bring the error ceiling under 10%, about 20 to 30 minutes of work | research-brief-claude, research-brief-gemini | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet | 2026-11-04 |
| Saurabh Shukla (EchoNerve) on decision cells, "open every source. If that is too many cells, the sheet is too big for that use." (exact; spoken by role) | research-brief-claude | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet | 2026-11-04 |
| UD Technology Team (UDomain), "Do not use it for figures you must defend. A generated number has no formula trail." and "use Gemini only to draft or label around them" (paraphrase in narration) | research-brief-gemini | https://www.ud.hk/resources/ai/2026-07-10-fill-with-gemini-sheets | 2026-07-10 |

### 4.5 What we can now do (`bullets`)

- Narration opens: "Everything we've worked through fits into a single sentence, and it's worth saying once."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Five clean random cells leave an error ceiling of 45%; thirty clean cells bring it under 10% | research-brief-claude, research-brief-gemini |  |  |
| Checking tiers set by how a column is used, with an audit note | research-brief-claude, research-brief-gemini |  |  |
| Random selection with a random-number column; checking top rows is biased | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |

### 4.6 One thing to keep (`landing`)

- Narration opens: "The habit that carries all of this is a small one."

| Claim | Briefs | Source | Date |
|---|---|---|---|
| Record the exact audit summary (rows checked, matches found, failure pattern) alongside the deliverable | research-brief-gemini | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ | 2026-11-25 |
| Justin McKelvey's advice to add a "last generated" date column so stale answers are easy to spot | research-brief-claude | https://justinmckelvey.com/blog/gemini-in-google-sheets | 2026-11-07 |

<!-- Everything below this line is written by hand and kept when digest_module.py runs again. -->

## Subject profile

A feature inside a product: Fill with Gemini in Google Sheets on the web, which fills selected empty cells through the AI function and, since late October 2026, attaches the web pages it used to each cell. Analysts, coordinators and managers use it to enrich lists (companies, suppliers, venues, countries) with facts they would otherwise look up one at a time. It replaces manual lookup and copy-paste, and it changes the checking job: each value is now checkable, and a run is large enough that nobody checks all of it. `demo` and `build` fit first, since the subject is a feature used as it is; `probe` fits the video's caveats about clean-looking wrong cells and small samples; `swap` fits the manual lookup step it replaces; `compare` fits two ways of asking for the same column.

## Ingredients

Ideas the video taught that a viewer could watch operating. One row each, citing the slide that taught it.

| ID | Slide | The idea | Where it operates in a real job |
|---|---|---|---|
| I1 | 1.3 | Fill with Gemini fills selected empty cells, and the function reads only the prompt and the row it is pointed at | Setting up the fill on a list: which columns the prompt points at decides what Gemini can use to tell two similar names apart |
| I2 | 1.3 | The pages used are attached to each cell and opened by clicking into the cell, hovering and clicking Sources | Every check in an audit starts here, one cell at a time |
| I3 | 1.3 | A filled value is inserted as an edit and does not refresh when the web changes | Dating a filled column, and deciding when it needs filling again |
| I4 | 1.4 | Each value got cheaper to check and each run got much bigger, so we count the cells before trusting a column | Sizing a column before deciding how much of it to check |
| I5 | 2.2 | A citation records where Gemini looked; whether the page states the value is a separate question | The pass or fail decision on each checked cell: read the page for the value |
| I6 | 2.3 | Failure one: the page does not say it (misread table, wrong subsidiary, the page names the company without the figure) | Sorting a failed check by its cause |
| I7 | 2.3 | Failure two: the page is out of date, and the cell never refreshes | Reading the date on a cited page against when the value is needed |
| I8 | 2.3 | Failure three: credible pages disagree, for example full-time staff in a filing against headcount with contractors | Deciding which measure a column holds, and writing it in the header |
| I9 | 2.5 | When a cell passes, copy in the sentence from the page that states the value | An evidence column beside each checked cell |
| I10 | 2.5 | Wrong cells carry the same confident text and the same tidy citation as right ones | Watching a planted wrong value look exactly like the rest of the column |
| I11 | 3.2 | Check a random draw: give every row a random number, freeze it, sort by it, check the first rows; the top of a list is biased toward well-documented companies | Choosing which cells to open |
| I12 | 3.3 | If one cell in ten is wrong, five random cells catch at least one error 41% of the time; about 45% on a 20-row list with two wrong | Deciding whether a five-cell check is worth reporting as a check |
| I13 | 3.4 | A clean sample sets a ceiling: five clean cells still allow up to 45% wrong, ten about 26%, twenty about 14%, thirty under 10% | Writing what a clean result rules out in the audit note |
| I14 | 3.5 | One cited cell takes under a minute to check; thirty take about half an hour; five is a smoke test for the prompt | Budgeting the check, and testing a prompt before the full fill |
| I15 | 4.2 | A four-step routine: read the citation, check a random sample, cross-check a second source, sign off with a note; a failed sample sends that kind of row to a full check | The order of work after any fill |
| I16 | 4.3 | A failure pattern in the sample (directory-sourced rows) earns its own check of every row like it | Acting on a failed cell beyond fixing that one cell |
| I17 | 4.4 | Checking tiers by use: a first look gets five cells; a working list gets thirty; a figure that changes a decision gets every source; a figure we must defend gets a formula, with Gemini only labelling around it | Assigning a tier to each column before checking |
| I18 | 4.6 | Hand over a filled column with one line: how many cells checked at random, how many matched, and what we did about the rest; a "last generated" date helps spot stale answers | The note that travels with the deliverable |

## Caveats

Limits the video stated. One row each. Every card names the caveat that could bite its job.

| ID | Slide | The limit | Where it could bite |
|---|---|---|---|
| C1 | 2.2 | A citation does not show the value is right, and Google's post does not claim the cited pages are right | Any case that reads a Sources view as a pass |
| C2 | 2.3 | All three failures leave a normal-looking citation behind, and the third (pages disagree) has no documented Sheets case | A planted row whose cited page is real and still wrong for the column |
| C3 | 2.4 | The 74.5% citation figure comes from other products in 2023; no figure exists for Gemini in Sheets | Any line tempted to predict how many cells will fail |
| C4 | 2.5 | Wrong values carry no hedge; nothing in a wrong cell looks different | A reviewer scanning the column for odd-looking values |
| C5 | 1.3 | A filled value does not refresh when the web changes | A list reused weeks later, or a headcount that changed after the fill |
| C6 | 1.2 | Web only, eligible plans, rollout from 20 October 2026; Google's help page still says 350 cells against 3,000 in the announcement (MONITOR) | The recording account, and any fill larger than 350 cells |
| C7 | 3.4 | A small clean sample is weak evidence: five clean cells allow an error rate up to 45% | Signing off on a column after a handful of matches |
| C8 | 4.4 | A figure we must defend has no formula trail when Gemini fills it, so it should not be filled | A column of rates or prices that goes into a calculation |
| C9 | 3.2 | The top rows of a curated list pass more often, so checking them tells us least about the rest | A list sorted by size or by how well known the names are |

## Can-dos

From the plan's module close, quoted.

1. Working engineer: "read five clean cells as an error ceiling of 45%, and size a sample to the error rate a column can afford."
2. Non-technical manager: "set a checking tier for each AI-filled column by how it will be used, and ask for the audit note that goes with it."
3. Early-career learner: "check a cited cell by finding the sentence on the page that states the value, and pick the cells to check at random."

## Deferred

From the plan's "Deferred to the hands-on", quoted.

> - Gemini fills a 20-company list with headquarters and headcount; learners audit five cited cells in a shared saved copy and log each as pass or fail.
> - The sampling calculator. The video carries the 41% arithmetic, never the calculator.
> - Production blocker for the hands-on, not the video: no source confirms Sources survive Make a copy, paste as values, or a viewer without an eligible plan.

Note for the cards: a web-sourced fill needs public pages, so the lists filled in these cases name public organisations, venues or countries. Everything else (the company doing the job, its people, its notes, its keys, its old files) is invented.

## Extra evidence

Exact quotes from the briefs, only for claims a card makes that the video did not. `check_ideas.py` verifies each against the brief it names.

| ID | Practitioner and role | Exact quote | Brief | Passage opens | Source and date |
|---|---|---|---|---|---|
| E1 | Bradshaw, Online Journalism Blog | "copy and paste the results as values only as soon as the formulae have run" | research-brief-claude.md | Bradshaw's warning implies | https://onlinejournalismblog.com/2025/04/10/google-sheets-has-a-new-ai-function-how-does-it-perform-on-classification-tasks/, accessed 2026-11-25 |
