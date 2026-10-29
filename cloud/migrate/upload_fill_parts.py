#!/usr/bin/env python3
"""Store the fill variant icons of the fill side pairs (icon_set/state/side-fill/fill-icons/manifest.json, written by
`python3 -m icon_set side-fill icons`) with POST /api/icons/styled, 50 a request: each is an icon of style fill in
its solo / sub icon's own family (solo/<name>--fill, solo/<name>--fill-region-3…, sub/<name>--fill), style_of that
normal icon, Ready in Icon review. The outline is the normal solo / sub icon itself and is not sent.

    python3 cloud/migrate/upload_fill_parts.py --base-url http://127.0.0.1:8821            # dry run
    python3 cloud/migrate/upload_fill_parts.py --base-url … --send                         # push token from cloud/.env
    PICTOGRAPHIC_SESSION=<the reviewer's pictographic_session cookie> \
    python3 cloud/migrate/upload_fill_parts.py --base-url … --send --approve               # and approve each, as them

A variant whose file was sent before (fill-icons/uploaded.json, per site) is skipped; the route itself reports a
drawing it holds already as unchanged, so a lost ledger costs only requests. A changed drawing replaces the icon's
(back to Ready); one that people have worked on (a review other than Ready, an edit, feedback) is kept and listed,
unless --replace. Run the import SQL first, then this, then the picks SQL.

--approve approves each variant's current drawing in Icon review (POST /api/reviews, status approve) as the person
whose session it sends, exactly as their Approve button does: the review records them, and every fill pair output
using the variant is rechecked (its Failed check clears once both its parts are approved). A variant approved
before on the same drawing is skipped. With a session the variants are stored as that person too (no push token).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
WORK = REPO / 'icon_set/state/side-fill'
MANIFEST = WORK / 'fill-icons/manifest.json'
# What was sent and what the site stored (the route cleans the SVG, so its sha is not the file's).
LEDGER = WORK / 'fill-icons/uploaded.json'
BATCH = 50


def as_reviewer(base_url: str, session: str, path: str, payload: dict) -> dict:
    """A POST as the signed-in reviewer (their session cookie, the site's own origin)."""
    base = base_url.rstrip('/')
    request = urllib.request.Request(base + path, data=json.dumps(payload).encode(), method='POST', headers={
        'Content-Type': 'application/json', 'User-Agent': 'pictographic-migrate/1.0', 'Origin': base,
        'Cookie': f'pictographic_session={session}'})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as error:
        raise RuntimeError(f'POST {path} -> HTTP {error.code}: {json.loads(error.read() or b"{}").get("error")}') from None


def approve(base_url: str, session: str, manifest: list, ledger: dict) -> list[str]:
    """Approve each stored variant's current drawing as the session's reviewer; returns the failures."""
    todo = [m['key'] for m in manifest if ledger.get(m['key'], {}).get('site_sha256')
            and ledger[m['key']].get('approved_sha256') != ledger[m['key']]['site_sha256']]
    print(f'{len(todo)} fill variants to approve', flush=True)
    failed = []

    def one(key):
        sha = ledger[key]['site_sha256']
        try:
            answer = as_reviewer(base_url, session, '/api/reviews', {'icon': key, 'status': 'approve', 'svg_sha256': sha})
            ledger[key]['approved_sha256'] = sha
            ledger[key]['approved_by'] = answer.get('updated_by')
        except RuntimeError as error:
            failed.append(f'{key}: {error}')
    with ThreadPoolExecutor(4) as pool:
        for n, _ in enumerate(pool.map(one, todo), 1):
            if n % 200 == 0 or n == len(todo):
                print(f'approved {n - len(failed)}/{len(todo)} ({len(failed)} failed)', flush=True)
    return failed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--replace', action='store_true', help='also replace variants people have worked on')
    parser.add_argument('--limit', type=int)
    parser.add_argument('--approve', action='store_true', help='approve each variant as the PICTOGRAPHIC_SESSION reviewer')
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    ledger_all = json.loads(LEDGER.read_text()) if LEDGER.is_file() else {}
    ledger = ledger_all.setdefault(args.base_url.rstrip('/'), {})
    todo = []
    for item in manifest:
        svg = (WORK / item['svg']).read_text()
        if ledger.get(item['key'], {}).get('file_sha256') != hashlib.sha256(svg.encode()).hexdigest():
            todo.append((item, svg))
    print(f'{len(manifest)} fill variant icons; {len(manifest) - len(todo)} sent already; {len(todo)} to send'
          + (f' (the first {args.limit})' if args.limit else ''))
    todo = todo[:args.limit] if args.limit else todo
    if not args.send:
        for item, _ in todo[:5]:
            print(f'  would store {item["key"]} (style fill of {item["source_key"]})')
        if args.approve:
            waiting = sum(1 for m in manifest if ledger.get(m['key'], {}).get('approved_sha256') != ledger.get(m['key'], {}).get('site_sha256', '-'))
            print(f'and approve about {waiting} variants (all sent variants not yet approved on their current drawing)')
        return 0
    session = os.environ.get('PICTOGRAPHIC_SESSION')
    if args.approve and not session:
        raise SystemExit('error: --approve needs PICTOGRAPHIC_SESSION (the reviewer\'s session cookie value)')
    token = None if session else cloudapi.push_token(args.base_url)
    totals, failed, kept = {}, [], []
    for start in range(0, len(todo), BATCH):
        batch = todo[start:start + BATCH]
        items = [{'source_key': item['source_key'], 'style': 'fill', 'variant': item['variant'], 'svg': svg} for item, svg in batch]
        try:
            payload = {'items': items, 'replace': args.replace}
            answer = (as_reviewer(args.base_url, session, '/api/icons/styled', payload) if session
                      else cloudapi.post_json(args.base_url, '/api/icons/styled', payload, token=token))
        except RuntimeError as error:
            failed.extend(f'{item["key"]}: {error}' for item, _ in batch)
            continue
        files = {item['key']: item['svg_sha256'] for item, _ in batch}
        for result in answer['results']:
            ledger[result['key']] = {'file_sha256': files[result['key']], 'site_sha256': result['svg_sha256']}
            totals[result['outcome']] = totals.get(result['outcome'], 0) + 1
        kept.extend(k['key'] for k in answer['kept_manual'])
        failed.extend(f'{e.get("key") or e.get("source_key")} {e.get("variant") or ""}: {e["error"]}' for e in answer['errors'])
        print(f'sent {min(start + BATCH, len(todo))}/{len(todo)} {totals} ({len(failed)} failed, {len(kept)} kept)', flush=True)
        LEDGER.write_text(json.dumps(ledger_all, indent=1) + '\n')
    for key in kept[:10]:
        print('  kept (people worked on it; --replace to replace)', key)
    if args.approve:
        failed += approve(args.base_url, session, manifest, ledger)
        LEDGER.write_text(json.dumps(ledger_all, indent=1) + '\n')
    for line in failed[:10]:
        print('  failed', line)
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
