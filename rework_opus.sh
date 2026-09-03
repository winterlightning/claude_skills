#!/usr/bin/env bash
#
# One-command symbol rework:
#   stage -> draft -> detect -> remake with Claude -> verify -> upload
#
#   ./rework_opus.sh "https://symlib.pictographic.ai/download-wrong-icons-json?cat=Building+Construction"
#   ./rework_opus.sh "Building Construction"
#   ./rework_opus.sh <url> --from make          # re-run the remake onward
#   ./rework_opus.sh <url> --to verify --yes    # build and check, upload nothing
#   ./rework_opus.sh <url> --from upload --yes  # just re-upload what is already built
#   ./rework_opus.sh <url> --to detect          # stage, draft, detect, then stop
#
# Every stage is idempotent, so re-running the same command resumes rather than
# starting over. The workflow it drives is docs/icons/rework.md.
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

MODEL="${REWORK_MODEL:-opus}"
PERMISSION_MODE="${REWORK_PERMISSION_MODE:-bypassPermissions}"
UPLOADER="${REWORK_UPLOADER:-$ROOT/upload.py}"
STAGES=(stage draft detect make verify upload)

TARGET=""
OUT=""
FROM="stage"
TO="upload"
LABEL=""
ASSUME_YES=0
DRY_RUN=0
FORCE=0

die()  { printf '\n\033[31merror:\033[0m %s\n' "$*" >&2; exit 1; }
step() { printf '\n\033[1m==> %s\033[0m\n' "$*"; }
note() { printf '    %s\n' "$*"; }

usage() {
  awk 'NR>1 { if (/^#/) { sub(/^# ?/, ""); print } else exit }' "${BASH_SOURCE[0]}"
  cat <<'EOF'

Options:
  --out DIR       batch folder (default work/rework-<label>)
  --from STAGE    start at stage: stage | draft | detect | make | verify | upload
  --to STAGE      stop after this stage (default upload)
  --name LABEL    upload variant label (default the manifest's api.label)
  --model NAME    model for the remake stage (default opus, or $REWORK_MODEL)
  --uploader PATH upload.py to stage (default ./upload.py, or $REWORK_UPLOADER)
  --yes           do not prompt before the real upload
  --dry-run       stop after the upload dry run; POST nothing
  --force         re-download sources and re-run detection
  -h, --help      this text
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --out)     OUT="${2:?--out needs a directory}"; shift 2 ;;
    --from)    FROM="${2:?--from needs a stage}"; shift 2 ;;
    --to)      TO="${2:?--to needs a stage}"; shift 2 ;;
    --name)    LABEL="${2:?--name needs a label}"; shift 2 ;;
    --model)   MODEL="${2:?--model needs a name}"; shift 2 ;;
    --uploader) UPLOADER="${2:?--uploader needs a path}"; shift 2 ;;
    --yes|-y)  ASSUME_YES=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    --force)   FORCE=1; shift ;;
    -h|--help) usage; exit 0 ;;
    -*)        die "unknown option $1 (try --help)" ;;
    *)         [[ -n "$TARGET" ]] && die "only one URL or category, got '$TARGET' and '$1'"
               TARGET="$1"; shift ;;
  esac
done

[[ -n "$TARGET" ]] || { usage; exit 1; }
printf '%s\n' "${STAGES[@]}" | grep -qx "$FROM" || die "--from must be one of: ${STAGES[*]}"
printf '%s\n' "${STAGES[@]}" | grep -qx "$TO"   || die "--to must be one of: ${STAGES[*]}"

# Run stage $1 only when it falls in the [--from, --to] window.
index_of() {
  local want="$1" i=0 s
  for s in "${STAGES[@]}"; do [[ "$s" == "$want" ]] && { echo "$i"; return; }; i=$((i+1)); done
  echo -1
}
FROM_I="$(index_of "$FROM")"; TO_I="$(index_of "$TO")"
[[ "$FROM_I" -le "$TO_I" ]] || die "--from $FROM comes after --to $TO"
active() {
  local i; i="$(index_of "$1")"
  [[ "$i" -ge "$FROM_I" && "$i" -le "$TO_I" ]]
}

command -v python3 >/dev/null || die "python3 not found"

# --------------------------------------------------------------- resolve batch
# The staging script derives the folder from the payload label, so ask it where
# it landed rather than guessing the slug here.
if [[ "$TARGET" == http*://* ]]; then FETCH=(--url "$TARGET"); else FETCH=(--cat "$TARGET"); fi
[[ -n "$OUT" ]] && FETCH+=(--out "$OUT")
FETCH+=(--uploader "$UPLOADER")

# Checked up front: a batch staged without an uploader cannot finish.
if active upload && [[ ! -f "$UPLOADER" ]]; then
  die "no uploader at $UPLOADER
    Pass --uploader <path/to/upload.py>, set REWORK_UPLOADER, or run with
    --to verify to build the batch without uploading."
fi

if active stage; then
  step "1/6  stage — fetch the rework JSON and resolve one source per symbol"
  [[ $FORCE -eq 1 ]] && FETCH+=(--overwrite)
  python3 core/fetch_rework_batch.py "${FETCH[@]}" | tee /tmp/rework-stage.$$ || die "staging failed"
  BATCH="$(sed -n 's/^wrote .* in \(.*\)$/\1/p' /tmp/rework-stage.$$ | tail -1)"
  rm -f /tmp/rework-stage.$$
else
  BATCH="${OUT:-}"
  [[ -n "$BATCH" ]] || BATCH="$(ls -dt work/rework-* 2>/dev/null | head -1)"
  [[ -n "$BATCH" ]] || die "no staged batch found; run without --from, or pass --out"
  note "reusing staged batch $BATCH"
fi
BATCH="$(cd "$BATCH" && pwd)"
[[ -f "$BATCH/batch.json" ]] || die "$BATCH is missing batch.json — stage the batch first"

COUNT="$(python3 -c "import json;print(json.load(open('$BATCH/batch.json'))['count'])")"
note "batch: $BATCH  ($COUNT symbols)"

# ---------------------------------------------------------------------- draft
# Symbols that resolved to no final, reference, or prototype have nothing to
# detect. The runbook's "Source-priority ladder" requires a draft from the brief
# first; the full remake happens later, from the same evidence.
if active draft; then
  step "2/6  draft — author a source for symbols no ladder rung resolved"
  NEEDED="$(python3 - "$BATCH" <<'PYD'
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
batch = json.loads((root / "batch.json").read_text())
print("\n".join(f"{r['iconName']}|{r['concept']}|{r['minimalDescription']}"
                 for r in batch["symbols"]
                 if not (root / r["sourcePath"]).is_file()))
PYD
)"
  if [[ -z "$NEEDED" ]]; then
    note "every symbol resolved to a drawing; nothing to draft"
  else
    command -v claude >/dev/null || die "the claude CLI is not on PATH"
    printf '%s\n' "$NEEDED" | while IFS='|' read -r n _ _; do note "needs a draft: $n"; done
    {
      echo "Read docs/icons/SKILL.md and the Source-priority ladder and"
      echo "Read briefs and verify sources sections in docs/icons/rework.md."
      echo
      echo "Author one draft source SVG for each symbol listed below, into:"
      echo
      echo "  $BATCH/sources/<icon-name>.svg"
      echo
      echo "These symbols have no current final, no reference, and no prototype,"
      echo "so the brief defines the draft's subject, feature budget, and arrangement."
      echo "The draft gives detection a drawing to measure. Final composition"
      echo "comes later. Do not compose, emit, or validate anything; do not touch"
      echo "any other symbol; do not fetch anything."
      echo
      echo "Use the normal design canvas, stroke, and permitted geometry in"
      echo "docs/icons/rules.md. Draw only the parts the brief authorizes; its"
      echo "feature budget is binding."
      echo
      echo "Symbols (icon-name | concept | brief):"
      printf '%s\n' "$NEEDED"
    } > "$BATCH/draft-prompt.txt"
    note "prompt written to $BATCH/draft-prompt.txt"
    claude -p "$(cat "$BATCH/draft-prompt.txt")" \
      --model "$MODEL" --permission-mode "$PERMISSION_MODE" --add-dir "$BATCH" \
      || die "the draft stage did not complete; re-run with --from draft"
  fi
fi

# --------------------------------------------------------------------- detect
if active detect; then
  step "3/6  detect — batch shape detection on the staged sources"
  # sources/ is globbed by the detector, so it must hold exactly the batch's
  # own files: a stray SVG would silently join the evidence scope.
  python3 - "$BATCH" <<'PY' || die "resolve the source folder, then re-run with --from detect"
import json, sys
from pathlib import Path

root = Path(sys.argv[1])
batch = json.loads((root / "batch.json").read_text())
expected = {Path(r["sourcePath"]).name: r["sid"] for r in batch["symbols"]}
present = {p.name for p in (root / "sources").glob("*.svg")}

missing = sorted(f"{sid}  {name}" for name, sid in expected.items() if name not in present)
strays = sorted(present - set(expected))
if missing:
    print("    no source drawing staged for:")
    for line in missing:
        print("      " + line)
    print("    These symbols resolved to no final, reference, or prototype.")
    print("    Per the Source-priority ladder in docs/icons/rework.md, author")
    print(f"    {root}/sources/<icon-name>.svg from the brief first.")
if strays:
    print("    unexpected file(s) in the source folder:")
    for name in strays:
        print("      " + name)
    print("    The staged folder is the entire evidence scope; a stray SVG would")
    print("    be detected and composed as an extra icon. Remove it, or re-stage")
    print("    the batch into a clean folder with --out.")
sys.exit(1 if (missing or strays) else 0)
PY
  DETECT=(python3 core/batch_detect_svg_shapes.py "$BATCH/sources" "$BATCH/detection")
  [[ $FORCE -eq 1 ]] && DETECT+=(--overwrite)
  "${DETECT[@]}" || die "detection failed"
  python3 - "$BATCH" <<'PY'
import json,sys
from pathlib import Path
s=json.loads((Path(sys.argv[1])/"detection"/"batch-summary.json").read_text())
print(f"    {s['svgCount']} sources · {s['readyCount']} ready · "
      f"{s['reviewRequiredCount']} review · {s['failedCount']} failed")
for f in s.get("files",[]):
    if f.get("status")!="ready": print("    review:",f["source"])
for f in s.get("failures",[]): print("    FAILED:",f["source"],f.get("error"))
PY
fi

# ----------------------------------------------------------------------- make
if active make; then
  step "4/6  make — remake every symbol with Claude ($MODEL)"
  command -v claude >/dev/null || die "the claude CLI is not on PATH"
  cat > "$BATCH/make-prompt.txt" <<EOF
Read docs/icons/SKILL.md, then docs/icons/rework.md completely. Follow their
linked normal rules and shared pipeline for the staged batch at:

  $BATCH

The wrapper's stage, draft, and detect stages are complete: the batch is staged,
missing-source drafts are present, and detection has run. Brief review, source
triage, mapping, composition, and QA still need to be completed.

Read briefs.md and verify the staged sources and detection evidence, then follow
these sections of docs/icons/rework.md in order:
- Map every symbol against its brief
- Inspect references, compose, and run QA
- Perform concept review, then family review

Binding points, from that runbook:
- R0 — the brief outranks the source drawing. minimal_description in briefs.md is
  the authoritative subject and feature budget; the staged source is evidence of
  geometry, never of meaning. Record a briefDiff entry for every disagreement and
  omit every part the brief does not authorize. Preserve sourceOrigin from
  batch.json and apply the runbook's source-priority and prototype rules.
- R1 — judge before you remake. For every symbol sourced from a final or a
  prototype, account for every required feature as present, missing, or excess
  against the staged drawing, then record
  sourceAnalysis.briefCompliance with a verdict of correct, partial, or wrong.
  The library's "wrong" flag is a claim to be tested, not a finding to assume: if
  a current final already implements its brief, say so and reproduce it rather
  than redrawing it to justify the rework.
- This staged folder is the entire subject-input scope. Do not open unselected
  user SVGs or variants, stage extra subjects, or fetch anything. Relevant paired
  SVGs under references/lucide/original/ and references/lucide/atomic-debug/ may
  be inspected as construction references; they cannot change a symbol's brief.
- Resolve each symbol's brief, mapping and material review questions before
  composing it. Continue safe work on other symbols when one is blocked.
- Read docs/shared/atomic-shapes.md for exact editable geometry and reference
  retrieval. Use python3 core/lucide_reference.py search 'query' --limit 6 and
  python3 core/lucide_reference.py inspect ICON --json to inspect useful pairs.
  Original SVGs are authoritative reference evidence; debug segmentation is an
  inspection aid, not a required output structure or proof of design intent.
- Record sourceAnalysis.lucideReferences with each name, selection reason and
  applied construction principles. Do not invent a match when none is useful.
- Apply the linked guides' visual-quality requirements. New contours live
  directly in editable geometry; do not extend the shape registry or generate
  shape assets. There is no element-count quota, strict 45-degree rule, fixed
  radius list or compulsory reuse gate. Technical compliance alone does not
  make an icon acceptable.
- Write editable sources to $BATCH/editable/<icon-name>.json using the
  iconName in batch.json, and emit to $BATCH/output. New sources must declare
  schemaVersion: 2, iconType: normal, and an ordered elements array with stable
  id, optional role, supported tag and geometry-only attrs. Do not use legacy
  instances/shapeId. Preserve sourceAnalysis and profile/keyfit metadata; use
  elements:[id,id] for spacing relationships. Keep connected contours as paths
  when useful, including intentional arcs, quadratic and cubic curves.
- Use the default exact keyfit mode unless an intrinsically thin/sparse subject
  justifies the documented optical mode, rationale and measured paintedBounds.
  Optical mode still requires containment and true-size visual review.
- Run every normal-profile QA gate in docs/shared/icon-pipeline.md, then the
  concept and family reviews in the rework adapter. Repair and rerun downstream
  gates before reporting completion.

Do NOT run upload.py and do NOT POST anything. The wrapper handles a separately
authorized upload after verification and its dry-run/confirmation sequence.

Report at the end: per symbol, the icon name, the R1 verdict, the keyshape token,
the brief-diff decisions, reference choices/construction principles, and the QA
result. List separately any symbol you
judged already correct. Name any symbol you could not finish and why.
EOF
  note "prompt written to $BATCH/make-prompt.txt"
  claude -p "$(cat "$BATCH/make-prompt.txt")" \
    --model "$MODEL" \
    --permission-mode "$PERMISSION_MODE" \
    --add-dir "$BATCH" \
    || die "the remake stage did not complete; inspect the output above and re-run with --from make"
fi

# --------------------------------------------------------------------- verify
if active verify; then
  step "5/6  verify — emitted outputs and the QA gates"
  python3 - "$BATCH" <<'PY' || exit 1
import json,sys
from pathlib import Path
root=Path(sys.argv[1]); batch=json.loads((root/"batch.json").read_text())
missing=[]; invalid=[]
for r in batch["symbols"]:
    for key in ("design","ship"):
        if not (root/r[key]).is_file(): missing.append(f"{r['sid']}  {r[key]}")
    source=root/"editable"/f"{r['iconName']}.json"
    if not source.is_file():
        missing.append(f"{r['sid']}  editable/{r['iconName']}.json")
        continue
    try:
        doc=json.loads(source.read_text())
    except (OSError, ValueError) as error:
        invalid.append(f"{r['sid']}  unreadable editable source: {error}")
        continue
    if not isinstance(doc,dict):
        invalid.append(f"{r['sid']}  editable source must be a JSON object")
        continue
    if (doc.get("schemaVersion") != 2 or not isinstance(doc.get("elements"),list)
            or not doc["elements"] or "instances" in doc):
        invalid.append(f"{r['sid']}  new reworks require schemaVersion 2 and nonempty elements, not legacy instances")
    if doc.get("iconType") != "normal":
        invalid.append(f"{r['sid']}  this payload lane requires an explicit normal profile")
    if doc.get("name") != r["iconName"]:
        invalid.append(f"{r['sid']}  editable name must match batch iconName {r['iconName']!r}")
if missing:
    print("    missing output:"); [print("      "+m) for m in missing]
if invalid:
    print("    invalid editable source:"); [print("      "+message) for message in invalid]
if missing or invalid:
    print("    re-run with --from make, or finish those symbols by hand.")
    sys.exit(1)
print(f"    {len(batch['symbols'])} symbols have editable source, design SVG, and ship SVG")
PY

  shopt -s nullglob
  DESIGNS=("$BATCH"/output/*-design.svg)
  SHIPS=(); for f in "$BATCH"/output/*.svg; do [[ "$f" == *-design.svg ]] || SHIPS+=("$f"); done
  shopt -u nullglob

  BATCH_PHYSICAL="$(cd "$BATCH" && pwd -P)"
  QA_ROOT="$BATCH_PHYSICAL/qa"
  [[ ! -L "$QA_ROOT" ]] || die "refusing to use symlinked QA root $QA_ROOT"
  mkdir -p "$QA_ROOT"
  QA_ROOT="$(cd "$QA_ROOT" && pwd -P)"
  [[ "$QA_ROOT" == "$BATCH_PHYSICAL/qa" ]] || die "QA root escaped the batch: $QA_ROOT"
  mkdir -p "$QA_ROOT/structure" "$QA_ROOT/overlap"
  STRUCTURE_FAILED=0
  OVERLAP_FAILED=0
  QA_FAILED=0

  # Report-producing gates must never read a previous run's aggregate after
  # their current command fails. Only these exact, batch-scoped QA folders may
  # be reset here.
  reset_qa_dir() {
    local gate="$1" target
    case "$gate" in
      grid|keyshape|holes) target="$QA_ROOT/$gate" ;;
      *) die "refusing to reset unknown QA directory '$gate'" ;;
    esac
    [[ "$target" == "$QA_ROOT"/* ]] || die "refusing to reset QA outside $QA_ROOT"
    rm -rf -- "$target"
    mkdir -p "$target"
  }

  note "structural validation (editable source + emitted parity)"
  for source in "$BATCH"/editable/*.json; do
    name="$(basename "$source" .json)"
    if ! python3 core/validate_icon.py "$source" --dir "$BATCH/output" \
      2>&1 | tee "$QA_ROOT/structure/$name.log"; then
      STRUCTURE_FAILED=1
    fi
  done

  note "overlap evidence (icons with declared spacing relationships)"
  for source in "$BATCH"/editable/*.json; do
    name="$(basename "$source" .json)"
    SPACING_COUNT="$(python3 -c 'import json,sys; doc=json.load(open(sys.argv[1])); print(len((doc.get("sourceAnalysis") or {}).get("spacingChecks") or []))' "$source")"
    if [[ "$SPACING_COUNT" -eq 0 ]]; then
      note "$name: no declared spacing relationships — audit not applicable"
      continue
    fi
    if ! python3 core/render_overlap_audit.py "$source" \
      "$QA_ROOT/overlap/$name-overlap-audit.svg" \
      2>&1 | tee "$QA_ROOT/overlap/$name.log"; then
      OVERLAP_FAILED=1
    fi
  done

  note "grid gate (design canvas)"
  reset_qa_dir "grid"
  GRID_EXCEPTIONS=()
  if [[ -f "$BATCH/grid-exceptions.json" ]]; then
    GRID_EXCEPTIONS=(--exceptions "$BATCH/grid-exceptions.json")
  fi
  if ! python3 core/check_svg_grid.py "${DESIGNS[@]}" --expected design \
    ${GRID_EXCEPTIONS[@]+"${GRID_EXCEPTIONS[@]}"} \
    --output-dir "$QA_ROOT/grid" >/dev/null; then
    QA_FAILED=1
  fi
  note "keyshape containment (ship canvas)"
  reset_qa_dir "keyshape"
  if ! python3 core/check_keyfit.py "${SHIPS[@]}" \
    --expected-editable-dir "$BATCH/editable" \
    --output-dir "$QA_ROOT/keyshape" >/dev/null; then
    QA_FAILED=1
  fi
  note "hole and pinch QA (ship canvas)"
  reset_qa_dir "holes"
  if ! python3 core/qa_overlays.py "${SHIPS[@]}" \
    --output-dir "$QA_ROOT/holes" --min-radius-design-u 1 >/dev/null; then
    QA_FAILED=1
  fi

  # Each gate writes a flat JSON list of {file, status}; read those rather than
  # scraping stdout, which the HTML reports pollute with the word "fail".
  python3 - "$BATCH" <<'PY' || QA_FAILED=1
import json, sys
from pathlib import Path

qa = Path(sys.argv[1]) / "qa"
batch = json.loads((Path(sys.argv[1]) / "batch.json").read_text())
GATES = (("grid",     qa / "grid" / "grid-results.json",       "overallStatus"),
         ("keyshape", qa / "keyshape" / "keyfit-results.json", "status"),
         ("holes",    qa / "holes" / "hole-diameters.json",    "status"))
EXPECTED = {
    "grid": {Path(row["design"]).name for row in batch["symbols"]},
    "keyshape": {Path(row["ship"]).name for row in batch["symbols"]},
    "holes": {Path(row["ship"]).name for row in batch["symbols"]},
}

bad = []
for gate, path, key in GATES:
    if not path.is_file():
        bad.append((gate, path.name, "report missing — the gate did not run"))
        continue
    rows = json.loads(path.read_text())
    seen = {row.get("file") for row in rows}
    for missing in sorted(EXPECTED[gate] - seen):
        bad.append((gate, missing, "result missing — the file was not processed"))
    for row in rows:
        status = str(row.get(key) or row.get("status") or "").lower()
        if status not in ("pass", "ok"):
            detail = row.get("reason") or row.get("remediation") or ""
            issues = row.get("issues") or []
            if issues and not detail:
                first = issues[0]
                detail = (first if isinstance(first, str)
                          else first.get("detail") or first.get("code") or str(first))
            bad.append((gate, row.get("file", "?"), f"{status}: {detail}".strip(": ")))

if bad:
    print("\n    \033[31mQA failures\033[0m")
    for gate, name, detail in bad:
        print(f"      [{gate}] {name}")
        if detail:
            print(f"               {detail}")
    print(f"\n    full reports: {qa}")
    sys.exit(1)
print("    grid, keyshape, and hole/pinch reports clean")
PY

  if [[ "$STRUCTURE_FAILED" -ne 0 || "$OVERLAP_FAILED" -ne 0 || "$QA_FAILED" -ne 0 ]]; then
    die "not uploading a batch with failing QA. Fix it, then re-run with --from verify."
  fi
  note "structural gates clean; all required overlap evidence was generated"
fi

# --------------------------------------------------------------------- upload
if active upload; then
  step "6/6  upload — POST each design SVG back as the symbol's final"
  [[ -f "$BATCH/upload.py" && -f "$BATCH/manifest.json" ]] \
    || die "$BATCH is missing upload.py or manifest.json — re-stage the batch"
  UP=(); [[ -n "$LABEL" ]] && UP=(--name "$LABEL")

  (cd "$BATCH" && python3 upload.py --dry-run ${UP[@]+"${UP[@]}"}) | sed 's/^/    /'

  if [[ $DRY_RUN -eq 1 ]]; then
    note "--dry-run set; nothing was posted"
    exit 0
  fi
  if [[ $ASSUME_YES -ne 1 ]]; then
    [[ -t 0 ]] || die "refusing to upload without a terminal to confirm at; pass --yes"
    printf '\n    This replaces %s live symbol finals at the host above.\n' "$COUNT"
    read -r -p "    Type 'upload' to proceed: " REPLY
    [[ "$REPLY" == "upload" ]] || die "cancelled; nothing was posted"
  fi
  (cd "$BATCH" && python3 upload.py ${UP[@]+"${UP[@]}"}) | sed 's/^/    /' || die "upload reported failures"
fi

step "done — $BATCH"
