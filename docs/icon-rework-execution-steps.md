# Symbol-Library Rework Adapter

Use this adapter when the input is a symbol-library JSON payload with
`kind: "rework"` and finished icons may be posted back as each symbol's new final.
Follow the shared composition, script, QA, and repair sequence in
[icon-pipeline.md](icon-pipeline.md). This page adds the brief contract,
source-priority ladder, concept review, and controlled upload.

Use [icon-execution-steps.md](icon-execution-steps.md) for one directly supplied
SVG and [icon-batch-execution-steps.md](icon-batch-execution-steps.md) for a set of
SVGs staged by hand.

## Rework boundary

| | SVG lanes | Rework lane |
| --- | --- | --- |
| Input | one or more selected SVGs | one `kind: "rework"` JSON payload |
| Design brief | supplied drawing | `concept` + `minimal_description` |
| Source | supplied | resolved through the priority ladder below |
| Acceptance | source-informed simplification | brief compliance, then icon QA |
| Delivery | files | files plus an optional approved POST |
| Uploaded artifact | none | 48×48 `<name>-design.svg` with 4u stroke |

This lane currently produces normal 48×48 → 24×24 library icons. Do not silently
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
| `correct` | Subject, every required cue, and feature budget already match | Rebuild as traceable editable atomic source; do not redesign merely to justify the rework; report disagreement with `wrong: true` |
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
geometry is still foreign-grid and must be rebuilt from atoms.

## Payload field contract

Only these fields decide what to make.

### Required per symbol

| Field | Role |
| --- | --- |
| `sid` | Stable identity and upload URL key |
| `concept` | Subject and readable part of the icon name |
| `minimal_description` | Binding subject, required cues, and feature budget |
| `files.final` | Source candidate 1: current shipped icon |
| `files.reference_svg` or chosen `references[].path` | Source candidate 2: chosen reference |
| `files.prototype` | Source candidate 3: earlier foreign-grid drawing |
| `upload_url` | Destination for an approved design-SVG POST |

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

Resolve exactly one drawing per symbol, highest available first:

```text
1. files.final          current shipped icon       → detect and remake
2. files.reference_svg chosen reference            → detect and remake
3. files.prototype     earlier foreign-grid icon   → detect and remake with brief
4. none                draft SVG from the brief    → detect and remake
```

Every rung produces one file in `sources/`, then enters detection and the same
canonical icon pipeline.

The prototype is normally a 26u viewBox with 1.5 stroke and a literal color. Use
it for subject, part count, and arrangement, never for canvas, stroke, or exact
proportion. Read it together with `minimal_description`; the brief wins.

When no drawing exists, first author a legible 48u draft from `concept` and
`minimal_description`. The draft fixes subject, part count, and arrangement; it
is not the finished composition. Use only lines, arcs, and quadratics. Do not
compose the final icon directly from prose, because every symbol must reach
mapping with the same SVG + detection JSON + plot evidence bundle.

Carry `sourceOrigin` (`final`, `reference`, `prototype`, or `brief`) from
`batch.json` into `sourceAnalysis` and the delivery notes.

## Lane sequence

```text
fetch and stage
→ read briefs
→ verify one resolved source per symbol
→ batch detection and triage
→ record R1 verdict and map every symbol
→ whole-batch quality-first reuse-or-extend review
→ canonical composition and QA
→ concept review, then family review
→ upload dry-run
→ requester confirmation
→ POST
→ deliver report
```

Do not compose before every brief, source, R1 verdict, mapping, and atom request
is resolved. Do not POST before the upload stage and explicit confirmation.

## 1. Fetch and stage

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

The staged folder is the entire evidence scope. Do not open an SVG outside it or
fetch another category into the same folder. Icon names are
`<sid-kebab>-<concept-kebab>`; the staging script stops on a collision because two
identical names would overwrite output and upload state.

## 2. Read briefs and verify sources

Read `briefs.md` completely before mapping. For each symbol:

- confirm `concept` names a drawable subject;
- enumerate the exact feature budget in `minimal_description`;
- confirm the resolved source origin;
- note whether the source appears correct, partial, or wrong, without finalizing
  R1 until it is rendered and compared carefully.

Open every staged source and confirm it renders. Read `batch.json` →
`sourceCounts`; a batch dominated by `prototype` or `brief` sources needs more
design judgment and that fact belongs in the delivery notes.

For every `sourceOrigin: "brief"`, create `sources/<icon-name>.svg` before
detection. If another source must be resolved, rerun `fetch_rework_batch.py` with
the same `--out`; existing files remain unless `--overwrite` is explicit.

## 3. Detect and triage

```bash
BATCH=work/rework-building-construction
python3 core/batch_detect_svg_shapes.py \
  "$BATCH/sources" \
  "$BATCH/detection"
```

Pass `--overwrite` when a staged source changed. Apply the triage depth from the
[SVG batch adapter](icon-batch-execution-steps.md): rendered source for `ready`,
source + plot + direct path measurement for `review-required`, and resolution or
reported omission for `failed`.

Foreign-canvas references and prototypes often require review. That is expected;
measure their path data instead of reading proportions from the plot.

## 4. Map every symbol against its brief

Before composing anything:

1. Render the source and apply the required triage depth.
2. Finalize R1 `briefCompliance` against `minimal_description`.
3. Record `briefDiff` for every missing or excess feature.
4. Map every identity-bearing element using the decisions in the canonical
   pipeline. Unauthorized excess parts are `omit` with a brief-based reason.
5. Record relationships and painted-clearance checks.
6. Resolve every detector `manualReview` item semantically.

The editable source carries `sid`, `concept`, `brief`, `sourceOrigin`,
`briefCompliance`, `briefDiff`, mappings, relationships, and spacing checks under
`sourceAnalysis`. Maintain one batch `atom-requests.md` as described by the batch
adapter. No composition happens during this phase.

## 5. Consolidate atoms, compose, and run QA

Use the whole-batch quality-first reuse-or-extend review from
[icon-batch-execution-steps.md](icon-batch-execution-steps.md). A high new-atom
rate is a prompt to re-read the minimal briefs and deduplicate requests, not a
quota: keep every generic parametric atom that improves the finished icon, and
never force catalog reuse to lower the count.

Then compose in checkpointed groups of five and run every normal-profile stage in
[icon-pipeline.md](icon-pipeline.md): emission, structural baseline, grid,
overlap, declared keyshape, hole/pinch, and true-size review. Store editable JSON
in `$BATCH/editable` and output in `$BATCH/output`.

After every repair, re-emit and rerun all downstream gates. Do not upload an icon
whose automated report, mapping, or visual review is incomplete.

## 6. Perform concept review, then family review

Concept review is the acceptance test unique to this lane. Put each finished icon
beside its `concept` and `minimal_description` and answer:

1. Reading only the brief, would you draw this icon?
2. Seeing only the icon, would you name it this concept?

A “no” means the rework failed even if every geometry checker passed.

Then verify the output against R1:

- `wrong` or `partial`: the output differs from the source exactly where
  `missing` and `excess` said it should.
- `correct`: the output remains faithful, and the delivery report explains why
  the library's `wrong` flag appears mistaken.
- Every required feature is visible at 24px and no unauthorized feature appears.

Finish with the batch family review: true-size and magnified contact sheets,
consistent optical weight, motifs, gap rhythm, stance, margins, and no accidental
near-duplicates.

## 7. Dry-run and approve the upload

`upload.py` reads `manifest.json` beside itself, so run it inside the batch folder.
The staged manifest points each symbol's upload to its 48×48 design SVG.

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

Its independent verify stage reruns structural, declared-overlap evidence, grid,
keyshape, and hole/pinch gates and blocks upload when any required result is
missing or failing. Generated overlap panels still require human interpretation;
the wrapper also does not replace concept review or the true-size family review
required by this adapter. The real upload requires the wrapper's interactive
confirmation unless the requester explicitly authorized `--yes`.

## 8. Deliver the rework report

Per symbol, deliver the canonical pipeline artifacts plus:

- `sid`, `concept`, brief, source origin, R1 verdict, and brief diff;
- `<icon-name>-design.svg`, the uploaded artifact when upload was authorized;
- `<icon-name>.svg`, the 24px ship output;
- concept-review result and upload result or “not uploaded”.

Per batch, deliver one `batch-notes.md` with:

- label, category, symbol list, and source origin per symbol;
- triage counts and atom changes;
- per-symbol R1 verdict, required/present/missing/excess accounting, and decisions;
- all symbols judged already correct, listed separately;
- concept and family review findings;
- omitted/blocked symbols and reasons;
- upload host, label, approval, and result per `sid`.

Also retain `manifest.json`, `batch.json`, `briefs.md`, detection summary, QA
reports, and contact sheets. Completion traces JSON brief → R1 verdict → source →
detector element → maker decision → atom → design SVG → review → upload result.
End after this batch; do not fetch another category automatically.

## Stop conditions

Stop the affected symbol and report the blocker when:

- `kind` is not `"rework"` or the payload has no symbols;
- two symbols resolve to the same icon name;
- no source candidate and no `minimal_description` exists;
- `concept` and `minimal_description` describe different subjects;
- the brief is too vague to enumerate required features and reach R1;
- staged source or detection evidence cannot be resolved;
- a necessary atom requires prohibited geometry or a whole-icon primitive;
- a user decision would change the subject or feature budget;
- the upload dry run shows an unexpected host, label, symbol set, or missing file;
- the host rejects a symbol;
- the requester has not confirmed the real upload.

Do not stop solely because many symbols need new atoms. Apply the generic
parametric atom contract to every request, finish safe work, and report every real
omission, its stopping step, and reason. Never POST an affected or incomplete
symbol.
