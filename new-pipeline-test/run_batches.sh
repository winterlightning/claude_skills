#!/bin/bash
# run_batches.sh — run the batch-NNN.sh scripts written by fetch_repeat_disapproved.py, one after another.
#
# Each batch is one run_pipeline.sh call (10 items of NAME SOURCE_ID [REFERENCE]). This runner
# does them one after another (one runner per batches folder; a lock enforces it). run_pipeline.sh
# itself is parallel-safe, so batches pasted by hand in other terminals may run alongside. A finished batch leaves a marker, so re-running
# the same command resumes where it stopped.
#
# Usage:
#   new-pipeline-test/run_batches.sh BATCH_DIR                  # every batch not done yet
#   new-pipeline-test/run_batches.sh BATCH_DIR --from 5 --to 12 # batch-005 .. batch-012
#   new-pipeline-test/run_batches.sh BATCH_DIR --count 3        # the next 3 batches not done
#   new-pipeline-test/run_batches.sh BATCH_DIR --status         # show done / failed / pending, run nothing
#
# BATCH_DIR is the batches/ folder (or the fetch folder that contains it).
#
# Options:
#   --from N / --to N     batch number range (inclusive)
#   --count N             run at most N batches this time
#   --retry-failed        also re-run batches that failed before (default: skip them)
#   --redo                re-run batches even if done
#   --stop-on-fail        stop at the first failed batch (default: continue)
#   --status              print the state of every batch and exit
#
# State, next to the batch scripts:
#   logs/batch-NNN.log    full output of that batch
#   state/batch-NNN.done  finished with exit 0 (holds the finish time)
#   state/batch-NNN.failed  finished non-zero (holds exit code + time)
#   run_batches.lock      present while a runner is active
set -uo pipefail
shopt -s nullglob

die() { echo "error: $*" >&2; exit 1; }
log() { echo "[$(date +%H:%M:%S)] $*"; }

dir="" from=1 to=999999 count=0 retry_failed=0 redo=0 stop_on_fail=0 status_only=0
while [ $# -gt 0 ]; do
    case "$1" in
        --from) from="$((10#${2:?}))"; shift 2 ;;
        --to) to="$((10#${2:?}))"; shift 2 ;;
        --count) count="${2:?}"; shift 2 ;;
        --retry-failed) retry_failed=1; shift ;;
        --redo) redo=1; shift ;;
        --stop-on-fail) stop_on_fail=1; shift ;;
        --status) status_only=1; shift ;;
        -h|--help) sed -n '2,32p' "$0"; exit 0 ;;
        -*) die "unknown option $1" ;;
        *) [ -z "$dir" ] || die "only one BATCH_DIR"; dir="$1"; shift ;;
    esac
done
[ -n "$dir" ] || die "give the batches folder (see --help)"
[ -d "$dir/batches" ] && dir="$dir/batches"
[ -d "$dir" ] || die "not a folder: $dir"
dir="$(cd "$dir" && pwd)"
batches=("$dir"/batch-[0-9][0-9][0-9].sh)
[ ${#batches[@]} -gt 0 ] || die "no batch-NNN.sh in $dir"
mkdir -p "$dir/logs" "$dir/state"

num_of() { local b; b="$(basename "$1" .sh)"; echo "$((10#${b#batch-}))"; }
state_of() {
    local name; name="$(basename "$1" .sh)"
    if [ -f "$dir/state/$name.done" ]; then echo done
    elif [ -f "$dir/state/$name.failed" ]; then echo failed
    else echo pending; fi
}

if [ "$status_only" = 1 ]; then
    d=0 f=0 p=0
    for b in "${batches[@]}"; do
        s="$(state_of "$b")"
        case "$s" in done) d=$((d+1)) ;; failed) f=$((f+1)); echo "failed   $(basename "$b")  $(cat "$dir/state/$(basename "$b" .sh).failed")" ;; *) p=$((p+1)) ;; esac
    done
    echo "${#batches[@]} batches: $d done, $f failed, $p pending"
    [ -f "$dir/run_batches.lock" ] && echo "runner active: $(cat "$dir/run_batches.lock")"
    exit 0
fi

# One runner per batches folder, and one run_pipeline.sh on the machine.
lock="$dir/run_batches.lock"
if [ -f "$lock" ] && kill -0 "$(cut -d' ' -f1 "$lock")" 2>/dev/null; then
    die "another runner is active: $(cat "$lock")"
fi
echo "$$ started $(date '+%F %T')" > "$lock"
current=""
cleanup() { rm -f "$lock"; }
interrupted() {
    [ -n "$current" ] && log "interrupted during $current (not marked; it will run again next time)"
    cleanup; exit 130
}
trap cleanup EXIT
trap interrupted INT TERM

ran=0 ok=0 bad=0 summary=()
for b in "${batches[@]}"; do
    n="$(num_of "$b")"
    [ "$n" -ge "$from" ] && [ "$n" -le "$to" ] || continue
    s="$(state_of "$b")"
    [ "$s" = done ] && [ "$redo" = 0 ] && continue
    [ "$s" = failed ] && [ "$retry_failed" = 0 ] && [ "$redo" = 0 ] && continue
    [ "$count" -gt 0 ] && [ "$ran" -ge "$count" ] && break

    name="$(basename "$b" .sh)"
    current="$name"
    rm -f "$dir/state/$name.done" "$dir/state/$name.failed"
    log "$name: started ($(grep -c '^#   ' "$b") icons) -> logs/$name.log"
    start=$SECONDS
    bash "$b" > "$dir/logs/$name.log" 2>&1
    rc=$?
    mins=$(( (SECONDS - start + 59) / 60 ))
    ran=$((ran+1))
    current=""
    if [ $rc -eq 0 ]; then
        date '+%F %T' > "$dir/state/$name.done"
        ok=$((ok+1)); summary+=("OK    $name  ${mins} min")
        log "$name: done in ${mins} min"
    else
        echo "exit $rc $(date '+%F %T')" > "$dir/state/$name.failed"
        bad=$((bad+1)); summary+=("FAIL  $name  exit $rc, ${mins} min  (tail logs/$name.log)")
        log "$name: FAILED (exit $rc) — $(grep -E '^FAIL' "$dir/logs/$name.log" | wc -l | tr -d ' ') item(s) failed, see logs/$name.log"
        [ "$stop_on_fail" = 1 ] && break
    fi
done

echo
[ $ran -eq 0 ] && echo "nothing to run (all selected batches are done or failed; see --status, --retry-failed, --redo)"
printf '%s\n' ${summary[@]+"${summary[@]}"}
echo "ran $ran: $ok ok, $bad failed"
[ $bad -eq 0 ]
