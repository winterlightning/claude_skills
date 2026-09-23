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
from icon_set.scripts.deploy import REVIEWS_TABLE, create_server
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
        self.connection.execute("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?,?,'pending',?,'hina') "
                                "ON CONFLICT(icon, svg_sha256) DO UPDATE SET status='pending', updated_at=excluded.updated_at, "
                                "updated_by='hina', worker=NULL, claimed_at=NULL, note=''", (ICON, SHA, when.isoformat()))
        return ('pending', 'hina', when.isoformat())

    def row(self):
        return work_claims.load_row(self.connection, ICON, SHA)

    def test_open_then_claimed_then_done_then_reopened_by_new_disapproval(self):
        decision = self.disapprove()
        self.assertIsNone(work_claims.work_state(self.row(), NOW))
        work = work_claims.claim(self.connection, ICON, SHA, ' mac-a/claude ', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual((work['state'], work['worker']), ('claimed', 'mac-a/claude'))
        self.assertEqual(work['expires_at'], (NOW + timedelta(hours=work_claims.LEASE_HOURS)).isoformat())
        row = self.row()
        self.assertEqual((row['status'], row['worker'], row['claimed_at'], row['updated_by']), ('claimed', 'mac-a/claude', NOW.isoformat(), 'hina'),
                         'the claim is a status on the review row; the reviewer keeps the disapproval')
        with self.assertRaises(work_claims.WorkError) as refused:
            work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=('claimed', 'hina', decision[2]), now=NOW, record=self.record, user='system')
        self.assertEqual(refused.exception.status, 409)
        self.assertEqual(refused.exception.work['state'], 'claimed')
        with self.assertRaises(work_claims.WorkError):
            work_claims.finish(self.connection, ICON, SHA, 'mac-b/claude', 'done', decision=decision, now=NOW, record=self.record, user='system')
        later = NOW + timedelta(minutes=30)
        result = work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'done', note='sub/square-v2', decision=decision, now=later, record=self.record, user='system')
        self.assertEqual(result['status'], 'ready')
        self.assertEqual(result['work']['state'], 'done')
        row = self.row()
        self.assertEqual((row['status'], row['updated_by'], row['worker'], row['note']), ('ready', 'mac-a/claude', 'mac-a/claude', 'sub/square-v2'))
        self.assertEqual(work_claims.work_state(row, later), 'done')
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=('ready', 'mac-a/claude', later.isoformat()), now=later, record=self.record, user='system')
        # A reviewer who disapproves again clears the worker: the icon is open at once.
        again = self.disapprove(later + timedelta(hours=2))
        self.assertIsNone(work_claims.work_state(self.row(), later + timedelta(hours=3)))
        work = work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=again, now=later + timedelta(hours=3), record=self.record, user='system')
        self.assertEqual((work['state'], work['worker']), ('claimed', 'mac-b/claude'))
        self.assertEqual([entry[1] for entry in self.log], ['work_claim', 'work_done', 'review', 'work_claim'])

    def test_expired_claim_goes_back_to_disapproved_and_open(self):
        decision = self.disapprove()
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        fresh = NOW + timedelta(hours=work_claims.LEASE_HOURS, minutes=-1)
        stale = NOW + timedelta(hours=work_claims.LEASE_HOURS, minutes=1)
        self.assertEqual(work_claims.work_state(self.row(), fresh), 'claimed')
        self.assertIsNone(work_claims.work_state(self.row(), stale), 'an expired claim has no work state, never claimed')
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=fresh, record=self.record, user='system')
        with self.assertRaises(work_claims.WorkError):
            work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'done', decision=decision, now=stale, record=self.record, user='system')
        self.assertEqual(work_claims.release_expired(self.connection, fresh, self.record), 0)
        self.assertEqual(work_claims.release_expired(self.connection, stale, self.record), 1)
        row = self.row()
        self.assertEqual((row['status'], row['worker'], row['claimed_at']), ('pending', None, None), 'the review status is Disapproved again')
        self.assertEqual(work_claims.work_field(row, work_claims.work_state(row, stale)), {'state': None})
        self.assertEqual([entry[1] for entry in self.log][-1], 'work_expired')
        # Even without the release, a claim wins over a stale claimed row directly.
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        work = work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=('claimed', 'hina', decision[2]), now=stale, record=self.record, user='system')
        self.assertEqual((work['state'], work['worker'], work['claimed_at']), ('claimed', 'mac-b/claude', stale.isoformat()))

    def test_claim_is_one_conditional_update(self):
        decision = self.disapprove()
        # Someone else wins between the read and the write: the update changes no row and the claim is refused.
        self.connection.execute("UPDATE reviews SET status='claimed', worker='mac-z', claimed_at=? WHERE icon=?", (NOW.isoformat(), ICON))
        with patch.object(work_claims, 'load_row', side_effect=[dict(self.row(), status='pending', worker=None, claimed_at=None), self.row()]):
            with self.assertRaises(work_claims.WorkError) as refused:
                work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual((refused.exception.status, refused.exception.work['worker']), (409, 'mac-z'))

    def test_cannot_fix_needs_a_note_and_blocks_until_redisapproved(self):
        decision = self.disapprove()
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        with self.assertRaises(work_claims.WorkError) as refused:
            work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'cannot-fix', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(refused.exception.status, 400)
        result = work_claims.finish(self.connection, ICON, SHA, 'mac-a/claude', 'cannot-fix', note='needs 5 gaps', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(result['work']['state'], 'cannot-fix')
        self.assertNotIn('status', result)
        self.assertEqual(self.connection.execute('SELECT status, worker, note FROM reviews WHERE icon=?', (ICON,)).fetchone(),
                         ('pending', 'mac-a/claude', 'needs 5 gaps'), 'cannot-fix is not a review status: Disapproved with the worker and note kept')
        catalog = {ICON: {'key': ICON, 'svg_sha256': SHA, 'family': 'sub'}}
        decisions = {ICON: ('pending', 'hina', decision[2])}
        self.assertEqual(work_claims.queue(self.connection, catalog, decisions, {}, NOW)['total'], 0)
        everything = work_claims.queue(self.connection, catalog, decisions, {}, NOW, claimable_only=False)
        self.assertEqual((everything['items'][0]['status'], everything['items'][0]['work']['state']), ('disapprove', 'cannot-fix'))
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-b/claude', decision=decisions[ICON], now=NOW, record=self.record, user='system')
        self.assertEqual(work_claims.abandon(self.connection, ICON, SHA, 'anyone', decision=decisions[ICON], now=NOW, record=self.record, user='system')['work'], {'state': None})
        self.assertEqual(work_claims.queue(self.connection, catalog, decisions, {}, NOW)['total'], 1)

    def test_abandon_reopens_for_anyone(self):
        decision = self.disapprove()
        work_claims.claim(self.connection, ICON, SHA, 'mac-a/claude', decision=decision, now=NOW, record=self.record, user='system')
        result = work_claims.abandon(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(result['work'], {'state': None})
        row = self.row()
        self.assertEqual((row['status'], row['worker'], row['claimed_at']), ('pending', None, None))
        with self.assertRaises(work_claims.WorkError) as refused:
            work_claims.abandon(self.connection, ICON, SHA, 'mac-b/claude', decision=decision, now=NOW, record=self.record, user='system')
        self.assertEqual(refused.exception.status, 409)

    def test_queue_lists_oldest_claimable_disapprovals_with_feedback(self):
        catalog = {'sub/a': {'key': 'sub/a', 'svg_sha256': 'a1', 'family': 'sub', 'category': 'shapes'},
                   'sub/b': {'key': 'sub/b', 'svg_sha256': 'b1', 'family': 'sub', 'category': 'shapes'},
                   'solo/c': {'key': 'solo/c', 'svg_sha256': 'c1', 'family': 'solo', 'category': 'tools'},
                   'solo/d': {'key': 'solo/d', 'svg_sha256': 'd1', 'family': 'solo'}}
        decisions = {'sub/a': ('pending', 'hina', '2026-09-20T10:00:00+00:00'),
                     'sub/b': ('pending', 'ray', '2026-09-19T10:00:00+00:00'),
                     'solo/c': ('pending', 'hina', '2026-09-21T10:00:00+00:00'),
                     'solo/d': ('approve', 'hina', '2026-09-21T10:00:00+00:00')}
        for key, (status, actor, stamp) in decisions.items():
            self.connection.execute('INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?,?,?,?,?)',
                                    (key, catalog[key]['svg_sha256'], status, stamp, actor))
        self.connection.execute("INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reason, author) VALUES ('sub/a','older','a1','t1','other','ray')")
        self.connection.execute("INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reason, author) VALUES ('sub/a','Round the corners','a1','t2','bad-stroke','hina')")
        work_claims.claim(self.connection, 'solo/c', 'c1', 'mac-a/claude', decision=decisions['solo/c'], now=NOW, record=self.record, user='system')
        decisions['solo/c'] = ('claimed', 'hina', decisions['solo/c'][2])
        page = work_claims.queue(self.connection, catalog, decisions, {}, NOW)
        self.assertEqual([item['key'] for item in page['items']], ['sub/b', 'sub/a'])
        self.assertEqual(page['items'][1]['feedback'], 'Round the corners')
        self.assertEqual(page['items'][1]['reason'], 'bad-stroke')
        self.assertEqual(page['items'][1]['status'], 'disapprove')
        self.assertEqual(page['items'][1]['work'], {'state': None})
        self.assertEqual(work_claims.queue(self.connection, catalog, decisions, {'family': ['solo']}, NOW)['total'], 0)
        self.assertEqual([item['key'] for item in work_claims.queue(self.connection, catalog, decisions, {'reason': ['bad-stroke']}, NOW)['items']], ['sub/a'])
        self.assertEqual(work_claims.review_listing(self.connection, catalog, decisions, {'reason': ['bad-stroke']}, NOW)['total'], 1)
        everything = work_claims.queue(self.connection, catalog, decisions, {}, NOW, claimable_only=False)
        self.assertEqual([(item['key'], item['status'], item['work']['state']) for item in everything['items']],
                         [('sub/b', 'disapprove', None), ('sub/a', 'disapprove', None), ('solo/c', 'claimed', 'claimed')])
        paged = work_claims.queue(self.connection, catalog, decisions, {'limit': ['1']}, NOW)
        self.assertEqual((paged['total'], paged['next_offset'], paged['items'][0]['key']), (2, 1, 'sub/b'))
        rows = work_claims.listing(self.connection, catalog, decisions, NOW)['claims']
        self.assertEqual([(row['icon'], row['state'], row['current'], row['status']) for row in rows], [('solo/c', 'claimed', True, 'claimed')])
        review = work_claims.review_listing(self.connection, catalog, decisions, {}, NOW)
        self.assertEqual(review['counts'], {'unclaimed': 2, 'claimed': 1})
        self.assertEqual(review['items'][0]['key'], 'solo/c', 'most recent work first')
        # A deployed fix changes the hash: the new revision starts Ready with no row and leaves the listing.
        catalog['solo/c']['svg_sha256'] = 'c2'
        decisions['solo/c'] = ('ready', None, None)
        self.assertEqual(work_claims.listing(self.connection, catalog, decisions, NOW)['claims'], [])
        review = work_claims.review_listing(self.connection, catalog, decisions, {}, NOW)
        self.assertEqual({item['key']: item['work']['state'] for item in review['items']}, {'sub/a': None, 'sub/b': None})
        history = work_claims.history(self.connection, catalog, decisions, 'solo/c', NOW)
        self.assertEqual([(rev['svg_sha256'], rev['current'], (rev['claim'] or {}).get('worker')) for rev in history['revisions']],
                         [('c1', False, 'mac-a/claude'), ('c2', True, None)])

    def test_worker_validation(self):
        decision = self.disapprove()
        for bad in ('', ' ', 'x' * 121, 'a\nb', None, 3):
            with self.assertRaises(work_claims.WorkError):
                work_claims.claim(self.connection, ICON, SHA, bad, decision=decision, now=NOW, record=self.record, user='system')
        with self.assertRaises(work_claims.WorkError):
            work_claims.claim(self.connection, ICON, SHA, 'mac-a', decision=('ready', None, None), now=NOW, record=self.record, user='system')


class MigrationTests(unittest.TestCase):
    def test_legacy_claims_and_snapshots_fold_into_the_review_rows(self):
        connection = sqlite3.connect(':memory:')
        connection.execute('''CREATE TABLE reviews (icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL, status TEXT NOT NULL,
            updated_at TEXT NOT NULL, updated_by TEXT, PRIMARY KEY(icon, svg_sha256))''')
        connection.execute('''CREATE TABLE work_claims (icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL, state TEXT NOT NULL,
            worker TEXT NOT NULL, note TEXT NOT NULL DEFAULT '', claimed_at TEXT NOT NULL, updated_at TEXT NOT NULL, expires_at TEXT,
            PRIMARY KEY(icon, svg_sha256))''')
        connection.execute('''CREATE TABLE work_snapshots (icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL, svg TEXT NOT NULL,
            saved_at TEXT NOT NULL, PRIMARY KEY(icon, svg_sha256))''')
        t0, t1, t2 = '2026-09-23T06:00:00+00:00', '2026-09-23T07:00:00+00:00', '2026-09-23T08:00:00+00:00'
        connection.executemany('INSERT INTO reviews VALUES (?,?,?,?,?)', [
            ('solo/a', 'a1', 'pending', t0, 'hina'), ('solo/b', 'b1', 'pending', t0, 'hina'),
            ('solo/c', 'c1', 'ready', t1, 'thuan-mac'), ('solo/d', 'd1', 'pending', t2, 'hina')])
        connection.executemany('INSERT INTO work_claims VALUES (?,?,?,?,?,?,?,?)', [
            ('solo/a', 'a1', 'working', 'thuan-mac', '', t1, t1, t2),
            ('solo/b', 'b1', 'cannot-fix', 'thuan-mac', 'MIC impossible', t1, t1, None),
            ('solo/c', 'c1', 'done', 'thuan-mac', 'v2', t0, t1, None),
            ('solo/d', 'd1', 'cannot-fix', 'thuan-mac', 'old verdict', t0, t1, None)])  # disapproved again after the report
        connection.execute("INSERT INTO work_snapshots VALUES ('solo/a', 'a1', '<svg/>', ?)", (t1,))
        work_claims.init_work_claims(connection)
        rows = {key: (row['status'], row['worker'], row['claimed_at'], row['note']) for key, row in
                ((k[0], r) for k, r in work_claims.load_rows(connection).items())}
        self.assertEqual(rows, {'solo/a': ('claimed', 'thuan-mac', t1, ''),
                                'solo/b': ('pending', 'thuan-mac', t1, 'MIC impossible'),
                                'solo/c': ('ready', 'thuan-mac', t0, 'v2'),
                                'solo/d': ('pending', None, None, '')})
        self.assertEqual(work_claims.work_state(work_claims.load_row(connection, 'solo/b', 'b1'), NOW), 'cannot-fix')
        self.assertEqual(work_claims.load_result(connection, 'solo/a', 'a1', 'before')['svg'], '<svg/>')
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        self.assertNotIn('work_claims', tables)
        self.assertNotIn('work_snapshots', tables)
        work_claims.init_work_claims(connection)  # idempotent


def init_database_tables(connection):
    connection.execute(REVIEWS_TABLE)
    connection.execute('''CREATE TABLE feedback (id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL,
        svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL, reason TEXT NOT NULL DEFAULT 'other', author TEXT,
        edited_by TEXT, edited_at TEXT)''')
    connection.execute("CREATE TABLE icon_types (icon TEXT PRIMARY KEY, icon_type TEXT NOT NULL)")
    connection.execute('''CREATE TABLE activity_log (id INTEGER PRIMARY KEY, username TEXT NOT NULL, action TEXT NOT NULL,
        icon TEXT, details TEXT NOT NULL DEFAULT '{}', created_at TEXT NOT NULL)''')
    work_claims.init_work_claims(connection)


class ServerBase(unittest.TestCase):
    def start(self, folder, production, sync_source=None, *, family='sub', folder_name='sub32', names=('square',),
              canvas=None, svg=None):
        dist = folder / 'dist'
        dist.mkdir()
        if svg is None and names == ('square',) and family == 'sub':
            manifest(dist, family, folder_name, 'square')
        else:
            directory = dist / folder_name
            directory.mkdir(parents=True, exist_ok=True)
            rows = [{'family': family, 'icon_id': name, 'name': name, 'svg_sha256': 'abc'} for name in names]
            if canvas:
                for row in rows:
                    row['canvas_size'] = canvas
            (directory / 'manifest.json').write_text(json.dumps({'icons': rows}))
            for name in names:
                (directory / (name + '.svg')).write_text(svg or '<svg xmlns="http://www.w3.org/2000/svg"/>')
        # The fixture must not depend on the live icon registry.
        with patch('icon_set.model.icons.registry.factories', return_value={}), \
                patch('icon_set.scripts.symbol_family.stage', side_effect=lambda target, records: records):
            stage_gallery(dist, dist, [folder_name])
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
        self.assertEqual((body['work']['state'], body['item']['key'], body['item']['reason']), ('claimed', ICON, 'bad-stroke'))
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', dict(claim, worker='mac-b/claude'))
        self.assertEqual((status, body['work']['worker']), (409, 'mac-a/claude'))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/queue')[1]['total'], 0)
        everything = self.request(self.server, 'GET', '/api/work/disapproved')[1]
        self.assertEqual((everything['total'], everything['items'][0]['status'], everything['items'][0]['work']['state']), (1, 'claimed', 'claimed'))
        status, body, _ = self.request(self.server, 'GET', '/api/work?icon=' + ICON)
        self.assertEqual((status, body['status'], body['work']['state']), (200, 'claimed', 'claimed'))
        self.assertEqual(self.request(self.server, 'GET', '/api/reviews')[1][ICON], 'claimed', 'the claim is the review status')
        self.request(self.server, 'POST', '/api/icon-type', {'icon': ICON, 'icon_type': 'avatar'}, self.cookie)
        status, body, _ = self.request(self.server, 'GET', '/api/icon-types?status=claimed')
        self.assertEqual(body['icons'][0]['work']['state'], 'claimed')
        # More feedback while a worker is on it keeps the claim.
        self.disapprove('Also the top bar')
        self.assertEqual(self.request(self.server, 'GET', '/api/work?icon=' + ICON)[1]['work']['worker'], 'mac-a/claude')
        detail = self.request(self.server, 'GET', '/api/review-detail?icon=' + ICON)[1]
        self.assertEqual(detail['work']['worker'], 'mac-a/claude')
        status, body, _ = self.request(self.server, 'POST', '/api/work/done', dict(claim, worker='mac-b/claude'))
        self.assertEqual(status, 409)
        status, body, _ = self.request(self.server, 'POST', '/api/work/done', dict(claim, note='sub/square-v2'))
        self.assertEqual((status, body['status'], body['work']['state']), (200, 'ready', 'done'), body)
        self.assertEqual(self.request(self.server, 'GET', '/api/reviews')[1][ICON], 'ready')
        feedback = self.request(self.server, 'GET', '/api/feedback?icon=' + ICON)[1]
        self.assertEqual(len(feedback), 2, 'the disapproval feedback stays for the reviewer')
        self.assertEqual(self.request(self.server, 'GET', '/api/work/queue')[1]['total'], 0)
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', dict(claim, worker='mac-b/claude'))
        self.assertEqual(status, 409, 'Ready icons are not claimable')
        self.disapprove('Still crooked')
        status, body, _ = self.request(self.server, 'GET', '/api/work/queue')
        self.assertEqual((body['total'], body['items'][0]['work']['state']), (1, None))
        status, body, _ = self.request(self.server, 'POST', '/api/work/claim', dict(claim, worker='mac-b/claude'))
        self.assertEqual((status, body['work']['worker']), (201, 'mac-b/claude'))
        listing = self.request(self.server, 'GET', '/api/work')[1]['claims']
        self.assertEqual([(row['icon'], row['worker'], row['state']) for row in listing], [(ICON, 'mac-b/claude', 'claimed')])
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

    def test_review_listing_and_history(self):
        self.disapprove()
        claim = {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a/claude'}
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', claim)[0], 201)
        listing = self.request(self.server, 'GET', '/api/work/review')[1]
        self.assertEqual((listing['total'], listing['counts'], listing['items'][0]['work']['results']), (1, {'claimed': 1}, []))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/snapshot?icon=' + ICON + '&svg_sha256=' + SHA)[0], 404, 'snapshots are gone')
        self.assertEqual(self.request(self.server, 'POST', '/api/work/heartbeat', claim)[0], 404, 'no heartbeat: the lease is claimed_at + LEASE_HOURS')
        self.assertEqual(self.request(self.server, 'POST', '/api/work/done', dict(claim, note='sub/square-v2'))[0], 200)
        listing = self.request(self.server, 'GET', '/api/work/review?state=done')[1]
        self.assertEqual((listing['total'], listing['items'][0]['status'], listing['items'][0]['work']['state']), (1, 'ready', 'done'))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/disapproved')[1]['total'], 0, 'Ready icons leave the disapproved list')
        history = self.request(self.server, 'GET', '/api/work/history?icon=' + ICON)[1]
        self.assertEqual((history['current']['status'], history['current']['work']['state']), ('ready', 'done'))
        self.assertEqual(len(history['revisions']), 1)
        revision = history['revisions'][0]
        self.assertTrue(revision['current'])
        self.assertEqual((revision['claim']['worker'], revision['review']['status'], len(revision['feedback'])), ('mac-a/claude', 'ready', 1))
        self.assertEqual([event['action'] for event in history['events']], ['feedback', 'work_claim', 'work_done', 'review'])
        self.assertEqual(self.request(self.server, 'GET', '/api/work/history?icon=sub/missing')[0], 404)
        # The reviewer approves the fixed revision: the worker columns are cleared with the decision.
        status, body, _ = self.request(self.server, 'POST', '/api/reviews', {'icon': ICON, 'svg_sha256': SHA, 'status': 'approve'}, self.cookie)
        self.assertEqual(status, 201, body)
        self.assertEqual(self.request(self.server, 'GET', '/api/work?icon=' + ICON)[1]['work'], {'state': None})
        self.assertEqual(self.request(self.server, 'GET', '/api/work/review')[1]['total'], 0)

    def test_abandon_by_anyone_and_reviewer_redisapproval(self):
        self.disapprove()
        claim = {'icon': ICON, 'svg_sha256': SHA, 'worker': 'mac-a/claude'}
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', claim)[0], 201)
        status, body, _ = self.request(self.server, 'POST', '/api/work/abandon', dict(claim, worker='mac-b'))
        self.assertEqual((status, body['work']['state']), (200, None))
        self.assertEqual(self.request(self.server, 'GET', '/api/work/queue')[1]['total'], 1)
        self.assertEqual(self.request(self.server, 'POST', '/api/work/claim', claim)[0], 201)
        # A reviewer's explicit Disapprove on a claimed icon takes it back: the worker is cleared.
        status, body, _ = self.request(self.server, 'POST', '/api/reviews', {'icon': ICON, 'svg_sha256': SHA, 'status': 'disapprove'}, self.cookie)
        self.assertEqual(status, 201, body)
        self.assertEqual(self.request(self.server, 'GET', '/api/work?icon=' + ICON)[1]['work'], {'state': None})
        with closing(sqlite3.connect(self.database)) as connection:
            self.assertEqual(connection.execute('SELECT status, worker FROM reviews WHERE icon=?', (ICON,)).fetchone(), ('pending', None))


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
        self.assertEqual((status, body['work']['state']), (201, 'claimed'))
        status, body, _ = self.request(development, 'POST', '/api/work/claim', dict(claim, worker='mac-b'))
        self.assertEqual((status, body['work']['worker']), (409, 'mac-a/claude'))
        with closing(sqlite3.connect(development_db)) as connection:
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM reviews WHERE status='claimed'").fetchone()[0], 0)
        with closing(sqlite3.connect(production_db)) as connection:
            self.assertEqual(connection.execute("SELECT worker FROM reviews WHERE status='claimed'").fetchone()[0], 'mac-a/claude')
        self.assertEqual(self.request(development, 'GET', '/api/work')[1]['claims'][0]['worker'], 'mac-a/claude')
        self.assertEqual(self.request(development, 'GET', '/api/work/history?icon=' + ICON)[1]['current']['work']['state'], 'claimed')
        detail = self.request(development, 'GET', '/api/review-detail?icon=' + ICON)[1]
        self.assertEqual(detail['work']['state'], 'claimed')
        production.shutdown()
        production.server_close()
        development.work_cache = None
        status, body, _ = self.request(development, 'POST', '/api/work/abandon', claim)
        self.assertEqual(status, 502)
        self.assertIn('unreachable', body['error'])
        detail = self.request(development, 'GET', '/api/review-detail?icon=' + ICON)[1]
        self.assertEqual(detail['work']['state'], 'unknown')


if __name__ == '__main__':
    unittest.main()
