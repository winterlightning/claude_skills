"""Every change needs a login and is attributed: on the record itself and in the activity log."""
import json
from contextlib import closing
import sqlite3
import unittest
from unittest.mock import Mock

from icon_set.tests import test_gallery

ACTION_ROUTES = ('/api/generation', '/api/generation/accept', '/api/generation/discard', '/api/icon-flag',
                 '/api/feedback/edit', '/api/feedback', '/api/reviews', '/api/reject-combination',
                 '/api/pending-briefs/complete', '/api/reject-combination/restore', '/api/reference-images')


class ActivityLogTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def activity(self):
        with closing(sqlite3.connect(self.database)) as connection:
            return [(user, action, icon, json.loads(details)) for user, action, icon, details in
                    connection.execute('SELECT username, action, icon, details FROM activity_log ORDER BY id')]

    def test_every_action_requires_login(self):
        for route in ACTION_ROUTES:
            with self.subTest(route=route):
                status, body = self.request('POST', route, {'icon': 'sub/square', 'svg_sha256': 'abc'}, anonymous=True)
                self.assertEqual(status, 401)
                self.assertIn('Log in', json.loads(body)['error'])
        self.assertEqual([row[1] for row in self.activity()], ['login'], 'Refused requests record nothing')
        # Reading stays public.
        for path in ('/api/reviews', '/api/feedback?icon=sub/square', '/api/icon-flag?icon=sub/square',
                     '/api/review-detail?icon=sub/square', '/gallery/index.html'):
            self.assertEqual(self.request('GET', path, anonymous=True)[0], 200, path)

    def test_approver_filter_uses_current_approved_revision(self):
        icon = {'icon': 'sub/square', 'svg_sha256': 'abc'}
        for user in ('phuong', 'hina', 'jakes', 'ray'):
            self.request('POST', '/api/auth/login', {'username': user, 'password': '1'}, anonymous=True)
            status, body = self.request('POST', '/api/reviews', dict(icon, status='approve'))
            self.assertEqual(status, 201)
            self.assertEqual(json.loads(body)['updated_by'], user)
            data = json.loads(self.request('GET', '/api/reviews?include_approvers=1', anonymous=True)[1])
            self.assertEqual(data['approved_by'], {'sub/square': user})
            self.assertEqual(data['statuses'], json.loads(self.request('GET', '/api/reviews')[1]))
        with closing(sqlite3.connect(self.database)) as connection, connection:
            connection.execute("UPDATE reviews SET updated_by=NULL")
        self.assertEqual(json.loads(self.request('GET', '/api/reviews?include_approvers=1')[1])['approved_by'], {})
        with closing(sqlite3.connect(self.database)) as connection, connection:
            connection.execute("UPDATE reviews SET svg_sha256='old', updated_by='hina'")
        self.assertEqual(json.loads(self.request('GET', '/api/reviews?include_approvers=1')[1])['approved_by'], {})
        self.request('POST', '/api/reviews', dict(icon, status='approve'))
        with closing(sqlite3.connect(self.database)) as connection, connection:
            connection.execute("UPDATE reviews SET status='rejected' WHERE svg_sha256='old'")
        data = json.loads(self.request('GET', '/api/reviews?include_approvers=1')[1])
        self.assertEqual(data['statuses']['sub/square'], 'rejected')
        self.assertEqual(data['approved_by'], {})

    def test_rejector_filter_tracks_rejection_and_restore(self):
        icon = {'icon': 'sub/square', 'svg_sha256': 'abc'}
        for user in ('phuong', 'ray'):
            self.request('POST', '/api/auth/login', {'username': user, 'password': '1'}, anonymous=True)
            self.assertEqual(self.request('POST', '/api/reviews', dict(icon, status='rejected'))[0], 201)
            data = json.loads(self.request('GET', '/api/reviews?include_approvers=1', anonymous=True)[1])
            self.assertEqual(data['rejected_by'], {'sub/square': user})
            self.assertEqual(data['approved_by'], {})
        with closing(sqlite3.connect(self.database)) as connection, connection:
            connection.execute("UPDATE reviews SET svg_sha256='old'")
        data = json.loads(self.request('GET', '/api/reviews?include_approvers=1')[1])
        self.assertEqual(data['rejected_by'], {'sub/square': 'ray'}, 'Rejection persists across revisions')
        self.assertEqual(self.request('POST', '/api/reject-combination/restore', icon)[0], 200)
        data = json.loads(self.request('GET', '/api/reviews?include_approvers=1')[1])
        self.assertEqual(data['rejected_by'], {})

    def test_actions_record_who_did_them(self):
        icon = {'icon': 'sub/square', 'svg_sha256': 'abc'}
        self.assertEqual(self.request('POST', '/api/feedback', dict(icon, feedback='Round it'))[0], 201)
        row = json.loads(self.request('GET', '/api/feedback?icon=sub/square')[1])[0]
        self.assertEqual(row['author'], 'jakes')
        self.assertEqual(self.request('POST', '/api/feedback/edit', {'id': row['id'], 'feedback': 'Round it more',
                                                                   'previous_feedback': 'Round it'})[0], 200)
        self.assertEqual(self.request('POST', '/api/icon-flag', {'icon': 'sub/square', 'flag': 'other'})[0], 200)
        self.assertEqual(self.request('POST', '/api/icon-flag', {'icon': 'sub/square', 'flag': ''})[0], 200)

        # A second reviewer approves; the detail names them, not the first reviewer.
        self.request('POST', '/api/auth/logout', {})
        self.assertEqual(self.request('POST', '/api/auth/login', {'username': 'hina', 'password': '1'}, anonymous=True)[0], 200)
        self.assertEqual(self.request('POST', '/api/reviews', dict(icon, status='approve'))[0], 201)
        detail = json.loads(self.request('GET', '/api/review-detail?icon=sub/square')[1])
        self.assertEqual((detail['status'], detail['updated_by']), ('approve', 'hina'))
        self.assertEqual(self.request('POST', '/api/reviews', dict(icon, status='rejected'))[0], 201)
        self.assertEqual(json.loads(self.request('GET', '/api/review-detail?icon=sub/square')[1])['updated_by'], 'hina')
        self.assertEqual(self.request('POST', '/api/reject-combination/restore', icon)[0], 200)

        self.server.generation = Mock()
        self.server.generation.start.return_value = {'id': 'a' * 32, 'mode': 'generate', 'name': 'Mark', 'source': None}
        self.server.generation.decide.return_value = {'id': 'a' * 32, 'mode': 'generate', 'name': 'Mark', 'source': None}
        self.assertEqual(self.request('POST', '/api/generation', {'mode': 'generate', 'name': 'Mark', 'prompt': 'x', 'family': 'sub'})[0], 202)
        self.assertEqual(self.server.generation.start.call_args.args[2], 'hina')
        self.assertEqual(self.request('POST', '/api/generation/discard', {'id': 'a' * 32})[0], 202)
        self.assertEqual(self.server.generation.decide.call_args.args, ('a' * 32, False, 'hina'))

        log = self.activity()
        self.assertEqual([(user, action) for user, action, _, _ in log], [
            ('jakes', 'login'), ('jakes', 'feedback'), ('jakes', 'feedback_edit'), ('jakes', 'flag'), ('jakes', 'unflag'),
            ('jakes', 'logout'), ('hina', 'login'), ('hina', 'review'), ('hina', 'review'), ('hina', 'restore'),
            ('hina', 'generate'), ('hina', 'generation_discard'),
        ])
        self.assertEqual(log[2][3], {'feedback_id': row['id'], 'previous_feedback': 'Round it'})
        self.assertEqual([details.get('status') for _, action, _, details in log if action == 'review'], ['approve', 'rejected'])
        self.assertTrue(all(icon_key == 'sub/square' for _, action, icon_key, _ in log
                            if action in ('feedback', 'feedback_edit', 'flag', 'unflag', 'review', 'restore')))

    def test_rejected_combination_and_brief_completion_record_actor(self):
        split = {'icon': 'sub/square', 'svg_sha256': 'abc', 'combination_type': 'side', 'reason': 'two things',
                 'components': [{'name': 'Box', 'family': 'solo', 'description': 'a box'},
                                {'name': 'Plus', 'family': 'sub', 'description': 'a plus'}]}
        self.assertEqual(self.request('POST', '/api/reject-combination', split)[0], 201)
        self.assertEqual(self.request('POST', '/api/reject-combination', split)[0], 201)
        briefs = json.loads(self.request('GET', '/api/pending-briefs')[1])
        self.assertEqual({brief['created_by'] for brief in briefs}, {'jakes'})
        detail = json.loads(self.request('GET', '/api/review-detail?icon=sub/square')[1])
        self.assertEqual((detail['status'], detail['updated_by']), ('rejected', 'jakes'))
        data = json.loads(self.request('GET', '/api/reviews?include_approvers=1')[1])
        self.assertEqual(data['rejected_by'], {'sub/square': 'jakes'})
        self.assertEqual([action for _, action, _, _ in self.activity()].count('reject_combination'), 1,
                         'A repeated click is not recorded twice')


if __name__ == '__main__':
    unittest.main()
