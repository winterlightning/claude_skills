# Solo queue offset 60 — 10 frozen items

All ten current states and saved reference briefs were read from localhost:8000 immediately before review. All remained TODO with no linked model at that time. Each reference was rendered and visually inspected. Original artwork and editorial briefs were preserved. No verified combination splits, no status changes, no save failures.

Author of the three new originals: `gpt-6-astra`. All three targeted builds completed successfully; entries in both family manifests were verified valid with zero errors and warnings.

## 1. Double Up Chevron
UUID: `52dc4cf2-c01c-479a-94a1-3ad9cbef9449`
Source: `pictographic-primitives/_uncategorized_39/up 1_52dc4cf2-c01c-479a-94a1-3ad9cbef9449.svg`

Square keyshape (6,6)-(42,42), two equal repeated chevrons. Lucide chevrons-up informed the two continuous angular strokes. No details omitted. Valid with zero warnings; visually clear, symmetric and evenly separated at 48px in light and dark.

## 2. Set Intersection Symbol
UUID: `6bad0489-febc-4c6d-a02e-bb32765a3240`
Source: `pictographic-primitives/_uncategorized_39/walrus_6bad0489-febc-4c6d-a02e-bb32765a3240.svg`

Square keyshape (6,6)-(42,42), two equal legs and tangent semicircular crown. No useful Lucide arch match. Reference is an open arch; no animal details invented. Valid with zero warnings; smooth and balanced at 48px in both themes.

## 3. Speech Bubble with Checkmark
UUID: `3bb8a803-55a9-4a2d-a6ac-2586a065ac7f`
Source: `pictographic-primitives/chat/criteria_3bb8a803-55a9-4a2d-a6ac-2586a065ac7f.svg`

Container HRECT_L (2,10)-(62,54), rounded bubble with lower-right tail, check and two message rows. Preserved the recorded user decision to keep the whole subject. Lucide message-square-text informed contour construction. No content omitted. Valid with zero warnings; checked at native 64px in both themes. Tested additional hosted plus/check fail; heart is unresolved review.

## 4. Confused Speech Bubble Message
UUID: `835a03b0-4d14-4e41-ac37-15d8f7325426`
Source: `pictographic-primitives/chat/language barrier confused_835a03b0-4d14-4e41-ac37-15d8f7325426.svg`

Unresolved fixed-typeface fit. Exact text #?!; reuse symbol-number-sign, symbol-question and symbol-exclamation. Three glyphs plus two 4px gaps total 32px ink width; enclosing strokes and clearance need 16px more, exceeding the 44px maximum SOLO48 ink envelope. No replacement letters drawn or gallery reclassification made.

## 5. Speech Bubbles with Question Marks
UUID: `944d0ea3-f712-4093-a262-a9b150fbef6c`
Source: `pictographic-primitives/chat/language barrier question_944d0ea3-f712-4093-a262-a9b150fbef6c.svg`

Unresolved fixed-typeface fit. Two overlapping round speech bubbles, each containing symbol-question, retain their opposite tails. A 24px-high glyph requires at least 40px framed height including strokes and clearance; no validated two-bubble layout produced. No glyph redraw or reclassification.

## 6. Underlined Alphabet Letters
UUID: `7ad20e87-7343-4347-8dd5-6c0cde10087e`
Source: `pictographic-primitives/other/la (text u)_7ad20e87-7343-4347-8dd5-6c0cde10087e.svg`

Typeface reuse layout only: exact La from letter-l-uppercase and letter-a with a horizontal underline. Existing glyph paths retained byte-for-byte inside translated groups. Light and dark 48px layouts inspected. Not a Python original, not validated as SOLO48, and not counted as a completed icon.

## 7. Burning Brick Fireplace
UUID: `5a6bc318-1415-407d-8cee-66dc95d8d15f`
Source: `pictographic-primitives/outdoors/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg`

Ambiguous: flame floating above a two-row, three-column brick block. Fireplace scene and firewall metaphor remain plausible. Saved editorial brief explicitly holds generation for human review. No drawing or reclassification.

## 8. Pig with Apple Feed Bag
UUID: `1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4`
Source: `pictographic-primitives/outdoors/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg`

Ambiguous: right-facing pig head touches a rectangular apple panel with no definite bag opening. Feed bag and apple sign/card remain plausible. Saved editorial hold preserved. No drawing or reclassification.

## 9. Credit Card Machine and Receipt
UUID: `29a5a818-9fcd-4062-843c-4ae6c6b33268`
Source: `pictographic-primitives/payments/credit card payment_29a5a818-9fcd-4062-843c-4ae6c6b33268.svg`

Ambiguous: receipt emerges from left payment terminal; separate card at upper-right and downward arrow below. Instructional insertion scene vs component split remains unresolved in saved editorial brief. No drawing or reclassification.

## 10. Binary Code Sequence
UUID: `abff6337-b854-552e-afe3-b89605887cad`
Source: `pictographic-primitives/programing/binary_abff6337-b854-552e-afe3-b89605887cad.svg`

Unresolved fixed-typeface fit: 010 above 001. Reuse digit-0 and digit-1. Two 24px-high rows with 4px clearance need 52px, beyond the 48px canvas before margins. Exporter supports only height 24. No glyph redraw.

## Evidence

- `fixed-worklist.json`: frozen UUID order, source paths and exact saved briefs.
- `00-intake.json` through `09-intake.json`: per-item gallery reads.
- `00-reference.png` through `09-reference.png`: inspected source renders.
- `review-light.png` and `review-dark.png`: enlarged and native renders of the three new drawings.
- `typeface-reuse-layouts.json`: exact strings, existing glyph IDs and unresolved fit constraints.
- `underlined-la-light.svg` and `underlined-la-dark.svg`: typeface layout artifacts.
- `hosting-*.txt`: checked-bubble hosting limitations.

## Why six references remain unresolved

The [queue skill](../../../.agents/skills/icon-solo-queue/SKILL.md) says: “If the reference cannot be inspected or its interpretation remains ambiguous, report that limitation and skip drawing this item.” This applies to the brick/flame, pig/panel, and payment-scene references. Their saved briefs already hold generation for human review; no interpretation answer arrived during this run.

The [distilled skill](../../../.agents/skills/icon-solo-distilled/SKILL.md) says: “reuse `icon_set/typeface/glyphs.json`, never redraw letterforms.” The current exporter only supports fixed 24px-high glyphs; the three text-bearing layouts have unresolved SOLO48 fit constraints. Exact glyph IDs and content are retained in `typeface-reuse-layouts.json`. The La layout is a separate reusable layout artifact, not a completed validated icon.

## Final results

Offset 60, returned count 10: **3 completed icons (2 solo, 1 container), 1 typeface layout only, 6 unresolved references (3 text-fit constraints, 3 ambiguous interpretations).** No current-status skips, no confirmed combination splits, no gallery saving failures. Shared-output contention and one transient concurrent registry-file removal were overcome by targeted retries. No commits or full-library builds were performed.

- `double-up-chevron-reference-52dc4cf2`: [solo48 SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/double-up-chevron-reference-52dc4cf2.svg); valid, zero warnings.
- `rounded-arch`: [solo48 SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/rounded-arch.svg); valid, zero warnings.
- `speech-bubble-with-checkmark`: [container64 SVG](/Applications/Workspaces/pictographic/claude_skills/published/container64/speech-bubble-with-checkmark.svg); valid, zero warnings.
