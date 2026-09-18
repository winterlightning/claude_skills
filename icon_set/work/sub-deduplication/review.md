# Sub icon deduplication review

Scanned all 1,899 inventoried reusable 32px exports. Exact SVG comparison ignores titles, descriptions, metadata, formatting and unreferenced element IDs, but preserves geometry and paint attributes. SVGs containing references or styles are compared exactly.

The exact pass identified 157 aliases across 119 groups. Rendered non-text exports were then screened by silhouette similarity and related names. All 528 proposed comparisons were visually inspected in candidates-0.png through candidates-14.png. 253 comparisons were accepted as the same recognizable concept with differing proportions, drawing style or incidental details; the others retain separate identities for different glyphs, directions, states, structures or uncertain meaning. Overlapping accepted comparisons were consolidated into groups.

Final result: 367 aliases, 238 groups, 1,532 canonical entries. 775 of 1,757 side pairs changed. Canonical sub choices are shown in all 6,242 catalog pairings; 2,136 of these have remapped source artwork. Source UUIDs, authored models, source-reference relationships, original exports and approval records are retained. Main icons are not deduplicated.

Evidence is the current normalized export artwork actually used by the pairing system, freshly rasterized at 64px for comparison. This is a concept-equivalence review, not authored-model QA, source fidelity certification, symmetry approval or a geometric repair. No drawings were reauthored. Full model QA was not run. Visually different text glyphs were excluded from approximate matching; exact duplicate text artwork is included.

Decisions and exact reviewed artwork fingerprints are in ../../data/sub-deduplication-review.json. Canonical mappings are in ../../data/sub-deduplication.json, and the canonical inventory is ../../data/canonical-sub32.json. Reviewed mappings stop applying when either source artwork changes. Matching is conservative; the similarity screen is not a proof that every possible semantic synonym was found.

The report gallery is ../../dist/gallery/sub-deduplication.html. All 1,757 side previews were rebuilt with the unchanged combination engine. Targeted tests cover metadata-aware equality, native-sub preference, pair replacement, duplicate choices, original reference retention, idempotency, stale pair rejection and expiration of reviewed mappings. Existing combination and catalog tests also pass (15 tests total).

Run `python3 -m icon_set.scripts.deduplicate_subs` after changing exports; pair refresh and export normalization invoke it automatically. Then rebuild combination previews when retained artwork changes. Sub-scaling inspection was regenerated after this migration. Original aliases remain as compatibility files and should not be deleted while old external links may reference them.
