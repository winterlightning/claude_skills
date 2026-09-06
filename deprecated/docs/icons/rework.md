# Normal-Icon Rework Adapter

Use this adapter for a local manifest-based rework pack or a symbol-library JSON
payload with `kind: "rework"`. Local output does not authorize a remote upload.
Start with the [normal icon skill](SKILL.md), then follow the shared composition,
script, QA, and repair sequence in [the icon pipeline](../shared/icon-pipeline.md).
This page adds the brief contract, source-priority ladder, concept review, and
controlled upload. Choose the correct lane below; local pack metadata is not
required to satisfy the URL-payload-only field contract.

Use the [single-SVG adapter](../shared/icon-execution-steps.md) for one directly
supplied SVG and the [SVG batch adapter](../shared/icon-batch-execution-steps.md)
for a set of SVGs staged by hand.

Both lanes normalize a concept name, minimal description, and icon type/profile.
User references are optional in the shared workflow: no-reference items use the
brief directly; supplied SVGs are detected, while PNGs or other files require
format-appropriate inspection. The helpers below have narrower input contracts
and do not convert arbitrary references into SVGs. Every intake joins the same
profile-informed design and distance → holes → keyshape repair loop.

## Local manifest pack lane

Use this lane when the user selects downloaded pack folders containing
`manifest.json`, per-symbol prototype/reference files, and manifest `upload`
paths. Do not refetch a category or rewrite the original manifest, prototypes,
pack README or uploader. A pack's `upload` field is a local delivery destination,
not authorization to POST. `wrong` is status metadata, not a filter when the
user asks to rework all symbols in the selected packs.

The current helper requires a local `files.prototype` SVG and a safe relative
`upload` destination for every entry. It builds the entire manifest, not a
filtered subset. This SVG requirement belongs to this helper, not to icon
generation generally. If the user selects only some symbols, use the explicitly scoped
single/batch pipeline rather than silently widening the request or editing the
original manifest. The URL lane's source-priority ladder does not run here.

From the repository root:

```bash
python3 core/rework_pack.py inspect <pack-folder>
python3 core/rework_pack.py prepare <pack-folder>
```

`prepare` analyzes the pack prototypes, writes per-symbol detection JSON/plots,
and creates `prototype-contact-sheet.png`. Inspect the manifest's exact symbol
set and existing files. Use
`minimal_description` as the feature brief when present, the stable `name` (or
`concept` when provided) as its readable label, and the supplied prototype to
resolve shape meaning. Unlike the payload lane, a local pack may lack `concept`.
Do not invent required features from its list of downstream icon usages.
Record disagreements or an ambiguous essential cue instead of guessing.

Apply the shared [extracted-prototype rule](../shared/icon-rules.md#extracted-prototypes-restore-missing-geometry):
restore contours or parts missing because of clearance around an object in the
larger source icon. Preserve prototype files, not those extraction artifacts;
retain genuine openings and overlaps required by the new composition.

For each selected symbol:

1. Review its brief and prototype/source, determine the icon type, and read that
   profile before planning the design. Detect the chosen SVG and record its
   source origin, required cues and any intended simplification.
2. Search the bundled Lucide corpus, inspect useful original/debug pairs, and
   record names, reasons and applied principles in `sourceAnalysis.lucideReferences`.
3. Author `editable/<icon-name>.json` in the pack, matching the JSON `name`,
   using schema-version-2 `elements`, the selected profile, and complete evidence.
   This rework lane defaults to normal; generation packs may route another role
   explicitly through [GENERATE_SKILL.md](../GENERATE_SKILL.md).
   Follow [R8 naming](../shared/icon-rules.md#symbol-ids-and-variants):
   retain the normalized `sym-<id>` prefix in the base name and every requested
   variant; keep the original ID in metadata and manifest destinations unchanged.
   Set `sourceAnalysis.symbolId` to the manifest `sid`; each pack symbol must
   have exactly one chosen editable source in this folder. Keep exploratory
   variants outside the builder's final `editable/` folder. New contours are
   geometry, not requests to add registry entries.
4. Emit with the canonical emitter, then run the shared structural, grid and
   declared-overlap prerequisites and the distance → holes → keyshape gates.
   A diagnostic build is not acceptance. Repair through editable geometry;
   after each edit re-emit, recheck prerequisites, and restart at distance.
   Review the output at the configured profile's native canvas/stroke; keep foreign-grid sources
   unchanged as evidence. Record `sourceAnalysis.visualReview` for the exact
   emitted canonical SVG:

```json
"visualReview": {
  "status": "pass",
  "shipSize": 48,
  "notes": "Describe the actual recognition, balance, joins and spacing review.",
  "geometrySha256": "SHA-256 of the reviewed native SVG bytes"
}
```

`shipSize` is a compatibility field name: it records the resolved native canvas,
not a half-size export. The JSON above illustrates the built-in 48px normal
default; use the actual configured value. Container previews still follow their
separate workflow.

Obtain the hash with `shasum -a 256 <pack-folder>/output/<name>.svg` after
inspection; a placeholder or stale hash cannot pass. Geometry changes require
fresh emission and review, not copying the previous verdict. The local
Lucide-guided runner also requires useful valid reference records; if no relevant
reference can be found, report that evidence gap rather than inventing one.

Historical half-size review evidence is stale under the native-size contract.
If an old source is explicitly selected for migration, re-emit it at the native
dimensions, inspect that actual SVG, and record its new hash and findings. Never
turn a 24px verdict into a 48px verdict by changing `shipSize` alone. Existing
ignored rework packs are historical artifacts and are not rebuilt or edited
automatically when the rules change.

5. Run the local build to emit, validate and prepare the reviewed sources:

```bash
python3 core/rework_pack.py build <pack-folder>
```

`build` processes existing editable JSON; it does not infer or author the
symbol's meaning. It emits the canonical native SVG and same-size compatibility
alias and reruns required QA, including distance → holes → keyshape, then copies
passing, hash-reviewed native SVGs to the exact relative paths declared by the manifest's
`upload` fields. Its `review.html` gallery and `contact-sheet.png` support visual
review. Inspect every canonical output at its native size;
numerical success alone does not prove semantic or visual quality. Keep explicit
review findings and any corrections with the pack.

`--skip-qa` emits diagnostic drafts, exits nonzero and never publishes manifest
delivery files; do not report it as a completed rework. A missing/failing symbol must stay visibly
blocked in the report; no silent partial completion. Rebuild after source edits
and inspect the refreshed evidence. Preserve original inputs throughout.

Require all three gates to pass on the same final SVG bytes and resolved profile.
Read failure summaries, hole/pinch zones, and actual versus expected keyshape
bounds before repairing. Reviews, checker errors, and missing or stale evidence
block delivery; never distort an intended connection or relax the profile merely
to obtain a pass.

Each build writes fresh `qa/<timestamp>/` evidence plus `rework-results.json`,
`review.html` and `contact-sheet.png` at the pack root. Prior delivered files are
not proof that the current run passed; inspect the current per-symbol results.
The local lane delivers editable sources, canonical native SVGs, per-symbol
manifest delivery SVGs, QA and native-size review artifacts. Same-size filename
aliases are compatibility artifacts, not additional required resolutions. It does not execute `upload.py`.
The pack runner does not deliver containers without separate filled-preview
evidence; use the container skill and manual profile-aware pipeline for that case.
If the user later explicitly authorizes uploading, inspect the local uploader's
dry-run, exact destinations and files first. Do not substitute the payload
lane's filename convention for this pack's verified manifest destinations;
the native geometry stays 1:1 in either case.

## URL and payload lane boundary

| | SVG lanes | Rework lane |
| --- | --- | --- |
| Input | one or more selected SVGs | one `kind: "rework"` JSON payload |
| Design brief | name + description, or a recorded interpretation of a legacy SVG-only request | `concept` + `minimal_description` |
| Reference intake | supplied SVG | optional SVG resolved through the priority ladder below |
| Acceptance | brief/reference review, then the shared three gates and native review | brief compliance, then the same gates and reviews |
| Delivery | files | files plus an optional approved POST |
| Uploaded artifact | none | Configured normal-native SVG; the staged manifest retains its `<name>-design.svg` compatibility alias |

The URL/payload lane produces the configured `normal` role only (built-in
48px/4px defaults), even though the generic pipeline supports custom profiles. Do not silently
upload a sub icon, container preview, or another profile as a symbol final.

## R0 — the brief outranks the drawing

The payload's `wrong: true` is the library's claim that the current drawing is
wrong. The drawing remains useful geometry evidence, but it is not the statement
of what the icon should depict.

- `minimal_description` is the authoritative subject and feature budget.
- `concept` is the authoritative name.
- The staged SVG is evidence of arrangement and craft, never authority over
  meaning.
- When drawing and brief disagree, the brief wins and the difference is recorded.
- Do not reproduce a rejected drawing faithfully merely because it is clean.

## R1 — judge before remaking

Before mapping a symbol sourced from `files.final` or `files.prototype`, compare
that drawing with the brief and record `sourceAnalysis.briefCompliance`:

| Verdict | Meaning | Required action |
| --- | --- | --- |
| `correct` | Subject, every required cue, and feature budget already match | Rebuild as traceable editable geometry; do not redesign merely to justify the rework; report disagreement with `wrong: true` |
| `partial` | Subject is right but a required cue is missing or excess detail breaks the budget | Keep compliant parts and remake the difference |
| `wrong` | Subject or identity-bearing form is wrong | Remake from the brief |

Record evidence, not only a label:

```json
"briefCompliance": {
  "verdict": "partial",
  "requiredFeatures": [
    "rectangular frame",
    "one panel shifted left",
    "clear opening on the right",
    "one small handle"
  ],
  "present": ["rectangular frame", "clear opening on the right"],
  "missing": ["one panel shifted left"],
  "excess": ["second chevron mark"],
  "reason": "panel offset absent and handle count exceeded"
}
```

Enumerate the brief's required features and account for each as present or
missing; list every unauthorized feature as excess. Excess detail is a real brief
failure even when the geometry passes every numeric gate.

A `correct` prototype verdict means its subject and features match. Prototype
geometry is still foreign-grid and must be recomposed as exact editable elements.
It does not require copying extraction cutouts: apply the shared
[prototype reconstruction rule](../shared/icon-rules.md#extracted-prototypes-restore-missing-geometry)
and record restored geometry in the source mapping. If the artifact hides a
required cue, record that cue as missing and use `partial` rather than `correct`.

## Payload field contract

This section applies only to the URL/payload lane. Only these fields decide what to make.

### Required per symbol

| Field | Role |
| --- | --- |
| `sid` | Stable identity and upload URL key |
| `concept` | Subject and readable part of the icon name |
| `minimal_description` | Binding subject, required cues, and feature budget |
| `upload_url` | Destination for an approved design-SVG POST |

### Optional reference candidates

| Field | Role |
| --- | --- |
| `files.final` | Candidate 1: current shipped SVG |
| `files.reference_svg` or chosen `references[].path` | Candidate 2: chosen SVG reference |
| `files.prototype` | Candidate 3: earlier foreign-grid SVG |

The staging helper resolves SVGs only. Other user-supplied file formats remain
optional evidence for format-appropriate intake; do not rename a PNG to `.svg`
or pretend the helper detected it.

### Context only

| Field | Restriction |
| --- | --- |
| `description` | May disambiguate the brief; never add features the brief omitted |
| `name`, `icons`, `name_source` | Labels only; `concept` defines the subject |
| `wrong`, `had_final`, `instances`, `n_icons` | Status metadata, not a feature list |
| `pictoicon_url` | Landing page, not source geometry |

### Required at batch level

| Field | Role |
| --- | --- |
| `kind` | Must equal `"rework"` |
| `label` | Batch and default folder name |
| `symbols`, `count`, `skipped` | Authorized scope |
| `api.base`, `api.label` | Upload host and variant label |
| `api.path`, `api.method`, `api.body` | Raw UTF-8 SVG POST contract |

Reading another field to decide what to draw is a process error. In particular,
the full `description` often describes the busy drawing being replaced.

## Source-priority ladder

Resolve at most one SVG drawing per symbol, highest available first:

```text
1. files.final          current shipped icon       → detect and remake
2. files.reference_svg chosen reference            → detect and remake
3. files.prototype     earlier foreign-grid icon   → detect and remake with brief
4. none                name + minimal description → design directly from the brief
```

Rungs 1–3 produce one file in `sources/` for detection. Rung 4 intentionally has
no source SVG, detection report, or preflight plot. Both intakes enter the same
canonical design and verification pipeline after input analysis.

The prototype is normally a 26u viewBox with 1.5 stroke and a literal color. Use
it for subject, part count, and arrangement, never for canvas, stroke, or exact
proportion. Read it together with `minimal_description`; the brief wins.

When no drawing exists, derive the subject, required parts, arrangement, and
relationships from `concept` and `minimal_description`. Read the normal profile,
choose a keyshape and construction idea, and author editable geometry directly.
Do not fabricate a reference SVG or source detector IDs. Internal Lucide
original/debug reference study still informs style in both intake modes.

Carry `sourceOrigin` (`final`, `reference`, `prototype`, or `brief`) from
`batch.json` into `sourceAnalysis` and the delivery notes.

## Lane sequence

```text
fetch and stage
→ read briefs
→ normalize each brief and optional reference intake
→ detect/triage actual SVG references; analyze no-reference briefs directly
→ record reference R1 verdict where applicable and each symbol's feature plan
→ inspect relevant reference pairs and record construction principles
→ profile-informed composition and prerequisites
→ distance → holes → keyshape → native-size visual review
→ concept review, then family review
→ upload dry-run
→ requester confirmation
→ POST
→ deliver report
```

Resolve each symbol's brief, any reference R1 verdict/mapping, and construction choices
before composing it. Continue safe work on unaffected symbols. Do not POST
before the upload stage and explicit confirmation.

## Fetch and stage

Run from the repository root:

```bash
python3 core/fetch_rework_batch.py --cat "Building Construction"
```

Alternatives:

```bash
python3 core/fetch_rework_batch.py --url <download-wrong-icons-json-url>
python3 core/fetch_rework_batch.py --json sample_response.json --out work/rework-local
```

Use `--overwrite` only to re-resolve sources deliberately. The script writes:

```text
work/rework-<label>/
├── manifest.json
├── batch.json
├── briefs.md
├── upload.py
├── sources/
├── detection/
├── editable/
├── output/
└── qa/
```

The staged folder is the entire subject-evidence scope. Relevant bundled Lucide
references may inform construction, not subject meaning. Do not inspect unselected
user variants or fetch another category into the same folder. Icon names are
`<sid-kebab>-<concept-kebab>`; the staging script stops on a collision because two
identical names would overwrite output and upload state.
Use the exact staged `iconName` for the selected output. Apply the shared
[R8 naming rule](../shared/icon-rules.md#symbol-ids-and-variants) to any
separately requested variants without changing staged names or upload mappings.

## Read briefs and verify sources

Read `briefs.md` completely before mapping. For each symbol:

- confirm `concept` names a drawable subject;
- enumerate the exact feature budget in `minimal_description`;
- confirm the resolved source origin;
- if a source exists, note whether it appears correct, partial, or wrong, without finalizing
  R1 until it is rendered and compared carefully.

Open every actual staged source and confirm it renders. Read `batch.json` →
`sourceCounts`; a batch dominated by `prototype` or `brief` sources needs more
design judgment and that fact belongs in the delivery notes.

For every `sourceOrigin: "brief"`, use direct brief analysis and leave SVG-only
source/detection evidence absent; the absence is intentional, not a missing
acceptance report. If another source must be resolved, rerun `fetch_rework_batch.py` with
the same `--out`; existing files remain unless `--overwrite` is explicit.

## Detect and triage

Run detection only on actually staged SVG references. Skip this stage when the
batch has none; mixed batches still author their no-reference items directly.

```bash
BATCH=work/rework-building-construction
python3 core/batch_detect_svg_shapes.py \
  "$BATCH/sources" \
  "$BATCH/detection"
```

Pass `--overwrite` when a staged source changed. Apply the triage depth from the
[SVG batch adapter](../shared/icon-batch-execution-steps.md): rendered source for `ready`,
source + plot + direct path measurement for `review-required`, and resolution or
reported omission for `failed`.

Foreign-canvas references and prototypes often require review. That is expected;
measure their path data instead of reading proportions from the plot.

## Map every symbol against its brief

Before composing each symbol:

1. Enumerate the brief's required cues; render and triage a source only when one exists.
2. For an actual reference, finalize R1 `briefCompliance` against `minimal_description`.
   For no-reference work, record the semantic feature plan without inventing a
   source verdict.
3. Record `briefDiff` for every missing or excess reference feature, when applicable.
4. Map every identity-bearing reference element, or map planned brief features
   to editable IDs for no-reference work. Unauthorized excess reference parts
   are `omit` with a brief-based reason.
5. Record relationships and painted-clearance checks.
6. Resolve every applicable detector `manualReview` item semantically.

The editable source carries `sid`, `concept`, `brief`, `sourceOrigin`,
reference-only `briefCompliance`/`briefDiff` when applicable, mappings,
relationships, and spacing checks under `sourceAnalysis`. Also retain chosen
`lucideReferences` and their construction
principles. Shared family decisions belong in batch notes, not an atom request list.

## Inspect references, compose, and run QA

Use the reference-selection and common-construction review from
[the SVG batch adapter](../shared/icon-batch-execution-steps.md). Keep original
SVGs authoritative and use debug segments for geometry evidence. Recompose each
subject with directly editable elements; no registry extension, fixed element
count or compulsory reuse threshold is part of acceptance.

Then compose in manageable checkpointed groups and run every normal-profile stage in
[the icon pipeline](../shared/icon-pipeline.md): emission, structural baseline,
grid, declared overlap, then distance → holes → keyshape and native-size review.
Store editable JSON in `$BATCH/editable` and output in `$BATCH/output`.

After every repair, re-emit both aliases, recheck prerequisites, and restart at
distance. Final distance, hole, and keyshape reports must all freshly pass for
the same geometry and resolved profile. Missing/stale evidence, checker errors,
or unresolved reviews block completion; investigate ambiguous curved joins
instead of distorting them or lowering thresholds. Do not upload an icon
whose automated report, mapping, or visual review is incomplete.

## Perform concept review, then family review

The shared workflow always checks the intended meaning; this lane records it
explicitly against the payload. Put each finished icon beside its `concept` and
`minimal_description` and answer:

1. Reading only the brief, would you draw this icon?
2. Seeing only the icon, would you name it this concept?

A “no” means the rework failed even if every geometry checker passed.

Then verify the output against R1 when a reference was judged:

- `wrong` or `partial`: the output differs from the source exactly where
  `missing` and `excess` said it should.
- `correct`: the output remains faithful to the intended subject and features,
  not extraction artifacts, and the delivery report explains why the library's
  `wrong` flag appears mistaken. Any contour reconstruction is documented.

For every intake, including no-reference items, every required feature must be
visible at the configured normal native size and no unauthorized feature may appear.

Finish with the configured-normal batch family review: one native-size contact sheet,
consistent optical weight, motifs, gap rhythm, stance, margins, and no accidental
near-duplicates.

## Dry-run and approve the upload

The maintained production uploader is the repository-root
[`upload.py`](../../upload.py). [`core/fetch_rework_batch.py`](../../core/fetch_rework_batch.py)
copies it into each staged batch (unless `--uploader` or `REWORK_UPLOADER` selects
another script), and [`rework_opus.sh`](../../rework_opus.sh) runs that batch-local
copy. Updating the root uploader does not update existing batch copies.

`upload.py` reads `manifest.json` beside itself, so run the batch-local script
inside the batch folder. Its destination is `--base` when supplied, otherwise
`manifest.json` → `api.base`; the production origin is
`https://symlib.pictographic.ai`.
The staged manifest points each symbol's upload to its `-design.svg`
compatibility alias. It has the same configured native geometry and stroke as canonical
`<name>.svg`; do not create a reduced companion.

Every upload POST must send these headers:

```text
Content-Type: image/svg+xml; charset=utf-8
User-Agent: symlib-rework-upload/1.0
```

The explicit agent string avoids the production Cloudflare rejection of the
default `Python-urllib` agent (`403`, error `1010`). Before uploading an older
batch, inspect its actual `upload.py` and carry over the header patch if missing,
preserving any batch-specific changes. Do not re-stage the whole batch merely
to refresh this header. `--force` changes server canvas/keyshape validation; it
does not fix an HTTP client-identification rejection.

Always dry-run first:

```bash
cd "$BATCH"
python3 upload.py --dry-run
```

Confirm the dry run shows:

- exactly the symbols that passed concept, family, and icon QA;
- one existing `-design.svg` per symbol;
- the intended host and label;
- no unexplained `skip` line.

A missing file must be resolved before upload unless that symbol was deliberately
omitted and reported. Uploading replaces live shared-library finals. Obtain
explicit confirmation from the requester before the real POST.

```bash
python3 upload.py
python3 upload.py --name rework-2
python3 upload.py --base https://staging-host
```

Each request sends raw `image/svg+xml; charset=utf-8` content to
`/api/v1/symbols/<sid>/final?name=<label>`. Record every printed per-symbol result.
Retry only after resolving a reported failure; never hide a partial upload.

Return to the repository root after upload work.

## Optional wrapper

`rework_opus.sh` orchestrates `stage → draft → detect → make → verify → upload`
and is resumable by stage:

```bash
./rework_opus.sh <category-or-url> --to verify
./rework_opus.sh <category-or-url> --from make --to verify
./rework_opus.sh <category-or-url> --dry-run
```

The `draft` stage name is retained for compatibility; brief-only items are
planned directly, not turned into artificial source SVGs. Detection applies only
to actual staged SVG references.

Its independent verify stage reruns structural, grid, and declared-overlap
prerequisites, then distance → holes → keyshape, and blocks upload when any
required result is missing, stale, under review, erroneous, or failing.
New payload reworks must be version-2 normal-profile sources
whose names match the staged batch; legacy instance documents are not accepted
as new rework outputs. A batch-local `grid-exceptions.json`, when present, is
passed to the grid gate and remains subject to its hash-locked exception checks.
Generated overlap panels still require human interpretation;
the wrapper also does not replace concept review or the true-size family review
required by this adapter. The real upload requires the wrapper's interactive
confirmation unless the requester explicitly authorized `--yes`.

## Deliver the rework report

Per symbol, deliver the canonical pipeline artifacts plus:

- `sid`, `concept`, brief, source origin, and reference-only R1 verdict/brief diff
  when applicable;
- `<icon-name>.svg`, the canonical output at the configured normal canvas/stroke;
- `<icon-name>-design.svg`, the same-size compatibility alias referenced by the
  staged upload manifest when upload was authorized;
- concept-review result and upload result or “not uploaded”.

Per batch, deliver one `batch-notes.md` with:

- label, category, symbol list, and source origin per symbol;
- triage counts, selected references and construction decisions;
- per-symbol required-feature accounting and decisions, plus reference-only R1
  verdict/present/missing/excess accounting when applicable;
- all symbols judged already correct, listed separately;
- concept and family review findings;
- omitted/blocked symbols and reasons;
- upload host, label, approval, and result per `sid`.

Also retain `manifest.json`, `batch.json`, `briefs.md`, applicable detection
summary, QA reports, and contact sheets. Completion traces JSON brief → optional
reference analysis → maker decision → editable element → design SVG → all three
passing gates → review → upload result.
End after this batch; do not fetch another category automatically.

## Stop conditions

Stop the affected symbol and report the blocker when:

- `kind` is not `"rework"` or the payload has no symbols;
- two symbols resolve to the same icon name;
- no source candidate and no `minimal_description` exists;
- `concept` and `minimal_description` describe different subjects;
- the brief is too vague to enumerate required features and reach R1;
- staged source or detection evidence cannot be resolved;
- an essential form cannot be represented safely by the supported geometry schema;
- a user decision would change the subject or feature budget;
- the upload dry run shows an unexpected host, label, symbol set, or missing file;
- the host rejects a symbol;
- the requester has not confirmed the real upload.

Finish safe work and report every real omission, its stopping step and reason.
Never POST an affected or incomplete symbol. No upload is implied by a request
to redraw, validate or deliver local files.
