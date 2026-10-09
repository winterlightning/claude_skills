# Import a rejected-icon visual review

`import_rejected_review.py` converts an existing visual review into separate,
source-preserving correction worklists. It is an offline, files-only handoff:
there is no apply mode, network client, database access, image generation or
review-status mutation. Every imported record remains `pending_human_review`.

The importer accepts the parent-confirmed `pictographic-rejected-visual-review/v1`
schema. The full 379-record export has **not been imported or verified** in this
change because its Library download was unavailable. The checked-in fixture is
one minimal parent-supplied example, with its provenance labeled explicitly;
test-generated records are synthetic, not additional reviewed findings.

## Import and verify the inventory

Run from the repository root using Python 3.10 or newer:

```sh
python3 -m icon_set.scripts.import_rejected_review \
  --file /path/to/all379.json --out work/rejected-review-20261009 \
  --expect-count total=379 \
  --expect-count split_into_components=139 \
  --expect-count container_combinations=90 \
  --expect-count side_combinations=49 \
  --expect-count other_recommendations=240 \
  --expect-count unresolved_splits=0 \
  --expect-count retain_family_review=235 \
  --expect-count author_new_drawing=2 \
  --expect-count recategorize_family=2 \
  --expect-count unknown=1
```

These are expected counts supplied with the review, not results from running
the full export. A mismatch aborts before writing. Only
`recommended_action == "split_into_components"` routes a record into a split
worklist: other recommendations can also carry `combination_type`.

The output contains:

- `source-review.json`: byte-for-byte input, including metadata and evidence.
- `manifest.json`: source SHA-256, counts by action and worklist, and filenames.
- `container_combinations.json`: container + symbol split recommendations.
- `side_combinations.json`: main + side-sub split recommendations.
- `other_recommendations.json`: retain-family, drawing, recategorization, unknown
  and unrecognized actions, preserving their original briefs and feedback.
- `unresolved_splits.json`: split requests without a supported combination type.
- `verified-references.json`: exact verified reference IDs with every use, its
  original matched key, match kind and outstanding checks.
- `README.md`: inventory and review instructions.

An identical import is a no-op. A differing existing bundle is never overwritten;
choose another output directory so human edits survive. Staging failures leave
no partial destination. No credentials or production environment are needed.

## Input contract

The root is `{ "metadata": { "schema":
"pictographic-rejected-visual-review/v1", ... }, "records": [...] }`.
Each record needs a unique nonempty `key`, a nonempty `recommended_action`, and
`recommendation_only: true`. The importer preserves every additional field.
`components`, when present, must be an array of objects; nested `components`
arrays are traversed with their full component paths retained.

The review also carries `index`, `source_reference_id`, current family/name/category,
`current_state`, `current_effective_svg_sha256`, `combination_type`, proposed
family/category, `reason_wrong`, `confidence`, `exact_new_drawing_brief`,
`existing_human_review`, and `evidence_urls`. Missing source references, invalid
revision hashes and non-rejected source states become explicit review issues.
Neither confidence nor a proposed family grants authorization to change an icon.

Components retain `role`, `visual_description`, `required_family`, `canvas_size`,
`match_status`, `reference_id`, `matched_key`, `candidate_reference_ids`,
`reference_entry_kind`, `match_kind`, `requires_role_adaptation`, `limitation`,
`absence_proven`, `assembly_readiness_verified`, and `evidence`. Only an explicit
`verified_existing` match with a nonempty reference ID enters the reuse index.
The verification source is the supplied review; the importer does not claim an
independent lookup or visual check. Candidate IDs are never selected, an
unverified match does not establish absence, and functional equivalents retain
their contour limitations. The original nested component tree stays intact.

Container roles are `container` and `symbol`. Side roles are `main` and `sub`
(the display alias `side_sub` is recognized only for side combinations). Other
role labels or extra/nested parts stay flagged for review; symbols never become
side subs through normalization. An explicit assembly-readiness claim still
does not bypass human review or authorize a write.

## Review through the existing tools

1. Inspect source pixels and component reference pixels using the original
   evidence. The importer does not inspect images or make new visual decisions.
2. Use the emitted **GET-only** checks for `/api/icon?key=...` and
   `/api/review-detail?icon=...`. Compare the current SVG SHA-256 and review state
   against the saved record; reconcile a changed drawing before proceeding.
3. Inspect existing `/api/combinations` and its parts. Reuse a verified reference
   identity only after resolving contour differences and any role adaptation.
   Missing geometry, ambiguous matches, nested splits, placement and assembly
   readiness remain reviewer decisions.
4. Keep corrections in the ordinary review workflow until separately authorized
   and supported by the API. No payload here marks an icon ready, approved,
   restored or complete, or claims it in the production fix queue.

Two current API limitations prevent blindly submitting the review as a batch:

- `POST /api/reject-combination` uses the legacy `brief_queue.validate_split`
  contract: container + **sub**, not container + symbol. It also returns an
  existing active split unchanged. Do not restore/reject to force a rewrite;
  restore changes review state and removes feedback.
- `POST /api/combinations/pair` creates **side-only** `draw:<id>:<role>`
  placeholders. It does not accept verified component reference IDs, and
  `/api/combinations/parts` picks an icon/layout/draw name rather than replacing
  the part's reference identity. Do not silently substitute those placeholders
  or send ignored reference-ID fields.

Consequently split worklists carry `reference_mapping_requires_api_support`.
A reviewed API extension or dedicated correction operation is still needed
before applying reference mappings. Existing `queue_brief.py --files-only` can
be used later for a supported, explicitly reviewed component brief; this importer
does not call its queueing mode or translate a symbol into the legacy sub family.

Both deployed Worker URLs, including `pictographic-review-next`, share production
storage according to `cloud/README.md`. Use isolated fixtures for testing.

```sh
python3 -m unittest icon_set.tests.test_import_rejected_review
```
