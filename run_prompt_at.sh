#!/bin/zsh
# Wait until a clock time (default 04:00), then open N Terminal windows,
# start claude in each one with the contents of prompt.md as the first prompt.
#
#   ./run_prompt_at.sh            # 1 terminal at 04:02
#   ./run_prompt_at.sh 5          # 5 terminals at 04:02
#   ./run_prompt_at.sh 5 16:00    # 5 terminals at 16:00
#
# Env: CLAUDE_CMD (default: "claude --dangerously-skip-permissions"),
#      STAGGER seconds between windows (default 20).

COUNT=${1:-1}
AT=${2:-04:02}
DIR="/Applications/Workspaces/pictographic/claude_skills"
PROMPT_FILE="$DIR/prompt.md"
CLAUDE_CMD=${CLAUDE_CMD:-"claude --dangerously-skip-permissions"}
STAGGER=${STAGGER:-20}

now=$(date +%s)
target=$(date -j -f "%H:%M:%S" "${AT}:00" +%s) || exit 1
(( target <= now )) && target=$(( target + 86400 ))
wait=$(( target - now ))
echo "Will open $COUNT terminal(s) at $(date -r $target '+%Y-%m-%d %H:%M') (in $((wait/3600))h $((wait%3600/60))m)."
echo "Keep this window open and the Mac awake (lid open / on power)."

# caffeinate keeps the Mac from idle-sleeping while we wait
caffeinate -i -s sleep $wait

if [[ ! -s "$PROMPT_FILE" ]]; then
  echo "$(date '+%H:%M') prompt.md is empty - nothing sent." >&2
  exit 1
fi

# Snapshot the prompt so every window gets the same text even if the file changes
SNAP=$(mktemp /tmp/prompt.XXXXXX)
cp "$PROMPT_FILE" "$SNAP"

for i in $(seq 1 $COUNT); do
  osascript <<OSA
tell application "Terminal"
  activate
  do script "cd '$DIR' && $CLAUDE_CMD \"\$(cat '$SNAP')\""
end tell
OSA
  echo "$(date '+%H:%M:%S') opened terminal $i/$COUNT"
  (( i < COUNT )) && sleep $STAGGER
done
