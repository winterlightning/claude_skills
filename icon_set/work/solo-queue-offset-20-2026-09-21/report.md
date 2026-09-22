# Solo queue audit — offset 20

Requested offset: **20**. Returned count: **10** (total at fetch: 91).
Fixed page fetched once successfully from `http://localhost:8000`; no replacement items or next page fetched. Each source status and saved brief was read immediately before intake; snapshots are beside this report. All ten status records were absent (default TODO), and saved reference families/briefs were available. Original reference SVGs were rendered and visually inspected. No original artwork, classification, editorial brief, or component brief was overwritten.

## Outcomes

| Source UUID | Subject | Outcome |
|---|---|---|
| a795a20f-a600-407a-afe4-25fbc99203fd | Longship with curved sail and three oars | Valid, zero warnings; light/dark native review passed. Exported. |
| 2f1ae9d4-7c42-400d-8760-d69f1f5f0abd | Blood drop with ring | Existing editorial hold preserved. Ring meaning remains ambiguous; neither a physical relationship nor modifier can be established. No drawing or split. |
| 770b8052-e66d-401b-ae0d-9284719da14f | Rounded horizontal subtraction mark | Deferred to the saved, authoritative **sub** family. It is not a SOLO48 subject; current saved brief explicitly defers to icon-sub. No state change or drawing. |
| 8c0da42a-e577-481a-a50e-84f0e8648aae | Four-stud toy brick | Revised existing draft with a thickness edge. Valid, zero warnings; visual approval failed because it still resembles a button/die and loses protruding-stud perspective. Not exported. |
| 6e501462-4458-4ee8-918b-3b9b1c8dded4 | Left profile with brain | Existing draft revalidated: valid, zero warnings. Brain is an intrinsic organ, not a modifier. Visual approval remains unresolved: lobes and descending extension lost. Draft preserved, not exported. |
| 0231a044-ecb1-470e-bcc3-8a45ccdc5d4a | Right profile with folded brain | Existing draft revalidated: valid, zero warnings. Visual approval remains unresolved: folds and stem reduced to an indistinct small loop. Draft preserved, not exported. |
| 951456f0-7a11-4ecc-b29c-400594778716 | Arched speedometer | Valid, zero warnings; light/dark native review passed. Exported; manifest entry and SVG hash verified. |
| 9129cb90-67e3-45db-ba5e-bf44ad6e9221 | Domed columned building | Valid, zero warnings; light/dark native review passed. Exported; manifest entry and SVG hash verified. |
| 4216f978-fc24-48e8-8c36-261313bcdf26 | Oil pump jack | Repaired false attachment declarations by using actual shared endpoints. Valid, zero warnings, but horsehead opening and upper tower opening remain pinched. Not exported. |
| b2153799-7259-4ede-84eb-5855c5aaae3b | Open laurel wreath | New draft unresolved. Mirrored six-leaf layout and rebalanced lower pair still fail spacing and exact envelope. Not exported. |

No verified combinations were found or prepared; no combination saving was attempted, so there are no failed saves or retry payloads. No item was found already generated or actively assigned in the status response. The sub-family defer is separate from a changed TODO status.

## Passing designs and evidence

- **Longship:** SQUARE (6,6)–(42,42) supports a broad sail over shallow hull and all three diagonal oars. Source provides curved sail, hull and count; Lucide `sailboat` original and atoms provide contour/attachment principles. Omitted tiny mast projection and ornamental raised prow. At 48 pixels the curved sail, hull opening and three oars remain legible in both themes. Source: `../../model/icons/solo/longship_with_curved_sail_and_three_oars_a795a20f_a600_407a_afe4_25fbc99203fd.py`. Output: `../../../published/solo48/longship-with-curved-sail-and-three-oars.svg`.
- **Speedometer:** HRECT_L (4,8)–(44,40) matches the broad arched dial. Source provides closed base, ticks, hub and diagonal needle; Lucide `gauge` original and atoms inform minimal needle/dial hierarchy. Five detached ticks reduced to three attached ticks; small hub moved upward for certified clearance. Both themes retain clear needle direction and dial silhouette. Source: `../../model/icons/solo/arched_speedometer_951456f0_7a11_4ecc_b29c_400594778716.py`. Output: `../../../published/solo48/arched-speedometer.svg`.
- **Building:** SQUARE (6,6)–(42,42) balances the dome, cornice and base. Source provides dome and classical front; Lucide `landmark` original and atoms provide detached column rhythm. Thick cornice/base outlines reduced to single strokes; three evenly spaced columns retained. Symmetry and negative space survive both themes. Source: `../../model/icons/solo/domed_columned_building_9129cb90_67e3_45db_ba5e_bf44ad6e9221.py`. Output: `../../../published/solo48/domed-columned-building.svg`.

Authorship uses the existing `gpt-6` value. All UUIDs and supplied source paths are retained in the Python originals. Light/dark contact-sheet evidence rendered through `contact_sheet.py`, then rasterized at scale 1 for true 48-pixel native views, is stored alongside this report.

## Unresolved geometry and visual details

- Brick: tried rounded body with thickness strip, which had exact-distance curve warnings; straight body and shared divider certified the spacing, but recognition remains insufficient. Four studs were preserved; replacing them with two would change the subject. Lucide `toy-brick` was inspected.
- Heads: inspected both actual source renders, existing draft renders and `human_ref/user.svg`. Existing drafts document Lucide brain construction. Did not force a container split for anatomical organs or remove the brain to obtain completion.
- Pump jack: beam/tower, ground/legs, brace/legs and horsehead/beam now share actual endpoints; reduced lattice to one brace. No useful Lucide oil-pump match. Validator success does not resolve the tiny horsehead slit or tower opening.
- Wreath: three pointed leaves per side, mirrored about x=24; crossing stem tips omitted to budget space. Rebalancing the lower pair removed its central collision, but adjacent leaves remain only 3.05–3.33 units apart on centerlines (required 8). Ink bottom 43.75 misses SQUARE bottom 44 by 0.25. No useful Lucide wreath match. Native light/dark renders confirm that the crowded loops also lose pointed-leaf character. Further reduction risks losing the wreath identity; keep as a draft for redesign.

Validation descriptions are saved separately beside this report. Shared build output was busy during initial gauge attempts; retries wait for the lock without interrupting other work. No full-library build, metadata seeding, commit or publish was requested or performed.

Final export verification: all three passing icons are present in the solo manifest, marked valid with zero warnings, and their emitted SVG hashes match the manifest. See `export-verification.json` and `generated-native.png`.
