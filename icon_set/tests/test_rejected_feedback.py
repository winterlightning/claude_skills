"""Rejected icons stay disabled until explicitly restored, preserving source/history."""
from contextlib import nullcontext
import json
from email.message import Message
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
import sqlite3
import shutil
import subprocess
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from icon_set.scripts.deploy import GalleryHandler, init_database
from icon_set.scripts.reference_images import ReferenceStore
from icon_set.scripts.gallery import stage_gallery
from icon_set.tests import test_gallery


class RejectedFeedbackTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.dist = self.root / 'dist'
        self.dist.mkdir()
        test_gallery.manifest(self.dist, 'sub', 'sub32', 'square')
        stage_gallery(self.dist, self.dist, ['sub32'])
        self.database = self.root / 'feedback.sqlite3'
        init_database(self.database)

    def request(self, method, path, data=None):
        # Exercise the actual HTTP route handlers without requiring a listening socket.
        handler = GalleryHandler.__new__(GalleryHandler)
        handler.root, handler.database = self.dist, self.database
        handler.server = SimpleNamespace(references=ReferenceStore(self.root / 'reference-images'), artwork=SimpleNamespace(get=lambda key: None, snapshot=nullcontext))
        handler.current_user = lambda: 'jakes'  # every change is made by a logged-in reviewer
        handler.path = path
        body = json.dumps(data).encode() if data is not None else b''
        handler.rfile = BytesIO(body)
        handler.headers = Message()
        handler.headers['Content-Type'] = 'application/json'
        handler.headers['Content-Length'] = str(len(body))
        responses = []
        handler.json_response = lambda payload, status=200: responses.append((status, json.dumps(payload).encode()))
        getattr(handler, 'do_' + method)()
        return responses[0]

    def test_reject_feedback_rebuild_and_restore(self):
        payload = {'icon': 'sub/square', 'svg_sha256': 'abc'}
        source = self.dist / 'sub32/square.svg'
        before = source.read_bytes()
        self.assertEqual(self.request('POST', '/api/reviews', dict(payload, status='rejected'))[0], 201)
        init_database(self.database)
        code, body = self.request('POST', '/api/feedback', dict(payload, feedback='Keep for reference'))
        self.assertEqual(code, 201)
        self.assertEqual(json.loads(body)['status'], 'rejected')
        for status in ('approve', 'pending', 'ready', 're-generated'):
            self.assertEqual(self.request('POST', '/api/reviews', dict(payload, status=status, reason='bad-stroke'))[0], 409)
        self.assertEqual(self.request('POST', '/api/generation', dict(payload, mode='fix'))[0], 409)
        catalog = self.dist / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        data['icons'][0]['svg_sha256'] = 'changed'
        data['icons'].append(dict(data['icons'][0], key='sub/square-v2', icon_id='square-v2', variant_of='square'))
        catalog.write_text(json.dumps(data))
        states = json.loads(self.request('GET', '/api/reviews')[1])
        self.assertEqual(states['sub/square'], 'rejected')
        self.assertEqual(states['sub/square-v2'], 'ready')
        self.assertEqual(self.request('POST', '/api/reject-combination/restore', payload)[0], 409)
        payload['svg_sha256'] = 'changed'
        self.assertEqual(self.request('POST', '/api/reject-combination/restore', payload)[0], 200)
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])['sub/square'], 'ready')
        self.assertEqual(self.request('POST', '/api/reviews', dict(payload, status='approve'))[0], 201)
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(json.loads(self.request('GET', '/api/feedback-feed')[1]), [])

    def test_discard_removes_model_files_and_rows_of_a_rejected_icon_only(self):
        source_root = self.root / 'repo'
        family = source_root / 'icon_set/model/icons/sub'
        family.mkdir(parents=True)
        model = family / 'square.py'
        model.write_text("from ._base import Sub32\n\nclass Square(Sub32):\n    icon_id = 'square'\n")
        catalog = self.dist / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        data['icons'][0]['python_source'] = {'path': 'icon_set/model/icons/sub/square.py', 'family': 'sub', 'class_name': 'Square'}
        catalog.write_text(json.dumps(data))
        payload = {'icon': 'sub/square', 'svg_sha256': 'abc'}
        # The handler resolves models under PACKAGE_ROOT.parent; point it at the fixture repo.
        self.enterContext(patch('icon_set.scripts.deploy.PACKAGE_ROOT', source_root / 'icon_set'))

        code, body = self.request('POST', '/api/icons/discard', payload)
        self.assertEqual(code, 409)
        self.assertIn('Only rejected icons', json.loads(body)['error'])
        self.assertTrue(model.exists())

        self.assertEqual(self.request('POST', '/api/feedback', dict(payload, feedback='Not needed'))[0], 201)
        self.assertEqual(self.request('POST', '/api/reviews', dict(payload, status='rejected'))[0], 201)
        # Another module importing the class blocks the discard without touching anything.
        (family / 'user.py').write_text('from .square import Square\n')
        code, body = self.request('POST', '/api/icons/discard', payload)
        self.assertEqual(code, 409)
        self.assertIn('imports Square', json.loads(body)['error'])
        self.assertTrue(model.exists())
        (family / 'user.py').unlink()

        code, body = self.request('POST', '/api/icons/discard', payload)
        self.assertEqual(code, 200, body)
        self.assertFalse(model.exists())
        self.assertFalse((self.dist / 'sub32/square.svg').exists())
        self.assertEqual(json.loads((self.dist / 'sub32/manifest.json').read_text())['icons'], [])
        self.assertEqual(json.loads(catalog.read_text())['icons'], [])
        with sqlite3.connect(self.database) as connection:
            for table in ('reviews', 'feedback', 'icon_flags'):
                self.assertEqual(connection.execute(f"SELECT COUNT(*) FROM {table} WHERE icon='sub/square'").fetchone()[0], 0)
            self.assertEqual(connection.execute("SELECT action FROM activity_log ORDER BY id DESC").fetchone()[0], 'discard')
        archived = list((self.root / 'discarded-icons').glob('*-sub-square.py'))
        self.assertEqual(len(archived), 1)
        self.assertIn("icon_id = 'square'", archived[0].read_text())
        self.assertEqual(self.request('POST', '/api/icons/discard', payload)[0], 404)

    def test_keep_side_sub_rejects_and_discards_the_alternative_everywhere(self):
        source_root = self.root / 'repo'
        pairs = {'rows': [{'id': 'a', 'subs': [{'icon': 'kept', 'family': 'sub'}, {'icon': 'square', 'family': 'sub'}]},
                          {'id': 'b', 'subs': [{'icon': 'square', 'family': 'sub'}, {'icon': 'kept', 'family': 'sub'}]}]}
        (source_root / 'icon_set/data').mkdir(parents=True)
        files = (source_root / 'icon_set/data/combination-pairs.json', self.dist / 'gallery/experiment-combination.json')
        for path in files:
            path.write_text(json.dumps(pairs))
        self.enterContext(patch('icon_set.scripts.deploy.PACKAGE_ROOT', source_root / 'icon_set'))
        calls = []

        def discard(icons, **kwargs):
            # Discard only runs once the alternative is recorded as rejected.
            calls.append([(i['key'], kwargs['connection'].execute(
                'SELECT status FROM reviews WHERE icon=? AND svg_sha256=?', (i['key'], i['svg_sha256'])).fetchone()[0]) for i in icons])
            return {'discarded': [{'icon': i['key'], 'source': 'x.py', 'archive': 'x'} for i in icons], 'failed': []}
        self.enterContext(patch('icon_set.scripts.deploy.discard_many', side_effect=discard))
        payload = {'pair_id': 'a', 'keep': 'sub/kept'}

        self.assertEqual(self.request('POST', '/api/combinations/side/keep-sub', dict(payload, keep='sub/other'))[0], 409)
        code, body = self.request('POST', '/api/combinations/side/keep-sub', dict(payload, dry_run=True))
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['remove'], [{'key': 'sub/square', 'icon': 'square', 'pairs': 2}])
        self.assertEqual(calls, [])
        self.assertEqual(json.loads(files[0].read_text()), pairs)

        code, body = self.request('POST', '/api/combinations/side/keep-sub', payload)
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(body)['removed'], ['sub/square'])
        self.assertEqual(calls, [[('sub/square', 'rejected')]])
        for path in files:
            self.assertEqual([[s['icon'] for s in r['subs']] for r in json.loads(path.read_text())['rows']], [['kept'], ['kept']])

    def test_failed_icon_can_be_discarded_without_rejecting_it(self):
        source_root = self.root / 'repo'
        family = source_root / 'icon_set/model/icons/sub'
        family.mkdir(parents=True)
        model = family / 'broken.py'
        model.write_text("from ._base import Sub32\nclass Broken(Sub32):\n    icon_id = 'broken'\n")
        catalog = self.dist / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        failed = dict(data['icons'][0], key='sub/broken', icon_id='broken', name='broken',
                      build_failed=True, preview_url='../failed/sub32/broken.svg',
                      python_source={'path': 'icon_set/model/icons/sub/broken.py', 'family': 'sub', 'class_name': 'Broken'})
        data['failed_icons'] = [failed]
        catalog.write_text(json.dumps(data))
        directory = self.dist / 'failed/sub32'
        directory.mkdir(parents=True)
        (directory/'broken.svg').write_text('<svg/>')
        (directory/'manifest.json').write_text(json.dumps({'icons':[failed], 'count':1}))
        self.enterContext(patch('icon_set.scripts.deploy.PACKAGE_ROOT', source_root/'icon_set'))
        self.assertEqual(self.request('POST', '/api/icons/discard', {'icon':'sub/broken', 'svg_sha256':'stale'})[0],409)
        self.assertTrue(model.exists())
        note = {'icon':'sub/broken','svg_sha256':'abc','feedback':'Widen the opening and straighten the tail.'}
        self.assertEqual(self.request('POST','/api/feedback',dict(note,svg_sha256='stale'))[0],409)
        self.assertEqual(self.request('POST','/api/feedback',note)[0],201)
        code, history = self.request('GET','/api/feedback?icon=sub%2Fbroken')
        self.assertEqual(code,200)
        self.assertEqual(json.loads(history)[0]['feedback'],note['feedback'])
        self.assertEqual(json.loads(self.request('GET','/api/reviews')[1])['sub/broken'],'pending')
        self.assertEqual(self.request('POST','/api/reviews',dict(note,status='approve'))[0],404)
        code, body = self.request('POST','/api/icons/discard',{'icon':'sub/broken','svg_sha256':'abc'})
        self.assertEqual(code,200,body)
        self.assertFalse(model.exists())
        self.assertFalse((directory/'broken.svg').exists())
        self.assertEqual(json.loads((directory/'manifest.json').read_text())['icons'],[])
        current = json.loads(catalog.read_text())
        self.assertEqual(current['failed_icons'],[])
        self.assertEqual(len(current['icons']),1)
        self.assertTrue(list((self.root/'discarded-icons').glob('*-sub-broken.py')))
        self.assertEqual(self.request('POST','/api/icons/discard',{'icon':'sub/broken','svg_sha256':'abc'})[0],404)

    def test_batch_discard_removes_eligible_icons_and_reports_the_rest(self):
        source_root = self.root / 'repo'
        family = source_root / 'icon_set/model/icons/sub'
        family.mkdir(parents=True)
        (family / 'shapes.py').write_text(
            "from ._base import Sub32\n\nclass Square(Sub32):\n    icon_id = 'square'\n\n\n"
            "class Circle(Sub32):\n    icon_id = 'circle'\n\n\nclass Dot(Sub32):\n    icon_id = 'dot'\n")
        (family / 'user.py').write_text('from .shapes import Dot\n')
        for name in ('circle', 'dot', 'kept'):
            (self.dist / f'sub32/{name}.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        manifest = self.dist / 'sub32/manifest.json'
        manifest.write_text(json.dumps({'icons': [{'family': 'sub', 'icon_id': name, 'name': name, 'svg_sha256': 'abc'}
                                                  for name in ('circle', 'dot', 'kept', 'square')]}))
        catalog = self.dist / 'gallery/icons.json'
        template = json.loads(catalog.read_text())['icons'][0]
        classes = {'square': 'Square', 'circle': 'Circle', 'dot': 'Dot', 'kept': 'Kept'}
        catalog.write_text(json.dumps({'icons': [dict(template, key=f'sub/{name}', icon_id=name, name=name,
                                                      preview_url=f'../sub32/{name}.svg',
                                                      python_source={'path': 'icon_set/model/icons/sub/shapes.py',
                                                                     'family': 'sub', 'class_name': cls})
                                                 for name, cls in classes.items()]}))
        self.enterContext(patch('icon_set.scripts.deploy.PACKAGE_ROOT', source_root / 'icon_set'))
        for name in ('square', 'circle', 'dot'):
            self.assertEqual(self.request('POST', '/api/reviews',
                                          {'icon': f'sub/{name}', 'svg_sha256': 'abc', 'status': 'rejected'})[0], 201)

        items = [{'icon': f'sub/{name}', 'svg_sha256': 'abc'} for name in ('square', 'circle', 'dot', 'kept')]
        code, body = self.request('POST', '/api/icons/discard', {'icons': items + [items[0]]})
        self.assertEqual(code, 200, body)
        result = json.loads(body)
        self.assertEqual(sorted(row['icon'] for row in result['discarded']), ['sub/circle', 'sub/square'])
        self.assertEqual({row['icon']: row['error'] for row in result['failed']}, {
            'sub/kept': 'Only rejected icons can be discarded. Reject it first.',
            'sub/dot': 'user.py imports Dot; update it before discarding.'})
        # Two classes left the shared module in one batch; the imported one stays.
        remaining = (family / 'shapes.py').read_text()
        self.assertNotIn('class Square', remaining)
        self.assertNotIn('class Circle', remaining)
        self.assertIn('class Dot', remaining)
        compile(remaining, 'shapes.py', 'exec')
        self.assertEqual([row['icon_id'] for row in json.loads(manifest.read_text())['icons']], ['dot', 'kept'])
        self.assertEqual([row['key'] for row in json.loads(catalog.read_text())['icons']], ['sub/dot', 'sub/kept'])
        self.assertFalse((self.dist / 'sub32/circle.svg').exists())
        self.assertTrue((self.dist / 'sub32/dot.svg').exists())
        self.assertEqual(self.request('POST', '/api/icons/discard', {'icons': []})[0], 400)

    def test_existing_four_status_database_migrates_without_data_loss(self):
        with sqlite3.connect(self.database) as connection:
            connection.execute('DROP TABLE reviews')
            connection.execute("""CREATE TABLE reviews (
                icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('ready','pending','re-generated','approve')),
                updated_at TEXT NOT NULL, PRIMARY KEY(icon,svg_sha256))""")
            connection.execute("INSERT INTO reviews VALUES ('sub/square','abc','approve','original-date')")
        init_database(self.database)
        init_database(self.database)
        with sqlite3.connect(self.database) as connection:
            self.assertEqual(connection.execute('SELECT icon, svg_sha256, status, updated_at FROM reviews').fetchone(),
                             ('sub/square', 'abc', 'approve', 'original-date'))
        self.assertEqual(self.request('POST', '/api/reviews',
                                    {'icon': 'sub/square', 'svg_sha256': 'abc', 'status': 'rejected'})[0], 201)


@unittest.skipUnless(shutil.which('node'), 'Node is needed for gallery behavior checks')
class RejectedGalleryTests(unittest.TestCase):
    def test_rejection_filters_and_brief_downloads(self):
        template = (Path(__file__).resolve().parents[1] / 'scripts/templates/gallery.html').read_text()
        functions = ['iconState', 'inSection', 'feedbackIconState', 'feedbackBriefFiles', 'syncInspector',
                     'discardMode', 'selectable']
        code = '\n'.join(next(line for line in template.splitlines() if line.startswith('function ' + name + '('))
                         for name in functions)
        harness = """
const assert = require('node:assert/strict');
let reviews={'sub/rejected':'rejected','sub/approved':'approve'}, reviewsLoaded=true;
let section='icons',reviewFilter='',selected={key:'sub/rejected'};
const saving=new Set(), elements={};
const $=id=>elements[id]||(elements[id]={setAttribute(){}});
let pendingStatusKey=null;function updatePendingReason(){}
const regeneratedVariants=()=>[{}];
const buildChangeBrief=()=> 'brief';
""" + code + """
const rejected={key:'sub/rejected',family:'sub',icon_id:'rejected'};
const approved={key:'sub/approved',family:'sub',icon_id:'approved',author:'gpt-6'};
assert.equal(inSection(rejected),false);
assert.equal(inSection(approved),true);
assert.equal(selectable(approved),true);assert.equal(selectable(rejected),false);
reviewFilter='rejected';assert.equal(inSection(rejected),true);
assert.equal(selectable(rejected),true);assert.equal(selectable(approved),false);
section='final';reviewFilter='';assert.equal(inSection(rejected),false);assert.equal(inSection(approved),true);
assert.equal(feedbackIconState(rejected),'rejected');
const files=feedbackBriefFiles([{id:1,icon:rejected.key},{id:2,icon:approved.key}],[rejected,approved]);
assert.equal(files.length,0);
reviews[approved.key]='pending';
assert.equal(feedbackBriefFiles([{id:2,icon:approved.key}],[approved]).length,1);
syncInspector();assert.equal($('download').hidden,true);assert.equal($('fixPanel').hidden,true);
assert.equal($('restoreCombined').hidden,false);assert.equal($('approveDetail').disabled,true);
assert.equal($('discardIcon').hidden,false);
reviews[rejected.key]='ready';syncInspector();assert.equal($('download').hidden,false);
assert.equal($('fixPanel').hidden,false);assert.equal($('restoreCombined').hidden,true);
assert.equal($('discardIcon').hidden,true);
"""
        subprocess.run(['node', '-e', harness], check=True, capture_output=True, text=True)
        script = template.split('<script>', 1)[1].split('</script>', 1)[0]
        subprocess.run(['node', '--check'], input=script, check=True, capture_output=True, text=True)
