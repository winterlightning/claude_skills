"""A side pair part's name to draw (migration 0016): saved, listed, cleared by null and by picking an icon.
TEST COPIES ONLY (same switches as test_combination_builds.py).

    PICTOGRAPHIC_COMBINATIONS=http://127.0.0.1:8821 PICTOGRAPHIC_COMBINATIONS_WRITE=1 \\
        python3 -m pytest cloud/worker/tests/combinations/test_draw_name.py -q
"""
from __future__ import annotations

import pytest

from test_combination_builds import Client, admin, pytestmark  # noqa: F401  (pytestmark: the same skip)


@pytest.fixture(scope='module')
def client():
    return admin()


def part(client, reference_id, role):
    status, data = client.get('/api/combinations', q=reference_id, limit=1, size=64)
    assert status == 200 and data['items'], data
    return next(p for p in data['items'][0]['parts'] if p['role'] == role)


@pytest.fixture(scope='module')
def side(client):
    status, data = client.get('/api/combinations', kind='side', size=64, limit=1)
    assert status == 200 and data['items'], data
    item = data['items'][0]
    sub = next(p for p in item['parts'] if p['role'] == 'sub')
    yield item['reference_id'], sub['icon']
    client.call('POST', '/api/combinations/parts', {'reference_id': item['reference_id'], 'role': 'sub', 'draw_name': None})


def test_a_name_to_draw_is_saved_and_listed(client, side):
    reference_id, _icon = side
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': reference_id, 'role': 'sub', 'draw_name': '  Rocket launch  '})
    assert status == 200, data
    assert part(client, reference_id, 'sub')['draw_name'] == 'Rocket launch'


def test_null_clears_it_and_a_bad_name_is_refused(client, side):
    reference_id, _icon = side
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': reference_id, 'role': 'sub', 'draw_name': 'x' * 121})
    assert status == 400, data
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': reference_id, 'role': 'sub', 'draw_name': None})
    assert status == 200, data
    assert part(client, reference_id, 'sub')['draw_name'] is None


def test_picking_an_icon_clears_the_name(client, side):
    reference_id, icon = side
    client.call('POST', '/api/combinations/parts', {'reference_id': reference_id, 'role': 'sub', 'draw_name': 'Rocket launch'})
    status, data = client.call('POST', '/api/combinations/parts', {'reference_id': reference_id, 'role': 'sub', 'icon': icon})
    assert status == 200, data
    assert part(client, reference_id, 'sub')['draw_name'] is None
