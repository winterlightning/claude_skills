"""Bring the snapshot's source drawings (icon_set/data/side-fill) up to the site's current ones, for parts whose
drawing there is not the one the site has (status redrawn or no-source).

    curl -s "<site>/api/combinations/drawings?keys=solo/a,sub/b" > drawings.json     # one bounded read, ≤ 100 keys
    python3 -m icon_set side-fill sources drawings.json            # report
    python3 -m icon_set side-fill sources drawings.json --write    # then `side-fill build`, publish, icons, d1-import

A main's drawing is its source in normal/ and data/latest-side-main-48/ (the region-fill review reads it); a sub's is
archive/sub-32-revisions/<name>/<sha>.svg (and data/latest-side-sub-32/). Decisions reviewed on another drawing are
not applied to it (they are keyed by drawing sha): the engine's defaults run and the fill is reviewed in Icon review.
A pair laid out on an earlier drawing than the site's current one keeps that layout and stays uncombined until it
is laid out again on the pair page; its part's fill is still exported (fill_icons), since data/site-drawings.json
records that this drawing is the site's.
"""
import argparse
import hashlib
import json
from pathlib import Path

from .paths import DATA

SITE_DRAWINGS = DATA / 'data/site-drawings.json'


def site_drawings() -> dict[str, str]:
    """{part key: drawing sha the site said is current} (written by `sources --write`)."""
    return json.loads(SITE_DRAWINGS.read_text()) if SITE_DRAWINGS.is_file() else {}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def targets(key: str, digest: str) -> list[Path]:
    family, name = key.split('/', 1)
    if family == 'sub':
        return [DATA / 'archive/sub-32-revisions' / name / f'{digest}.svg', DATA / 'data/latest-side-sub-32' / f'{name}.svg']
    return [DATA / 'normal' / f'{name}.svg', DATA / 'data/latest-side-main-48' / f'{name}.svg']


def laid_out_on() -> dict[str, set[str]]:
    """{part key: drawing shas the saved pair layouts were made on}."""
    found = {}
    for item in json.loads((DATA / 'data/production-layouts.json').read_text())['items']:
        for part in item['parts']:
            if part.get('icon'):
                found.setdefault(part['icon'], set()).add(part.get('current_sha') or part.get('built_sha'))
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('drawings', type=Path, help='GET /api/combinations/drawings output: {key: {svg_sha256, svg}}')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args(argv)
    drawings = json.loads(args.drawings.read_text())
    layouts = laid_out_on()
    report = {'written': [], 'unchanged': [], 'relayout': [], 'skipped': []}
    for key, drawing in sorted(drawings.items()):
        svg = (drawing or {}).get('svg')
        if not svg or key.split('/', 1)[0] not in ('solo', 'container', 'sub'):
            report['skipped'].append(key)
            continue
        data = svg.encode()
        if sha(data) != drawing.get('svg_sha256'):
            raise SystemExit(f'error: {key}: the drawing does not hash to its svg_sha256')
        if drawing['svg_sha256'] not in layouts.get(key, set()):
            report['relayout'].append(key)          # laid out on another drawing: lay out again on the pair page
        paths = targets(key, drawing['svg_sha256'])
        if all(p.is_file() and p.read_bytes() == data for p in paths):
            report['unchanged'].append(key)
            continue
        report['written'].append(key)
        if args.write:
            for path in paths:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if args.write:
        known = site_drawings()
        known.update({key: d['svg_sha256'] for key, d in drawings.items() if key not in report['skipped']})
        SITE_DRAWINGS.write_text(json.dumps(dict(sorted(known.items())), indent=1) + '\n')
    print(json.dumps({k: v for k, v in report.items()}, indent=1))
    if report['written'] and not args.write:
        print('(report only: --write to update the snapshot)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
