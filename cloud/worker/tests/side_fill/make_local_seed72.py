"""A local D1 seed for the 72 fill side pairs, on top of make_local_seed.py (which adds the references and the test
logins): the main-54 / sub-36 icons the 72 pairs use, with the drawings the snapshot holds
(icon_set/data/side-fill-72, `python3 -m icon_set side-fill import72`). Nothing is read from production.

    python3 cloud/worker/tests/side_fill/make_local_seed72.py > /tmp/seed72.sql
    (cd cloud/worker && npx wrangler d1 execute pictographic-review-next --local --persist-to STATE --file /tmp/seed72.sql)
"""
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DATA72 = REPO / 'icon_set/data/side-fill-72'
PROFILES = {'main-54': ('MAIN54', 54), 'sub-36': ('SUB36', 36)}


def q(value):
    if value is None:
        return 'NULL'
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def main():
    out = sys.stdout
    snap = json.loads((DATA72 / 'export.json').read_text())
    now = '2026-11-11T00:00:00.000Z'
    for key, part in sorted(snap['parts'].items()):
        svg = (DATA72 / part['source']).read_text()
        sha = hashlib.sha256(svg.encode()).hexdigest()
        family, name = key.split('/', 1)
        profile, canvas = PROFILES[family]
        out.write(f"INSERT OR IGNORE INTO icons(key, icon_id, name, family, profile, canvas_size, svg_sha256, pushed_at, sort_name, record) VALUES "
                  f"({q(key)}, {q(name)}, {q(name)}, {q(family)}, {q(profile)}, {canvas}, {q(sha)}, {q(now)}, {q(name)}, '{{}}');\n")
        out.write(f"INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES ({q(sha)}, {q(key)}, {q(svg)}, 'build', {q(now)});\n")


if __name__ == '__main__':
    main()
