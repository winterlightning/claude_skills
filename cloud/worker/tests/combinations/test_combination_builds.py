"""Writes through the combination routes: drawings, candidates, parts and builds. TEST COPIES ONLY.

    PICTOGRAPHIC_COMBINATIONS=http://127.0.0.1:8821 PICTOGRAPHIC_COMBINATIONS_WRITE=1 \\
        python3 -m pytest cloud/worker/tests/combinations -q

Skipped unless PICTOGRAPHIC_COMBINATIONS_WRITE=1, and refused for the production Worker: they build
combined icons and change reference_parts. The SVG is made by combine.js (run with node), as the page does.
Signs in with the first user in wrangler.next.toml's ADMIN_USERS.
"""
from __future__ import annotations

import http.cookiejar
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request

import pytest

BASE = os.environ.get('PICTOGRAPHIC_COMBINATIONS', 'http://127.0.0.1:8821')
ROOT = Path(__file__).resolve().parents[4]
COMBINE = ROOT / 'icon_set/scripts/templates/combine.js'
pytestmark = pytest.mark.skipif(os.environ.get('PICTOGRAPHIC_COMBINATIONS_WRITE') != '1' or 'pictographic-review.' in BASE,
                                reason='writes: set PICTOGRAPHIC_COMBINATIONS_WRITE=1 against a test copy')


class Client:
    def __init__(self):
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(self, method, path, body=None):
        request = urllib.request.Request(BASE + path, method=method, data=None if body is None else json.dumps(body).encode(),
                                         headers={'Content-Type': 'application/json', 'User-Agent': 'pictographic-verify/1.0'})
        try:
            with self.opener.open(request, timeout=120) as response:
                return response.status, json.loads(response.read() or b'{}')
        except urllib.error.HTTPError as error:
            return error.code, json.loads(error.read() or b'{}')

    def get(self, path, **params):
        return self.call('GET', f'{path}?{urllib.parse.urlencode(params)}')


def admin():
    text = (ROOT / 'cloud/worker/wrangler.next.toml').read_text()
    users = json.loads(re.search(r"^ADMIN_USERS = '(.*)'$", text, re.M).group(1))
    name, password = next(iter(users.items()))
    client = Client()
    status, data = client.call('POST', '/api/auth/login', {'username': name, 'password': password})
    assert status == 200, data
    return client


def compose(main_svg, symbol_svg, placement):
    script = ("const C=require(process.argv[1]);let s='';process.stdin.on('data',d=>s+=d).on('end',()=>{"
              "const a=JSON.parse(s);process.stdout.write(JSON.stringify(C.container(a.main,a.symbol,a.placement)));});")
    out = subprocess.run(['node', '-e', script, str(COMBINE)], input=json.dumps({'main': main_svg, 'symbol': symbol_svg, 'placement': placement}),
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


@pytest.fixture(scope='module')
def client():
    return admin()


@pytest.fixture(scope='module')
def pair(client):
    """A container pair with both icons picked, and their drawings."""
    for offset in range(0, 2000, 200):
        status, data = client.get('/api/combinations', kind='container', limit=200, offset=offset)
        assert status == 200
        for item in data['items']:
            icons = {p['role']: p['icon'] for p in item['parts']}
            if icons.get('container') and icons.get('symbol'):
                status, drawings = client.get('/api/combinations/drawings', keys=f"{icons['container']},{icons['symbol']}")
                assert status == 200
                if all(drawings.get(k, {}).get('svg') for k in icons.values()):
                    return item, icons, drawings
    pytest.skip('no container pair with both drawings')


def request(item, icons, drawings, placement=None, **override):
    result = compose(drawings[icons['container']]['svg'], drawings[icons['symbol']]['svg'], placement or {'center': [32, 32], 'ink': None})
    build = {'reference_id': item['reference_id'], 'svg': result['svg'], 'parts': {
        'container': {'icon': icons['container'], 'svg_sha256': drawings[icons['container']]['svg_sha256'], 'layout': result['layout']['container']},
        'symbol': {'icon': icons['symbol'], 'svg_sha256': drawings[icons['symbol']]['svg_sha256'], 'layout': result['layout']['symbol']}}}
    build.update(override)
    return build, result


def one(client, reference_id):
    status, data = client.get('/api/combinations', q=reference_id, limit=1)
    assert status == 200 and data['items'], data
    return data['items'][0]


def test_drawings_match_the_listing(client, pair):
    item, icons, drawings = pair
    for p in item['parts']:
        assert drawings[p['icon']]['svg_sha256'] == p['current_sha']
    assert client.get('/api/combinations/drawings', keys='')[0] == 400
    assert client.get('/api/combinations/drawings', keys=','.join(f'a/{i}' for i in range(101)))[0] == 400


def test_candidates(client):
    status, found = client.get('/api/combinations/candidates', role='symbol', q='heart')
    assert status == 200 and found and all(c['key'].startswith('symbol/') for c in found)
    assert client.get('/api/combinations/candidates', role='other')[0] == 400


def test_build_needs_login(pair):
    item, icons, drawings = pair
    build, _ = request(item, icons, drawings)
    status, _ = Client().call('POST', '/api/combinations/build', {'builds': [build]})
    assert status == 401


def test_build_refuses_a_redrawn_part(client, pair):
    item, icons, drawings = pair
    build, _ = request(item, icons, drawings)
    build['parts']['symbol']['svg_sha256'] = '0' * 64
    status, data = client.call('POST', '/api/combinations/build', {'builds': [build]})
    assert status == 200 and data['results'][0]['ok'] is False and 'redrawn' in data['results'][0]['error']


def test_build_refuses_wrong_parts(client, pair):
    item, icons, drawings = pair
    build, _ = request(item, icons, drawings)
    build['parts'] = {'container': build['parts']['container']}
    assert client.call('POST', '/api/combinations/build', {'builds': [build]})[1]['results'][0]['ok'] is False
    build, _ = request(item, icons, drawings)
    build['parts']['symbol']['icon'] = icons['container']
    assert client.call('POST', '/api/combinations/build', {'builds': [build]})[1]['results'][0]['ok'] is False
    assert client.call('POST', '/api/combinations/build', {'builds': [build] * 51})[0] == 400


def test_build_then_stale_then_rebuild(client, pair):
    item, icons, drawings = pair
    build, result = request(item, icons, drawings, {'center': [30, 34], 'ink': [20, 20]})
    status, data = client.call('POST', '/api/combinations/build', {'builds': [build]})
    assert status == 200, data
    built = data['results'][0]
    assert built['ok'], built
    after = one(client, item['reference_id'])
    assert after['state'] == 'built' and after['icon']['svg_sha256'] == built['svg_sha256']
    symbol = next(p for p in after['parts'] if p['role'] == 'symbol')
    assert symbol['layout'] == result['layout']['symbol'] and symbol['built_sha'] == drawings[icons['symbol']]['svg_sha256']
    # The stored drawing is the one the browser made (after the server's clean-up) and is served.
    status, stored = client.get('/api/combinations/drawings', keys=built['key'])
    assert status == 200 and stored[built['key']]['svg_sha256'] == built['svg_sha256'] and '<g id="symbol"' in stored[built['key']]['svg']
    # Picking another symbol makes it stale until it is built again.
    status, others = client.get('/api/combinations/candidates', role='symbol', q='')
    other = next(c for c in others if c['key'] != icons['symbol'])
    status, _ = client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'symbol', 'icon': other['key']})
    assert status == 200
    assert one(client, item['reference_id'])['state'] == 'stale'
    # Back to the first symbol and rebuilt: built again.
    status, _ = client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'symbol', 'icon': icons['symbol']})
    assert status == 200
    build, _ = request(item, icons, drawings)
    assert client.call('POST', '/api/combinations/build', {'builds': [build]})[1]['results'][0]['ok']
    assert one(client, item['reference_id'])['state'] == 'built'


def test_parts_validation(client, pair):
    item, icons, _ = pair
    call = lambda body: client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], **body})[0]
    assert call({'role': 'symbol', 'icon': icons['container']}) == 400      # wrong family
    assert call({'role': 'symbol', 'icon': 'symbol/does-not-exist'}) == 404
    assert call({'role': 'main', 'icon': icons['symbol']}) == 404           # not a part of this combination
    assert call({'role': 'symbol', 'layout': [{'x': 'a'}]}) == 400
    assert call({'role': 'symbol'}) == 400
    assert Client().call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'symbol', 'layout': None})[0] == 401


def test_unsafe_svg_is_cleaned_or_refused(client, pair):
    item, icons, drawings = pair
    build, result = request(item, icons, drawings)
    build['svg'] = result['svg'].replace('</svg>', '<script>alert(1)</script></svg>')
    status, data = client.call('POST', '/api/combinations/build', {'builds': [build]})
    out = data['results'][0]
    if out['ok']:
        status, stored = client.get('/api/combinations/drawings', keys=out['key'])
        assert '<script' not in stored[out['key']]['svg']
    # Leave the pair as a clean build.
    build, _ = request(item, icons, drawings)
    assert client.call('POST', '/api/combinations/build', {'builds': [build]})[1]['results'][0]['ok']


def test_combined_icon_waits_for_its_parts(client, pair):
    item, icons, drawings = pair
    build, _ = request(item, icons, drawings)
    built = client.call('POST', '/api/combinations/build', {'builds': [build]})[1]['results'][0]
    assert built['ok']
    approve = lambda key, sha: client.call('POST', '/api/reviews', {'icon': key, 'svg_sha256': sha, 'status': 'approve'})
    unapproved = [role for role in ('container', 'symbol') if drawings[icons[role]]['review'] != 'approve']
    if unapproved:
        status, data = approve(built['key'], built['svg_sha256'])
        assert status == 409 and 'first' in data['error']
        for role in unapproved:
            assert approve(icons[role], drawings[icons[role]]['svg_sha256'])[0] in (200, 201)
    # Parts approved: the combined icon can be approved without building again.
    assert approve(built['key'], built['svg_sha256'])[0] in (200, 201)
    assert one(client, item['reference_id'])['icon']['review'] == 'approve'


# ---- side pairs, built with combine-side.js (pairRequest) the way side-pairs.html builds them

SIDE = ROOT / 'icon_set/scripts/templates/combine-side.js'


def side_request(item, drawings, **options):
    script = ("const S=require(process.argv[1]);let s='';process.stdin.on('data',d=>s+=d).on('end',()=>{const a=JSON.parse(s);"
              "const r=S.pairRequest(a.item,new Map(Object.entries(a.drawings)),a.options);"
              "process.stdout.write(JSON.stringify({request:r.request,sha:S.sha256(r.svg)}));});")
    out = subprocess.run(['node', '-e', script, str(SIDE)], input=json.dumps({'item': item, 'drawings': drawings, 'options': options}),
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def side_item(client, **params):
    status, data = client.get('/api/combinations', kind='side', forms='1', limit=50, **params)
    assert status == 200
    for item in data['items']:
        keys = [p['icon'] for p in item['parts'] if p['icon']] + ([item['icon']['key']] if item['icon'] else [])
        status, drawings = client.get('/api/combinations/drawings', keys=','.join(keys))
        if all(drawings.get(k, {}).get('svg') for k in keys):
            return item, drawings
    pytest.skip(f'no side pair with {params}')


def test_side_rebuild_of_a_stale_pair(client):
    item, drawings = side_item(client, state='stale')
    built = side_request(item, drawings)
    status, data = client.call('POST', '/api/combinations/build', {'builds': [built['request']]})
    result = data['results'][0]
    assert status == 200 and result['ok'], result
    assert result['svg_sha256'] == built['sha'], 'the stored drawing is the one the browser made'
    after = one(client, item['reference_id'])
    assert after['state'] == 'built' and after['icon']['svg_sha256'] == built['sha']


def test_side_rebuild_of_a_built_pair_keeps_its_drawing(client):
    # A pair whose parts are unchanged rebuilds to the drawing it has (the Python engine's, byte for byte).
    status, data = client.get('/api/combinations', kind='side', state='built', forms='1', limit=200)
    for item in data['items']:
        if any(p.get('updated_by') == 'recombine-all' for p in item['parts']):
            keys = [p['icon'] for p in item['parts'] if p['icon']]
            status, drawings = client.get('/api/combinations/drawings', keys=','.join(keys))
            built = side_request(item, drawings)
            if built['sha'] == item['icon']['svg_sha256']:
                assert client.call('POST', '/api/combinations/build', {'builds': [built['request']]})[1]['results'][0]['svg_sha256'] == built['sha']
                return
    pytest.skip('no rebuilt side pair on this copy')


def test_side_native_text_pair_builds_without_a_sub_icon(client):
    status, data = client.get('/api/combinations', kind='side', forms='1', limit=500)
    for item in data['items']:
        sub = next(p for p in item['parts'] if p['role'] == 'sub')
        main = next(p for p in item['parts'] if p['role'] == 'main')
        if sub['icon'] is None and (sub.get('form') or {}).get('native_text') and main['icon']:
            status, drawings = client.get('/api/combinations/drawings', keys=main['icon'])
            built = side_request(item, drawings)
            assert built['request']['parts']['sub']['icon'] is None
            result = client.call('POST', '/api/combinations/build', {'builds': [built['request']]})[1]['results'][0]
            assert result['ok'], result
            return
    pytest.skip('no native text pair on this copy')


def test_side_pair_made_from_a_reference(client):
    status, data = client.get('/api/combinations/candidates', role='main', q='')
    # A reference that is no combination yet: made into one, then undone.
    rid = '0005e7b2-b6eb-47bb-9376-770c2522288d'
    call = lambda body: client.call('POST', '/api/combinations/pair', body)
    assert Client().call('POST', '/api/combinations/pair', {'reference_id': rid})[0] == 401
    assert call({'reference_id': 'no-such-reference'})[0] == 404
    assert call({'reference_id': rid, 'position': 'xx'})[0] == 400
    status, made = call({'reference_id': rid, 'position': 'tl'})
    assert status == 200
    item = one(client, rid)
    assert {p['role'] for p in item['parts']} == {'main', 'sub'}
    status, removed = call({'reference_id': rid, 'remove': True})
    assert status == 200 and removed['removed']
    assert client.get('/api/combinations', q=rid, limit=1)[1]['total'] == 0
