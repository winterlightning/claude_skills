#!/usr/bin/env bash
set -euo pipefail

# Run prompt batches through five concurrent Codex Terminal sessions.
# Usage:
#   ./run-codex-batches.sh
#   ./run-codex-batches.sh --status
#   ./run-codex-batches.sh --reset

PROMPT_FILE="${PROMPT_FILE:-/Users/jakes/Downloads/claude_skills/copy-prompts.txt}"
REPO_DIR="${REPO_DIR:-/Users/jakes/Downloads/claude_skills}"
WORKERS="${WORKERS:-5}"
BATCHES_PER_SESSION="${BATCHES_PER_SESSION:-1}"
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
STATE_DIR="${STATE_DIR:-$(dirname "$SCRIPT_PATH")/.codex-batch-runner/copy-prompts}"
PROMPTS_DIR="$STATE_DIR/prompts"
DONE_DIR="$STATE_DIR/done"
LOG_DIR="$STATE_DIR/logs"
RUN_DIR="$STATE_DIR/running"

fail() {
  printf 'Error: %s\n' "$*" >&2
  exit 1
}

prepare() {
  [[ -f "$PROMPT_FILE" ]] || fail "Prompt file not found: $PROMPT_FILE"
  [[ -d "$REPO_DIR" ]] || fail "Repository directory not found: $REPO_DIR"
  command -v codex >/dev/null 2>&1 || fail "codex is not available in PATH"
  command -v python3 >/dev/null 2>&1 || fail "python3 is not available in PATH"

  mkdir -p "$PROMPTS_DIR" "$DONE_DIR" "$LOG_DIR" "$RUN_DIR"
  rm -f "$PROMPTS_DIR"/*.txt

  python3 - "$PROMPT_FILE" "$PROMPTS_DIR" <<'PY'
from pathlib import Path
import re
import sys

source = Path(sys.argv[1]).read_text(encoding="utf-8")
out_dir = Path(sys.argv[2])
blocks = [part.strip() for part in re.split(r"(?m)^─+\s*$", source) if part.strip()]
if not blocks:
    raise SystemExit("No prompt batches were found")
for index, block in enumerate(blocks, 1):
    (out_dir / f"batch-{index:03d}.txt").write_text(block + "\n", encoding="utf-8")
print(len(blocks))
PY
}

ensure_prepared() {
  if [[ ! -f "$PROMPTS_DIR/batch-001.txt" ]]; then
    prepare >/dev/null
  fi
}

show_status() {
  local total done_count running_count
  total=$(find "$PROMPTS_DIR" -type f -name 'batch-*.txt' 2>/dev/null | wc -l | tr -d ' ')
  done_count=$(find "$DONE_DIR" -type f -name 'batch-*.done' 2>/dev/null | wc -l | tr -d ' ')
  running_count=$(find "$RUN_DIR" -type f -name 'worker-*.pid' 2>/dev/null | wc -l | tr -d ' ')
  printf 'Completed: %s/%s\nActive workers: %s\nState: %s\n' "$done_count" "$total" "$running_count" "$STATE_DIR"
}

worker() {
  local worker_id="$1" total group_number group_start group_end batch_number
  local prompt_path batch_name exit_code log_file combined_prompt batch_names session_name
  printf '%s\n' "$$" > "$RUN_DIR/worker-$worker_id.pid"
  trap 'rm -f "$RUN_DIR/worker-'"$worker_id"'.pid"' EXIT INT TERM

  total=$(find "$PROMPTS_DIR" -type f -name 'batch-*.txt' | wc -l | tr -d ' ')
  group_number=1
  group_start=1
  while (( group_start <= total )); do
    group_end=$((group_start + BATCHES_PER_SESSION - 1))
    (( group_end > total )) && group_end=$total

    # Five workers process five groups concurrently. Every group gets a fresh Codex context.
    if (( (group_number - 1) % WORKERS + 1 != worker_id )); then
      group_number=$((group_number + 1))
      group_start=$((group_start + BATCHES_PER_SESSION))
      continue
    fi

    combined_prompt=""
    batch_names=""
    for ((batch_number=group_start; batch_number<=group_end; batch_number++)); do
      batch_name=$(printf 'batch-%03d' "$batch_number")
      [[ -f "$DONE_DIR/$batch_name.done" ]] && continue
      prompt_path="$PROMPTS_DIR/$batch_name.txt"
      [[ -f "$prompt_path" ]] || continue
      if [[ -n "$combined_prompt" ]]; then
        combined_prompt+=$'\n\n────────────────────\n\n'
      fi
      combined_prompt+="$(cat "$prompt_path")"
      batch_names+="$batch_name"$'\n'
    done

    if [[ -z "$combined_prompt" ]]; then
      group_number=$((group_number + 1))
      group_start=$((group_start + BATCHES_PER_SESSION))
      continue
    fi

    session_name=$(printf 'session-%03d_batches-%03d-%03d' "$group_number" "$group_start" "$group_end")
    log_file="$LOG_DIR/$session_name.log"
    printf '\n[%s] Worker %s starting %s in one Codex session\n' "$(date '+%F %T')" "$worker_id" "$session_name" | tee -a "$log_file"

    set +e
    # Codex's interactive UI requires a terminal. `script` supplies a PTY and
    # records the session without turning Codex stdout into a pipe.
    script -q -a -e "$log_file" codex -a never -C "$REPO_DIR" "$combined_prompt"
    exit_code=$?
    set -e

    if (( exit_code == 0 )); then
      while IFS= read -r batch_name; do
        [[ -n "$batch_name" ]] || continue
        printf '%s\n' "completed $(date '+%F %T') by worker $worker_id in $session_name" > "$DONE_DIR/$batch_name.done"
      done <<< "$batch_names"
      printf '[%s] Worker %s completed %s\n' "$(date '+%F %T')" "$worker_id" "$session_name" | tee -a "$log_file"
    else
      printf '[%s] Worker %s: %s failed (exit %s); continuing\n' "$(date '+%F %T')" "$worker_id" "$session_name" "$exit_code" | tee -a "$log_file"
    fi

    group_number=$((group_number + 1))
    group_start=$((group_start + BATCHES_PER_SESSION))
  done

  printf '\nWorker %s has no more batches.\n' "$worker_id"
  show_status
}

case "${1:-}" in
  --worker)
    [[ "${2:-}" =~ ^[1-9][0-9]*$ ]] || fail "Invalid worker number"
    command -v codex >/dev/null 2>&1 || fail "codex is not available in PATH"
    ensure_prepared
    worker "$2"
    ;;
  --status)
    ensure_prepared
    show_status
    ;;
  --reset)
    rm -rf "$STATE_DIR"
    printf 'Cleared batch state: %s\n' "$STATE_DIR"
    ;;
  -h|--help)
    sed -n '3,8p' "$0"
    ;;
  "")
    [[ "$WORKERS" =~ ^[1-9][0-9]*$ ]] || fail "WORKERS must be a positive integer"
    [[ "$BATCHES_PER_SESSION" =~ ^[1-9][0-9]*$ ]] || fail "BATCHES_PER_SESSION must be a positive integer"
    total=$(prepare) || exit 1

    # Refuse a second launcher while worker processes from this run are alive.
    active=0
    for pid_file in "$RUN_DIR"/worker-*.pid; do
      [[ -f "$pid_file" ]] || continue
      pid=$(cat "$pid_file" 2>/dev/null || true)
      if [[ "$pid" =~ ^[0-9]+$ ]] && kill -0 "$pid" 2>/dev/null; then
        active=$((active + 1))
      else
        rm -f "$pid_file"
      fi
    done
    (( active == 0 )) || fail "$active worker(s) are already running. Use --status to inspect progress."

    printf 'Found %s batches. Opening %s Terminal sessions...\n' "$total" "$WORKERS"
    for ((worker_id=1; worker_id<=WORKERS; worker_id++)); do
      command="$(printf '%q ' "$SCRIPT_PATH" --worker "$worker_id")"
      osascript -e 'tell application "Terminal"' \
                -e "do script \"$command\"" \
                -e 'activate' \
                -e 'end tell' >/dev/null
    done
    printf 'Started. Check progress with: %q --status\n' "$SCRIPT_PATH"
    ;;
  *)
    fail "Unknown option: $1"
    ;;
esac
