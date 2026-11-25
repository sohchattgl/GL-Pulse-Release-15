# Provenance: Segment 1, A Source in Every Cell

Module: Every Cell Gets a Receipt. Briefs cited: research-brief-claude, research-brief-gemini, research-brief-openai.
Agreement counts how many briefs carry the claim. Fill the last column during audit.

## Claims by slide

| Slide | Claim | Briefs | Agreement | Source as cited | Contradiction | MONITOR | Human check |
|---|---|---|---|---|---|---|---|
| 1 | Teams routinely spot-check the first five values of an AI-filled list and sign off on the rest | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-25 |  |  | |
| 1 | Before the October 2026 update, values filled by Fill with Gemini carried no sources and looked like plain text | research-brief-openai, research-brief-gemini, research-brief-claude | 3 | https://www.ud.hk/resources/ai/2026-07-10-fill-with-gemini-sheets | Claude brief: an undated Google help snippet says the Sources view was "currently available only to users in Workspace Experiments and Beta programs"; Gemini brief: Clay showed per-row sources in a spreadsheet grid since 2023. |  | |
| 1 | Since late October 2026, each web-sourced value carries the pages Gemini used, inside that cell | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 |  |  | |
| 1 | A citation records where Gemini looked, which is different from showing the value is right | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet |  |  | |
| 2 | The AI function launched on 25 June 2025 and generated only the first 200 selected cells | research-brief-claude, research-brief-gemini | 2 | https://workspaceupdates.googleblog.com/2025/06/generate-data-with-gemini-in-google-sheets.html 2025-06-25 |  |  | |
| 2 | From 15 October 2025 the AI function was grounded in Google Search, and that post never mentions sources | research-brief-claude | 1 | https://workspaceupdates.googleblog.com/2025/10/enhanced-ai-function-sheets-google-search.html 2025-10-15 |  |  | |
| 2 | Fill with Gemini launched on 22 April 2026 as an entry point to the AI function, by drag or by selecting empty cells and clicking Fill | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/04/effortlessly-automate-data-entry-in-Google-Sheets-using-Fill-with-Gemini.html 2026-04-22 |  |  | |
| 2 | Google announced cell-level web sources on 28 October 2026, rollout from 20 October 2026, Sheets on the web only, eligible plans | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 | The module hook says "On 30 October 2026"; 30 October 2026 is the date of the Google Workspace Weekly Recap that relisted the item. | yes | |
| 2 | The same update raised a single request to up to 3,000 cells | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 | Google Help: "only the first 350 selected cells with AI functions will be generated" (Claude, Gemini briefs). | yes | |
| 3 | Fill with Gemini is an entry point to the existing AI function, started by dragging or by selecting empty cells | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/04/effortlessly-automate-data-entry-in-Google-Sheets-using-Fill-with-Gemini.html |  |  | |
| 3 | The function does not have access to the entire spreadsheet or other Drive files; it sees the prompt and the range it is pointed at | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://support.google.com/docs/answer/15877199?hl=en |  |  | |
| 3 | For factual questions the function is grounded in Google Search results | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2025/10/enhanced-ai-function-sheets-google-search.html |  |  | |
| 3 | The pages used are attached to each cell and opened by clicking into the cell, hovering and clicking Sources | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://support.google.com/docs/answer/15877199?hl=en |  |  | |
| 3 | A generated value is inserted as an edit and does not refresh; prompts built by joining cells give no refresh prompt | research-brief-claude, research-brief-gemini | 2 | https://support.google.com/docs/answer/15877199?hl=en |  |  | |
| 3 | A company's headcount can change after the fill while the cited page or value stays as it was (illustrative) | research-brief-gemini, research-brief-openai | 2 | not cited in brief |  |  | |
| 4 | At launch in June 2025 the AI function generated only the first 200 selected cells | research-brief-claude, research-brief-gemini | 2 | https://workspaceupdates.googleblog.com/2025/06/generate-data-with-gemini-in-google-sheets.html 2025-06-25 |  |  | |
| 4 | Up to 3,000 cells per request from October 2026, fifteen times the 200-cell launch cap (computed) | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 | Google Help: "only the first 350 selected cells with AI functions will be generated"; McKelvey: "Google doesn't say." | yes | |
| 4 | Up to 55 times faster than manual entry for 500-cell tasks, from a 95-participant internal Google study | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html 2026-10-28 |  | yes | |
| 4 | Checking one cited cell takes under a minute (Jose S., Analytics Made Simple) | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |
| 4 | 3,000 values at just under a minute each is close to fifty hours (computed from the under-a-minute figure) | research-brief-gemini | 1 | not cited in brief |  |  | |
| 4 | Saurabh Shukla, EchoNerve newsletter, exact: "Nobody opens 3,000 sources."; paraphrase of "It looks checked. I think that look is the risk." | research-brief-claude | 1 | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet 2026-11-04 |  |  | |

## Single-source claims

- Slide 1: Teams routinely spot-check the first five values of an AI-filled list and sign off on the rest (research-brief-gemini)
- Slide 2: From 15 October 2025 the AI function was grounded in Google Search, and that post never mentions sources (research-brief-claude)
- Slide 4: Checking one cited cell takes under a minute (Jose S., Analytics Made Simple) (research-brief-gemini)
- Slide 4: 3,000 values at just under a minute each is close to fifty hours (computed from the under-a-minute figure) (research-brief-gemini)
- Slide 4: Saurabh Shukla, EchoNerve newsletter, exact: "Nobody opens 3,000 sources."; paraphrase of "It looks checked. I think that look is the risk." (research-brief-claude)

## Contradictions and the side taken

- Slide 1: Before the October 2026 update, values filled by Fill with Gemini carried no sources and looked like plain text. Contradiction: Claude brief: an undated Google help snippet says the Sources view was "currently available only to users in Workspace Experiments and Beta programs"; Gemini brief: Clay showed per-row sources in a spreadsheet grid since 2023.. Side taken: Scoped to general Google Sheets users, for whom neither the April 2026 nor the October 2025 post mentions sources; testers and other products are left out of the narration..
- Slide 2: Google announced cell-level web sources on 28 October 2026, rollout from 20 October 2026, Sheets on the web only, eligible plans. Contradiction: The module hook says "On 30 October 2026"; 30 October 2026 is the date of the Google Workspace Weekly Recap that relisted the item.. Side taken: 28 October 2026 in narration and on the rail (as October 2026); rollout from 20 October on the MONITOR caption; 30 October not used..
- Slide 2: The same update raised a single request to up to 3,000 cells. Contradiction: Google Help: "only the first 350 selected cells with AI functions will be generated" (Claude, Gemini briefs).. Side taken: 3,000 as Google's announcement states it, in narration and on the rail; the 350-cell help page goes on the MONITOR caption..
- Slide 4: Up to 3,000 cells per request from October 2026, fifteen times the 200-cell launch cap (computed). Contradiction: Google Help: "only the first 350 selected cells with AI functions will be generated"; McKelvey: "Google doesn't say.". Side taken: 3,000 as Google's announcement states it; the 350-cell help page is on the MONITOR caption, never spoken..

## MONITOR flags

- Slide 2: Google announced cell-level web sources on 28 October 2026, rollout from 20 October 2026, Sheets on the web only, eligible plans
- Slide 2: The same update raised a single request to up to 3,000 cells
- Slide 4: Up to 3,000 cells per request from October 2026, fifteen times the 200-cell launch cap (computed)
- Slide 4: Up to 55 times faster than manual entry for 500-cell tasks, from a 95-participant internal Google study

## Hook and value proposition status

- Hook: partially supported; per-cell web sources in Fill with Gemini and "a citation shows origin, not correctness" are in all three briefs; the hook's 30 October date is wrong (announced 28 October 2026, rollout from 20 October), so the narration says late October.
- Value proposition: partially supported; the 41 percent sampling figure is computed in all three briefs, the four-step ladder is the module's own framework, and the hands-on's reliance on Sources surviving a shared copy is unverified (not used in this segment).
