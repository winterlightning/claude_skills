#!/bin/bash
# run_pipeline.sh — the new-pipeline-test process (process.md) end to end, two agents.
#
#   1. Codex    $generate-png-solo(-with-reference)  -> <run>/<slug>.png + <slug>_raw.svg
#   2. (script) vectorize/process.sh, only if Codex left no <slug>_raw.svg
#   3. (script) svg_metrics.py                        -> <slug>_metrics.json, _fitted.svg, _fitted-48.png
#   4. Claude   /icon-solo redraw from raw svg + metrics -> <under>_redraw.py, <slug>_redraw.svg/.png
#   5. (script) build_report.py                       -> output_png/report.html
#
# Codex runs one subject at a time (run folders are found by diffing output_png),
# and each finished PNG is handed to a background Claude redraw right away, so
# Codex draws the next subject while Claude redraws the previous one.
#
# Usage (from anywhere):
#   new-pipeline-test/run_pipeline.sh "coffee mug" "paper plane"
#   new-pipeline-test/run_pipeline.sh --shape tall "pencil"
#   new-pipeline-test/run_pipeline.sh --ref "jumbo jet" ~/Downloads/jet.svg --ref "taco" ref/taco.png
#   new-pipeline-test/run_pipeline.sh --redraw-only output_png/20260928-1439-jumbo-jet
#
# Options:
#   --shape tall|wide|square|round   passed to the PNG skill for every subject
#   --ref NAME PATH                  one subject drawn from a reference image (repeatable)
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
# Logs: <run>/codex.log and <run>/claude.log; a summary line per subject at the end.
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
subjects=()     # "plain<TAB>subject" or "ref<TAB>name<TAB>abs path"
redraw_dirs=()

die() { echo "error: $*" >&2; exit 1; }
log() { echo "[$(date +%H:%M:%S)] $*"; }

while [ $# -gt 0 ]; do
    case "$1" in
        --shape) shape="${2:-}"; shift 2 ;;
        --ref)
            [ $# -ge 3 ] || die "--ref needs NAME PATH"
            [ -f "$3" ] || die "reference not found: $3"
            subjects+=("ref	$2	$(cd "$(dirname "$3")" && pwd)/$(basename "$3")"); shift 3 ;;
        --redraw-only)
            d="$2"; [ -d "$d" ] || d="$OUT/$2"
            [ -d "$d" ] || die "run folder not found: $2"
            redraw_dirs+=("$(cd "$d" && pwd)"); shift 2 ;;
        --no-redraw) no_redraw=1; shift ;;
        --max-parallel) max_parallel="$2"; shift 2 ;;
        -h|--help) sed -n '2,34p' "$0"; exit 0 ;;
        -*) die "unknown option $1" ;;
        *) subjects+=("plain	$1"); shift ;;
    esac
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
    local run="$1" slug under rel status=""
    slug="$(slug_of "$run")"
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
    claude -p --model "$CLAUDE_MODEL" "${CLAUDE_ARGS[@]}" "/icon-solo Redraw the traced icon in $rel as a Solo48 model (the Redraw step of new-pipeline-test/process.md).
Inputs: $rel/${slug}_raw.svg (the vectorized trace), $rel/${slug}_metrics.json (keyshape suggestion + fit, parts on the 48 grid, junctions, clearances, holes, human head gap and an issues list), $rel/${slug}_fitted.svg and $rel/$slug.png (the generated image).${ref_note}
Rebuild the subject on the 48 grid (do not copy trace coordinates), use the suggested keyshape unless the metrics show a better fit, and repair every issue in the metrics list that you can; report any you cannot, with the reason.
Save everything in $rel only:
- $rel/${under}_redraw.py: the Solo48 model, SOURCE_PATH = \"$rel/${slug}_raw.svg\", AUTHOR = \"$CLAUDE_MODEL\", with a docstring stating the plan and which metric issues were fixed.
- $rel/${slug}_redraw.svg, $rel/${slug}_redraw.png (large preview) and $rel/${slug}_redraw-48.png (native 48 px).
Do not register the module under icon_set/model/icons, do not touch published/, and do not run the build or gallery updates. Work without asking questions; end with a short report." \
        > "$run/claude.log" 2>&1 || status=" (claude exited non-zero)"

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
    IFS=$'\t' read -r kind name ref <<< "$entry"
    shape_arg=""; [ -n "$shape" ] && shape_arg=" --shape $shape"
    if [ "$kind" = ref ]; then
        prompt="\$generate-png-solo-with-reference $name $ref$shape_arg"
    else
        prompt="\$generate-png-solo $name$shape_arg"
    fi
    prompt="$prompt

Work without asking questions. Save the reference (if any) as reference.svg or reference.png in the run folder."

    before="$(ls -1 "$OUT")"
    log "$name: Codex generating PNG"
    clog="$(mktemp "${TMPDIR:-/tmp}/codex-log.XXXXXX")"
    codex exec -C "$ROOT" "${CODEX_ARGS[@]}" "$prompt" < /dev/null > "$clog" 2>&1
    codex_rc=$?
    new_runs=()
    while IFS= read -r d; do
        [ -n "$d" ] && [ -d "$OUT/$d" ] && new_runs+=("$OUT/$d")
    done < <(comm -13 <(echo "$before" | sort) <(ls -1 "$OUT" | sort))

    if [ ${#new_runs[@]} -eq 0 ]; then
        mv "$clog" "$OUT/codex-failed-$(date +%Y%m%d-%H%M%S).log"
        echo "FAIL  $name  Codex created no run folder (exit $codex_rc)" >> "$results"
        log "$name: Codex made no run folder"
        continue
    fi
    for run in "${new_runs[@]}"; do cp "$clog" "$run/codex.log"; done
    rm -f "$clog"
    log "$name: Codex done -> ${new_runs[*]#"$ROOT"/}"
    for run in "${new_runs[@]}"; do
        throttle
        post_process "$run" &
    done
done

wait
"$PY" "$HERE/build_report.py" >/dev/null 2>&1 && log "report: ${OUT#"$ROOT"/}/report.html"
echo
cat "$results"
grep -q '^FAIL' "$results" && exit 1
exit 0
