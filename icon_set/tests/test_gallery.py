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

from icon_set.scripts.gallery import add_creation_times, add_modification_times, remap_categories, stage_gallery, stage_preview, stage_review_facets
from icon_set.scripts.deploy import create_server, init_database


def manifest(root, family, folder, name):
    directory = root / folder
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'manifest.json').write_text(json.dumps({'icons': [
        {'family': family, 'icon_id': name, 'name': name, 'svg_sha256': 'abc'}
    ]}))
    (directory / (name + '.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')


class GalleryTests(unittest.TestCase):
    def test_review_facets_require_matching_revision_and_complete_measurements(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            staged, published, target = root / 'stage', root / 'published', root / 'gallery'
            target.mkdir()
            records = [{'key': 'solo/a', 'family': 'solo', 'icon_id': 'a', 'svg_sha256': 'current'}]
            relative = Path('qa/solo/a/metrics.json')
            metrics = {'svg_sha256': 'current', 'symmetry': {'axes': [
                {'axis': 'vertical', 'ink_symmetric': True, 'status': 'pass'},
                {'axis': 'horizontal', 'ink_symmetric': False, 'status': 'not_applicable'}]}}
            for directory, sha in [(staged, 'old'), (published, 'current')]:
                (directory / relative).parent.mkdir(parents=True)
                (directory / relative).write_text(json.dumps({**metrics, 'svg_sha256': sha}))
            stage_review_facets(records, staged, published, target)
            self.assertEqual(json.loads((target / 'review-facets.json').read_text()), {
                'solo/a': {'svg_sha256': 'current', 'axes': ['vertical']}})
            records[0]['svg_sha256'] = 'changed'
            stage_review_facets(records, staged, published, target)
            self.assertEqual(json.loads((target / 'review-facets.json').read_text()), {})

    def test_modification_tracks_content_but_not_checkout_timestamps(self):
        import os
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = 'icon_set/model/icons/solo/example.py'
            path = root / source
            path.parent.mkdir(parents=True)
            path.write_text('# original')
            row = {'key': 'solo/example', 'python_source': {'path': source}, 'svg_sha256': 'svg1'}
            history = type('History', (), {'stdout': '@200\n'+source+'\n@100\n'+source+'\n'})()
            clean = type('Diff', (), {'stdout': ''})()
            with patch('icon_set.scripts.gallery.REPO_ROOT', root), patch('icon_set.scripts.gallery.subprocess.run', side_effect=[history, clean]):
                add_modification_times([row], root / 'dist')
            self.assertEqual(row['modified_at'], '1970-01-01T00:03:20+00:00')
            catalog = root / 'dist/gallery/icons.json'
            catalog.parent.mkdir(parents=True)
            catalog.write_text(json.dumps({'icons': [row]}))
            os.utime(path, (500, 500))
            rebuilt = {'key': row['key'], 'python_source': row['python_source'], 'svg_sha256': 'svg1'}
            with patch('icon_set.scripts.gallery.REPO_ROOT', root), patch('icon_set.scripts.gallery.subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                add_modification_times([rebuilt], root / 'dist')
                self.assertEqual(rebuilt['modified_at'], row['modified_at'])
                rebuilt['svg_sha256'] = 'svg2'
                add_modification_times([rebuilt], root / 'dist')
                self.assertEqual(rebuilt['modified_at_source'], 'changed-svg-build')
                self.assertNotEqual(rebuilt['modified_at'], row['modified_at'])
                path.write_text('# edited')
                os.utime(path, (600, 600))
                add_modification_times([rebuilt], root / 'dist')
                self.assertEqual(rebuilt['modified_at'], '1970-01-01T00:10:00+00:00')

    def test_creation_dates_survive_rebuild_without_git(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = 'icon_set/model/icons/solo/example.py'
            (root / source).parent.mkdir(parents=True)
            (root / source).write_text('# source')
            row = {'key': 'solo/example', 'python_source': {'path': source}}
            history = type('History', (), {'stdout': '@200\n'+source+'\n@100\n'+source+'\n'})()
            with patch('icon_set.scripts.gallery.REPO_ROOT', root), patch('icon_set.scripts.gallery.subprocess.run', return_value=history):
                add_creation_times([row], root / 'dist')
            self.assertEqual(row['created_at'], '1970-01-01T00:01:40+00:00')
            catalog = root / 'dist/gallery/icons.json'
            catalog.parent.mkdir(parents=True)
            catalog.write_text(json.dumps({'icons': [row]}))
            rebuilt = {'key': row['key'], 'python_source': row['python_source']}
            with patch('icon_set.scripts.gallery.REPO_ROOT', root), patch('icon_set.scripts.gallery.subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                add_creation_times([rebuilt], root / 'dist')
            self.assertEqual(rebuilt['created_at'], row['created_at'])

    def test_preview_catalog_contains_full_library_with_only_public_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            row = {'icon_id': 'folder', 'name': 'Folder', 'family': 'solo',
                   'preview_url': '../solo48/folder.svg', 'primitives': ['large payload']}
            stage_preview(target, [row, dict(row, icon_id='unrelated')])
            icons = json.loads((target / 'preview-icons.json').read_text())['icons']
            self.assertEqual([i['icon_id'] for i in icons], ['folder', 'unrelated'])
            self.assertEqual(icons[0], {key: row.get(key, '') for key in
                                       ('icon_id', 'name', 'family', 'preview_url', 'category')})
            for asset in ('preview.html', 'preview.css', 'preview.js',
                          'preview-scene.html', 'preview-scene.css', 'preview-scene.js',
                          'preview-editor.js', 'preview-editor.css', 'preview-library.js', 'preview-more.js', 'preview-more.css'):
                self.assertTrue((target / asset).is_file())
            stage_preview(target, [])
            self.assertEqual(json.loads((target / 'preview-icons.json').read_text())['icons'], [])

    def test_categories_follow_source_identity_including_variants_and_failures(self):
        catalog = {'categories': {'animals': {}, 'pets': {}, 'clothes': {}}, 'rows': [
            {'models': ['bird'], 'category': 'animals'},
            {'models': ['failed-dog'], 'category': 'pets'},
            {'models': ['ambiguous'], 'category': 'animals'},
            {'models': ['ambiguous'], 'category': 'pets'},
        ]}
        rows = [
            {'icon_id': 'bird', 'category': 'animals/birds'},
            {'icon_id': 'bird-v2', 'variant_root': 'bird', 'category': 'nature/animals'},
            {'icon_id': 'failed-dog', 'build_failed': True, 'category': 'animals'},
            {'icon_id': 'robe', 'category': 'objects/clothing'},
            {'icon_id': 'circle', 'category': 'containers'},
            {'icon_id': 'plus', 'category': 'primitives/operator'},
            {'icon_id': 'ambiguous', 'category': 'nature/animals'},
        ]
        remap_categories(rows, catalog)
        self.assertEqual([r['category'] for r in rows], [
            'animals', 'animals', 'pets', 'clothes', 'containers',
            'primitives/operator', 'nature/animals',
        ])
        before = json.dumps(rows)
        remap_categories(rows, {'rows': [], 'categories': {}})
        self.assertEqual(json.dumps(rows), before)

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
            from icon_set.model import contracts
            laboratory = json.loads((gallery / 'laboratory.json').read_text())
            self.assertEqual(laboratory['profile'], contracts.icon_profile())
            self.assertEqual(laboratory['keyshapes'], contracts.keyshapes())
            for asset in ('icon-laboratory.html', 'icon-laboratory.css', 'icon-laboratory.js'):
                self.assertTrue((gallery / asset).is_file())
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
        # Every change needs a login; tests act as one reviewer unless they ask not to.
        self.cookie = None
        status, _ = self.request('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'}, anonymous=True)
        self.assertEqual(status, 200)

    def request(self, method, path, data=None, headers=None, anonymous=False):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        headers = dict(headers or {'Content-Type': 'application/json'})
        if self.cookie and not anonymous:
            headers['Cookie'] = self.cookie
        try:
            connection.request(method, path, body=json.dumps(data) if data is not None else None,
                               headers=headers)
            response = connection.getresponse()
            cookie = response.getheader('Set-Cookie')
            if cookie and path == '/api/auth/login' and response.status == 200:
                self.cookie = cookie.split(';', 1)[0]
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

    def test_static_icons_revalidate_but_api_is_never_cached(self):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        self.addCleanup(connection.close)
        connection.request('GET', '/sub32/square.svg')
        response = connection.getresponse()
        response.read()
        self.assertEqual(response.getheader('Cache-Control'), 'no-cache')
        modified = response.getheader('Last-Modified')
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        self.addCleanup(connection.close)
        connection.request('GET', '/sub32/square.svg', headers={'If-Modified-Since': modified})
        self.assertEqual(connection.getresponse().status, 304)
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        self.addCleanup(connection.close)
        connection.request('GET', '/api/reviews', headers={'Cookie': self.cookie})
        self.assertEqual(connection.getresponse().getheader('Cache-Control'), 'no-store')
        self.assertGreaterEqual(self.server.request_queue_size, 128)

    def test_review_states_persist_and_new_svg_requires_review(self):
        key = 'sub/square'
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'ready')
        for status in ('pending', 're-generated', 'approve', 'ready', 'approve'):
            self.assertEqual(self.request('POST', '/api/reviews',
                {'icon': key, 'svg_sha256': 'abc', 'status': status, 'reason': 'bad-stroke'})[0], 201)
            init_database(self.database)  # Startup migration preserves explicit choices.
            self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])[key], 'ready' if status == 're-generated' else status)
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

    def test_published_variant_is_ready_without_overriding_parent_disapproval(self):
        key = 'sub/square'
        self.request('POST', '/api/feedback',
                     {'icon': key, 'svg_sha256': 'abc', 'feedback': 'Round corners'})
        catalog = self.dist / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        data['icons'].append(dict(data['icons'][0], key='sub/square-v2',
                                  icon_id='square-v2', variant_of='square'))
        catalog.write_text(json.dumps(data))
        states = json.loads(self.request('GET', '/api/reviews')[1])
        self.assertEqual(states[key], 'pending')
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

    def test_validation_evidence_runs_qa_overlays_on_the_served_svg(self):
        svg = self.dist / 'sub32/square.svg'
        svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" '
                       'stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
                       '<path d="M6 6L26 6L26 26L6 26Z"/></svg>')
        code, body = self.request('GET', '/api/qa-evidence?icon=sub%2Fsquare')
        self.assertEqual(code, 200, body)
        data = json.loads(body)
        import hashlib
        self.assertEqual(data['svg_sha256'], hashlib.sha256(svg.read_bytes()).hexdigest())
        self.assertIsNone(data['library'])
        qa = data['qa_overlays']
        self.assertEqual(qa['script'], 'qa_overlays.py')
        self.assertFalse(qa['cached'])
        self.assertTrue(qa['distance']['distance_passed'])
        self.assertEqual(qa['distance']['lowest_distance'], 20.0)
        self.assertEqual(qa['holes']['negative_space_status'], 'pass')
        self.assertEqual(qa['holes']['hole_count'], 1)
        self.assertEqual(set(qa['images']), {'distance', 'holes'})
        for url in qa['images'].values():
            code, image = self.request('GET', url)
            self.assertEqual(code, 200)
            self.assertTrue(image.startswith(b'\x89PNG'))
        self.assertTrue(json.loads(self.request('GET', '/api/qa-evidence?icon=sub%2Fsquare')[1])['qa_overlays']['cached'])
        # Evidence is cached beside the database, never inside the served dist.
        self.assertTrue(any((self.database.parent / 'qa-evidence').rglob('*_distance_debug.png')))
        self.assertFalse(any(self.dist.rglob('*_debug.png')))
        self.assertEqual(self.request('GET', '/api/qa-evidence?icon=sub%2Fmissing')[0], 404)
        self.assertEqual(self.request('GET', '/api/qa-evidence/image?icon=sub%2Fsquare&kind=../x')[0], 404)

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
