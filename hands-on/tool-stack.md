# Tool stack: Every Cell Gets a Receipt

Release folder: `Release 15`. Digest: `hands-on/module-digest.md`. Written to `references/tool-stack.md`.

## Subject

The models, products, techniques or risks this release is about, and the alternatives the video names. Never a comparison tool.

| Subject | What it is | Named in |
|---|---|---|
| Fill with Gemini | The Sheets entry point that fills selected empty cells with the AI function and, since October 2026, attaches the web pages it used to each cell | slide 1.3 |
| AI function | The formula Fill with Gemini writes into each cell, grounded in Google Search for factual questions; it can be typed by hand | slide 1.2 |

The video names no competing product on a slide. Clay appears only in a contradiction note on 1.1 and is not a route here.

## Surfaces

Kind: `vendor-ui`, `no-code`, `hosted-demo`, `local` or `comparison`. Access: `open`, `waitlist`, `paused` or `unknown`. Capabilities: short lower-case words separated by commas.

| Surface | Runs | Route | Kind | Access | Account and cost | Capabilities | Shows | URL | Checked |
|---|---|---|---|---|---|---|---|---|---|
| Google Sheets on the web, Fill with Gemini | Fill with Gemini, AI function | Signed-in Google account with Gemini in Sheets enabled | vendor-ui | open | An eligible plan: Workspace Business Standard or Plus, Enterprise Standard or Plus, Google AI Pro or Ultra, Google AI Pro for Education, or the AI Expanded Access add-on. Google AI Pro is listed at $19.99 a month; Workspace offers a 14-day trial, and which trial tier includes Gemini in Sheets is not settled by the pricing page | fill, prompt, sources view, open page, random draw, freeze values, sort, filter, formula, note, new tab | The filled value in each cell, and the pages behind it when the cell is clicked, hovered and Sources is opened | https://workspaceupdates.googleblog.com/2026/10/fill-with-gemini-now-provides-cell-level-citations-for-web-sources-and-supports-larger-requests.html | 26 November 2026 |
| Google Sheets on the web, AI function typed in a cell | AI function, Fill with Gemini | The same account; the formula typed into a cell and filled down by hand | vendor-ui | open | The same eligible plan | prompt, fill, sources view, open page, random draw, freeze values, sort, filter, formula, note, new tab | The same value and Sources view; the prompt is visible in the formula bar | https://support.google.com/docs/answer/15877199?hl=en | 26 November 2026 |
| Google AI Studio with Grounding with Google Search | Gemini models grounded in Google Search, outside Sheets | Google account, AI Studio playground | comparison | open | A free Google account; grounding is free to test in AI Studio per Google's October 2024 post (not re-verified) | playground run, grounded answer, sources list | Answer text with the search queries and source links listed beside it | https://ai.google.dev/gemini-api/docs/generate-content/google-search | 26 November 2026 |
| Google Search in a browser | Nothing of the subject; the manual lookup the fill replaces | Any browser | comparison | open | No account | web search, open page, copy, paste | Search results and the pages themselves | https://www.google.com | 26 November 2026 |

## Notes from the check

- Google Sheets on the web, Fill with Gemini: web only; rollout began 20 October 2026 with up to 15 days to appear (MONITOR). Google's help page still says only the first 350 selected cells are generated, against 3,000 in the announcement, so every case keeps its fill under 350 cells. The Sources view opens by clicking into the cell, hovering and clicking Sources; the exact label is `[confirm label]` until the build sees it.
- No retrieved source says whether Sources survive Make a copy or paste as values, or show to a viewer without an eligible plan (MONITOR). Every case fills live on camera and opens Sources before any freeze, so the capture never depends on that.
- Google Sheets on the web, AI function typed in a cell: the fallback when the Fill with Gemini entry point is missing or renamed; values typed this way are the same function and carry the same Sources.
- Make, n8n, Zapier and Activepieces reach the Gemini model through a key and write text into a sheet; none shows cell Sources, so none runs the subject and none is listed.
- No local route exists; the Sheets feature is cloud-only.
- Gate 0: the user kept Google Sheets on the web, Fill with Gemini, and dropped the other three rows, which stay listed for the record and are used by no card. Every card therefore runs on one surface with no fallback surface; when it is down, the recording waits (`references/tool-stack.md`, "When a surface goes down"). A swap card's before step is the team's old manual step on our own file, and a compare card's two routes are two prompts on the same surface.

## Confirmed

Confirmed at gate 0 on 26 November 2026: Google Sheets on the web, Fill with Gemini.
