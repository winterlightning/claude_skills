# Sub-profile migration

Completed the retained inventory of 1,532 artworks as independent SUB32 Python models: 1,313 created and 219 existing models reused. The original 48px models remain independently editable. The relationship table contains 1,544 source links, including shared references to the same deduplicated sub model.

All 332 text models use a natural-width canvas and a measured ink height of 32. Coordinates snap to the integer grid; existing artwork validation findings are retained. The horizontal ellipsis scales its dots and spacing together to 256 × 32, using 32-unit round caps because point-only glyphs have no centerline height. This narrow exception is rejected for non-point geometry.

All 1,757 side pairs point to sub models and their preview caches were refreshed. All 6,242 catalog rows use the migrated sub choices where generated options exist. The canonical inventory, aliases and source IDs preserve deduplication and provenance.

Artwork QA: 721 pass, 753 fail, 58 require review. The 811 non-passing models remain editable review drafts outside the validated release. Conversion does not constitute visual approval or repair of every inherited drawing. See `qa.json` and the searchable `../../dist/gallery/sub-profiles.html` for findings and source/model comparisons.

Validation: 20 focused migration, deduplication and ink-sizing tests passed; stroke editor UI tests passed. Earlier broader targeted checks passed 47 tests. Final integrity checks cover unique models, Python source files, all 332 actual text ink heights, profile-link targets, active pairing family/IDs, catalog choices, current QA SVG hashes and all preview fingerprints. A broader validator run encountered three existing fixture failures involving the missing approved `minus` FREE-keyshape record. A full suite was not completed; other existing schema tests have unrelated float-coordinate failures.

Relevant maintained entry points: `migrate_sub_profiles`, `activate_sub_profiles`, `sub_profile_report`, and `profile_links` in `icon_set/scripts`. Migration is idempotent and preserves existing model edits unless explicitly run with `--rewrite-generated`. Source snapshots and mappings live in `icon_set/data/sub-profile-*.json` and `icon-profile-links.json`.
