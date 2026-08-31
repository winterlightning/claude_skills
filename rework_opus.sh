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
# starting over. The workflow it drives is docs/icon-rework-execution-steps.md.
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
# detect.
# The runbook's Step 3 says author one from the brief first, so do exactly that
# and nothing else — the full remake happens later, from the same evidence.
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
      echo "Author one draft source SVG for each symbol listed below, into:"
      echo
      echo "  $BATCH/sources/<icon-name>.svg"
      echo
      echo "These symbols have no current final, no reference, and no prototype,"
      echo "so the brief is all there is. Per"
      echo "docs/icon-rework-execution-steps.md Step 3 a"
      echo "draft is a legible sketch that fixes subject, part count, and"
      echo "arrangement so detection has something to measure — NOT a finished"
      echo "icon, and not a composition. Do not compose, emit, or validate"
      echo "anything; do not touch any other symbol; do not fetch anything."
      echo
      echo "Each file: viewBox=\"0 0 48 48\", fill=\"none\","
      echo "stroke=\"currentColor\", stroke-width=\"4\", round caps and joins."
      echo "Lines, arcs, and quadratics only — never a cubic. Draw only the parts"
      echo "the brief authorizes; its feature budget is binding."
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
    print("    Per docs/icon-rework-execution-steps.md Step 3, author")
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
Read docs/icon-rework-execution-steps.md completely and follow it for the
staged batch at:

  $BATCH

Steps 1-5 are already done: the batch is staged and detection has run. Begin at
Step 6 and work through Step 11.

Binding points, from that runbook:
- R0 — the brief outranks the source drawing. minimal_description in briefs.md is
  the authoritative subject and feature budget; the staged source is evidence of
  geometry, never of meaning. Record a briefDiff entry for every disagreement and
  omit every part the brief does not authorize. batch.json records which ladder
  rung each source came from as sourceOrigin: final, reference, prototype, or
  brief. A prototype is foreign-grid (26u viewBox, 1.5 stroke) and is usually the
  drawing that was already rejected — read it only for subject, part count, and
  arrangement, together with the brief, and rebuild all of its geometry from
  atoms.
- R1 — judge before you remake. For every symbol sourced from a final or a
  prototype, enumerate the features
  minimal_description requires and account for each as present, missing, or
  excess against the staged drawing, then record
  sourceAnalysis.briefCompliance with a verdict of correct, partial, or wrong.
  The library's "wrong" flag is a claim to be tested, not a finding to assume: if
  a current final already implements its brief, say so and reproduce it rather
  than redrawing it to justify the rework. Watch especially for excess features —
  these briefs are explicitly budgeted.
- This staged folder is the entire evidence scope. Do not open an SVG outside it
  and do not fetch anything.
- Phase 1 maps every symbol before any composition; the atom gate comes next;
  compose only after both.
- Write editable sources to $BATCH/editable/<icon-name>.json using the
  iconName in batch.json, and emit to $BATCH/output.
- Run every gate in Step 10 and both reviews in Step 11.

Do NOT run upload.py and do NOT POST anything. The wrapper script handles the
upload after it verifies your output.

Report at the end: per symbol, the icon name, the R1 verdict, the keyshape token,
the brief-diff decisions, and the QA result. List separately any symbol you
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
missing=[]
for r in batch["symbols"]:
    for key in ("design","ship"):
        if not (root/r[key]).is_file(): missing.append(f"{r['sid']}  {r[key]}")
    if not (root/"editable"/f"{r['iconName']}.json").is_file():
        missing.append(f"{r['sid']}  editable/{r['iconName']}.json")
if missing:
    print("    missing output:"); [print("      "+m) for m in missing]
    print("    re-run with --from make, or finish those symbols by hand.")
    sys.exit(1)
print(f"    {len(batch['symbols'])} symbols have editable source, design SVG, and ship SVG")
PY

  shopt -s nullglob
  DESIGNS=("$BATCH"/output/*-design.svg)
  SHIPS=(); for f in "$BATCH"/output/*.svg; do [[ "$f" == *-design.svg ]] || SHIPS+=("$f"); done
  shopt -u nullglob

  note "grid gate (design canvas)"
  python3 core/check_svg_grid.py "${DESIGNS[@]}" --expected design \
    --output-dir "$BATCH/qa/grid" >/dev/null || true
  note "keyshape containment (ship canvas)"
  python3 core/check_keyfit.py "${SHIPS[@]}" \
    --expected-editable-dir "$BATCH/editable" \
    --output-dir "$BATCH/qa/keyshape" >/dev/null || true
  note "hole and pinch QA (ship canvas)"
  python3 core/qa_overlays.py "${SHIPS[@]}" \
    --output-dir "$BATCH/qa/holes" --min-radius-design-u 1 >/dev/null || true

  # Each gate writes a flat JSON list of {file, status}; read those rather than
  # scraping stdout, which the HTML reports pollute with the word "fail".
  python3 - "$BATCH" <<'PY' || die "not uploading a batch with failing QA. Fix it, then re-run with --from verify."
import json, sys
from pathlib import Path

qa = Path(sys.argv[1]) / "qa"
GATES = (("grid",     qa / "grid" / "grid-results.json",       "overallStatus"),
         ("keyshape", qa / "keyshape" / "keyfit-results.json", "status"),
         ("holes",    qa / "holes" / "hole-diameters.json",    "status"))

bad = []
for gate, path, key in GATES:
    if not path.is_file():
        bad.append((gate, path.name, "report missing — the gate did not run"))
        continue
    for row in json.loads(path.read_text()):
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
print("    all gates clean")
PY
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
