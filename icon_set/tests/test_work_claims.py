"""Work claims: one production database decides who fixes which disapproved icon."""
from contextlib import closing
from datetime import datetime, timedelta, timezone
import http.client
import json
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest
from unittest.mock import patch

from icon_set.scripts import work_claims
from icon_set.scripts.deploy import create_server
from icon_set.scripts.gallery import stage_gallery
from icon_set.tests.test_gallery import manifest

NOW = datetime(2026, 9, 23, 12, 0, tzinfo=timezone.utc)
ICON, SHA = 'sub/square', 'abc'


class StateRuleTests(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        init_database_tables(self.connection)
        self.log = []

    def record(self, connection, user, action, icon=None, **details):
        self.log.append((user, action, icon, details))

    def disapprove(self, when=NOW - timedelta(hours=1)):
        self.connection.execute("INSERT OR REPLACE INTO reviews VALUES (?,?,'pending',?,'hina')", (ICON, SHA, when.isoformat()))
        return ('pending', 'hina', when.isoformat())

    def test_open_then_claimed_then_done_then_reopened_by_new_disapproval(self):
        decision = self.disapprove()
        self.assertEqual(work_claims.work_state(None, decision[2], NOW), 'open')
        work = work_claims.claim(self.connection, ICON, SHA, ' mac-a/claude ', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual((work['state'], work['worker']), ('working', 'mac-a/claude'))
        self.assertEqual(work['expires_at'], (NOW + timedelta(hours=3)).isoformat())
        with self.assertRaises(work_claims.WorkError) as refused:
            work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(refused.exception.status, 409)
        self.assertEqual(refused.exception.work['state'], 'working')
        with self.assertRaises(work_claims.WorkError):
            work_claims.finish(self.connection, ICON, SHA, 'mac-b/claude', 'done', decision=decision, now=NOW, record=self.record, user='system')
        later = NOW + timedelta(minutes=30)
        result = work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'done', note='sub/square-v2', decision=decision, now=later, record=self.record, user='system')
        self.assertEqual(result['status'], 'ready')
        self.assertEqual(result['work']['state'], 'done')
        status = self.connection.execute('SELECT status, updated_by FROM reviews WHERE icon=? AND svg_sha256=?', (ICON, SHA)).fetchone()
        self.assertEqual(status, ('ready', 'mac-a/claude'))
        # Done stays done while the revision is Ready or newly re-approved ...
        ready = ('ready', 'mac-a/claude', later.isoformat())
        self.assertEqual(work_claims.work_state(work_claims.load_claim(self.connection, ICON, SHA), ready[2], later), 'done')
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=ready, now=later, record=self.record, user='system')
        # ... until a reviewer disapproves it again after the report.
        again = self.disapprove(later + timedelta(hours=2))
        self.assertEqual(work_claims.work_state(work_claims.load_claim(self.connection, ICON, SHA), again[2], later + timedelta(hours=3)), 'open')
        work = work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=again, now=later + timedelta(hours=3), record=self.record, user='system')
        self.assertEqual((work['state'], work['worker']), ('working', 'mac-b/claude'))
        self.assertEqual([entry[1] for entry in self.log], ['work_claim', 'work_done', 'review', 'work_claim'])

    def test_expired_lease_is_claimable_and_logged(self):
        decision = self.disapprove()
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        stale = NOW + timedelta(hours=3, minutes=1)
        self.assertEqual(work_claims.work_state(work_claims.load_claim(self.connection, ICON, SHA), decision[2], stale), 'expired')
        with self.assertRaises(work_claims.WorkError):
            work_claims.heartbeat(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=stale, record=self.record, user='system')
        work = work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=stale, record=self.record, user='system')
        self.assertEqual(work['worker'], 'mac-b/claude')
        self.assertIn('work_expired', [entry[1] for entry in self.log])
        extended = work_claims.heartbeat(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=stale, record=self.record, user='system', lease_hours=1)
        self.assertEqual(extended['expires_at'], (stale + timedelta(hours=1)).isoformat())

    def test_cannot_fix_needs_a_note_and_blocks_until_redisapproved(self):
        decision = self.disapprove()
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        with self.assertRaises(work_claims.WorkError) as refused:
            work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'cannot-fix', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(refused.exception.status, 400)
        result = work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'cannot-fix', note='needs 5 gaps', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(result['work']['state'], 'cannot-fix')
        self.assertNotIn('status', result)
        self.assertEqual(self.connection.execute('SELECT status FROM reviews WHERE icon=?', (ICON,)).fetchone()[0], 'pending')
        catalog = {ICON: {'key': ICON, 'svg_sha256': SHA, 'family': 'sub'}}
        decisions = {ICON: decision}
        self.assertEqual(work_claims.queue(self.connection, catalog, decisions, {}, NOW)['total'], 0)

    def test_abandon_reopens_and_only_owner_or_admin_may(self):
        decision = self.disapprove()
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        with self.assertRaises(work_claims.WorkError):
            work_claims.abandon(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=NOW, record=self.record, user='system')
        result = work_claims.abandon(self.connection, ICON, SHA, 'jakes', decision=decision, now=NOW, record=self.record, user='jakes', admin=True)
        self.assertEqual(result['work'], {'state': 'open'})
        self.assertIsNone(work_claims.load_claim(self.connection, ICON, SHA))

    def test_queue_lists_oldest_claimable_disapprovals_with_feedback(self):
        catalog = {'sub/a': {'key': 'sub/a', 'svg_sha256': 'a1', 'family': 'sub', 'category': 'shapes'},
                   'sub/b': {'key': 'sub/b', 'svg_sha256': 'b1', 'family': 'sub', 'category': 'shapes'},
                   'solo/c': {'key': 'solo/c', 'svg_sha256': 'c1', 'family': 'solo', 'category': 'tools'},
                   'solo/d': {'key': 'solo/d', 'svg_sha256': 'd1', 'family': 'solo'}}
        decisions = {'sub/a': ('pending', 'hina', '2026-09-20T10:00:00+00:00'),
                     'sub/b': ('pending', 'ray', '2026-09-19T10:00:00+00:00'),
                     'solo/c': ('pending', 'hina', '2026-09-21T10:00:00+00:00'),
                     'solo/d': ('approve', 'hina', '2026-09-21T10:00:00+00:00')}
        self.connection.execute("INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reason, author) VALUES ('sub/a','older','a1','t1','other','ray')")
        self.connection.execute("INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reason, author) VALUES ('sub/a','Round the corners','a1','t2','bad-stroke','hina')")
        work_claims.claim(self.connection, 'solo/c', 'c1', 'mac-a/claude', decision=decisions['solo/c'], now=NOW, record=self.record, user='system')
        page = work_claims.queue(self.connection, catalog, decisions, {}, NOW)
        self.assertEqual([item['key'] for item in page['items']], ['sub/b', 'sub/a'])
        self.assertEqual(page['items'][1]['feedback'], 'Round the corners')
        self.assertEqual(page['items'][1]['reason'], 'bad-stroke')
        self.assertEqual(page['items'][1]['status'], 'disapprove')
        self.assertEqual(page['items'][1]['work'], {'state': 'open'})
        self.assertEqual(work_claims.queue(self.connection, catalog, decisions, {'family': ['solo']}, NOW)['total'], 0)
        everything = work_claims.queue(self.connection, catalog, decisions, {}, NOW, claimable_only=False)
        self.assertEqual([(item['key'], item['work']['state']) for item in everything['items']],
                         [('sub/b', 'open'), ('sub/a', 'open'), ('solo/c', 'working')])
        paged = work_claims.queue(self.connection, catalog, decisions, {'limit': ['1']}, NOW)
        self.assertEqual((paged['total'], paged['next_offset'], paged['items'][0]['key']), (2, 1, 'sub/b'))
        rows = work_claims.listing(self.connection, catalog, decisions, NOW)['claims']
        self.assertEqual((rows[0]['icon'], rows[0]['state'], rows[0]['current'], rows[0]['status']), ('solo/c', 'working', True, 'disapprove'))
        catalog['solo/c']['svg_sha256'] = 'c2'
        self.assertEqual(work_claims.listing(self.connection, catalog, decisions, NOW)['claims'][0]['state'], 'superseded')
        # The new revision is still disapproved: it is open again, the old claim is history.
        review = work_claims.review_listing(self.connection, catalog, decisions, {}, NOW)
        self.assertEqual({item['key']: item['work']['state'] for item in review['items']}, {'sub/a': 'open', 'sub/b': 'open', 'solo/c': 'open'})
        # A deployed fix that starts Ready shows the claim as superseded.
        decisions['solo/c'] = ('ready', None, None)
        review = work_claims.review_listing(self.connection, catalog, decisions, {}, NOW)
        self.assertEqual({item['key']: (item['status'], item['work']['state']) for item in review['items']},
                         {'sub/a': ('disapprove', 'open'), 'sub/b': ('disapprove', 'open'), 'solo/c': ('ready', 'superseded')})
        self.assertEqual(review['items'][0]['key'], 'solo/c', 'most recent work first')
        self.assertEqual(work_claims.review_listing(self.connection, catalog, decisions, {'state': ['superseded']}, NOW)['total'], 1)

    def test_worker_and_lease_validation(self):
        decision = self.disapprove()
        for bad in ('', ' ', 'x' * 121, 'a\nb', None, 3):
            with self.assertRaises(work_claims.WorkError):
                work_claims.claim(self.connection, ICON, SHA, bad, decision=decision, now=NOW, record=self.record, user='system')
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-a', decision=decision, now=NOW, record=self.record, user='system', lease_hours=48)
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-a', decision=('ready', None, None), now=NOW, record=self.record, user='system')


def init_database_tables(connection):
    connection.execute('''CREATE TABLE reviews (icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL, status TEXT NOT NULL,
        updated_at TEXT NOT NULL, updated_by TEXT, PRIMARY KEY(icon, svg_sha256))''')
    connection.execute('''CREATE TABLE feedback (id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL,
        svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL, reason TEXT NOT NULL DEFAULT 'other', author TEXT)''')
    connection.execute("CREATE TABLE icon_types (icon TEXT PRIMARY KEY, icon_type TEXT NOT NULL)")
    work_claims.init_work_claims(connection)


class ServerBase(unittest.TestCase):
    def start(self, folder, production, sync_source=None):
        dist = folder / 'dist'
        dist.mkdir()
        manifest(dist, 'sub', 'sub32', 'square')
        # The fixture must not depend on the live icon registry.
        with patch('icon_set.model.icons.registry.factories', return_value={}), \
                patch('icon_set.scripts.symbol_family.stage', side_effect=lambda target, records: records):
            stage_gallery(dist, dist, ['sub32'])
        database = folder / 'data' / 'feedback.sqlite3'
        kwargs = {'production': production}
        if sync_source:
            kwargs['sync_source'] = sync_source
        server = create_server(dist, database, port=0, **kwargs)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        return server, database

    @staticmethod
    def request(server, method, path, data=None, cookie=None):
        connection = http.client.HTTPConnection('127.0.0.1', server.server_port)
        headers = {'Content-Type': 'application/json'}
        if cookie:
            headers['Cookie'] = cookie
        try:
            connection.request(method, path, body=json.dumps(data) if data is not None else None, headers=headers)
            response = connection.getresponse()
            return response.status, json.loads(response.read() or b'null'), response.getheader('Set-Cookie')
        finally:
            connection.close()

    def login(self, server):
        status, _, cookie = self.request(server, 'POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        self.assertEqual(status, 200)
        return cookie.split(';', 1)[0]


class ProductionServerTests(ServerBase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.server, self.database = self.start(Path(self.temp.name), production=True)
        self.cookie = self.login(self.server)

    def disapprove(self, feedback='Round the corners'):
        status, body, _ = self.request(self.server, 'POST', '/api/reviews', {
            'icon': ICON, 'svg_sha256': SHA, 'status': 'disapprove', 'reason': 'bad-stroke', 'feedback': feedback}, self.cookie)
        self.assertEqual(status, 201, body)

    def test_claim_done_and_redisapproval_round_trip(self):
        status, body, _ = self.request(self.server, 'GET', '/api/work/queue')
        self.assertEqual((status, body['total']), (200, 0))
        self.disapprove()
        status, body, _ = self.request(self.server, 'GET', '/api/work/queue?family=sub')
        self.assertEqual((status, body['total'], body['items'][0]['key']), (200, 1, ICON))
        self.assertEqual(body['items'][0]['feedback'], 'Bad stroke drawn\n\nRound the corners')
        claim = {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a/claude'}
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', claim)
        self.assertEqual(status, 201, body)
        self.assertEqual((body['work']['state'], body['item']['key'], body['item']['reason']), ('working', ICON, 'bad-stroke'))
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', dict(claim, worker='mac-b/claude'))
        self.assertEqual((status, body['work']['worker']), (409, 'mac-a/claude'))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/queue')[1]['total'], 0)
        everything = self.request(self.server, 'GET', '/api/work/disapproved')[1]
        self.assertEqual((everything['total'], everything['items'][0]['status'], everything['items'][0]['work']['state']), (1, 'disapprove', 'working'))
        status, body, _ = self.request(self.server, 'GET', '/api/work?icon=' + ICON)
        self.assertEqual((status, body['status'], body['work']['state']), (200, 'disapprove', 'working'))
        self.request(self.server, 'POST', '/api/icon-type', {'icon': ICON, 'icon_type': 'avatar'}, self.cookie)
        status, body, _ = self.request(self.server, 'GET', '/api/icon-types?status=disapprove')
        self.assertEqual(body['icons'][0]['work']['state'], 'working')
        detail = self.request(self.server, 'GET', '/api/review-detail?icon=' + ICON)[1]
        self.assertEqual(detail['work']['worker'], 'mac-a/claude')
        status, body, _ = self.request(self.server, 'POST', '/api/work/done', dict(claim, worker='mac-b/claude'))
        self.assertEqual(status, 409)
        status, body, _ = self.request(self.server, 'POST', '/api/work/done', dict(claim, note='sub/square-v2'))
        self.assertEqual((status, body['status'], body['work']['state']), (200, 'ready', 'done'), body)
        self.assertEqual(self.request(self.server, 'GET', '/api/reviews')[1][ICON], 'ready')
        feedback = self.request(self.server, 'GET', '/api/feedback?icon=' + ICON)[1]
        self.assertEqual(len(feedback), 1, 'the disapproval feedback stays for the reviewer')
        self.assertEqual(self.request(self.server, 'GET', '/api/work/queue')[1]['total'], 0)
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', dict(claim, worker='mac-b/claude'))
        self.assertEqual(status, 409, 'Ready icons are not claimable')
        self.disapprove('Still crooked')
        status, body, _ = self.request(self.server, 'GET', '/api/work/queue')
        self.assertEqual((body['total'], body['items'][0]['work']['state']), (1, 'open'))
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', dict(claim, worker='mac-b/claude'))
        self.assertEqual((status, body['work']['worker']), (201, 'mac-b/claude'))
        listing = self.request(self.server, 'GET', '/api/work')[1]['claims']
        self.assertEqual([(row['icon'], row['worker'], row['state']) for row in listing], [(ICON, 'mac-b/claude', 'working')])
        with closing(sqlite3.connect(self.database)) as connection:
            actions = [row[0] for row in connection.execute("SELECT action FROM activity_log WHERE action LIKE 'work_%' ORDER BY id")]
        self.assertEqual(actions, ['work_claim', 'work_done', 'work_claim'])

    def test_refuses_stale_hash_rejected_icons_and_bad_workers(self):
        self.disapprove()
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', {'icon': ICON, 'svg_sha256': 'old', 'worker': 'mac-a'})
        self.assertEqual((status, body['svg_sha256']), (409, SHA))
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', {'icon': ICON, 'svg_sha256': SHA, 'worker': ''})
        self.assertEqual(status, 400)
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', {'icon': 'sub/missing', 'svg_sha256': SHA, 'worker': 'a'})[0], 404)
        self.request(self.server, 'POST', '/api/reviews', {'icon': ICON, 'svg_sha256': SHA, 'status': 'rejected'}, self.cookie)
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a'})
        self.assertEqual(status, 409)
        self.assertIn('rejected', body['error'])

    def test_claim_many_reports_each_icon(self):
        self.disapprove()
        body = {'worker': 'mac-a/claude', 'icons': [ICON, {'icon': ICON, 'svg_sha256': SHA}, {'icon': 'sub/missing'}, {'icon': ICON, 'svg_sha256': 'old'}]}
        status, result, _ = self.request(self.server, 'POST', '/api/work/claim', body)
        self.assertEqual(status, 200, result)
        self.assertEqual([item['key'] for item in result['claimed']], [ICON])
        self.assertEqual([(row['icon'], row['status']) for row in result['refused']], [('sub/missing', 404)])
        status, result, _ = self.request(self.server, 'POST', '/api/work/claim', {'worker': 'mac-b/claude', 'icons': [ICON]})
        self.assertEqual((status, result['saved'], result['refused'][0]['status'], result['refused'][0]['work']['worker']), (200, False, 409, 'mac-a/claude'))
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', {'worker': 'mac-b', 'icons': []})[0], 400)
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', {'worker': '', 'icons': [ICON]})[0], 400)

    def test_review_listing_history_and_snapshot(self):
        self.disapprove()
        claim = {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a/claude'}
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', claim)[0], 201)
        listing = self.request(self.server, 'GET', '/api/work/review')[1]
        self.assertEqual((listing['total'], listing['counts'], listing['items'][0]['work']['snapshot']), (1, {'working': 1}, True))
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        connection.request('GET', '/api/work/snapshot?icon=' + ICON + '&svg_sha256=' + SHA)
        response = connection.getresponse()
        self.assertEqual((response.status, response.getheader('Content-Type')), (200, 'image/svg+xml'))
        self.assertIn(b'<svg', response.read())
        connection.close()
        self.assertEqual(self.request(self.server, 'POST', '/api/work/done', dict(claim, note='sub/square-v2'))[0], 200)
        listing = self.request(self.server, 'GET', '/api/work/review?state=done')[1]
        self.assertEqual((listing['total'], listing['items'][0]['status'], listing['items'][0]['work']['state']), (1, 'ready', 'done'))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/disapproved')[1]['total'], 0, 'Ready icons leave the disapproved list')
        history = self.request(self.server, 'GET', '/api/work/history?icon=' + ICON)[1]
        self.assertEqual((history['current']['status'], history['current']['work']['state']), ('ready', 'done'))
        self.assertEqual(len(history['revisions']), 1)
        revision = history['revisions'][0]
        self.assertTrue(revision['current'] and revision['snapshot'])
        self.assertEqual((revision['claim']['worker'], revision['review']['status'], len(revision['feedback'])), ('mac-a/claude', 'ready', 1))
        self.assertEqual([event['action'] for event in history['events']], ['feedback', 'work_claim', 'work_done', 'review'])
        self.assertEqual(self.request(self.server, 'GET', '/api/work/history?icon=sub/missing')[0], 404)
        self.assertEqual(self.request(self.server, 'GET', '/api/work/snapshot?icon=' + ICON + '&svg_sha256=nope')[0], 404)

    def test_abandon_by_owner_or_logged_in_reviewer(self):
        self.disapprove()
        claim = {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a/claude'}
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', claim)[0], 201)
        self.assertEqual(self.request(self.server, 'POST', '/api/work/abandon', dict(claim, worker='mac-b'))[0], 409)
        status, body, _ = self.request(self.server, 'POST', '/api/work/abandon', dict(claim, worker='jakes'), self.cookie)
        self.assertEqual((status, body['work']['state']), (200, 'open'))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/queue')[1]['total'], 1)


class ForwardingTests(ServerBase):
    def test_development_server_forwards_to_production_only(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / 'prod').mkdir()
        (root / 'dev').mkdir()
        production, production_db = self.start(root / 'prod', production=True)
        origin = f'http://127.0.0.1:{production.server_port}'
        development, development_db = self.start(root / 'dev', production=False, sync_source=origin)
        cookie = self.login(production)
        status, body, _ = self.request(production, 'POST', '/api/reviews', {
            'icon': ICON, 'svg_sha256': SHA, 'status': 'disapprove', 'reason': 'meaning', 'feedback': 'Looks like a box'}, cookie)
        self.assertEqual(status, 201)
        status, body, _ = self.request(development, 'GET', '/api/work/queue?family=sub')
        self.assertEqual((status, body['total']), (200, 1))
        claim = {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a/claude'}
        status, body, _ = self.request(development, 'POST', '/api/work/claim', claim)
        self.assertEqual((status, body['work']['state']), (201, 'working'))
        status, body, _ = self.request(development, 'POST', '/api/work/claim', dict(claim, worker='mac-b'))
        self.assertEqual((status, body['work']['worker']), (409, 'mac-a/claude'))
        with closing(sqlite3.connect(development_db)) as connection:
            self.assertEqual(connection.execute('SELECT COUNT(*) FROM work_claims').fetchone()[0], 0)
        with closing(sqlite3.connect(production_db)) as connection:
            self.assertEqual(connection.execute('SELECT worker FROM work_claims').fetchone()[0], 'mac-a/claude')
        self.assertEqual(self.request(development, 'GET', '/api/work')[1]['claims'][0]['worker'], 'mac-a/claude')
        connection = http.client.HTTPConnection('127.0.0.1', development.server_port)
        connection.request('GET', '/api/work/snapshot?icon=' + ICON + '&svg_sha256=' + SHA)
        relayed = connection.getresponse()
        self.assertEqual((relayed.status, relayed.getheader('Content-Type')), (200, 'image/svg+xml'))
        self.assertIn(b'<svg', relayed.read())
        connection.close()
        self.assertEqual(self.request(development, 'GET', '/api/work/history?icon=' + ICON)[1]['current']['work']['state'], 'working')
        detail = self.request(development, 'GET', '/api/review-detail?icon=' + ICON)[1]
        self.assertEqual(detail['work']['state'], 'working')
        production.shutdown()
        production.server_close()
        development.work_cache = None
        status, body, _ = self.request(development, 'POST', '/api/work/heartbeat', claim)
        self.assertEqual(status, 502)
        self.assertIn('unreachable', body['error'])
        detail = self.request(development, 'GET', '/api/review-detail?icon=' + ICON)[1]
        self.assertEqual(detail['work']['state'], 'unknown')


if __name__ == '__main__':
    unittest.main()
