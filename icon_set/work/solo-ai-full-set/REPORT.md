# Full json_to_solo review

Reviewed all 1,722 original drawings. The originals are unchanged: all current model SVG hashes match the inventory captured before this pass.

| Result | Icons |
|---|---:|
| New visible revisions passing release checks | 203 |
| Construction cleanup passing release checks | 330 |
| Earlier refinements preserved | 200 |
| Original retained after visual review | 981 |
| New candidates still held for spacing review | 8 |

The full-set repair is not completely resolved: the eight candidates below remain unreleased. All new drawings are candidates for human review, not human approvals. Earlier refinements are preserved without claiming they were revalidated against the changed spacing validator.

The 203 visible revisions use SOLO48, stroke 4, round joins and caps, and the appropriate circle, square, horizontal or vertical keyshape. Plans and references are recorded per candidate in batch.json and the source modules. Relevant Lucide originals and atomic-debug geometry informed circles, pins, arrows, leaves, clouds, gifts, vehicles and other matching subjects. Human figures follow the shared human reference; the two-person group uses a four-unit detached head-to-body ink gap.

All 32 original contact sheets were inspected in light and dark themes, at native 48 and enlarged 96 sizes. The 211 manual candidates were compared against their originals in both themes, with final changed sheets checked again. Construction cleanup is restricted to exact collinear/zero-length cleanup and explicit closure; the largest render difference was 0.4393 aggregate pixel equivalents, with identical anchors.

Validation: 533 new release candidates pass inspect_icon; all 541 emitted candidate SVGs, including the eight held in failed/solo48, match their current models byte for byte. Every declared new attachment has a shared endpoint. All 541 modules retain source identity and name gpt-6 as author. The passing build exited 0; the final exception build intentionally exited 1 and withheld the eight unresolved candidates.

The focused variant and straight-spacing tests passed (14 tests). The full repository suite was run but was not green: it reported 6,242 subtest failures and 26 errors across 346 tests. Many concern unrelated missing corpus exports, existing corpus validation, and local test-server socket permissions. It also captured an intermediate Swift candidate before its final correction; the final candidate passes release validation and export comparison. Do not interpret the focused success as a green full repository suite.

## Remaining spacing review

The icon-solo skill requires: “A `review` warning is **not** a pass.” It also directs reporting the check and element when a candidate cannot be made to pass. Wider gaps and simpler fits were attempted below; versions that lost the identifying silhouette were not selected. No profile or tolerance was changed, and no exception was approved.

### pine-f98a2e8b → pine-f98a2e8b-v2

Attempted wider branch gaps and shorter tier overhangs. Keep three tiers and the trunk; the tight branch returns remain flagged for manual exception review.

- internal-spacing [tree]: tree-2 and tree-4 have 2.2666 units of ink clearance over 3.7709 units; requires 4; review required
- internal-spacing [tree]: tree-2 and tree-9 have 2.073 units of ink clearance over 2.6403 units; requires 4; review required
- internal-spacing [tree]: tree-7 and tree-9 have 2.2666 units of ink clearance over 3.7709 units; requires 4; review required

### plane-1-travel → plane-1-travel-v2

Attempted wider wing tips, wider fuselage and shortened tail. Keep this distinct horizontal plane; swept-wing returns still need a spacing exception review.

- internal-spacing [plane]: plane-2 and plane-4 have 2.7286 units of ink clearance over 9.1927 units; requires 4; review required
- internal-spacing [plane]: plane-9 and plane-11 have 2.7286 units of ink clearance over 9.1927 units; requires 4; review required

### plane-1 → plane-1-v2

Attempted broader wings and tail at several integer-grid positions. Preserve the ascending single-wing perspective; the wing and tail returns still need manual spacing review.

- internal-spacing [plane]: plane-0 and plane-9 have 2.4979 units of ink clearance over 5.7144 units; requires 4; review required
- internal-spacing [plane]: plane-5 and plane-7 have 3.4188 units of ink clearance over 5.6879 units; requires 4; review required
- internal-spacing [plane]: plane-7 and plane-9 have 3.3974 units of ink clearance over 7.9903 units; requires 4; review required

### plane → plane-v2

Attempted wider wing and tail returns. Preserve this distinct two-wing perspective; narrow diagonal channels still need a spacing exception review.

- internal-spacing [plane]: plane-0 and plane-13 have 1.9001 units of ink clearance over 5.1718 units; requires 4; review required
- internal-spacing [plane]: plane-2 and plane-4 have 2.8386 units of ink clearance over 5.4565 units; requires 4; review required
- internal-spacing [plane]: plane-9 and plane-11 have 2.1778 units of ink clearance over 6.9121 units; requires 4; review required

### dragon-fruit → dragon-fruit-v2

Attempted three broader crown leaves, but that removed the distinctive spiky fruit shape. Preserve five crown points; their short returns need manual spacing review.

- internal-spacing [fruit]: fruit-1 and fruit-3 have 1.9133 units of ink clearance over 3.2057 units; requires 4; review required
- internal-spacing [fruit]: fruit-4 and fruit-6 have 1.9133 units of ink clearance over 3.2057 units; requires 4; review required

### adobe-cloud-logo → adobe-cloud-logo-v2

Attempted broader inner counters and shifted loop terminals. Preserve the interlocking cloud mark; the parallel diagonal loop cannot yet meet the four-unit ink gap without a substantial logo change.

- internal-spacing [outer / inner]: outer-0 and inner-0 have 2.8016 units of ink clearance over 3.7198 units; requires 4; review required
- internal-spacing [outer / inner]: outer-0 and inner-1 have 3.3438 units of ink clearance over 7.4183 units; requires 4; review required
- internal-spacing [outer / inner]: outer-1 and inner-1 have 3.31 units of ink clearance over 9.2693 units; requires 4; review required
- internal-spacing [inner]: inner-0 and inner-2 have 2.9613 units of ink clearance over 12.459 units; requires 4; review required

### picasa-logo → picasa-logo-v2

Attempted a roomier five-facet routing, but it changed the logo too much. Preserve the original facet arrangement; the narrow right rim band needs manual spacing review.

- internal-spacing [rim / right]: rim-2 and right-1 have 1.4197 units of ink clearance over 9.9 units; requires 4; review required
- internal-spacing [rim / bar]: rim-3 and bar have 1.4242 units of ink clearance over 9.8911 units; requires 4; review required
- internal-spacing [rim / bar]: rim-4 and bar have 2.5919 units of ink clearance over 7.1775 units; requires 4; review required

### vimeo-logo → vimeo-logo-v2

Attempted widening the looping counter and moving the returning stroke. Preserve the recognizable hooked V; its curved return still needs a spacing exception review.

- internal-spacing [mark]: mark-2 and mark-6 have 2.7957 units of ink clearance over 4.9148 units; requires 4; review required
- internal-spacing [mark]: mark-3 and mark-6 have 2.7891 units of ink clearance over 15.7768 units; requires 4; review required

## Review page

http://127.0.0.1:8000/gallery/solo-ai-full-set.html

Filter “Visible fixes” for the 203 new drawings, or “Spacing review” for the eight unresolved candidates. All original, earlier, cleanup and retained entries are searchable.
