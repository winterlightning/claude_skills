"""Text-symbol saves against a disposable local Worker/D1 copy, never production.

PICTOGRAPHIC_COMBINATIONS=http://127.0.0.1:8886 PICTOGRAPHIC_COMBINATIONS_WRITE=1 \
PICTOGRAPHIC_TEST_USERNAME=local PICTOGRAPHIC_TEST_PASSWORD=layout-test \
    python3 -m pytest cloud/worker/tests/combinations/test_container_text_layouts.py -q

The test copy needs the container references and drawings from the library, including
the 8K screen reference below. Uploads and layout saves are intentional test writes.
"""
from copy import deepcopy
import json
import os
from urllib.parse import urlsplit, urlencode
from uuid import uuid4

import pytest

from test_combination_builds import BASE, ROOT, Client, compose

pytestmark = pytest.mark.skipif(
    os.environ.get('PICTOGRAPHIC_COMBINATIONS_WRITE') != '1'
    or urlsplit(BASE).hostname not in ('127.0.0.1', 'localhost', '::1'),
    reason='requires an explicitly enabled disposable loopback Worker',
)
REFERENCE = '069bf6b4-e362-4e8f-901f-ee15d4d77042'
ATTRS = 'fill="none" stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'


def text_svg(x=8):
    # A wide native two-letter label, deliberately wider than a 32/36 symbol canvas.
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 24" {ATTRS}>'
            '<desc>{"typeface":"v2","text":"HI","manual_elements":true}</desc>'
            f'<path d="M{x} 4 V20 M20 4 V20 M{x} 12 H20"/>'
            '<path d="M32 4 H40 M36 4 V20 M32 20 H40"/></svg>')


@pytest.fixture(scope='module')
def client():
    client = Client()
    status, data = client.call('POST', '/api/auth/login', {
        'username': os.environ['PICTOGRAPHIC_TEST_USERNAME'],
        'password': os.environ['PICTOGRAPHIC_TEST_PASSWORD'],
    })
    assert status == 200, data
    yield client
    client.call('POST', '/api/auth/logout', {})


def one(client, size):
    status, data = client.get('/api/combinations', kind='container', q=REFERENCE, size=size, limit=1)
    assert status == 200 and len(data['items']) == 1, data
    return data['items'][0]


def drawings(client, icons):
    status, result = client.get('/api/combinations/drawings', keys=','.join(icons.values()))
    assert status == 200 and all(result.get(k, {}).get('svg') for k in icons.values()), result
    return result


def make_request(client, size, symbol=None, box=None):
    item = one(client, size)
    icons = {p['role']: p['icon'] for p in item['parts']}
    if symbol:
        icons['symbol'] = symbol
    art = drawings(client, icons)
    made = compose(art[icons['container']]['svg'], art[icons['symbol']]['svg'], {
        'canvas': size, 'box': box or {'x': 13, 'y': 23, 'w': 40, 'h': 16}, 'nativeText': True,
    })
    made['layout']['symbol'][0].update(scope='pair', native_text=True)
    return {
        'reference_id': REFERENCE, 'expected_sha256': (item['icon'] or {}).get('svg_sha256'),
        'svg': made['svg'], 'parts': {
            role: {'icon': key, 'svg_sha256': art[key]['svg_sha256'], 'layout': made['layout'][role]}
            for role, key in icons.items()
        },
    }


def save_and_reopen(client, size, request):
    status, data = client.call('POST', '/api/combinations/build', {'size': size, 'builds': [request]})
    assert status == 200 and data['results'][0]['ok'], data
    built = data['results'][0]
    after = one(client, size)
    for part in after['parts']:
        sent = request['parts'][part['role']]
        assert part['icon'] == sent['icon']
        assert part['layout'] == sent['layout']
        assert part['built_sha'] == sent['svg_sha256']
    assert after['icon']['key'] == built['key']
    assert after['icon']['svg_sha256'] == built['svg_sha256']
    # Icon review reads the same current drawing as the reopened layout editor.
    status, icon = client.get('/api/icon', key=built['key'])
    assert status == 200 and icon['svg_sha256'] == built['svg_sha256'], icon
    url = BASE + '/api/icon-artwork/svg?' + urlencode({'icon': built['key']})
    with client.opener.open(url) as response:
        assert response.read().decode() == request['svg']
    return built


def upload(client, family, svg, role='symbol', reference=REFERENCE):
    status, data = client.call('POST', '/api/icons/upload', {
        'name': 'Container text save regression', 'family': family, 'category': 'text',
        'svg': svg, 'approve': False, 'bypass_validation': True,
        'reference': {'id': reference, 'role': role},
    })
    assert status in (200, 201), data
    return data['record']['key']


def test_64_existing_text_moves_resizes_and_keeps_artwork(client):
    other_size = one(client, 72)
    # Reset the pick so this regression can be rerun after the letter-edit tests.
    status, data = client.call('POST', '/api/combinations/parts', {
        'reference_id': REFERENCE, 'role': 'symbol', 'icon': f'text/session-text-{REFERENCE}', 'size': 64,
    })
    assert status == 200, data
    before = one(client, 64)
    symbol = next(p for p in before['parts'] if p['role'] == 'symbol')
    assert symbol['icon'].startswith('text/'), 'test copy must start with the existing native text pick'
    art = drawings(client, {'symbol': symbol['icon']})
    for box in ({'x': 14, 'y': 23, 'w': 40, 'h': 16}, {'x': 16, 'y': 22, 'w': 36, 'h': 18}):
        save_and_reopen(client, 64, make_request(client, 64, box=box))
    assert drawings(client, {'symbol': symbol['icon']}) == art
    assert one(client, 72) == other_size
    # Explicitly picking the existing text is valid too.
    status, data = client.call('POST', '/api/combinations/parts', {
        'reference_id': REFERENCE, 'role': 'symbol', 'icon': symbol['icon'], 'size': 64,
    })
    assert status == 200, data


def test_text_build_still_checks_revision_layout_and_svg(client):
    request = make_request(client, 64)
    before = one(client, 64)
    for mutate in (
        lambda r: r['parts']['symbol'].update(svg_sha256='0' * 64),
        lambda r: r['parts']['symbol'].update(icon='text/does-not-exist'),
        lambda r: r['parts']['symbol'].update(layout=[{'x': 'bad'}]),
        lambda r: r['parts']['container'].update(icon=r['parts']['symbol']['icon']),
        lambda r: r.update(svg=r['svg'].replace('</svg>', '<script>alert(1)</script></svg>')),
    ):
        invalid = deepcopy(request)
        mutate(invalid)
        status, data = client.call('POST', '/api/combinations/build', {'size': 64, 'builds': [invalid]})
        assert status == 200 and not data['results'][0]['ok'], data
        assert one(client, 64) == before


@pytest.mark.parametrize('size,family', [(64, 'symbol'), (72, 'symbol-36')])
def test_text_upload_edit_save_and_size_isolation(client, size, family):
    other_size = one(client, 72 if size == 64 else 64)
    before = one(client, size)
    if size == 72:
        # The exact recovered drawing used by Build and save in the 72px editor.
        defaults = json.loads((ROOT / 'published/gallery/container-layouts72.json').read_text())
        svg = defaults['pairs'][REFERENCE]['text_svg']
    else:
        svg = text_svg()
    key = upload(client, family, svg)
    # Upload alone must not change picks or layouts. Reuploading a previously picked
    # symbol can legitimately change its current revision and make the pair stale.
    after_upload = one(client, size)
    assert [(p['role'], p['icon'], p['layout']) for p in after_upload['parts']] == [
        (p['role'], p['icon'], p['layout']) for p in before['parts']]
    assert after_upload['icon'] == before['icon']
    built = save_and_reopen(client, size, make_request(client, size, symbol=key))
    assert built['build_failed'], 'recovered text must not silently acquire approval'
    assert drawings(client, {'symbol': key})[key]['review'] != 'approve'
    # Editing individual letter geometry uploads a new revision, then persists the layout again.
    key = upload(client, family, text_svg(x=10))
    box = {'x': 15.5, 'y': 24, 'w': 38, 'h': 16} if size == 72 else {'x': 14, 'y': 22, 'w': 36, 'h': 18}
    save_and_reopen(client, size, make_request(client, size, symbol=key, box=box))
    assert one(client, 72 if size == 64 else 64) == other_size


@pytest.mark.parametrize('family,role,canvas', [
    ('container', 'container', 64), ('symbol', 'symbol', 32),
    ('container-72', 'container', 72), ('symbol-36', 'symbol', 36),
])
def test_component_upload_roles(client, family, role, canvas):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}" {ATTRS}><path d="M8 8 H24 V24"/></svg>'
    key = upload(client, family, svg, role, reference=str(uuid4()))
    assert key.startswith(family + '/')


@pytest.mark.parametrize('family,role', [
    ('symbol-36', 'container'), ('container-72', 'symbol'),
    ('sub-36', 'symbol'), ('main-54', 'container'), ('symbol', 'sub'),
])
def test_unrelated_upload_roles_still_rejected(client, family, role):
    status, data = client.call('POST', '/api/icons/upload', {
        'name': 'Invalid role', 'family': family, 'svg': text_svg(),
        'reference': {'id': REFERENCE, 'role': role},
    })
    assert status == 400 and 'matching the family' in data['error'], data


def test_72_reference_upload_still_checks_svg(client):
    status, data = client.call('POST', '/api/icons/upload', {
        'name': 'Unsafe text', 'family': 'symbol-36',
        'svg': text_svg().replace('</svg>', '<script>alert(1)</script></svg>'),
        'reference': {'id': REFERENCE, 'role': 'symbol'},
    })
    assert status == 400 and 'reference must' not in data['error'], data


def test_legacy_text_cannot_be_picked_as_a_72px_symbol(client):
    before = one(client, 72)
    status, data = client.call('POST', '/api/combinations/parts', {
        'reference_id': REFERENCE, 'role': 'symbol', 'size': 72,
        'icon': f'text/session-text-{REFERENCE}',
    })
    assert status == 400, data
    assert one(client, 72) == before
