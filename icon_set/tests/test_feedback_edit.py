import json
import unittest
from icon_set.tests import test_gallery

class FeedbackEditTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_autosave_updates_one_entry_and_rejects_stale_writes(self):
        payload = {'icon': 'sub/square', 'svg_sha256': 'abc', 'feedback': 'Round it', 'reason': 'other'}
        code, body = self.request('POST', '/api/feedback', payload)
        self.assertEqual(code, 201)
        saved = json.loads(body)
        update = dict(payload, feedback_id=saved['id'], previous_feedback='Round it',
                      feedback='Round the lower corners.', reason='bad-stroke')
        self.assertEqual(self.request('POST', '/api/feedback', update)[0], 201)
        rows = json.loads(self.request('GET', '/api/feedback?icon=sub/square')[1])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['id'], saved['id'])
        self.assertEqual(rows[0]['feedback'], update['feedback'])
        self.assertEqual(rows[0]['reason'], 'bad-stroke')
        self.assertEqual(rows[0]['edited_by'], 'jakes')
        self.assertEqual(self.request('POST', '/api/feedback', update)[0], 409)
        self.assertEqual(self.request('POST', '/api/feedback', dict(update, svg_sha256='old'))[0], 409)
        self.assertEqual(self.request('POST', '/api/feedback', dict(update, feedback_id='wrong'))[0], 400)
        self.assertEqual(len(json.loads(self.request('GET', '/api/feedback-feed')[1])), 1)

    def test_edit_in_place_preserves_revision_and_review(self):
        self.request('POST','/api/feedback',{'icon':'sub/square','svg_sha256':'abc','feedback':'Original'})
        self.request('POST','/api/reviews',{'icon':'sub/square','svg_sha256':'abc','status':'approve'})
        before=json.loads(self.request('GET','/api/feedback-feed')[1])[0]
        data={'id':before['id'],'previous_feedback':'Original','feedback':' Updated request '}
        self.assertEqual(self.request('POST','/api/feedback/edit',data)[0],200)
        after=json.loads(self.request('GET','/api/feedback-feed')[1])
        self.assertEqual(before['author'],'jakes')
        self.assertEqual(after,[dict(before,feedback='Updated request',edited_by='jakes',edited_at=after[0]['edited_at'])])
        self.assertIsNotNone(after[0]['edited_at'])
        self.assertEqual(json.loads(self.request('GET','/api/feedback?icon=sub/square')[1])[0]['feedback'],'Updated request')
        self.assertEqual(json.loads(self.request('GET','/api/reviews')[1])['sub/square'],'approve')
        self.assertEqual(self.request('POST','/api/feedback/edit',data)[0],409)
        self.assertEqual(self.request('POST','/api/feedback/edit',dict(data,id=999))[0],404)
        for value in (' ', 'x'*10001, None):
            self.assertEqual(self.request('POST','/api/feedback/edit',dict(data,feedback=value))[0],400)
        self.assertEqual(self.request('POST','/api/feedback/edit',data,{'Content-Type':'application/json','Origin':'http://elsewhere.test'})[0],403)
