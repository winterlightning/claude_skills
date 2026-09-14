"""Reference images: upload validation, serving, feedback storage and the schema upgrade."""
import base64
import http.client
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from icon_set.scripts.deploy import init_database
from icon_set.scripts.reference_images import ReferenceStore
from icon_set.tests import test_gallery

PNG = b'\x89PNG\r\n\x1a\n' + b'\x00' * 32
SVG = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M2 2h20v20z"/></svg>'


class ReferenceStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.store = ReferenceStore(Path(self.tmp.name) / 'refs')

    def test_accepts_png_and_svg_by_content(self):
        png = self.store.save('My Shape (1).PNG', PNG)
        self.assertEqual((png['kind'], png['name']), ('png', 'my-shape-1.png'))
        svg = self.store.save('../../evil.svg', SVG)
        self.assertEqual((svg['kind'], svg['name']), ('svg', 'evil.svg'))
        self.assertEqual(self.store.read(svg['id']), (SVG, 'image/svg+xml'))
        self.assertEqual(self.store.resolve([png['id'], svg['id'], png['id']]), [png, svg])

    def test_rejects_unsafe_or_invalid_uploads(self):
        for data in (b'', b'GIF89a', b'<html></html>', b'<svg', '<svg>é</svg>'.encode('latin-1'),
                     b'<!DOCTYPE svg [<!ENTITY x "y">]><svg xmlns="http://www.w3.org/2000/svg">&x;</svg>',
                     b'\x89PNG\r\n\x1a\n' + b'\x00' * (2 * 1024 * 1024)):
            with self.assertRaises(ValueError):
                self.store.save('x', data)
        image_id = self.store.save('a.png', PNG)['id']
        for ids in ('nope', [image_id] * 5, ['../' + image_id], ['f' * 64], [{'id': image_id}]):
            with self.assertRaises(ValueError):
                self.store.resolve(ids)


class ReferenceServerTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp

    def call(self, method, path, data=None, cookie=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        headers = {'Content-Type': 'application/json'}
        if cookie:
            headers['Cookie'] = cookie
        try:
            connection.request(method, path, body=json.dumps(data) if data is not None else None, headers=headers)
            response = connection.getresponse()
            return response.status, response.read(), response
        finally:
            connection.close()

    def login(self):
        status, _, response = self.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        self.assertEqual(status, 200)
        return response.getheader('Set-Cookie').split(';', 1)[0]

    def upload(self, name, data, cookie):
        return self.call('POST', '/api/reference-images', {'name': name, 'data': base64.b64encode(data).decode()}, cookie)

    def test_upload_serve_and_attach_to_feedback(self):
        self.assertEqual(self.upload('a.png', PNG, None)[0], 401, 'Guests cannot upload')
        cookie = self.login()
        status, body, _ = self.upload('a.png', PNG, cookie)
        self.assertEqual(status, 201, body)
        png = json.loads(body)
        svg = json.loads(self.upload('b.svg', SVG, cookie)[1])
        self.assertEqual(self.upload('c.gif', b'GIF89a', cookie)[0], 400)
        self.assertEqual(self.call('POST', '/api/reference-images', {'name': 'x', 'data': '%%%'}, cookie)[0], 400)

        status, content, response = self.call('GET', '/api/reference-images?id=' + svg['id'])
        self.assertEqual((status, content, response.getheader('Content-Type')), (200, SVG, 'image/svg+xml'))
        self.assertIn('sandbox', response.getheader('Content-Security-Policy'))
        self.assertEqual(self.call('GET', '/api/reference-images?id=' + 'f' * 64)[0], 404)
        self.assertFalse(any(self.dist.rglob(png['id'] + '*')), 'References are never stored under dist')

        feedback = {'icon': 'sub/square', 'feedback': 'Match this', 'svg_sha256': 'abc'}
        self.assertEqual(self.call('POST', '/api/feedback', dict(feedback, reference_images=['f' * 64]))[0], 400)
        self.assertEqual(self.call('POST', '/api/feedback', dict(feedback, reference_images=[png['id'], svg['id']]))[0], 201)
        self.assertEqual(self.call('POST', '/api/feedback', dict(feedback, feedback='No images'))[0], 201)
        rows = json.loads(self.call('GET', '/api/feedback?icon=sub/square')[1])
        self.assertEqual([row['reference_images'] for row in rows], [[], [png, svg]])
        feed = json.loads(self.call('GET', '/api/feedback-feed')[1])
        self.assertEqual(feed[1]['reference_images'], [png, svg])

    def test_existing_database_gains_reference_column(self):
        database = Path(self.tmp.name) / 'old.sqlite3'
        with sqlite3.connect(database) as connection:
            connection.execute('CREATE TABLE feedback (id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL, '
                               'svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL)')
            connection.execute("INSERT INTO feedback VALUES (1, 'sub/square', 'Old', 'abc', '2026-01-01')")
        connection.close()
        init_database(database)
        init_database(database)
        with sqlite3.connect(database) as connection:
            self.assertEqual(connection.execute('SELECT feedback, reference_images FROM feedback').fetchall(), [('Old', '[]')])
        connection.close()


if __name__ == '__main__':
    unittest.main()
