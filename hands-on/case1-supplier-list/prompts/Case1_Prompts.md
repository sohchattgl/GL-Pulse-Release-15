# Case study 1: The Supplier List With a Note Attached, prompts

Every prompt and setting the Parts enter, in the order they enter them. Paste each block exactly as it stands.

## Prompt 1: the headquarters fill

Entered in Part 1, step 2, into cell H3, then copied into H4 to H42.

::: prompt Prompt 1 (from prompts/Case1_Prompts.md): the headquarters fill
H3: =GEMINI("For the company in this row, give the city and country of its headquarters. Use the legal name in column B and the website in column C to identify the company, and answer for the company that runs that website. Write the answer as City, Country, with nothing else in the cell.", B3:C3)
:::

## Config 1: the check log headings

Entered in Part 2, step 1, one heading per cell from I2 to L2.

::: config Config 1 (from prompts/Case1_Prompts.md): the check log headings
I2: Draw
J2: Pass or fail
K2: Evidence sentence
L2: Second source
:::

## Config 2: the random number

Entered in Part 2, step 2, into cell I3, then copied into I4 to I42.

::: config Config 2 (from prompts/Case1_Prompts.md): the random number
I3: =RAND()
:::
