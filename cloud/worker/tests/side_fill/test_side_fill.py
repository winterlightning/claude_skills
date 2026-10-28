"""Fill side pairs routes (routes/side_fill.rs, migration 0023): answers and D1 rows read.

Every response says what it read in X-D1-Rows-Read; each route has a ceiling here so no change can bring back a
query that reads a table whole. Run against a local Worker on a seeded D1 (production-sized: 3,614 pairs, ~1,800
fill icons), never production:

    python3 cloud/worker/tests/side_fill/make_local_seed.py > /tmp/seed.sql      # + side-fill d1-import, upload, picks
    PICTOGRAPHIC_SIDE_FILL=http://localhost:8821 python3 -m pytest cloud/worker/tests/side_fill -q
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

import pytest

BASE = os.environ.get('PICTOGRAPHIC_SIDE_FILL', 'http://localhost:8821')
SESSION = 'pictographic_session=side-fill-test-session'     # make_local_seed.py's test login

# Ceilings on D1 rows read per request (each measured well under them on the seeded D1).
BUDGET = {'pairs60': 1200, 'pairs120': 2400, 'pair': 80, 'parts48': 500, 'pick': 40, 'unpick': 40}


def call(method: str, path: str, body=None, **params):
    url = f'{BASE}{path}' + (f'?{urllib.parse.urlencode(params)}' if params else '')
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(url, data=data, method=method, headers={
        'User-Agent': 'pictographic-verify/1.0', 'Content-Type': 'application/json', 'Cookie': SESSION, 'Origin': BASE})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.status, json.loads(response.read()), int(response.headers.get('X-D1-Rows-Read', -1))
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read()), int(error.headers.get('X-D1-Rows-Read', -1))


def get(path, **params):
    status, data, rows = call('GET', path, **params)
    assert status == 200, data
    return data, rows


@pytest.mark.parametrize('state', [None, 'picked', 'unpicked', 'uncombined'])
def test_pair_pages_stay_in_budget(state):
    params = {'limit': 60, **({'state': state} if state else {})}
    after, seen, pages = None, set(), 0
    while pages < 4:                       # the first pages, following the keyset cursor
        data, rows = get('/api/side-fill/pairs', **params, **({'after': after} if after else {}))
        assert rows <= BUDGET['pairs60'], (state, pages, rows)
        ids = [p['id'] for p in data['pairs']]
        assert not seen & set(ids), 'a cursor page repeated a pair'
        seen |= set(ids)
        assert all(state is None or p['state'] == state for p in data['pairs'])
        keys = [p['sort_key'] for p in data['pairs']]
        assert keys == sorted(keys)
        pages += 1
        after = data['next']
        if not after:
            break
    assert data['counts']['all'] == sum(n for s, n in data['counts'].items() if s != 'all')


def test_a_big_page_stays_in_budget():
    _, rows = get('/api/side-fill/pairs', limit=120)
    assert rows <= BUDGET['pairs120']


def test_limit_is_capped():
    status, data, _ = call('GET', '/api/side-fill/pairs', limit=10000)
    assert status == 400, data


def test_a_pair_reads_a_handful_of_rows():
    data, _ = get('/api/side-fill/pairs', state='picked', limit=1)
    pair_id = data['pairs'][0]['id']
    pair, rows = get('/api/side-fill/pair', id=pair_id)
    assert rows <= BUDGET['pair']
    assert pair['id'] == pair_id and pair['picks'] and 'neighbours' in pair


@pytest.mark.parametrize('role', ['main', 'sub'])
def test_part_pages_stay_in_budget(role):
    data, rows = get('/api/side-fill/parts', role=role, limit=48)
    assert rows <= BUDGET['parts48']
    assert all(p['role'] == role for p in data['parts'])


def a_pair_with_variants():
    """A picked pair (as GET /pair has it, variants included) whose main and sub both have fill variants."""
    data, _ = get('/api/side-fill/pairs', state='picked', limit=60)
    for listed in data['pairs']:
        pair, _ = get('/api/side-fill/pair', id=listed['id'])
        if pair['main_variants'] and pair['sub_variants']:
            return pair, data['counts']
    raise AssertionError('no picked pair with fill variants on the first page')


def test_the_grid_leaves_variants_out_but_names_each_pick():
    data, _ = get('/api/side-fill/pairs', state='picked', limit=10)
    assert all(not p['main_variants'] and not p['sub_variants'] for p in data['pairs'])
    assert all(pick['main']['label'] and pick['sub']['label'] for p in data['pairs'] for pick in p['picks'])


def test_pick_and_unpick_write_one_pair():
    pair, counts_before = a_pair_with_variants()
    before = pair
    main, sub = pair['main_variants'][0]['key'], pair['sub_variants'][0]['key']
    top = max(p['rank'] for p in before['picks'])
    status, answer, rows = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'rank': top + 1, 'main': main, 'sub': sub})
    assert status == 200, answer
    assert rows <= BUDGET['pick']
    after, _ = get('/api/side-fill/pair', id=pair['id'])
    assert [p['rank'] for p in after['picks']] == [p['rank'] for p in before['picks']] + [top + 1]
    status, answer, rows = call('POST', '/api/side-fill/unpick', {'reference_id': pair['id'], 'rank': top + 1})
    assert status == 200, answer
    assert rows <= BUDGET['unpick']
    restored, _ = get('/api/side-fill/pair', id=pair['id'])
    assert restored['picks'] == before['picks']
    assert get('/api/side-fill/pairs', limit=1)[0]['counts'] == counts_before


def test_pick_refuses_a_variant_of_another_part():
    pair, _ = a_pair_with_variants()
    data, _ = get('/api/side-fill/pairs', state='picked', limit=60)
    other = next(p for p in data['pairs'] if p['main'] != pair['main'] and p['picks'])
    foreign = other['picks'][0]['main']['icon']
    status, answer, _ = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'main': foreign, 'sub': pair['sub_variants'][0]['key']})
    assert status == 400, answer


def test_move_and_insert_keep_every_pick():
    pair, _ = a_pair_with_variants()
    ranks = [p['rank'] for p in pair['picks']]
    main, sub = pair['main_variants'][0]['key'], pair['sub_variants'][0]['key']
    status, answer, rows = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'rank': 1, 'insert': True, 'main': main, 'sub': sub})
    assert status == 200, answer
    assert rows <= BUDGET['pick']
    inserted, _ = get('/api/side-fill/pair', id=pair['id'])
    assert [p['rank'] for p in inserted['picks']] == list(range(1, len(ranks) + 2))
    assert [p['combined'] for p in inserted['picks'][1:]] == [p['combined'] for p in pair['picks']]
    status, answer, rows = call('POST', '/api/side-fill/move', {'reference_id': pair['id'], 'rank': 1, 'to': len(ranks) + 1})
    assert status == 200, answer
    assert rows <= BUDGET['pick']
    moved, _ = get('/api/side-fill/pair', id=pair['id'])
    assert [p['combined'] for p in moved['picks'][:len(ranks)]] == [p['combined'] for p in pair['picks']]
    status, answer, _ = call('POST', '/api/side-fill/unpick', {'reference_id': pair['id'], 'rank': len(ranks) + 1})
    assert status == 200, answer
    restored, _ = get('/api/side-fill/pair', id=pair['id'])
    assert restored['picks'] == pair['picks']


def test_pick_needs_a_login():
    data, _ = get('/api/side-fill/pairs', state='picked', limit=1)
    pair = data['pairs'][0]
    request = urllib.request.Request(f'{BASE}/api/side-fill/pick', method='POST', data=json.dumps({'reference_id': pair['id']}).encode(),
                                     headers={'Content-Type': 'application/json', 'User-Agent': 'pictographic-verify/1.0'})
    with pytest.raises(urllib.error.HTTPError) as error:
        urllib.request.urlopen(request, timeout=60)
    assert error.value.code == 401


def built_pick_with_fill_variants():
    """A pair from the first page whose first pick is built from two fill variants (no outline part)."""
    data, _ = get('/api/side-fill/pairs', state='picked', limit=60)
    for pair in data['pairs']:
        pick = pair['picks'][0]
        if pick['combined'] and pick['main']['label'] != 'outline' and pick['sub']['label'] != 'outline':
            return pair, pick
    raise AssertionError('no built pick of two fill variants on the first page')


def drawing(key):
    """An icon's current drawing ({svg_sha256, svg, review})."""
    request = urllib.request.Request(f'{BASE}/api/combinations/drawings?keys={urllib.parse.quote(key)}', headers={'User-Agent': 'pictographic-verify/1.0'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read())[key]


def upload_variant(pair, role, label, svg):
    status, answer, _ = call('POST', '/api/icons/upload', {'name': f'test {label}', 'family': 'main-fill-48' if role == 'main' else 'sub-fill-32',
        'variant_of': pair[role], 'variant_label': label, 'bypass_validation': True, 'svg': svg})
    assert status == 200, answer
    return answer


def test_a_redrawn_part_makes_its_picks_stale():
    pair, pick = built_pick_with_fill_variants()
    key = pick['main']['icon']
    original = drawing(key)['svg']
    redrawn = original.replace('</svg>', '<path d="M1 1L1 1" fill="none" stroke="none"/></svg>')
    try:
        upload_variant(pair, 'main', pick['main']['label'], redrawn)
        after, _ = get('/api/side-fill/pair', id=pair['id'])
        first = after['picks'][0]
        assert first['main']['icon'] == key
        assert first['main']['svg_sha256'] != first['main']['built_sha'], 'the pick should show its main was redrawn'
    finally:
        upload_variant(pair, 'main', pick['main']['label'], original)
    restored, _ = get('/api/side-fill/pair', id=pair['id'])
    assert restored['picks'][0]['main']['svg_sha256'] == restored['picks'][0]['main']['built_sha']


def review(key, status):
    sha = drawing(key)['svg_sha256']
    return call('POST', '/api/reviews', {'icon': key, 'status': status, 'svg_sha256': sha})


def test_a_combined_icon_is_approved_only_after_its_parts():
    pair, pick = built_pick_with_fill_variants()
    combined, main, sub = pick['combined']['key'], pick['main']['icon'], pick['sub']['icon']
    try:
        status, answer, _ = review(combined, 'approve')
        assert status == 409 and 'Approve the main' in answer['error'], answer
        for key in (main, sub):
            status, answer, _ = review(key, 'approve')
            assert status in (200, 201), answer
        after, _ = get('/api/side-fill/pair', id=pair['id'])
        assert after['picks'][0]['combined']['build_failed'] is False, 'approving both parts clears the failed build'
        status, answer, _ = review(combined, 'approve')
        assert status in (200, 201), answer
    finally:
        for key in (combined, main, sub):
            review(key, 'ready')
    reset, _ = get('/api/side-fill/pair', id=pair['id'])
    assert reset['picks'][0]['combined']['build_failed'] is True
