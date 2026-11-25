# Reconciliation: Every Cell Gets a Receipt

Briefs: `research/research-brief-claude.md` (Claude), `research/research-brief-gemini.md` (Gemini), `research/research-brief-openai.md` (OpenAI). Passages are cited by their first words. The Gemini brief is one unbroken block of text; its passages are cited the same way.

## 1. Claims in every brief

| Claim | Where each brief states it |
|---|---|
| Google added per-cell web source citations to Fill with Gemini in Sheets, announced on 28 October 2026, with gradual rollout from 20 October 2026 (up to 15 days). | Claude "On 28 October 2026, Google's Workspace team published"; Gemini "On October 28, 2026, Google published its official"; OpenAI "These changes were announced Oct 28, 2026" |
| Citations appear in Google Sheets on the web only. | Claude "Sources 'are available in Google Sheets on the web'"; Gemini "Cell-level web citations are restricted exclusively"; OpenAI "Citations appear only in the Sheets web UI" |
| The same update raised a request to up to 3,000 cells. | Claude "expanded capacity supporting up to 3,000 cells"; Gemini "Oct 28, 2026 Workspace Updates post: up to 3,000 cells"; OpenAI "raised the maximum request size to 3,000 cells" |
| Google claims "up to 55 times faster than manual entry for 500 cell tasks"; the April 2026 claim was 9x on 100-cell tasks. Both from internal studies. | Claude "Speed claims. '9x faster … 100-cell tasks'"; Gemini "Oct 28, 2026 release note reports up to 55 times"; OpenAI "Earlier (Apr 2026) Sheets AI claimed ~9× faster" |
| Fill with Gemini launched in April 2026 as an entry point to the AI function. | Claude "On 22 April 2026, Google introduced Fill with Gemini"; Gemini "On April 22, 2026 (Rapid Release) and May 6, 2026"; OpenAI "launched April 2026" |
| A user opens a cell's sources by clicking the cell, hovering, and clicking Sources. | Claude "The reader opens them by clicking into the cell"; Gemini "clicking the filled cell, hovering over the content"; OpenAI "the user selects or clicks the cell and hovers" |
| The function sees only the prompt, the range it is pointed at, and Google Search; it cannot read the whole spreadsheet or private files. | Claude "It 'doesn't have access to your entire spreadsheet'"; Gemini "At this first link in the chain, scope isolation is strict"; OpenAI "Gemini in Sheets has access only to the provided data range" |
| A citation shows where the value came from; it does not show the value is right. | Claude "A source in a cell shows where the AI looked"; Gemini "A source shows where Gemini found the answer"; OpenAI "the mechanism does *not* guarantee correctness" |
| Google's own help page warns against relying on Gemini as professional advice and says it "may suggest inaccurate" information. | Claude "Google: 'Don't rely on Gemini features as medical'"; Gemini "First, no professional advice"; OpenAI "Google's own documentation cautions that AI suggestions" |
| A five-cell random check catches a one-in-ten error rate about 41% of the time (1 − 0.9⁵ = 0.4095). | Claude "When p = 0.1, the chance that a 5-cell sample"; Gemini "Plugging in p = 0.10 and n = 5"; OpenAI "Sampling result ('5-cell check catches 41%" |
| The eligible plans: Business Standard and Plus, Enterprise Standard and Plus, Google AI Pro and Ultra, AI Expanded Access. | Claude "The post lists availability for Business Standard"; Gemini "Same Workspace Business Standard"; OpenAI "Any user with a Workspace Business Standard/Plus" |
| 30 October 2026 is not the launch date. | Claude "So 30 October is a recap date"; Gemini "Two days later, on October 30, 2026"; OpenAI "We did not find any reference to Oct 30" |
| The "four-step trust ladder" is not a named external framework. | Claude "'Four-step trust ladder' (read, spot-check"; Gemini "SUPPORTED as an original pedagogical framework"; OpenAI "We found *no source* that explicitly enumerates" |

## 2. Claims in two briefs

| Claim | Briefs | Missing from | Passage |
|---|---|---|---|
| The AI function launched 25 June 2025 with a cap of the first 200 selected cells. | Claude, Gemini | OpenAI | Claude "Google introduced the AI function"; Gemini "Google first introduced the =AI() function" |
| Google's help page still caps a run at the first 350 selected cells. | Claude, Gemini | OpenAI | Claude "Google Help: 'only the first 350 selected cells'"; Gemini "First, batch size" |
| Liu, Zhang and Liang (Stanford, 2023): 74.5% of citations supported their sentence; 51.5% of sentences were fully supported, across four generative search engines. | Claude, Gemini | OpenAI | Claude "a mere 51.5% of generated sentences"; Gemini "Auditing four commercial generative search engines" |
| The answers rated most helpful carried more unsupported citations (Claude: inverse correlation; Gemini: 4.48/5 fluency and 4.50/5 utility against 51.5%). | Claude, Gemini | OpenAI | Claude "Liu et al. found 'citation precision is inversely correlated"; Gemini "The researchers also documented a sharp gap" |
| Five clean random checks still allow a true error rate up to 45.1% at 95% confidence; about 30 clean checks bring the ceiling to about 10%. | Claude, Gemini | OpenAI | Claude "What a clean sample proves"; Gemini "Second, consider the zero-error upper bound" |
| On a short list sampled without replacement, the five-cell catch rate is 44.7% (20 cells, 2 wrong) or 42.7% (40 cells, 4 wrong). | Claude, Gemini | OpenAI | Claude "Correction for a short list"; Gemini "On the module's smaller 20-company hands-on list" |
| 29 random cells give a 95% chance of catching a one-in-ten error rate. | Claude, Gemini | OpenAI | Claude "Sample size needed for a 95% chance"; Gemini "reaching 95% detection requires 29 cells" |
| A generated value is inserted as an edit and does not refresh; prompts built by joining cells give no refresh prompt at all. | Claude, Gemini | OpenAI | Claude "Step 6: The value is frozen"; Gemini "What happens after a value lands in the grid" |
| Grounding links a piece of generated text to the sources used for it (groundingSupports); the link records use, not that the page states the value. Documented for the API, not for Sheets. | Claude, Gemini | OpenAI | Claude "Step 5: How a grounded answer is linked"; Gemini "Third, Gemini synthesizes the cell's short text answer" |
| Limits: text only, no nesting inside other functions, no undo, blocked on Box, Dropbox and Egnyte, 24-hour lockout at the long-term limit. | Claude, Gemini | OpenAI | Claude "Technical limitation 1"; Gemini "A second category of technical limitations" |
| A source can be out of date: an old directory or press release still cited after headcount changed. | Gemini, OpenAI (both illustrative) | Claude (has Google's no-refresh rule and Dixon's stale figure instead) | Gemini "At the web-search stage, Google Search can return an outdated"; OpenAI "Dependence on search" |
| Two credible sources can disagree, and the model may pick one and still cite it. | Gemini, OpenAI | Claude (finds no Sheets case) | Gemini "pull two credible sources that measure different scopes"; OpenAI "The AI also cannot resolve conflicts" |
| Android Authority: "A source doesn't guarantee accuracy, but it certainly makes double-checking less of a hassle." | Claude (author unconfirmed), OpenAI (Shimul Sood, 29 Oct 2026) | Gemini | Claude "Android Authority, 'Gemini in Google Sheets is getting faster"; OpenAI "Shimul Sood (Android Authority" |
| Business Standard $14 per user a month on an annual plan; Google AI Pro $19.99 a month. | Claude, Gemini | OpenAI | Claude "Business Standard is $14 per user"; Gemini "Same Workspace Business Standard ($14" |

## 3. Claims in one brief

| Claim | Brief | Passage |
|---|---|---|
| Google Search grounding for the AI function began 15 October 2025, and that post never mentions sources or citations. | Claude | "From 15 October 2025, Google began" |
| Saurabh Shukla (EchoNerve newsletter, 4 Nov 2026): "Nobody opens 3,000 sources. That is the problem."; "It looks checked. I think that look is the risk."; for decision cells, "open every source. If that is too many cells, the sheet is too big for that use." | Claude | "Step 7: Why citations create a sampling problem"; "Practitioner voices" table; "Shukla's tiering for decision cells" |
| Ben Dixon (dixon.ai): six UK factual questions to five assistants; Gemini app "3 held, 2 slipped"; "Every non-passing source answer on the board: 0 hedges."; advice to "require the exact page, then find the claim on it". Not the Sheets surface. | Claude | "Ben Dixon (dixon.ai) | Six UK factual questions"; "Every non-passing source answer" |
| Justin McKelvey (7 Nov 2026): Google's pages disagree on 350 or 3,000; advice to add a "last generated" date column. | Claude | "Google's own pages disagree on how many cells"; "McKelvey's advice" |
| Paul Bradshaw (Apr 2025): results disappear on sort, filter or rename; row context influences output; paste results as values. | Claude | "Paul Bradshaw, Birmingham City University" |
| A Workspace Experiments help snippet documents a per-cell Sources view for Experiments and Beta users before general rollout (undated). | Claude | "A Google help page titled 'Use the AI function in Google Sheets (Workspace Experiments)'" |
| Jose S. (Analytics Made Simple, 10 Nov 2026): a 200-supplier headquarters list, 30 random rows sampled with a random-number column, audit note "30 random rows checked against sources, 29 matched; directory-sourced rows checked individually"; one cited cell checks in under a minute; checking the top rows is biased because larger firms are better documented; "Ten clean checks still leave room for up to about one wrong cell in three." | Gemini | "Jose S. (Analytics Made Simple)"; "Checking only the first five or ten rows"; "Ten clean checks still leave room" |
| Five cells serve as a prompt smoke test; sign-off on a large column needs at least 30 random cells, about 20 to 30 minutes. | Gemini | "Translated into an operational team policy" |
| UD Technology Team (10 Jul 2026): "Do not use it for figures you must defend. A generated number has no formula trail." | Gemini | "Second, no auditable financial figures" |
| Tow Center (Jaźwińska and Chandrasekar, Mar 2025): eight AI search engines "consistently more likely to provide an incorrect answer than to acknowledge limitations"; "unearned confidence". | Gemini | "Klaudia Jaźwińska and Aisvarya Chandrasekar" |
| Clay's Claygent has shown per-row web sources in a spreadsheet grid since 2023. | Gemini | "Outside mainstream office suites, however" |
| Microsoft retired Excel's COPILOT function on 14 September 2026. | Gemini | "In the surrounding competitive landscape" |
| Gemini API forum threads document grounding metadata going missing (April 2026) and invented URLs when grounding is combined with structured output. | Gemini | "At the API layer powering Gemini's grounding" |
| Apps Script cannot refresh the AI function (Mr Shane, Google Product Expert). | Gemini | "Mr Shane (Google Docs Editors Community" |
| Spatharioti et al. (CHI 2025): overreliance leads users to accept the first answer from LLM search. | Gemini | "In a randomized experiment published at CHI '25" |
| Filling lists with facts about named people raises GDPR questions. | OpenAI | "Privacy and compliance" |
| Gary Stanton (AIAdoptionTrends): "Use Gemini's new cell citations as a route to the evidence, then verify each decision-changing fact yourself." | OpenAI | "Another write-up framed a 'supplier comparison'" |
| Prompts that use only sheet text (classification) trigger no web search and carry no citation. | Gemini (OpenAI implies it) | Gemini "When a prompt operates purely on internal spreadsheet text"; OpenAI "If the model relies solely on pattern matching" |

Not carried: OpenAI's "likely Gemini-4", the "gem icon" and "underlined text" descriptions, and the Paris/Wikipedia example are unsourced illustrations.

## 4. Contradictions

1. **Cells per run.** Claude: Help page "only the first 350 selected cells with AI functions will be generated"; Workspace post "expanded capacity supporting up to 3,000 cells per request"; 2025 launch "only the first 200 selected cells". Gemini: "Help Center still specifies 350 selected cells per =AI() multi-cell run". McKelvey (Claude): "Google doesn't say." OpenAI states 3,000 only.
2. **Launch date.** Workspace post dated 28 October 2026; rollout "started on October 20, 2026"; weekly recap 30 October 2026; module hook "On 30 October 2026". All three briefs reject 30 October.
3. **Were sources visible before?** Claude: Experiments help snippet, "currently available only to users in Workspace Experiments and Beta programs" (undated). Gemini: before 20 October values "landed in the grid as opaque plain text", and Clay showed per-row sources since 2023. OpenAI: before the update Fill with Gemini "provided *no* provenance".
4. **What a citation proves.** Google post: "full visibility to audit, verify, and cross-reference outputs for greater trust and accuracy." Shukla (Claude): "Its post does not claim the cited pages are right." Jose S. (Gemini): "it does not show the answer is right."
5. **Accuracy on one Google page.** "To automatically generate accurate and timely answers" against "Gemini features may suggest inaccurate or inappropriate information" (Claude, Gemini).
6. **Third failure mode, credible sources disagree.** Claude: "plausible but has no evidence for Sheets". OpenAI: "We did not find a source stating 'out of date' or 'disagree' as separate points." Gemini: "SUPPORTED", with an illustrative scope example (full-time staff against headcount with contractors).
7. **Rule of three against the exact bound.** At five clean checks, 3/n gives 60% and the exact bound gives 45.07% (Gemini). At 30 clean checks both give about 10% (Claude, Gemini).
8. **Live formulas against frozen values.** Google Help stresses Refresh and Insert; Jose S. and FreakyJolly (Gemini) and Bradshaw (Claude) say paste as values at once.

Side taken for slides: 28 October 2026 as the announcement date, with rollout from 20 October; 3,000 cells per request as Google's announcement states it, with the 350-cell help page on the MONITOR caption; sources were absent for general Sheets users before October; disagreement between credible sources taught as a failure mode with no documented Sheets case, said plainly.

## 5. MONITOR flags

| Claim | Briefs flagging it |
|---|---|
| Rollout from 20 October 2026, up to 15 days | Claude, Gemini, OpenAI |
| Sources on Sheets for the web only; not on mobile apps | Claude, Gemini, OpenAI |
| Up to 3,000 cells per request | Claude, Gemini |
| Help page cap of 350 selected cells | Claude, Gemini |
| Eligible plans list; Business Starter excluded | Claude, Gemini, OpenAI |
| Experiments and Beta Sources view (undated snippet) | Claude |
| Usage limits: 5,000 and 25,000 per month by tier; 24-hour lockout; no published per-tier quotas | Claude, Gemini |
| Prices: Business Standard $14 annual, $16.80 monthly; Google AI Pro $19.99; Ultra $249.99 | Claude, Gemini |
| 55 times faster on 500-cell tasks | Claude, Gemini, OpenAI |
| Whether Sources survive Make a copy, paste as values, or viewing without an eligible plan | Claude, Gemini |
| Language coverage, 19 languages | Gemini |
| Excel COPILOT retired 14 September 2026; Clay pricing and valuation | Gemini |
| Third-party surfaces (Zapier, Make, n8n, Activepieces, AI Studio) and their prices | Claude, Gemini, OpenAI |

Added: none. Every pricing, limit and availability claim the module might carry is already flagged.

## 6. Genuine reversals

1. **The receipt records where Gemini looked.** Google presents citations as delivering "greater trust and accuracy"; every brief finds the citation proves origin only. Shukla: "A source in a cell shows where the AI looked. It does not show that the page says what the cell says." (Claude, Gemini, OpenAI)
2. **The update that made one cell cheap to check made the run bigger.** Request size went from 200 cells (June 2025) to 3,000 (October 2026) in the same post that added citations. Shukla: "Nobody opens 3,000 sources." The 55x figure measures speed of entry; Shukla: "That figure measures speed, not correctness." (Claude, Gemini)
3. **Wrong answers look like right ones, and citations add to the look.** Liu et al.: the answers that seem more helpful carry more unsupported citations. Dixon: "0 hedges" on any failing answer. Tow Center: "unearned confidence". Shukla: "It looks checked. I think that look is the risk." (Claude, Gemini)
4. **Five clean cells prove less than they seem.** A five-cell check catches a one-in-ten error rate 41% of the time, and five clean cells still allow an error rate up to 45%. (Claude, Gemini; OpenAI computes the 41%)
5. **For the columns that matter most, the right amount to check is all of it, or the column should not be AI-filled.** Shukla: "If that is too many cells, the sheet is too big for that use." UD: "Do not use it for figures you must defend." (Claude, Gemini, one each)

## 7. Hook and value proposition

**Hook: partially supported.** Supported: Google added per-cell web citations to Fill with Gemini, and a citation shows origin, not correctness (all three). Unsupported as worded: "On 30 October 2026" (all three; the announcement is 28 October, rollout from 20 October). Qualified: "none showed where it came from" holds for general Google Sheets users (all three) but not for Experiments testers (Claude) or for Clay (Gemini); the plan scopes it to Sheets. "Every value looked equally confident" has no Sheets evidence; Dixon's "0 hedges" (Gemini app) and the Tow Center's "unearned confidence" support it in substance. "The question has moved to how much to check" is framing, supported in substance by the sampling arithmetic.

**Value proposition: partially supported.** The 41% figure is supported by computation in all three briefs; on a 20 or 40 cell list the exact figure is 43 to 45% (Claude, Gemini). The four-step ladder (read, spot-check, cross-check, sign off) is the module's own framework, consistent with Jose S., Dixon, Shukla and Stanton; it is presented as ours, never as an industry standard. The three failure modes: the first is supported by Liu et al. for search engines generally; the second is partially supported (no-refresh rule, Dixon's stale figure, illustrative examples); the third has no documented Sheets case. The hands-on (20 companies, five cited cells audited in a shared copy) is unverified: no source confirms Sources survive a copy, paste as values, or a viewer without an eligible plan (Claude, Gemini). That is a production blocker for the hands-on, not for the video.
