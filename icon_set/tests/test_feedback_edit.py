import json
import unittest
from icon_set.tests import test_gallery

class FeedbackEditTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_edit_in_place_preserves_revision_and_review(self):
        self.request('POST','/api/feedback',{'icon':'sub/square','svg_sha256':'abc','feedback':'Original'})
        self.request('POST','/api/reviews',{'icon':'sub/square','svg_sha256':'abc','status':'approve'})
        before=json.loads(self.request('GET','/api/feedback-feed')[1])[0]
        data={'id':before['id'],'previous_feedback':'Original','feedback':' Updated request '}
        self.assertEqual(self.request('POST','/api/feedback/edit',data)[0],200)
        after=json.loads(self.request('GET','/api/feedback-feed')[1])
        self.assertEqual(after,[dict(before,feedback='Updated request')])
        self.assertEqual(json.loads(self.request('GET','/api/feedback?icon=sub/square')[1])[0]['feedback'],'Updated request')
        self.assertEqual(json.loads(self.request('GET','/api/reviews')[1])['sub/square'],'approve')
        self.assertEqual(self.request('POST','/api/feedback/edit',data)[0],409)
        self.assertEqual(self.request('POST','/api/feedback/edit',dict(data,id=999))[0],404)
        for value in (' ', 'x'*10001, None):
            self.assertEqual(self.request('POST','/api/feedback/edit',dict(data,feedback=value))[0],400)
        self.assertEqual(self.request('POST','/api/feedback/edit',data,{'Content-Type':'application/json','Origin':'http://elsewhere.test'})[0],403)
