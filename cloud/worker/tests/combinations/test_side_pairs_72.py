"""Side pairs at 72: upload a main-54 and a sub-36 drawn from a pair's part references, see them picked, build the
pair with combine-side.js at size 72 and review it. TEST COPIES ONLY (same switches as test_combination_builds.py).

    PICTOGRAPHIC_COMBINATIONS=http://127.0.0.1:8821 PICTOGRAPHIC_COMBINATIONS_WRITE=1 \\
        python3 -m pytest cloud/worker/tests/combinations/test_side_pairs_72.py -q
"""
from __future__ import annotations

import pytest

from test_combination_builds import Client, admin, pytestmark, side_request  # noqa: F401  (pytestmark: the same skip)

ATTRS = 'fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
MAIN = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 54 54" {ATTRS}><rect x="6" y="6" width="42" height="42" rx="6"/><path d="M6 17L48 17"/></svg>'
SUB = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36" {ATTRS}><circle cx="18" cy="18" r="12"/></svg>'


@pytest.fixture(scope='module')
def client():
    return admin()


def one(client, reference_id, size=72):
    status, data = client.get('/api/combinations', q=reference_id, limit=1, size=size)
    assert status == 200 and data['items'], data
    return data['items'][0]


@pytest.fixture(scope='module')
def pair(client):
    """A side pair with no 72 drawings yet, its main and sub uploaded from its part references."""
    status, data = client.get('/api/combinations', size=72, kind='side', missing=1, limit=20)
    assert status == 200 and data['size'] == 72, data
    for item in data['items']:
        refs = {p['role']: p['part_reference_id'] for p in item['parts']}
        if set(refs) != {'main', 'sub'} or any(r.startswith('draw:') for r in refs.values()):
            continue
        picked = {}
        for role, family, svg in (('main', 'main-54', MAIN), ('sub', 'sub-36', SUB)):
            status, up = client.call('POST', '/api/icons/upload', {'name': f'72 test {role}', 'family': family, 'svg': svg,
                                                                    'reference_id': refs[role]})
            assert status == 201, up
            assert {'reference_id': item['reference_id'], 'role': role, 'size': 72} in up['combination_parts'], up
            picked[role] = up['record']['key']
        return item, picked
    pytest.skip('no side pair without 72 drawings')


def test_families(client):
    status, data = client.get('/api/icon-families')
    sizes = {f['id']: f['canvas_size'] for f in data['families']}
    assert (sizes.get('main-54'), sizes.get('sub-36'), sizes.get('combination-72')) == (54, 36, 72)


def test_upload_picks_the_parts(client, pair):
    item, picked = pair
    now = one(client, item['reference_id'])
    assert {p['role']: p['icon'] for p in now['parts']} == picked
    assert now['state'] == 'unbuilt' and now['icon'] is None
    # the 64 pair keeps its own icons
    assert not any(str(p['icon']).startswith(('main-54/', 'sub-36/')) for p in one(client, item['reference_id'], 64)['parts'])


def test_wrong_canvas_and_family_are_refused(client, pair):
    item, picked = pair
    status, _ = client.call('POST', '/api/icons/upload', {'name': 'x', 'family': 'main-54', 'svg': SUB})
    assert status == 400
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'main', 'icon': picked['sub'], 'size': 72})
    assert status == 400, data
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'main', 'icon': picked['main'], 'size': 80})
    assert status == 400, data


def test_build_review_and_stale(client, pair):
    item, picked = pair
    state64 = one(client, item['reference_id'], 64)['state']
    current = one(client, item['reference_id'])
    status, drawings = client.get('/api/combinations/drawings', keys=','.join(picked.values()))
    assert status == 200
    made = side_request(current, drawings, size=72)
    # a 64 build of 72 parts is refused
    status, data = client.call('POST', '/api/combinations/build', {'builds': [made['request']]})
    assert status == 200 and not data['results'][0]['ok'], data
    status, data = client.call('POST', '/api/combinations/build', {'size': 72, 'builds': [made['request']]})
    result = data['results'][0]
    assert status == 200 and result['ok'], data
    assert result['key'] == f"combination-72/{item['reference_id']}" and result['build_failed']   # parts still Ready
    built = one(client, item['reference_id'])
    assert built['state'] == 'built' and built['icon']['key'] == result['key']
    # not approvable until both parts are
    status, data = client.call('POST', '/api/reviews', {'icon': result['key'], 'svg_sha256': result['svg_sha256'], 'status': 'approve'})
    assert status == 409, data
    for key in picked.values():
        sha = drawings[key]['svg_sha256']
        status, data = client.call('POST', '/api/reviews', {'icon': key, 'svg_sha256': sha, 'status': 'approve'})
        assert status in (200, 201), data
    status, data = client.call('POST', '/api/reviews', {'icon': result['key'], 'svg_sha256': result['svg_sha256'], 'status': 'approve'})
    assert status in (200, 201), data
    assert one(client, item['reference_id'])['icon']['review'] == 'approve'
    # picking another sub makes the 72 pair stale and leaves the 64 pair alone
    status, up = client.call('POST', '/api/icons/upload', {'name': '72 test sub 2', 'family': 'sub-36', 'svg': SUB.replace('r="12"', 'r="10"')})
    assert status == 201, up
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'sub', 'icon': up['record']['key'], 'size': 72})
    assert status == 200, data
    assert one(client, item['reference_id'])['state'] == 'stale'
    assert one(client, item['reference_id'], 64)['state'] == state64


def test_lists_only_side_pairs_at_72(client):
    status, data = client.get('/api/combinations', size=72, kind='container', limit=1)
    assert status == 200 and data['total'] == 0 and 'container' not in data['counts']
    status, data = client.get('/api/combinations', size=73)
    assert status == 400
