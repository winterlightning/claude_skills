import json
import unittest
from icon_set.tests import test_gallery
from icon_set.scripts.deploy import init_database

class IconFlagTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_flags_persist_clear_and_leave_reviews_alone(self):
        endpoint='/api/icon-flag'
        self.assertEqual(json.loads(self.request('GET',endpoint+'?icon=sub/square')[1]),{'flag':''})
        for flag in ('container_combination','combination','other'):
            self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':flag})[0],200)
            init_database(self.database)
            self.assertEqual(json.loads(self.request('GET',endpoint+'?icon=sub/square')[1]),{'flag':flag})
        self.assertEqual(json.loads(self.request('GET','/api/reviews')[1])['sub/square'],'ready')
        self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':''})[0],200)
        self.assertEqual(json.loads(self.request('GET',endpoint+'?icon=sub/square')[1]),{'flag':''})
        self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':'bad'})[0],400)
        self.assertEqual(self.request('POST',endpoint,{'icon':'missing','flag':'other'})[0],404)
        self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':'other'}, {'Content-Type':'application/json','Origin':'http://elsewhere.test'})[0],403)
