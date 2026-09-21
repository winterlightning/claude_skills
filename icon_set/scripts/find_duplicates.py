#!/usr/bin/env python3
"""Find assets that are drawn identically, or nearly so.

Two detectors run over every ``*.svg`` under a root folder (default ``published/``):

1. **exact** -- the SVG geometry is normalised (title, ids, whitespace and
   colour stripped) and hashed. Files with the same hash are the same drawing
   even if they were saved under different names.
2. **similar** -- every SVG is rasterised onto a fixed square grid and turned
   into an ink mask. Two icons are scored by IoU (intersection over union of
   their ink pixels), which is reported as a percentage. 100% means the two
   renders are pixel-identical.

Rasters are cached in an ``.npz`` file so re-runs with a different threshold
are instant.

Examples::

    python icon_set/scripts/find_duplicates.py                    # >= 90 %
    python icon_set/scripts/find_duplicates.py --min 0.8 --top 200
    python icon_set/scripts/find_duplicates.py --root published/solo48 --json dups.json
    python icon_set/scripts/find_duplicates.py --within-folder    # only compare siblings
    python icon_set/scripts/find_duplicates.py --exact-only       # skip rasterising
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ROOT = ROOT / "published"
DEFAULT_CACHE = ROOT / "icon_set" / "state" / "find_duplicates_cache.npz"

# ---------------------------------------------------------------- exact hash

_TITLE_RE = re.compile(r"<title>.*?</title>", re.S)
_ATTR_RE = re.compile(r'\s(?:id|class|data-[\w-]+|aria-[\w-]+)="[^"]*"')
_COLOR_RE = re.compile(r'\s(?:stroke|fill|color)="[^"]*"')
_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_WS_RE = re.compile(r"\s+")
_NUM_RE = re.compile(r"-?\d+\.\d+")


def _round_numbers(text: str) -> str:
    # 12.0000001 and 12 are the same coordinate.
    return _NUM_RE.sub(lambda m: f"{float(m.group()):g}", text)


def normalise_svg(text: str) -> str:
    text = _COMMENT_RE.sub("", text)
    text = _TITLE_RE.sub("", text)
    text = _ATTR_RE.sub("", text)
    text = _COLOR_RE.sub("", text)
    text = _round_numbers(text)
    text = _WS_RE.sub(" ", text)
    text = text.replace("> <", "><").strip()
    return text


def geometry_hash(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    return hashlib.sha1(normalise_svg(text).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- rasterise

_CURRENT_COLOR_RE = re.compile(r"currentColor", re.I)


def rasterise(args: tuple[str, int]) -> np.ndarray:
    """Return a packed (uint8) ink mask of ``size*size`` bits for one SVG."""
    path, size = args
    try:
        import cairosvg
        from PIL import Image
        import io

        text = Path(path).read_text(encoding="utf-8", errors="replace")
        text = _CURRENT_COLOR_RE.sub("#000000", text)
        png = cairosvg.svg2png(
            bytestring=text.encode("utf-8"),
            output_width=size,
            output_height=size,
        )
        alpha = np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"))[..., 3]
        mask = alpha > 127
    except Exception:  # broken SVG: treat as empty so it never matches
        mask = np.zeros((size, size), dtype=bool)
    return np.packbits(mask.ravel())


def load_or_build_rasters(
    files: list[Path], size: int, cache: Path, workers: int, quiet: bool
) -> np.ndarray:
    """Return a bool matrix (n_files, size*size). Uses/updates the cache."""
    def mtime(p: Path) -> int:
        try:
            return int(p.stat().st_mtime)
        except OSError:  # file vanished mid-run (parallel build); still hashed by path
            return -1

    keys = [f"{p}|{mtime(p)}|{size}" for p in files]
    cached: dict[str, np.ndarray] = {}
    if cache.exists():
        try:
            with np.load(cache, allow_pickle=False) as z:
                cached = dict(zip(z["keys"].tolist(), z["packed"]))
        except Exception:
            cached = {}

    todo = [(i, p) for i, (p, k) in enumerate(zip(files, keys)) if k not in cached]
    packed = [cached.get(k) for k in keys]
    if todo:
        if not quiet:
            print(f"rasterising {len(todo)} of {len(files)} files at {size}px "
                  f"({workers} workers)...", file=sys.stderr)
        with ProcessPoolExecutor(max_workers=workers) as pool:
            jobs = [(str(p), size) for _, p in todo]
            for n, (idx, result) in enumerate(
                zip((i for i, _ in todo), pool.map(rasterise, jobs, chunksize=64)), 1
            ):
                packed[idx] = result
                if not quiet and n % 5000 == 0:
                    print(f"  {n}/{len(todo)}", file=sys.stderr)
        cache.parent.mkdir(parents=True, exist_ok=True)
        keep_keys = list(cached.keys()) + [keys[i] for i, _ in todo]
        keep_packed = list(cached.values()) + [packed[i] for i, _ in todo]
        np.savez_compressed(
            cache, keys=np.array(keep_keys), packed=np.stack(keep_packed)
        )
    stacked = np.stack(packed)
    return np.unpackbits(stacked, axis=1)[:, : size * size].astype(bool)


# ---------------------------------------------------------------- similarity


def similar_pairs(
    masks: np.ndarray,
    threshold: float,
    group_of: np.ndarray | None,
    block: int = 1024,
    quiet: bool = False,
):
    """Yield (i, j, iou) for i < j with iou >= threshold.

    Uses a blocked matmul: intersection = A_block @ A.T, union from ink counts.
    """
    a = masks.astype(np.float32)
    counts = a.sum(axis=1)
    n = len(a)
    at = a.T.copy()
    for start in range(0, n, block):
        stop = min(start + block, n)
        inter = a[start:stop] @ at  # (b, n)
        union = counts[start:stop, None] + counts[None, :] - inter
        with np.errstate(divide="ignore", invalid="ignore"):
            iou = np.where(union > 0, inter / union, 0.0)
        # keep only j > i
        rows, cols = np.nonzero(iou >= threshold)
        for r, c in zip(rows, cols):
            i = start + r
            if c <= i:
                continue
            if group_of is not None and group_of[i] != group_of[c]:
                continue
            yield int(i), int(c), float(iou[r, c])
        if not quiet:
            print(f"  compared {stop}/{n}", file=sys.stderr)


def clusters(n: int, pairs) -> list[list[int]]:
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, j in pairs:
        parent[find(i)] = find(j)
    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return [g for g in groups.values() if len(g) > 1]


# ---------------------------------------------------------------- main


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                    help="folder to scan recursively for *.svg")
    ap.add_argument("--min", type=float, default=0.90,
                    help="report pairs with IoU >= this fraction (default 0.90)")
    ap.add_argument("--size", type=int, default=32,
                    help="raster grid in px (default 32; 48 is stricter/slower)")
    ap.add_argument("--within-folder", action="store_true",
                    help="only compare files that sit in the same folder")
    ap.add_argument("--exact-only", action="store_true",
                    help="only run the geometry-hash detector (no rasterising)")
    ap.add_argument("--top", type=int, default=0,
                    help="print at most N similar pairs (0 = all)")
    ap.add_argument("--json", type=Path, help="also write the full report here")
    ap.add_argument("--csv", type=Path, help="also write similar pairs as CSV")
    ap.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--exclude", action="append", default=[],
                    help="substring of a path to skip (repeatable); hidden "
                         "folders such as .icon-build-* are always skipped")
    ap.add_argument("-q", "--quiet", action="store_true")
    args = ap.parse_args(argv)

    files = sorted(
        p for p in args.root.rglob("*.svg")
        if not any(part.startswith(".") for part in p.relative_to(args.root).parts)
        and not any(x in str(p) for x in args.exclude)
        and p.is_file()
    )
    if not files:
        print(f"no .svg files under {args.root}", file=sys.stderr)
        return 1
    rel = [str(p.relative_to(args.root)) for p in files]
    if not args.quiet:
        print(f"{len(files)} svg files under {args.root}", file=sys.stderr)

    # 1. exact geometry duplicates
    by_hash: dict[str, list[int]] = defaultdict(list)
    for i, p in enumerate(files):
        h = geometry_hash(p)
        if h:
            by_hash[h].append(i)
    exact_groups = sorted(
        (v for v in by_hash.values() if len(v) > 1), key=len, reverse=True
    )

    report = {
        "root": str(args.root),
        "files": len(files),
        "exact_groups": [[rel[i] for i in g] for g in exact_groups],
    }

    print(f"# exact duplicates (same geometry): {len(exact_groups)} groups, "
          f"{sum(len(g) for g in exact_groups)} files")
    for g in exact_groups:
        print(f"  [{len(g)}]")
        for i in g:
            print(f"    {rel[i]}")

    if args.exact_only:
        if args.json:
            args.json.write_text(json.dumps(report, indent=2))
        return 0

    # 2. pixel similarity
    masks = load_or_build_rasters(files, args.size, args.cache, args.workers, args.quiet)
    group_of = None
    if args.within_folder:
        folders = {p.parent for p in files}
        ids = {f: k for k, f in enumerate(sorted(folders))}
        group_of = np.array([ids[p.parent] for p in files])

    if not args.quiet:
        print("comparing...", file=sys.stderr)
    pairs = list(similar_pairs(masks, args.min, group_of, quiet=args.quiet))
    pairs.sort(key=lambda t: -t[2])

    pixel_identical = clusters(len(files), ((i, j) for i, j, s in pairs if s >= 0.9999))
    pixel_identical.sort(key=len, reverse=True)

    print(f"\n# pixel-identical at {args.size}px: {len(pixel_identical)} groups, "
          f"{sum(len(g) for g in pixel_identical)} files")
    for g in pixel_identical:
        print(f"  [{len(g)}]")
        for i in g:
            print(f"    {rel[i]}")

    shown = pairs if not args.top else pairs[: args.top]
    print(f"\n# similar pairs (IoU >= {args.min:.0%}): {len(pairs)} pairs"
          + (f", showing {len(shown)}" if args.top and len(pairs) > args.top else ""))
    for i, j, s in shown:
        print(f"  {s:6.1%}  {rel[i]}  <->  {rel[j]}")

    empty = int((masks.sum(axis=1) == 0).sum())
    if empty:
        print(f"\n# {empty} files rendered empty (broken or blank) and were ignored")

    report.update({
        "size": args.size,
        "min_iou": args.min,
        "pixel_identical_groups": [[rel[i] for i in g] for g in pixel_identical],
        "similar_pairs": [
            {"a": rel[i], "b": rel[j], "iou": round(s, 4)} for i, j, s in pairs
        ],
        "empty": [rel[i] for i in np.nonzero(masks.sum(axis=1) == 0)[0]],
    })
    if args.json:
        args.json.write_text(json.dumps(report, indent=2))
        print(f"\nwrote {args.json}", file=sys.stderr)
    if args.csv:
        with args.csv.open("w") as fh:
            fh.write("iou,a,b\n")
            for i, j, s in pairs:
                fh.write(f"{s:.4f},{rel[i]},{rel[j]}\n")
        print(f"wrote {args.csv}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
