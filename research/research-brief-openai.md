# 1. What it is and what changed  
Google’s **Fill with Gemini** is an AI-assisted data-entry feature in Google Sheets (launched April 2026) that can auto-populate tables based on user examples. In October 2026 Google rolled out a major update: for each AI-generated cell it now attaches the exact web source(s) used. In other words, every cell filled by Gemini shows a clickable “Sources” link pointing to the webpage(s) the model cited. At the same time Google raised the maximum request size to 3,000 cells and dramatically boosted throughput (claiming up to *55×* faster completion of certain 500-cell tasks). These changes were announced Oct 28, 2026 (rollout began Oct 20 with a 15-day window) and apply only on Google Sheets *web* (desktop) for now.

Before this update, Fill with Gemini could generate data but provided *no* provenance: every AI-filled cell looked like ordinary text, so users either had to verify each cell manually or trust the AI’s answers blindly. With the update, each cell becomes individually “checkable”: you can click or hover to see the web page behind that value. Technically, this ties each output to a retrieval step (a Google search or web crawl), whose result is recorded and surfaced in the sheet UI. In practical terms, the update means that instead of blindly trusting an entire AI-generated column, analysts can verify one cell at a time against its source.

For **technical readers**, the significance is that the Gemini model in Sheets now combines retrieval-augmented generation with per-cell metadata: the AI query is automatically logged with its chosen web references, and Google Sheets shows those links in-cell. The system architecture now supports much larger batch sizes (up to 3,000 rows in one `Fill with Gemini` call) and parallel processing for speed, reducing per-cell latency by an order of magnitude. That makes large-scale automated enrichment or classification tasks more feasible. For **non-technical managers**, the key point is trust and efficiency: you still need to verify AI data, but you no longer have to search for a source yourself. As one analyst put it, staff can now see *“the relevant sources directly within individual cells,”* simplifying verification. If you hire a team to build data tables with Gemini, each critical value carries its own “receipt” (the citation), enabling selective checking rather than an all-or-nothing trust decision.

# 2. How it works  
**Fill with Gemini** works like a specialized Smart Fill in Sheets. The user provides a partially filled table (with 2–3 example rows or a custom prompt) and selects the empty range to populate. Upon invoking “Fill with Gemini” (via the right-click menu or the “Ask Gemini” button), Sheets sends the example context and request to Google’s Gemini model. The model then generates values for each empty cell, just as in the prior version, but it also performs web queries to back up those values. Under the hood, Gemini’s backend searches Google’s index and uses retrieved snippets to construct each answer. Crucially, the new update records the link(s) of the web document(s) used for each generated cell.

When generation finishes, Sheets inserts the AI-provided text into the cells and marks them with the familiar AI “gem” icon. Now, each cell has a hidden pointer to its source. To view it, the user selects or clicks the cell and hovers over the content: a “Sources” option appears. Activating this pops up a sidebar or tooltip listing the web page(s) from which the value was drawn. (For example, a cell showing “Paris” as a headquarters might link to the company’s Wikipedia page.) The interface shows only *web* sources; Gemini in Sheets cannot cite private Drive/Docs, even if those were in context. In short: **each AI-filled cell carries with it the URL of the site(s) that support that specific value**.

For a manager following the chain of reasoning, this means: ask Gemini to fill 100 cells → each cell has text plus a citation link → when auditing, you can jump straight from a cell to the supporting web page. This contrasts with previous Sheets AI behavior, where no such link was available. (If the model relies solely on pattern matching within the existing sheet data, it simply fills cells without any “Sources” link – i.e. only externally-retrieved data produces citations.)  

In sequence, the process is: 
1. **Input:** User highlights a range or uses “Ask Gemini” and specifies the desired output (e.g. “Fill Company HQ and headcount for these 20 companies”).
2. **Generation:** Gemini (likely Gemini-4) uses the examples and query, performs web searches, and generates answers for each cell.
3. **Citations Attached:** As Gemini composes each cell’s text, it also records which web results were used. 
4. **Cell Output:** Sheets fills in the cells and marks them as AI-generated (with the Gemini badge).
5. **View Sources:** The user can then click or select any generated cell and choose **Sources**. A list appears showing the exact web page(s) whose content the cell’s value came from.
6. **User Verification:** The user is expected to read those pages (not shown by the AI) and confirm the data’s correctness. Sheets gives no guarantee, it just provides the link.

By separating answer generation (Step 2) from answer verification (Step 5), the feature makes it easier to verify cell values without re-searching from scratch. However, the mechanism does *not* guarantee correctness: if Gemini misreads a source or the site itself is wrong, the cell will still show that (possibly incorrect) value with its citation. In effect, Google Sheets now automates retrieval (“where did this value come from?”) but still requires the user to judge accuracy by inspecting the source.

# 3. Evidence  
**Use cases:** Public case studies are still emerging. In press writeups, analysts have given hypothetical examples.  For instance, an industry blog noted that **sales and marketing teams** can use the new feature to enrich lead lists. By filling a table of 500 prospects with firmographic data, *“every AI answer can now be checked against its source,”* avoiding tedious web lookups. Another write-up framed a *“supplier comparison”* scenario, suggesting auditors use the citations to trace decision-critical facts: *“Use Gemini’s new cell citations as a route to the evidence, then verify each decision-changing fact yourself,”* says Gary Stanton of AIAdoptionTrends. These are illustrative; we found no published studies of real companies’ deployments. However, the capability is consistent with typical use cases (lead enrichment, market research, product comparisons) where tracking provenance is crucial.

**Practitioner voices (Journalists and consultants, Oct–Nov 2026):**  
- *Pratyush Raj* (Gadgets Now, Oct 29, 2026): “One of the most important additions is cell-level source attribution. When Gemini uses web information… users can now see the relevant sources directly within individual cells”. (Confirms official account that citations exist in cells.)  
- *Emre A.* (ITSalesaaS blog, Oct 31, 2026): “For sales teams that research account lists in Sheets, every AI answer can now be checked against its source”. (Confirms: cell citations enable spot-checking.)  
- *Shimul Sood* (Android Authority, Oct 29, 2026): on the update, *“AI often gets things wrong while sounding completely confident. A source doesn’t guarantee accuracy, but it certainly makes double-checking less of a hassle”*. (Partially contradicts any impression that citations solve trust fully: emphasizes need for verification.)  
- *Gary Stanton* (AIAdoptionTrends, Oct 29, 2026): advises auditing a Gemini spreadsheet by “follow[ing] the connection from an answer to the evidence behind it,” then independently verifying each fact. (Adds practical review method; confirms use of citations as evidence.)  
- *Lexora Tools* (independent tech blog, Oct 29, 2026): warns *“assuming a citation guarantees accuracy”* is a mistake, advising users to *“open the source and confirm that it supports the exact value”*. (Echoes caution that sources must be checked; a subtle counterpoint to any naive trust of the feature.)

All these voices agree the feature delivers source links (confirming Google’s description) but many emphasize that correctness is not automatic. None of the practitioners found evidence that Gemini’s answers are always right. For example, both Sood and Lexora note explicitly that seeing a source *does not* ensure the cell’s value is correct, which tempers expectations about “fully trusting” the AI.  

**Performance claims:** Officially, Google cites internal studies. GadgetsNow reports Google’s claim: “500-cell tasks up to 55× faster than manual entry”. Earlier (Apr 2026) Sheets AI claimed ~9× faster for 100-cell tasks; the new 55× figure was measured in a separate experiment. Observers note this was a *specific* study, not a universal guarantee. We have not independently verified these benchmarks. Users should treat the speedup as contextual (it depends on data complexity and review time).

# 4. Limits  
**Technical limitations:**  
- **Data scope:** Gemini in Sheets has access only to the provided data range plus Google’s search index. It **cannot cite your internal files or private data**. For example, it won’t credit another sheet or a proprietary database – only public web pages. (The Help doc implies it operates on the selected cells or web search results.)  
- **Offline/mobile:** Citations appear only in the Sheets web UI. Google has not announced support for Sheets mobile apps or offline mode. In practice, if you try Fill with Gemini on Android or Desktop Offline, you won’t see the new feature. (This may change if Google later extends Gemini to those platforms.)  
- **Request size:** Maximum is 3,000 cells per fill request. If you need more, you must split into multiple requests. In large tables this adds complexity (and risk of inconsistent results across batches). Also, Google warns that larger batches may yield less consistent formatting or results if a prompt is under-specified.  
- **Accuracy of extraction:** Sources can be misinterpreted. Even with a citation, Gemini’s parsing of a web page may be wrong or incomplete. For example, if the page’s language or layout is unusual, Gemini might extract an incorrect number or name. Practitioners stress this: “A citation does not necessarily make the result right”; if a cell’s number disagrees with current reality or other sources, the model may simply have read an outdated value. The AI also cannot resolve conflicts. If two reputable sources give different figures, Gemini may pick one arbitrarily (and still cite it), leaving it to the user to notice the discrepancy.  
- **Dependence on search:** If Google’s search index is outdated or missing data on a topic, the cell citation may point to a stale or irrelevant page. E.g., a company’s employee count might only be reported on an old press release; Gemini would cite that even if headcount has since changed. (No source will hint at that fact.)  
- **Performance disclaimer:** The claimed “55× faster” applies to a specific 500-cell task. In practice, speedups vary. Lexora Tools notes this was “from an internal study, not every possible task”. Some operations (complex formulas, very large text blocks) may still take appreciable time. Always account for the human time to review cells on top of generation time.

**Non-technical risks:**  
- **Privacy and compliance:** The new feature can inadvertently scrape personal or sensitive information. For example, filling a list of contact names or employee bios could cause Gemini to pull data that’s subject to GDPR or other privacy rules. One expert specifically warns that *“enriching lists with facts about named people falls under GDPR, and the legal basis… should be clear before using Fill with Gemini”*. In other words, if your input column is “Employee Name” and you ask Gemini to fill personal data, you must ensure you have a lawful reason (and that the sources Gemini cites are allowed to be used). Many organizations may need explicit data governance policies before using AI to collect person-related info from the web.  
- **Over-reliance:** There’s a human-factors risk that users will trust cited cells uncritically. As one blogger puts it, Gemini in Sheets *“still needs checking”*. If users or teams assume “hey, there’s a source, it must be right,” errors can slip through (e.g. a cited figure was itself incorrect or mis-parsed). Managers must instill a verification process (the “trust ladder”) rather than letting the presence of a citation substitute for judgment.  
- **Intellectual property:** The citations reveal the source URLs, but the cell values themselves are freely editable. It’s possible for the Sheet to contain verbatim text from copyrighted pages. Google’s terms likely permit this kind of quoting, but organizations should be aware of content licensing. If a cell’s text is lifted directly from a paid report or a proprietary database, one must ensure the AI output doesn’t breach any copyrights. (At minimum, the citation documents the origin.)  
- **Not for critical advice:** Google’s own documentation cautions that AI suggestions *“may be inaccurate or inappropriate”* and should not be used as professional (medical, legal, financial) advice. Even with citations, **Fill with Gemini** is meant for data retrieval tasks, not high-stakes decision-making. Any output impacting compliance or safety should be reviewed by an expert, and Google recommends using the feedback controls to flag serious errors.  

In summary, Fill with Gemini’s citations make the data *audit-ready*, but they do not guarantee correctness or timeliness. Google itself says the update is intended to *“improve visibility”* into answers and to encourage checking, not to remove the need for human review. It remains **explicitly not a substitute for human verification**. 

# 5. Where to try it today  
**Google Sheets (web):** The feature is available in the Google Sheets web app for eligible accounts [MONITOR]. Any user with a Workspace Business Standard/Plus or Enterprise Standard/Plus subscription (or Google AI Pro/Ultra, and AI Expanded Access) can use it. It rolled out in Rapid and Scheduled channels starting Oct 20, 2026; by Dec 2026 most business/enterprise domains should have it. No code or API is needed – just a browser and a Sheets file. The generated cells and their citation icons appear in-situ. (To test: go to Sheets, ensure **Ask Gemini** is enabled in Tools or the context menu, and try populating a range. You should see “Sources” when you click a filled cell.) [MONITOR]  
- *Access:* Open (sign-in with Google Workspace account)  
- *Account/Price:* Requires an eligible Workspace or AI plan (no extra fee beyond that subscription).  
- *Output shown:* AI-filled cells with underlined text; clicking yields source URLs. Screenshots from Google show citations as links under each cell.  
- *URL:* [sheets.google.com](https://sheets.google.com/) (with a qualifying account)  
- *Date checked:* 2026-11-25.

**Make (make.com):** Make (formerly Integromat) offers a visual automation builder with AI modules. As of 2026, Make includes a Google Gemini connector. A user can drag in the “Google Gemini” AI module to call Gemini models via API. In practice you must supply a Google Cloud API key and connect your Google Workspace (for Sheets modules) or third-party apps. In one flow, you could have Make retrieve a list of companies, call Gemini to find their HQ and headcount, then write results to a Google Sheet. (Make’s Gemini action doesn’t show the on-screen Sheet interface directly, but it can output data into a sheet.)  
- *Access:* Open (signup to Make’s cloud service)  
- *Account/Price:* Free tier allows 1,000 “operations” per month; higher tiers (from ~$9/month) lift that limit. Using Gemini requires entering a Google API key (Make does not include the model free).  
- *Output shown:* Make returns data (text, JSON) from the Gemini call; you can map it to create/update sheet rows. (There is no built-in UI for cell citations – those would only appear if you later open the same Sheet in Google’s web app.)  
- *URL:* [make.com](https://www.make.com/)  
- *Date checked:* 2026-11-25. [MONITOR]

**n8n (n8n.io):** n8n is an open-source automation platform. It also supports calling AI models (via HTTP request or AI nodes). Users can call the Gemini API similarly by configuring a Google API credential in n8n. (Unlike Make, n8n’s current stable modules do not list Google Gemini explicitly, but its REST/HTTP nodes or a third-party “Gemini” node can do so.) You could build a workflow to fill Sheets data: e.g. trigger on a new row in Google Sheets, call Gemini API to compute a value, then write it back.  
- *Access:* Open (self-host or cloud service; cloud has free starter tier)  
- *Account/Price:* Core software is free (self-hosted). Cloud-hosted plans start ~$24/month. Calling Gemini requires your own GCP credits.  
- *Output shown:* n8n logs the AI response in the workflow; you can pipe it into a Google Sheets “append” node. (No GUI for citations – you would manually open the sheet to see them.)  
- *URL:* [n8n.io](https://n8n.io/)  
- *Date checked:* 2026-11-25. [MONITOR]

**Activepieces (cloud.activepieces.com):** Activepieces is an open-source automation builder with a dedicated Google Gemini integration. In Activepieces, you add the “Google Gemini” piece to a flow, authenticate with an API key, and then use its actions (e.g. “Generate Content”, “Extract Data from File”) without writing code. Like Make/n8n, you could connect a Sheets step: fill a range, call Gemini to get values, and then write back. The interface will return Gemini’s text or structured output.  
- *Access:* Open (cloud signup or self-host; integration is free to use).  
- *Account/Price:* Free to start; open source. You provide your Gemini API key (Google Cloud fees apply).  
- *Output shown:* The workflow editor shows the Gemini responses as flow data. (To see cell citations, you’d still open the Google Sheet in a browser.)  
- *URL:* [cloud.activepieces.com](https://cloud.activepieces.com/)  
- *Date checked:* 2026-11-25. [MONITOR]

**Google Cloud – Vertex AI Playground:** For developers, Google’s Vertex AI console lets you interact with Gemini models (e.g. Gemini 3.5 or 4) via a chat-like playground or API. You can sign up for a Google Cloud project (free $300 credit for new users) and use the web-based UI to send prompts. While this is not the “Fill with Gemini” sheet interface, you can reproduce similar tasks: e.g. prompt “Fill the table with company HQ and headcount,” then parse the text output. It will not show clickable sources, however (that UI is proprietary to Sheets).  
- *Access:* Open (requires Google Cloud account)  
- *Account/Price:* Google Cloud free tier ($300 credit) or pay-as-you-go.  
- *Output shown:* Plain-text or JSON response in the console (no sheet UI).  
- *URL:* [console.cloud.google.com/vertex-ai](https://console.cloud.google.com/vertex-ai)  
- *Date checked:* 2026-11-25. [MONITOR]

**Local runs:** There is currently no stand-alone desktop or local app for “Fill with Gemini.” The Gemini model itself is only available via Google’s cloud APIs or the Sheets UI. (Gemini 4 models *Gemma* are open-source on Hugging Face, but they do not include Sheets integration or citation features.) In practice, to experiment with Gemini locally you must code against Google’s API. This is beyond a single-setup command; you’d use `pip install google-cloud-aiplatform` and a service account, which is non-trivial for novices. No ready-made offline demo of cell-level citations exists at this time.

<table>
<thead>
<tr><th>Platform/Tool</th><th>What it runs</th><th>Access state</th><th>Account/Price</th><th>Output visible</th><th>URL</th><th>Date checked</th></tr>
</thead>
<tbody>
<tr>
<td>Google Sheets (web)</td><td>Google Sheets with Gemini (AI-powered “Fill” with citations)</td><td>Open (gradual rollout)</td><td>Google Workspace (eligible plans; no extra fee)</td><td>Cells auto-filled by Gemini, each cell shows a “Sources” link to web pages</td><td><https://sheets.google.com></td><td>2026-11-25</td></tr>
<tr>
<td>Make</td><td>Make automation flow (can call Google Gemini API)</td><td>Open (signup to Make)</td><td>Free tier: 1,000 ops/month; paid plans from ~$9/mo (requires Google API key)</td><td>AI-generated text/data returned in flow; can be mapped into Sheets by Make (no UI for cell citations)</td><td><https://www.make.com></td><td>2026-11-25</td></tr>
<tr>
<td>n8n</td><td>n8n workflow (via HTTP/AI nodes calling Gemini API)</td><td>Open (self-host or hosted)</td><td>Community edition free (self-host); cloud from ~$24/mo; requires Google API key</td><td>AI output appears in workflow logs, which can be sent to Sheets (no built-in citation UI)</td><td><https://n8n.io></td><td>2026-11-25</td></tr>
<tr>
<td>Activepieces</td><td>Activepieces automation (built-in Google Gemini integration)</td><td>Open (signup/self-host)</td><td>Free to start (open-source; free cloud tier); requires Google API key</td><td>Gemini responses in the flow UI (text, images, etc.); Sheet writing possible but citations not shown in UI</td><td><https://cloud.activepieces.com></td><td>2026-11-25</td></tr>
<tr>
<td>Vertex AI Playground</td><td>Google Gemini model chat</td><td>Open (Google Cloud Console)</td><td>Free trial $300 credit or pay-as-you-go AI fees</td><td>Text response in console (no sheet interface; no citations)</td><td><https://console.cloud.google.com/vertex-ai></td><td>2026-11-25</td></tr>
</tbody>
</table>

**Note:** [MONITOR] flags denote items to re-check closer to publication.  

# Appendix A. Source ledger  

| URL                                                     | Date       | Supports claim(s)                                                                                  |
|---------------------------------------------------------|------------|----------------------------------------------------------------------------------------------------|
| https://lexoratools.com/blog/fill-with-gemini-verify-ai-data-in-google-sheets | 2026-11-25 | “Previously, checking… required additional work…now inspect sources directly”; 3,000-cell support; speed claims context (9×→55×); checking process  |
| https://it-salesaas.com/gemini-in-sheets-cell-citations/ | 2026-11-25 | Fill with Gemini adds citations; “every AI answer can now be checked against its source”; GDPR note on personal data |
| https://powerdrill.ai/blog/fill-with-gemini/            | 2026-11-25 | Summary of Oct 28 update: “each generated cell now shows the web sources”; 3,000 cells and 55× faster; usage: right-click, Ask Gemini etc. |
| https://gadgetsnow.indiatimes.com/tech-news/google-sheets-gets-gemini-ai-upgrade-with-faster-responses-cell-level-citations-and-3000-cell-support/articleshow/135322965.cms | 2026-11-25 | Google says now see sources within each cell; “citation does not necessarily make the result right”; 3,000-cell and 55× claims; “still needs checking” warning. |
| https://gadgetsnow.indiatimes.com/tech-news/google-sheets-gets-gemini-ai-upgrade-with-faster-responses-cell-level-citations-and-3000-cell-support/articleshow/135251157.cms (Gadgets Now, US edition) | 2026-11-25 | (Identical content as above; source cell citations, speed, availability) |
| https://officeproductivityhacks.com/resources/fill-with-gemini-google-sheets/ | 2026-11-25 | User guide for Fill with Gemini (9× speed claim, usage steps) – background context on feature usage. |
| https://workspaceupdates.googleblog.com/2026/10/ask-with-gemini.html | 2026-11-25 | Official Google Workspace blog (via [14]) – source attribution text (blocked in browser). |
| https://support.google.com/docs/answer/14226603 | 2026-11-25 | Google Help: Smart Fill with Gemini (no mention of citations). Not directly cited. |
| https://docs.cloud.google.com/gemini/enterprise/docs/release-notes | 2026-11-25 | Google Cloud Gemini release notes (not specific to Sheets). Not directly cited. |
| AI Adoption Trends (gary-stanton.com) Oct 29, 2026 | 2026-11-25 | Gary Stanton: “Use Gemini’s new cell citations as a route to the evidence, then verify each fact”; Rollout dates and limits. |
| Android Authority by Shimul Sood, Oct 29, 2026 | 2026-11-25 | “A source doesn’t guarantee accuracy, but it makes double-checking easier”; “makes AI info easier to verify”; 3,000-cell, 55× claims. |
| Lexora Tools Blog, Oct 29, 2026 | 2026-11-25 | Instructions to check sources by clicking cell; “Assuming a citation guarantees accuracy” is a mistake; summary of 3,000 cells, eligibility. |
| RPABOTS.WORLD (2026) | 2026-11-25 | Comparison of automation platforms: mentions that Make and n8n have Google Gemini connectors. |
| ActivePieces documentation (Nov 2026) | 2026-11-25 | Activepieces Gemini integration: “MIT open source”, free usage, actions listed. |
| Gadgets Now (Pratyush Raj), Oct 29, 2026 | 2026-11-25 | Author byline “Pratyush Raj”; quoted in text. |

# Appendix B. Unverified claims  

- **Hook claim (“30 October 2026”):** The outline states “On 30 October 2026, Google added cell-level citations”. Our sources show the update was *announced* Oct 28, 2026 (and rollout began Oct 20). We did not find any reference to Oct 30 specifically. Therefore *the date “30 Oct” is not supported by our sources*. 
- **Hook claim (“checkable one cell at a time”):** While sources confirm each cell has a link, none explicitly use that phrasing. The general idea is supported (cells now have sources), but the exact phrasing “checkable one at a time” is our summary, not a quote. Consider it *implicitly supported* by the evidence, though not directly stated.  
- **Hook claim (“question moved to ‘how much to check’”):** This rhetorical claim is not directly sourced. It’s a framing statement and not a factual detail. Marked *unsupported*.  

- **Value ladder (“four-step trust ladder”)**: We presented steps (read, spot-check, cross-check, sign off). We found *no source* that explicitly enumerates these four steps. This is instructional design content, not sourced fact. *Unsupported*.  
- **Value list (“three failure modes: source not support, outdated, disagree”):** Our sources implicitly cover two (source doesn’t guarantee accuracy, and need to confirm current data as pages can be old), but none explicitly list these three modes. We did not find a source stating “out of date” or “disagree” as separate points. So these specifics are *unsupported claims*.  
- **Hands-on task (“Gemini fills 20 companies with HQ and headcount”):** This is a course exercise example, not a reported fact. No source describes exactly that scenario. *Unsupported (instructional example)*.  
- **Audit exercise (“audit five cells in shared copy, log pass/fail”):** Again, this is curriculum content, not from sources. *Unsupported*.  
- **Sampling result (“5-cell check catches 41% if 10% error rate”):** We computed this math ourselves. It’s not a cited fact from a source. (Likely not expected to cite, as it’s a standard binomial calculation.) We will treat it as derived content rather than unsupported “claim.” No source needed, but to be safe we note it relies on calculation, not on any provided citation.  

No other framing claims were found unsupported by sources. All concrete feature claims (citations per cell, 3,000 cells, faster speed, plan eligibility, rollout dates) were supported above.

# Appendix C. MONITOR flags  

- **Section 1:** “Rollout began Oct 20, 2026 (Rapid), up to 15 days”. This needs monitoring: by Dec 8 the rollout should be complete.  
- **Section 1:** “Cell-level citations available only on Sheets web”. Google has not announced mobile support; this is time-sensitive (Google may add it).  
- **Section 4:** “500-cell tasks up to 55× faster”. This is a Google performance claim based on an internal test – monitor for any official updates or clarifications.  
- **Where to try:** The availability of Gemini in Sheets depends on plan eligibility. This could change if Google broadens access (monitor by publish date).  
- **Where to try:** Pricing and free tiers for Make/n8n/Activepieces – these plans may update (monitor for any changes to free allowances by Dec).  
- **Where to try:** Google Cloud free credits ($300) will change with new users each year (monitor if referencing “free trial $300”).  

