# Case study 2: prompts and configuration

Every block the Parts of Case study 2, "A Checking Tab for Every Filled Column", enter on screen, in the order they are entered. Each block is typed or pasted exactly as it stands.

## Config 1: the policy table on the Checking tab

::: config Config 1 (from prompts/Case2_Prompts.md): the policy table
Tab: Checking. Type into A1:C5.
A1: Use              B1: Cells to check   C1: Gemini fills it?
A2: First look       B2: 5                C2: Yes
A3: Working list     B3: 30               C3: Yes
A4: Decision figure  B4: All              C4: Yes, open every source
A5: Must defend      B5: None             C5: No, formula from approved table
:::

## Config 2: the ceiling table on the Checking tab

::: config Config 2 (from prompts/Case2_Prompts.md): the ceiling table
Tab: Checking. Type into A7:C11, then fill B8:C8 down to row 11.
A7: Clean random cells   B7: Highest error rate still allowed   C7: Minutes, at under one a cell
A8: 5    B8: =1-0.05^(1/A8)    C8: =A8
A9: 10
A10: 20
A11: 30
:::

## Config 3: the column table on the Checking tab

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

## Prompt 1: the currency fill

::: prompt Prompt 1 (from prompts/Case2_Prompts.md): the currency fill
D2: =GEMINI("For the country named in this row, give the three-letter code of the currency that is legal tender there today (for example EUR or JPY). Return the code only, with no other words.", A2)
:::

## Prompt 2: the tax rate fill

::: prompt Prompt 2 (from prompts/Case2_Prompts.md): the tax rate fill
E2: =GEMINI("For the country named in this row, give the standard VAT or GST rate in force today, as a number with no % sign (for example 19 or 25.5). Return the number only, with no other words.", A2)
:::

## Config 4: the random draw on the Countries tab

::: config Config 4 (from prompts/Case2_Prompts.md): the random draw
Tab: Countries. Type into F1 and F2.
F1: Draw
F2: =RANDARRAY(60)
:::

## Config 5: the currency sample on the Checking tab

::: config Config 5 (from prompts/Case2_Prompts.md): the currency sample
Tab: Checking. Type into I1:M1, I2, L33 and M33.
I1: Country   J1: Region   K1: Launch wave   L1: Currency   M1: Pass or fail
I2: =SORTN(Countries!A2:D61,30,0,Countries!F2:F61,TRUE)
L33: Passed
M33: =COUNTIF(M2:M31,"Pass")
:::

## Config 6: the tax team lookup on the Countries tab

::: config Config 6 (from prompts/Case2_Prompts.md): the tax team lookup
Tab: Countries. Type into G1:H2, then fill G2:H2 down to row 61.
G1: Tax team rate
H1: Gemini against table
G2: =XLOOKUP(A2,'Standard rates'!A:A,'Standard rates'!C:C)
H2: =IF(IFERROR(VALUE(E2),-1)=G2,"Match","Differs")
:::

## Config 7: the results column on the Checking tab

::: config Config 7 (from prompts/Case2_Prompts.md): the results column
Tab: Checking. Type into H13:H15.
H13: Result
H14: =M33&" of 30 passed"
H15: =COUNTIF(Countries!H2:H61,"Differs")&" of 60 differ from the tax team's table"
:::
