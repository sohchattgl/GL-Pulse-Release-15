# Case study 1: The Supplier List With a Note Attached

## What this case study is about

We are the operations analyst at Larkfield Components, a parts distributor. Next quarter's freight contracts are being set, and the logistics lead has to put each of our forty suppliers into a shipping region before deciding which regional carrier contract to renew. Purchasing's supplier master holds the legal name, the website and the buyer for each supplier, and leaves the headquarters column empty. A supplier placed in the wrong region lands on the wrong carrier's contract for a whole quarter.

Fill with Gemini fills the headquarters city and country for all forty rows from one prompt, and attaches to each cell the pages it used. We then run the checking routine from the video once, by hand, on this one list: read the pages behind a random ten cells, copy in the sentence that states each city, check two suppliers against what our purchasing team holds on file, cross-check anything that failed, and write the one-line note that travels with the sheet.

Part 1 fills the headquarters column for forty suppliers from one prompt. Part 2 draws ten rows at random, opens each cell's Sources and logs pass or fail with the sentence that decided it. Part 3 audits two suppliers against the team's key, cross-checks any failure and writes the note for the logistics lead.

The finished walkthrough runs about 11 minutes. It draws on segment 1 of the video, "A Source in Every Cell", segment 2, "Where Gemini Looked", segment 3, "Five Clean Cells", and segment 4, "How Much to Check".

## Glossary

| Term | Meaning |
|---|---|
| Supplier master | Purchasing's list of the suppliers we buy from: account code, legal name, website, buyer and notes. Ours holds forty suppliers on rows 3 to 42 of the Suppliers tab. |
| Legal name | The registered name on the supplier's invoices, in column B. It is one of the two things the prompt points Gemini at. |
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
8. Upload `01_Supplier_List.xlsx` to Google Drive and open it with Google Sheets [confirm label]. Check that rows 1 and 2 stay in place when you scroll; if they do not, use View, Freeze, 2 rows [confirm label].
9. Confirm the surface: Google Sheets on the web, signed in to an account on an eligible plan with Gemini in Sheets turned on. Select two empty cells in column H and confirm the prompt menu with Fill appears, then press Escape. No fallback surface was confirmed at gate 0, so if Fill with Gemini is missing on the day, the recording waits. Forty cells sit well under the 350 cells Google's help page gives for one run.
10. Check every label the steps quote against the screen: Fill and Sources appear in Google's own pages; the prompt box, Paste special, Values only, Sort sheet, Freeze and the upload labels are marked `[confirm label]` until you see them.
11. Keep out of frame the account's email address and avatar, other tabs and any notification. Between takes of Part 1, upload a fresh copy of `01_Supplier_List.xlsx`; Parts 2 and 3 run on the same sheet without a reset.

### Planted, for the person recording only

| Planted in | What it is | What it is for |
|---|---|---|
| `01_Supplier_List.xlsx`, Suppliers tab, row 29 | MISUMI Europa GmbH, the European company of a group with its head office in Tokyo. The row gives the European company's website. A page about the parent group is real and wrong for our row. | Part 3 |
| `01_Supplier_List.xlsx`, Suppliers tab, row 37 | Elma Electronic AG shares its trading name with Elma Schmidbauer GmbH in Singen, Germany. A page about the other Elma is real and wrong for our row. | Part 3 |

## The walkthrough

### Part 1: Fill headquarters city and country for forty suppliers from one prompt

This Part runs the fill. It comes first because every later check reads what this fill returns. The prompt points Gemini at the legal name and the website in each row, because the function reads only the prompt and the row it is pointed at.

1. Show the Suppliers tab of the uploaded list, scrolled to the top so the title, the headings and the first rows are in frame.
2. Click H3 and drag down to H42 to select the forty empty cells under HQ city, country.
3. In the prompt menu Fill with Gemini opens beside the selection, click the box for your own prompt [confirm label] and paste Prompt 1.

::: prompt Prompt 1 (from prompts/Case1_Prompts.md): the headquarters fill
For the company in this row, give the city and country of its headquarters. Use the legal name in column B and the website in column C to identify the company, and answer for the company that runs that website. Write the answer as City, Country, with nothing else in the cell.
:::

4. Click Fill and wait until all forty cells hold a value, then capture. The wait is cut in the edit.
5. Check that H3 to H42 each hold a value written as a city and a country, with no cell blank and none showing an error.
6. Click H3 and read the formula bar. If it shows an AI formula, check that its range covers B3 and C3; if it shows only the value, note that and move on.

#### If it does something else

If no prompt menu appears, the account lacks Fill with Gemini and the recording waits. If the fill stops short of row 42, select the cells still empty, run Prompt 1 on them and keep the capture. If cells show errors, upload a fresh copy and take the Part again.

#### Voiceover for Part 1

- V1 (step 1, experience): We're the operations analyst at Larkfield Components, a parts distributor, and our logistics lead needs forty suppliers grouped into shipping regions before next quarter's freight contracts are set. The grouping rests on one fact per supplier, where its headquarters is.
- V2 (step 1, experience): A supplier in the wrong region goes on the wrong carrier's contract for three months. So before we hand this list over, we need to know how much of it we can actually vouch for.
- V3 (step 2, setup): Select the forty empty cells under HQ city, country. Forty is a size one person can fill and check before lunch.
- V4 (step 3, setup): Paste the prompt into the box beside the selection. It names the legal name and the website, because Gemini reads only the prompt and the row it is pointed at, and the website is what tells two firms with similar names apart.
- V5 (step 4, setup): Click Fill. What follows is one run of Fill with Gemini in Google Sheets on the web, recorded on [after the run: the recording date].
- V6 (step 5, mechanism): Forty values came back, each a city and a country, and every one of them looks equally finished. [after the run: how long the fill took, and whether any cell came back blank.]
- V7 (step 6, mechanism): The formula bar shows what Gemini was given for this row. [after the run: whether the range covered the legal name and the website, as the formula bar shows it.]

### Part 2: Draw ten rows at random and check each cell's sources

This Part picks ten rows by a frozen random number and checks each one against the pages Gemini cited. It comes before the audit because the note's first two numbers are counted from this log. The top of the list holds the best-known names, so the draw ignores the order the list arrived in.

1. Click I2 and type the four headings below, one per cell from I2 to L2.

::: config Config 1 (from prompts/Case1_Prompts.md): the check log headings
I2: Draw
J2: Pass or fail
K2: Evidence sentence
L2: Second source
:::

2. Click I3, type the formula below, press Enter, and double-click the small square at the cell's lower right corner so the formula fills down to I42.

::: config Config 2 (from prompts/Case1_Prompts.md): the random number
I3: =RAND()
:::

3. Select I3 to I42, copy, and paste back with Edit, Paste special, Values only [confirm label], so the numbers stop changing.
4. Click any cell in column I and choose Data, Sort sheet, Sort sheet by column I (A to Z) [confirm label].
5. Check that rows 1 and 2 stayed at the top, that I3 shows a plain number in the formula bar, and that each row still has its legal name, website and filled value side by side. Rows 3 to 12 are the draw.
6. Click into H3, hover over the value and click Sources to see the pages Fill with Gemini used. Capture the list.
7. Open the pages in the list in order until one names the headquarters, and copy the sentence that names it.
8. Paste the sentence into K3 and type Pass in J3 when it names the city in H3 and the country matches. When no listed page names that city as the headquarters, type Fail in J3 and type into K3 what the page says instead.
9. Repeat steps 6 to 8 for rows 4 to 12. Capture rows 3, 4 and 12 in full; the edit cuts the other seven to a time-lapse.
10. Check that J3 to J12 each hold Pass or Fail and that K3 to K12 each hold a sentence.

#### If it does something else

If the Sources label is missing after the sort, press Ctrl+Z to undo it, confirm the label is back, and check the ten rows with the smallest numbers in column I instead; keep the capture. If a cited page will not open, log Fail with the reason.

#### Voiceover for Part 2

- V8 (step 2, mechanism): Now we choose which cells to open. The first rows on this list are the names everyone knows, with current websites and plenty of coverage, so every row gets a random number and the same chance of being opened.
- V9 (step 3, mechanism): Paste the numbers back as values. A random number changes with every edit, and freezing it keeps the draw from reshuffling while we work.
- V10 (step 4, mechanism): The sort puts ten rows at the top that nobody picked. [after the run: which suppliers landed on rows 3 to 12, and how many of them came from the bottom half of the original list.]
- V11 (step 6, mechanism): Every check starts in the cell. We click in, hover, open Sources, and the pages Gemini used are listed under the value. [after the run: how many pages the first cell listed.]
- V12 (step 7, mechanism): Those pages show where Gemini looked. The cell passes only when we find a sentence on one of them that names this city as the headquarters.
- V13 (step 8, mechanism): The sentence goes into the column beside the value, so the logistics lead sees the evidence without opening anything. [after the run: the first row's result, and the sentence we copied.]
- V14 (step 9, mechanism): The second row runs the same way, Sources, page, sentence. [after the run: the supplier, what its page said, and whether it passed.]
- V15 (step 9, mechanism): The other seven rows run the same three moves. [after the run: any row whose page named the company without naming its city, and what we logged for it.]
- V16 (step 10, mechanism): Ten rows, ten results, each with the sentence that decided it. [after the run: how many of the ten passed.]

### Part 3: Audit two suppliers against the team's key, cross-check failures and write the note

This Part checks the two suppliers our purchasing team holds on file, whether or not the draw reached them, settles each failure from a second source, and writes the note. It comes last because the note counts what Parts 2 and 3 logged. A wrong cell carries a normal-looking citation, so these two are held against the key whether or not the draw reached them.

1. Open `02_Supplier_Key.xlsx` in Excel beside the browser, on the Key tab.
2. In the sheet, press Ctrl+F, find MISUMI Europa GmbH, and check its value in column H against Frankfurt am Main, Germany in the key, letter by letter.
3. Click into its value, hover, click Sources, and read whose page Fill with Gemini cited: the European company's, the parent group's, or another firm's.
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
- [ ] Show the prompt in the prompt box before Fill is clicked, naming column B and column C.
- [ ] Show column I holding frozen numbers and the sheet sorted by them, with rows 1 and 2 still at the top.
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

Tool facts: Google Sheets on the web, Fill with Gemini, as checked on 26 November 2026; the Fill and Sources labels and the 350-cell help page limit from Google's help page and its April and October 2026 announcements.

What we constructed: Larkfield Components, its operations analyst, its buyers, its supplier master with notes and an unmaintained regions tab, the team's key for two planted suppliers, and the joining of the fill, a random draw, evidence sentences, a key check, a second source and the audit note in one routine run once. The forty suppliers are real public companies named by legal name and website, because the fill needs public pages; the two key entries were checked against their pages on 26 November 2026.
