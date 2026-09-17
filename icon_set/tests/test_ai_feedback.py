"""AI feedback jobs are revision-bound drafts with no library/review writes."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.generation import GenerationManager
from icon_set.scripts.review_icon import FeedbackReviewManager, run_review, validate_result
from icon_set.tests import test_gallery


class ReviewJobTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.runner = GenerationManager(self.root, self.root/'dist', self.root/'generation')
        self.manager = FeedbackReviewManager(self.runner, self.root/'reviews')
        self.document = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M4 4H28V28H4Z"/></svg>'
        self.record = dict(key='sub/square', icon_id='square', canvas_size=32, profile='SUB32', keyshape='SQUARE',
                           svg_sha256=hashlib.sha256(self.document.encode()).hexdigest())
        self.data = dict(icon=self.record['key'], svg_sha256=self.record['svg_sha256'])

    def start(self):
        with patch('icon_set.scripts.review_icon.shutil.which', return_value='/codex'), patch('threading.Thread.start'):
            return self.manager.start(self.data, self.record, self.document, 'jakes')

    def test_duplicate_reconnects_and_generation_shares_busy_state(self):
        row = self.start()
        self.assertEqual(self.start()['id'], row['id'])
        self.assertTrue(self.runner.busy)
        with self.assertRaises(ValueError):
            self.manager.start(self.data, self.record, self.document, 'other')
        with patch('icon_set.scripts.review_icon.run_review', return_value={'verdict': 'keep', 'feedback': 'Keep. No changes needed.'}):
            self.manager.run(row, self.record, self.document)
        saved = self.manager.read(row['id'])
        self.assertEqual(saved['status'], 'completed')
        self.assertEqual(saved['verdict'], 'keep')
        self.assertFalse(self.runner.busy)

    def test_stale_input_failure_and_restart_recovery(self):
        with self.assertRaises(ValueError):
            self.manager.start(dict(self.data, svg_sha256='old'), self.record, self.document, 'jakes')
        with self.assertRaises(ValueError):
            self.manager.start(self.data, self.record, self.document+' ', 'jakes')
        row = self.start()
        with patch('icon_set.scripts.review_icon.run_review', side_effect=ValueError('Timed out')):
            self.manager.run(row, self.record, self.document)
        self.assertFalse(self.runner.busy)
        self.assertEqual(self.manager.read(row['id'])['status'], 'failed')
        row = self.start()
        FeedbackReviewManager(self.runner, self.manager.storage)
        self.assertEqual(self.manager.read(row['id'])['status'], 'failed')
        for bad in ['../job', '', None]:
            with self.assertRaises(ValueError): self.manager.read(bad)

    def test_result_validation(self):
        for result in [{}, {'verdict': 'perfect', 'feedback': 'good'}, {'verdict': 'keep', 'feedback': ''},
                       {'verdict': 'repair', 'feedback': 'x'*6001}, []]:
            with self.assertRaises(ValueError): validate_result(result)

    def test_selected_image_read_only_runner_and_original_preserved(self):
        template = self.root/'icon_set/scripts/templates/review_icon_prompt.md'
        template.parent.mkdir(parents=True)
        template.write_text('Read skill; selected {{ICON_JSON}}')
        original = self.root/'original.py'; original.write_text('original')
        def snapshot(workspace):
            workspace.mkdir(parents=True)
            (workspace/'original.py').write_text(original.read_text())
            return {'original.py': hashlib.sha256(original.read_bytes()).hexdigest()}
        calls = []
        def command(args, workspace, log, timeout=1800):
            calls.append(args)
            if '--output-last-message' in args:
                Path(args[args.index('--output-last-message')+1]).write_text(json.dumps(
                    {'verdict': 'keep', 'feedback': 'Keep. No changes needed.'}))
        with patch.object(self.runner, 'snapshot', snapshot), patch.object(self.runner, 'command', command):
            result = run_review(self.runner, self.record, self.document, self.root/'result')
        self.assertEqual(result['verdict'], 'keep')
        cli = calls[-1]
        self.assertEqual(cli[cli.index('--sandbox')+1], 'read-only')
        self.assertTrue(any(arg.startswith('--image=') for arg in cli))
        self.assertEqual((self.root/'result/workspace/review-input/selected.svg').read_text(), self.document)
        self.assertEqual(original.read_text(), 'original')


class FeedbackAPITests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_authorization_revision_and_no_feedback_submission(self):
        payload = {'icon': 'sub/square', 'svg_sha256': 'abc'}
        reviews_before = json.loads(self.request('GET', '/api/reviews')[1])
        with patch('icon_set.scripts.review_icon.FeedbackReviewManager.start', side_effect=ValueError('test unavailable')) as start:
            self.assertEqual(self.request('POST', '/api/ai-feedback', payload, anonymous=True)[0], 400)
            self.assertEqual(start.call_args.args[-1], 'system')
        self.assertEqual(self.request('GET', '/api/ai-feedback?id='+'a'*32, anonymous=True)[0], 400)
        self.assertEqual(self.request('POST', '/api/ai-feedback', payload,
            {'Content-Type': 'application/json', 'Origin': 'https://elsewhere.test'})[0], 403)
        self.assertEqual(self.request('POST', '/api/ai-feedback', dict(payload, svg_sha256='old'))[0], 409)
        row = dict(id='a'*32, status='completed', icon='sub/square', svg_sha256='abc',
                   created_by='jakes', verdict='keep', feedback='Keep. No changes needed.')
        with patch.object(self.server.ai_feedback, 'start', return_value=row) as start:
            self.assertEqual(self.request('POST', '/api/ai-feedback', payload)[0], 202)
            self.assertEqual(start.call_args.args[2], (self.dist/'sub32/square.svg').read_text())
        self.server.ai_feedback.write(row)
        code, body = self.request('GET', '/api/ai-feedback?id='+row['id'])
        self.assertEqual(code, 200)
        self.assertEqual(json.loads(body)['feedback'], row['feedback'])
        self.assertEqual(json.loads(self.request('GET', '/api/feedback?icon=sub/square')[1]), [])
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1]), reviews_before)
        self.server.ai_feedback.write(dict(row, svg_sha256='previous'))
        result = json.loads(self.request('GET', '/api/ai-feedback?id='+row['id'])[1])
        self.assertEqual(result['status'], 'stale'); self.assertNotIn('feedback', result)
        self.server.ai_feedback.write(dict(row, created_by='other'))
        self.assertEqual(self.request('GET', '/api/ai-feedback?id='+row['id'])[0], 403)

    def test_uploaded_artwork_is_sent_instead_of_python(self):
        from icon_set.scripts.deploy import GalleryHandler
        record = dict(key='sub/square', svg_sha256='uploaded', artwork_source='use_upload')
        with patch.object(GalleryHandler, 'catalog_icon', return_value=record), \
             patch('icon_set.scripts.deploy.resolve_artwork', return_value={'svg': '<svg>uploaded</svg>'}), \
             patch.object(self.server.ai_feedback, 'start', return_value={'id': 'a'*32}) as start:
            self.assertEqual(self.request('POST', '/api/ai-feedback', {'icon': record['key'], 'svg_sha256': 'uploaded'})[0], 202)
            self.assertEqual(start.call_args.args[2], '<svg>uploaded</svg>')


if __name__ == '__main__':
    unittest.main()
