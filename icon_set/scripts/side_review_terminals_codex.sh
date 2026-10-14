#!/bin/bash
# The 64 side pairs reviewed by Codex instead of Claude: keep Terminal windows running /side-layout-adjust batches with
# `codex --sandbox danger-full-access -a never exec "<prompt>"` until no unreviewed 64 pair is left. Same batching as
# side_review_terminals.sh (it can run next to the 72 Claude launcher: different work folders).
#
#   side_review_terminals_codex.sh               6 Codex windows at once, 10 unreviewed pairs per batch
#   side_review_terminals_codex.sh 4             4 windows
#   TAKE=5 side_review_terminals_codex.sh        batch size (default 10)
#   EFFORT=medium side_review_terminals_codex.sh reasoning effort for the review (default: medium; your config says low)
#   MODEL=gpt-6-astra side_review_terminals_codex.sh   model (default: gpt-6-sol; list: codex debug models)
#   ROUNDS=3 / FILTER=--auto / IDS_FILE=list.tsv      as in side_review_terminals.sh
#
# Codex has no Claude skills or hooks: each batch prompt tells it to read .claude/skills/side-layout-adjust/SKILL.md
# and follow it, and the batch ends when codex exits (the window then closes). Pairs it leaves without a verdict stay
# unreviewed and are not handed out again in this run.
SELF="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
TAKE="${TAKE:-10}"
ROUNDS="${ROUNDS:-0}"
FILTER="${FILTER:-}"
IDLE="${IDLE:-600}"   # seconds a stopped batch with pairs left may sit idle before it is closed
EFFORT="${EFFORT:-medium}"
MODEL="${MODEL:-gpt-6-sol}"   # in your account's Codex model catalog (codex debug models); config.toml's gpt-6.1-sol is rejected
RECHECK="${RECHECK:-0}"
IDS_FILE="${IDS_FILE:-}"   # review again exactly the reference ids in this file (first column), with --recheck
if [[ -n "$IDS_FILE" ]]; then IDS_FILE="$(cd "$(dirname "$IDS_FILE")" && pwd)/$(basename "$IDS_FILE")"; RECHECK=1; fi
SINCE="${SINCE:-}"
OLDER_THAN="${OLDER_THAN:-}"   # with RECHECK=1: also redo every fix/redraw recorded before this ISO time

# Inside a new window: run one batch with codex exec, then leave a marker for the launcher.
if [[ "${1:-}" == "--run" ]]; then
  name="$2"; marker="$3"; shift 3
  cd "$REPO" || exit 1
  printf '\033]0;codex side-layout-adjust %s\007' "$name"
  recheck=""
  if [[ "${1:-}" == "--recheck" ]]; then recheck="--recheck "; shift; fi
  model_id="${MODEL:-$(sed -n 's/^model *= *"\(.*\)"/\1/p' "$HOME/.codex/config.toml" | head -1)}"
  prompt="You are reviewing Pictographic side combinations (64 build) in the repo $REPO.
Read .claude/skills/side-layout-adjust/SKILL.md in full first and follow it exactly, as if it were invoked as:
/side-layout-adjust ${recheck}$*
- The work folders are prefetched in icon_set/work/side-layout-adjust/<id>/: when a folder has fetch.json and no
  review.json, do not fetch again; read fetch.json (and its snap block).
- Look at the pictures the skill names (current@4x.png, main@4x.png, sub@4x.png, overlap-current.png, search.png,
  proposed@4x.png, hull-current.png) with your image viewing tool before every verdict; the scripts are a reference.
- Run every node command from the repo root. Record every pair with node icon_set/scripts/side_review_record.mjs,
  passing --model ${model_id:-codex} as the model id.
- Work the batch in the foreground and finish every pair before you stop. Do not push to production, do not edit
  files outside these work folders, do not commit.
At the end print one line per pair: concept, verdict, the change proposed (or none)."
  echo "codex review batch $name: $*"
  codex --sandbox danger-full-access -a never ${MODEL:+-m "$MODEL"} -c model_reasoning_effort="$EFFORT" exec -C "$REPO" "$prompt"
  echo "$?" > "$marker"
  echo "batch $name finished (exit $(cat "$marker")); this window closes shortly"
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
    [[ "$REPO/icon_set/work/side-layout-adjust/$id/review.json" -nt "$MARK/$1.start" ]] || return 1
  done < "$MARK/$1.ids"
}

check_batch() {  # $1 = batch name, $2 = window id; returns 0 once its window is closed
  # codex exec exits at the end of its batch and leaves the marker.
  [[ -f "$MARK/$1" ]] || return 1
  batch_done "$1" || echo "$(date +%H:%M) batch $1 ended with pairs unrecorded (they stay unreviewed)"
  sleep 3
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
# Refresh the review pages with every verdict the batches recorded.
for r in "$REPO"/icon_set/work/side-overlap-audit/*/review.py; do
  [[ -f "$r" ]] && /opt/homebrew/bin/python3 "$r" | tail -1
done
echo "all batches finished"
