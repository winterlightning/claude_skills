# Single-Icon SVG Adapter

Use this adapter when one selected SVG is remade as one Unlimited Shapes icon.
Follow the shared stages, commands, type-support limits, QA order, and repair loop
in [icon-pipeline.md](icon-pipeline.md). This page adds only the single-file scope,
evidence checkpoint, and handoff rules.

Use [icon-batch-execution-steps.md](icon-batch-execution-steps.md) for an explicit
set of SVGs. Use
[icon-rework-execution-steps.md](icon-rework-execution-steps.md) when the input is
a symbol-library rework JSON whose brief outranks the drawing.

## Single-file boundary

- Process exactly one source SVG in this execution.
- Do not scan, detect, compare, rank, or remake sibling files or variants.
- A filename such as `variant 1` is only the selected source's name; it does not
  authorize opening variants 2–4.
- Preserve the source unchanged and put every generated artifact in a separate
  work folder.
- If the user later selects another SVG, start a separate execution from intake.

## Lane sequence

```text
record one SVG + output folder + icon type
→ detect that SVG only
→ verify the three-file evidence bundle
→ enter the canonical pipeline at evidence review
→ deliver one icon and stop
```

Do not compose before detection, evidence review, type declaration, and source
mapping are complete.

## 1. Record scope and type

Record:

```text
source SVG:    /absolute/path/to/reference.svg
output folder: /absolute/path/to/work/<icon-name>
icon type:     normal | sub | container
```

Choose the type from [icon-types.md](icon-types.md). A request for an icon inside,
within, or held by another icon normally means a separately authored `container`
and `sub`, not the legacy 16u corner badge. If that interpretation would change
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
- an existing atom that preserves visual quality, or a fully integrated new
  generic parametric atom when it does not;
- editable atomic JSON as the repair source;
- the type-appropriate emission and QA path;
- a visual keyshape rationale based on the whole composition at true ship size;
- documented simplifications, omissions, exceptions, and blocked checks.

Do not attach or inspect sibling variants while resolving a mapping or choosing an
atom.

## 5. Deliver one traceable result

The handoff contains:

- editable JSON with `iconType`, declared keyshape, `sourceAnalysis` mappings,
  relationships, and spacing checks;
- type-appropriate design and exact half-scale ship SVGs;
- container slot metadata and non-shipping filled preview when applicable;
- the detection JSON and preflight plot;
- grid, overlap, keyshape, hole/pinch, and true-size evidence for the declared
  profile;
- intentional simplifications, omissions, approved exceptions, and new-atom work.

Completion means each important source element traces through maker decision →
atom instance → emitted SVG → QA evidence. End after delivering this icon.

## Stop conditions

Stop and report the blocker instead of guessing when:

- more than one source SVG is presented without an explicit batch request;
- the selected source and detection artifacts do not correspond;
- a source, report, dependency, or output location is unavailable;
- an essential feature remains semantically unexplained;
- a required atom would need prohibited cubic geometry or encode a whole icon;
- a required checker or profile artifact is unavailable;
- a user decision would materially change the subject or intended icon meaning.
