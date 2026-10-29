"""Publish reviewed stroke-fill/v1 icons as the fills the side combinations read.

Mains go to data/current-normal-fill-48/<name>/<source-sha>.svg (the shared output/normal-fill
collection is left untouched); subs replace data/current-normal-fill-32/<name>/<source-sha>.svg.
fill_path() reads these before the older flat fills. Only outputs whose source hash a saved pair
uses are published; rework errors and fills held for repair keep the older fill.
"""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .adaptive_overlap import DEFAULT_LAYOUTS, ROOT, fill_path

ROLES = {
    'main': (WORK / 'main48-region-fill-review-stroke-fill', DATA / 'data/current-normal-fill-48'),
    'sub': (WORK / 'sub32-region-fill-review-stroke-fill', DATA / 'data/current-normal-fill-32'),
}
LOG = DATA / 'data/stroke-fill-publish-log.jsonl'
SKIP_STATUSES = {'held_for_repair', 'needs_repair', 'error'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def publishable(role, layouts):
    """{(name, source sha): stroke-fill output} for reworked icons whose source version a pair uses."""
    review, _target = ROLES[role]
    manifest = json.loads((review / 'manifest.json').read_text())
    used = {(part['icon'].split('/', 1)[1], part.get('current_sha') or part.get('built_sha')): part
            for item in layouts for part in item['parts'] if part['role'] == role and part.get('icon')}
    return {(r['name'], r['source_sha256']): (review / r['output'], used[(r['name'], r['source_sha256'])])
            for r in manifest['records']
            if r['kind'] != 'error' and r['review_status'] not in SKIP_STATUSES
            and (r['name'], r['source_sha256']) in used and (review / r['output']).is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('roles', nargs='*', choices=sorted(ROLES), default=sorted(ROLES))
    parser.add_argument('--apply', action='store_true', help='write files (default: dry run)')
    parser.add_argument('--names', nargs='*', help='only these icons (a rebuilt review can differ elsewhere too)')
    args = parser.parse_args()
    layouts = json.loads(DEFAULT_LAYOUTS.read_text())['items']
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    for role in args.roles:
        _review, target = ROLES[role]
        files = {key: v for key, v in publishable(role, layouts).items() if not args.names or key[0] in args.names}
        old = {key: (sha(fill_path(part, role)) if fill_path(part, role).is_file() else None)
               for key, (_src, part) in files.items()}
        changed = {key: src for key, (src, _part) in files.items() if old[key] != sha(src)}
        print(f'{role}: publishable {len(files)} · fill changes {len(changed)}')
        for name, source_sha in sorted(changed):
            print(f'  {name} {source_sha[:12]}')
        if not args.apply or not changed:
            continue
        if target.exists():
            # In the ignored build state: a copy under DATA would join the snapshot (and its R2 manifest).
            backup = WORK / 'stroke-fill-publish-backups' / stamp / target.name
            shutil.copytree(target, backup)
            print(f'backup {backup}')
        with LOG.open('a') as log:
            for (name, source_sha), src in sorted(changed.items()):
                out = target / name / f'{source_sha}.svg'
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, out)
                log.write(json.dumps({'at': stamp, 'role': role, 'name': name, 'source_sha256': source_sha,
                                      'old_fill_sha256': old[(name, source_sha)], 'new_fill_sha256': sha(out),
                                      'from': str(src.relative_to(ROOT))}) + '\n')
    if args.apply:
        print(f'log {LOG}')


if __name__ == '__main__':
    main()
