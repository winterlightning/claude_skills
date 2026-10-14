#!/bin/bash
# Keep Terminal windows running /corner-review-next batches until nothing is left to review.
# Each slot is one Terminal window that runs its batches back to back, each in a fresh
# `claude --dangerously-skip-permissions`; the window closes when its slot is done.
#
#   open_review_terminals.sh               6 slots at once, offsets 0 10 20 30 40 50
#   open_review_terminals.sh --seq         one window at a time
#   open_review_terminals.sh 0 10 20       custom offsets (one slot per offset)
#   TAKE=5 open_review_terminals.sh        batch size (default 10)
#   ROUNDS=3 open_review_terminals.sh      stop each slot after 3 batches (default 0 = until no todo left)
#
# next_batch.py claims each batch (status reviewing), so a slot reusing its offset gets new icons.
# Once fewer todo icons are left than a slot's offset, the slot goes on at offset 0 (claims never
# overlap, the offset only spreads the slots), so the last icons of the list get reviewed too.
#
# New icons come in with: core.fetch --status all, round/sharp_corner_processing.py --files <new ones>,
# review/build_status.py (new icons start todo). After the review: core.apply_review, core.publish.
# Ctrl-C in the launcher stops starting new batches (running batches finish first).
#
# Interactive claude never exits on its own: its Stop hook ends it ($PPID of the hook is claude)
# a moment after the batch's last answer, and the window goes straight on to the next batch.
# (Before 2026-10-08 the launcher polled every 5 s, waited 3 s, killed claude, then closed the
# window and opened a new one for every batch.)

SELF="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
STATUS="$REPO/corner_processing/review/status.json"
TAKE="${TAKE:-10}"
ROUNDS="${ROUNDS:-0}"

todo_left() {  # icons still todo in status.json (a reviewer may be rewriting it: retry, then assume plenty)
  local n
  for _ in 1 2 3; do
    n="$(/opt/homebrew/bin/python3 -c '
import json, sys
s = json.load(open(sys.argv[1]))
print(sum(1 for e in s["icons"] if e.get("status") == "todo"))' "$STATUS" 2>/dev/null)" \
      && { echo "$n"; return; }
    sleep 1
  done
  echo 999999
}

# Inside a window: run this slot's batches one after another, then leave a marker for the launcher.
if [[ "${1:-}" == "--slot" ]]; then
  off="$2"; take="$3"; rounds="$4"; mark="$5"
  cd "$REPO" || exit 1
  hook="(sleep 2; kill -TERM \$PPID) >/dev/null 2>&1 &"
  settings="$(/opt/homebrew/bin/python3 -c 'import json, sys
print(json.dumps({"hooks": {"Stop": [{"hooks": [{"type": "command", "command": sys.argv[1]}]}]}}))' "$hook")"
  done_n=0
  while :; do
    [[ -f "$mark/stopping" ]] && { echo "launcher stopped: no new batch"; break; }
    [[ $rounds -gt 0 && $done_n -ge $rounds ]] && break
    left="$(todo_left)"
    [[ $left -le 0 ]] && { echo "no todo icons left"; break; }
    o=$off; [[ $left -le $o ]] && o=0
    done_n=$((done_n + 1))
    printf '\033]0;corner-review offset %s · batch %s\007' "$o" "$done_n"
    echo "$(date +%H:%M) /corner-review-next --take $take --offset $o  ($left todo)"
    claude --dangerously-skip-permissions --settings "$settings" "/corner-review-next --take $take --offset $o"
    echo "$(date +%H:%M) batch $done_n done (claude exit $?)"
  done
  echo "$done_n" > "$mark/slot-$off"
  exit 0
fi

SEQ=0
if [[ "${1:-}" == "--seq" ]]; then SEQ=1; shift; fi
OFFSETS=("$@")
if [[ ${#OFFSETS[@]} -eq 0 ]]; then OFFSETS=(0 10 20 30 40 50); fi
if [[ $SEQ -eq 1 ]]; then OFFSETS=("${OFFSETS[0]}"); fi
MARK="$(mktemp -d)" || exit 1

trap 'touch "$MARK/stopping"; echo " stopping: no new batches, running batches finish first"' INT

WIN=()
for off in "${OFFSETS[@]}"; do
  WIN+=("$(osascript -e "tell application \"Terminal\"
    do script \"exec '$SELF' --slot $off $TAKE $ROUNDS '$MARK'\"
    return id of front window
  end tell")")
  echo "$(date +%H:%M) slot $off started"
done

LEFT=("${!OFFSETS[@]}")
while [[ ${#LEFT[@]} -gt 0 ]]; do
  sleep 5
  NEXT=()
  for i in "${LEFT[@]}"; do
    off="${OFFSETS[$i]}"
    if [[ -f "$MARK/slot-$off" ]]; then
      echo "$(date +%H:%M) slot $off finished after $(cat "$MARK/slot-$off") batch(es)"
      osascript -e "tell application \"Terminal\" to close (every window whose id is ${WIN[$i]})" >/dev/null 2>&1
    else
      NEXT+=("$i")
    fi
  done
  LEFT=("${NEXT[@]}")
done
rm -rf "$MARK"
echo "all slots finished"
