#!/usr/bin/env python3
"""GET /api/icons on a local Worker against the answers gallery.html gave (core/tests/fixtures/icon-query*.json).

Needs a local database of its own: those tables are emptied and the fixture loaded into them.

    cd cloud/worker
    npx wrangler d1 migrations apply pictographic-review-next --local -c wrangler.next.toml --persist-to /tmp/iq-state
    npx wrangler dev -c wrangler.next.toml --local --persist-to /tmp/iq-state --port 8831
    python3 tests/icon_list/check_local.py --base-url http://127.0.0.1:8831 --persist-to /tmp/iq-state

Rows are written with SQL (wrangler d1 execute --local); the list columns come from POST /api/icons/reindex and the
symmetry from POST /api/catalog/push, so those routes are checked too.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request

HERE = Path(__file__).resolve().parent
WORKER = HERE.parents[1]
FIXTURES = WORKER / 'core/tests/fixtures'


def q(value) -> str:
    if value is None:
        return 'NULL'
    if isinstance(value, bool):
        return str(int(value))
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (dict, list)):
        value = json.dumps(value, separators=(',', ':'))
    return "'" + str(value).replace("'", "''") + "'"


def seed_sql(fixture: dict) -> str:
    out = [f'DELETE FROM {t};' for t in ('icons', 'reviews', 'split_requests', 'feedback', 'store_documents', 'icon_graphs')]
    for r in fixture['records']:
        key = r['key']
        out.append('INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, build_failed, '
                   f"uploaded, record, pushed_at) VALUES ({q(key)}, {q(r['icon_id'])}, {q(r['name'])}, {q(r['family'])}, {q(r.get('category'))}, "
                   f"{q(r.get('profile'))}, 48, {q(fixture['current_sha'][key])}, {q(r['preview_url'])}, {q(bool(r.get('build_failed')))}, "
                   f"{q(bool(r.get('uploaded_icon')))}, {q(r)}, 'p');")
    for r in fixture['reviews']:
        out.append('INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note) VALUES '
                   f"({q(r['icon'])}, {q(r['svg_sha256'])}, {q(r['status'])}, {q(r['updated_at'])}, {q(r.get('updated_by'))}, "
                   f"{q(r.get('worker'))}, {q(r.get('claimed_at'))}, {q(r.get('note') or '')});")
    for s in fixture['splits']:
        out.append('INSERT INTO split_requests(icon, svg_sha256, combination_type, reason, reference_path, active, created_at, created_by) '
                   f"VALUES ({q(s['icon'])}, {q(s['svg_sha256'])}, 'side', 'r', 'p', {q(s['active'])}, {q(s['created_at'])}, {q(s['created_by'])});")
    for f in fixture['feedback']:
        out.append(f"INSERT INTO feedback(id, icon, feedback, svg_sha256, created_at, author, reason) VALUES ({f['id']}, {q(f['icon'])}, 'x', "
                   f"{q(f['svg_sha256'])}, 't', {q(f.get('author'))}, {q(f['reason'])});")
    for a in fixture['artwork']:
        out.append(f"INSERT INTO store_documents(store, key, document, updated_at, updated_by) VALUES ('icon-artwork', {q(a['key'])}, "
                   f"{q(a['document'])}, 't', 'u');")
    for sha in fixture['graphs']:
        out.append(f"INSERT INTO icon_graphs(svg_sha256, icon, graph) VALUES ({q(sha)}, 'x', '{{}}');")
    return '\n'.join(out) + '\n'


def call(base: str, method: str, path: str, body=None, token: str | None = None):
    data = json.dumps(body).encode() if body is not None else None
    headers = {'Content-Type': 'application/json', 'User-Agent': 'pictographic-check/1.0'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    request = urllib.request.Request(base + path, data=data, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--base-url', default='http://127.0.0.1:8831')
    parser.add_argument('--persist-to', required=True)
    args = parser.parse_args()
    fixture = json.loads((FIXTURES / 'icon-query.json').read_text())
    expected = json.loads((FIXTURES / 'icon-query-expected.json').read_text())
    token = next(line.split('=', 1)[1].strip().strip('"') for line in (WORKER / '.dev.vars').read_text().splitlines()
                 if line.startswith('PUSH_TOKEN='))
    with tempfile.NamedTemporaryFile('w', suffix='.sql', delete=False) as handle:
        handle.write(seed_sql(fixture))
    subprocess.run(['npx', 'wrangler', 'd1', 'execute', 'pictographic-review-next', '--local', '-c', 'wrangler.next.toml',
                    '--persist-to', args.persist_to, '--file', handle.name], cwd=WORKER, check=True, capture_output=True)
    offset = 0
    while offset is not None:
        offset = call(args.base_url, 'POST', '/api/icons/reindex', {'offset': offset, 'limit': 50}, token)['next_offset']
    call(args.base_url, 'POST', '/api/catalog/push', {'push_id': 'check', 'icons': [], 'final': False,
                                                      'upload_facets': fixture['facets']}, token)
    failures = 0
    for case, want in zip(fixture['cases'], expected['results']):
        got = call(args.base_url, 'GET', '/api/icons?' + urllib.parse.urlencode({k: v for k, v in case.items()}))
        mine = {'keys': [i['key'] for i in got['items']], 'total': got['total'], 'versions': got['versions'], 'offset': got['offset'],
                'states': got['states'], 'categories': got['categories']}
        theirs = {k: want[k] for k in mine}
        if mine != theirs:
            failures += 1
            print('DIFFERS', case, '\n  got ', mine, '\n  want', theirs)
    facets = call(args.base_url, 'GET', '/api/icons/facets')
    key = fixture['artwork'][0]['key']
    detail = call(args.base_url, 'GET', '/api/icon?key=' + urllib.parse.quote(key))
    assert detail['key'] == key and detail['review']['state'] and 'keywords' in detail, detail
    print(f"{len(fixture['cases']) - failures} of {len(fixture['cases'])} cases match the page; facets: "
          f"{len(facets['authors'])} authors, {len(facets['categories'])} categories, total {facets['total']}; "
          f"detail of {key}: {sorted(detail)[:8]}…")
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
