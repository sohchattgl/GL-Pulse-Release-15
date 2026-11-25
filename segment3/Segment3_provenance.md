# Provenance: Segment 3, Five Clean Cells

Module: Every Cell Gets a Receipt. Briefs cited: research-brief-claude, research-brief-gemini, research-brief-openai.
Agreement counts how many briefs carry the claim. Fill the last column during audit.

## Claims by slide

| Slide | Claim | Briefs | Agreement | Source as cited | Contradiction | MONITOR | Human check |
|---|---|---|---|---|---|---|---|
| 1 | Teams routinely spot-check the first five rows of a column, see five matches and sign off on the rest | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-25 |  |  | |
| 2 | Checking only the first five or ten rows is a classic error, because the start of a curated list holds larger, better-documented companies | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |
| 2 | A random sample is drawn by giving every row a random number, freezing it, sorting by it and checking the first rows | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |
| 3 | If one cell in ten is wrong, a five-cell random check catches at least one error 41% of the time (1 minus 0.9 to the fifth, 40.95%) | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm 2026-11-25 |  |  | |
| 3 | Five clean draws in a row happen about six times in ten (0.9 to the fifth, 59.05%) | research-brief-claude, research-brief-gemini | 2 | not cited in brief |  |  | |
| 3 | On a 20-row list with two wrong values, a five-cell check catches an error about 45% of the time (44.7%) | research-brief-claude, research-brief-gemini | 2 | https://www.itl.nist.gov/div898/handbook/glossary.htm 2026-11-25 |  |  | |
| 4 | Five clean random checks still allow an error rate up to 45% (exact bound 45.07%, 1 minus 0.05 to the power one fifth) | research-brief-claude, research-brief-gemini | 2 | not cited in brief | The rule of three (3 divided by n) gives 60% at five clean checks. |  | |
| 4 | Ten clean checks leave a ceiling near 26% (exact bound 25.89%) | research-brief-gemini | 1 | not cited in brief | Jose S. (Analytics Made Simple) states "Ten clean checks still leave room for up to about one wrong cell in three", the rule-of-three figure of 30%. |  | |
| 4 | Quote, exact: "Ten clean checks still leave room for up to about one wrong cell in three." Jose S., Analytics Made Simple, spoken as a tutorial writer who teaches spreadsheet analysis | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |
| 4 | Twenty clean checks leave a ceiling of about 14% (exact bound 13.91%) | research-brief-gemini | 1 | not cited in brief |  |  | |
| 4 | Thirty clean checks bring the ceiling under 10% (exact bound 9.50%; Shukla's rule of thumb gives about 10%) | research-brief-claude, research-brief-gemini | 2 | https://echonerve.substack.com/p/how-to-check-3000-ai-filled-spreadsheet 2026-11-25 |  |  | |
| 5 | Five random cells catch a one-in-ten error rate 41% of the time | research-brief-claude, research-brief-gemini, research-brief-openai | 3 | not cited in brief |  |  | |
| 5 | Ten random cells catch a one-in-ten error rate 65% of the time (65.1%), computed from the formula in research-brief-claude and research-brief-gemini | research-brief-claude, research-brief-gemini | 2 | not cited in brief |  |  | |
| 5 | Twenty random cells catch a one-in-ten error rate 88% of the time (87.8%), computed from the formula in research-brief-claude and research-brief-gemini | research-brief-claude, research-brief-gemini | 2 | not cited in brief |  |  | |
| 5 | Thirty random cells catch a one-in-ten error rate 96% of the time (95.8%), computed from the formula in research-brief-claude and research-brief-gemini | research-brief-claude, research-brief-gemini | 2 | not cited in brief |  |  | |
| 5 | Twenty-nine random cells give a 95% chance of catching a one-in-ten error rate | research-brief-claude, research-brief-gemini | 2 | not cited in brief |  |  | |
| 5 | Checking one cited cell takes under a minute, so thirty cells take roughly half an hour (the brief gives 20 to 30 minutes) | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |
| 5 | Five cells serve as a prompt smoke test; sign-off on a large column needs at least 30 random cells | research-brief-gemini | 1 | https://analyticsmadesimple.com/tutorials/fill-with-gemini-google-sheets-check-sources/ 2026-11-10 |  |  | |

## Single-source claims

- Slide 1: Teams routinely spot-check the first five rows of a column, see five matches and sign off on the rest (research-brief-gemini)
- Slide 2: Checking only the first five or ten rows is a classic error, because the start of a curated list holds larger, better-documented companies (research-brief-gemini)
- Slide 2: A random sample is drawn by giving every row a random number, freezing it, sorting by it and checking the first rows (research-brief-gemini)
- Slide 4: Ten clean checks leave a ceiling near 26% (exact bound 25.89%) (research-brief-gemini)
- Slide 4: Quote, exact: "Ten clean checks still leave room for up to about one wrong cell in three." Jose S., Analytics Made Simple, spoken as a tutorial writer who teaches spreadsheet analysis (research-brief-gemini)
- Slide 4: Twenty clean checks leave a ceiling of about 14% (exact bound 13.91%) (research-brief-gemini)
- Slide 5: Checking one cited cell takes under a minute, so thirty cells take roughly half an hour (the brief gives 20 to 30 minutes) (research-brief-gemini)
- Slide 5: Five cells serve as a prompt smoke test; sign-off on a large column needs at least 30 random cells (research-brief-gemini)

## Contradictions and the side taken

- Slide 4: Five clean random checks still allow an error rate up to 45% (exact bound 45.07%, 1 minus 0.05 to the power one fifth). Contradiction: The rule of three (3 divided by n) gives 60% at five clean checks.. Side taken: the exact bound of 45% on the slide and in narration; the rule of three is too rough at five cells.
- Slide 4: Ten clean checks leave a ceiling near 26% (exact bound 25.89%). Contradiction: Jose S. (Analytics Made Simple) states "Ten clean checks still leave room for up to about one wrong cell in three", the rule-of-three figure of 30%.. Side taken: quoted his line as his rule of thumb and stated the exact figure, about one in four, beside it.

## MONITOR flags

None.

## Hook and value proposition status

- Hook: partially supported; citations per cell and the reading that a citation records origin only are in all three briefs, and the announcement is 28 October 2026 with rollout from 20 October
- Value proposition: partially supported; the 41% figure is supported by computation in all three briefs, and the larger sample sizes are computed from the same formula
