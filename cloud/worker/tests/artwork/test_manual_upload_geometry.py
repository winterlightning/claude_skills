"""Manual Edit and Pick do not need Browser Edit geometry (PR #3 review).

An uploaded original Browser Edit cannot read (here: transforms) still loads its artwork choices, takes a manual
replacement and a pick, and reopens on it; Browser Edit of that original is still refused. Run against an isolated
Worker on scratch data, with the graphics service reachable through its GRAPHICS binding:

    PICTOGRAPHIC_NEW=http://127.0.0.1:8787 python3 -m pytest cloud/worker/tests/artwork -q
"""
from __future__ import annotations

import http.cookiejar
import json
import os
import urllib.error
import urllib.request

import pytest

BASE = os.environ.get('PICTOGRAPHIC_NEW', 'http://127.0.0.1:8787')


class Client:
    def __init__(self):
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(self, method, path, body=None):
        request = urllib.request.Request(BASE + path, data=json.dumps(body).encode() if body is not None else None, method=method,
                                         headers={'Content-Type': 'application/json', 'User-Agent': 'pictographic-verify/1.0'})
        try:
            with self.opener.open(request, timeout=120) as response:
                status, raw = response.status, response.read()
        except urllib.error.HTTPError as error:
            status, raw = error.code, error.read()
        try:
            return status, json.loads(raw)
        except ValueError:
            return status, raw.decode('utf-8', 'replace')


def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
            f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


@pytest.fixture(scope='module')
def client():
    try:
        urllib.request.urlopen(urllib.request.Request(BASE + '/api/runtime', headers={'User-Agent': 'pictographic-verify/1.0'}), timeout=10)
    except OSError:
        pytest.skip(f'{BASE} is not running')
    c = Client()
    assert c.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})[0] == 200
    return c


def upload(client, name, body):
    status, answer = client.call('POST', '/api/icons/upload', {'name': name, 'family': 'solo', 'svg': svg(body)})
    assert status in (200, 201), answer
    return answer['record']['key']


def test_transformed_original_takes_manual_replacement_and_pick(client):
    key = upload(client, 'Transformed original', '<g transform="translate(2 0)"><path d="M10 24H36"/></g>')
    status, art = client.call('GET', f'/api/icon-artwork?icon={key}')
    assert status == 200, art
    assert 'transforms' in art['geometry_error']
    assert not art['record'].get('primitives')

    status, saved = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': art['svg_sha256'], 'revision': 0, 'source_mode': 'use_org',
                                                              'action': 'upload', 'svg': svg('<path d="M10 24H38M24 10V38"/>'), 'filename': 'm.svg'})
    assert status == 200, saved
    art = client.call('GET', f'/api/icon-artwork?icon={key}')[1]
    upload_sha = art['choice']['uploaded']['svg_sha256']
    status, picked = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': art['svg_sha256'],
                                                               'revision': art['choice']['revision'], 'source_mode': 'use_upload'})
    assert status == 200 and picked['record']['review_status'] == 'approve', picked

    status, reopened = client.call('GET', f'/api/icon-artwork?icon={key}')
    assert status == 200 and reopened['source_mode'] == 'use_upload' and reopened['record']['svg_sha256'] == upload_sha
    assert 'M24 10V38' in str(client.call('GET', f'/api/icon-artwork/svg?icon={key}&v=x')[1])
    assert client.call('GET', f'/api/icons?keys={key}')[1]['items'][0]['svg_sha256'] == upload_sha

    # Browser Edit needs the strokes: picking an edit of the transformed original is still refused ...
    status, _ = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': reopened['svg_sha256'],
                                                          'revision': reopened['choice']['revision'], 'source_mode': 'use_edited'})
    assert status in (400, 503)
    # ... while the manual upload, a flat drawing, opens in Browser Edit as its own base.
    status, base = client.call('GET', f'/api/icon-artwork?icon={key}&base={upload_sha}')
    assert status == 200 and base['base']['graph']['primitives'], base


def test_readable_upload_still_offers_its_strokes(client):
    key = upload(client, 'Plain original', '<path d="M10 24H38"/>')
    status, art = client.call('GET', f'/api/icon-artwork?icon={key}')
    assert status == 200 and art['record']['primitives'] and 'geometry_error' not in art, art
