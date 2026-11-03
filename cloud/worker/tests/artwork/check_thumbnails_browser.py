#!/usr/bin/env python3
"""Check real gallery/Pick images in Microsoft Edge against the isolated Worker fixture.

Serves committed gallery assets with a read-only API proxy to loopback. No browser
requests can mutate storage. Install Playwright's Python package; use installed Edge.
"""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[4]


class Gallery(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def do_GET(self):
        if not self.path.startswith('/api/'):
            return super().do_GET()
        try:
            response = urllib.request.urlopen(self.server.worker + self.path, timeout=60)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            body = response.read()
            self.send_response(response.status)
            self.send_header('Content-Type', response.headers.get('Content-Type', 'application/json'))
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--worker', default='http://127.0.0.1:8893')
    parser.add_argument('--fixtures', type=Path, required=True)
    parser.add_argument('--screenshots', type=Path, required=True)
    parser.add_argument('--stored-assets', action='store_true', help='Read gallery assets through the Worker from local R2')
    args = parser.parse_args()
    url = urllib.parse.urlsplit(args.worker)
    if url.scheme != 'http' or url.hostname not in ('localhost', '127.0.0.1', '::1'):
        raise ValueError('Use an isolated loopback Worker.')
    args.screenshots.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Gallery, directory=str(ROOT / 'published')))
    server.worker = args.worker.rstrip('/')
    threading.Thread(target=server.serve_forever, daemon=True).start()
    origin = args.worker.rstrip('/') if args.stored_assets else f'http://127.0.0.1:{server.server_port}'
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel='msedge', headless=True)
            page = browser.new_page(viewport={'width': 1400, 'height': 1000})
            page.route('**/*', lambda route: route.continue_() if route.request.method == 'GET' else route.abort())
            pending = set()
            last_artwork = [0]

            def artwork_request(request, finished=False):
                if '/api/icon-artwork?' in request.url:
                    if finished:
                        pending.discard(request)
                    else:
                        pending.add(request)
                    last_artwork[0] = time.monotonic()

            page.on('request', artwork_request)
            page.on('requestfinished', lambda request: artwork_request(request, True))
            page.on('requestfailed', lambda request: artwork_request(request, True))
            for row in json.loads(args.fixtures.read_text()):
                query = urllib.parse.urlencode({'tab': 'icons', 'family': row['family'], 'status': 'approve',
                                                'page_size': 192, 'view': 'generated'})
                page.goto(f'{origin}/gallery/index.html?{query}')
                card = page.locator(f'.card[data-key="{row["key"]}"]')
                card.wait_for()
                card.scroll_into_view_if_needed()
                thumbnail = card.locator('.tile img').first
                thumbnail.evaluate('(img)=>img.decode()')
                assert thumbnail.evaluate('(img)=>img.naturalWidth>0')
                card.locator('.tile').click()
                # Wrangler's development stream stays open; wait for inspector requests only.
                deadline = time.monotonic() + 30
                while pending or time.monotonic() - last_artwork[0] < .2:
                    assert time.monotonic() < deadline, 'Inspector artwork requests did not finish'
                    page.wait_for_timeout(50)
                page.locator('#editingTab').click()
                page.locator('#strokeBase').wait_for()
                for value, sha in [('original', row['original_sha']), ('upload', row['manual_sha'])]:
                    page.locator('#browserEditTab').click()
                    page.locator('#strokeBase').select_option(value)
                    page.locator('#pickEditTab').click()
                    page.wait_for_function('sha => document.querySelector("#pickPreview_use_edited").src.includes("sha="+sha)', arg=sha)
                    for mode in ['use_org', 'use_upload', 'use_edited']:
                        image = page.locator('#pickPreview_' + mode)
                        image.wait_for(state='visible')
                        image.evaluate('(img)=>img.decode()')
                        assert image.evaluate('(img)=>img.naturalWidth>0')
                    page.screenshot(path=str(args.screenshots / f'{row["family"]}-{value}.png'))
                print(row['family'] + ': grid image and all three Pick images load for both edit bases')
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    main()
