#!/usr/bin/env python3
"""Exercise thumbnail selection through a real local Worker, D1, R2 and graphics service.

Requires empty, migrated local storage and ADMIN_USERS={"tester":"preview-only"}.
Refuses remote URLs. Creates synthetic artwork only; emits keys for browser checks.
"""
import argparse
import http.cookiejar
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request


class Client:
    def __init__(self, base):
        url = urllib.parse.urlsplit(base)
        if url.scheme != 'http' or url.hostname not in ('127.0.0.1', 'localhost', '::1'):
            raise ValueError('This mutating fixture requires a loopback HTTP Worker.')
        self.base = base.rstrip('/')
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(self, method, path, body=None, expected=200):
        request = urllib.request.Request(self.base + path, method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={'Content-Type': 'application/json', 'User-Agent': 'thumbnail-regression/1.0'})
        try:
            with self.opener.open(request, timeout=60) as response:
                status, raw = response.status, response.read()
        except urllib.error.HTTPError as error:
            status, raw = error.code, error.read()
        try:
            answer = json.loads(raw)
        except ValueError:
            answer = raw.decode()
        assert status == expected, (method, path, status, answer)
        return answer


def query(path, **params):
    return path + '?' + urllib.parse.urlencode(params)


def svg(canvas, extra=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}" '
            'fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" '
            f'stroke-linejoin="round"><path d="M8 8H{canvas-8}V{canvas-8}H8Z"/>{extra}</svg>')


def check(client, family, canvas):
    if family != 'solo':
        families = client.call('GET', '/api/icon-families')['families']
        existing = next((row for row in families if row['id'] == family), None)
        if existing:
            assert existing['canvas_size'] == canvas
        else:
            client.call('POST', '/api/icon-families', {'id': family, 'name': family, 'canvas_size': canvas}, expected=201)
    record = client.call('POST', '/api/icons/upload',
        {'name': f'Thumbnail regression {canvas}', 'family': family, 'svg': svg(canvas)}, expected=201)['record']
    key = record['key']
    art_path = query('/api/icon-artwork', icon=key)
    art = client.call('GET', art_path)
    original = art['svg_sha256']
    original_svg = client.call('GET', query('/api/icon-artwork/svg', icon=key, variant='use_org'))
    # Save an original-base edit without changing its validation/approval.
    edit = client.call('POST', '/api/stroke-edits', {'icon': key, 'svg_sha256': original,
        'revision': 0, 'offsets': {'contour:stroke-1': [1, 0]}})
    preview = client.call('GET', query('/api/icon-artwork/svg', icon=key, variant='browser_edit', sha=original))
    assert f'viewBox="0 0 {canvas} {canvas}"' in preview
    assert preview != original_svg
    # Custom preview rendering must not bypass the existing validation gate.
    client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
        'revision': 0, 'source_mode': 'use_edited', 'edit_revision': 1}, expected=400)
    candidate = svg(canvas, f'<path d="M16 {canvas/2:g}H{canvas-16}"/>')
    uploaded = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
        'revision': 0, 'source_mode': 'use_org', 'action': 'upload', 'svg': candidate})
    manual_sha = uploaded['choice']['uploaded']['svg_sha256']
    manual_svg = client.call('GET', query('/api/icon-artwork/svg', icon=key, variant='use_upload'))
    picked = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
        'revision': 1, 'source_mode': 'use_upload'})
    # Reopening caches the selected graph. It must not replace the original base.
    reopened = client.call('GET', art_path)
    assert reopened['svg_sha256'] == original and reopened['source_mode'] == 'use_upload'
    listed = client.call('GET', query('/api/icons', keys=key))['items'][0]
    assert listed['artwork_source'] == 'use_upload' and listed['svg_sha256'] == manual_sha
    version = urllib.parse.parse_qs(urllib.parse.urlsplit(listed['preview_url']).query)['v'][0]
    assert version == manual_sha
    served = client.call('GET', '/' + listed['preview_url'].removeprefix('../'))
    assert served == manual_svg
    # Save an edit of the candidate and verify Pick resolves each base independently.
    client.call('POST', '/api/stroke-edits', {'icon': key, 'svg_sha256': manual_sha,
        'revision': 0, 'offsets': {'contour:stroke-1': [2, 0]}})
    manual_preview = client.call('GET', query('/api/icon-artwork/svg', icon=key, variant='browser_edit', sha=manual_sha))
    assert manual_preview != preview and manual_preview != manual_svg
    assert client.call('GET', query('/api/icon-artwork/svg', icon=key, variant='browser_edit', sha=original)) == preview
    client.call('GET', query('/api/icon-artwork/svg', icon=key, variant='browser_edit', sha='stale'), expected=409)
    client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
        'revision': 0, 'source_mode': 'use_org'}, expected=409)
    # Original remains intact after selecting a candidate; then leave it picked for browser QA.
    client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
        'revision': picked['choice']['revision'], 'source_mode': 'use_org'})
    assert client.call('GET', query('/api/icon-artwork/svg', icon=key)) == original_svg
    art = client.call('GET', art_path)
    client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
        'revision': art['choice']['revision'], 'source_mode': 'use_upload'})
    if family == 'solo':
        # Exercise a validated Browser Edit selection too, using the existing human-review path.
        client.call('POST', '/api/stroke-edits', {'icon': key, 'svg_sha256': original,
            'revision': 1, 'offsets': {'contour:stroke-1': [1, 0]},
            'validation_override': {'reason': 'Synthetic local verification fixture'}})
        art = client.call('GET', art_path)
        selected = client.call('POST', '/api/icon-artwork', {'icon': key, 'svg_sha256': original,
            'revision': art['choice']['revision'], 'source_mode': 'use_edited', 'edit_revision': 2})
        row = client.call('GET', query('/api/icons', keys=key))['items'][0]
        assert row['artwork_source'] == 'use_edited'
        assert client.call('GET', '/' + row['preview_url'].removeprefix('../')) == preview
        assert client.call('GET', art_path)['svg_sha256'] == original
    print(f'{family}: save, Pick preview, cached-base reopen, thumbnail bytes, stale guards, restore passed')
    return {'key': key, 'family': family, 'canvas': canvas, 'original_sha': original, 'manual_sha': manual_sha}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', default='http://127.0.0.1:8893')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    client = Client(args.base_url)
    client.call('POST', '/api/auth/login', {'username': 'tester', 'password': 'preview-only'})
    results = [check(client, family, canvas) for family, canvas in
               [('solo-64', 64), ('icon-72', 72), ('main-54', 54), ('sub-36', 36), ('solo', 48)]]
    args.output.write_text(json.dumps(results, indent=2) + '\n')


if __name__ == '__main__':
    main()
