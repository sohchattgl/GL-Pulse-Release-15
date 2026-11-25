# Narration Scripts: Segment 1

What Google changed in Sheets in October 2026, and how a value filled by Gemini comes to carry the pages behind it.

Voice notes for TTS:
- Conversational pace, a host thinking aloud with a colleague. Plain sentences, no rush.
- "Gemini" is read JEM-in-eye. "Fill with Gemini" is read "Fill with JEM-in-eye". "Google Sheets" and "Google Search" are plain words. "AI function" is read "A I function". "EchoNerve" is read "Echo Nerve". "Workspace" is a plain word.
- Numbers are spoken in words, "two hundred", "three thousand", "fifty-five times", "ninety-five". Dates in full spoken form, "the twenty-eighth of October, twenty twenty-six"; months with years as "June twenty twenty-five".

---

## Segment 1: A Source in Every Cell
*Source: `Segment1_Slides.pptx`*

### Slide 1

A list of company facts lands in our shared folder, filled in by AI in a few seconds, and someone has to decide whether it is good enough to send on. Headquarters city, headcount, one value for every company. So we do what most teams do. We open the first five companies, they look right, and we pass the whole list along. Until October, that habit was a guess with nothing behind it. Every value Fill with Gemini wrote into Google Sheets looked like ordinary typed text, with no trail back to where it came from, so a wrong city and a right one looked exactly alike. Since late October twenty twenty-six, each value Gemini finds on the web arrives with the pages it used. That makes any single value checkable on its own. A receipt records where Gemini looked, and with a long list in front of us the useful question becomes how much of it we actually have to open. First, let's see how a value comes to carry its receipt at all.

### Slide 2

The receipts arrived at the end of a short history, and each step in it changed what a filled value could tell us. Google added the AI function to Sheets in June twenty twenty-five. It wrote text into a selection, and only the first two hundred selected cells got an answer, so any mistake stayed small and close to hand. In October twenty twenty-five the function started answering from Google Search, which meant it could fill in facts nobody had typed into the sheet, like the city a company is based in. Google's announcement of that change never mentions sources. From that point the values could come from the open web, and nothing in the sheet said which page they came from. In April twenty twenty-six, Fill with Gemini arrived as a quicker way into the same function. We drag down from one finished example, or select empty cells and press Fill, and the whole range fills itself. Then, on the twenty-eighth of October twenty twenty-six, Google's Workspace team announced that every value drawn from the web now carries the exact pages behind it, kept with that one value, in Sheets on the web. The same announcement raised a single request to three thousand cells. That second change gets far less attention than the first, and it matters just as much.

### Slide 3

Knowing when the receipts arrived, we can build the chain that produces one, a link at a time, because each link is a place where a value can go wrong. It starts with a request. We select some empty cells and ask Sheets to fill them, or drag down from one finished example, and underneath sits the same AI function as before. The second link is the one most people miss. The function cannot read the whole spreadsheet or anything else in our Drive. It sees the prompt and only the part of the sheet we point it at, usually the company name in that same row. So that one name is all the context it has, and a vague name gets a vague answer. Third, because the question is about the outside world, the function runs a Google Search, and Gemini writes one short value from the pages that come back. Fourth, the pages it used are attached to that one value, and anyone can open them by clicking into it, hovering, and choosing Sources. That is the receipt. One more fact about the finished value changes how we read it. Once inserted, it stays fixed. Google says it does not refresh by itself, and when a prompt is built by joining cells together we don't even get a prompt to refresh. So if a company's headcount changes after the fill, the value keeps the old number, and the page behind it may already say something else.

### Slide 4

The same announcement that made one value cheap to check also made each run much bigger, and those two changes pull in opposite directions. When the AI function launched, a single run stopped at two hundred cells. Now one request can fill three thousand, fifteen times as many, and every one of them arrives with its own sources. Google also says that filling five hundred cells is up to fifty-five times faster than typing them in by hand, from its own study of ninety-five people. That figure measures how fast values go in. It says nothing about how fast anyone checks them, and checking still happens one value at a time, at just under a minute each. The writer of the EchoNerve newsletter put the problem in five words. Nobody opens three thousand sources. He also noticed what the receipts do to the person reading the sheet. A list that fills itself in seconds, with a web source on every value, looks checked, and that look is the risk. At just under a minute each, three thousand values is close to fifty hours of reading, which no team spends on a list of company facts. So the small habit worth keeping is to count before we trust. When a filled list arrives, we note how many of its values came from the web, and we decide how many we will open before it goes anywhere. Deciding that well starts with knowing what one of those sources actually proves.

---
