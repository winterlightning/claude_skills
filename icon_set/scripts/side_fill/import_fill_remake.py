"""One-off import of the fill side-pair work from a fill-remake checkout into icon_set/data/side-fill.

    python3 -m icon_set side-fill import --from ~/Downloads/fill-remake            # report only
    python3 -m icon_set side-fill import --from ~/Downloads/fill-remake --write    # copy

Copies only what the engine reads, for the icons the 64 side pairs use:
  data/     layouts (placements already folded in), picks, layout specs, review decisions and marks,
            the reviewed stroke-fill mains / subs and the legacy 32px fills
  archive/  the sub sources (side-sub-32 and the exact saved revisions)
  normal/   the main sources, normal-fill/ their 48px fills
  recipes/  the region recipes (icons/<name>/attempt-*/recipe.json, overrides/<name>.json)
The preserved 48px fills back the main48 review's keep-current / keep-variant marks. Logs and selection
histories stay behind. The report says how many pair parts still match the drawing
published in claude_skills (the rest were redrawn since; their pairs are rebuilt from the new drawing).
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from .paths import DATA

REPO_PUBLISHED = DATA.parents[2] / 'published'
DATA_FILES = ('production-layouts.json', 'pair-placement-overrides.json', 'ai-variant-decisions.json',
              'ai-layout-proposals.json', 'main-region-variant-policy.json', 'main48-user-review-marks.json',
              'main48-region-fill-review-decisions.json', 'sub32-region-fill-review-decisions.json',
              'sub32-user-review-marks.json', 'side-keyshapes.json', 'latest-side-main-48-selection.json',
              'latest-side-sub-32-selection.json')
DATA_FOLDERS = ('latest-side-main-48', 'latest-side-sub-32', 'current-normal-fill-48', 'current-normal-fill-32',
                'legacy-normal-fill-32', 'preserved-main-fill-48-20261026')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plan(source):
    """[(from, to)] for every file the engine needs, plus the used icon names."""
    side = source / 'side_combinations'
    items = json.loads((side / 'data/production-layouts.json').read_text())['items']
    mains, subs = set(), set()
    for item in items:
        for part in item['parts']:
            if part.get('icon'):
                (mains if part['role'] == 'main' else subs).add(part['icon'].split('/', 1)[1])
    copies = [(side / 'data' / name, DATA / 'data' / name) for name in DATA_FILES]
    for folder in DATA_FOLDERS:
        copies += [(f, DATA / 'data' / folder / f.relative_to(side / 'data' / folder))
                   for f in sorted((side / 'data' / folder).rglob('*')) if f.is_file()]
    for folder in ('side-sub-32', 'sub-32-revisions'):
        copies += [(f, DATA / 'archive' / folder / f.relative_to(side / 'archive' / folder))
                   for f in sorted((side / 'archive' / folder).rglob('*')) if f.is_file()]
    recipes = source / 'fill_processing/collection-11059'
    for name in sorted(mains):
        copies.append((source / 'normal' / f'{name}.svg', DATA / 'normal' / f'{name}.svg'))
        copies.append((source / 'output/normal-fill' / f'{name}.svg', DATA / 'normal-fill' / f'{name}.svg'))
        copies.append((recipes / 'overrides' / f'{name}.json', DATA / 'recipes/overrides' / f'{name}.json'))
        copies += [(r, DATA / 'recipes' / r.relative_to(recipes)) for r in sorted((recipes / 'icons' / name).glob('attempt-*/recipe.json'))]
    return [(a, b) for a, b in copies if a.is_file()], mains, subs, items


def match_report(items):
    """How many pair parts were built from the drawing claude_skills publishes now."""
    counts = {}
    for item in items:
        for part in item['parts']:
            if not part.get('icon'):
                continue
            name = part['icon'].split('/', 1)[1]
            published = REPO_PUBLISHED / ('solo48' if part['role'] == 'main' else 'sub32') / f'{name}.svg'
            want = part.get('current_sha') or part.get('built_sha')
            state = 'not published (upload or removed)' if not published.is_file() else \
                'same drawing' if sha(published) == want else 'redrawn since'
            key = f"{part['role']}: {state}"
            counts[key] = counts.get(key, 0) + 1
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--from', dest='source', type=Path, required=True, help='the fill-remake checkout')
    parser.add_argument('--write', action='store_true', help='copy the files (default: report only)')
    args = parser.parse_args(argv)
    copies, mains, subs, items = plan(args.source.expanduser().resolve())
    size = sum(a.stat().st_size for a, _ in copies)
    print(json.dumps({'pairs': len(items), 'mains': len(mains), 'subs': len(subs), 'files': len(copies),
                      'megabytes': round(size / 1e6, 1), 'parts': match_report(items)}, indent=2))
    if not args.write:
        print('Report only: pass --write to copy.')
        return 0
    for a, b in copies:
        b.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(a, b)
    print(f'copied {len(copies)} files into {DATA}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
