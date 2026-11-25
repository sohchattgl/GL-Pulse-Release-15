# Narration Scripts: Segment 2

What a cell's citation proves in Fill with Gemini, and the three ways a cited value can still be wrong.

Voice notes for TTS:
- Conversational pace, a host thinking aloud with a colleague. Plain sentences, no rush.
- "Gemini" is read "JEM-in-eye". "Percy Liang" is read "PER-see LEE-ahng". "Tianyi Zhang" is read "tee-EN-yee JAHNG". "Tow Center": "Tow" rhymes with "go". "Columbia Journalism School" as written. "EchoNerve" is read "Echo Nerve", two plain English words. "Fill with Gemini" and "Google Sheets" as plain English.
- Percentages read in full, "seventy-four point five percent", "fifty-one point five percent". Years as "twenty twenty-three" and "twenty twenty-five". Counts as words, "three hundred and fifty", "three thousand".

---

## Segment 2: Where Gemini Looked
*Source: `Segment2_Slides.pptx`*

### Slide 1

We left off with a long list of filled values, and every one of them now arrives with its pages attached. So let's do what most of us do first. We click into a filled value, hover, and open its sources. A real company page appears, with the company's name across the top. It feels finished. The value has a page behind it, the page looks official, and we move on to the next one. That is the moment Google designed for. Its announcement presents the citations as a way to easily audit and verify what Gemini writes. And there's a quiet risk in that moment. A clickable list of sources can make us trust a value more than we did before, because the presence of a receipt starts to stand in for reading it. Nobody has to decide to skip the reading. It just happens, one value at a time. So before we budget a single hour of checking, we need a plain answer to one question. When Gemini attaches a page to a value, what has it actually told us?

### Slide 2

Behind every filled value sits a short chain of events, and the citation comes from one link in that chain. We ask for a company's headquarters city. Gemini turns the request into a web search, Google Search returns a handful of pages, and Gemini writes a short answer from what it read. Then the pages it used are attached to that one value. Google hasn't published how Sheets makes that connection. In the tools Google offers developers for the same kind of search-backed answer, the connection runs from a stretch of generated text to the pages used to write it. So the link records that a page was used. It records nothing about whether the page states the value. The writer of the EchoNerve newsletter put it in one line: a citation shows where the AI looked, and it doesn't show that the page says what we've been given. Google's own announcement promises full visibility to audit and verify, and it stops there. It never claims the cited pages are right. Gemini has answered the first question, where it looked, at no cost to us. The second question, whether the page says this value, is still ours, and it decides whether a number is safe to put in front of a client.

### Slide 3

The chain behind a filled value has three places where it can go wrong, and each one leaves a perfectly normal citation behind. The first is in the reading. Gemini finds the right company's page and misreads a dense table, or takes the city of a subsidiary, or attaches a page that mentions the company and never states the figure at all. The citation is real and the page is real. The value just isn't on it. Only opening the page catches that one. The second is in time. Search can return an old directory, or a press release from before a round of layoffs, so the headcount Gemini writes was true once. And once the value lands, it stays put. Google says a generated value goes in as an ordinary edit, and when the prompt is built by joining other cells, Sheets won't even offer to refresh it. So a value that was right in October can be wrong by spring, still pointing at its page. The third is disagreement. Two credible pages can measure different things, an annual filing counting full-time staff and a business directory counting headcount with contractors. Gemini picks one and cites it, and nothing tells us a choice was made. Nobody has documented this one inside Sheets yet. It can still happen, and Google shows how easily: its help page says a run fills the first three hundred and fifty selected cells, and its announcement says a request can cover three thousand. For a pricing or supplier decision, all three failures cost us the same thing, a confident number we act on.

### Slide 4

How often that first failure happens is something researchers at Stanford set out to measure. In twenty twenty-three, Nelson Liu, Tianyi Zhang and Percy Liang took four commercial AI search engines, the kind that answer a question in a paragraph and attach links, and had people check every citation against the page it pointed to. Only seventy-four point five percent of the citations supported the sentence they were attached to. And only fifty-one point five percent of the sentences were fully supported by their citations. These were other products, measured three years before Gemini started citing pages in our spreadsheets, so the number doesn't carry over directly. Nobody has measured this for Sheets yet. What it gives us is a sense of scale for planning. If roughly one citation in four failed in products built for answering questions, we can't treat a cited value as right because its link opens. A list of three thousand companies at anything like that rate would hold hundreds of values whose page says something else.

### Slide 5

There's a pattern across the studies of cited answers, and it runs against our instincts. The same Stanford team found that the answers people rated most helpful tended to carry more unsupported citations, so the useful-sounding answer was the one more likely to be wrong about its own links. In twenty twenty-five, researchers at the Tow Center, part of Columbia Journalism School, tested eight AI search tools, Gemini among them, and found them consistently more likely to give a wrong answer than to admit a limit. They called it unearned confidence. And a writer who tested five AI assistants on the same factual questions checked every citation he could open and found zero hedges on any answer that failed. So a wrong value in our sheet looks exactly like a right one. Same format, same tone, same link. The citation is what makes a wrong value look checked, and nothing else about it looks any different. That leaves one small habit. When a value passes, we paste the sentence from the page that states it right next to the value, which is what that writer advises: require the exact page, then find the claim on it. With thousands of values we can't do that for every one, which brings us to counting.

---
