# Review sheet: Every Cell Gets a Receipt, hands-on

Guide: `hands-on/EXECUTION-GUIDE.md`, knitted to `hands-on/EXECUTION-GUIDE.docx`. `check_handson.py` on `hands-on`: no errors, one warning (Case study 1's key is an `.xlsx` marked ours, which the checker cannot read; its text was checked by hand). Both cases together run 23 finished minutes, under the 25-minute cap.

Built in two cases at the user's choice at gate 1: H1, and H3. The user first picked H3 alone, then added H1 when asked for a second.

## Case study 1: The Supplier List With a Note Attached

| Item | Detail |
|---|---|
| Folder | `hands-on/case1-supplier-list/` |
| Shape | `demo`, operations |
| Subject and surface | Fill with Gemini on Google Sheets on the web: open on 26 November 2026 to eligible plans; no fallback confirmed at gate 0 |
| Ingredients and Parts | I1 Part 1 (the prompt names legal name and website; the formula bar is checked); I11, I2, I9 Part 2 (frozen random draw, Sources, evidence sentence); I15 Parts 2 and 3; I18 Part 3 (the note in I1); I13 only inside the bracketed note (about 26% after ten clean) |
| Caveat | C2, Part 3: two planted suppliers (MISUMI Europa GmbH, row 29, parent group in Tokyo; Elma Electronic AG, row 37, shares its name with Elma Schmidbauer in Singen), held against the team's key whether or not the draw reached them |
| Parts | 3, with 6, 10 and 12 steps |
| Voiceover | 26 lines: experience 2, setup 3, mechanism 20, click 0, landing 1; 837 spoken words, about 5.6 spoken minutes; 11 finished minutes stated |
| First line | "We're the operations analyst at Larkfield Components, a parts distributor, and our logistics lead needs forty suppliers grouped into shipping regions before next quarter's freight contracts are set. The grouping rests on one fact per supplier, where its headquarters is." |
| Click | none; the audit runs to the landing |
| Run on the surface | No Part. The worker could not operate Google Sheets; Fill and Sources come from Google's help page and announcements |
| Still `[confirm label]` | 6: the prompt box, Paste special, Values only, Sort sheet by column I (A to Z), View, Freeze, and the upload and open-with labels |
| Case words | 3,826 outside blocks |
| Checker | no errors; the `.xlsx` key warning above |
| Source files | `01_Supplier_List.xlsx` (case), `02_Supplier_Key.xlsx` (ours); rebuild matches |

Defect note. The forty suppliers are real public companies, an exception to the materials rule, because the fill needs public pages; both key entries were checked on 26 November 2026 and the person recording re-checks them on the day. Nobody has confirmed that Sources survive a sort, so Part 2 carries a fallback (undo the sort and check the ten smallest numbers in place).

## Case study 2: A Checking Tab for Every Filled Column

| Item | Detail |
|---|---|
| Folder | `hands-on/case2-checking-tab/` |
| Shape | `build`, finance |
| Subject and surface | Fill with Gemini on Google Sheets on the web: open on 26 November 2026 to eligible plans; no fallback confirmed at gate 0 |
| Ingredients and Parts | I17, I13, I14 Part 1 (policy table, ceiling table at 45.1%, 25.9%, 13.9%, 9.5%, minutes); I4 Part 2 (the tab counts filled cells); I11 Part 3 (RANDARRAY, frozen, SORTN of thirty) |
| Caveat | C8, Part 4: the tax rate is filled on purpose, then held against the tax team's signed-off table by lookup; pricing reads the lookup column. Plants: the United States (no national rate, table uses 0), Romania (21 since 1 August 2025), Bulgaria (euro since 1 January 2026) |
| Parts | 4, with 8, 7, 10 and 11 steps |
| Voiceover | 29 lines: experience 2, setup 3, mechanism 20, click 3, landing 1; 873 spoken words, about 5.8 spoken minutes; 12 finished minutes stated, with thirty currency checks cut to a time-lapse after the first three |
| First line | "We're the finance analyst at Halden Outdoor, an online retailer opening sixty new countries. By Friday the finance controller needs every country's currency and standard sales tax rate, because local list prices get set from this sheet." |
| Click | The tax rate was the column we most wanted filled, and the tab says to take it from the table whatever the match count (V26 to V28, rests on C8) |
| Run on the surface | No Part. Formulas checked by reading; row references checked against the built files (United Kingdom row 2, United States 14, Romania 38, Bulgaria 39) |
| Still `[confirm label]` | 14, including Generate and Insert, write your own prompt, Format as percent, Decrease decimal places, File, Import, Upload, Insert new sheet(s), Create a filter, Save as Google Sheets, the add-tab plus sign and the Locale setting |
| Case words | 4,012 outside blocks |
| Checker | no errors, no warnings |
| Source files | `01_Country_Sheet.xlsx`, `02_Tax_Rate_Table.xlsx`, `03_Checking_Policy.docx`, all case voice; rebuild matches |

Defect note. All sixty standard rates were checked against PwC Worldwide Tax Summaries on 26 November 2026, and the table is dated inside the case (in force 1 November 2026); a rate change before recording means editing the build script. "Gemini only labels around it" became renamed headers and the lookup column, with no second fill, to stay within twelve minutes.

## Across the pair

- Jobs, shapes and functions differ: a supplier list for freight regions (demo, operations) and a country pricing sheet (build, finance).
- No prompt or config appears in both; the checker enforces it. Both cases draw and freeze a random sample, case 1 by hand with RAND and a sort, case 2 inside the tab with RANDARRAY and SORTN; the repetition is deliberate and the second plays as the routine made reusable.
- The subject runs live in both, on the one confirmed surface.
- In sequence: case 1 runs the video's routine once by hand and ends on the note; case 2 turns the tiers and the arithmetic into a tab and ends on the column the tab refuses.
- Open before recording: every `[confirm label]`, the bracketed outcome lines, the key and rate re-checks on the day, and the account's eligibility. No surface pass has been run, so the front matter's pre-flight date is the tool-stack check, never a run.
