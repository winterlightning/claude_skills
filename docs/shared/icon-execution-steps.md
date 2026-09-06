# Single-Icon SVG Adapter

Use this adapter when one selected SVG is remade as one Unlimited Shapes icon.
It implements the SVG-reference intake of the shared workflow, not a separate
generation pipeline. For name + description without a reference, or with a PNG
or another file format, use the corresponding intake in
[icon-pipeline.md](icon-pipeline.md); do not fabricate an SVG for this adapter.
Follow the shared stages, commands, type-support limits, QA order, and repair loop
in [icon-pipeline.md](icon-pipeline.md). This page adds only the single-file scope,
evidence checkpoint, and handoff rules.

Use [icon-batch-execution-steps.md](icon-batch-execution-steps.md) for an explicit
set of SVGs. Use
[normal-icon rework](../icons/rework.md) when the input is
a symbol-library rework JSON whose brief outranks the drawing.

## Single-file boundary

- Process exactly one source SVG in this execution.
- Do not scan, detect, compare, rank, or remake sibling files or variants.
- A filename such as `variant 1` is only the selected source's name; it does not
  authorize opening variants 2–4.
- Relevant bundled Lucide original/debug pairs may inform construction; they do
  not expand the subject input set or override the selected source's meaning.
- Preserve the source unchanged and put every generated artifact in a separate
  work folder.
- If the user later selects another SVG, start a separate execution from intake.

## Lane sequence

```text
normalize concept name + minimal description + selected SVG + icon type/profile
→ detect that SVG only
→ verify the three-file evidence bundle
→ analyze the reference, then plan from the selected profile and Lucide style guidance
→ canonical composition and prerequisites
→ distance → holes → keyshape → native-size visual review
→ deliver one icon and stop
```

Do not compose before detection, evidence review, type declaration, and source
mapping are complete.

## 1. Record scope and type

Record:

```text
concept name:  <subject>
minimal description: <required features and arrangement>
source SVG:    /absolute/path/to/reference.svg
output folder: /absolute/path/to/work/<icon-name>
icon type:     <configured profile name>
```

Use the supplied name and description as the brief. For a legacy SVG-only
request, record the subject and essential features inferred from that selected
reference; ask only when ambiguity would materially change the intended icon.

Choose the type from [icon-types.md](icon-types.md). A request for an icon inside,
within, or held by another icon normally means a separately authored `container`
and `sub`, rather than a [normal corner badge](../icons/rules.md#composite-corner-badges). If that interpretation would change
the requested meaning, stop for a user decision.

A useful folder layout is:

```text
work/<icon-name>/
├── detection/
├── editable/
├── output/
└── qa/
```

Run commands from the repository root; do not use a machine-specific absolute
project path.

## 2. Detect only the selected SVG

```bash
python3 core/detect_svg_shapes.py \
  "/absolute/path/to/reference.svg" \
  --output "work/<icon-name>/detection/<icon-name>-shapes.json" \
  --plot "work/<icon-name>/detection/<icon-name>-preflight.png"
```

Do not pass a folder, wildcard, or list. Do not substitute
`batch_detect_svg_shapes.py` in a single-icon execution.

## 3. Pass the evidence checkpoint

Before composition, verify these three artifacts describe the same selected icon:

1. Original source SVG.
2. Matching `*-shapes.json` detection report.
3. Matching `*-preflight.png` plot.

Inspect:

- `summary.readyForIconMaker`;
- every source element ID;
- `makerPreflight.suggestedAtoms`;
- `makerPreflight.manualReview`;
- every `specIssues` warning or error;
- labeled geometry in the preflight plot and the original rendered source.

`readyForIconMaker: false` is a manual-review requirement, not permission to guess
and not necessarily a permanent stop. Resolve the marked geometry semantically.
If the source name, geometry, JSON, or plot does not correspond, regenerate the
detection artifacts before continuing.

## 4. Enter the canonical pipeline

Continue at “Review evidence and map the source” in
[icon-pipeline.md](icon-pipeline.md). Keep the complete evidence bundle together:

```text
source SVG:      /absolute/path/to/reference.svg
detection JSON:  /absolute/path/to/<icon-name>-shapes.json
preflight plot:  /absolute/path/to/<icon-name>-preflight.png
editable source: /absolute/path/to/editable/<icon-name>.json
output folder:   /absolute/path/to/output
```

Single-icon work still requires:

- one recorded maker decision for every identity-bearing source element;
- relationship and painted-clearance records for relevant pairs and openings;
- relevant original/debug reference review with recorded construction principles;
- exact editable elements with stable IDs, including connected contours where useful;
- schema-version-2 editable JSON as the repair source;
- the type-appropriate emission and QA path;
- fresh passing distance, hole, and keyshape gates on the same final geometry and
  resolved profile, in that order;
- a visual keyshape rationale based on the whole composition at native size;
- documented simplifications, omissions, exceptions, and blocked checks.

Do not attach or inspect unselected sibling variants while resolving a mapping
or choosing a construction approach.

After any geometry repair, re-emit both output aliases, recheck the prerequisites,
and restart at distance—even if the repair addressed a hole or keyshape failure.
Use the reported element pair, violating zone, or measured bounds to repair the
drawing. A missing/stale report, checker error, or unresolved review blocks
completion; do not alter intended connections or relax the profile to force a pass.

## 5. Deliver one traceable result

The handoff contains:

- editable JSON with `iconType`, declared keyshape, `sourceAnalysis` mappings,
  relationships, and spacing checks;
- canonical native SVG at the declared profile's configured canvas and stroke; any `-design.svg` is a same-size alias;
- container slot metadata and non-shipping filled preview when applicable;
- the detection JSON and preflight plot;
- grid, overlap, distance, hole/pinch, keyshape, and true-size evidence for the declared
  profile;
- intentional simplifications, omissions, approved exceptions, and reference choices.

Completion means each important source element traces through maker decision →
editable element → emitted SVG → QA evidence. End after delivering this icon.

## Stop conditions

Stop and report the blocker instead of guessing when:

- more than one source SVG is presented without an explicit batch request;
- the selected source and detection artifacts do not correspond;
- a source, report, dependency, or output location is unavailable;
- an essential feature remains semantically unexplained;
- an essential form cannot be represented safely by the supported geometry schema;
- a required checker or profile artifact is unavailable;
- a user decision would materially change the subject or intended icon meaning.
