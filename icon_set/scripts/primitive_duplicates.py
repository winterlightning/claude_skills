#!/usr/bin/env python3
"""Find original primitives that are the same drawing and record them as aliases.

python3 icon_set/scripts/primitive_duplicates.py                # dry run: print the groups
python3 icon_set/scripts/primitive_duplicates.py --write        # write icon_set/data/primitive-aliases.json
python3 icon_set/scripts/primitive_duplicates.py --show 40      # print more groups in the dry run
python3 icon_set/scripts/primitive_duplicates.py --iou 0.999    # stricter: pixel-identical only

Every SVG under the primitives folder is rasterised at 192px, thresholded, and
max-pooled 4x4 to a 48px ink mask (the 8-unit strokes of the 1024 artwork are
thinner than a pixel at 48px, so the pooling keeps them). Two primitives are
the same drawing when their masks have an IoU of at least ``--iou`` (default
0.99), or when their normalised SVG text is identical. Nothing is deleted: every uuid, file and database row
stays, and primitives_catalog.py folds each alias into its canonical row.

The canonical of a group is, in order: the uuid with the most linked icon
models, a named category over ``_uncategorized_*``, the lowest batch, the
shortest concept, then the path. A group whose members are unchanged keeps the
canonical recorded in the existing file, so manual overrides survive re-runs.
"""
from __future__ import annotations

import argparse
import collections
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import sys

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.find_duplicates import clusters, normalise_svg, similar_pairs  # noqa: E402

SCHEMA = 'pictographic.primitive-aliases.v1'
POLICY = ('Original artwork drawn the same: ink-mask IoU of at least {iou:.0%} at 48px after 4x max-pool, '
          'or identical normalised SVG text. Files, uuids and every row keyed by them are retained; the '
          'catalog folds aliases into the canonical row.')
DEFAULT_IOU = 0.99
DEFAULT_OUTPUT = REPO_ROOT / 'icon_set' / 'data' / 'primitive-aliases.json'
DEFAULT_CACHE = REPO_ROOT / 'icon_set' / 'state' / 'primitive_duplicates_cache.npz'
BIG, GRID = 192, 48


def rasterise(path: str) -> np.ndarray:
    """Packed 48x48 ink mask: render at 192px, alpha > 0, max-pool 4x4."""
    try:
        import cairosvg
        from PIL import Image
        png = cairosvg.svg2png(bytestring=Path(path).read_bytes(), output_width=BIG, output_height=BIG)
        alpha = np.asarray(Image.open(io.BytesIO(png)).convert('RGBA'))[..., 3] > 0
        k = BIG // GRID
        mask = alpha.reshape(GRID, k, GRID, k).max(axis=(1, 3))
    except Exception:  # unreadable artwork never matches anything
        mask = np.zeros((GRID, GRID), dtype=bool)
    return np.packbits(mask.ravel())


def load_masks(files: list[Path], cache: Path, workers: int | None, quiet: bool) -> np.ndarray:
    from concurrent.futures import ProcessPoolExecutor
    keys = [f'{p}|{int(p.stat().st_mtime)}' for p in files]
    cached: dict[str, np.ndarray] = {}
    if cache.is_file():
        try:
            with np.load(cache, allow_pickle=False) as data:
                cached = dict(zip(data['keys'].tolist(), data['packed']))
        except Exception:
            cached = {}
    todo = [i for i, key in enumerate(keys) if key not in cached]
    packed = [cached.get(key) for key in keys]
    if todo:
        if not quiet:
            print(f'rasterising {len(todo)} of {len(files)} primitives', file=sys.stderr)
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for i, result in zip(todo, pool.map(rasterise, [str(files[i]) for i in todo], chunksize=32)):
                packed[i] = result
        cache.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(cache, keys=np.array(keys), packed=np.stack(packed))
    return np.unpackbits(np.stack(packed), axis=1)[:, :GRID * GRID].astype(bool)


def find_groups(root: Path, rows: dict[str, dict], cache: Path, workers: int | None, quiet: bool,
                iou: float = DEFAULT_IOU) -> list[dict]:
    """Groups of uuids drawn identically; each carries match='pixel' or 'text'."""
    files = sorted(root / row['path'] for row in rows.values())
    uuids = [row['uuid'] for row in sorted(rows.values(), key=lambda r: root / r['path'])]
    masks = load_masks(files, cache, workers, quiet)
    if not quiet:
        print('comparing', file=sys.stderr)
    pairs = [(i, j) for i, j, score in similar_pairs(masks, iou, None, quiet=True)]
    pixel = clusters(len(files), pairs)
    text: dict[str, list[int]] = collections.defaultdict(list)
    for i, path in enumerate(files):
        digest = hashlib.sha1(normalise_svg(path.read_text(encoding='utf-8', errors='replace')).encode()).hexdigest()
        text[digest].append(i)
    match = {}
    for group in pixel:
        for i in group:
            match[i] = 'pixel'
    merged = clusters(len(files), pairs + [(g[0], i) for g in text.values() if len(g) > 1 for i in g[1:]])
    groups = []
    for group in merged:
        members = sorted(uuids[i] for i in group)
        groups.append({'members': members, 'match': 'pixel' if all(i in match for i in group) else 'text'})
    return groups


def choose_canonical(members: list[str], rows: dict[str, dict], linked: dict[str, int]) -> str:
    def rank(uid: str):
        row = rows[uid]
        return (-linked.get(uid, 0), row['category'].startswith('Uncategorized'), row['batch'] or '~',
                len(row['concept']), row['path'])
    return min(members, key=rank)


def build_aliases(groups: list[dict], rows: dict[str, dict], linked: dict[str, int], previous: dict | None,
                  iou: float = DEFAULT_IOU) -> dict:
    kept = {}
    for group in (previous or {}).get('groups', []):
        kept[tuple(sorted([group['canonical']] + group['aliases']))] = group['canonical']
    out_groups, aliases = [], {}
    for group in sorted(groups, key=lambda g: (-len(g['members']), g['members'][0])):
        members = group['members']
        canonical = kept.get(tuple(members)) or choose_canonical(members, rows, linked)
        others = [uid for uid in members if uid != canonical]
        out_groups.append({
            'canonical': canonical, 'aliases': others, 'match': group['match'],
            'files': {uid: {'path': rows[uid]['path'], 'concept': rows[uid]['concept'],
                            'category': rows[uid]['category']} for uid in members}})
        for uid in others:
            aliases[uid] = canonical
    return {'schema': SCHEMA, 'policy': POLICY.format(iou=iou), 'min_iou': iou,
            'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'scanned': len(rows), 'canonical_count': len(rows) - len(aliases),
            'groups': out_groups, 'aliases': aliases}


def main(argv=None) -> int:
    from icon_set.scripts.primitives_catalog import model_links, primitives_root, scan

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--primitives', type=Path, help='Original primitives folder')
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--cache', type=Path, default=DEFAULT_CACHE)
    parser.add_argument('--write', action='store_true', help='Write the aliases file (default: dry run)')
    parser.add_argument('--show', type=int, default=15, help='Groups to print in the dry run')
    parser.add_argument('--iou', type=float, default=DEFAULT_IOU,
                        help=f'Minimum ink-mask IoU to call two primitives the same drawing (default {DEFAULT_IOU})')
    parser.add_argument('--workers', type=int, default=None)
    parser.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args(argv)

    root = primitives_root(args.primitives)
    rows = {row['uuid']: row for row in scan(root) if row['uuid']}
    links = model_links()
    linked = {uid: len(links['by_id'].get(uid, ())) + len(links['by_reference_id'].get(uid, ())) for uid in rows}
    groups = find_groups(root, rows, args.cache, args.workers, args.quiet, args.iou)
    previous = json.loads(args.output.read_text(encoding='utf-8')) if args.output.is_file() else None
    result = build_aliases(groups, rows, linked, previous, args.iou)

    sizes = collections.Counter(len(g['aliases']) + 1 for g in result['groups'])
    print(f"{result['scanned']} primitives, {len(result['groups'])} duplicate groups, "
          f"{len(result['aliases'])} aliases, {result['canonical_count']} canonical")
    print('  group sizes: ' + ', '.join(f'{n}x{c}' for n, c in sorted(sizes.items())))
    print('  match: ' + ', '.join(f'{k}={v}' for k, v in collections.Counter(g['match'] for g in result['groups']).items()))
    if not args.write:
        for group in result['groups'][:args.show]:
            files = group['files']
            print(f"\n  keep  {group['canonical']}  {files[group['canonical']]['concept']}  ({files[group['canonical']]['path']})")
            for uid in group['aliases']:
                print(f"  alias {uid}  {files[uid]['concept']}  ({files[uid]['path']})")
        print(f'\ndry run; pass --write to save {args.output}')
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'-> {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
