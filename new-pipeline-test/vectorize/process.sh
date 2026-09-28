#!/bin/bash
# process.sh — PNG -> one combined 1024x1024 SVG, saved next to the PNG.
#
# Usage:  ./process.sh input.png [more.png ...]
#         NO_PREPROCESS=1 ./process.sh input.png        # feed the PNG to png2svg untouched
#         NO_SNAP=1 ./process.sh input.png              # skip the keyshape stretch-to-fit snap
#
# Stages (the raw vectorizing stage of pg_app_utility/png_to_svg_new/process.sh):
#   1. pre_process_input.py   flatten transparency onto white, collapse all ink to black
#   2. png2svg                trace the PNG into one SVG per connected component
#   3. combine_svgs.py        merge the parts, step-8 normalize onto 1024x1024, keyshape snap
#
# Output: only <stem>_raw.svg (fitted to 1024x1024, keyshape-snapped), written
# in the same folder as the input PNG. The intermediates (prepped PNG,
# per-object __N.svg parts, pre-snap SVG) live in a temp dir that is deleted
# afterwards; the part count is printed on the "done:" line.
set -euo pipefail
shopt -s nullglob

HERE="$(cd "$(dirname "$0")" && pwd)"

# freshly copied-in binaries often lack the execute bit — self-heal
for bin in "$HERE/png2svg" "$HERE/holecmp"; do
    [ -f "$bin" ] && [ ! -x "$bin" ] && chmod +x "$bin"
done

if [ $# -lt 1 ]; then
    echo "usage: $0 input.png [more.png ...]" >&2
    exit 1
fi

snap_flag=""
[ "${NO_SNAP:-0}" = "1" ] && snap_flag="--no-snap"

work="$(mktemp -d "${TMPDIR:-/tmp}/vectorize.XXXXXX")"
trap 'rm -rf "$work"' EXIT

for png in "$@"; do
    if [ ! -f "$png" ]; then
        echo "skip: $png (not found)" >&2
        continue
    fi
    stem="$(basename "$png")"
    stem="${stem%.*}"
    outdir="$(cd "$(dirname "$png")" && pwd)"
    tmp="$work/$stem"
    rm -rf "$tmp"
    mkdir -p "$tmp"

    if [ "${NO_PREPROCESS:-0}" != "1" ]; then
        if ! python3 "$HERE/pre_process_input.py" "$png" \
                -o "$tmp/prepped/$stem.png" >/dev/null; then
            echo "error: $stem — pre_process_input failed" >&2
            exit 1
        fi
        png="$tmp/prepped/$stem.png"
    fi

    "$HERE/png2svg" "$png" --svg-dir "$tmp"
    parts=("$tmp/$stem"__*.svg)
    if [ ${#parts[@]} -eq 0 ]; then
        echo "error: png2svg produced no object SVGs for $stem" >&2
        exit 1
    fi
    python3 "$HERE/combine_svgs.py" "${parts[@]}" $snap_flag \
        -o "$tmp/${stem}_final.svg"
    mv "$tmp/${stem}_final.svg" "$outdir/${stem}_raw.svg"

    echo "done: $outdir/${stem}_raw.svg (${#parts[@]} parts)"
done
