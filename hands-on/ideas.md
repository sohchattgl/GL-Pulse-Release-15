# Hands-on ideas: Every Cell Gets a Receipt

Release folder: `Release 15`. Digest: `hands-on/module-digest.md`. Tool stack: `hands-on/tool-stack.md`. Segment plan: `plan/segment-plan.md`.

Five ideas. Each passes the seven tests in `references/ideation.md`; the set meets the spread. The user picks two at gate 1.

Every card runs on the one surface confirmed at gate 0, so none names a fallback surface; when the surface is down, the recording waits. Each list Gemini fills names public organisations, venues or countries, because a web-sourced fill needs public pages; the company doing the job and every file it owns are invented.

## Spread across this set

| Rule | How this set meets it |
|---|---|
| At least three shapes | H1 demo, H2 probe, H3 build, H4 swap, H5 compare |
| At least one demo or build | H1, H3 |
| At most two probes | 1 |
| Every segment drawn on | 1: H1, H3, H4, H5; 2: H1, H2, H4, H5; 3: H1, H2, H3, H5; 4: H1, H3, H4 |
| At least three business functions | operations, sales, finance, people, marketing |
| No two cards share shape and function | five shapes across five functions |

---

## H1. The Supplier List With a Note Attached

**Job.** We are the operations analyst at Larkfield Components, a parts distributor, and we fill headquarters city and country for forty suppliers so the logistics lead can group them into shipping regions for next quarter's freight contracts.

**Business function.** operations

**Reader.** The logistics lead, who assigns each supplier to a freight region and decides which regional carrier contract to renew.

**Shape.** `demo`

**Subject and surface.** Fill with Gemini on Google Sheets on the web, Fill with Gemini. Fallback: none confirmed; the recording waits.

**Ingredients.**

| ID | Slide | Where it operates in this job |
|---|---|---|
| I1 | 1.3 | Part 1: the prompt points at the supplier name and its website column, which is all Gemini has to tell two similar names apart |
| I2 | 1.3 | Part 2: each sampled cell's Sources view is opened on screen |
| I11 | 3.2 | Part 2: a random number for every row, frozen, sorted, and the first ten rows checked |
| I9 | 2.5 | Part 2: each passing cell gets the sentence from the page that states the city |
| I15 | 4.2 | Parts 2 and 3: read, sample, cross-check the failures, sign off |
| I18 | 4.6 | Part 3: the audit note the logistics lead receives with the list |

**What is ours.** The viewer watches the whole four-step routine run once on one ordinary list, ending in the exact note that travels with the sheet, so the routine from the last segment becomes forty minutes of somebody's Tuesday.

**Caveat.** C2: two planted suppliers have cited pages that are real and wrong for our row (a parent group's head office for a regional subsidiary, and a name shared with an unrelated firm abroad). The team's key for those two rows sits in the source material, and Part 3 checks them whether or not the random draw reached them.

**Surface steps.**
1. prompt: write the fill instruction pointing at the supplier name and website columns
2. fill: fill headquarters city and country for the forty empty rows
3. random draw: add a random number beside every row
4. freeze values: freeze those numbers so the draw stops changing
5. sort: sort by the frozen number and take the first ten rows
6. sources view: open the pages behind each of the ten cells
7. open page: read the page for the city and copy the sentence that states it
8. note: write the audit note above the table

**Claim ledger.**

| Claim | Tag | Source |
|---|---|---|
| Each filled cell carries the pages Gemini used, opened from the cell | video | I2 |
| The function reads only the prompt and the row it is pointed at | video | I1 |
| A wrong cell looks the same as a right one | video | C2 |
| How many of the ten sampled cells pass on this run | observed | |
| Whether the draw reaches either planted row, and what Gemini wrote for each | observed | |

**The audit.** The team's key (02_Supplier_Key.xlsx) holds, for the two planted rows only, the headquarters our purchasing team holds on file and the page that states it. The audit note's three numbers (cells checked, cells matched, what we did about the rest) are counted from the check log on screen. The ceiling for ten clean cells, about 26%, comes from slide 3.4.

**Click.** none; the audit runs to the landing.

**Parts.**
1. Fill headquarters city and country for forty suppliers from one prompt.
2. Draw ten rows at random, open each cell's sources and log pass or fail with the evidence sentence.
3. Audit: check the two planted rows against the team's key, cross-check any failure, and write the note for the logistics lead.

**Source material to build.**
01_Supplier_List.xlsx: forty suppliers with legal name, website and the buyer who owns the account, headquarters columns empty.
02_Supplier_Key.xlsx: the team's key for the two planted rows, marked ours.

**Observable outcome.** The capture shows forty filled rows, ten opened Sources views with a pass or fail and an evidence sentence each, and a note with three numbers. How many cells pass, and whether the planted rows come back right or wrong, are the model's and the web's on the day; the voiceover sorts the run between a clean sample, a sample with failures, and a planted row caught only by the key.

**Finished minutes.** 11

**What could make it fail on the day.** The recording account lacks Gemini in Sheets or the Sources label has changed; a planted supplier's real headquarters has moved since the build; the fill stalls on a large selection; checking ten cells runs long, so seven are cut to a time-lapse.

---

## H2. The Top Five Passed

**Job.** We are in sales operations at Brightwater Analytics, a software company, and we fill headquarters country and state for thirty prospect accounts so the sales manager can split them into territories before the quarterly kickoff.

**Business function.** sales

**Reader.** The sales manager, who assigns each account to a territory and a rep by where it is headquartered.

**Shape.** `probe`

**Subject and surface.** Fill with Gemini on Google Sheets on the web, Fill with Gemini. Fallback: none confirmed; the recording waits.

**Ingredients.**

| ID | Slide | Where it operates in this job |
|---|---|---|
| I11 | 3.2 | Part 3: a random draw replaces the first five rows as the sample |
| I12 | 3.3 | Part 3: what a five-cell check could catch, said once against our result |
| I13 | 3.4 | Part 4: the audit note states what five clean cells rule out |
| I10 | 2.5 | Part 2: the planted rows lower in the list look exactly like the top rows |

**What is ours.** The viewer watches the same filled list pass the convenient check and then meet a fair one, on a list built the way real prospect lists are built, largest accounts first.

**Caveat.** C9: the list arrives sorted by annual revenue, so its top five are the best-documented companies; three smaller accounts lower down are planted with names close to larger firms or a headquarters that moved. Part 2 checks the top five first, as the habit does, and Part 3 checks a random five.

**Surface steps.**
1. prompt: write the fill instruction pointing at account name and website
2. fill: fill headquarters country and state for thirty rows
3. sources view: open the sources for the first five rows
4. random draw: add a random number beside every row
5. freeze values: freeze the numbers
6. sort: sort by them and open the first five
7. open page: read each page for the stated headquarters
8. note: write the audit note for the sales manager

**Claim ledger.**

| Claim | Tag | Source |
|---|---|---|
| The top rows of a list sorted by size are the best-documented companies | video | C9 |
| Five clean random cells still allow an error rate up to 45% | video | I13 |
| A wrong value carries the same confident text and citation as a right one | video | I10 |
| Whether the top five pass on this run | observed | |
| Whether the random five reach a planted row, and what each check finds | observed | |

**The audit.** The team's key (02_Territory_Key.xlsx) holds the headquarters our CRM records for the three planted accounts, entered by reps after discovery calls. The audit compares those three with what Gemini wrote, and the note states the sample, the matches and the 45% ceiling from slide 3.4.

**Click.** The top five passing reads as a checked list; the audit shows that a clean five is consistent with almost half the list being wrong, whatever the random five found. Rests on I13.

**Parts.**
1. Fill headquarters country and state for thirty prospects from one prompt.
2. Check the top five rows the way the habit does, and log the result.
3. Draw five rows at random, check them, and log the result beside the first.
4. Audit: hold the three planted accounts against the team's key and write what the sample rules out.

**Source material to build.**
01_Prospect_Accounts.xlsx: thirty accounts sorted by annual revenue, with website, rep and stage, headquarters columns empty.
02_Territory_Key.xlsx: the CRM headquarters for the three planted accounts, marked ours.

**Observable outcome.** The capture shows two five-cell checks side by side and three planted rows held against a key. Both checks may pass, one may catch a planted row, or Gemini may get the planted rows right; the voiceover sorts the run between those three outcomes, and the click holds in all three.

**Finished minutes.** 10

**What could make it fail on the day.** The random draw on the day may land on the top rows, so the voiceover reads whatever it reached; a planted account's real headquarters changes; the account lacks Gemini in Sheets.

---

## H3. A Checking Tab for Every Filled Column

**Job.** We are the finance analyst at Halden Outdoor, an online retailer expanding into new markets, and we prepare a country sheet with currency and the standard sales tax rate for sixty countries so the finance controller can set local prices.

**Business function.** finance

**Reader.** The finance controller, who sets local list prices from the sheet and signs off what goes into the pricing model.

**Shape.** `build`

**Subject and surface.** Fill with Gemini on Google Sheets on the web, Fill with Gemini. Fallback: none confirmed; the recording waits.

**Ingredients.**

| ID | Slide | Where it operates in this job |
|---|---|---|
| I17 | 4.4 | Part 1: the tab's tier column, set by how each filled column will be used |
| I13 | 3.4 | Part 1: the tab's ceiling lookup, from five clean cells to thirty |
| I14 | 3.5 | Part 1: the tab's time estimate at under a minute a cell |
| I4 | 1.4 | Part 2: the tab counts the filled cells before anyone checks them |
| I11 | 3.2 | Part 3: the tab's random draw picks the rows for the currency check |

**What is ours.** The viewer watches the module's tiers and arithmetic become one reusable tab that reads any filled column and says how many cells to check, what a clean result would rule out, and when the column should not be filled at all.

**Caveat.** C8: the tax rate is a figure we must defend. Part 2 fills it anyway, on camera, and Part 4 holds the column against the tax team's rate table, where the tab's tier sends it to a lookup from that table with Gemini kept to the labels.

**Surface steps.**
1. new tab: add a Checking tab to the country sheet
2. formula: build the tier, sample size, ceiling and time columns from the team's checking policy
3. prompt: write the fill instructions for currency and tax rate
4. fill: fill both columns for sixty countries
5. random draw: draw the currency sample from the Checking tab
6. freeze values: freeze the draw
7. sources view: open the sources for each sampled currency cell
8. formula: look the tax rate up from the tax team's table and compare it with the filled column

**Claim ledger.**

| Claim | Tag | Source |
|---|---|---|
| Thirty clean random cells bring the ceiling under 10%; five leave it at 45% | video | I13 |
| One cited cell takes under a minute to check | video | I14 |
| A figure we must defend gets a formula, with Gemini only labelling around it | video | C8 |
| How many sampled currency cells pass on this run | observed | |
| How many filled tax rates differ from the tax team's table | observed | |

**The audit.** The tax team's rate table (02_Tax_Rate_Table.xlsx), dated and signed off inside the case, is the fact the tax column is held against. The checking policy memo (03_Checking_Policy.docx) gives the tier for each use, and the tab's figures for five, ten, twenty and thirty cells come from slide 3.4.

**Click.** The column we most wanted Gemini to fill is the one the tab tells us to take from a table, whatever the fill got right. Rests on C8.

**Parts.**
1. Build the Checking tab from the team's checking policy: tier, cells to check, ceiling and time.
2. Fill currency and tax rate for sixty countries and let the tab count the cells.
3. Run the tab on the currency column: draw the sample, open each cell's sources, log the results.
4. Audit: hold the tax column against the tax team's table, and record the tier's answer for each column.

**Source material to build.**
01_Country_Sheet.xlsx: sixty countries with region and launch wave, currency and tax rate columns empty.
02_Tax_Rate_Table.xlsx: the tax team's standard rates with an effective date, marked case.
03_Checking_Policy.docx: the team's one-page checking policy, tiers by use, marked case.

**Observable outcome.** The capture shows a working Checking tab, a sampled currency column with a pass or fail per cell, and a tax column compared row by row with the rate table. The fill may match the table on every row or differ on some; the voiceover sorts the run between those outcomes, and the tier's answer for the tax column is the same either way.

**Finished minutes.** 12

**What could make it fail on the day.** A country changes its standard rate between the build and the recording, so the worker dates the table inside the case; the formulas need care on screen; the account lacks Gemini in Sheets.

---

## H4. Headcount, as of When

**Job.** We are the people analyst at Corran Health, a regional care provider, and we refresh a headcount benchmark of fifteen peer organisations so the HR director can propose next year's staffing ratio to the board.

**Business function.** people

**Reader.** The HR director, who puts one benchmark figure per peer in a board paper on staffing.

**Shape.** `swap`

**Subject and surface.** Fill with Gemini on Google Sheets on the web, Fill with Gemini. Before: the team's old step, copying headcounts from last year's industry directory export opened in the same sheet. Fallback: none confirmed; the recording waits.

**Ingredients.**

| ID | Slide | Where it operates in this job |
|---|---|---|
| I7 | 2.3 | Part 3: the date on each cited page, read against the board paper's date |
| I8 | 2.3 | Parts 2 and 3: the measure each page counts (employees, full-time equivalents, or staff with contractors) |
| I3 | 1.3 | Part 4: a "last generated" column, since the fill will not refresh |
| I16 | 4.3 | Part 4: a failure pattern found in the check sends every row like it to a check of its own |
| I5 | 2.2 | Part 3: each cell is judged on what its page states |

**What is ours.** The viewer watches one familiar copy-from-last-year step replaced by a cited fill, then sees the citation answer the two questions the old directory never could: what the figure counts, and when it was true.

**Caveat.** C5: a filled value does not refresh. The old directory export carries its 2025 dates in a column, and Part 4 adds a generated date beside every filled figure. Mode three of C2 has no documented Sheets case, so whether any two pages disagree on this run is observed, never asserted.

**Surface steps.**
1. open page: show last year's directory figures and their dates, the old step
2. prompt: write the fill instruction asking for headcount, what it counts, and the date the page gives
3. fill: fill those three columns for fifteen peers
4. sources view: open the sources for all fifteen, the tier a board figure gets
5. open page: read each page for the measure and the date
6. filter: filter the rows whose page counts a different measure or predates the year
7. note: write the audit note and the generated date for the board paper

**Claim ledger.**

| Claim | Tag | Source |
|---|---|---|
| A filled value is inserted once and does not refresh | video | C5 |
| A page can be out of date, or count a different measure from another credible page | video | I7 |
| A figure that changes a decision gets every source opened | video | I16 |
| How many of the fifteen pages state the figure, its measure and a date | observed | |
| Whether any fill differs from last year's directory, and why | observed | |

**The audit.** The directory export (01_Peer_Directory_2025.xlsx) gives last year's figure and its date for each peer, and the board paper brief (02_Board_Paper_Brief.docx) states the measure the director wants: employees, counted by head, as of the latest annual report. Each filled cell is held against that measure and date.

**Click.** The fill looks like an update of last year's figures; the sources show some figures count a different thing, so the comparison with last year can move because the measure changed. Rests on I8.

**Parts.**
1. The old step: last year's directory figures, and the two things they never told us.
2. The swap: fill headcount, measure and page date for fifteen peers from one prompt.
3. Open all fifteen sources and record what each page counts and when.
4. Audit: hold every row against the board paper's measure and date, check every row like any failure, and write the note.

**Source material to build.**
01_Peer_Directory_2025.xlsx: last year's directory export for fifteen peers, with figure, unit and date, marked case.
02_Board_Paper_Brief.docx: the HR director's two-paragraph brief naming the measure and the date the board needs, marked case.

**Observable outcome.** The capture shows fifteen filled rows with a measure and date beside each, fifteen opened sources, and a filter that isolates any row whose measure or date fails the brief. Gemini may fill the measure column well, leave it blank, or misstate it; the voiceover sorts the run between those outcomes.

**Finished minutes.** 12

**What could make it fail on the day.** Gemini may ignore the measure and date columns of the prompt; a peer publishes a new report between build and recording; opening fifteen sources runs long, so most are cut to a time-lapse; the account lacks Gemini in Sheets.

---

## H5. Two Ways to Ask for One Column

**Job.** We are the event coordinator at Fernhill Events, an events agency, and we fill the largest theatre-style room capacity for twenty conference venues across three cities so the account director can shortlist venues for a client conference of six hundred.

**Business function.** marketing

**Reader.** The account director, who drops every venue that cannot seat six hundred in one room and sends the client a shortlist.

**Shape.** `compare`

**Subject and surface.** Fill with Gemini on Google Sheets on the web, Fill with Gemini, first prompt. Route B: Google Sheets on the web, Fill with Gemini, second prompt, on a copy of the same twenty rows. Fallback: none confirmed; the recording waits.

**Ingredients.**

| ID | Slide | Where it operates in this job |
|---|---|---|
| I1 | 1.3 | Parts 1 and 2: the second prompt names the measure and points at the venue's city and website, all Gemini has to work with |
| I14 | 3.5 | Part 1: each prompt is smoke-tested on five rows before the full fill |
| I5 | 2.2 | Part 3: each cell is judged on whether its page states that measure |
| I6 | 2.3 | Part 3: a page that gives a venue's total capacity or a different room counts as the page not saying it |

**What is ours.** The viewer watches the same twenty venues filled twice from one sheet, and sees the shortlist decision turn on which question was asked, judged cell by cell from the pages.

**Caveat.** C1: a citation shows where Gemini looked. Both routes return cited cells, so the comparison is made on what the pages state, read in Part 3; two venues are planted whose sites publish a total venue figure far above their largest room.

**Surface steps.**
1. prompt: write the first prompt, asking for capacity
2. fill: smoke-test it on five rows, then fill all twenty
3. prompt: write the second prompt naming the largest single room, theatre style, with city and website
4. fill: smoke-test it on five rows, then fill the copy
5. sources view: open the sources for the same eight rows in both routes
6. open page: read each page for the measure asked
7. filter: filter both routes to venues at six hundred or more and compare the shortlists

**Claim ledger.**

| Claim | Tag | Source |
|---|---|---|
| The function sees only the prompt and the row it is pointed at | video | I1 |
| A citation records where Gemini looked | video | C1 |
| A page that names the venue without the figure asked for is a failed check | video | I6 |
| Whether the two routes give different capacities for the same venues | observed | |
| Whether the two shortlists differ, and on which venues | observed | |

**The audit.** The client brief (01_Client_Brief.docx) fixes the measure: six hundred seated theatre style in one room. The venue list (02_Venue_List.xlsx) carries the city and website for each venue, and the agency's site visit notes (03_Site_Visit_Notes.docx) give the largest room for the two planted venues and three others the team has visited.

**Click.** none; the audit runs to the landing.

**Parts.**
1. Route A: smoke-test and run the plain capacity prompt on twenty venues.
2. Route B: smoke-test and run the prompt that names the measure, on a copy of the same rows.
3. Open the same eight rows' sources in both routes and log whether each page states the measure asked.
4. Audit: hold both shortlists against the site visit notes and the client brief.

**Source material to build.**
01_Client_Brief.docx: the client's one-page event brief with the seating requirement, marked case.
02_Venue_List.xlsx: twenty venues with city and website, capacity column empty, marked case.
03_Site_Visit_Notes.docx: the agency's visit notes for five venues, marked case.

**Observable outcome.** The capture shows two filled columns side by side, eight rows checked in each route, and two filtered shortlists. The routes may agree, differ on the planted venues, or differ elsewhere; the voiceover sorts the run between those outcomes.

**Finished minutes.** 11

**What could make it fail on the day.** A venue changes its published capacity; Gemini fills both routes the same way, which the voiceover reads as it is; the account lacks Gemini in Sheets.
