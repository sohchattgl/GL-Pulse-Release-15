# Narration Scripts: Segment 4

Turns the sampling arithmetic into a four-step checking routine and a checking tier for each column by its use, then closes the module.

Voice notes for TTS:
- Conversational pace, a host thinking aloud. Plain sentences, no rush.
- "Gemini" is read "JEM-in-eye". "EchoNerve" is read "Echo Nerve". "UDomain" is read "You Domain".
- "29 of 30" is read "twenty-nine of thirty". Percentages are read in full, as "forty-five percent" and "ten percent".

---

## Segment 4: How Much to Check
*Source: `Segment4_Slides.pptx`*

### Slide 1

Half an hour of checking is easy to agree to in principle, and harder when someone is waiting on the answer. Imagine a filled list of supplier figures, a few hundred values, each one carrying the pages behind it, and a colleague who needs it for a pricing decision this afternoon. They ask one question. How sure are we? Gemini can now fill a long list in a single request, and every value arrives looking equally finished. If we treat a visible source as proof, unchecked numbers move straight into pricing, supplier and headcount decisions, at the speed the tool was built for. So what routine do we follow before we vouch for a filled list, and how much of it does each list deserve? A first look and a figure that sets a price cost different amounts when they go wrong, and our checking has to tell them apart.

### Slide 2

The routine we need can be built from the ways a single value goes wrong, one failure at a time. A citation tells us where Gemini looked, and nothing about whether the page says what the value says. So the opening step is to read the citation: open the page and find the sentence that states the value. An independent tester who audits the citations of AI assistants puts the rule simply: require the exact page, then find the claim on it. The next failure is scale. We can't read every page, and if we read only the first few names on a sorted list, we read the best-documented companies, the ones least likely to be wrong. So we check a sample picked at random. After that comes the page itself. One page can be out of date, and two good pages can measure different things, full-time staff on one and headcount with contractors on the other. So anything that matters gets a second source. And nobody downstream can see any of this checking, so we sign off with a note that says what we did. When the sample turns up a failure, the routine loops back, and that kind of value gets checked in full. No vendor publishes these four steps. They gather what careful practitioners already do, treating each citation as a route to the evidence.

### Slide 3

That routine has been run end to end, in public, by a tutorial writer who teaches spreadsheet analysis. He had Gemini fill the headquarters city for a list of two hundred suppliers, then froze the answers as plain values so they could not shift while he worked. He put a random number beside every supplier, fixed those numbers, and sorted by them, so the thirty he checked were a fair draw. For each one he opened the cited page and looked for the city, in under a minute apiece, so the whole check cost less than half an hour. Twenty-nine matched their pages. One did not. The note he wrote is one sentence long: thirty random rows checked against sources, twenty-nine matched, directory-sourced rows checked individually. That last clause is the loop at work. The note named the kind of page to distrust, the business directory, and every supplier that leaned on one got a check of its own. One miss in thirty, spread across two hundred suppliers, would leave several more wrong cities among the values nobody opened, and that follow-up is what goes looking for them.

### Slide 4

With that routine in hand, the remaining decision is how much of it each list deserves, and the answer rises with what the list will be used for. The lightest use is a first look, where we only want to know whether the prompt works. Five random cells catch a broken prompt or a messy format before we spend our monthly usage allowance on it. That is all five can do, since five clean cells still allow an error rate up to forty-five percent. The next use is a list the team works from. A wrong value there wastes effort, so we want a ceiling on errors, and thirty clean random cells bring it under ten percent for about half an hour. Then comes a figure that changes a decision, a price or a choice of supplier. A sample describes the list as a whole, while a decision rests on one value, so a single wrong figure is a wrong decision. The writer of the EchoNerve newsletter puts the rule plainly. Open every source, and if that is too many cells, the sheet is too big for that use. Beyond that is a figure we must defend to an auditor or a board, and the UD Technology Team at a company called UDomain draws the line there. A generated number has no formula trail, so we keep the formula and let Gemini only label around it. For the lists that matter most, the right amount of checking is every value, or Gemini does not fill them at all.

### Slide 5

Everything we've worked through fits into a single sentence, and it's worth saying once. A citation tells us where Gemini looked, and how much of a list we check is set by what the list will be used for and by the arithmetic of a random sample. What that means depends on where we sit. An engineer can now read five clean cells as an error ceiling of forty-five percent, and size a sample to the error rate a list can afford. A manager can set a checking tier for each list Gemini fills, by how it will be used, and ask for the audit note that goes with it, so trust becomes a sentence someone can question. And someone early in their career can check a cited value by finding the sentence on the page that states it, and can pick the values to check at random, away from the famous names. All of it takes a random number beside each value and the patience to open thirty pages.

### Slide 6

The habit that carries all of this is a small one. We date each filled value, so the next reader knows how old it is. And when we hand over a filled column, one line goes with it: how many cells we checked at random, how many matched, and what we did about the rest.

---
