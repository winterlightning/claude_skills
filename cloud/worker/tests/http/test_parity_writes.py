"""Write-route parity: the same actions against the Python server and the Worker give the same answers.

Run against scratch data only (the old server on a database COPY, the Worker on local D1):

    PICTOGRAPHIC_OLD=http://127.0.0.1:8799 PICTOGRAPHIC_NEW=http://127.0.0.1:8787 \\
        python3 -m pytest cloud/worker/tests/http -q

Timestamps, generated ids and hashes of new uploads are masked before comparing.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import http.cookiejar
import json
import os
import re
import urllib.error
import urllib.request

import pytest

OLD = os.environ.get('PICTOGRAPHIC_OLD', 'http://127.0.0.1:8799')
NEW = os.environ.get('PICTOGRAPHIC_NEW', 'http://127.0.0.1:8787')
STAMP = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(\+00:00|Z)?')
SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path d="M8 8L40 40" stroke="currentColor" '
       'stroke-width="4" fill="none"/></svg>')


class Client:
    def __init__(self, base: str):
        self.base = base
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(self, method: str, path: str, body=None, headers=None, raw: bytes | None = None):
        data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
        request = urllib.request.Request(self.base + path, data=data, method=method,
                                         headers={'Content-Type': 'application/json', 'User-Agent': 'pictographic-verify/1.0',
                                                  **(headers or {})})
        try:
            with self.opener.open(request, timeout=300) as response:
                status, content = response.status, response.read()
        except urllib.error.HTTPError as error:
            status, content = error.code, error.read()
        try:
            return status, json.loads(content)
        except ValueError:
            return status, content.decode('utf-8', 'replace')

    def get(self, path):
        return self.call('GET', path)

    def post(self, path, body, **kwargs):
        return self.call('POST', path, body, **kwargs)


def mask(value):
    """Hide values that legitimately differ between two runs."""
    if isinstance(value, dict):
        return {k: ('<id>' if k in ('id', 'feedback_id', 'split_id') and isinstance(v, int) else mask(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [mask(v) for v in value]
    if isinstance(value, str):
        value = STAMP.sub('<time>', value)
        return re.sub(r'upload-[0-9a-f]{16}', 'upload-<hex>', value)
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


@pytest.fixture(scope='module')
def clients():
    for base in (OLD, NEW):
        try:
            urllib.request.urlopen(urllib.request.Request(base + '/api/runtime', headers={'User-Agent': 'pictographic-verify/1.0'}), timeout=10)
        except OSError:
            pytest.skip(f'{base} is not running')
    return Client(OLD), Client(NEW)


def pick(client: Client):
    """Stable test subjects from the shared starting data."""
    queue = client.get('/api/work/queue?limit=20')[1]['items']
    reviews = client.get('/api/reviews')[1]
    ready = [k for k, s in reviews.items() if s == 'ready' and k.startswith('solo/')]
    approved = [k for k, s in reviews.items() if s == 'approve' and k.startswith('solo/')]
    return queue, ready, approved


def sha_of(client: Client, key: str) -> str:
    return client.get(f'/api/work?icon={key}')[1]['svg_sha256']


def scenario(client: Client, subjects) -> list:
    queue, ready, approved = subjects
    log = []

    def step(name, result):
        log.append((name, result[0], mask(result[1])))
        return result

    step('session before', client.get('/api/auth/session'))
    step('bad login', client.post('/api/auth/login', {'username': 'ray', 'password': 'wrong'}))
    step('login', client.post('/api/auth/login', {'username': 'ray', 'password': '1'}))
    step('session after', client.get('/api/auth/session'))

    a, b = ready[0], ready[1]
    step('approve', client.post('/api/reviews', {'icon': a, 'svg_sha256': sha_of(client, a), 'status': 'approve'}))
    step('stale sha', client.post('/api/reviews', {'icon': a, 'svg_sha256': 'x', 'status': 'ready'}))
    step('unknown icon', client.post('/api/reviews', {'icon': 'solo/nope', 'svg_sha256': '', 'status': 'ready'}))
    step('bad status', client.post('/api/reviews', {'icon': a, 'svg_sha256': sha_of(client, a), 'status': 'maybe'}))
    step('disapprove needs reason', client.post('/api/reviews', {'icon': b, 'svg_sha256': sha_of(client, b), 'status': 'disapprove',
                                                                 'reason': 'other', 'feedback': ' '}))
    status, created = step('disapprove with feedback', client.post('/api/reviews', {
        'icon': b, 'svg_sha256': sha_of(client, b), 'status': 'disapprove', 'reason': 'bad-stroke', 'feedback': 'thin stroke'}))
    feedback = client.get(f'/api/feedback?icon={b}')[1]
    step('feedback list', (200, feedback))
    entry = feedback[0]
    step('edit feedback stale', client.post('/api/feedback/edit', {'id': entry['id'], 'feedback': 'x', 'previous_feedback': 'wrong'}))
    step('edit feedback', client.post('/api/feedback/edit', {'id': entry['id'], 'feedback': 'thicker please',
                                                             'previous_feedback': entry['feedback']}))
    edited = client.get(f'/api/feedback?icon={b}')[1][0]
    step('delete feedback', client.post('/api/feedback/delete', {'id': edited['id'], 'previous_feedback': edited['feedback'],
                                                                 'previous_edited_at': edited['edited_at']}))
    step('back to ready clears feedback', client.post('/api/reviews', {'icon': b, 'svg_sha256': sha_of(client, b), 'status': 'ready'}))
    step('detail', client.get(f'/api/review-detail?icon={b}'))

    step('flag', client.post('/api/icon-flag', {'icon': a, 'flag': 'text'}))
    step('bad flag', client.post('/api/icon-flag', {'icon': a, 'flag': 'purple'}))
    step('unflag', client.post('/api/icon-flag', {'icon': a, 'flag': ''}))
    step('type', client.post('/api/icon-type', {'icon': a, 'icon_type': '  avatar  '}))
    step('type read', client.get(f'/api/icon-type?icon={a}'))

    if queue:
        c = queue[0]
        claim = {'icon': c['key'], 'svg_sha256': c['svg_sha256'], 'worker': 'parity-worker'}
        step('claim', client.post('/api/work/claim', claim))
        step('claim again', client.post('/api/work/claim', claim))
        step('claim other', client.post('/api/work/claim', dict(claim, worker='someone-else')))
        step('result bad svg', client.post('/api/work/result', dict(claim, stage='before', svg='<svg/>')))
        step('result', client.post('/api/work/result', dict(claim, stage='before', svg=SVG, note='as found')))
        step('result read', client.get(f"/api/work/result?icon={c['key']}&svg_sha256={c['svg_sha256']}&stage=before"))
        step('cannot-fix needs note', client.post('/api/work/cannot-fix', dict(claim, note='')))
        step('done', client.post('/api/work/done', dict(claim, note='fixed')))
        step('abandon done', client.post('/api/work/abandon', claim))
        step('history', client.get(f"/api/work/history?icon={c['key']}"))
        if len(queue) > 2:
            step('claim many', client.post('/api/work/claim', {'worker': 'parity-worker', 'icons': [
                queue[1]['key'], {'icon': queue[2]['key'], 'svg_sha256': 'stale'}, queue[1]['key'], 5]}))
            step('abandon', client.post('/api/work/abandon', {'icon': queue[1]['key'], 'svg_sha256': queue[1]['svg_sha256'],
                                                              'worker': 'another'}))

    primitives = client.get('/api/primitives?status=todo')[1] + client.get('/api/primitives?status=drawn')[1]
    if primitives:
        uid = primitives[0]['uuid']
        step('skip', client.post('/api/primitives/status', {'uuids': [uid], 'status': 'skip', 'reason': 'container',
                                                             'main_brief': {'family': 'container', 'name': 'Shield', 'description': 'A shield'}}))
        step('skip same', client.post('/api/primitives/status', {'uuids': [uid], 'status': 'skip', 'reason': 'container'}))
        step('skip other needs note', client.post('/api/primitives/status', {'uuids': [uid], 'status': 'skip', 'reason': 'other'}))
        step('todo', client.post('/api/primitives/status', {'uuids': [uid.upper()], 'status': 'todo'}))
        step('brief', client.post('/api/primitives/briefs', {'uuid': uid, 'family': 'solo', 'brief': 'Draw a shield.'}))
        step('bad symbol link', client.post('/api/primitives/symbol-link', {'uuid': uid, 'icon': a}))
        step('status read', client.get('/api/primitives/summary'))

    split = {'icon': a, 'svg_sha256': sha_of(client, a), 'combination_type': 'side', 'reason': 'two things',
             'components': [{'name': 'Monitor', 'family': 'solo', 'description': 'screen'},
                            {'name': 'Cloud', 'family': 'sub', 'description': 'badge'}]}
    step('reject combination', client.post('/api/reject-combination', split))
    step('reject again', client.post('/api/reject-combination', split))
    step('review rejected', client.post('/api/reviews', {'icon': a, 'svg_sha256': sha_of(client, a), 'status': 'approve'}))
    step('briefs', client.get('/api/pending-briefs'))
    step('restore', client.post('/api/reject-combination/restore', {'icon': a, 'svg_sha256': sha_of(client, a)}))

    step('family', client.post('/api/icon-families', {'id': 'parity-family', 'name': 'Parity', 'canvas_size': 48}))
    step('family again', client.post('/api/icon-families', {'id': 'parity-family', 'name': 'Parity', 'canvas_size': 48}))
    step('upload bad svg', client.post('/api/icons/upload', {'name': 'x', 'family': 'solo', 'svg': '<svg><script/></svg>'}))
    step('upload wrong canvas', client.post('/api/icons/upload', {'name': 'x', 'family': 'sub', 'svg': SVG}))

    step('cross origin', client.post('/api/reviews', {}, headers={'Origin': 'https://evil.example'}))
    step('not json', client.call('POST', '/api/reviews', raw=b'x=1', headers={'Content-Type': 'application/x-www-form-urlencoded'}))
    step('too large', client.call('POST', '/api/reviews', raw=b'{"a":"' + b'x' * 70000 + b'"}'))
    step('unknown route', client.post('/api/nope', {}))
    step('logout', client.post('/api/auth/logout', {}))
    step('session end', client.get('/api/auth/session'))
    return log


def test_same_answers_for_same_writes(clients):
    old, new = clients
    subjects = pick(old)
    assert mask(subjects) == mask(pick(new)), 'the two servers must start from the same data'
    old_log, new_log = scenario(old, subjects), scenario(new, subjects)
    print('\n' + ' | '.join(f'{name}:{status}' for name, status, _ in new_log))
    differences = [(o[0], o[1:], n[1:]) for o, n in zip(old_log, new_log) if o != n]
    assert not differences, json.dumps(differences[:5], indent=1)[:4000]


def test_only_one_concurrent_claim_wins(clients):
    _, new = clients
    queue = new.get('/api/work/queue?limit=50')[1]['items']
    if not queue:
        pytest.skip('no claimable icon')
    item = queue[-1]

    def claim(worker):
        return Client(NEW).post('/api/work/claim', {'icon': item['key'], 'svg_sha256': item['svg_sha256'], 'worker': worker})[0]

    with ThreadPoolExecutor(max_workers=8) as pool:
        statuses = list(pool.map(claim, [f'racer-{n}' for n in range(8)]))
    assert statuses.count(201) == 1, statuses
    assert set(statuses) <= {201, 409}, statuses
    holder = new.get(f"/api/work?icon={item['key']}")[1]['work']
    assert holder['state'] == 'working' and holder['worker'].startswith('racer-')
    new.post('/api/work/abandon', {'icon': item['key'], 'svg_sha256': item['svg_sha256'], 'worker': 'cleanup'})
