"""Rejected icons stay disabled until explicitly restored, preserving source/history."""
import json
from email.message import Message
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
import sqlite3
import shutil
import subprocess
import unittest

from icon_set.scripts.deploy import GalleryHandler, init_database
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
            self.assertEqual(self.request('POST', '/api/reviews', dict(payload, status=status))[0], 409)
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
        self.assertEqual(json.loads(self.request('GET', '/api/feedback-feed')[1])[0]['feedback'], 'Keep for reference')

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
            self.assertEqual(connection.execute('SELECT * FROM reviews').fetchone(),
                             ('sub/square', 'abc', 'approve', 'original-date'))
        self.assertEqual(self.request('POST', '/api/reviews',
                                    {'icon': 'sub/square', 'svg_sha256': 'abc', 'status': 'rejected'})[0], 201)


@unittest.skipUnless(shutil.which('node'), 'Node is needed for gallery behavior checks')
class RejectedGalleryTests(unittest.TestCase):
    def test_rejection_filters_and_brief_downloads(self):
        template = (Path(__file__).resolve().parents[1] / 'scripts/templates/gallery.html').read_text()
        functions = ['iconState', 'inSection', 'feedbackIconState', 'feedbackBriefFiles', 'syncInspector']
        code = '\n'.join(next(line for line in template.splitlines() if line.startswith('function ' + name + '('))
                         for name in functions)
        harness = """
const assert = require('node:assert/strict');
let reviews={'sub/rejected':'rejected','sub/approved':'approve'}, reviewsLoaded=true;
let section='icons',reviewFilter='',selected={key:'sub/rejected'};
const saving=new Set(), elements={};
const $=id=>elements[id]||(elements[id]={});
const regeneratedVariants=()=>[{}];
const buildChangeBrief=()=> 'brief';
""" + code + """
const rejected={key:'sub/rejected',family:'sub',icon_id:'rejected'};
const approved={key:'sub/approved',family:'sub',icon_id:'approved'};
assert.equal(inSection(rejected),false);
assert.equal(inSection(approved),true);
reviewFilter='rejected';assert.equal(inSection(rejected),true);
section='final';assert.equal(inSection(rejected),false);assert.equal(inSection(approved),true);
assert.equal(feedbackIconState(rejected),'rejected');
const files=feedbackBriefFiles([{id:1,icon:rejected.key},{id:2,icon:approved.key}],[rejected,approved]);
assert.equal(files.length,1);assert.match(files[0].name,/approved/);
syncInspector();assert.equal($('download').hidden,true);assert.equal($('fixPanel').hidden,true);
assert.equal($('restoreCombined').hidden,false);assert.equal($('approveDetail').disabled,true);
reviews[rejected.key]='ready';syncInspector();assert.equal($('download').hidden,false);
assert.equal($('fixPanel').hidden,false);assert.equal($('restoreCombined').hidden,true);
"""
        subprocess.run(['node', '-e', harness], check=True, capture_output=True, text=True)
        script = template.split('<script>', 1)[1].split('</script>', 1)[0]
        subprocess.run(['node', '--check'], input=script, check=True, capture_output=True, text=True)
