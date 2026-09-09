#!/usr/bin/env bash
# run_icon_agent.sh WORKSPACE PROMPT_FILE [MODEL]
set -euo pipefail
if [[ ${1:-} == generate || ${1:-} == fix ]]; then
  script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
  exec "${PYTHON_BIN:-python3}" "$script_dir/submit_generation.py" "$@"
fi
if [[ $# -lt 2 || $# -gt 3 ]]; then
  echo 'Usage: run_icon_agent.sh WORKSPACE PROMPT_FILE [MODEL]' >&2
  exit 2
fi
workspace=$(cd -- "$1" && pwd)
prompt_file=$2
runner=${CODEX_BIN:-codex}
args=(-a never exec --sandbox workspace-write --skip-git-repo-check -C "$workspace")
if [[ -n ${3:-} ]]; then args+=(--model "$3"); fi
exec "$runner" "${args[@]}" - < "$prompt_file"
