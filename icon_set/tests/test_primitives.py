"""Primitives progress: catalog, TODO/SKIP store, server API and original artwork route."""
import http.client
import json
import os
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest
from contextlib import closing
from unittest.mock import patch

from icon_set.scripts import primitive_status as ps
from icon_set.scripts.deploy import create_server, init_database, record_activity
from icon_set.scripts.gallery import stage_gallery
from icon_set.scripts.primitives_catalog import (REPO_ROOT, build_catalog, conversion_warning, link, model_links,
                                                  primitives_root, scan)

U1 = '00000000-0000-4000-8000-000000000001'
U2 = '00000000-0000-4000-8000-000000000002'
U3 = '00000000-0000-4000-8000-000000000003'
U4 = '00000000-0000-4000-8000-000000000004'
ORIGINAL = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path d="M0 0L10 10"/></svg>'
BRIEF = {'combination_type': 'container', 'components': [
    {'name': 'Monitor frame', 'family': 'container', 'description': 'Empty monitor. Exclude the arrow.'},
    {'name': 'Upload arrow', 'family': 'sub', 'description': 'Upward arrow alone. Exclude the monitor.'}]}


def primitives_tree(root: Path) -> Path:
    files = {
        f'computers/monitor upload_{U1}.svg': ORIGINAL,
        f'_uncategorized_07/south west_{U2}.svg': ORIGINAL,
        f'video-games/batch-01/cat 1_{U3}.svg': ORIGINAL,
        f'tools/hammer_{U4}.svg': ORIGINAL,
        'tools/notes.txt': 'not artwork',
    }
    for relative, text in files.items():
        (root / relative).parent.mkdir(parents=True, exist_ok=True)
        (root / relative).write_text(text)
    (root / '_manifest.csv').write_text('id,old_concept,concept,categories,folder,file\n'
                                        f'"{U1}","monitor upload","Monitor with Upward Arrow","computers","computers","x.svg"\n')
    return root


def fake_links():
    return dict(by_id={U1: ['monitor-icon']}, by_reference_id={U3: ['cat-icon']},
                by_path={f'tools/hammer_{U4}.svg': [('hammer-icon', None)]}, by_reference_path={},
                anonymous={}, families={})


class CatalogTests(unittest.TestCase):
    def test_categories_batches_concepts_and_model_states(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = primitives_tree(Path(tmp))
            built = {'monitor-icon': {'key': 'solo/monitor-icon', 'preview_url': '../solo48/monitor-icon.svg'}}
            failed = {'cat-icon': {'key': 'solo/cat-icon', 'preview_url': '../failed/solo48/cat-icon.svg'}}
            catalog = build_catalog(root, built, failed, fake_links())
        rows = {row['uuid']: row for row in catalog['rows']}
        self.assertEqual(catalog['count'], 4)
        self.assertEqual((rows[U1]['category'], rows[U1]['concept'], rows[U1]['state']),
                         ('computers', 'Monitor with Upward Arrow', 'generated'))
        self.assertEqual(rows[U1]['generated'][0]['key'], 'solo/monitor-icon')
        self.assertEqual((rows[U2]['category'], rows[U2]['batch'], rows[U2]['state']), ('Uncategorized', '07', 'none'))
        self.assertEqual((rows[U3]['category'], rows[U3]['batch'], rows[U3]['state'], rows[U3]['match']),
                         ('video-games', 'batch-01', 'build_failed', 'declared source reuse'))
        self.assertEqual((rows[U4]['state'], rows[U4]['match']), ('model_only', 'source path'))
        self.assertEqual(rows[U2]['concept'], 'South West')
        self.assertEqual(catalog['categories']['Uncategorized'], {'total': 1, 'none': 1})

    def test_conversions_copy_is_flagged_and_root_resolution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'a').mkdir()
            (root / f'a/x_{U1}.svg').write_text('<svg viewBox="0 0 48 48"/>')
            self.assertIn('48u conversions', conversion_warning(root, scan(root)))
            with patch.dict(os.environ, {'PICTOGRAPHIC_PRIMITIVES': tmp}):
                self.assertEqual(primitives_root(), root.resolve())
        self.assertEqual(primitives_root('/x/y'), Path('/x/y').resolve())
        self.assertNotEqual(primitives_root().parent.name, 'claude_skills')

    @unittest.skipUnless(primitives_root().is_dir(), 'original primitives are not available')
    def test_indexed_links_match_category_report_rules_on_real_models(self):
        from icon_set.scripts.category_report import match_models, model_catalog
        models, links = model_catalog(), model_links()
        rows = scan(primitives_root())
        linked = [row for row in rows if link(row, links)[0]]
        sample = linked[::max(1, len(linked) // 150)] + rows[::max(1, len(rows) // 100)]
        copy = REPO_ROOT / 'pictographic-primitives'
        for row in sample:
            source = dict(source_id=row['uuid'], paths=[copy / row['path']], proposed_icon_id=row.get('proposed_icon_id'))
            expected = sorted({m['icon_id'] for m in match_models(source, models)[0]})
            with self.subTest(row=row['path']):
                self.assertEqual(link(row, links)[0], expected)


class StatusStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.database = Path(self.tmp.name) / 'feedback.sqlite3'
        init_database(self.database)

    def apply(self, *args, **kwargs):
        with closing(sqlite3.connect(self.database)) as connection, connection:
            return ps.set_status(connection, *args, user='agent', record=record_activity, **kwargs)

    def test_skip_todo_round_trip_is_idempotent_and_logged(self):
        self.assertEqual(self.apply([U1, U2, U1], 'skip', 'container')['changed'], 2)
        self.assertEqual(self.apply([U1], 'skip', 'container')['changed'], 0)
        self.assertEqual(self.apply([U1], 'skip', 'other', 'two subjects side by side')['changed'], 1)
        self.assertEqual(self.apply([U2, U3], 'todo')['changed'], 1)
        with closing(sqlite3.connect(self.database)) as connection:
            statuses = ps.load_status(connection)
            actions = [row[0] for row in connection.execute('SELECT action FROM activity_log ORDER BY id')]
        self.assertEqual(list(statuses), [U1])
        self.assertEqual((statuses[U1]['reason'], statuses[U1]['note'], statuses[U1]['updated_by']),
                         ('other', 'two subjects side by side', 'agent'))
        self.assertEqual(actions, ['primitive_skip', 'primitive_skip', 'primitive_skip', 'primitive_todo'])

    def test_validation(self):
        for args, kwargs in [(([U1], 'skip', 'other'), {}), (([U1], 'skip', 'logo'), {}), (([U1], 'done'), {}),
                             ((['nope'], 'skip', 'container'), {}), (([], 'todo'), {}),
                             (([U1] * 2 + [f'00000000-0000-4000-8000-{i:012d}' for i in range(600)], 'todo'), {}),
                             (([U4], 'skip', 'container'), {'known': {U1}})]:
            with self.subTest(args=args[1:], kwargs=kwargs), self.assertRaises(ValueError):
                self.apply(*args, **kwargs)

    def test_brief_migration_preservation_and_clear(self):
        with sqlite3.connect(':memory:') as db:
            db.execute('CREATE TABLE primitive_status(uuid TEXT PRIMARY KEY,status TEXT,reason TEXT,note TEXT,updated_by TEXT,updated_at TEXT)')
            db.execute("INSERT INTO primitive_status VALUES (?,'skip','container','old note','agent','today')", (U1,))
            ps.init_primitive_status(db)
            ps.init_primitive_status(db)
            self.assertEqual(ps.load_status(db)[U1]['note'], 'old note')
            self.assertIsNone(ps.load_status(db)[U1]['combination_brief'])
        self.assertEqual(self.apply([U1], 'skip', 'container', combination_brief=BRIEF)['changed'], 1)
        self.assertEqual(self.apply([U1], 'skip', 'container', combination_brief=BRIEF)['changed'], 0)
        self.apply([U1], 'skip', 'container', 'updated note')
        with sqlite3.connect(self.database) as db:
            self.assertEqual(ps.load_status(db)[U1]['combination_brief'], BRIEF)
        self.apply([U1], 'skip', 'container', combination_brief=None)
        with sqlite3.connect(self.database) as db:
            self.assertIsNone(ps.load_status(db)[U1]['combination_brief'])
        self.apply([U1], 'skip', 'container', combination_brief=BRIEF)
        self.apply([U1], 'todo')
        with sqlite3.connect(self.database) as db:
            self.assertNotIn(U1, ps.load_status(db))

    def test_invalid_brief_does_not_mutate_status(self):
        for brief in ({}, [], {'combination_type': 'side', 'components': []},
                      {**BRIEF, 'components': [BRIEF['components'][1], BRIEF['components'][0]]},
                      {**BRIEF, 'components': [{**BRIEF['components'][0], 'name': ' '}, BRIEF['components'][1]]}):
            with self.subTest(brief=brief), self.assertRaises(ValueError):
                self.apply([U1], 'skip', 'container', combination_brief=brief)
        for uuids, status, reason in (([U1,U2], 'skip', 'container'), ([U1], 'todo', None), ([U1], 'skip', 'text_number')):
            with self.assertRaises(ValueError):
                self.apply(uuids, status, reason, combination_brief=BRIEF)
        with sqlite3.connect(self.database) as db:
            self.assertEqual(ps.load_status(db), {})

    def test_independent_fields_preserve_other_component(self):
        main, sub = BRIEF['components']
        self.apply([U1], 'skip', 'container', main_brief=main)
        with sqlite3.connect(self.database) as db:
            self.assertEqual(ps.load_status(db)[U1]['main_brief'], main)
            self.assertIsNone(ps.load_status(db)[U1]['sub_brief'])
        self.apply([U1], 'skip', 'container', sub_brief=sub)
        self.apply([U1], 'skip', 'container', main_brief={**main, 'name': 'Edited main'})
        with sqlite3.connect(self.database) as db:
            self.assertEqual(ps.load_status(db)[U1]['sub_brief'], sub)
        self.apply([U1], 'skip', 'container', main_brief=None)
        with sqlite3.connect(self.database) as db:
            self.assertIsNone(ps.load_status(db)[U1]['main_brief'])
            self.assertEqual(ps.load_status(db)[U1]['sub_brief'], sub)
        with self.assertRaises(ValueError):
            self.apply([U1], 'skip', 'container', sub_brief=main)

    def test_side_position_preserves_briefs_and_clears_on_reason_change(self):
        main, sub = BRIEF['components']
        self.apply([U1], 'skip', 'combination', main_brief=main, sub_brief=sub, sub_position='bottom-right')
        self.apply([U1], 'skip', 'combination', 'updated note')
        with sqlite3.connect(self.database) as db:
            self.assertEqual(ps.load_status(db)[U1]['sub_position'], 'bottom-right')
        self.apply([U1], 'skip', 'combination', sub_position='top')
        with sqlite3.connect(self.database) as db:
            self.assertEqual(ps.load_status(db)[U1]['sub_brief'], sub)
            self.assertEqual(ps.load_status(db)[U1]['main_brief'], main)
        for position in ('diagonal', [], 5):
            with self.assertRaises(ValueError):
                self.apply([U1], 'skip', 'combination', sub_position=position)
        with self.assertRaises(ValueError):
            self.apply([U1], 'skip', 'container', sub_position='top')
        self.apply([U1], 'skip', 'container')
        with sqlite3.connect(self.database) as db:
            self.assertIsNone(ps.load_status(db)[U1]['sub_position'])

    def test_migrate_existing_paired_brief_to_separate_columns(self):
        with sqlite3.connect(self.database) as db:
            db.execute("INSERT INTO primitive_status(uuid,status,reason,note,updated_by,updated_at,combination_brief) VALUES (?,'skip','container','','agent','today',?)", (U1, json.dumps(BRIEF)))
            ps.init_primitive_status(db)
            ps.init_primitive_status(db)
            decision = ps.load_status(db)[U1]
            self.assertEqual(decision['main_brief'], BRIEF['components'][0])
            self.assertEqual(decision['sub_brief'], BRIEF['components'][1])
            self.assertIsNone(db.execute('SELECT combination_brief FROM primitive_status WHERE uuid=?', (U1,)).fetchone()[0])

    def test_generated_wins_and_reports_conflict(self):
        rows = [dict(uuid=U1, category='a', state='generated'), dict(uuid=U2, category='a', state='build_failed'),
                dict(uuid=U3, category='b', state='none')]
        decisions = {U1: {'reason': 'text_number'}, U2: {'reason': 'container'}}
        merged = ps.merge(rows, decisions)
        self.assertEqual([row['status'] for row in merged], ['generated', 'skip', 'todo'])
        summary = ps.summarize(merged)
        self.assertEqual(summary['categories']['a'], {'total': 2, 'generated': 1, 'build_failed': 1, 'conflict': 1,
                                                      'skip': 1, 'skip_container': 1})
        self.assertEqual(summary['overall']['todo'], 1)


class PrimitivesServerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.primitives = primitives_tree(root / 'primitives')
        (root / 'secret.svg').write_text(ORIGINAL)
        self.dist = root / 'dist'
        (self.dist / 'sub32').mkdir(parents=True)
        (self.dist / 'sub32/manifest.json').write_text(json.dumps({'icons': [
            {'family': 'sub', 'icon_id': 'square', 'name': 'square', 'svg_sha256': 'abc'}]}))
        (self.dist / 'sub32/square.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        with patch.dict(os.environ, {'PICTOGRAPHIC_PRIMITIVES': str(self.primitives)}):
            stage_gallery(self.dist, self.dist, ['sub32'])
        self.database = root / 'data/feedback.sqlite3'
        self.server = create_server(self.dist, self.database, port=0, primitives=self.primitives)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.cookie = None

    def request(self, method, path, data=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        headers = {'Content-Type': 'application/json'}
        if self.cookie:
            headers['Cookie'] = self.cookie
        try:
            connection.request(method, path, body=json.dumps(data) if data is not None else None, headers=headers)
            response = connection.getresponse()
            if path == '/api/auth/login' and response.status == 200:
                self.cookie = response.getheader('Set-Cookie').split(';', 1)[0]
            return response.status, response.read(), response
        finally:
            connection.close()

    def test_page_catalog_status_api_and_original_route(self):
        self.assertEqual(self.request('GET', '/gallery/primitives.html')[0], 200)
        catalog = json.loads(self.request('GET', '/gallery/primitives.json')[1])
        self.assertEqual(catalog['count'], 4)
        code, body, response = self.request('GET', '/primitives/computers/monitor%20upload_' + U1 + '.svg')
        self.assertEqual((code, body.decode()), (200, ORIGINAL))
        self.assertIn('sandbox', response.getheader('Content-Security-Policy'))
        for path in ['/primitives/../secret.svg', '/primitives/%2e%2e/secret.svg', '/primitives/tools/notes.txt',
                     '/primitives/_manifest.csv', '/primitives/', '/primitives/missing.svg']:
            with self.subTest(path=path):
                self.assertEqual(self.request('GET', path)[0], 404)

        change = {'uuids': [U2], 'status': 'skip', 'reason': 'text_number', 'note': 'letters only'}
        self.assertEqual(self.request('POST', '/api/primitives/status', change)[0], 401)
        self.assertEqual(self.request('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})[0], 200)
        self.assertEqual(self.request('POST', '/api/primitives/status', {**change, 'reason': 'other', 'note': ''})[0], 400)
        self.assertEqual(self.request('POST', '/api/primitives/status', {**change, 'uuids': ['00000000-0000-4000-8000-00000000abcd']})[0], 400)
        code, body, _ = self.request('POST', '/api/primitives/status', change)
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['decisions'][U2]['reason'], 'text_number')

        self.assertEqual(json.loads(self.request('GET', '/api/primitives/status')[1])[U2]['updated_by'], 'jakes')
        rows = json.loads(self.request('GET', '/api/primitives?category=Uncategorized&status=skip')[1])
        self.assertEqual([(row['uuid'], row['batch'], row['status']) for row in rows], [(U2, '07', 'skip')])
        summary = json.loads(self.request('GET', '/api/primitives/summary')[1])
        self.assertEqual((summary['overall']['total'], summary['overall']['skip'], summary['overall']['todo']), (4, 1, 3))

    def test_component_brief_api_round_trip(self):
        change = {'uuids': [U1], 'status': 'skip', 'reason': 'container', 'combination_brief': BRIEF}
        self.assertEqual(self.request('POST', '/api/primitives/status', change)[0], 401)
        self.request('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        self.assertEqual(self.request('POST', '/api/primitives/status', {**change, 'combination_brief': {}})[0], 400)
        code, body, _ = self.request('POST', '/api/primitives/status', change)
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['decisions'][U1]['combination_brief'], BRIEF)
        rows = json.loads(self.request('GET', '/api/primitives?category=computers&status=skip')[1])
        self.assertEqual(rows[0]['decision']['combination_brief'], BRIEF)
        independent = {k: v for k, v in change.items() if k != 'combination_brief'}
        updated_sub = {**BRIEF['components'][1], 'name': 'Separate arrow'}
        code, body, _ = self.request('POST', '/api/primitives/status', {**independent, 'sub_brief': updated_sub})
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['decisions'][U1]['main_brief'], BRIEF['components'][0])
        self.assertEqual(json.loads(body)['decisions'][U1]['sub_brief'], updated_sub)
        code, body, _ = self.request('POST', '/api/primitives/status', {**independent, 'reason': 'combination', 'sub_position': 'bottom-right'})
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['decisions'][U1]['sub_position'], 'bottom-right')
        self.assertEqual(json.loads(body)['decisions'][U1]['sub_brief'], updated_sub)
        self.request('POST', '/api/primitives/status', {**change, 'combination_brief': None})
        self.assertIsNone(json.loads(self.request('GET', '/api/primitives/status')[1])[U1]['combination_brief'])


if __name__ == '__main__':
    unittest.main()
