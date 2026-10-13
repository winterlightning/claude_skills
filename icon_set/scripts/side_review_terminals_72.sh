#!/bin/bash
# The icon-72 side pairs (main-54 + sub-36): keep Terminal windows running /side-layout-adjust-72 batches until no
# unreviewed 72 pair is left. Same as side_review_terminals.sh (64), which can run at the same time: the two use
# different work folders (side-layout-adjust-72 vs side-layout-adjust), so they never pick the same pair.
# Keep Terminal windows running /side-layout-adjust-72 batches until no unreviewed pair is left.
# Every batch runs in its own window with a fresh `claude --dangerously-skip-permissions`;
# when the batch finishes the window closes and a new window starts the next batch in that slot.
#
#   side_review_terminals.sh               6 slots at once, 10 unreviewed pairs per batch
#   side_review_terminals.sh 3             3 slots at once
#   side_review_terminals.sh --seq         one window at a time
#   TAKE=5 side_review_terminals.sh        batch size (default 10)
#   ROUNDS=3 side_review_terminals.sh      stop each slot after 3 batches (default 0 = until none left)
#   FILTER=--auto side_review_terminals.sh only pairs on automatic placement (or --hand)
#   RECHECK=1 side_review_terminals.sh    review again the pairs whose review breaks the keyshape system
#                                          (side_keyshape_check.mjs --recheck), with /side-layout-adjust --recheck
#   RECHECK=1 SINCE=2026-10-09 ...          only reviews recorded on or after that day
#   IDS_FILE=list.tsv ...                    review again exactly the pairs in the file (one id per line, first column)
#   RECHECK=1 OLDER_THAN=2026-10-09T09:50:45Z ...   also redo fixes / redraws made before that skill change
#
# The launcher picks each batch's reference ids itself, skipping the pairs any running window
# already holds, so parallel windows never review the same pair (an --offset into the
# --unreviewed list shifts as pairs get recorded). Keep this launcher running: it closes
# finished windows, opens the next ones and at the end refreshes the review pages.
# Ctrl-C stops starting new batches (running windows keep going).

SELF="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
# Every side tool reads the combination size from here (side_compose.mjs), and the windows inherit it.
export SIDE_SIZE=72
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
TAKE="${TAKE:-10}"
ROUNDS="${ROUNDS:-0}"
FILTER="${FILTER:-}"
IDLE="${IDLE:-600}"   # seconds a stopped batch with pairs left may sit idle before it is closed
RECHECK="${RECHECK:-0}"
IDS_FILE="${IDS_FILE:-}"   # review again exactly the reference ids in this file (first column), with --recheck
if [[ -n "$IDS_FILE" ]]; then IDS_FILE="$(cd "$(dirname "$IDS_FILE")" && pwd)/$(basename "$IDS_FILE")"; RECHECK=1; fi
SINCE="${SINCE:-}"
OLDER_THAN="${OLDER_THAN:-}"   # with RECHECK=1: also redo every fix/redraw recorded before this ISO time

# Inside a new window: run one batch, then leave a marker for the launcher.
if [[ "${1:-}" == "--run" ]]; then
  name="$2"; marker="$3"; shift 3
  cd "$REPO" || exit 1
  printf '\033]0;side-layout-adjust-72 %s\007' "$name"
  echo "/side-layout-adjust-72 $*"
  # Interactive claude never exits on its own: a Stop hook marks each end of a turn (.stop) and a PreToolUse hook
  # marks work (.busy). The launcher ends this claude once every pair has a new verdict, or once it has sat idle
  # after a stop: a turn can end while the session waits for its own background job, which is not the end of the batch.
  claude --dangerously-skip-permissions \
    --settings "{\"hooks\":{\"Stop\":[{\"hooks\":[{\"type\":\"command\",\"command\":\"touch '$marker.stop'\"}]}],\"PreToolUse\":[{\"hooks\":[{\"type\":\"command\",\"command\":\"touch '$marker.busy'\"}]}]}}" \
    "/side-layout-adjust-72 $*"
  echo "$?" > "$marker"
  exit 0
fi

SEQ=0
if [[ "${1:-}" == "--seq" ]]; then SEQ=1; shift; fi
SLOTS="${1:-6}"
if [[ $SEQ -eq 1 ]]; then SLOTS=1; fi
MARK="$(mktemp -d)" || exit 1
# Remove only the launcher's own temp folder (never an empty or other path).
cleanup() { [[ -n "$MARK" && -d "$MARK" && "$MARK" == */tmp.* ]] && rm -r "$MARK"; }

# The next TAKE unreviewed pair ids that no running window holds, one per line.
next_ids() {
  local held
  # Also skip every id handed out earlier in this run: a pair the skill stops on without a
  # verdict (rebuild_change main, fetch refusal) stays unreviewed and would be picked again forever.
  held="$(cat "$MARK"/*.ids "$MARK/handed-out" 2>/dev/null)"
  if [[ -n "$IDS_FILE" ]]; then
    grep -v "^#" "$IDS_FILE" | cut -f1 | grep .
  elif [[ "$RECHECK" == 1 ]]; then
    (cd "$REPO" && node icon_set/scripts/side_keyshape_check.mjs --recheck ${SINCE:+--since "$SINCE"} ${OLDER_THAN:+--older-than "$OLDER_THAN"} 2>/dev/null)
  else
    (cd "$REPO" && node icon_set/scripts/side_layout.mjs list --limit $((TAKE + SLOTS * TAKE)) --unreviewed $FILTER 2>/dev/null) \
      | awk -F'\t' 'NF > 3 {print $1}'
  fi \
    | grep -v -x -F -f <(printf '%s\n' "$held" | grep .) 2>/dev/null \
    | head -n "$TAKE"
}

open_window() {  # $1 = batch name, rest = reference ids; prints the window id
  local name="$1"; shift
  osascript -e "tell application \"Terminal\"
    activate
    do script \"exec '$SELF' --run $name '$MARK/$name' $*\"
    return id of front window
  end tell"
}

# Every pair of batch $1 has a review.json written after the batch started.
batch_done() {
  local id
  while read -r id; do
    [[ -n "$id" ]] || continue
    [[ "$REPO/icon_set/work/side-layout-adjust-72/$id/review.json" -nt "$MARK/$1.start" ]] || return 1
  done < "$MARK/$1.ids"
}

check_batch() {  # $1 = batch name, $2 = window id; returns 0 once its window is closed
  local stop="$MARK/$1.stop" busy="$MARK/$1.busy"
  # A turn ended and no tool ran since: done when every pair is recorded, else after IDLE seconds of quiet
  # (a pair the skill skips on purpose, such as rebuild_change main, never gets a verdict).
  if [[ -f "$stop" && ! "$busy" -nt "$stop" ]]; then
    local age=$(( $(date +%s) - $(stat -f %m "$stop") ))
    if batch_done "$1" || (( age > IDLE )); then
      sleep 3
      pkill -f "$stop"
      rm -f "$stop"
      batch_done "$1" || echo "$(date +%H:%M) batch $1 idle $((age / 60)) min with pairs unrecorded, closing it"
    fi
  fi
  [[ -f "$MARK/$1" ]] || return 1
  sleep 1
  osascript -e "tell application \"Terminal\" to close (every window whose id is $2)" >/dev/null 2>&1
  rm -f "$MARK/$1.ids"
  echo "$(date +%H:%M) batch $1 done, window closed"
}

STOPPING=0
trap 'STOPPING=1; echo " stopping: no new batches, running windows keep going"' INT

# Slot i: NAME/WIN hold its current batch, DONE counts its batches.
NAME=(); WIN=(); DONE=()
start_slot() {  # $1 = slot; returns 1 when the slot should stop
  local i="$1" ids
  [[ $STOPPING -eq 1 ]] && return 1
  [[ $ROUNDS -gt 0 && ${DONE[$i]:-0} -ge $ROUNDS ]] && return 1
  ids=($(next_ids))
  if [[ ${#ids[@]} -eq 0 ]]; then if [[ "$RECHECK" == 1 ]]; then echo "slot $((i + 1)): recheck list empty (no off-system review left${SINCE:+ since $SINCE})"; else echo "slot $((i + 1)): no unreviewed pairs left"; fi; return 1; fi
  NAME[$i]="s$((i + 1))-r$(( ${DONE[$i]:-0} + 1 ))"
  printf '%s\n' "${ids[@]}" > "$MARK/${NAME[$i]}.ids"
  touch "$MARK/${NAME[$i]}.start"
  printf '%s\n' "${ids[@]}" >> "$MARK/handed-out"
  if [[ "$RECHECK" == 1 ]]; then WIN[$i]="$(open_window "${NAME[$i]}" --recheck "${ids[@]}")"
  else WIN[$i]="$(open_window "${NAME[$i]}" "${ids[@]}")"; fi
  echo "$(date +%H:%M) batch ${NAME[$i]} started: ${#ids[@]} pairs, ${ids[0]} .. ${ids[${#ids[@]}-1]}"
}

ACTIVE=()
for ((i = 0; i < SLOTS; i++)); do
  start_slot "$i" && ACTIVE+=("$i")
  sleep 2
done
while [[ ${#ACTIVE[@]} -gt 0 ]]; do
  NEXT=()
  for i in "${ACTIVE[@]}"; do
    if check_batch "${NAME[$i]}" "${WIN[$i]}"; then
      DONE[$i]=$(( ${DONE[$i]:-0} + 1 ))
      start_slot "$i" && NEXT+=("$i")
    else
      NEXT+=("$i")
    fi
  done
  ACTIVE=("${NEXT[@]}")
  [[ ${#ACTIVE[@]} -gt 0 ]] && sleep 5
done
cleanup
# Refresh the 72 review page data (icon_set/work/side-72, the page reads it on reload).
(cd "$REPO" && node icon_set/scripts/side72_fetch.mjs | tail -1)
echo "all batches finished"
