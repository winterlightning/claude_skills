#!/usr/bin/env bash
# run_icon_agent.sh WORKSPACE PROMPT_FILE [MODEL]
set -euo pipefail
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
