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
                                                  primitives_root, scan, work_runs)

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
            catalog = build_catalog(root, built, failed, fake_links(), work={})
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

    def test_folder_only_runs_count_as_drawn(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = primitives_tree(Path(tmp) / 'primitives')
            work = Path(tmp) / 'work'
            for run, status in (('20260923T01', 'invalid'), ('20260923T02', 'review')):
                (work / 'primitive-make-ray' / U2 / run).mkdir(parents=True)
                (work / 'primitive-make-ray' / U2 / run / 'result.json').write_text(json.dumps(
                    {'source_uuid': U2, 'validation_status': status}))
                os.utime(work / 'primitive-make-ray' / U2 / run / 'result.json', (1, 1 if run.endswith('01') else 2))
            (work / 'side-main-make-thuan' / U1 / 'r').mkdir(parents=True)  # generated wins over a work run
            (work / 'side-main-make-thuan' / U1 / 'r' / 'result.json').write_text(json.dumps({'validation_status': 'valid'}))
            (work / 'primitive-make-ray' / U3 / 'empty').mkdir(parents=True)  # no result.json: not a run
            runs = work_runs(work)
            self.assertEqual(set(runs), {U1, U2})
            self.assertEqual(runs[U2], {'skill': 'primitive-make-ray', 'runs': 2,
                                        'run': f'primitive-make-ray/{U2}/20260923T02', 'status': 'review'})
            built = {'monitor-icon': {'key': 'solo/monitor-icon', 'preview_url': '../solo48/monitor-icon.svg'}}
            catalog = build_catalog(root, built, {}, fake_links(), work=runs)
        rows = {row['uuid']: row for row in catalog['rows']}
        self.assertEqual((rows[U2]['state'], rows[U2]['work']['status']), ('work_only', 'review'))
        self.assertEqual(rows[U1]['state'], 'generated')
        self.assertNotIn('work', rows[U1])
        self.assertEqual(catalog['categories']['Uncategorized'], {'total': 1, 'work_only': 1})
        self.assertEqual(ps.effective(rows[U2], None), 'drawn')

    def test_conversions_copy_is_flagged_and_root_resolution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'a').mkdir()
            (root / f'a/x_{U1}.svg').write_text('<svg viewBox="0 0 48 48"/>')
            self.assertIn('48u conversions', conversion_warning(root, scan(root)))
            with patch.dict(os.environ, {'PICTOGRAPHIC_PRIMITIVES': tmp}):
                self.assertEqual(primitives_root(), root.resolve())
        self.assertEqual(primitives_root('/x/y'), Path('/x/y').resolve())
        self.assertEqual(primitives_root(), (REPO_ROOT / 'pictographic-primitives').resolve())

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

    def test_existing_drawings_are_not_todo(self):
        from icon_set.scripts.primitive_status import effective
        self.assertEqual(effective({'state': 'model_only'}, None), 'drawn')
        self.assertEqual(effective({'state': 'build_failed'}, None), 'drawn')
        self.assertEqual(effective({'state': 'work_only'}, None), 'drawn')
        self.assertEqual(effective({'state': 'none', 'models': ['existing']}, None), 'drawn')
        self.assertEqual(effective({'state': 'none'}, None), 'todo')
        self.assertEqual(effective({'state': 'model_only'}, {'reason': 'container'}), 'skip')

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
        self.assertEqual(self.request('POST', '/api/primitives/status', change)[0], 200)
        self.assertEqual(self.request('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})[0], 200)
        self.assertEqual(self.request('POST', '/api/primitives/status', {**change, 'reason': 'other', 'note': ''})[0], 400)
        self.assertEqual(self.request('POST', '/api/primitives/status', {**change, 'uuids': ['00000000-0000-4000-8000-00000000abcd']})[0], 400)
        code, body, _ = self.request('POST', '/api/primitives/status', change)
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['decisions'][U2]['reason'], 'text_number')

        self.assertEqual(json.loads(self.request('GET', '/api/primitives/status')[1])[U2]['updated_by'], 'system')
        rows = json.loads(self.request('GET', '/api/primitives?category=Uncategorized&status=skip')[1])
        self.assertEqual([(row['uuid'], row['batch'], row['status']) for row in rows], [(U2, '07', 'skip')])
        summary = json.loads(self.request('GET', '/api/primitives/summary')[1])
        self.assertEqual((summary['overall']['total'], summary['overall']['skip'], summary['overall']['todo']), (4, 1, 3))

    def test_make_ray_prompt_api_lists_todo_reference_files(self):
        code, body, response = self.request('GET', '/api/primitives/prompt?category=Uncategorized')
        self.assertEqual(code, 200, body)
        self.assertIn('text/plain', response.getheader('Content-Type'))
        self.assertEqual(body.decode().splitlines(), [
            'Run $primitive-make-ray draw each of these 1 reference files in order. (tp:Uncategorized)',
            '  Most of these already have a primitive-make-ray run that failed validation. Do not skip a file '
            'because a result.json exists: author a fresh run in a new RESULT_DIR for every file, unless its '
            'newest existing run is already valid, in which case report it as done and move on.',
            f'  icon_set/work/todo-references/south west_{U2}.svg'])
        result = json.loads(self.request('GET', '/api/primitives/prompt?category=tools&count=1&format=json')[1])
        self.assertEqual((result['category'], result['count'], result['todo_total'], result['remaining']), ('tools', 1, 1, 0))
        self.assertEqual(result['files'], [f'icon_set/work/todo-references/hammer_{U4}.svg'])
        self.assertEqual(result['icons'][0]['uuid'], U4)
        paged = json.loads(self.request('GET', '/api/primitives/prompt?count=2&offset=1&format=json')[1])
        self.assertEqual((paged['category'], paged['count'], paged['todo_total'], paged['remaining']), ('all', 2, 4, 1))
        self.request('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        self.request('POST', '/api/primitives/status', {'uuids': [U2], 'status': 'skip', 'reason': 'text_number', 'note': 'x'})
        skipped = json.loads(self.request('GET', '/api/primitives/prompt?category=Uncategorized&format=json')[1])
        self.assertEqual((skipped['count'], skipped['todo_total'], skipped['files']), (0, 0, []))
        for query in ('count=0', 'count=101', 'offset=-1', 'count=many'):
            with self.subTest(query=query):
                self.assertEqual(self.request('GET', '/api/primitives/prompt?' + query)[0], 400)

    def test_reference_brief_round_trip_preserves_status(self):
        change = {'uuid': U1, 'family': 'solo', 'brief': 'Concept: Monitor\nDescription: A monitor viewed from the front.'}
        self.assertEqual(self.request('POST', '/api/primitives/briefs', change)[0], 200)
        self.request('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        before = json.loads(self.request('GET', '/api/primitives/summary')[1])
        code, body, _ = self.request('POST', '/api/primitives/briefs', change)
        self.assertEqual(code, 200, body)
        saved = json.loads(body)
        self.assertEqual(saved['brief'], change['brief'])
        self.assertEqual(saved['updated_by'], 'system')
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/briefs')[1])[U1], saved)
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/summary')[1]), before)
        for patch_data in ({'family': ''}, {'family': 'invalid'}, {'brief': ' '}, {'brief': 'x' * 20001},
                           {'uuid': 'unknown'}, {'brief': {'description': 'not text'}}):
            with self.subTest(patch_data=str(patch_data)[:100]):
                self.assertEqual(self.request('POST', '/api/primitives/briefs', {**change, **patch_data})[0], 400)
                self.assertEqual(json.loads(self.request('GET', '/api/primitives/briefs')[1])[U1], saved)
        self.request('POST', '/api/primitives/status', {'uuids': [U1], 'status': 'skip', 'reason': 'container'})
        self.request('POST', '/api/primitives/status', {'uuids': [U1], 'status': 'todo'})
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/briefs')[1])[U1], saved)
        updated = {**change, 'family': 'avatar', 'brief': 'Updated brief'}
        self.assertEqual(self.request('POST', '/api/primitives/briefs', updated)[0], 200)
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/briefs')[1])[U1]['brief'], 'Updated brief')
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/briefs')[1])[U1]['family'], 'avatar')

    def test_component_brief_api_round_trip(self):
        change = {'uuids': [U1], 'status': 'skip', 'reason': 'container', 'combination_brief': BRIEF}
        self.assertEqual(self.request('POST', '/api/primitives/status', change)[0], 200)
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


class GenerationQueueServerTests(unittest.TestCase):
    request = PrimitivesServerTests.request
    def setUp(self):
        # Build only the API fixture; unrelated galleries need live workspace datasets.
        def stage_fixture(staged, published, folders):
            target = staged / 'gallery'
            target.mkdir()
            (target / 'index.html').write_text('<html></html>')
            (target / 'icons.json').write_text('[]')
            catalog = build_catalog(self.primitives, {}, {},
                                    dict(by_id={}, by_reference_id={}, by_path={},
                                         by_reference_path={}, anonymous={}, families={}))
            (target / 'primitives.json').write_text(json.dumps(catalog))
        with patch(__name__ + '.stage_gallery', side_effect=stage_fixture):
            PrimitivesServerTests.setUp(self)

    def test_generation_queue_excludes_existing_drawings(self):
        from icon_set.scripts.primitive_briefs import generation_queue
        rows = [dict(uuid=str(i), path=f'{i}.svg', category='x', batch='',
                     state=state, models=models)
                for i, (state, models) in enumerate([
                    ('generated', []), ('model_only', []), ('build_failed', []),
                    ('none', ['existing']), ('none', []), ('none', []), ('work_only', [])])]
        result = generation_queue({'rows': rows}, {'5': {'reason': 'other'}}, {}, {})
        self.assertEqual([item['uuid'] for item in result['briefs']], ['4'])
        item = result['briefs'][0]
        self.assertEqual(item['skill'], 'icon-solo-distilled')
        self.assertIn('$icon-solo-distilled', item['brief'])
        self.assertIn('icon_set/skills/icon-design-distilled/', item['brief'])
        original = 'Run $icon-solo. Read icon_set/skills/icon-design/intake.md. Keep $icon-solo-distilled.'
        saved = {'4': {'family': 'solo', 'brief': original}}
        item = generation_queue({'rows': rows}, {}, saved, {'brief': ['ready']})['briefs'][0]
        self.assertIn('Run $icon-solo-distilled.', item['brief'])
        self.assertNotIn('distilled-distilled', item['brief'])
        self.assertEqual(saved['4']['brief'], original)

    def test_generation_queue_templates_filters_and_saved_briefs(self):
        code, body, _ = self.request('GET', '/api/primitives/generation-queue?category=Uncategorized&family=sub')
        self.assertEqual(code, 200)
        data = json.loads(body)
        self.assertEqual(data['total'], 1)
        item = data['briefs'][0]
        self.assertEqual(item['uuid'], U2)
        self.assertEqual(item['brief_source'], 'template')
        self.assertIn('$icon-sub', item['brief'])
        self.assertIn(U2, item['brief'])
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/briefs')[1]), {})
        self.request('POST', '/api/primitives/briefs', {'uuid': U2, 'family': 'solo', 'brief': 'Keep editorial instructions.'})
        data = json.loads(self.request('GET', '/api/primitives/generation-queue?brief=ready&family=sub')[1])
        self.assertEqual([r['uuid'] for r in data['briefs']], [U2])
        self.assertTrue(data['briefs'][0]['brief'].endswith('Keep editorial instructions.'))
        self.assertTrue(data['briefs'][0]['classification_decision']['authoritative'])
        self.assertEqual(data['briefs'][0]['family'], 'solo')
        data = json.loads(self.request('GET', '/api/primitives/generation-queue?category=Uncategorized&brief=missing')[1])
        self.assertEqual(data['total'], 0)
        self.request('POST', '/api/primitives/status', {'uuids': [U2], 'status': 'skip', 'reason': 'container'})
        self.assertEqual(json.loads(self.request('GET', '/api/primitives/generation-queue?brief=ready')[1])['total'], 0)
        data = json.loads(self.request('GET', '/api/primitives/generation-queue?limit=1')[1])
        self.assertEqual(len(data['briefs']), 1)
        self.assertEqual(data['next_offset'], 1)
        data = json.loads(self.request('GET', '/api/primitives/generation-queue?q=hammer')[1])
        self.assertEqual([r['uuid'] for r in data['briefs']], [U4])
        for query in ['limit=0', 'limit=501', 'offset=-1', 'offset=no', 'family=bad', 'brief=bad']:
            self.assertEqual(self.request('GET', '/api/primitives/generation-queue?' + query)[0], 400)

    def test_queue_includes_authenticated_reclassification_history(self):
        self.request('POST', '/api/primitives/status', {'uuids': [U2], 'status': 'skip', 'reason': 'combination', 'note': 'Previous split'})
        self.request('POST', '/api/primitives/status', {'uuids': [U2], 'status': 'todo'})
        result = json.loads(self.request('GET', '/api/primitives/generation-queue?family=solo')[1])
        item = next(r for r in result['briefs'] if r['uuid'] == U2)
        event = item['classification_history'][-1]
        self.assertEqual((event['from'], event['to']), ('combination', 'todo'))
        self.assertEqual(event['authority'], 'user')
        self.assertTrue(event['user'])
        self.assertEqual(event['previous_note'], 'Previous split')
        self.assertTrue(item['classification_decision']['authoritative'])
        self.assertIn('Do not judge the classification again', item['brief'])
        self.assertNotIn('## Reference triage', item['brief'])
