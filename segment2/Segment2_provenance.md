# Provenance: Segment 2, Where Gemini Looked

Module: Every Cell Gets a Receipt. Briefs cited: research-brief-claude, research-brief-gemini, research-brief-openai.
Agreement counts how many briefs carry the claim. Fill the last column during audit.

## Claims by slide

| Slide | Claim | Briefs | Agreement | Source as cited | Contradiction | MONITOR | Human check |
|---|---|---|---|---|---|---|---|
| 1 | Google's announcement presents cell-level citations as a way to audit and verify Gemini-generated data | research-brief-claude, research-brief-gemini | 2 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 |  |  | |
| 1 | A clickable Sources badge can heighten automation bias if reviewers treat the receipt as proof without reading the page | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |
| 1 | A user opens a cell's sources by clicking into the cell, hovering and clicking Sources | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://support.google.com/docs/answer/15877199?hl=en |  |  | |
| 2 | A citation shows where the AI looked; it does not show that the page states the value (paraphrase of Saurabh Shukla, EchoNerve, "A source in a cell shows where the AI looked. It does not show that the page says what the cell says.") | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet 2026-11-04 |  |  | |
| 2 | In Google's developer grounding, the link connects generated text to the pages used for it; documented for the developer tools, not for Sheets | research-brief-claude, research-brief-gemini | 2 | https://ai.google.dev/gemini-api/docs/generate-content/google-search |  |  | |
| 2 | Google's post promises "full visibility to audit, verify, and cross-reference outputs" and does not claim the cited pages are right | research-brief-claude, research-brief-gemini | 2 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 | Google's post frames citations as giving "greater trust and accuracy"; Shukla reads it narrowly, "Its post does not claim the cited pages are right." |  | |
| 2 | The mechanism does not guarantee correctness | research-brief-openai | 1 | not cited in brief |  |  | |
| 3 | The model can misread a table, pull the wrong subsidiary's city, or attach a page that mentions the company without stating the figure | research-brief-gemini, research-brief-claude, research-brief-openai | 3 | https://cs.stanford.edu/~nfliu/papers/liu+zhang+liang.arxiv2023.pdf |  |  | |
| 3 | Search can return an outdated directory or press release after headcount has changed (illustrative) | research-brief-gemini, research-brief-openai | 2 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ |  |  | |
| 3 | A generated value is inserted as an edit; when a prompt joins cells, "you don't get a prompt to refresh the data" | research-brief-claude, research-brief-gemini | 2 | https://support.google.com/docs/answer/15877199?hl=en |  |  | |
| 3 | Two credible pages measuring different scopes (full-time staff in a filing against headcount with contractors) can disagree, and Gemini may cite one | research-brief-gemini, research-brief-openai | 2 | not cited in brief | Claude finds this failure mode "plausible but has no evidence for Sheets"; OpenAI found no source naming it as a separate point. |  | |
| 3 | Google's help page caps a run at the first 350 selected cells; the 28 October 2026 announcement says up to 3,000 cells per request | research-brief-claude, research-brief-gemini | 2 | https://support.google.com/docs/answer/15877199?hl=en 2026-10-28 | Help page "only the first 350 selected cells with AI functions will be generated"; Workspace post "up to 3,000 cells per request" | yes | |
| 4 | Liu, Zhang and Liang (Stanford, EMNLP Findings 2023) found only 74.5% of citations supported their associated sentence, across four generative search engines | research-brief-claude, research-brief-gemini | 2 | https://arxiv.org/abs/2304.09848 2023-04-19 |  |  | |
| 4 | 51.5% of generated sentences were fully supported by citations | research-brief-claude, research-brief-gemini | 2 | https://arxiv.org/abs/2304.09848 |  |  | |
| 4 | No Sheets-specific citation accuracy rate has been published | research-brief-claude, research-brief-gemini | 2 | not cited in brief |  |  | |
| 5 | Liu et al. found citation precision inversely correlated with perceived utility; responses that seem more helpful often carry more unsupported statements or inaccurate citations | research-brief-claude, research-brief-gemini | 2 | https://arxiv.org/pdf/2304.09848v1 2023-04-19 |  |  | |
| 5 | Tow Center (Jaźwińska and Chandrasekar, March 2025) found eight AI search engines "consistently more likely to provide an incorrect answer than to acknowledge limitations"; "unearned confidence" | research-brief-gemini | 1 | https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php 2025-03-06 |  |  | |
| 5 | Ben Dixon (dixon.ai) tested five assistants including the Gemini app; "Every non-passing source answer on the board, 0 hedges." | research-brief-claude | 1 | https://dixon.ai/posts/ai-cites-wrong-source/ 2026-10-22 |  |  | |
| 5 | Dixon's advice, "require the exact page, then find the claim on it" | research-brief-claude | 1 | https://dixon.ai/posts/ai-cites-wrong-source/ |  |  | |
| 5 | Shukla: "It looks checked. I think that look is the risk." (source of the slide title framing) | research-brief-claude | 1 | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet 2026-11-04 |  |  | |

## Single-source claims

- Slide 1: A clickable Sources badge can heighten automation bias if reviewers treat the receipt as proof without reading the page (research-brief-gemini)
- Slide 2: The mechanism does not guarantee correctness (research-brief-openai)
- Slide 5: Tow Center (Jaźwińska and Chandrasekar, March 2025) found eight AI search engines "consistently more likely to provide an incorrect answer than to acknowledge limitations"; "unearned confidence" (research-brief-gemini)
- Slide 5: Ben Dixon (dixon.ai) tested five assistants including the Gemini app; "Every non-passing source answer on the board, 0 hedges." (research-brief-claude)
- Slide 5: Dixon's advice, "require the exact page, then find the claim on it" (research-brief-claude)
- Slide 5: Shukla: "It looks checked. I think that look is the risk." (source of the slide title framing) (research-brief-claude)

## Contradictions and the side taken

- Slide 2: Google's post promises "full visibility to audit, verify, and cross-reference outputs" and does not claim the cited pages are right. Contradiction: Google's post frames citations as giving "greater trust and accuracy"; Shukla reads it narrowly, "Its post does not claim the cited pages are right.". Side taken: Shukla's narrow reading, since the post's wording promises visibility for auditing and contains no claim that cited pages are correct.
- Slide 3: Two credible pages measuring different scopes (full-time staff in a filing against headcount with contractors) can disagree, and Gemini may cite one. Contradiction: Claude finds this failure mode "plausible but has no evidence for Sheets"; OpenAI found no source naming it as a separate point.. Side taken: taught as a failure mode that can happen, with the narration stating plainly that no Sheets case has been documented.
- Slide 3: Google's help page caps a run at the first 350 selected cells; the 28 October 2026 announcement says up to 3,000 cells per request. Contradiction: Help page "only the first 350 selected cells with AI functions will be generated"; Workspace post "up to 3,000 cells per request". Side taken: both figures shown as an example of Google's own pages disagreeing; the caption carries both.

## MONITOR flags

- Slide 3: Google's help page caps a run at the first 350 selected cells; the 28 October 2026 announcement says up to 3,000 cells per request

## Hook and value proposition status

- Hook: partially supported; per-cell web citations and "a citation shows origin, not correctness" are supported by all three briefs, the 30 October date is not (announced 28 October 2026, rollout from 20 October)
- Value proposition: partially supported; the three failure modes taught here are supported (mode 1), partially supported (mode 2) and without a documented Sheets case (mode 3), said plainly
