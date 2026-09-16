"""Rejecting a combination creates two durable standalone generation briefs."""
import json
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.tests import test_gallery as gallery_tests
from icon_set.scripts.brief_queue import init_brief_queue, list_briefs
from icon_set.scripts import queue_brief


class SplitWorkflowTests(unittest.TestCase):
    setUp = gallery_tests.ServerTests.setUp
    request = gallery_tests.ServerTests.request

    def payload(self):
        return {'icon': 'sub/square', 'svg_sha256': 'abc', 'combination_type': 'side',
                'reason': 'A separate subject and modifier.', 'components': [
                    {'name': 'Document', 'family': 'solo', 'description': 'The document alone.'},
                    {'name': 'Plus', 'family': 'sub', 'description': 'The plus alone.'}]}

    def test_reject_queues_exactly_two_and_blocks_approval(self):
        self.assertEqual(self.request('POST', '/api/reject-combination', self.payload())[0], 201)
        self.assertEqual(self.request('POST', '/api/reject-combination', self.payload())[0], 201)
        rows = json.loads(self.request('GET', '/api/pending-briefs')[1])
        self.assertEqual([r['name'] for r in rows], ['Document', 'Plus'])
        self.assertEqual([r['status'] for r in rows], ['pending', 'pending'])
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])['sub/square'], 'rejected')
        self.assertEqual(self.request('POST', '/api/reviews', {'icon': 'sub/square', 'svg_sha256': 'abc', 'status': 'approve'})[0], 409)
        with sqlite3.connect(self.database) as connection:
            init_brief_queue(connection)
            self.assertEqual(len(list_briefs(connection)), 2)

    def test_generated_component_link_and_restore(self):
        self.request('POST', '/api/reject-combination', self.payload())
        rows = json.loads(self.request('GET', '/api/pending-briefs')[1])
        path = self.dist/'gallery/icons.json'
        data = json.loads(path.read_text())
        data['icons'].append({'key': 'solo/document', 'icon_id': 'document', 'family': 'solo', 'svg_sha256': 'generated'})
        path.write_text(json.dumps(data))
        endpoint = '/api/pending-briefs/complete'
        self.assertEqual(self.request('POST', endpoint, {'brief_id': rows[0]['id'], 'generated_icon': 'sub/square'})[0], 400)
        self.assertEqual(self.request('POST', endpoint, {'brief_id': rows[0]['id'], 'generated_icon': 'solo/document'})[0], 200)
        self.assertEqual(json.loads(self.request('GET', '/api/pending-briefs')[1])[0]['status'], 'generated')
        self.assertEqual(self.request('POST', '/api/reject-combination/restore', {'icon':'sub/square','svg_sha256':'abc'})[0], 200)
        self.assertEqual(json.loads(self.request('GET', '/api/pending-briefs')[1]), [])
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])['sub/square'], 'ready')

    def test_bad_split_or_stale_revision_never_creates_queue_rows(self):
        for change, status in [({'components': []},400), ({'svg_sha256':'stale'},409), ({'combination_type':'unknown'},400)]:
            data = self.payload(); data.update(change)
            self.assertEqual(self.request('POST', '/api/reject-combination', data)[0], status)
        self.assertEqual(json.loads(self.request('GET', '/api/pending-briefs')[1]), [])


class ReferenceQueueTests(unittest.TestCase):
    def test_source_before_generation_can_be_queued_idempotently(self):
        with TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            (root/'source.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
            data = {'reference_path':'source.svg','combination_type':'container','components':[
                {'name':'Badge','family':'container','description':'Empty badge outline'},
                {'name':'Check','family':'sub','description':'Check mark alone'}]}
            payload = root/'brief.json';payload.write_text(json.dumps(data))
            database = root/'data/feedback.sqlite3'
            with patch.object(queue_brief,'ROOT',root):
                for _ in range(2):
                    self.assertEqual(queue_brief.main(['--file',str(payload),'--database',str(database)]),0)
            with sqlite3.connect(database) as connection:
                rows = list_briefs(connection)
            self.assertEqual(len(rows),2)
            self.assertEqual(rows[0]['icon'],'reference:source.svg')


if __name__ == '__main__':
    unittest.main()
