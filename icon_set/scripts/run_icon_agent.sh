#!/usr/bin/env bash
# run_icon_agent.sh WORKSPACE PROMPT_FILE [MODEL] [IMAGE...]
set -euo pipefail
if [[ ${1:-} == generate || ${1:-} == fix ]]; then
  script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
  exec "${PYTHON_BIN:-python3}" "$script_dir/submit_generation.py" "$@"
fi
if [[ $# -lt 2 ]]; then
  echo 'Usage: run_icon_agent.sh WORKSPACE PROMPT_FILE [MODEL] [IMAGE...]' >&2
  exit 2
fi
workspace=$(cd -- "$1" && pwd)
prompt_file=$2
model=${3:-}
shift $(( $# < 3 ? $# : 3 ))
runner=${CODEX_BIN:-codex}
args=(-a never exec --sandbox workspace-write --skip-git-repo-check -C "$workspace")
if [[ -n $model ]]; then args+=(--model "$model"); fi
args+=(-)
# The stdin marker goes first: --image takes several values and would swallow it.
for image in "$@"; do args+=("--image=$image"); done
exec "$runner" "${args[@]}" < "$prompt_file"
