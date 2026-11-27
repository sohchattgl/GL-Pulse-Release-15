# Every Cell Gets a Receipt: hands-on case studies

Execution Guide | operations, finance

## How to use this guide

One person records each case study Part by Part in Supademo or a screen recorder, step by step, and an AI voice reads each Part's voiceover over the capture. Before recording, work through each case's "Before recording" steps: build the source material, read every file, and write down the audit facts.

Case study 1, The Supplier List With a Note Attached, puts the GEMINI function in Google Sheets to work on a supplier list an operations analyst needs grouped into freight regions: a demo that fills the list, checks a random ten cells against their sources, and ends on the note that travels with the sheet. It draws on segments 1, 2, 3 and 4. Case study 2, A Checking Tab for Every Filled Column, puts the same function to work on a sixty-country pricing sheet: a build that turns the video's checking tiers and sample arithmetic into one reusable tab, then runs it on a currency column and a tax rate column. It draws on segments 1, 3 and 4.

The subject runs live on its surface. The inputs are files we built, and every fact in an output has to come from one of them or from a page Gemini cited on camera. The audit facts are chosen before anything runs. The voiceover describes what this run did, in the past tense, and makes no forecast about other runs.

Last checked against the live surface: Google Sheets on the web, the GEMINI function, 27 November 2026, with Case study 1's Part 1 and the draw in Part 2 run on screen.

## What you need

- Google Sheets on the web, with the GEMINI function: open on 27 November 2026 to accounts with Gemini in Sheets enabled on an eligible plan (Workspace Business Standard or Plus, Enterprise Standard or Plus, Google AI Pro or Ultra, Google AI Pro for Education, or the AI Expanded Access add-on; Google AI Pro is listed at $19.99 a month). It runs in Sheets on the web only. No fallback surface was confirmed; if the surface is unavailable on the day, the recording waits.
- A screen recorder or Supademo, capturing a browser window at 1920 by 1080. Keep out of frame: the account's email address and avatar, other browser tabs and bookmarks, any notification, and any sheet that is not the case's own.
- Excel and Word, or any reader that opens `.xlsx` and `.docx` files, to read the source material before recording.
- Python with python-docx and openpyxl, to build the source material once.

| Case study | Files |
|---|---|
| Case study 1: The Supplier List With a Note Attached | `01_Supplier_List.xlsx`, purchasing's forty suppliers with account code, legal name, website and buyer, the headquarters column empty; `02_Supplier_Key.xlsx`, the team's key for two suppliers, with the page that states each headquarters; `Case1_Prompts.docx`, the headquarters fill prompt and the two entries Part 2 types into the check log |
| Case study 2: A Checking Tab for Every Filled Column | `01_Country_Sheet.xlsx`, sixty countries with region and launch wave, currency and tax rate empty; `02_Tax_Rate_Table.xlsx`, the tax team's dated standard rates; `03_Checking_Policy.docx`, the finance director's memo setting a checking tier for each use; `Case2_Prompts.docx`, the two fill prompts and the seven tables and formulas the Parts type in |

## Terms used in every case study

| Term | Meaning |
|---|---|
| GEMINI formula | =GEMINI(prompt, cells): the Google Sheets function that writes a value from a prompt and the cells it is given, using the pages Google Search finds. Copied down a column, it fills every row. Sorting the sheet runs every GEMINI formula again. |
| Sources | The pages Gemini used for one filled cell, opened from the link icon with the page count under that cell. They show where Gemini looked; reading the page shows whether it states the value. The button beside it, Refresh and fill, runs the formula again and replaces the value. |
| Random draw | A random number beside every row, frozen so it stops changing, then sorted, so the rows we check are a fair sample of the whole list. |
| Pass or fail | The result of checking one cell: it passes when the cited page states the value in the cell, and fails otherwise. |
| Ceiling | The highest error rate a clean sample still allows: about 45% after five clean cells, about 26% after ten, under 10% after thirty. |

# Case study 1: The Supplier List With a Note Attached

## What this case study is about

We are the operations analyst at Larkfield Components, a parts distributor. Next quarter's freight contracts are being set, and the logistics lead has to put each of our forty suppliers into a shipping region before deciding which regional carrier contract to renew. Purchasing's supplier master holds the legal name, the website and the buyer for each supplier, and leaves the headquarters column empty. A supplier placed in the wrong region lands on the wrong carrier's contract for a whole quarter.

The GEMINI function in Google Sheets fills the headquarters city and country for all forty rows from one formula copied down the column, and attaches to each cell the pages it used. We then run the checking routine from the video once, by hand, on this one list: read the pages behind a random ten cells, copy in the sentence that states each city, check two suppliers against what our purchasing team holds on file, cross-check anything that failed, and write the one-line note that travels with the sheet.

Part 1 fills the headquarters column for forty suppliers from one formula. Part 2 draws ten rows at random, opens each cell's Sources and logs pass or fail with the sentence that decided it. Part 3 audits two suppliers against the team's key, cross-checks any failure and writes the note for the logistics lead.

The finished walkthrough runs about 11 minutes. It draws on segment 1 of the video, "A Source in Every Cell", segment 2, "Where Gemini Looked", segment 3, "Five Clean Cells", and segment 4, "How Much to Check".

## Glossary

| Term | Meaning |
|---|---|
| Supplier master | Purchasing's list of the suppliers we buy from: account code, legal name, website, buyer and notes. Ours holds forty suppliers on rows 3 to 42 of the Suppliers tab. |
| Legal name | The registered name on the supplier's invoices, in column B. It is one of the two cells the formula points Gemini at. |
| GEMINI formula | =GEMINI(prompt, cells): Gemini in Sheets answers the prompt for the cells given and attaches the pages it used. Sheets runs every GEMINI formula again when the sheet is sorted, and runs one again when Refresh and fill is clicked under it. |
| Entity we buy from | Column D: whether we buy from the supplier's group or from a local company that belongs to it. Four rows buy from a local company. |
| Freight region | The group of countries one carrier contract covers. The logistics lead assigns each supplier to one from its headquarters country. |
| Evidence sentence | The sentence copied from a cited page that names the headquarters, pasted into column K beside the cell it supports. |
| Second source | A page Gemini did not cite, used to settle a failed cell: here, the supplier's own contact, imprint or about page, logged in column L. |
| Team's key | `02_Supplier_Key.xlsx`: the headquarters our purchasing team holds on file for two suppliers, with the page that states each one. It is ours, written before the fill. |
| Audit note | The line typed above the table that tells the logistics lead how many rows were checked at random, how many matched, and what we did about the rest, with the date of the fill. |

## Who the output is for

The logistics lead receives the filled supplier master with the audit note in cell I1. They group the forty suppliers into freight regions by headquarters country and decide which regional carrier contract to renew. They read the note first, then look at any row marked Fail and what we did about it. The note is one line, two at most, with three numbers and a date.

## Before recording

1. Build the source material from the release folder:

    ```
    python "hands-on/case1-supplier-list/build_materials.py"
    ```

2. Confirm the files:

    | File | What it holds | Voice | Used in |
    |---|---|---|---|
    | `01_Supplier_List.xlsx` | Purchasing's export: forty suppliers with account code, legal name, website, entity, category, buyer and notes, the HQ city, country column empty, and a Regions 2024 tab nobody has kept up | case | Parts 1, 2 and 3 |
    | `02_Supplier_Key.xlsx` | The team's key for two suppliers: headquarters on file, the page that states it and why the row is in the key, plus a How we check tab | ours | Part 3 |

3. Open `01_Supplier_List.xlsx` in Excel. Note the title in row 1, the headings in row 2, the forty suppliers on rows 3 to 42, the empty column H, and the four rows whose column D says UK company or EU company. The Regions 2024 tab is part of the clutter and plays no part.
4. Open `02_Supplier_Key.xlsx` in Excel. Note the two rows on the Key tab and the six lines on the How we check tab. Keep this file off screen until Part 3.
5. Open `Case1_Prompts.docx` in Word. It holds Prompt 1 and the two settings blocks Part 2 types in, in the order the Parts enter them; copy from it, never from memory.
6. Write down the audit facts. Facts chosen before anything runs test the output against what we picked; facts noticed afterwards only confirm what the subject chose to mention.

    | Audit fact | Source |
    |---|---|
    | The list holds 40 suppliers, on rows 3 to 42, with column H empty | `01_Supplier_List.xlsx`, Suppliers tab, rows 3 to 42 |
    | MISUMI Europa GmbH is account LK-S1066 on row 29, website uk.misumi-ec.com, bought from as an EU company | `01_Supplier_List.xlsx`, Suppliers tab, row 29, columns A to D |
    | Headquarters on file for MISUMI Europa GmbH: Frankfurt am Main, Germany | `02_Supplier_Key.xlsx`, Key tab, row 2, column D |
    | MISUMI Europa GmbH's parent group, MISUMI Group Inc., has its head office in Tokyo, Japan | `02_Supplier_Key.xlsx`, Key tab, row 2, column F |
    | Elma Electronic AG is account LK-S1083 on row 37, website elma.com | `01_Supplier_List.xlsx`, Suppliers tab, row 37, columns A to C |
    | Headquarters on file for Elma Electronic AG: Wetzikon, Switzerland | `02_Supplier_Key.xlsx`, Key tab, row 3, column D |
    | Elma Schmidbauer GmbH, an unrelated firm with the same trading name, has its head office in Singen, Germany | `02_Supplier_Key.xlsx`, Key tab, row 3, column F |
    | Four rows buy from a local company: Omron Electronics Ltd, SKF (U.K.) Limited, MISUMI Europa GmbH and RS Components Ltd | `01_Supplier_List.xlsx`, Suppliers tab, column D |
    | Ten clean rows still allow an error rate of up to about 26% | `02_Supplier_Key.xlsx`, How we check tab, row 5 |

7. Re-check the key on the day. The key was checked against both pages on 26 November 2026. Open each URL in column E of the Key tab and confirm the page still names the headquarters in column D. If a page has moved or names another city, change the `KEY` entry in `build_materials.py`, build again, and update the audit facts before recording.
8. Upload `01_Supplier_List.xlsx` to Google Drive and open it with Google Sheets [confirm label]. Check that rows 1 and 2 stay in place when you scroll; if they do not, use View, Freeze, 2 rows.
9. Confirm the surface: Google Sheets on the web, GEMINI function, signed in to an account on an eligible plan with Gemini in Sheets turned on. In an empty cell to the right of the table, type =GEMINI("Say hello") and press Enter. When it returns a value, delete it. If it shows #NAME?, the account lacks the function and the recording waits; no fallback surface was confirmed at gate 0.
10. Check every label the steps quote against the screen. Refresh and fill, the link icon with a page count, Sort sheet A to Z and View, Freeze, 2 rows were seen on screen on 27 November 2026; the upload labels are marked `[confirm label]` until you see them.
11. Keep out of frame the account's email address and avatar, other tabs and any notification. Between takes of Part 1, upload a fresh copy of `01_Supplier_List.xlsx`; Parts 2 and 3 run on the same sheet without a reset.

### Planted, for the person recording only

| Planted in | What it is | What it is for |
|---|---|---|
| `01_Supplier_List.xlsx`, Suppliers tab, row 29 | MISUMI Europa GmbH, the European company of a group with its head office in Tokyo. The row gives the European company's website. A page about the parent group is real and wrong for our row. | Part 3 |
| `01_Supplier_List.xlsx`, Suppliers tab, row 37 | Elma Electronic AG shares its trading name with Elma Schmidbauer GmbH in Singen, Germany. A page about the other Elma is real and wrong for our row. | Part 3 |

## The walkthrough

### Part 1: Fill headquarters city and country for forty suppliers from one prompt

This Part runs the fill. It comes first because every later check reads what this fill returns. The formula hands Gemini the legal name and the website in each row, because the function reads only the prompt and the cells it is given.

1. Show the Suppliers tab of the uploaded list, scrolled to the top so the title, the headings and the first rows are in frame.
2. Click H3, the first empty cell under HQ city, country, paste Prompt 1, our prompt inside the GEMINI function, and press Enter. Wait until H3 shows a city and a country.

::: prompt Prompt 1 (from prompts/Case1_Prompts.md): the headquarters fill
H3: =GEMINI("For the company in this row, give the city and country of its headquarters. Use the legal name in column B and the website in column C to identify the company, and answer for the company that runs that website. Write the answer as City, Country, with nothing else in the cell.", B3:C3)
:::

3. Click H3 and press Ctrl+C. Click the Name box above column A, type H4:H42, press Enter, and press Ctrl+V, so the formula fills the other thirty-nine cells.
4. Wait until no cell in column H shows Generating…, then capture. The wait is cut in the edit.
5. Check that H3 to H42 each hold a value written as a city and a country, with no cell blank and none showing an error.
6. Click H3 and read the formula bar: the GEMINI formula, with the range B3:C3 covering the legal name and the website.

#### If it does something else

If the formula shows #NAME?, the account lacks the GEMINI function and the recording waits. If a cell stays on Generating… for more than two minutes, click it, hover over it and click Refresh and fill, and keep the capture. If cells show errors, upload a fresh copy and take the Part again.

#### Voiceover for Part 1

- V1 (step 1, experience): We're the operations analyst at Larkfield Components, a parts distributor, and our logistics lead needs forty suppliers grouped into shipping regions before next quarter's freight contracts are set. The grouping rests on one fact per supplier, where its headquarters is.
- V2 (step 1, experience): A supplier in the wrong region goes on the wrong carrier's contract for three months. So before we hand this list over, we need to know how much of it we can actually vouch for.
- V3 (step 2, setup): The first empty cell under HQ city, country gets one GEMINI formula. Forty rows is a size one person can fill and check before lunch.
- V4 (step 2, setup): The formula hands Gemini the legal name and the website, because Gemini reads only the prompt and the cells it is given, and the website is what tells two firms with similar names apart.
- V5 (step 3, setup): We copy the formula down the column. What follows is one run of the GEMINI function in Google Sheets on the web, recorded on [after the run: the recording date].
- V6 (step 5, mechanism): Forty values came back, each a city and a country, and every one of them looks equally finished. [after the run: how long the fill took, and whether any cell came back blank.]
- V7 (step 6, mechanism): The formula bar shows what Gemini was given for this row: our prompt, and the legal name and website in B3 and C3.

### Part 2: Draw ten rows at random and check each cell's sources

This Part picks ten rows by a frozen random number and checks each one against the pages Gemini cited. It comes before the audit because the note's first two numbers are counted from this log. The top of the list holds the best-known names, so the draw ignores the order the list arrived in. Sorting makes Sheets run every GEMINI formula again, so the values we check are the ones the cells hold after the sort.

1. Click I2 and type the four headings below, one per cell from I2 to L2.

::: config Config 1 (from prompts/Case1_Prompts.md): the check log headings
I2: Draw
J2: Pass or fail
K2: Evidence sentence
L2: Second source
:::

2. Click I3, type the formula below and press Enter. Copy I3 and paste it into I4:I42 the way Part 1 copied H3.

::: config Config 2 (from prompts/Case1_Prompts.md): the random number
I3: =RAND()
:::

3. Select I3 to I42, press Ctrl+C, then press Ctrl+Shift+V to paste the numbers back as values only, so they stop changing.
4. Right-click the letter I at the top of column I and choose Sort sheet A to Z.
5. Wait until no cell in column H shows Generating…, then capture column H. The sort ran the GEMINI function again in every cell, and these are the values we check.
6. Check that rows 1 and 2 stayed at the top, that I3 shows a plain number in the formula bar, and that each row still has its legal name, website and filled value side by side. Rows 3 to 12 are the draw.
7. Click H3 and hover over the value. In the bar that opens under the cell, click the link icon with the page count, and leave Refresh and fill alone, because it runs the formula again and replaces the value. Capture the list of pages. If the bar shows no link icon, the cell has no Sources: type Fail in J3 and "No source" in K3, and go to the next row.
8. Open the pages in the list in order until one names the headquarters, and copy the sentence that names it.
9. Paste the sentence into K3 and type Pass in J3 when it names the city in H3 and the country matches. When no listed page names that city as the headquarters, type Fail in J3 and type into K3 what the page says instead.
10. Repeat steps 7 to 9 for rows 4 to 12. Capture rows 3, 4 and 12 in full; the edit cuts the other seven to a time-lapse.
11. Check that J3 to J12 each hold Pass or Fail and that K3 to K12 each hold a sentence or "No source".

#### If it does something else

If Refresh and fill gets clicked by mistake, the cell's value and its Sources are replaced: check the new value, say so in column L, and keep the capture. If a cited page will not open, log Fail with the reason.

#### Voiceover for Part 2

- V8 (step 2, mechanism): Now we choose which cells to open. The first rows on this list are the names everyone knows, with current websites and plenty of coverage, so every row gets a random number and the same chance of being opened.
- V9 (step 3, mechanism): Paste the numbers back as values. A random number changes with every edit, and freezing it keeps the draw from reshuffling while we work.
- V10 (step 5, mechanism): The sort puts ten rows at the top that nobody picked, and it ran every formula again. [after the run: the ten suppliers on rows 3 to 12, and how many came from the list's bottom half.]
- V11 (step 7, mechanism): Every check starts in the cell. We click in, hover, click the link icon with the page count, and the pages Gemini used are listed under the value. [after the run: how many pages the first cell listed, or that it listed none.]
- V12 (step 8, mechanism): Those pages show where Gemini looked. The cell passes only when we find a sentence on one of them that names this city as the headquarters, and a cell with no pages behind it fails.
- V13 (step 9, mechanism): The sentence goes into the column beside the value, so the logistics lead sees the evidence without opening anything. [after the run: the first row's result, and the sentence we copied.]
- V14 (step 10, mechanism): The second row runs the same way, Sources, page, sentence. [after the run: the supplier, what its page said, and whether it passed.]
- V15 (step 10, mechanism): The other seven rows run the same three moves. [after the run: any row whose page named the company without naming its city, and what we logged for it.]
- V16 (step 11, mechanism): Ten rows, ten results, each with the sentence that decided it. [after the run: how many of the ten passed.]

### Part 3: Audit two suppliers against the team's key, cross-check failures and write the note

This Part checks the two suppliers our purchasing team holds on file, whether or not the draw reached them, settles each failure from a second source, and writes the note. It comes last because the note counts what Parts 2 and 3 logged. A wrong cell carries a normal-looking citation, so these two are held against the key whether or not the draw reached them.

1. Open `02_Supplier_Key.xlsx` in Excel beside the browser, on the Key tab.
2. In the sheet, press Ctrl+F, find MISUMI Europa GmbH, and check its value in column H against Frankfurt am Main, Germany in the key, letter by letter.
3. Click into its value, hover, click the link icon with the page count, and read whose page Gemini cited: the European company's, the parent group's, or another firm's.
4. Type into its column L "Key:" followed by the headquarters on file, and Pass or Fail into its column J if the draw did not reach it.
5. Repeat steps 2 to 4 for Elma Electronic AG, against Wetzikon, Switzerland, reading whether the cited page describes the firm at elma.com or another Elma.
6. For each Fail in J3 to J12, open the supplier's website from column C, find its contact, imprint or about page, and type that page's address and the city and country it states into column L.
7. If any failure came from a parent group's page, open Sources for each of the four rows whose column D says UK company or EU company and log each one as in Part 2; write the kind of any other failure into column L.
8. Check each audit fact against the sheet and the key, digit by digit: forty rows, both account codes, both rows, both websites, both headquarters on file.
9. Search column H for any value with no Sources behind it or holding more than a city and a country, and log it as Fail.
10. Count from J3 to J12 and column L: rows checked at random, rows that matched, and what we did about the rest.
11. Click I1 and type the audit note in the version that fits the count:
    - [after the run, if all ten matched: "HQ column filled with Gemini on {date}. 10 of 40 rows checked at random against their sources, 10 matched, so up to about 26% of the column could still be wrong. MISUMI Europa and Elma Electronic checked against purchasing's records: {result for each}."]
    - [after the run, if any failed: "HQ column filled with Gemini on {date}. 10 of 40 rows checked at random against their sources, {n} matched. The {n} that failed were corrected from each supplier's own site, and {what the full check covered}. MISUMI Europa and Elma Electronic checked against purchasing's records: {result for each}."]
12. Check that I1 shows the note with three numbers and the date above the table, and capture the whole sheet.

#### If it does something else

If a key page no longer names the headquarters on file, stop and correct the build script before recording again. If more than four rows need a second source, keep the capture and cut the extra checks to a time-lapse in the edit.

#### Voiceover for Part 3

- V17 (step 1, mechanism): Before the fill, our purchasing team wrote down two suppliers' headquarters from their own records. Those answers are ours, set down before Gemini returned anything.
- V18 (step 2, mechanism): MISUMI Europa is the European company of a group based in Tokyo, and our row gives the European company's website, because that's who invoices and ships to us. [after the run: what Gemini wrote for this row, beside Frankfurt am Main, Germany.]
- V19 (step 3, mechanism): Its Sources show whose page Gemini read. [after the run: whether the cited page was the European company's, the parent group's or another, and whether the row was in our random ten.]
- V20 (step 5, mechanism): Elma Electronic shares its name with an unrelated maker of cleaning equipment in Germany, and the website in our row is what separates them. [after the run: what Gemini wrote, beside Wetzikon, Switzerland, and which Elma the cited page described.]
- V21 (step 5, mechanism): So this run could have gone three ways: a clean sample, a sample with failures, or a wrong value that only the key caught. [after the run: which one we got, and the row that put us there.]
- V22 (step 6, mechanism): A failed cell gets a second source, the supplier's own site. [after the run: each failure, and what the supplier's own page said, or that there were none to settle.]
- V23 (step 7, mechanism): One failure tells us about every row like it. [after the run: whether a failure came from a parent group's page, and what the four local-company rows showed when we opened them.]
- V24 (step 10, mechanism): The note's three numbers come straight from the log on screen. [after the run: rows checked at random, rows matched, and what we did about the rest.]
- V25 (step 11, mechanism): The note carries the fill date too, so next quarter's reader knows how old the cities are. [after the run: the ceiling of about 26% if all ten matched, or what we did with each failure.]
- V26 (step 12, landing): Our logistics lead got forty headquarters and one line saying how far to trust them. [after the run: the note as written.] Next time we hand over a filled column, we draw ten rows at random, paste the deciding sentence beside each, and put that one line on top.

## How to tell you are done

- [ ] Show H3 to H42 filled, forty cells, each holding a city and a country.
- [ ] Show the GEMINI formula in H3's formula bar, with the range B3:C3.
- [ ] Show column I holding frozen numbers and the sheet sorted by them, with rows 1 and 2 still at the top and no cell in column H on Generating….
- [ ] Show the Sources list open for each of rows 3, 4 and 12, and a time-lapse of the other seven.
- [ ] Show J3 to J12 each holding Pass or Fail and K3 to K12 each holding a sentence.
- [ ] Show the MISUMI Europa GmbH and Elma Electronic AG rows with their Sources open and the key's headquarters typed into column L.
- [ ] Show a second source typed into column L for every row marked Fail, or no Fail in the log.
- [ ] Show the audit note in I1 with the date and three numbers that match a count of columns J and L.
- [ ] Confirm the exported voiceover reads in under twelve minutes with every bracket written from the capture.

## Where this came from

| ID | Source | What it says |
|---|---|---|
| I1 | slide 1.3 | Fill with Gemini fills selected empty cells, and the function reads only the prompt and the row it is pointed at |
| I2 | slide 1.3 | The pages used are attached to each cell and opened by clicking into the cell, hovering and clicking Sources |
| I9 | slide 2.5 | When a cell passes, copy in the sentence from the page that states the value |
| I11 | slide 3.2 | Check a random draw: give every row a random number, freeze it, sort by it, check the first rows; the top of a list is biased toward well-documented companies |
| I13 | slide 3.4 | A clean sample sets a ceiling: ten clean cells still allow up to about 26% wrong |
| I15 | slide 4.2 | A four-step routine: read the citation, check a random sample, cross-check a second source, sign off with a note; a failed sample sends that kind of row to a full check |
| I18 | slide 4.6 | Hand over a filled column with one line: how many cells checked at random, how many matched, and what we did about the rest; a "last generated" date helps spot stale answers |
| C2 | slide 2.3 | All three failures leave a normal-looking citation behind, and the third (pages disagree) has no documented Sheets case |

Tool facts: Google Sheets on the web, the GEMINI function, run on screen on 27 November 2026. The formula, the bar under a filled cell with Refresh and fill and the link icon that opens Sources, a cell returned with no Sources, the run of every formula again after Sort sheet A to Z, and View, Freeze, 2 rows were all seen in that run. The key page for MISUMI Europa GmbH was read again that day and still names its European headquarters in Frankfurt am Main.

What we constructed: Larkfield Components, its operations analyst, its buyers, its supplier master with notes and an unmaintained regions tab, the team's key for two planted suppliers, and the joining of the fill, a random draw, evidence sentences, a key check, a second source and the audit note in one routine run once. The forty suppliers are real public companies named by legal name and website, because the fill needs public pages; the two key entries were checked against their pages on 26 November 2026.

# Case study 2: A Checking Tab for Every Filled Column

## What this case study is about

We are the finance analyst at Halden Outdoor, an online retailer of outdoor gear that is opening sixty new countries over 2027 and 2028. The finance controller sets local list prices from one country sheet, and needs two columns filled for every country by Friday: the currency and the standard sales tax rate. A wrong currency sends a price list out in money the customer does not use. A wrong tax rate goes straight into every local price, and the controller signs off what goes into the pricing model.

The GEMINI function in Google Sheets on the web fills both columns in minutes, one formula copied down each column, and attaches the web pages it used to each cell. The finance director has already written down how much checking each kind of column gets. We turn that policy into a Checking tab inside the sheet: it reads any filled column and says how many cells to open, what a clean result would rule out, how long the check takes, and when the column should not have been filled at all. The currency column gets the sample its tier asks for. The tax rate column is held against the tax team's own rate table.

Part 1 builds the Checking tab from the finance director's policy. Part 2 fills currency and tax rate for sixty countries and lets the tab count the cells. Part 3 runs the tab on the currency column: a random draw, the sources of each sampled cell, and a pass or fail for each. Part 4 audits the tax column against the tax team's table and records the tier's answer for each column.

The finished walkthrough runs about 12 minutes. It draws on segment 1 of the video, "A Source in Every Cell", segment 3, "Five Clean Cells", and segment 4, "How Much to Check".

## Glossary

| Term | Meaning |
|---|---|
| Checking tab | The tab we build in Part 1. It holds the policy's four tiers, the ceiling table and one row per filled column, and later the currency sample and the results. |
| Tier | How much checking a column gets, set by what the column is used for. Currency is a working list (thirty random cells); the tax rate is a figure we must defend (no fill, a formula from an approved table). |
| Ceiling | The highest error rate a clean result still allows. The tab works it out: 45.1% after five clean random cells, 9.5% after thirty. |
| Random draw | A random number for every country, frozen, then the thirty lowest numbers taken as the sample. Every country has the same chance of being checked. |
| Freeze | Pasting the random numbers back over themselves as plain values (Ctrl+Shift+V), so they stop changing while we work. |
| GEMINI formula | =GEMINI(prompt, cells): Gemini in Sheets answers the prompt for the cells given and attaches the pages it used. Sheets runs it again when Refresh and fill is clicked under the cell, which replaces the value. |
| Sources | What Sheets shows when we click into a filled cell, hover over the value and click the link icon with the page count: the pages Gemini used for that cell. |
| Standard rate | The main VAT or GST rate a country charges on most goods, as the tax team's table gives it, in percent. |
| Tax team's table | `02_Tax_Rate_Table.xlsx`: Halden's approved standard rates for the sixty countries, in force on 1 November 2026, signed off on 3 November 2026. |
| Launch wave | When Halden opens a country: Wave 1 in the first half of 2027, Wave 2 in the second half, Wave 3 in 2028. The sheet lists Wave 1 first. |
| Lookup | An XLOOKUP formula that takes each country's rate from the tax team's table, so every number traces back to a signed-off source. |

## Who the output is for

The finance controller at Halden Outdoor. They set each country's local list prices from the sheet and sign off what enters the pricing model. They check two things first: whether the currency column has been checked enough to send price lists out in it, and where each tax rate came from. They want the answer on the sheet itself: the Checking tab's rows for currency and tax rate, one line each, with the sample result and the tier's answer.

## Before recording

1. Build the source material, from the release folder:

    ```
    python "hands-on/case2-checking-tab/build_materials.py"
    ```

2. Confirm the files:

    | File | What it holds | Voice | Used in |
    |---|---|---|---|
    | `01_Country_Sheet.xlsx` | Sixty countries with region and launch wave, Currency and Standard tax rate (%) empty, and an analyst's Notes tab | case | Parts 1 to 4 |
    | `02_Tax_Rate_Table.xlsx` | The tax team's standard rate for each country, with last changes and notes, and a Sign-off tab | case | Part 4 |
    | `03_Checking_Policy.docx` | The finance director's memo of 9 November 2026: four tiers by use, and how they apply to this sheet | case | Parts 1 and 4 |

3. Read `01_Country_Sheet.xlsx`. Note that rows 2 to 61 hold sixty countries, Wave 1 first, and that columns D and E are empty.
4. Read `02_Tax_Rate_Table.xlsx`. Note the Sign-off tab's dates, the Last change column, and the notes on the United States, Bulgaria and Croatia rows.
5. Read `03_Checking_Policy.docx`. Note the four tiers, the reference line of ceilings, and the section on the new-markets country sheet.
6. Write down the audit facts. Facts chosen before anything runs test the output against what we picked; facts noticed afterwards only confirm what the subject chose to mention.

    | Audit fact | Source |
    |---|---|
    | The sheet holds 60 countries, in rows 2 to 61 | `01_Country_Sheet.xlsx`, Countries tab |
    | Rates in force on 1 November 2026, signed off by the Halden tax team on 3 November 2026 | `02_Tax_Rate_Table.xlsx`, Sign-off tab, rows 2 to 4 |
    | Romania's standard rate is 21, changed from 19 on 1 August 2025 | `02_Tax_Rate_Table.xlsx`, Standard rates tab, Romania row |
    | The United States has no national rate; the pricing model uses 0 | `02_Tax_Rate_Table.xlsx`, Standard rates tab, United States row and Note; `03_Checking_Policy.docx`, "How this applies to the new-markets country sheet" |
    | Bulgaria's prices are in euros since 1 January 2026, when the euro replaced the lev | `02_Tax_Rate_Table.xlsx`, Standard rates tab, Bulgaria row, Note |
    | Currency is a list the team works from: 30 random cells, pass or fail against the cited page | `03_Checking_Policy.docx`, "How this applies to the new-markets country sheet", first paragraph |
    | The tax rate is a figure we must defend: a formula from an approved table, and Gemini only labels around it | `03_Checking_Policy.docx`, "The four tiers", fourth row |
    | Five clean cells allow up to 45% wrong; thirty clean cells bring it under 10% | `03_Checking_Policy.docx`, the paragraph after the tiers table |
    | Any failed sampled cell sends the whole column to a cell-by-cell check | `03_Checking_Policy.docx`, the second paragraph after the tiers table |

7. Upload `01_Country_Sheet.xlsx` to Google Drive, open it with Google Sheets on the web, and save it as a Google Sheets file through File, Save as Google Sheets `[confirm label]`. Name it "Halden country sheet". Keep the uploaded file as the clean copy for retakes.
8. Open Google Sheets on the web, GEMINI function, with an account on an eligible plan (Workspace Business Standard or Plus, Enterprise Standard or Plus, Google AI Pro or Ultra, Google AI Pro for Education, or the AI Expanded Access add-on; Google AI Pro is $19.99 a month as checked on 26 November 2026). In a scratch cell, type =GEMINI("Name the capital of France") and press Enter. When it returns a value, click it, hover, and confirm the bar under it shows Refresh and fill and a link icon with a page count; then delete it. There is no fallback surface: when the formula shows #NAME?, the recording waits. It runs on the web only. Mark any label you could not see `[confirm label]`.
9. Keep out of frame: the account's email address, other Drive files, browser bookmarks and notifications. Between takes, delete the Checking and imported tabs and start again from a fresh Google Sheets copy of `01_Country_Sheet.xlsx`, because a fill cannot be undone.

### Planted, for the person recording only

| Planted in | What it is | What it is for |
|---|---|---|
| `02_Tax_Rate_Table.xlsx`, Standard rates, United States row | No national rate; the table uses 0 and the note says state sales tax is added at checkout. Any filled value other than 0 reads Differs. | Part 4 |
| `02_Tax_Rate_Table.xlsx`, Standard rates, Romania row | 21, raised from 19 on 1 August 2025, so older pages still show 19 | Part 4 |
| `02_Tax_Rate_Table.xlsx`, Standard rates, Bulgaria row, Note | Euro since 1 January 2026, so older pages still show the lev (BGN). Bulgaria is row 39 of the Countries tab. | Part 3 if the draw picks it, and Part 4, step 6 |

## The walkthrough

### Part 1: Build the Checking tab from the policy

This Part turns the finance director's checking policy into a tab inside the country sheet, before Gemini fills anything. It comes first so the tiers, the ceilings and the time per cell are fixed before any value exists to be pleased with. The tab's counts read zero at the end of this Part.

1. Open "Halden country sheet" in Google Sheets on the web and show the Countries tab: sixty rows, Currency and Standard tax rate (%) empty.
2. Open `03_Checking_Policy.docx` in Word beside the browser and scroll to "The four tiers".
3. Click the plus sign at the bottom left of the sheet to add a tab `[confirm label]`, then double-click the new tab's name and rename it Checking.
4. Type the policy table into A1:C5.

::: config Config 1 (from prompts/Case2_Prompts.md): the policy table
Tab: Checking. Type into A1:C5.
A1: Use              B1: Cells to check   C1: Gemini fills it?
A2: First look       B2: 5                C2: Yes
A3: Working list     B3: 30               C3: Yes
A4: Decision figure  B4: All              C4: Yes, open every source
A5: Must defend      B5: None             C5: No, formula from approved table
:::

5. Type the ceiling table into A7:C11, then select B8:C11 and press Ctrl+D to fill the formulas down.

::: config Config 2 (from prompts/Case2_Prompts.md): the ceiling table
Tab: Checking. Type into A7:C11, then fill B8:C8 down to row 11.
A7: Clean random cells   B7: Highest error rate still allowed   C7: Minutes, at under one a cell
A8: 5    B8: =1-0.05^(1/A8)    C8: =A8
A9: 10
A10: 20
A11: 30
:::

6. Type the column table into A13:G15, then select D14:G15 and press Ctrl+D.

::: config Config 3 (from prompts/Case2_Prompts.md): the column table
Tab: Checking. Type into A13:G15, then fill D14:G14 down to row 15.
A13: Column   B13: Use   C13: Filled cells   D13: Cells to check   E13: Highest error rate if all clean   F13: Minutes   G13: Gemini fills it?
A14: Currency   B14: Working list
A15: Tax rate   B15: Must defend
C14: =COUNTA(Countries!D2:D61)
C15: =COUNTA(Countries!E2:E61)
D14: =XLOOKUP(B14,$A$2:$A$5,$B$2:$B$5)
E14: =IF(ISNUMBER(D14),1-0.05^(1/D14),"No sample")
F14: =IF(ISNUMBER(D14),D14,IF(D14="All",C14,0))
G14: =XLOOKUP(B14,$A$2:$A$5,$C$2:$C$5)
:::

7. Select B8:B11, hold Ctrl and select E14, then click Format as percent `[confirm label]` and Decrease decimal places `[confirm label]` once, so each shows one decimal place.
8. Check the Checking tab: B8:B11 read 45.1%, 25.9%, 13.9% and 9.5%; C8:C11 read 5, 10, 20 and 30; C14 and C15 read 0; D14 reads 30 and D15 None; E14 reads 9.5% and E15 No sample; G15 reads "No, formula from approved table".

#### If it does something else

If a cell shows #NAME? or a parse error, compare it with the block character by character, retype it, and keep the capture. If the sheet's locale uses semicolons between arguments, stop, set File, Settings, Locale to United Kingdom `[confirm label]`, and take the Part again.

#### Voiceover for Part 1

- V1 (step 1, experience): We're the finance analyst at Halden Outdoor, an online retailer opening sixty new countries. By Friday the finance controller needs every country's currency and standard sales tax rate, because local list prices get set from this sheet.
- V2 (step 1, experience): Gemini in Sheets can put both columns in for us in minutes. What we can't say yet is how much of each column we'd have to check before anyone puts a price on it.
- V3 (step 2, setup): Our finance director's memo sets four tiers by what a column is used for. We're copying those tiers into the sheet, so every filled column gets the same answer.
- V4 (step 3, setup): Add a tab and call it Checking. It sits beside the country list and reads from it.
- V5 (step 4, setup): Type the four tiers from the memo, each with the number of cells it asks us to open, and whether Gemini fills that kind of column at all.
- V6 (step 5, mechanism): The second table takes a number of clean random cells and works out the highest error rate that could still have handed us that clean result. Beside it go the minutes, at under a minute a cell.
- V7 (step 6, mechanism): Each filled column gets a row. Currency is a list the team works from. The tax rate goes straight into a price, so the memo makes it a figure we must defend.
- V8 (step 8, mechanism): These are the figures from the segment on what a clean result rules out, now working on our own sheet. Currency asks for thirty cells and about half an hour, and the tax rate row asks for none.

### Part 2: Fill currency and tax rate for sixty countries

This Part runs the GEMINI function twice on the Countries tab, once per column, and lets the Checking tab count what arrived. The tax rate is filled against the policy on purpose, so the audit has something to hold against the tax team's table.

1. Go to the Countries tab and click D2, the first empty currency cell.
2. Paste the currency formula, our prompt inside the GEMINI function, and press Enter. Wait until D2 shows a code.

::: prompt Prompt 1 (from prompts/Case2_Prompts.md): the currency fill
D2: =GEMINI("For the country named in this row, give the three-letter code of the currency that is legal tender there today (for example EUR or JPY). Return the code only, with no other words.", A2)
:::

3. Click D2 and press Ctrl+C. Click the Name box above column A, type D3:D61, press Enter, and press Ctrl+V. Wait until no cell in column D shows Generating…. Capture the column filling and then the full column.
4. Click E2, paste the tax rate formula and press Enter.

::: prompt Prompt 2 (from prompts/Case2_Prompts.md): the tax rate fill
E2: =GEMINI("For the country named in this row, give the standard VAT or GST rate in force today, as a number with no % sign (for example 19 or 25.5). Return the number only, with no other words.", A2)
:::

5. Copy E2 into E3:E61 the same way, wait until no cell in column E shows Generating…, then click D2 and E2 in turn so the United Kingdom's values show in the formula bar.
6. Run the shape check: D2:D61 and E2:E61 each hold sixty values with no blank cell, and on the Checking tab C14 and C15 now read 60.

#### If it does something else

If a cell stays on Generating… for more than two minutes, click it, hover and click Refresh and fill, and keep the capture. If cells hold sentences instead of a code or a number, keep them: the audit reads them. If the formula shows #NAME?, stop; the recording waits.

#### Voiceover for Part 2

- V9 (step 1, mechanism): We start with the sixty empty currency cells. One column at a time keeps each fill tied to one prompt.
- V10 (step 2, mechanism): We ask for a three-letter code and nothing else, so a wrong currency has no sentence to hide in.
- V11 (step 4, mechanism): The tax rate gets the same treatment, a bare number. Our memo says this column should never be filled, and we fill it anyway, because the controller's first question is what Gemini would have given us.
- V12 (step 5, mechanism): Both columns are full. [after the run: how long the two fills took, and the currency and rate the United Kingdom's row now holds.]
- V13 (step 6, mechanism): The Checking tab has counted them: [after the run: the counts in C14 and C15]. Every one of those cells looks equally finished, and the tab now knows how many there are to vouch for.

### Part 3: Run the tab on the currency column

This Part draws the thirty currency cells the working-list tier asks for, freezes the draw, and checks each sampled cell against the pages Gemini attached to it. Nothing in this Part sorts the Countries tab, so the filled values stay as Part 2 left them. Capture the first three checks in full and the remaining twenty-seven as a time-lapse. The pass or fail for each goes in the Checking tab.

1. On the Countries tab, type the draw into F1 and F2.

::: config Config 4 (from prompts/Case2_Prompts.md): the random draw
Tab: Countries. Type into F1 and F2.
F1: Draw
F2: =RANDARRAY(60)
:::

2. Select F2:F61, press Ctrl+C, then press Ctrl+Shift+V to paste the numbers back as values only.
3. Check F2: the formula bar shows a plain number with no formula, and the numbers stay put when you click another cell.
4. On the Checking tab, type the sample into I1:M1, I2, L33 and M33.

::: config Config 5 (from prompts/Case2_Prompts.md): the currency sample
Tab: Checking. Type into I1:M1, I2, L33 and M33.
I1: Country   J1: Region   K1: Launch wave   L1: Currency   M1: Pass or fail
I2: =SORTN(Countries!A2:D61,30,0,Countries!F2:F61,TRUE)
L33: Passed
M33: =COUNTIF(M2:M31,"Pass")
:::

5. Check I2:L31: thirty countries, each with its region, wave and filled currency, in draw order.
6. Find the first sampled country on the Countries tab with Ctrl+F, click its Currency cell, hover over the value, and in the bar under the cell click the link icon with the page count, then open the cited page. Leave Refresh and fill alone: it runs the GEMINI function again and replaces the value.
7. Read the page for the currency in use in that country today, then type Pass in M2 on the Checking tab if the page states the filled code's currency as current, or Fail if it does not.
8. Repeat steps 6 and 7 for the second and third sampled countries, captured in full.
9. Repeat steps 6 and 7 for the remaining twenty-seven, captured as a time-lapse, and note how many minutes the thirty took.
10. Check M2:M31: thirty entries, no blank, and M33 showing the count of Pass.

#### If it does something else

If the bar under a cell shows no link icon, the cell has no Sources: mark it Fail with "no source" beside it and keep the capture. If Refresh and fill gets clicked by mistake, check the new value and keep the capture. If the cited page is not in a language you read, mark it Fail. If the random numbers change after step 2, take the Part again from step 1.

#### Voiceover for Part 3

- V14 (step 1, mechanism): Every country gets a random number. Our list opens with the wave-one markets, the best documented, so checking from the top would tell us least about the rest.
- V15 (step 2, mechanism): We paste the numbers back as plain values, so the draw stays put while we work.
- V16 (step 5, mechanism): The tab sorts the sixty by those numbers and keeps the first thirty. [after the run: how many of the thirty are wave-one countries.]
- V17 (step 6, mechanism): We open the first country's Sources and read the page for the currency in use there today. [after the run: the country, its code, and what the page said.]
- V18 (step 8, mechanism): Two more, in full. [after the run: the second and third countries, and pass or fail for each.]
- V19 (step 9, mechanism): The other twenty-seven get the same check, sped up here. [after the run: the minutes the thirty took, against the half hour the tab gave.]
- V20 (step 10, mechanism): Thirty passes would put the currency column's highest possible error rate under one in ten. One fail sends the whole column to a cell-by-cell check, as the memo says. [after the run: the count in M33, and which of the two this run was.]

### Part 4: Audit the tax column against the tax team's table

This Part brings in the tax team's signed-off rate table, takes each country's rate from it by lookup, and compares it with what the GEMINI formulas returned. It checks every audit fact, traces every differing row to its source, searches the filled columns for anything no file holds, and records the tier's answer for both columns.

1. Click File, Import, Upload `[confirm label]`, choose `02_Tax_Rate_Table.xlsx`, and pick Insert new sheet(s) `[confirm label]`.
2. Check the Sign-off tab: rates in force on 1 November 2026, signed off by the Halden tax team on 3 November 2026, 60 countries.
3. On the Countries tab, type the lookup into G1:H2, then select G2:H61 and press Ctrl+D.

::: config Config 6 (from prompts/Case2_Prompts.md): the tax team lookup
Tab: Countries. Type into G1:H2, then fill G2:H2 down to row 61.
G1: Tax team rate
H1: Gemini against table
G2: =XLOOKUP(A2,'Standard rates'!A:A,'Standard rates'!C:C)
H2: =IF(IFERROR(VALUE(E2),-1)=G2,"Match","Differs")
:::

4. Check G2:G61: sixty rates, none showing #N/A, with 20 for the United Kingdom in G2.
5. On the Checking tab, type the results column into H13:H15.

::: config Config 7 (from prompts/Case2_Prompts.md): the results column
Tab: Checking. Type into H13:H15.
H13: Result
H14: =M33&" of 30 passed"
H15: =COUNTIF(Countries!H2:H61,"Differs")&" of 60 differ from the tax team's table"
:::

6. Check each audit fact digit by digit with `02_Tax_Rate_Table.xlsx` and `03_Checking_Policy.docx` open: Romania's 21 in G38, the United States' 0 in G14 and its note, the Bulgaria note against the filled currency in D39, B8 and B11 against the memo's ceilings, and A2:C5 against the memo's four tiers.
7. On the Countries tab, click Data, Create a filter `[confirm label]`, and filter column H to show only Differs.
8. For each row that reads Differs, click its Standard tax rate cell, hover, click the link icon with the page count, and read the rate and date on the cited page.
9. Clear the filter and scan D2:E61 for any value that is something other than a three-letter code or a bare number, such as a word, a range or a state tax; no source file holds such a value, so note each row.
10. Read row 15 of the Checking tab: H15's count beside G15's answer for the tax rate.
11. Rename G1 to "Tax rate for pricing (tax team table)" and E1 to "Tax rate as filled by Gemini (not for pricing)".

#### If it does something else

If G shows #N/A, the imported tab's name differs from 'Standard rates'; rename the tab to match and keep the capture. If a filled rate reads Differs only because it carries a % sign or a word, keep it as Differs and say so. If the filter sends cells in columns D or E back to Generating…, wait for the values, read H again, and say so in the note.

#### Voiceover for Part 4

- V21 (step 1, mechanism): Now we bring in the tax team's rate table. Its sign-off tab dates it: rates in force on 1 November 2026, signed off two days later.
- V22 (step 3, mechanism): Each country's rate now comes from that table by formula, and the column beside it says whether Gemini's figure matches.
- V23 (step 5, mechanism): [after the run: the count H15 shows.] Zero would mean all sixty filled rates agreed with the table. Each row above zero is a price that would have rested on a rate our tax team never signed off.
- V24 (step 8, mechanism): The United States has no national sales tax, and our table uses zero. [after the run: what row 14 holds from the fill, and what its Sources page says.]
- V25 (step 8, mechanism): [after the run: each other row that reads Differs, Romania included if it does, with the rate and date on its cited page.]
- V26 (step 10, click): The tax rate was the column we most wanted Gemini to fill. The tab's answer for it reads the same whatever the match count says: take it from the table.
- V27 (step 10, click): A matching number from the fill still has no trail back to an approved source, and that trail is what the controller signs off. The lookup has one, and the filled column has a list of web pages.
- V28 (step 11, click): So the column that feeds pricing is now the lookup, and Gemini's column stays beside it as a record of what the web said.
- V29 (step 11, landing): This was one run, recorded on [after the run: the recording date], with [after the run: currency passes out of thirty, and tax rows that differ out of sixty]. Tomorrow, we add a Checking tab to the next sheet our team fills and type our own tiers into it. Then we let it tell us how many cells to open, and which columns Gemini should never fill.

## How to tell you are done

- [ ] Show the Checking tab's policy table, its ceiling table reading 45.1%, 25.9%, 13.9% and 9.5%, and its column table.
- [ ] Show C14 and C15 reading 0 at the end of Part 1 and the filled counts at the end of Part 2.
- [ ] Capture both fills on the Countries tab, sixty cells each, from the formula in row 2 to the full column.
- [ ] Show the frozen draw in F2 as a plain number in the formula bar.
- [ ] Show thirty sampled countries in I2:L31, each with Pass or Fail in column M and the count in M33.
- [ ] Open Sources on screen for at least three sampled currency cells, with the cited page in frame.
- [ ] Show sixty tax team rates in G2:G61 with Match or Differs beside each.
- [ ] Read the United States row and every Differs row against its Sources page on screen.
- [ ] Show H14, H15 and G15 on the Checking tab together at the end of Part 4.
- [ ] Show G1 and E1 renamed so the pricing column reads from the tax team's table.
- [ ] Confirm the exported voiceover with the time-lapse runs about twelve minutes.

## Where this came from

| ID | Source | What it says |
|---|---|---|
| I4 | slide 1.4 | Each value got cheaper to check and each run got much bigger, so we count the cells before trusting a column |
| I11 | slide 3.2 | Check a random draw: give every row a random number, freeze it, sort by it, check the first rows; the top of a list is biased toward well-documented companies |
| I13 | slide 3.4 | A clean sample sets a ceiling: five clean cells still allow up to 45% wrong, ten about 26%, twenty about 14%, thirty under 10% |
| I14 | slide 3.5 | One cited cell takes under a minute to check; thirty take about half an hour; five is a smoke test for the prompt |
| I17 | slide 4.4 | Checking tiers by use: a first look gets five cells; a working list gets thirty; a figure that changes a decision gets every source; a figure we must defend gets a formula, with Gemini only labelling around it |
| C8 | slide 4.4 | A figure we must defend has no formula trail when Gemini fills it, so it should not be filled |

Tool facts: Google Sheets on the web, the GEMINI function, run on screen in Case study 1 on 27 November 2026: the formula, the bar under a filled cell with Refresh and fill and the link icon that opens Sources, and a cell returned with no Sources were all seen in that run. This case's own steps have not yet been run on screen, and every other screen label is marked `[confirm label]`.

What we constructed: Halden Outdoor, its finance director's checking policy, its tax team's signed-off rate table and its sixty-country sheet are ours; the countries and their standard rates are real, checked on 26 November 2026 against PwC Worldwide Tax Summaries. The Checking tab, which joins the video's checking tiers, ceiling figures, time per cell, cell count and random draw in one reusable tab, is ours.

<!-- Assembled by assemble_guide.py from FRONT-MATTER.md and case*/CASE.md. Edit those files and assemble again. -->
