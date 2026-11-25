# Review sheet: Every Cell Gets a Receipt

Four segments, 3,968 narration words, about 26.5 minutes at 150 words per minute. Every segment passes `check_segment.py` with no errors; the one warning is the final landing slide at 22 seconds, which the rules allow.

Conditions of this build: no previews were rendered (LibreOffice and Poppler not installed, by the user's choice), so the eyes-only image checks in `visual-qa.md` did not run; the builder's text-fit check stood in for overflow. The checker ran against a stand-in narration parser because `pipelines/generate_video.py` is not on this machine. The sound-off and picture-off reading passes were run on every spec and narration file.

| Segment | Spec | Deck | Narration | Provenance | Previews | Slides | Words | Minutes | Checker |
|---|---|---|---|---|---|---|---|---|---|
| A Source in Every Cell | `segment1/segment1.yaml` | `segment1/Segment1_Slides.pptx` | `segment1/Segment1_narration.md` | `segment1/Segment1_provenance.md` | not rendered | 4 | 892 | 5.95 | pass, 0 warnings |
| Where Gemini Looked | `segment2/segment2.yaml` | `segment2/Segment2_Slides.pptx` | `segment2/Segment2_narration.md` | `segment2/Segment2_provenance.md` | not rendered | 5 | 1,045 | 6.97 | pass, 0 warnings |
| Five Clean Cells | `segment3/segment3.yaml` | `segment3/Segment3_Slides.pptx` | `segment3/Segment3_narration.md` | `segment3/Segment3_provenance.md` | not rendered | 5 | 982 | 6.55 | pass, 0 warnings |
| How Much to Check | `segment4/segment4.yaml` | `segment4/Segment4_Slides.pptx` | `segment4/Segment4_narration.md` | `segment4/Segment4_provenance.md` | not rendered | 6 | 1,049 | 6.99 | pass, landing 22s (allowed) |

## Defect notes

**A Source in Every Cell.** The process slide has four steps where the plan had five; five boxes overflow the content width in the builder, so search and writing share one step (the narration still walks all five). Slide 4 already quotes "looks checked, and that look is the risk", which takes some force from the closing point of Where Gemini Looked; cutting that sentence here is a candidate amendment.

**Where Gemini Looked.** Sound off, the takeaway band on slide 5 (copy in the sentence from the page) reads as a habit attached to a slide about why wrong cells look checked; it stands alone but sits loosely. Slide 3 uses Google's 350 against 3,000 pages as the example of credible sources disagreeing, which is a disagreement about a limit, not about a fact in a cell; acceptable, slightly stretched.

**Five Clean Cells.** The 200-supplier example was cut from slide 5 on cross-check, since How Much to Check tells it in full. Ten-cell and twenty-cell figures (65%, 88%, 26%, 14%) are computed and recorded as computed in provenance.

**How Much to Check.** The flow slide re-introduces the writer who tested five assistants as "an independent tester" and repeats his line "require the exact page", already heard at the end of Where Gemini Looked; it plays as a callback but introduces him as new. The 3,000-cell and 55x figures are left out, as planned.

## Cross-segment checks

- Titles all differ.
- Hand-offs: each segment's last sentence points to the next by content ("knowing what one of those sources actually proves"; "which brings us to counting"; "which columns deserve that half hour ... is the next thing to settle"); the module ends on the only `landing` slide.
- No narration names a document, a source in generic terms, a beat or a segment number. Specific public actors (Google's announcement, Stanford researchers, the Tow Center) are named where the naming is the point.
- Lesser-known people are spoken by role (the writer of the EchoNerve newsletter, a tutorial writer who teaches spreadsheet analysis, a writer who tested five AI assistants); slide text keeps names only with affiliation.

## Open before the video build

- Run the narration files through the real `pipelines/generate_video.py` parser; the checker here used a stand-in.
- Render previews once LibreOffice and Poppler are available, and run the eyes-only list in `visual-qa.md`.
- MONITOR captions (rollout from 20 October 2026, web only, 350 against 3,000 cells, 55x claim) need a recheck before publishing.
