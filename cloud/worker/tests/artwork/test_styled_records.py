"""POST /api/icons/styled lifecycle (PR #4 review): idempotent publication, check-only changes, required checks,
duplicate keys, people's work kept unless replace, a replacement that leaves no stale pick, the expected-sha guard,
and Browser Edit refused for sharp records while Manual Edit still works. Run against an isolated Worker on scratch
data (migrations through 0019), with the graphics service reachable through its GRAPHICS binding:

    PICTOGRAPHIC_NEW=http://127.0.0.1:8788 python3 -m pytest cloud/worker/tests/artwork -q
"""
from __future__ import annotations

import pytest

from test_manual_upload_geometry import client, svg, upload  # noqa: F401  (the shared fixture and helpers)

A = svg('<path d="M10 24H38"/>')
B = svg('<path d="M10 24H38M24 10V38"/>')
C = svg('<path d="M12 12H36V36H12Z"/>')


def styled(client, items, **extra):
    status, answer = client.call('POST', '/api/icons/styled', {'items': items, **extra})
    assert status == 200, answer
    return answer


def item(source, drawing, check='ok', style='round', **extra):
    return {'source_key': source, 'style': style, 'svg': drawing, 'check': check, **extra}


def card(client, key):
    return client.call('GET', f'/api/icons?keys={key}&style=all')[1]['items'][0]


def served(client, key):
    return str(client.call('GET', f'/api/icon-artwork/svg?icon={key}&v=x')[1])


@pytest.fixture
def source(client):
    return upload(client, 'Styled source', '<path d="M10 24H38"/>')


def test_publication_is_idempotent_and_follows_the_check(client, source):
    key = source + '--round'
    first = styled(client, [item(source, A)])
    assert first['created'] == 1 and first['results'][0]['key'] == key
    sha = first['results'][0]['svg_sha256']
    assert styled(client, [item(source, A)])['unchanged'] == 1
    # same drawing, the check now failing: only the record's check and failed flag change
    flipped = styled(client, [item(source, A, 'fail')])
    assert flipped['check_changed'] == 1 and flipped['results'][0]['svg_sha256'] == sha
    assert card(client, key)['build_failed'] is True
    back = styled(client, [item(source, A, 'ok')])
    assert back['check_changed'] == 1 and card(client, key)['build_failed'] is False
    assert styled(client, [item(source, A, 'ok')])['unchanged'] == 1


def test_missing_check_and_duplicates_are_refused(client, source):
    missing = styled(client, [{'source_key': source, 'style': 'round', 'svg': A}])
    assert missing['created'] == 0 and 'check' in missing['errors'][0]['error']
    twice = styled(client, [item(source, A), item(source, B)])
    assert twice['created'] == 1 and 'twice' in twice['errors'][0]['error']


def test_people_work_is_kept_and_replace_leaves_no_stale_pick(client, source):
    key = source + '--round'
    styled(client, [item(source, A)])
    # someone saves a manual edit B of the round record and picks it (approved)
    art = client.call('GET', f'/api/icon-artwork?icon={key}')[1]
    assert client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': art['svg_sha256'], 'revision': 0, 'source_mode': 'use_org',
                                                     'action': 'upload', 'svg': B, 'filename': 'b.svg'})[0] == 200
    art = client.call('GET', f'/api/icon-artwork?icon={key}')[1]
    assert client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': art['svg_sha256'], 'revision': art['choice']['revision'],
                                                     'source_mode': 'use_upload'})[0] == 200
    assert 'M24 10V38' in served(client, key)

    # a republish of C keeps that work by default ...
    kept = styled(client, [item(source, C)])
    assert kept['updated'] == 0 and kept['kept_manual'][0]['key'] == key
    assert 'M24 10V38' in served(client, key)
    # ... and with replace, C is what the card, the served SVG and the reopened original all show
    replaced = styled(client, [item(source, C)], replace=True)
    assert replaced['updated'] == 1, replaced
    c_sha = replaced['results'][0]['svg_sha256']
    assert 'M12 12H36V36H12Z' in served(client, key)
    assert card(client, key)['svg_sha256'] == c_sha
    reopened = client.call('GET', f'/api/icon-artwork?icon={key}')[1]
    assert reopened['choice'] is None and reopened['source_mode'] == 'use_org' and reopened['record']['svg_sha256'] == c_sha
    assert card(client, key)['review']['state'] == 'ready'


def test_expected_sha_guards_a_changed_record(client, source):
    first = styled(client, [item(source, A)])
    sha = first['results'][0]['svg_sha256']
    stale = styled(client, [item(source, B, expected_sha256='0' * 64)])
    assert stale['updated'] == 0 and stale['errors'][0]['conflict'] is True
    fresh = styled(client, [item(source, B, expected_sha256=sha)])
    assert fresh['updated'] == 1
    assert styled(client, [item(source, C, expected_sha256=None)])['errors'][0]['conflict'] is True


def test_sharp_records_refuse_browser_edit_but_take_manual_edit(client, source):
    key = source + '--sharp'
    dot = svg('<path d="M10 24H38"/><rect fill="currentColor" stroke="none" x="22" y="30" width="4" height="4"/>')
    assert styled(client, [item(source, dot, style='sharp')])['created'] == 1
    status, art = client.call('GET', f'/api/icon-artwork?icon={key}')
    assert status == 200 and 'Sharp' in art['geometry_error'] and not art['record'].get('primitives'), art
    status, edit = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': art['svg_sha256'], 'revision': 0,
                                                             'source_mode': 'use_edited'})
    assert status == 400 and 'Sharp' in edit['error']
    status, _ = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': art['svg_sha256'], 'revision': 0, 'source_mode': 'use_org',
                                                          'action': 'upload', 'svg': dot, 'filename': 'd.svg'})
    assert status == 200
    # the round record of the same icon still opens in Browser Edit
    styled(client, [item(source, A)])
    round_art = client.call('GET', f"/api/icon-artwork?icon={source}--round")[1]
    assert round_art['record'].get('primitives') and 'geometry_error' not in round_art
