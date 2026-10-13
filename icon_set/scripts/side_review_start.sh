#!/bin/bash
# Start the AI layout review of every side pair nobody has reviewed yet (64 and 72 at once).
#
#   icon_set/scripts/side_review_start.sh            6 review windows for 64 + 6 for 72
#   icon_set/scripts/side_review_start.sh 4 8        4 windows for 64, 8 for 72 (0 skips a size)
#   NO_SYNC=1 icon_set/scripts/side_review_start.sh  skip the folder sync
#
# 1. Syncs the work folders with production (side_sync_folders.mjs): a pair whose main or sub changed is rebuilt (its
#    earlier review moves to the history), a pair no longer reviewable moves out, new reviewable pairs get a folder.
# 2. Prints what is left: pairs with no review.json (your "good, no review" marks and earlier AI reviews are skipped).
# 3. Opens one Terminal window per size running its launcher (side_review_terminals.sh / side_review_terminals_72.sh),
#    which keeps that many review windows busy, 10 pairs a batch, until no unreviewed pair is left.
# Progress: the reports (icon_set/work/side-layout-adjust-report/, side-layout-adjust-72-report/), or
#   node icon_set/scripts/side_review_report.mjs --watch   (SIDE_SIZE=72 for 72)
# Stop: Ctrl-C in a launcher window stops new batches; running review windows finish their batch.
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
SLOTS64="${1:-6}"
SLOTS72="${2:-6}"
cd "$REPO" || exit 1

left() {  # $1 = work folder name: pairs with fetch.json and no review.json
  local n=0 d
  for d in "icon_set/work/$1"/*/; do
    [[ -f "$d/fetch.json" && ! -f "$d/review.json" ]] && n=$((n + 1))
  done
  echo "$n"
}

if [[ "${NO_SYNC:-0}" != 1 ]]; then
  echo "syncing the work folders with production…"
  [[ "$SLOTS64" -gt 0 ]] && node icon_set/scripts/side_sync_folders.mjs 2>/dev/null | tail -1
  [[ "$SLOTS72" -gt 0 ]] && SIDE_SIZE=72 node icon_set/scripts/side_sync_folders.mjs 2>/dev/null | tail -1
fi

L64="$(left side-layout-adjust)"
L72="$(left side-layout-adjust-72)"
echo "left for the AI review: 64 = $L64 pairs, 72 = $L72 pairs"

open_launcher() {  # $1 = launcher script, $2 = slots, $3 = title
  osascript -e "tell application \"Terminal\"
    activate
    do script \"cd '$REPO' && printf '\\\\033]0;$3\\\\007' && '$REPO/icon_set/scripts/$1' $2\"
  end tell" >/dev/null
}
if [[ "$SLOTS64" -gt 0 && "$L64" -gt 0 ]]; then open_launcher side_review_terminals.sh "$SLOTS64" "launcher 64"; echo "started the 64 launcher with $SLOTS64 windows"; fi
if [[ "$SLOTS72" -gt 0 && "$L72" -gt 0 ]]; then open_launcher side_review_terminals_72.sh "$SLOTS72" "launcher 72"; echo "started the 72 launcher with $SLOTS72 windows"; fi
echo "follow progress on the reports; Ctrl-C in a launcher window stops new batches"
