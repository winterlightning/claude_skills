"""Gallery snapshots, feedback persistence, and public file boundaries."""
import http.client
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

from icon_set.scripts.gallery import stage_gallery
from icon_set.scripts.deploy import create_server, init_database


def manifest(root, family, folder, name):
    directory = root / folder
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'manifest.json').write_text(json.dumps({'icons': [
        {'family': family, 'icon_id': name, 'name': name, 'svg_sha256': 'abc'}
    ]}))
    (directory / (name + '.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')


class GalleryTests(unittest.TestCase):
    def test_partial_build_combines_new_and_existing_families_deterministically(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            staged, published = root / 'stage', root / 'dist'
            staged.mkdir()
            manifest(published, 'sub', 'sub32', 'old')
            manifest(published, 'solo', 'solo48', 'retained')
            manifest(staged, 'sub', 'sub32', 'new')
            gallery = stage_gallery(staged, published, ['sub32', 'solo48', 'container64'])
            rows = json.loads((gallery / 'icons.json').read_text())['icons']
            self.assertEqual([r['key'] for r in rows], ['solo/retained', 'sub/new'])
            self.assertEqual(rows[1]['preview_url'], '../sub32/new.svg')
            first = (gallery / 'icons.json').read_bytes()
            other = root / 'second'
            other.mkdir()
            manifest(other, 'sub', 'sub32', 'new')
            self.assertEqual(first, (stage_gallery(other, published, ['sub32', 'solo48']) / 'icons.json').read_bytes())


    def test_failed_build_preserves_gallery_and_disabling_qa_still_builds_it(self):
        from icon_set.scripts import build as builder
        from icon_set.model.icons.registry import create
        from icon_set.tests.test_library_qa import small_hole_icon
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            dist = Path(tmp) / 'dist'
            with patch.object(builder, 'icons_in', return_value=[create('square')]):
                self.assertEqual(builder.build(dist, None, write_png=False, only=['sub'], report=False), 0)
            before = (dist / 'gallery/icons.json').read_bytes()
            self.assertTrue((dist / 'gallery/index.html').is_file())
            with patch.object(builder, 'icons_in', return_value=[small_hole_icon()]):
                self.assertEqual(builder.build(dist, None, write_png=False, only=['sub'], report=False), 1)
            self.assertEqual((dist / 'gallery/icons.json').read_bytes(), before)


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.dist = self.root / 'dist'
        self.dist.mkdir()
        manifest(self.dist, 'sub', 'sub32', 'square')
        stage_gallery(self.dist, self.dist, ['sub32'])
        self.database = self.root / 'data/feedback.sqlite3'
        self.server = create_server(self.dist, self.database, port=0)
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def request(self, method, path, data=None, headers=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        try:
            connection.request(method, path, body=json.dumps(data) if data is not None else None,
                               headers=headers or {'Content-Type': 'application/json'})
            response = connection.getresponse()
            return response.status, response.read()
        finally:
            connection.close()

    def test_gallery_and_feedback_round_trip_survives_new_server(self):
        self.assertEqual(self.request('GET', '/')[0], 302)
        self.assertEqual(self.request('GET', '/gallery/index.html')[0], 200)
        self.assertEqual(self.request('GET', '/sub32/square.svg')[0], 200)
        text = 'Make the corners softer — keep the size.'
        self.assertEqual(self.request('POST', '/api/feedback', {'icon': 'sub/square', 'feedback': text, 'svg_sha256': 'abc'})[0], 201)
        code, data = self.request('GET', '/api/feedback?icon=sub%2Fsquare')
        self.assertEqual(code, 200)
        self.assertEqual(json.loads(data)[0]['feedback'], text)
        self.server.shutdown()
        self.server.server_close()
        replacement = create_server(self.dist, self.database, port=0)
        self.server = replacement
        self.addCleanup(replacement.server_close)
        self.addCleanup(replacement.shutdown)
        threading.Thread(target=replacement.serve_forever, daemon=True).start()
        self.assertEqual(json.loads(self.request('GET', '/api/feedback?icon=sub%2Fsquare')[1])[0]['feedback'], text)

    def test_review_states_persist_and_new_svg_requires_review(self):
        key = 'sub/square'
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'ready')
        for status in ('pending', 're-generated', 'approve', 'ready', 'approve'):
            self.assertEqual(self.request('POST', '/api/reviews',
                {'icon': key, 'svg_sha256': 'abc', 'status': status})[0], 201)
            init_database(self.database)  # Startup migration preserves explicit choices.
            self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], status)
        catalog = self.dist / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        data['icons'][0]['svg_sha256'] = 'changed'
        catalog.write_text(json.dumps(data))
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'ready')
        self.assertEqual(self.request('POST', '/api/reviews',
            {'icon': key, 'svg_sha256': 'abc', 'status': 'approve'})[0], 409)

    def test_feedback_marks_pending_and_migration_keeps_later_approval(self):
        key = 'sub/square'
        payload = {'icon': key, 'svg_sha256': 'abc', 'status': 'approve'}
        self.assertEqual(self.request('POST', '/api/reviews', payload)[0], 201)
        self.assertEqual(self.request('POST', '/api/feedback',
            {'icon': key, 'svg_sha256': 'abc', 'feedback': 'Please adjust corners'})[0], 201)
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'pending')
        self.assertEqual(self.request('POST', '/api/reviews', payload)[0], 201)
        init_database(self.database)
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'approve')

    def test_published_variant_marks_pending_parent_regenerated(self):
        key = 'sub/square'
        self.request('POST', '/api/feedback',
                     {'icon': key, 'svg_sha256': 'abc', 'feedback': 'Round corners'})
        catalog = self.dist / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        data['icons'].append(dict(data['icons'][0], key='sub/square-v2',
                                  icon_id='square-v2', variant_of='square'))
        catalog.write_text(json.dumps(data))
        states = json.loads(self.request('GET', '/api/reviews')[1])
        self.assertEqual(states[key], 're-generated')
        self.assertEqual(states['sub/square-v2'], 'ready')
        self.request('POST', '/api/reviews',
                     {'icon': key, 'svg_sha256': 'abc', 'status': 'approve'})
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'approve')

    def test_legacy_review_schema_migrates_without_losing_decisions(self):
        import sqlite3
        with sqlite3.connect(self.database) as connection:
            connection.execute('DROP TABLE reviews')
            connection.execute("""CREATE TABLE reviews (
                icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('ready', 'pending', 'approve')),
                updated_at TEXT NOT NULL, PRIMARY KEY(icon, svg_sha256))""")
            connection.execute("INSERT INTO reviews VALUES ('sub/square','abc','approve','old')")
        init_database(self.database)
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])['sub/square'], 'approve')
        self.assertEqual(self.request('POST', '/api/reviews',
                         {'icon': 'sub/square', 'svg_sha256': 'abc', 'status': 're-generated'})[0], 201)

    def test_review_validation(self):
        for payload, code in [({'icon': 'sub/square', 'svg_sha256': 'abc', 'status': 'unknown'}, 400),
                              ({'icon': 'missing', 'svg_sha256': 'abc', 'status': 'approve'}, 404),
                              ({'icon': 'sub/square', 'svg_sha256': 'abc', 'status': []}, 400)]:
            self.assertEqual(self.request('POST', '/api/reviews', payload)[0], code)
        self.assertEqual(self.request('POST', '/api/reviews', {},
            {'Content-Type': 'application/json', 'Origin': 'https://elsewhere.example'})[0], 403)

    def test_internal_feedback_feed_opens_without_a_key(self):
        self.assertEqual(self.request('GET', '/api/feedback-feed')[0], 200)
        self.assertFalse(self.database.with_name('generator-key.txt').exists())

    def test_generator_feed_lists_requests_with_identity_and_revision(self):
        self.assertEqual(json.loads(self.request('GET', '/api/feedback-feed')[1]), [])
        self.request('POST', '/api/feedback', {'icon': 'sub/square', 'feedback': 'Round corners', 'svg_sha256': 'abc'})
        self.request('POST', '/api/feedback', {'icon': 'sub/square', 'feedback': 'Keep the size', 'svg_sha256': 'abc'})
        code, data = self.request('GET', '/api/feedback-feed')
        rows = json.loads(data)
        self.assertEqual(code, 200)
        self.assertEqual([r['feedback'] for r in rows], ['Keep the size', 'Round corners'])
        self.assertEqual(rows[0]['icon'], 'sub/square')
        self.assertEqual(rows[0]['svg_sha256'], 'abc')
        self.assertIn('created_at', rows[0])

    def test_invalid_feedback_is_rejected(self):
        for data, expected in [([], 400), ({'icon': 'sub/square', 'feedback': ' '}, 400),
                               ({'icon': 'missing', 'feedback': 'change'}, 404),
                               ({'icon': 'sub/square', 'feedback': 'change', 'svg_sha256': 'stale'}, 409),
                               ({'icon': 'sub/square', 'feedback': 'x' * 10001}, 400)]:
            with self.subTest(data=str(data)[:80]):
                self.assertEqual(self.request('POST', '/api/feedback', data)[0], expected)
        self.assertEqual(self.request('POST', '/api/feedback', {}, {'Content-Type': 'application/json', 'Origin': 'https://elsewhere.example'})[0], 403)
        self.assertEqual(self.request('POST', '/api/feedback', {}, {'Content-Type': 'text/plain'})[0], 415)

    def test_private_files_and_directory_listings_are_not_served(self):
        (self.root / 'secret.json').write_text('{"private": true}')
        (self.dist / 'escape.json').symlink_to(self.root / 'secret.json')
        (self.dist / '.hidden.json').write_text('{}')
        for path in ['/../secret.json', '/%2e%2e/secret.json', '/escape.json', '/.hidden.json', '/sub32/', '/gallery/', '/data/feedback.sqlite3']:
            with self.subTest(path=path):
                self.assertEqual(self.request('GET', path)[0], 404)
        with self.assertRaises(ValueError):
            create_server(self.dist, self.dist / 'feedback.sqlite3', port=0)


if __name__ == '__main__':
    unittest.main()
