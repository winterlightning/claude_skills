"""A local D1 seed for the fill side pairs tests: the 3,614 side pairs of icon_set/data/side-fill as "references" and
reference_parts rows, their source icons (solo/…, sub/…) with the drawings each pair was laid out from, and one test
login. Nothing is read from production.

    python3 cloud/worker/tests/side_fill/make_local_seed.py > /tmp/seed.sql
    (cd cloud/worker && npx wrangler d1 execute pictographic-review-next --local --persist-to STATE --file /tmp/seed.sql)
"""
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DATA = REPO / 'icon_set/data/side-fill'
TEST_TOKEN = 'side-fill-test-session'
REVIEWER_TOKEN = 'side-fill-test-reviewer-session'


def q(value):
    if value is None:
        return 'NULL'
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def source_file(part, role):
    name = part['icon'].split('/', 1)[1]
    if role == 'main':
        return DATA / 'normal' / f'{name}.svg'
    flat = DATA / 'archive/side-sub-32' / f'{name}.svg'
    return flat if flat.is_file() else DATA / 'archive/sub-32-revisions' / name / f"{part.get('current_sha') or part['built_sha']}.svg"


def published_keyshapes():
    """{icon key: (keyshape, keyshape_bounds)} of the published catalog, so a seeded icon has the keyshape its
    production record has (a styled fill copies it from there). Uploads made on the site since are not in it."""
    found = {}
    for path in sorted((REPO / 'published').glob('*/manifest.json')) + sorted((REPO / 'published/failed').glob('*/manifest.json')):
        try:
            icons = json.loads(path.read_text()).get('icons', [])
        except ValueError:
            continue
        for icon in icons:
            key = icon.get('key') or f"{icon.get('family', '')}/{icon.get('icon_id', '')}"
            if icon.get('keyshape'):
                found.setdefault(key, (icon['keyshape'], icon.get('keyshape_bounds')))
    return found


def main():
    out = sys.stdout
    keyshapes = published_keyshapes()
    items = json.loads((DATA / 'data/production-layouts.json').read_text())['items']
    seen_refs, seen_icons = set(), set()
    now = '2026-10-28T00:00:00.000Z'
    for item in items:
        out.write(f"INSERT OR IGNORE INTO \"references\"(reference_id, kind, concept, source) VALUES ({q(item['reference_id'])}, 'combination', {q(item['concept'])}, 'test');\n")
        for part in item['parts']:
            if part['part_reference_id'] not in seen_refs:
                seen_refs.add(part['part_reference_id'])
                out.write(f"INSERT OR IGNORE INTO \"references\"(reference_id, kind, concept, source) VALUES ({q(part['part_reference_id'])}, 'single', NULL, 'test');\n")
            out.write(f"INSERT OR IGNORE INTO reference_parts(reference_id, role, part_reference_id, position, icon, layout, built_sha) VALUES "
                      f"({q(item['reference_id'])}, {q(part['role'])}, {q(part['part_reference_id'])}, {q(part.get('position'))}, {q(part.get('icon'))}, "
                      f"{q(json.dumps(part.get('layout')) if part.get('layout') else None)}, {q(part.get('built_sha'))});\n")
            key = part.get('icon')
            if not key or key in seen_icons:
                continue
            path = source_file(part, part['role'])
            if not path.is_file():
                continue
            seen_icons.add(key)
            svg = path.read_text()
            sha = hashlib.sha256(svg.encode()).hexdigest()
            family, name = key.split('/', 1)
            profile, canvas = ('SOLO48', 48) if family == 'solo' else ('SUB32', 32)
            keyshape, bounds = keyshapes.get(key, (None, None))
            record = {'keyshape': keyshape, 'keyshape_bounds': bounds} if keyshape else {}
            out.write(f"INSERT OR IGNORE INTO icons(key, icon_id, name, family, profile, canvas_size, svg_sha256, pushed_at, sort_name, keyshape, record) VALUES "
                      f"({q(key)}, {q(name)}, {q(name)}, {q(family)}, {q(profile)}, {canvas}, {q(sha)}, {q(now)}, {q(name)}, {q(keyshape)}, {q(json.dumps(record))});\n")
            out.write(f"INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES ({q(sha)}, {q(key)}, {q(svg)}, 'build', {q(now)});\n")
    token = hashlib.sha256(TEST_TOKEN.encode()).hexdigest()
    out.write(f"INSERT OR REPLACE INTO admin_sessions(token, username, expires) VALUES ({q(token)}, 'side-fill-test', 99999999999);\n")
    # A local stand-in for the reviewer who approves the fill parts (upload_fill_parts.py --approve).
    token = hashlib.sha256(REVIEWER_TOKEN.encode()).hexdigest()
    out.write(f"INSERT OR REPLACE INTO admin_sessions(token, username, expires) VALUES ({q(token)}, 'jakes', 99999999999);\n")


if __name__ == '__main__':
    main()
