"""primitive_fix: claim solo icons, keep the first version, upload before/after, report."""
from contextlib import closing
import http.client
import io
import json
from pathlib import Path
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
        self.assertFalse((run / 'before-upload-error.txt').exists())
        history = self.request(self.server, 'GET', '/api/work/history?icon=solo/cup')[1]
        revision = history['revisions'][0]
        self.assertEqual(revision['claim']['worker'], 'thuan-mac')
        self.assertEqual(revision['results']['before']['has_python'], True)
        self.assertEqual(self.request(self.server, 'GET', '/api/work?icon=solo/anchor')[1]['work']['state'], 'open')
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
        self.module.write_text('AUTHOR = "after"\n', encoding='utf-8')
        warned = FakeIcon(FakeReport('valid', ['review: near-parallel edge']))
        with patch('sys.stderr', io.StringIO()) as err, patch.object(primitive_fix, 'load_icon', return_value=warned):
            code = primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                       'finish', '--icon', 'solo/anchor', '--outcome', 'done', '--note', 'straightened'])
        self.assertEqual(code, 2)
        self.assertIn('refused', err.getvalue())
        self.assertFalse((run / 'result.json').exists())
        self.assertEqual(self.request(self.server, 'GET', '/api/work?icon=solo/anchor')[1]['work']['state'], 'working')
        self.assertEqual(self.request(self.server, 'GET', '/api/work/history?icon=solo/anchor')[1]['revisions'][0]['results'].get('after'), None)
        clean = FakeIcon(FakeReport('valid'))
        with patch('sys.stdout', io.StringIO()) as out, patch.object(primitive_fix, 'load_icon', return_value=clean), \
                patch.object(primitive_fix, 'render_previews', return_value=['preview-light-48.png']):
            code = primitive_fix.main(['--base-url', self.base, '--worker', 'thuan-mac', '--results-root', str(self.results),
                                       'finish', '--icon', 'solo/anchor', '--outcome', 'done', '--note', 'straightened'])
        self.assertEqual(code, 0, out.getvalue())
        result = json.loads((run / 'result.json').read_text())
        self.assertEqual((result['outcome'], result['validation_status'], result['review_status']), ('done', 'valid', 'ready'))
        self.assertEqual((run / 'after' / '.test-module.py').read_text(), 'AUTHOR = "after"\n')
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


if __name__ == '__main__':
    unittest.main()
