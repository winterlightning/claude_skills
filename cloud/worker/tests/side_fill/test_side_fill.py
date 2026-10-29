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
    status, answer, rows = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'append': True, 'main': main, 'sub': sub})
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
    status, answer, _ = call('POST', '/api/icons/styled', {'items': [{'source_key': pair[role], 'style': 'fill', 'variant': label, 'svg': svg}],
                                                          'replace': True})
    assert status == 200 and not answer['errors'], answer
    return answer


def test_fill_variants_are_fill_icons_of_their_solo_and_sub():
    pair, _ = a_pair_with_variants()
    for role, family in (('main', 'solo'), ('sub', 'sub')):
        assert pair[role].startswith(family + '/')
        for variant in pair[f'{role}_variants']:
            suffix = '' if variant['variant'] in ('current', 'fill') else '-' + variant['variant']
            assert variant['key'] == f'{pair[role]}--fill{suffix}', variant
    status, answer, _ = call('GET', '/api/icons', family='solo', style='fill', q=pair['main'].split('/', 1)[1], limit=24)
    assert status == 200, answer
    listed = [i for i in answer.get('icons', answer.get('items', [])) if i['key'].startswith(pair['main'] + '--fill')]
    assert listed and all(i.get('family') == 'solo' for i in listed), answer


def test_only_solo_and_sub_icons_have_fill_variants():
    data, _ = get('/api/side-fill/pairs', state='picked', limit=1)
    combined = data['pairs'][0]['picks'][0]['combined']['key'].split('--fill')[0]
    status, answer, _ = call('POST', '/api/icons/styled', {'items': [{'source_key': combined, 'style': 'fill', 'svg': '<svg/>'}]})
    assert status == 200 and answer['errors'] and not answer['results'], answer


def review(key, status):
    sha = drawing(key)['svg_sha256']
    return call('POST', '/api/reviews', {'icon': key, 'status': status, 'svg_sha256': sha})


def restore_reviews(saved):
    """Put back the review each icon had ({key: status}): the tests leave the seeded review state as they found it."""
    for key, status in saved.items():
        status = status or 'ready'          # no review row is Ready
        if (drawing(key)['review'] or 'ready') != status:
            got, answer, _ = review(key, status)
            assert got in (200, 201), (key, answer)


def test_a_redrawn_part_makes_its_picks_stale():
    pair, pick = built_pick_with_fill_variants()
    key = pick['main']['icon']
    saved = {key: drawing(key)['review']}
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
        restore_reviews(saved)
    restored, _ = get('/api/side-fill/pair', id=pair['id'])
    assert restored['picks'][0]['main']['svg_sha256'] == restored['picks'][0]['main']['built_sha']


def test_a_combined_icon_is_approved_only_after_its_parts():
    pair, pick = built_pick_with_fill_variants()
    combined, main, sub = pick['combined']['key'], pick['main']['icon'], pick['sub']['icon']
    saved = {key: drawing(key)['review'] for key in (combined, main, sub)}
    try:
        for key in (combined, main, sub):
            review(key, 'ready')
        status, answer, _ = review(combined, 'approve')
        assert status == 409 and 'Approve the main' in answer['error'], answer
        for key in (main, sub):
            status, answer, _ = review(key, 'approve')
            assert status in (200, 201), answer
        after, _ = get('/api/side-fill/pair', id=pair['id'])
        assert after['picks'][0]['combined']['build_failed'] is False, 'approving both parts clears the failed build'
        status, answer, _ = review(combined, 'approve')
        assert status in (200, 201), answer
        for key in (main, sub):
            review(key, 'ready')
        reset, _ = get('/api/side-fill/pair', id=pair['id'])
        assert reset['picks'][0]['combined']['build_failed'] is True, 'a part back to Ready fails the build again'
    finally:
        restore_reviews({key: saved[key] for key in (main, sub, combined)})


def test_an_output_is_a_side_combination_64_icon_of_style_fill():
    pair, pick = built_pick_with_fill_variants()
    key = pick['combined']['key']
    assert key.startswith('side_combination64/' + pair['id'] + '--fill'), key
    request = urllib.request.Request(f'{BASE}/api/icon?key={urllib.parse.quote(key)}', headers={'User-Agent': 'pictographic-verify/1.0'})
    with urllib.request.urlopen(request, timeout=60) as response:
        record = json.loads(response.read())
    assert record['family'] == 'side_combination64'
    assert record.get('icon_style', record.get('style')) == 'fill'
    assert record['style_of'] == 'side_combination64/' + pair['id']


def test_originals_come_with_the_page_only_when_asked():
    plain, rows_plain = get('/api/side-fill/pairs', limit=60)
    assert all(p['original'] is None for p in plain['pairs'])
    data, rows = get('/api/side-fill/pairs', limit=60, original=1)
    assert rows <= BUDGET['pairs60'] and rows - rows_plain <= 3 * len(data['pairs']), (rows_plain, rows)
    for p in data['pairs']:
        assert p['original'] is None or p['original']['key'] == 'side_combination64/' + p['id']
    one, rows = get('/api/side-fill/pair', id=data['pairs'][0]['id'])
    assert 'original' in one and rows <= BUDGET['pair']


def pair_now(pair_id):
    return get('/api/side-fill/pair', id=pair_id)[0]


def build(pair_id, rank, version, svg, pick):
    return call('POST', '/api/side-fill/build', {'reference_id': pair_id, 'rank': rank, 'version': version, 'svg': svg,
        'main': {'icon': pick['main']['icon'], 'svg_sha256': drawing(pick['main']['icon'])['svg_sha256']},
        'sub': {'icon': pick['sub']['icon'], 'svg_sha256': drawing(pick['sub']['icon'])['svg_sha256']}})


def replace(pair_id, pick, version, layout=None, options='same'):
    return call('POST', '/api/side-fill/pick', {'reference_id': pair_id, 'rank': pick['rank'], 'version': version,
        'main': pick['main']['icon'], 'sub': pick['sub']['icon'],
        'layout': layout or {'main': pick['main']['layout'], 'sub': pick['sub']['layout']},
        'options': pick['options'] if options == 'same' else options})


@pytest.mark.parametrize('change', ['layout', 'options'])
def test_a_build_from_an_older_version_is_refused_and_writes_nothing(change):
    pair, pick = built_pick_with_fill_variants()
    key, old = pick['combined']['key'], drawing(pick['combined']['key'])
    try:
        # Tab 2 changes the pick (a layout moved one unit, or the options) and the pair gets a new version.
        if change == 'layout':
            moved = {'main': [{**b, 'x': b['x'] + 1} for b in pick['main']['layout']], 'sub': pick['sub']['layout']}
            status, answer, _ = replace(pair['id'], pick, pair['version'], layout=moved)
        else:
            status, answer, _ = replace(pair['id'], pick, pair['version'], options={**(pick['options'] or {}), 'sub_scaled': not (pick['options'] or {}).get('sub_scaled')})
        assert status == 200 and answer['version'] > pair['version'], answer
        # Tab 1 still shows the old version: its build is refused and the output is untouched.
        status, answer, _ = build(pair['id'], pick['rank'], pair['version'], old['svg'], pick)
        assert status == 409 and 'changed since it was loaded' in answer['error'], answer
        assert drawing(key)['svg_sha256'] == old['svg_sha256']
        # A pick that names an old version is refused the same way.
        status, answer, _ = replace(pair['id'], pick, pair['version'])
        assert status == 409, answer
    finally:
        now = pair_now(pair['id'])
        status, answer, _ = replace(pair['id'], pick, now['version'])
        assert status == 200, answer
        status, answer, _ = build(pair['id'], pick['rank'], answer['version'], old['svg'], pick)
        assert status == 200 and answer['key'] == key, answer


def test_a_kept_reviewed_output_is_never_written_over():
    pair, pick = built_pick_with_fill_variants()
    svg = drawing(pick['combined']['key'])['svg']
    add = {'reference_id': pair['id'], 'append': True, 'main': pick['main']['icon'], 'sub': pick['sub']['icon'],
           'layout': {'main': pick['main']['layout'], 'sub': pick['sub']['layout']}, 'options': pick['options']}
    status, added, _ = call('POST', '/api/side-fill/pick', add)
    assert status == 200, added
    status, first, _ = build(pair['id'], added['rank'], added['version'], svg, {'main': {'icon': added['main']}, 'sub': {'icon': added['sub']}})
    assert status == 200, first
    kept = first['key']
    review(kept, 'rejected')                    # someone reviewed it: removing the pick keeps the output
    status, answer, _ = call('POST', '/api/side-fill/unpick', {'reference_id': pair['id'], 'rank': added['rank']})
    assert status == 200, answer
    status, again, _ = call('POST', '/api/side-fill/pick', add)
    assert status == 200, again
    status, second, _ = build(pair['id'], again['rank'], again['version'], svg.replace('</svg>', '<path d="M1 1L2 2" stroke="none"/></svg>'),
                              {'main': {'icon': again['main']}, 'sub': {'icon': again['sub']}})
    try:
        assert status == 200 and second['key'] != kept, (kept, second)
        assert drawing(kept)['svg_sha256'] == first['svg_sha256'], 'the kept output must keep its drawing'
    finally:
        call('POST', '/api/side-fill/unpick', {'reference_id': pair['id'], 'rank': again['rank']})


def test_a_tenth_pick_is_refused_and_the_ninth_kept():
    pair, _ = a_pair_with_variants()
    main, sub = pair['main_variants'][0]['key'], pair['sub_variants'][0]['key']
    added = 0
    top = len(pair_now(pair['id'])['picks'])
    # Replacing a rank that has no pick is refused: it is not a way to add one.
    status, answer, _ = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'rank': top + 1, 'main': main, 'sub': sub})
    assert status == 409 and 'no pick at that rank' in answer['error'], answer
    try:
        while len(pair_now(pair['id'])['picks']) < 9:
            status, answer, _ = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'append': True, 'main': main, 'sub': sub})
            assert status == 200, answer
            added += 1
        ninth = [p for p in pair_now(pair['id'])['picks'] if p['rank'] == 9][0]
        status, answer, _ = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'append': True, 'main': main, 'sub': sub})
        assert status == 409 and 'at most 9' in answer['error'], answer
        status, answer, _ = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'rank': 1, 'insert': True, 'main': main, 'sub': sub})
        assert status == 409, answer
        assert [p for p in pair_now(pair['id'])['picks'] if p['rank'] == 9][0] == ninth
        # Replacing the ninth stays possible at 9 picks.
        status, answer, _ = call('POST', '/api/side-fill/pick', {'reference_id': pair['id'], 'rank': 9, 'main': main, 'sub': sub})
        assert status == 200, answer
    finally:
        for _ in range(added):
            top = max(p['rank'] for p in pair_now(pair['id'])['picks'])
            call('POST', '/api/side-fill/unpick', {'reference_id': pair['id'], 'rank': top})


def test_replacing_a_fill_names_the_drawing_it_replaces():
    pair, _ = a_pair_with_variants()
    variant = pair['main_variants'][0]
    current = drawing(variant['key'])
    stale = {'items': [{'source_key': pair['main'], 'style': 'fill', 'variant': variant['variant'],
                        'svg': current['svg'].replace('</svg>', '<path d="M1 1L2 2" stroke="none"/></svg>'), 'expected_sha256': '0' * 64}],
             'replace': True}
    status, answer, _ = call('POST', '/api/icons/styled', stale)
    assert status == 200 and answer['errors'] and answer['errors'][0].get('conflict'), answer
    status, answer, _ = call('POST', '/api/icons/styled', {**stale, 'items': [{**stale['items'][0], 'expected_sha256': None}]})
    assert status == 200 and answer['errors'] and answer['errors'][0].get('conflict'), 'Add fill must not overwrite a variant that exists'
    assert drawing(variant['key'])['svg_sha256'] == current['svg_sha256']


def test_each_save_returns_its_own_version_so_a_slower_tab_cannot_build_over_a_newer_save():
    pair, pick = built_pick_with_fill_variants()
    key, old = pick['combined']['key'], drawing(pick['combined']['key'])
    layouts = [{'main': [{**b, 'x': b['x'] + dx} for b in pick['main']['layout']], 'sub': pick['sub']['layout']} for dx in (1, 2)]
    try:
        # Tab A saves layout A, then tab B saves layout B on top of it.
        status, a, _ = replace(pair['id'], pick, pair['version'], layout=layouts[0])
        assert status == 200, a
        status, b, _ = replace(pair['id'], pick, a['version'], layout=layouts[1])
        assert status == 200, b
        assert a['version'] == pair['version'] + 1 and b['version'] == a['version'] + 1, 'each save reports the version it made'
        # A builds its drawing with the version its save returned: refused, nothing written.
        before, totals = pair_now(pair['id']), get('/api/side-fill/pairs', limit=1)[0]['counts']
        status, answer, _ = build(pair['id'], pick['rank'], a['version'], old['svg'].replace('</svg>', '<path d="M3 3L4 4" stroke="none"/></svg>'), pick)
        assert status == 409, answer
        after = pair_now(pair['id'])
        assert drawing(key)['svg_sha256'] == old['svg_sha256']
        assert after['picks'] == before['picks'] and get('/api/side-fill/pairs', limit=1)[0]['counts'] == totals
        # B builds with its own version: lands.
        status, answer, _ = build(pair['id'], pick['rank'], b['version'], old['svg'], pick)
        assert status == 200, answer
    finally:
        now = pair_now(pair['id'])
        status, answer, _ = replace(pair['id'], pick, now['version'])
        assert status == 200, answer
        status, answer, _ = build(pair['id'], pick['rank'], answer['version'], old['svg'], pick)
        assert status == 200 and answer['key'] == key, answer
