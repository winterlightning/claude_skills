"""Read production state, or set the eight repaired originals to Ready with --apply."""
import argparse
import ast
import concurrent.futures
import hashlib
import http.cookiejar
import json
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
BASE = 'https://suffered-scored-nicole-default.trycloudflare.com'
ICONS = ['car-seat', 'increase-indent', 'lab-bottle-experiment', 'lab-protection-glasses',
         'ladies-hat-with-bow', 'layers-front', 'water-spray', 'zoom-out']
OUT = Path(__file__).resolve().parent

def request(route, data=None, opener=None):
    req = urllib.request.Request(BASE + route, data=None if data is None else json.dumps(data).encode(),
                                 headers={'Content-Type': 'application/json', 'Cache-Control': 'no-cache'})
    with (opener.open(req, timeout=30) if opener else urllib.request.urlopen(req, timeout=30)) as response:
        return json.load(response)

def snapshot(name):
    key = 'solo/' + name
    query = '?icon=' + urllib.parse.quote(key, safe='')
    artwork = request('/api/icon-artwork' + query)
    detail = request('/api/review-detail' + query)
    remote_hash = artwork['record']['svg_sha256']
    local_hash = hashlib.sha256((ROOT / 'icon_set/dist/solo48' / (name + '.svg')).read_bytes()).hexdigest()
    return {'icon': key, 'svg_sha256': remote_hash, 'local_svg_sha256': local_hash,
            'matches_local_fix': remote_hash == local_hash, 'before': detail}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(snapshot, ICONS))
    if not args.apply:
        (OUT / 'preflight.json').write_text(json.dumps(rows, indent=2))
        print(json.dumps(rows, indent=2))
        return
    if not all(row['matches_local_fix'] for row in rows):
        raise RuntimeError('Production differs from the repaired local revisions; review before changing statuses.')
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    tree = ast.parse((ROOT / 'icon_set/scripts/deploy.py').read_text())
    users = next(ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign)
                 and any(isinstance(target, ast.Name) and target.id == 'ADMIN_USERS' for target in node.targets))
    login = request('/api/auth/login', {'username': 'jakes', 'password': users['jakes']}, opener)
    if login.get('user') != 'jakes':
        raise RuntimeError('Authentication failed')
    try:
        for row in rows:
            if row['before']['status'] == 'rejected':
                row['result'] = {'skipped': True, 'reason': 'Currently rejected; needs separate restoration.'}
            else:
                row['result'] = request('/api/reviews', {'icon': row['icon'], 'svg_sha256': row['svg_sha256'], 'status': 'ready'}, opener)
            row['after'] = request('/api/review-detail?icon=' + urllib.parse.quote(row['icon'], safe=''), opener=opener)
            (OUT / 'result.json').write_text(json.dumps(rows, indent=2))
            print(json.dumps(row), flush=True)
    finally:
        request('/api/auth/logout', {}, opener)
    assert all(row['after']['status'] == 'ready' for row in rows), 'Some icons are not Ready'

if __name__ == '__main__':
    main()
