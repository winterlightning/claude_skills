#!/bin/bash
# run_pipeline.sh — the new-pipeline-test process (process.md) end to end, two agents.
#
#   1. Codex    $generate-png-solo(-with-reference)  -> <run>/<slug>.png + <slug>_raw.svg
#   2. (script) vectorize/process.sh, only if Codex left no <slug>_raw.svg
#   3. (script) svg_metrics.py                        -> <slug>_metrics.json, _fitted.svg, _fitted-48.png
#   4. Claude   /icon-solo redraw from raw svg + metrics -> <under>_redraw.py, <slug>_redraw.svg/.png
#   5. (script) build_report.py                       -> output_png/report.html
#
# Codex runs one subject at a time (run folders are found by diffing output_png and kept only
# when their choice.json carries this item's source id, so several copies can run at once),
# and each finished PNG is handed to a background Claude redraw right away, so
# Codex draws the next subject while Claude redraws the previous one.
#
# Usage (from anywhere): one item = CONCEPT_NAME SOURCE_ID [REFERENCE], repeat for more.
#   new-pipeline-test/run_pipeline.sh "coffee mug" 0c92aa87-7dd1-43a5-b12c-bafae38f0600
#   new-pipeline-test/run_pipeline.sh "jumbo jet" 440ed8d8-ba1d-485b-bd8d-a6ae4bdc2513 ~/Downloads/jet.svg \
#                                     "taco" 83c18653-4bbf-498c-80b3-a71d2a06335a ref/taco.png \
#                                     "pencil" b54c8548-18c2-54c5-9f78-3a7907732a50
#   new-pipeline-test/run_pipeline.sh --redraw-only output_png/20260928-1439-jumbo-jet
#
# SOURCE_ID is the original icon's UUID; it goes to choice.json (source_icon_id) and
# becomes SOURCE_ICON_ID on the redrawn Solo48 model. Write `none` for a brand-new
# concept (SOURCE_ICON_ID = None). REFERENCE is optional: an existing .svg/.png right
# after the id; with it Codex uses $generate-png-solo-with-reference.
#
# Options:
#   --shape tall|wide|square|round   passed to the PNG skill for every item
#   --redraw-only RUN_DIR            skip Codex; run metrics + Claude redraw on an existing run (repeatable)
#   --no-redraw                      stop after metrics (Codex only)
#   --max-parallel N                 Claude redraws running at once (default 2)
#
# Environment:
#   CODEX_MODEL / CLAUDE_MODEL       model overrides (Claude defaults to claude-opus-5-5)
#   CODEX_FLAGS                      default: --dangerously-bypass-approvals-and-sandbox
#   CLAUDE_FLAGS                     default: --dangerously-skip-permissions
#   PY                               python with svgpathtools (default /opt/homebrew/bin/python3)
#
# Logs: <run>/codex.log, and <run>/claude.log written live (tail -f it to watch the redraw);
# a summary line per subject at the end.
set -uo pipefail
shopt -s nullglob

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
OUT="$HERE/output_png"
PY="${PY:-/opt/homebrew/bin/python3}"
CLAUDE_MODEL="${CLAUDE_MODEL:-claude-opus-5-5}"
read -r -a CODEX_ARGS <<< "${CODEX_FLAGS:---dangerously-bypass-approvals-and-sandbox}"
read -r -a CLAUDE_ARGS <<< "${CLAUDE_FLAGS:---dangerously-skip-permissions}"
[ -n "${CODEX_MODEL:-}" ] && CODEX_ARGS+=(-m "$CODEX_MODEL")

shape=""
no_redraw=0
max_parallel=2
subjects=()     # "name<TAB>source id or none<TAB>abs reference path or empty"
positional=()
redraw_dirs=()

die() { echo "error: $*" >&2; exit 1; }
log() { echo "[$(date +%H:%M:%S)] $*"; }

while [ $# -gt 0 ]; do
    case "$1" in
        --shape) shape="${2:-}"; shift 2 ;;
        --redraw-only)
            d="$2"; [ -d "$d" ] || d="$OUT/$2"
            [ -d "$d" ] || die "run folder not found: $2"
            redraw_dirs+=("$(cd "$d" && pwd)"); shift 2 ;;
        --no-redraw) no_redraw=1; shift ;;
        --max-parallel) max_parallel="$2"; shift 2 ;;
        -h|--help) sed -n '2,40p' "$0"; exit 0 ;;
        -*) die "unknown option $1" ;;
        *) positional+=("$1"); shift ;;
    esac
done

is_uuid() { echo "$1" | grep -Eq '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'; }
is_image() { [ -f "$1" ] && case "$1" in *.svg|*.SVG|*.png|*.PNG) true ;; *) false ;; esac; }

# Group the positional words into items: NAME SOURCE_ID [REFERENCE].
i=0
while [ $i -lt ${#positional[@]} ]; do
    name="${positional[$i]}"
    id="${positional[$((i+1))]:-}"
    [ -n "$id" ] || die "\"$name\" has no SOURCE_ID (give the original icon UUID, or none)"
    if [ "$id" != none ]; then
        is_uuid "$id" || die "\"$name\": SOURCE_ID must be a UUID or none, got \"$id\""
        id="$(echo "$id" | tr '[:upper:]' '[:lower:]')"
    fi
    ref=""
    next="${positional[$((i+2))]:-}"
    if [ -n "$next" ] && is_image "$next"; then
        ref="$(cd "$(dirname "$next")" && pwd)/$(basename "$next")"
        i=$((i+3))
    else
        case "$next" in *.svg|*.SVG|*.png|*.PNG) die "reference not found: $next" ;; esac
        i=$((i+2))
    fi
    subjects+=("$name	$id	$ref")
done
case "$shape" in ""|tall|wide|square|round) ;; *) die "--shape must be tall|wide|square|round" ;; esac
[ ${#subjects[@]} -gt 0 ] || [ ${#redraw_dirs[@]} -gt 0 ] || die "no subjects (see --help)"
command -v codex >/dev/null || [ ${#subjects[@]} -eq 0 ] || die "codex CLI not on PATH"
[ "$no_redraw" = 1 ] || command -v claude >/dev/null || die "claude CLI not on PATH"
"$PY" -c "import svgpathtools" 2>/dev/null || die "$PY lacks svgpathtools (set PY=...)"

mkdir -p "$OUT"
cd "$ROOT"
results="$(mktemp "${TMPDIR:-/tmp}/pipeline-results.XXXXXX")"
trap 'rm -f "$results"' EXIT

# The slug is the run folder name minus its YYYYMMDD-HHMM(-N) prefix; the PNG
# decides when a -2/-3 suffix is part of the folder rather than the subject.
slug_of() {
    local run="$1" png
    for png in "$run"/*.png; do
        case "$(basename "$png")" in *_*|*-48.png|*-try*.png) continue ;; esac
        basename "$png" .png; return
    done
    basename "$run" | sed -E 's/^[0-9]{8}-[0-9]{4}-//'
}

# Stages 2-4 for one run folder; runs in the background.
post_process() {
    local run="$1" source_id="${2:-}" slug under rel status="" id_py
    slug="$(slug_of "$run")"
    # The id the script was given wins; --redraw-only reads it back from choice.json.
    [ -n "$source_id" ] || source_id="$("$PY" -c 'import json,sys
try: v = json.load(open(sys.argv[1])).get("source_icon_id")
except Exception: v = None
print(v or "none")' "$run/choice.json")"
    if [ "$source_id" = none ]; then id_py="None"; else id_py="\"$source_id\""; fi
    under="${slug//-/_}"
    rel="${run#"$ROOT"/}"

    if [ ! -f "$run/$slug.png" ]; then
        echo "FAIL  $rel  no $slug.png (see codex.log)" >> "$results"; return
    fi
    if [ ! -f "$run/${slug}_raw.svg" ]; then
        log "$slug: vectorizing (Codex left no _raw.svg)"
        "$HERE/vectorize/process.sh" "$run/$slug.png" >> "$run/pipeline.log" 2>&1 \
            || { echo "FAIL  $rel  vectorize failed (see pipeline.log)" >> "$results"; return; }
    fi

    log "$slug: metrics"
    if ! "$PY" "$HERE/svg_metrics.py" "$run/${slug}_raw.svg" >> "$run/pipeline.log" 2>&1; then
        echo "FAIL  $rel  svg_metrics failed (see pipeline.log)" >> "$results"; return
    fi
    if [ "$no_redraw" = 1 ]; then
        echo "OK    $rel  metrics only" >> "$results"; return
    fi

    local ref_note=""
    for r in "$run"/reference.svg "$run"/reference.png; do
        [ -f "$r" ] && ref_note=" The original reference is $rel/$(basename "$r")."
    done

    log "$slug: Claude redraw started"
    claude -p --model "$CLAUDE_MODEL" --output-format stream-json --verbose "${CLAUDE_ARGS[@]}" "/icon-solo Redraw the traced icon in $rel as a Solo48 model (the Redraw step of new-pipeline-test/process.md).
Inputs: $rel/${slug}_raw.svg (the vectorized trace), $rel/${slug}_metrics.json (keyshape suggestion + fit, parts on the 48 grid, junctions, clearances, holes, human head gap and an issues list), $rel/${slug}_fitted.svg and $rel/$slug.png (the generated image).${ref_note}
Rebuild the subject on the 48 grid (do not copy trace coordinates), use the suggested keyshape unless the metrics show a better fit, and repair every issue in the metrics list that you can; report any you cannot, with the reason.
Save everything in $rel only:
- $rel/${under}_redraw.py: the Solo48 model, SOURCE_ICON_ID = $id_py, SOURCE_PATH = \"$rel/${slug}_raw.svg\", AUTHOR = \"$CLAUDE_MODEL\", with a docstring stating the plan and which metric issues were fixed.
- $rel/${slug}_redraw.svg, $rel/${slug}_redraw.png (large preview) and $rel/${slug}_redraw-48.png (native 48 px).
Do not register the module under icon_set/model/icons, do not touch published/, and do not run the build or gallery updates. Work without asking questions; end with a short report." \
        2>&1 < /dev/null | "$PY" -u "$HERE/claude_log.py" > "$run/claude.log" || status=" (claude exited non-zero)"

    if [ -f "$run/${slug}_redraw.svg" ]; then
        echo "OK    $rel  redraw: ${slug}_redraw.svg$status" >> "$results"
    else
        echo "FAIL  $rel  no ${slug}_redraw.svg$status, see claude.log" >> "$results"
    fi
    log "$slug: Claude redraw finished"
}

throttle() {
    while [ "$(jobs -rp | wc -l)" -ge "$max_parallel" ]; do sleep 5; done
}

# Existing runs: straight to metrics + redraw.
for d in ${redraw_dirs[@]+"${redraw_dirs[@]}"}; do
    throttle
    post_process "$d" &
done

# New subjects: Codex draws one at a time, redraws overlap.
for entry in ${subjects[@]+"${subjects[@]}"}; do
    IFS=$'\t' read -r name source_id ref <<< "$entry"
    shape_arg=""; [ -n "$shape" ] && shape_arg=" --shape $shape"
    id_arg=" --source-id $source_id"
    [ "$source_id" = none ] && id_arg=""
    if [ -n "$ref" ]; then
        prompt="\$generate-png-solo-with-reference $name $ref$id_arg$shape_arg

This is exactly one item. Name: $name
Reference (absolute path, may contain spaces): $ref"
    else
        prompt="\$generate-png-solo $name$id_arg$shape_arg

This is exactly one item. Subject: $name"
    fi
    if [ "$source_id" = none ]; then
        prompt="$prompt
Source icon id: none, this is a brand-new concept. Record source_icon_id null in choice.json and do not ask for an id."
    else
        prompt="$prompt
Source icon id (the original icon this replaces): $source_id. Record it as source_icon_id in choice.json exactly as given."
    fi
    prompt="$prompt

Work without asking questions. Save the reference (if any) as reference.svg or reference.png in the run folder."

    before="$(ls -1 "$OUT")"
    log "$name: Codex generating PNG"
    clog="$(mktemp "${TMPDIR:-/tmp}/codex-log.XXXXXX")"
    codex exec -C "$ROOT" "${CODEX_ARGS[@]}" "$prompt" < /dev/null > "$clog" 2>&1
    codex_rc=$?
    # Other run_pipeline.sh copies may add folders to output_png meanwhile; keep only this
    # item's: choice.json source_icon_id equals this id, else (no id recorded) the folder slug
    # matches the name. Never claim another item's folder (it would get this id and a second redraw).
    new_runs=()
    while IFS= read -r d; do
        [ -n "$d" ] && [ -d "$OUT/$d" ] && new_runs+=("$OUT/$d")
    done < <(comm -13 <(echo "$before" | sort) <(ls -1 "$OUT" | sort) \
             | "$PY" -c '
import json, re, sys
from pathlib import Path
out, sid, name = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
for d in (line.strip() for line in sys.stdin):
    if not d:
        continue
    try:
        recorded = json.loads((out / d / "choice.json").read_text()).get("source_icon_id", "missing")
    except (OSError, ValueError):
        recorded = "missing"
    folder_slug = re.sub(r"^\d{8}-\d{4}-", "", d)  # a -2/-3 same-minute suffix still startswith(slug + "-")
    if recorded == "missing" or (sid == "none" and recorded is None):
        mine = folder_slug == slug or folder_slug.startswith(slug + "-")
    else:
        mine = (recorded or "none").lower() == sid.lower()
    if mine:
        print(d)
' "$OUT" "$source_id" "$name")

    if [ ${#new_runs[@]} -eq 0 ]; then
        mv "$clog" "$OUT/codex-failed-$(date +%Y%m%d-%H%M%S).log"
        echo "FAIL  $name  Codex created no run folder (exit $codex_rc)" >> "$results"
        log "$name: Codex made no run folder"
        continue
    fi
    for run in "${new_runs[@]}"; do
        cp "$clog" "$run/codex.log"
        "$PY" - "$run/choice.json" "$source_id" <<'SETID'
import json, sys
from pathlib import Path
path, sid = Path(sys.argv[1]), sys.argv[2]
data = json.loads(path.read_text()) if path.is_file() else {}
data["source_icon_id"] = None if sid == "none" else sid
path.write_text(json.dumps(data, indent=2) + "\n")
SETID
    done
    rm -f "$clog"
    log "$name: Codex done -> ${new_runs[*]#"$ROOT"/}"
    for run in "${new_runs[@]}"; do
        throttle
        post_process "$run" "$source_id" &
    done
done

wait
"$PY" "$HERE/build_report.py" >/dev/null 2>&1 && log "report: ${OUT#"$ROOT"/}/report.html"
echo
cat "$results"
grep -q '^FAIL' "$results" && exit 1
exit 0
