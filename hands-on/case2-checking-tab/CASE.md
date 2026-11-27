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
| Freeze | Pasting the random numbers back over themselves as plain values (Edit, Paste special, Values only), so they stop changing while we work. |
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
9. Turn off Tools, Suggestion controls, Enable autocomplete. With it on, typing Pass in column M of the Checking tab completes to the heading Pass or fail.
10. Keep out of frame: the account's email address, other Drive files, browser bookmarks and notifications. Between takes, delete the Checking and imported tabs and start again from a fresh Google Sheets copy of `01_Country_Sheet.xlsx`, because a fill cannot be undone.

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

3. Click D2 and press Ctrl+C. Click the Name box above column A, type D3:D61, press Enter, and press Ctrl+V. Wait until no cell in column D shows Generating…. Capture the column filling and then the full column. Look for any cell shaded with diagonal stripes: the paste can leave a row holding the value copied from D2, and its sources, without running it. Click that cell, hover and click Generate and fill.
4. Click E2, paste the tax rate formula and press Enter.

::: prompt Prompt 2 (from prompts/Case2_Prompts.md): the tax rate fill
E2: =GEMINI("For the country named in this row, give the standard VAT or GST rate in force today, as a number with no % sign (for example 19 or 25.5). Return the number only, with no other words.", A2)
:::

5. Copy E2 into E3:E61 the same way, wait until no cell in column E shows Generating…, run Generate and fill on any striped cell as in step 3, then click D2 and E2 in turn so the United Kingdom's values show in the formula bar.
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

2. Select F2:F61, press Ctrl+C, then choose Edit, Paste special, Values only. On 27 November 2026 Ctrl+Shift+V left the RANDARRAY formula in place, so use the menu.
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
