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
