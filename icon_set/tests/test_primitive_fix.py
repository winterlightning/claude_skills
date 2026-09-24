"""primitive_fix: claim solo icons, keep the first version, upload before/after, report."""
from contextlib import closing
import http.client
import io
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts import primitive_fix, work_queue
from icon_set.tests.test_work_claims import ServerBase

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="12"/></svg>'


class FakeReport:
    def __init__(self, status='valid', warnings=()):
        self.status, self.errors, self.warnings = status, (), tuple(warnings)

    def describe(self):
        return f'status={self.status}; warnings={list(self.warnings)}'


class FakeIcon:
    def __init__(self, report):
        self.report = report

    def validate_icon(self):
        return self.report

    def to_svg(self):
        return SVG.replace('r="12"', 'r="10"')


class PrimitiveFixTests(ServerBase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'srv').mkdir()
        self.server, self.database = self.start(self.root / 'srv', production=True, family='solo', folder_name='solo48',
                                                names=('anchor', 'bell', 'cup'), canvas=48, svg=SVG)
        self.base = f'http://127.0.0.1:{self.server.server_port}'
        self.results = self.root / 'results'
        # A module the fixture icon points at, so start can copy it and finish can copy it back.
        self.module = Path(primitive_fix.REPO_ROOT) / 'icon_set' / 'work' / 'primitive-fix-thuan' / '.test-module.py'
        self.module.parent.mkdir(parents=True, exist_ok=True)
        self.module.write_text('AUTHOR = "before"\n', encoding='utf-8')
        self.addCleanup(lambda: self.module.unlink(missing_ok=True))
        # A /primitive-make-ray run holding the redrawn module, as the skill hands it to finish.
        self.uuid = '11111111-2222-3333-4444-555555555555'
        self.ray_run = Path(primitive_fix.REPO_ROOT) / 'icon_set' / 'work' / 'primitive-make-ray' / self.uuid / 'test-run'
        self.ray_run.mkdir(parents=True, exist_ok=True)
        (self.ray_run / 'attempt-01.py').write_text('x = 1\n', encoding='utf-8')
        (self.ray_run / f"anchor_{self.uuid.replace('-', '_')}.py").write_text('AUTHOR = "after"\n', encoding='utf-8')
        self.addCleanup(shutil.rmtree, self.ray_run.parent, True)
        cookie = self.login(self.server)
        for name, reason in (('anchor', 'bad-stroke'), ('bell', 'meaning'), ('cup', 'bad-stroke')):
            status, body, _ = self.request(self.server, 'POST', '/api/reviews', {
                'icon': 'solo/' + name, 'svg_sha256': 'abc', 'status': 'disapprove', 'reason': reason, 'feedback': 'Fix ' + name}, cookie)
            self.assertEqual(status, 201, body)

    def patch_catalog_source(self):
        """Give the fixture icons a python_source inside the repository."""
        relative = self.module.resolve().relative_to(primitive_fix.REPO_ROOT).as_posix()
        catalog = self.root / 'srv' / 'dist' / 'gallery' / 'icons.json'
        data = json.loads(catalog.read_text())
        for row in data['icons']:
            row['python_source'] = {'path': relative, 'family': 'solo', 'class_name': 'Icon'}
            row['original_sources'] = [{'source_path': f"todo/{row['icon_id']}_{self.uuid}.svg", 'url': 'originals/none.svg'}]
        catalog.write_text(json.dumps(data))

    def test_start_claims_records_first_version_and_uploads_before(self):
        self.patch_catalog_source()
        stdout = io.StringIO()
        with patch('sys.stdout', stdout):
            code = primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                       'start', '--limit', '2', '--offset', '1', '--disapprove-status', 'bad-stroke'])
        self.assertEqual(code, 0, stdout.getvalue())
        # bad-stroke icons are anchor and cup (oldest first); offset 1 skips anchor.
        self.assertIn('icon: solo/cup', stdout.getvalue())
        self.assertNotIn('icon: solo/anchor', stdout.getvalue())
        run = next((self.results / 'solo__cup').iterdir())
        self.assertTrue((run / 'brief.txt').is_file() and (run / 'claim.json').is_file())
        self.assertEqual((run / 'before' / '.test-module.py').read_text(), 'AUTHOR = "before"\n')
        self.assertIn('<svg', (run / 'before' / 'cup.svg').read_text())
        self.assertEqual(primitive_fix.reference_name({'original_sources': [{'source_path': f'todo/cup_{self.uuid}.svg'}]}),
                         f'cup_{self.uuid}.svg')
        self.assertIn('reference: ', stdout.getvalue())
        self.assertFalse((run / 'before-upload-error.txt').exists())
        history = self.request(self.server, 'GET', '/api/work/history?icon=solo/cup')[1]
        revision = history['revisions'][0]
        self.assertEqual(revision['claim']['worker'], 'thuan-mac')
        self.assertEqual(revision['results']['before']['has_python'], True)
        self.assertIsNone(self.request(self.server, 'GET', '/api/work?icon=solo/anchor')[1]['work']['state'])
        with patch('sys.stdout', io.StringIO()), patch('sys.stderr', io.StringIO()):
            code = primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                       'start', '--limit', '5', '--disapprove-status', 'other'])
        self.assertEqual(code, 3, 'nothing claimable for that reason')

    def test_finish_refuses_warnings_then_uploads_after_and_reports_done(self):
        self.patch_catalog_source()
        with patch('sys.stdout', io.StringIO()):
            self.assertEqual(primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                                 'start', '--limit', '1']), 0)
        run = next((self.results / 'solo__anchor').iterdir())
        (run / 'reference').mkdir(exist_ok=True)
        (run / 'reference' / f'anchor_{self.uuid}.svg').write_text(SVG, encoding='utf-8')
        with self.assertRaises(SystemExit):  # done needs the make-ray run
            primitive_fix.finish(self.base, 'thuan-mac', 'solo/anchor', 'done', 'x', self.results)
        warned = FakeIcon(FakeReport('valid', ['review: near-parallel edge']))
        with patch('sys.stderr', io.StringIO()) as err, patch.object(primitive_fix, 'load_icon', return_value=warned):
            code = primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                       'finish', '--icon', 'solo/anchor', '--run', str(self.ray_run),
                                       '--outcome', 'done', '--note', 'straightened'])
        self.assertEqual(code, 2)
        self.assertIn('refused', err.getvalue())
        self.assertFalse((run / 'result.json').exists())
        self.assertEqual(self.request(self.server, 'GET', '/api/work?icon=solo/anchor')[1]['work']['state'], 'working')
        self.assertEqual(self.request(self.server, 'GET', '/api/work/history?icon=solo/anchor')[1]['revisions'][0]['results'].get('after'), None)
        clean = FakeIcon(FakeReport('valid'))
        with patch('sys.stdout', io.StringIO()) as out, patch.object(primitive_fix, 'load_icon', return_value=clean), \
                patch.object(primitive_fix, 'render_previews', return_value=['preview-light-48.png']):
            code = primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                       'finish', '--icon', 'solo/anchor', '--run', str(self.ray_run),
                                       '--outcome', 'done', '--note', 'straightened'])
        self.assertEqual(code, 0, out.getvalue())
        result = json.loads((run / 'result.json').read_text())
        self.assertEqual((result['outcome'], result['validation_status'], result['review_status']), ('done', 'valid', 'ready'))
        module_name = f"anchor_{self.uuid.replace('-', '_')}.py"
        self.assertEqual((run / 'after' / module_name).read_text(), 'AUTHOR = "after"\n')
        self.assertEqual(result['module'].rsplit('/', 1)[-1], module_name)
        self.assertEqual(self.module.read_text(), 'AUTHOR = "before"\n', 'registered module untouched')
        self.assertIn('r="10"', (run / 'after' / 'anchor.svg').read_text())
        self.assertTrue((run / 'validation.txt').is_file())
        status, body, _ = self.request(self.server, 'GET', '/api/work?icon=solo/anchor')
        self.assertEqual((body['status'], body['work']['state']), ('ready', 'done'))
        revision = self.request(self.server, 'GET', '/api/work/history?icon=solo/anchor')[1]['revisions'][0]
        self.assertEqual(sorted(revision['results']), ['after', 'before'])
        self.assertEqual(revision['results']['after']['note'], 'straightened')
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        connection.request('GET', '/api/work/result?icon=solo/anchor&svg_sha256=abc&stage=after&part=python')
        response = connection.getresponse()
        self.assertEqual((response.status, response.read()), (200, b'AUTHOR = "after"\n'))
        connection.close()
        with closing(sqlite3.connect(self.database)) as db:
            actions = [row[0] for row in db.execute("SELECT action FROM activity_log WHERE icon='solo/anchor' AND action LIKE 'work_%' ORDER BY id")]
        self.assertEqual(actions, ['work_claim', 'work_result', 'work_result', 'work_done'])

    def test_finish_cannot_fix_needs_note_and_keeps_claim_row(self):
        self.patch_catalog_source()
        with patch('sys.stdout', io.StringIO()):
            primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results), 'start', '--limit', '1'])
        with self.assertRaises(SystemExit):
            primitive_fix.finish(self.base, 'thuan-mac', 'solo/anchor', 'cannot-fix', '', self.results)
        broken = FakeIcon(FakeReport('invalid'))
        with patch('sys.stdout', io.StringIO()), patch.object(primitive_fix, 'load_icon', return_value=broken), \
                patch.object(primitive_fix, 'render_previews', return_value=[]):
            code = primitive_fix.finish(self.base, 'thuan-mac', 'solo/anchor', 'cannot-fix', 'MIC 8 impossible', self.results)
        self.assertIsNone(json.loads(next((self.results / 'solo__anchor').iterdir()).joinpath('result.json').read_text())['make_ray_run'])
        self.assertEqual(code, 0)
        body = self.request(self.server, 'GET', '/api/work?icon=solo/anchor')[1]
        self.assertEqual((body['status'], body['work']['state'], body['work']['note']), ('disapprove', 'cannot-fix', 'MIC 8 impossible'))


class UploadRuleTests(ServerBase):
    def test_only_the_claim_owner_uploads_and_stages_follow_the_claim(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        server, _ = self.start(root, production=True, family='solo', folder_name='solo48', names=('anchor',), canvas=48, svg=SVG)
        cookie = self.login(server)
        self.request(server, 'POST', '/api/reviews', {'icon': 'solo/anchor', 'svg_sha256': 'abc', 'status': 'disapprove',
                                                       'reason': 'meaning', 'feedback': 'x'}, cookie)
        body = {'icon': 'solo/anchor', 'svg_sha256': 'abc', 'worker': 'thuan-mac', 'stage': 'before', 'svg': SVG}
        self.assertEqual(self.request(server, 'POST', '/api/work/result', body)[0], 409, 'no claim yet')
        self.assertEqual(self.request(server, 'POST', '/api/work/claim', {'icon': 'solo/anchor', 'svg_sha256': 'abc', 'worker': 'thuan-mac'})[0], 201)
        self.assertEqual(self.request(server, 'POST', '/api/work/result', dict(body, worker='mac-mini'))[0], 409, 'other worker')
        self.assertEqual(self.request(server, 'POST', '/api/work/result', dict(body, svg='<svg viewBox="0 0 32 32"/>'))[0], 400, 'wrong canvas')
        self.assertEqual(self.request(server, 'POST', '/api/work/result', dict(body, stage='later'))[0], 400)
        status, saved, _ = self.request(server, 'POST', '/api/work/result', dict(body, python_source='x = 1', python_path='icon_set/model/icons/solo/anchor.py'))
        self.assertEqual((status, saved['result']['stage'], saved['result']['has_python']), (200, 'before', True))
        self.assertEqual(self.request(server, 'POST', '/api/work/done', {'icon': 'solo/anchor', 'svg_sha256': 'abc', 'worker': 'thuan-mac'})[0], 200)
        self.assertEqual(self.request(server, 'POST', '/api/work/result', body)[0], 409, 'before is closed once done')
        self.assertEqual(self.request(server, 'POST', '/api/work/result', dict(body, stage='after'))[0], 200, 'after may follow done')
        listing = self.request(server, 'GET', '/api/work/review')[1]['items'][0]
        self.assertEqual(listing['work']['results'], ['after', 'before'])
        self.assertEqual(self.request(server, 'GET', '/api/work/result?icon=solo/anchor&svg_sha256=abc&stage=after&part=validation')[0], 404)


FIXED = SVG.replace('r="12"', 'r="9"')


class WorkFixDisplayTests(ServerBase):
    """An uploaded after SVG is what the gallery shows until the rebuilt Python model changes the revision."""

    @staticmethod
    def raw(server, path):
        connection = http.client.HTTPConnection('127.0.0.1', server.server_port)
        try:
            connection.request('GET', path)
            response = connection.getresponse()
            return response.status, response.read().decode('utf-8')
        finally:
            connection.close()

    def assert_fixed(self, response):
        status, text = response
        self.assertEqual(status, 200, text)
        self.assertIn('r="9"', text, 'the uploaded fix, as sanitised on upload')

    def fixed_server(self, root):
        server, _ = self.start(root, production=True, family='solo', folder_name='solo48', names=('anchor', 'bell'), canvas=48, svg=SVG)
        cookie = self.login(server)
        self.request(server, 'POST', '/api/reviews', {'icon': 'solo/anchor', 'svg_sha256': 'abc', 'status': 'disapprove',
                                                       'reason': 'bad-stroke', 'feedback': 'x'}, cookie)
        claim = {'icon': 'solo/anchor', 'svg_sha256': 'abc', 'worker': 'thuan-mac'}
        self.assertEqual(self.request(server, 'POST', '/api/work/claim', claim)[0], 201)
        self.assertEqual(self.request(server, 'POST', '/api/work/result', dict(claim, stage='after', svg=FIXED))[0], 200)
        self.assertEqual(self.request(server, 'POST', '/api/work/done', claim)[0], 200)
        return server

    def catalog(self, server):
        icons = self.request(server, 'GET', '/gallery/icons.json')[1]['icons']
        return {row['key']: row for row in icons}

    def test_production_shows_the_uploaded_fix_with_the_python_revision(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        server = self.fixed_server(Path(temp.name))
        rows = self.catalog(server)
        anchor, bell = rows['solo/anchor'], rows['solo/bell']
        self.assertEqual((anchor['artwork_source'], anchor['svg_sha256'], anchor['work_fix']['worker']), ('work_fix', 'abc', 'thuan-mac'))
        self.assertIn('/api/icon-artwork/svg?icon=solo%2Fanchor&v=abc-', anchor['preview_url'])
        self.assertNotIn('work_fix', bell)
        self.assert_fixed(self.raw(server, "/api/icon-artwork/svg?icon=solo/anchor"))
        self.assertEqual(self.request(server, 'GET', '/api/icon-artwork?icon=solo/anchor')[1]['source_mode'], 'use_org',
                         'a fix is not a saved artwork choice')
        self.assertEqual(self.request(server, 'GET', '/api/reviews')[1]['solo/anchor'], 'ready', 'the review status keeps its key')
        self.assertEqual(self.request(server, 'GET', '/api/work/review?state=done')[1]['total'], 1)
        self.assertEqual(self.request(server, 'GET', '/api/work/fixes')[1]['fixes'][0]['icon'], 'solo/anchor')
        # A rebuilt model is a new revision: the fix no longer applies and the Python drawing is shown.
        catalog = Path(temp.name) / 'dist' / 'gallery' / 'icons.json'
        data = json.loads(catalog.read_text())
        for row in data['icons']:
            row['svg_sha256'] = 'rebuilt'
        catalog.write_text(json.dumps(data))
        self.assertNotIn('work_fix', self.catalog(server)['solo/anchor'])

    def test_development_shows_production_fixes_and_survives_an_outage(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / 'prod').mkdir()
        (root / 'dev').mkdir()
        production = self.fixed_server(root / 'prod')
        development, _ = self.start(root / 'dev', production=False, sync_source=f'http://127.0.0.1:{production.server_port}',
                                    family='solo', folder_name='solo48', names=('anchor', 'bell'), canvas=48, svg=SVG)
        self.assertEqual(self.catalog(development)['solo/anchor']['artwork_source'], 'work_fix')
        self.assert_fixed(self.raw(development, "/api/icon-artwork/svg?icon=solo/anchor"))
        production.shutdown()
        production.server_close()
        development.fixes_cache = None
        self.assertEqual(self.catalog(development)['solo/anchor'].get('artwork_source', 'use_org'), 'use_org')

if __name__ == '__main__':
    unittest.main()
