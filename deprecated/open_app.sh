#!/bin/sh
# Starts the local Profile Manager and opens its session URL.
# Usage: ./open_app.sh [--port NUMBER] [--no-open]
exec python3 "$(dirname "$0")/core/profile_manager.py" "$@"
