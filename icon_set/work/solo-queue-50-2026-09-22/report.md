# Queue offset 50 — 22 September 2026

Outcome: 3 new validated exports; 6 references matched to existing reuse candidates; 1 unresolved layout. No prepared combinations, no skips for changed status, and no gallery-save failures.

Frozen page: 10 references, fetched from `http://localhost:8000`.
The exact response, source paths, editorial briefs and classification history are in
`queue.json`. Current status/brief snapshots are in `current-state.json`; reference
artwork is preserved in `references/` and rendered in `references.png`.

All ten sources had no explicit status entry when checked (the gallery's default
TODO state). Eight retained a saved container family. The queue also records
authoritative user decisions returning all ten references to TODO; those decisions
were preserved. No source was reclassified, split or marked skipped. No component
jobs were started. No gallery save was attempted, so there are no failed saves or
retry payloads. Existing source artwork and editorial briefs remain unchanged.

## Item accounting

| Source UUID | Subject | Result |
|---|---|---|
| `5dedab68-bdaf-44a3-8127-9ced04450355` | Wireless Screen Casting Icon | New SOLO48 original, valid with zero warnings; light/dark native review passed. Export verified in solo manifest. |
| `f9a37278-3937-439b-bbd9-5b384892713a` | Round Smart Watch | Existing `round-smartwatch` matches the saved reuse request; valid, zero warnings, native review passed, existing container export verified. No duplicate generated. |
| `01277467-c196-5c69-bba7-5182a13ec0bd` | Square Smartwatch Device | Existing `square-front-smartwatch-container` now supplies the front-facing square watch requested by the older brief; valid, zero warnings, native review passed, existing container export verified. |
| `9f86506b-13e1-43a2-99f9-4709e9b04ba0` | Square Smart Watch | Same front-facing reference and same verified reuse candidate as the previous item. No second duplicate generated. |
| `56184363-0fa8-5bb5-bae5-239ae516f66d` | Portrait Handheld Tablet | Existing `mobile-phone-device` matches the saved reuse request: upright rounded shell with lower bezel. Valid, zero warnings, native review passed, existing container export verified. |
| `dd4a0fad-d86e-5a86-ade8-4969df864353` | Square Face Smartwatch Device | Existing `square-smartwatch-device` matches the saved curved-strap reuse request; valid, zero warnings, native review passed, existing container export verified. |
| `7d8c35d4-e36c-4769-b5f9-af86d4cc16c2` | Stacked Paper Documents | New CONTAINER64 original `stacked-wavy-document-frames`; model valid with zero warnings, native light/dark review passed. Targeted build succeeded; export verified in the container manifest. |
| `10b617a1-d67b-49a8-9559-604c636a0780` | Empty Vertical Battery | Existing `empty-battery-level-indicator` matches the saved reuse request when rotated 90 degrees counterclockwise. Base model valid with zero warnings and existing export verified. No rotated production asset or source association was created. |
| `e8a716f5-9e73-4cb5-99f2-6b385806dd75` | Mailbox with Play Button | New CONTAINER64 original preserving the play triangle under the later whole-subject decision. Model valid with zero warnings, native light/dark review passed. Targeted build succeeded; export verified in the container manifest. |
| `33cfdb5e-48c9-567e-8e60-d450f8de2439` | Triple Seven Casino Slot Machine | Unresolved layout; no original generated and no validation/build success claimed. Preserve the whole subject and reuse `digit-7` three times. See below. |

Reuse candidates are verified existing artwork, not newly generated source-linked
deliverables. Their gallery references remain TODO; this run did not change their
saved reuse instructions or add new source associations.

## New originals and drawing findings

All new modules record `AUTHOR = 'gpt-6'`, an already-used author value, and preserve
the exact source UUID/path and source tags.

- **Wireless screen casting:** `HRECT_L`, giving the screen its wide silhouette.
  Lucide `airplay` informed the continuous rounded screen contour; the supplied
  reference informed the lower opening and centered triangle. The triangle is
  simplified to three straight sides. The screen's mirrored turns and triangle
  opening remain clear at 48 pixels in both themes. Source:
  `icon_set/model/icons/solo/wireless_screen_casting_icon_5dedab68_bdaf_44a3_8127_9ced04450355.py`.
  Export: `published/solo48/wireless-screen-casting-icon.svg`.
- **Stacked documents:** `HRECT_L`, fitting the horizontal layered silhouette.
  Lucide `files` informed the exposed rear-page contour. The reference supplies
  the defining wavy front edge. Hidden rear edges are omitted; the intentional
  offset remains, with no artificial symmetry. The wave and separated rear page
  read clearly at 64 pixels in both themes. Source:
  `icon_set/model/icons/container/stacked_paper_documents_7d8c35d4_e36c_4769_b5f9_af86d4cc16c2.py`.
  Export: `published/container64/stacked-wavy-document-frames.svg`.
- **Banded media frame:** `VRECT_XL`, preserving the upright frame, paired rails,
  broad bands and right-pointing triangle. Lucide `panels-top-left` informed
  rounded perimeter turns and real divider attachment nodes. The clipped lower
  outline is completed. The reference reads as a media frame; the editorial name
  is retained without inventing physical mailbox details. The bands and triangle
  remain distinct at 64 pixels in both themes. Source:
  `icon_set/model/icons/container/mailbox_with_play_button_e8a716f5_9e73_4cb5_99f2_6b385806dd75.py`.
  Export: `published/container64/mailbox-with-play-button.svg`.

See `validation.json`, `light.png` and `dark.png` for model-validation results and
native-size visual evidence. Hosting results are recorded in `hosting.json`.
The old probe IDs `plus`, `heart` and `check` do not exist in the current registry;
the corresponding isolated symbols `plus-sign-state-131`, `heart-state-63` and
`check-mark` were used instead. Stacked documents validate with plus and check;
heart returns review for contact with the front page. The media frame validates
with check; plus fails parallel spacing against the play triangle, and heart
returns review for rail contact. These composition findings do not change the
standalone icons' valid status and are not claims of visual composition approval.

## Slot-machine layout finding

The actual reference shows three side-by-side sevens, reel divisions, a cabinet
and a right-hand lever. No useful local Lucide slot-machine match was found.
The preferred `digit-7` exists in `icon_set/typeface/glyphs.json`; its original
ink size is 10 by 24, with stroke 4. Text must remain `777`, in that order, using
three instances of that glyph, never newly drawn numeral paths.

The initial upright layout budget keeps the lever and all three reel divisions.
Even at the documented minimum 12-pixel glyph height, each glyph's rounded
width is 6. A three-glyph row needs at least 26 pixels of ink width (18 plus two
4-pixel gaps) before adding any divisions, cabinet edges or lever. Including
both cabinet walls and their inner clearances already needs 42 pixels. The
widest rectangular SOLO48 envelope is only 44 pixels of ink width, leaving
insufficient width for the separate lever in that layout. A reduced layout
without reel divisions still has the cabinet/lever conflict. Removing the lever
or digits would weaken the requested whole subject, so neither was silently
omitted. A diagonal layout was also considered at the bounding-box stage:
the simplified cabinet plus lever needs at least about 50 by 28 pixels of
ink. Rotating that rectangular arrangement does not reduce its largest
axis-aligned dimension below 50 (at 45 degrees it is about 55). It therefore
does not fit a 44-pixel SOLO48 envelope. This is an unresolved design finding,
not a proof that every possible reconstruction is impossible.

No noncompliant original was placed in the registry, no glyph was redrawn, and
the source remains available for further layout work. There is no validator
failure report for this item because authoring stopped at the layout stage.

Final export verification: all three new SVG hashes match their manifest records; validation is valid with no errors or warnings. All 222 pre-existing container exports were retained. See `exports.json`. The shared output lock delayed the container build; a subsequent safe retry succeeded.
