# Solo reuse and centered-container review

Scope: the remaining 750 of the original 850 references. The first 100 retain their earlier audit.

The original 205 solos have 86 ready reuse matches, 75 adaptation targets, 16 container-to-solo conversions and 28 references requiring new solo briefs.

The centered-content recheck moved another 177 references into solo, giving 382 solo, 365 container combinations and 3 side combinations. The user-listed examples are all solo.

Across the 382 solos, 103 reuse existing solo artwork, 157 adapt existing artwork, 16 convert existing containers and 106 point to new solo briefs. Shared concepts are consolidated into 258 distinct authoring handoffs: 100 new concepts, 150 adaptations/conversions and 8 repairs to existing source-matched drawings.

- `index.html`: filterable original/artwork comparison.
- `review.json`: full 750-source classification and reuse map.
- `authoring-references/manifest.json`: standalone SOLO48 manifest, with complete source filenames.
- `solo-briefs/`: finalized briefs and 320/48 px previews.
- `authoring-plans.json`: existing targets, operations, source hashes and shared references.
- `verification.json`: saved-state and coverage checks.
- `before.json`, `before-save.json`: rollback evidence.

All 750 scoped sources have saved reference briefs. The 382 solo mappings are saved in the local gallery state; unrelated decisions and briefs were verified unchanged. No generation jobs were queued and no icon models were authored.

Eight manifest IDs intentionally point to existing source-matched models for repair. Every other proposed ID was checked against both the published catalog and the model registry. Source copies are byte-identical. Candidate searches cover the published solo/container inventory and unpublished models linked to the same source UUIDs; a “new” result means no suitable match found in that checked inventory.
