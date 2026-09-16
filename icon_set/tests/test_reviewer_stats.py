"""Current-decision activity, local calendar boundaries, and public dashboard integration."""
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
        self.db.execute('CREATE TABLE reviews(icon, svg_sha256, status, updated_at, updated_by)')
        self.db.execute('CREATE TABLE split_requests(icon, svg_sha256, created_by, created_at, active)')
        self.catalog = {}

    def review(self, icon='solo/a', status='approve', user='jakes', at='2026-09-16T01:00:00+00:00', sha=None, family='solo'):
        self.catalog.setdefault(icon, dict(svg_sha256=icon, family=family))
        self.db.execute('INSERT INTO reviews VALUES (?,?,?,?,?)', (icon, sha or icon, status, at, user))

    def stats(self, **params):
        return reviewer_stats(self.db, {key: [value] for key, value in params.items()}, USERS, self.catalog,
                              now=datetime(2026, 9, 16, 12, tzinfo=timezone.utc))

    def test_empty_period_contains_every_day_and_reviewer(self):
        result = self.stats()
        self.assertEqual((result['start'], result['end']), ('2026-09-10', '2026-09-16'))
        self.assertEqual(len(result['daily']), 7)
        self.assertEqual({row['reviewer'] for row in result['reviewers']}, set(USERS))
        self.assertEqual(len(result['reviewer_daily']), 28)
        self.assertEqual(result['totals']['total'], 0)

    def test_only_current_decisions_count_and_all_time_matches_current_status(self):
        self.review('solo/a', 'approve', at='2026-09-14T01:00:00Z')
        self.review('solo/regenerated', 'approve', sha='old')  # the catalog now holds another SVG
        self.review('solo/gone', 'approve')
        del self.catalog['solo/gone']
        self.review('solo/b', 'pending', user='hina')
        self.review('sub/c', 'approve', user='phuong', family='sub', at='2026-09-01T01:00:00Z')
        self.catalog['solo/d'] = dict(svg_sha256='d', family='solo')
        self.db.execute("INSERT INTO split_requests VALUES ('solo/d','d','ray','2026-09-15T01:00:00Z',1)")
        week = self.stats()
        self.assertEqual(week['totals'], dict(total=3, approved=1, disapproved=1, rejected=1))
        self.assertEqual(week['current']['totals'], dict(total=5, approved=2, disapproved=1, rejected=1, ready=1))
        everything = self.stats(period='all')
        self.assertEqual(everything['start'], '2026-09-01')
        current = everything['current']
        self.assertEqual(everything['totals']['total'], current['totals']['total'] - current['totals']['ready'])
        for key in ('approved', 'disapproved', 'rejected'):
            self.assertEqual(everything['totals'][key], current['totals'][key])
            self.assertEqual(sum(row[key] for row in everything['reviewers']), sum(row[key] for row in current['reviewers']))
        self.assertEqual(sum(day['total'] for day in everything['reviewer_daily']), 4)
        self.assertEqual([row['family'] for row in current['families']], ['solo', 'sub'])
        sub = self.stats(period='all', family='sub')
        self.assertEqual((sub['totals']['approved'], sub['current']['totals']['total']), (1, 1))
        ray = self.stats(period='all', reviewer='ray')
        self.assertEqual((ray['totals']['rejected'], ray['current']['totals']['total']), (1, 1))

    def test_changed_decision_moves_to_its_new_day_and_reviewer(self):
        self.review('solo/a', 'pending', user='hina', at='2026-09-14T01:00:00Z')
        self.db.execute("UPDATE reviews SET status='approve', updated_by='phuong', updated_at='2026-09-16T01:00:00Z'")
        result = self.stats()
        self.assertEqual(result['totals'], dict(total=1, approved=1, disapproved=0, rejected=0))
        self.assertEqual([row['reviewer'] for row in result['reviewers'] if row['total']], ['phuong'])
        self.assertEqual(result['daily'][-1]['total'], 1)

    def test_vietnam_midnight_and_end_exclusive(self):
        self.review(icon='solo/before', at='2026-09-15T16:59:59Z')
        self.review(icon='solo/start', at='2026-09-15T17:00:00Z')
        self.review(icon='solo/end', at='2026-09-16T16:59:59Z')
        self.review(icon='solo/after', at='2026-09-16T17:00:00Z')
        self.assertEqual(self.stats(start='2026-09-16', end='2026-09-16')['totals']['total'], 2)
        self.assertEqual(self.stats(start='2026-09-15', end='2026-09-15', timezone='UTC')['totals']['total'], 2)

    def test_daylight_saving_uses_calendar_days(self):
        self.review(icon='solo/start', at='2026-03-08T05:00:00Z')
        self.review(icon='solo/end', at='2026-03-09T03:59:59Z')
        self.review(icon='solo/after', at='2026-03-09T04:00:00Z')
        data = self.stats(start='2026-03-08', end='2026-03-08', timezone='America/New_York')
        self.assertEqual(data['totals']['total'], 2)

    def test_invalid_queries_are_rejected(self):
        for query in (dict(start='bad'), dict(timezone='invalid'), dict(timezone='/etc/passwd'),
                      dict(start='2026-09-17', end='2026-09-16'), dict(start='2020-01-01'),
                      dict(reviewer='unknown'), dict(end='9999-12-31'),
                      dict(start='0001-01-01', end='0001-01-01'), dict(family='unknown')):
            with self.subTest(query=query), self.assertRaises(ValueError):
                self.stats(**query)

    def test_former_reviewers_stay_available(self):
        self.review(user='former-reviewer')
        self.assertIn('former-reviewer', self.stats()['available_reviewers'])
        self.assertEqual(self.stats()['totals']['total'], 1)


class ReviewerStatsAPITests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_activity_follows_current_status(self):
        icon = dict(icon='sub/square', svg_sha256='abc')
        stats = lambda: json.loads(self.request('GET', '/api/reviewer-stats', anonymous=True)[1])
        self.assertEqual(self.request('POST', '/api/reviews', dict(icon, status='approve'))[0], 201)
        self.assertEqual(stats()['totals'], dict(total=1, approved=1, disapproved=0, rejected=0))
        self.assertEqual(self.request('POST', '/api/feedback', dict(icon, feedback='Fix the stroke'))[0], 201)
        data = stats()
        self.assertEqual(data['totals'], dict(total=1, approved=0, disapproved=1, rejected=0))
        self.assertEqual(data['current']['totals']['disapproved'], 1)
        self.request('POST', '/api/reviews', dict(icon, status='ready'))
        self.assertEqual(stats()['totals']['total'], 0)
        self.assertEqual(self.request('GET', '/api/reviewer-stats?start=bad')[0], 400)
        for asset in ('reviewers.html', 'reviewers.css', 'reviewers.js'):
            self.assertEqual(self.request('GET', '/gallery/' + asset, anonymous=True)[0], 200)


if __name__ == '__main__':
    unittest.main()
