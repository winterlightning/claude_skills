"""Historical throughput, local calendar boundaries, and public dashboard integration."""
from contextlib import closing
from datetime import datetime, timezone
import json
import sqlite3
import unittest

from icon_set.scripts.reviewer_stats import reviewer_stats
from icon_set.tests import test_gallery

USERS = ('jakes', 'ray', 'phuong', 'hina')


class ReviewerStatsTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.execute('CREATE TABLE activity_log(id INTEGER PRIMARY KEY, username, action, icon, details, created_at)')

    def event(self, user='jakes', action='review', icon='solo/a', status='approve', at='2026-09-16T01:00:00+00:00'):
        self.db.execute('INSERT INTO activity_log(username,action,icon,details,created_at) VALUES (?,?,?,?,?)',
                        (user, action, icon, json.dumps({'status': status}), at))

    def stats(self, **params):
        return reviewer_stats(self.db, {key: [value] for key, value in params.items()}, USERS,
                              now=datetime(2026, 9, 16, 12, tzinfo=timezone.utc))

    def test_empty_period_contains_every_day_and_reviewer(self):
        result = self.stats()
        self.assertEqual((result['start'], result['end']), ('2026-09-10', '2026-09-16'))
        self.assertEqual(len(result['daily']), 7)
        self.assertEqual({row['reviewer'] for row in result['reviewers']}, set(USERS))
        self.assertEqual(len(result['reviewer_daily']), 28)
        self.assertEqual(result['totals']['total'], 0)

    def test_latest_decision_per_icon_reviewer_day_and_preserved_history(self):
        self.event(status='pending')
        self.event(status='approve', at='2026-09-16T02:00:00Z')
        self.event(status='approve', at='2026-09-16T02:00:01Z')  # repeated click
        self.event(user='hina', status='rejected')  # another reviewer counts independently
        self.event(at='2026-09-15T02:00:00Z')  # another day counts again
        self.event(action='restore', status='ready', at='2026-09-16T03:00:00Z')
        self.event(icon='solo/deleted', action='reject_combination', status=None)
        result = self.stats()
        self.assertEqual(result['totals'], dict(total=4, approved=2, disapproved=0, rejected=2))
        self.assertEqual(result['unique_icons'], 2)
        self.assertEqual(sum(day['total'] for day in result['daily']), 4)
        self.assertEqual(sum(day['total'] for day in result['reviewer_daily']), 4)
        self.assertEqual(sum(row['total'] for row in result['reviewers']), 4)
        self.assertEqual(result['reviewers'][0]['active_days'], 2)
        self.assertEqual(self.stats(reviewer='hina')['totals']['total'], 1)

    def test_feedback_routes_and_unrelated_actions(self):
        self.event(action='feedback', status='pending')
        self.event(action='feedback_edit', status='pending')  # resubmitted disapproval
        self.event(icon='solo/b', action='feedback_edit', status='pending')
        self.event(icon='solo/c', action='feedback', status='rejected')
        for action in ('login', 'restore', 'feedback_delete', 'flag', 'discard', 'feedback_sync'):
            self.event(icon='solo/ignored', action=action, status='approve')
        self.event(icon='solo/ignored', action='feedback_edit', status=None)
        self.event(icon='solo/ignored', status='ready')
        self.assertEqual(self.stats()['totals'], dict(total=2, approved=0, disapproved=2, rejected=0))

    def test_vietnam_midnight_and_end_exclusive(self):
        self.event(icon='solo/before', at='2026-09-15T16:59:59Z')
        self.event(icon='solo/start', at='2026-09-15T17:00:00Z')
        self.event(icon='solo/end', at='2026-09-16T16:59:59Z')
        self.event(icon='solo/after', at='2026-09-16T17:00:00Z')
        data = self.stats(start='2026-09-16', end='2026-09-16')
        self.assertEqual(data['totals']['total'], 2)
        self.assertEqual(self.stats(start='2026-09-15', end='2026-09-15', timezone='UTC')['totals']['total'], 2)

    def test_daylight_saving_uses_calendar_days(self):
        self.event(icon='solo/start', at='2026-03-08T05:00:00Z')
        self.event(icon='solo/end', at='2026-03-09T03:59:59Z')
        self.event(icon='solo/after', at='2026-03-09T04:00:00Z')
        data = self.stats(start='2026-03-08', end='2026-03-08', timezone='America/New_York')
        self.assertEqual(data['totals']['total'], 2)

    def test_invalid_queries_are_rejected(self):
        for query in (dict(start='bad'), dict(timezone='invalid'), dict(timezone='/etc/passwd'),
                      dict(start='2026-09-17', end='2026-09-16'), dict(start='2020-01-01'),
                      dict(reviewer='unknown'), dict(end='9999-12-31'),
                      dict(start='0001-01-01', end='0001-01-01')):
            with self.subTest(query=query), self.assertRaises(ValueError):
                self.stats(**query)

    def test_bad_legacy_details_do_not_break_counts(self):
        self.event(user='former-reviewer')
        self.db.execute("INSERT INTO activity_log VALUES (2,'jakes','review','solo/b','not-json','2026-09-16T01:00:00Z')")
        self.assertIn('former-reviewer', self.stats()['available_reviewers'])
        self.assertEqual(self.stats()['totals']['total'], 1)


class ReviewerStatsAPITests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_dashboard_and_history_survive_current_status_changes(self):
        icon = dict(icon='sub/square', svg_sha256='abc')
        self.assertEqual(self.request('POST', '/api/reviews', dict(icon, status='approve'))[0], 201)
        self.assertEqual(self.request('POST', '/api/feedback', dict(icon, feedback='Fix the stroke'))[0], 201)
        status, raw = self.request('GET', '/api/reviewer-stats', anonymous=True)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(raw)['totals'], dict(total=1, approved=0, disapproved=1, rejected=0))
        self.request('POST', '/api/reviews', dict(icon, status='ready'))
        with closing(sqlite3.connect(self.database)) as db, db:
            db.execute('DELETE FROM reviews')
            db.execute('DELETE FROM feedback')
        self.assertEqual(json.loads(self.request('GET', '/api/reviewer-stats')[1])['totals']['total'], 1)
        self.assertEqual(self.request('GET', '/api/reviewer-stats?start=bad')[0], 400)
        for asset in ('reviewers.html', 'reviewers.css', 'reviewers.js'):
            self.assertEqual(self.request('GET', '/gallery/' + asset, anonymous=True)[0], 200)


if __name__ == '__main__':
    unittest.main()
