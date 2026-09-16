"""Persistence, version conflicts, and Python handoff for the stroke editor."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import http.client
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from icon_set.scripts.deploy import create_server
from icon_set.scripts.stroke_edits import StrokeEditStore, EditConflict, edited_graph, load_edit


def example():
    return {'key': 'sub/example', 'icon_id': 'example', 'family': 'sub', 'canvas_size': 32,
            'svg_sha256': 'version-a', 'style': {'stroke_width': 4},
            'primitives': [
                {'kind': 'line', 'element_id': 'a', 'start': [2, 2], 'end': [8, 2]},
                {'kind': 'arc', 'element_id': 'b', 'start': [8, 2], 'end': [12, 6],
                 'radius_x': 4, 'radius_y': 4, 'large_arc': False, 'sweep': True},
                {'kind': 'bezier', 'element_id': 'c', 'start': [2, 10], 'end': [12, 10],
                 'segments': [[[4, 8], [10, 8], [12, 10]]]}],
            'contours': [{'contour_id': 'outline', 'members': ['a', 'b'], 'closed': False}],
            'anchors': {'center': [16, 16]}, 'relationships': []}


class StrokeEditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = StrokeEditStore(self.root / 'edits')
        self.icon = example()
        self.data = {'svg_sha256': 'version-a', 'revision': 0, 'offsets': {'contour:outline': [3, -1], 'primitive:c': [.5, 2]}}

    def test_round_trip_translates_all_geometry_and_keeps_original(self):
        before = deepcopy(self.icon)
        row = self.store.save(self.icon, self.data, 'jakes')
        self.assertEqual(self.icon, before)
        primitives = row['edited_graph']['primitives']
        self.assertEqual(primitives[0]['start'], [5, 1])
        self.assertEqual(primitives[1]['end'], [15, 5])
        self.assertEqual(primitives[1]['radius_x'], 4)
        self.assertEqual(primitives[2]['segments'], [[[4.5, 10], [10.5, 10], [12.5, 12]]])
        self.assertEqual(row['validation']['status'], 'not-run')
        self.assertEqual(row['original_graph']['primitives'], before['primitives'])
        restarted = StrokeEditStore(self.store.root)
        self.assertEqual(restarted.get(self.icon['key'], 'version-a'), row)
        self.assertEqual(load_edit(self.store.path(self.icon['key'], 'version-a'), expected_svg_sha256='version-a'), row)
        with self.assertRaises(EditConflict):
            load_edit(self.store.path(self.icon['key'], 'version-a'), expected_svg_sha256='new')

    def test_resize_arc_and_bezier_and_read_legacy_edits(self):
        self.data['scales'] = {'contour:outline': [2, .5], 'primitive:c': [.5, 2]}
        row = self.store.save(self.icon, self.data, 'jakes')
        self.assertEqual(row['schema'], 'pictographic.stroke-edit.v2')
        a, b, c = row['edited_graph']['primitives']
        self.assertEqual(a['start'], [-9, 8])
        self.assertEqual([b['radius_x'], b['radius_y']], [8, 2])
        self.assertEqual(c['segments'], [[[10.5, 2], [13.5, 2], [14.5, 6]]])
        self.assertEqual(row['edited_graph']['style'], self.icon['style'])
        # A v1 client moving strokes must not wipe a previously saved resize.
        del self.data['scales']
        self.data['revision'] = 1
        moved = self.store.save(self.icon, self.data, 'hina')
        self.assertEqual(moved['scales'], row['scales'])
        for invalid in [None, [], {'missing': [2, 2]}, {'primitive:c': [0, 1]}, {'primitive:c': [1, 21]}, {'primitive:c': [True, 1]}]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.store.save(self.icon, dict(self.data, revision=2, scales=invalid), 'hina')
        legacy = dict(row, schema='pictographic.stroke-edit.v1')
        legacy.pop('scales')
        path = self.root / 'legacy.json'
        path.write_text(json.dumps(legacy))
        self.assertEqual(load_edit(path)['schema'], 'pictographic.stroke-edit.v1')

    def test_stale_writer_and_changed_icon_do_not_overwrite(self):
        def save():
            try:
                self.store.save(self.icon, self.data, 'jakes')
                return 'saved'
            except EditConflict:
                return 'conflict'
        with ThreadPoolExecutor(max_workers=2) as pool:
            self.assertCountEqual(list(pool.map(lambda _: save(), range(2))), ['saved', 'conflict'])
        self.icon['svg_sha256'] = 'version-b'
        with self.assertRaises(EditConflict):
            self.store.save(self.icon, self.data, 'jakes')
        self.assertIsNone(self.store.get(self.icon['key'], 'version-b'))
        self.assertEqual(len(self.store.previous_versions(self.icon['key'], 'version-b')), 1)
        self.data['svg_sha256'] = 'version-b'
        self.store.save(self.icon, self.data, 'jakes')
        self.assertEqual(self.store.get(self.icon['key'], 'version-a')['revision'], 1)

    def test_validation_reset_and_disk_failure(self):
        for invalid in [None, [], {'no-such-stroke': [1, 2]}, {'primitive:c': [True, 1]},
                        {'primitive:c': [float('nan'), 0]}, {'primitive:c': [float('inf'), 0]},
                        {'primitive:c': [1025, 0]}, {'primitive:c': [1]}]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                edited_graph(self.icon, invalid)
        row = self.store.save(self.icon, self.data, 'jakes')
        self.data.update(revision=1, offsets={})
        with patch('icon_set.scripts.stroke_edits.os.replace', side_effect=OSError('disk full')):
            with self.assertRaises(OSError):
                self.store.save(self.icon, self.data, 'jakes')
        self.assertEqual(self.store.get(self.icon['key'], 'version-a'), row)
        self.assertFalse(list(self.store.root.rglob('*.tmp')))
        reset = self.store.save(self.icon, self.data, 'hina')
        self.assertEqual(reset['edited_graph'], reset['original_graph'])
        self.assertEqual(reset['revision'], 2)


class StrokeEditAPITests(unittest.TestCase):
    def test_validation_endpoint_checks_unsaved_edits_without_writing(self):
        from icon_set.tests.test_edit_validation import portrait
        icon = portrait()
        (self.dist / 'gallery/icons.json').write_text(json.dumps({'icons': [icon]}))
        data = {'icon': icon['key'], 'svg_sha256': 'fixture', 'offsets': {}, 'keyshape': 'VRECT_M'}
        route = '/api/stroke-edits/validate'
        self.assertEqual(self.call('POST', route, data)[0], 401)
        self.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        self.assertEqual(self.call('POST', route, data, origin='https://foreign.example')[0], 403)
        status, report = self.call('POST', route, data)
        self.assertEqual(status, 200)
        self.assertEqual(report['status'], 'fail')
        self.assertFalse(list((self.database.parent / 'stroke-edits').rglob('*.json')))
        self.assertEqual(self.call('POST', route, data | {'svg_sha256': 'old'})[0], 409)
        self.assertEqual(self.call('POST', route, data | {'keyshape': 'FREE'})[0], 400)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.dist = self.root / 'dist'
        (self.dist / 'gallery').mkdir(parents=True)
        (self.dist / 'gallery/index.html').write_text('<!doctype html>')
        self.icon = example()
        (self.dist / 'gallery/icons.json').write_text(json.dumps({'icons': [self.icon]}))
        self.database = self.root / 'persistent/feedback.sqlite3'
        self.start()
        self.cookie = None

    def start(self):
        self.server = create_server(self.dist, self.database, port=0)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def call(self, method, path='/api/stroke-edits', data=None, origin=None):
        c = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        headers = {'Content-Type': 'application/json'}
        if self.cookie:
            headers['Cookie'] = self.cookie
        if origin:
            headers['Origin'] = origin
        c.request(method, path, json.dumps(data) if data is not None else None, headers)
        r = c.getresponse()
        if r.getheader('Set-Cookie'):
            self.cookie = r.getheader('Set-Cookie').split(';')[0]
        status, body = r.status, json.loads(r.read())
        c.close()
        return status, body

    def test_authenticated_round_trip_on_server_without_python_models(self):
        data = {'icon': 'sub/example', 'svg_sha256': 'version-a', 'revision': 0, 'offsets': {'primitive:c': [1, 0]}}
        self.assertEqual(self.call('POST', data=data)[0], 401)
        self.assertEqual(self.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})[0], 200)
        self.assertEqual(self.call('POST', data=data, origin='https://foreign.example')[0], 403)
        status, row = self.call('POST', data=data)
        self.assertEqual(status, 200)
        self.assertEqual(row['updated_by'], 'jakes')
        self.assertEqual(self.call('POST', data=data)[0], 409)
        self.assertEqual(self.call('GET', '/api/stroke-edits?icon=sub%2Fexample')[1]['edit'], row)
        files = list((self.database.parent / 'stroke-edits').rglob('*.json'))
        self.assertEqual(len(files), 1)
        self.assertEqual(load_edit(files[0]), row)
        self.server.shutdown(); self.server.server_close(); self.start()
        self.assertEqual(self.call('GET', '/api/stroke-edits?icon=sub%2Fexample')[1]['edit'], row)
        self.assertEqual(self.call('POST', data=dict(data, icon='../../escape'))[0], 404)
        self.assertEqual(self.call('GET', '/api/stroke-edits?icon=missing')[0], 404)
        self.assertFalse(list(self.dist.rglob('*stroke-edits*')))


if __name__ == '__main__':
    unittest.main()
