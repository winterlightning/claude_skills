"""Read-only checks of /api/combinations against a Worker with the combination tables (migration 0009).

    PICTOGRAPHIC_COMBINATIONS=https://pictographic-review-next.pictographic.workers.dev \\
        python3 -m pytest cloud/worker/tests/combinations -q

Only GET requests: safe against the test copy or production.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

import pytest

BASE = os.environ.get('PICTOGRAPHIC_COMBINATIONS', 'http://127.0.0.1:8821')
ROLES = {'side': {'main', 'sub'}, 'container': {'container', 'symbol'}}
SIDE_POSITIONS = {'tl', 'tr', 'bl', 'br', 'ri', 'le', 'bo', 'to'}


def get(path: str, **params):
    url = f'{BASE}{path}?{urllib.parse.urlencode(params)}'
    request = urllib.request.Request(url, headers={'User-Agent': 'pictographic-verify/1.0'})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.status, json.loads(response.read())
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read())


def combinations(**params):
    status, data = get('/api/combinations', **params)
    assert status == 200, data
    return data


@pytest.fixture(scope='module')
def everything():
    return combinations(limit=1)


def test_counts_add_up(everything):
    counts = everything['counts']
    assert set(counts) <= {'side', 'container'}
    assert everything['total'] == sum(n for kind in counts.values() for n in kind.values())
    for kind, states in counts.items():
        for state, n in states.items():
            assert combinations(kind=kind, state=state, limit=1)['total'] == n, (kind, state)


@pytest.mark.parametrize('kind', ['side', 'container'])
def test_items_are_consistent(kind):
    for state in ('built', 'stale', 'unbuilt'):
        data = combinations(kind=kind, state=state, limit=200)
        for item in data['items']:
            assert item['kind'] == kind and item['state'] == state
            roles = {p['role'] for p in item['parts']}
            assert roles <= ROLES[kind] and roles, item['reference_id']
            for part in item['parts']:
                expected = part['built_sha'] is not None and part['current_sha'] is not None \
                    and part['built_sha'] != part['current_sha']
                assert part['stale'] == expected
                assert part['layout'] is None or all({'x', 'y', 'w', 'h'} <= set(box) for box in part['layout'])
                if kind == 'side' and part['role'] == 'sub':
                    assert part['position'] in SIDE_POSITIONS
            built = [p for p in item['parts'] if p['built_sha']]
            if state == 'unbuilt':
                assert not built
            elif state == 'stale':
                assert any(p['stale'] for p in item['parts'])
            else:
                assert built and not any(p['stale'] for p in item['parts'])


def test_side_combinations_have_both_parts():
    data = combinations(kind='side', limit=500)
    assert all({p['role'] for p in item['parts']} == {'main', 'sub'} for item in data['items'])


def test_paging_does_not_overlap(everything):
    first = combinations(limit=50)
    second = combinations(limit=50, offset=first['next_offset'])
    ids = [i['reference_id'] for i in first['items'] + second['items']]
    assert len(ids) == len(set(ids)) == 100
    assert ids == sorted(ids)
    last = combinations(limit=50, offset=everything['total'] - 1)
    assert len(last['items']) == 1 and last['next_offset'] is None


def test_search():
    item = combinations(kind='side', state='built', limit=1)['items'][0]
    by_id = combinations(q=item['reference_id'])
    assert [i['reference_id'] for i in by_id['items']] == [item['reference_id']] and by_id['total'] == 1
    word = (item['concept'] or '').split()[0]
    found = combinations(q=word, limit=500)
    assert found['total'] == len(found['items']) or found['next_offset'] is not None
    assert all(word.lower() in (i['concept'] or '').lower() or i['reference_id'].startswith(word) for i in found['items'])


def test_combined_icon_is_served():
    item = combinations(kind='side', state='built', limit=1)['items'][0]
    assert item['icon'] and item['icon']['key'] == f"side_combination64/{item['reference_id']}"
    request = urllib.request.Request(BASE + item['icon']['preview_url'], headers={'User-Agent': 'pictographic-verify/1.0'})
    with urllib.request.urlopen(request, timeout=120) as response:
        assert response.headers['Content-Type'].startswith('image/svg+xml')
        assert b'<svg' in response.read(200)


@pytest.mark.parametrize('params', [{'kind': 'bad'}, {'state': 'bad'}, {'limit': 0}, {'limit': 501},
                                    {'offset': -1}, {'limit': 'x'}])
def test_bad_input(params):
    status, data = get('/api/combinations', **params)
    assert status == 400 and data['error']
