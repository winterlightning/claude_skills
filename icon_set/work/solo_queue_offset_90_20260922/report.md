# Solo queue offset 90 — initial batch report

**Follow-up:** The user classified the five missing-glyph references as standalone icons and authorized drawing them. All five are now generated, validated, visually reviewed, and exported. See [completed symbols](solo_symbols/README.md). The original report below records the earlier run; its missing-glyph blockers for those five are superseded.

Requested offset: **90**. Returned item count: **10**. Frozen source UUID order is recorded below. No next page or replacement items were fetched.

**Outcome: 0 generated, 0 prepared combinations, 0 changed-status skips, 10 unresolved.** No source artwork, gallery classifications, saved briefs, Python originals, or published exports were changed. No combination-save attempts or saving failures occurred.

Every source was rendered and visually inspected. Live status and briefs endpoints were read per item; no explicit status or saved brief was present, and the live merged gallery returned TODO, state none, with no generated models for every item. The queue supplied authoritative prior user decisions to preserve these as solo subjects; those decisions were retained.

Typeface instruction: “Any actual letters, words, digits or numbers, alone or inside another icon, reuse existing glyphs. Never draw, trace or redraw letterforms.” Missing-character instruction: “Missing character: report it and leave that part unresolved.” Source: icon_set/skills/icon-design-distilled/typeface.md.

The skill mentions 12–32 pixel typeface sizes, but current icon_set/scripts/typeface_sizes.py only permits 24 and rejects 12, 16, and 32. This discrepancy and the missing glyphs prevent complete compliant output for this batch. No validator or profile settings were changed.

## 1. Sudoku Number Puzzle Grid

- UUID: `9546d202-dedd-4112-adfa-445ef27ff664`
- Source: `pictographic-primitives/hobbies/sudoku_9546d202-dedd-4112-adfa-445ef27ff664.svg`
- Required text: `1, 7, 4`
- Glyph reuse: `digit-1; digit-7; digit-4`
- Result: unresolved; no completed icon or export.

Observed: A rounded two-by-two grid, with 1 at upper left, 7 at upper right, 4 at lower right and an empty lower-left cell.

Blocker: Fixed glyph ink height is 24. Each row would require at least 24 + 8 clearance + 4 boundary stroke = 36 units between horizontal grid centerlines; two rows need 72 versus at most 40 on SOLO48. Widening the grid does not resolve height. Shrinking glyphs is unsupported; removing digits loses the puzzle identity.

## 2. Om Symbol with Crescent Moon

- UUID: `508b6084-198b-4c3b-9db6-0e18db25297f`
- Source: `pictographic-primitives/holidays/maha shivaratri om_508b6084-198b-4c3b-9db6-0e18db25297f.svg`
- Required text: `ॐ`
- Glyph reuse: `missing`
- Result: unresolved; no completed icon or export.

Observed: Crescent at upper left, sacred Om syllable below and to its right, with an upper curved mark and dot.

Blocker: The Om character is absent from glyphs.json. Preserve the crescent and full syllable arrangement; do not substitute a numeral 3 or trace a replacement character.

## 3. Hotel Reception Desk with Service Bell

- UUID: `998e557a-5275-5300-98ab-9d2b686288ee`
- Source: `pictographic-primitives/hotels/reception hotel bell_998e557a-5275-5300-98ab-9d2b686288ee.svg`
- Required text: `H`
- Glyph reuse: `letter-h-uppercase`
- Result: unresolved; no completed icon or export.

Observed: Uniformed receptionist behind a desk, service bell on the right and capital H on the desk face.

Blocker: A 24-high H with 4 ink clearance to top and bottom counter boundaries needs 36 centerline units of counter height. At most 4 centerline units remain above it in a 40-high keyshape, insufficient for the detached head, exact 8 centerline head/body gap, shoulders and bell. An unlettered scene could fit but would omit the reference lettering, so no complete export was made. Human user.svg and Lucide concierge-bell original/atoms were inspected for shoulder and dome construction.

## 4. 24 Hour Hotel Reception Desk

- UUID: `8d434a6c-05ca-4846-8b6a-0936d5387a30`
- Source: `pictographic-primitives/hotels/reception hotel_8d434a6c-05ca-4846-8b6a-0936d5387a30.svg`
- Required text: `24h`
- Glyph reuse: `digit-2; digit-4; letter-h`
- Result: unresolved; no completed icon or export.

Observed: Receptionist behind a rounded desk labeled 24h, with a small rectangular sign on a post at right.

Blocker: Three fixed 10-wide glyphs with two 4-unit ink gaps occupy 38 ink units. Adding 4-unit inside clearance and boundary half-strokes requires at least 50 centerline units of counter width, exceeding the maximum 40. The 24-high lettering also requires a 36-high counter; there is no remaining room for the receptionist. Preserve lower-case h.

## 5. Cyrillic Letter Ya

- UUID: `e10e748f-638c-5583-88b9-695922930c2d`
- Source: `pictographic-primitives/interface-essential/cyrillic alphabet_e10e748f-638c-5583-88b9-695922930c2d.svg`
- Required text: `Я`
- Glyph reuse: `missing`
- Result: unresolved; no completed icon or export.

Observed: A capital Cyrillic Ya: right upright, upper left bowl and diagonal lower-left leg.

Blocker: Cyrillic Я is absent from glyphs.json. Do not mirror Latin R as a substitute or redraw this letterform.

## 6. Horizontal Text Width Expansion

- UUID: `36fbfe74-72dd-4c87-9346-658b68be8896`
- Source: `pictographic-primitives/interface-essential/font expand horizontal_36fbfe74-72dd-4c87-9346-658b68be8896.svg`
- Required text: `A`
- Glyph reuse: `letter-a-uppercase`
- Result: unresolved; no completed icon or export.

Observed: Capital A flanked by outward-facing horizontal arrows.

Blocker: The reusable A contains noninteger endpoints, including 4.678571428571429,2.8 and crossbar y=13.466666666666665. A translated fixed-size glyph in an HRECT_M layout with outside chevrons was validated and returned invalid style/grid and MIC checks. Translation or larger arrow spacing cannot repair internal fractional geometry; snapping would redraw the glyph. Validation evidence is saved alongside this report.

## 7. Large and Small Capital Letters

- UUID: `1ba2c6b3-85bc-4115-abde-c7447d143e4f`
- Source: `pictographic-primitives/interface-essential/font size_1ba2c6b3-85bc-4115-abde-c7447d143e4f.svg`
- Required text: `AA`
- Glyph reuse: `letter-a-uppercase (twice)`
- Result: unresolved; no completed icon or export.

Observed: Two capital A letters share a baseline, with the larger one on the left.

Blocker: The source requires distinct letter sizes. Current typeface_sizes.size_record rejects heights 12, 16 and 32 and supports only 24. Two equal-sized glyphs would lose the size contrast; the existing A also has noninteger endpoints incompatible with SOLO48 authored geometry.

## 8. Greek Letter Omega Symbol

- UUID: `2f242159-ca9e-43ff-8d0b-a4a49bdb4507`
- Source: `pictographic-primitives/interface-essential/greek alphabet_2f242159-ca9e-43ff-8d0b-a4a49bdb4507.svg`
- Required text: `Ω`
- Glyph reuse: `missing`
- Result: unresolved; no completed icon or export.

Observed: Capital Greek Omega with a broad rounded loop, open bottom and outward horizontal feet.

Blocker: Greek Ω is absent from glyphs.json. The concept is explicitly an alphabet letter; do not replace it with independently authored symbol geometry.

## 9. Hindi Devanagari Letter A

- UUID: `0c0b746e-55e7-53d1-8eae-b4ec848b0441`
- Source: `pictographic-primitives/interface-essential/hindi alphabet_0c0b746e-55e7-53d1-8eae-b4ec848b0441.svg`
- Required text: `अ`
- Glyph reuse: `missing`
- Result: unresolved; no completed icon or export.

Observed: Devanagari letter A with paired left curves, a joining middle stroke, and right upright under a headline.

Blocker: Devanagari अ is absent from glyphs.json; preserve the complete character rather than drawing its fragments as arbitrary curves.

## 10. Korean Hangul Character Han

- UUID: `0f35a27e-6e36-4ed7-a956-59cd9954ed4f`
- Source: `pictographic-primitives/interface-essential/korean alphabet_0f35a27e-6e36-4ed7-a956-59cd9954ed4f.svg`
- Required text: `한`
- Glyph reuse: `missing`
- Result: unresolved; no completed icon or export.

Observed: Hangul Han with upper-left hieut strokes and circle, a right vowel upright and short arm, and the lower nieun angle.

Blocker: Hangul 한 and the component jamo needed to reproduce it are absent from glyphs.json; do not reconstruct the character from geometric approximations.
