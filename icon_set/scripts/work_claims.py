"""Who is fixing which disapproved icon: claims with a lease, kept in the review database.

The review status stays what the gallery shows (ready / pending=disapprove /
approve / rejected). A claim row adds a *work* state for one icon revision:

    working     a machine holds the lease and is fixing this revision
    done        the fix was reported; the revision was returned to Ready
    cannot-fix  the worker gave up with a note; skipped until disapproved again

A claim belongs to the (icon, svg_sha256) pair it was made for. A deployed fix
changes the hash, so the old claim becomes history and the new revision starts
Ready without a row. A reviewer who disapproves the same revision again after a
report makes the icon claimable once more: the review timestamp is newer than
the claim. Working claims expire after LEASE_HOURS unless refreshed.

Every function takes an open connection and ``now`` so it can be tested without
HTTP. Only production keeps this table; development servers forward to it.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import re

LEASE_HOURS = 3
MIN_LEASE_HOURS, MAX_LEASE_HOURS = 1, 24
STATES = ('working', 'done', 'cannot-fix')
CLAIMABLE = ('open', 'expired')
MAX_WORKER = 120
MAX_NOTE = 4000
MAX_QUEUE = 500
_WORKER = re.compile(r'^[^\x00-\x1f\x7f]{1,%d}$' % MAX_WORKER)


class WorkError(ValueError):
    """A refused transition; ``status`` is the HTTP code and ``work`` the current state."""

    def __init__(self, message, status=409, work=None):
        super().__init__(message)
        self.status, self.work = status, work


def init_work_claims(connection) -> None:
    connection.execute('''CREATE TABLE IF NOT EXISTS work_claims (
        icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
        state TEXT NOT NULL CHECK(state IN ('working','done','cannot-fix')),
        worker TEXT NOT NULL, note TEXT NOT NULL DEFAULT '',
        claimed_at TEXT NOT NULL, updated_at TEXT NOT NULL, expires_at TEXT,
        PRIMARY KEY(icon, svg_sha256))''')


def parse_time(stamp):
    if not stamp:
        return None
    try:
        when = datetime.fromisoformat(str(stamp).replace('Z', '+00:00'))
    except ValueError:
        return None
    return when if when.tzinfo else when.replace(tzinfo=timezone.utc)


def validate_worker(worker) -> str:
    if not isinstance(worker, str) or not _WORKER.match(worker.strip()):
        raise WorkError(f'worker must be a name of 1-{MAX_WORKER} characters, e.g. "hostname/agent".', 400)
    return worker.strip()


def validate_note(note, required=False) -> str:
    if note is None:
        note = ''
    if not isinstance(note, str) or len(note) > MAX_NOTE:
        raise WorkError(f'note must be a string of at most {MAX_NOTE} characters.', 400)
    if required and not note.strip():
        raise WorkError('A note explaining why the icon cannot be fixed is required.', 400)
    return note.strip()


def validate_lease(hours) -> int:
    if hours is None:
        return LEASE_HOURS
    if type(hours) is not int or not MIN_LEASE_HOURS <= hours <= MAX_LEASE_HOURS:
        raise WorkError(f'lease_hours must be an integer from {MIN_LEASE_HOURS} to {MAX_LEASE_HOURS}.', 400)
    return hours


def load_claim(connection, key, sha):
    row = connection.execute('SELECT icon, svg_sha256, state, worker, note, claimed_at, updated_at, expires_at '
                             'FROM work_claims WHERE icon=? AND svg_sha256=?', (key, sha)).fetchone()
    return _row(row) if row else None


def load_claims(connection) -> dict:
    """(icon, sha) -> claim row for every saved claim."""
    return {(row[0], row[1]): _row(row) for row in connection.execute(
        'SELECT icon, svg_sha256, state, worker, note, claimed_at, updated_at, expires_at FROM work_claims')}


def _row(row):
    return dict(zip(('icon', 'svg_sha256', 'state', 'worker', 'note', 'claimed_at', 'updated_at', 'expires_at'), row))


def work_state(claim, review_updated_at, now) -> str:
    """The effective state of one revision's claim, as the queue and the API report it."""
    if not claim:
        return 'open'
    if claim['state'] == 'working':
        expires = parse_time(claim['expires_at'])
        return 'working' if expires and expires > now else 'expired'
    decided, reported = parse_time(review_updated_at), parse_time(claim['updated_at'])
    if decided and reported and decided > reported:
        return 'open'  # disapproved again after the report
    return claim['state']


def work_field(claim, state) -> dict:
    """What the API returns under ``work``."""
    field = {'state': state}
    if claim:
        field.update(worker=claim['worker'], note=claim['note'], claimed_at=claim['claimed_at'],
                     updated_at=claim['updated_at'], expires_at=claim['expires_at'], svg_sha256=claim['svg_sha256'])
    return field


def latest_feedback(connection) -> dict:
    """(icon, sha) -> the newest feedback entry for that revision."""
    latest = {}
    for icon, sha, reason, feedback, author, created_at in connection.execute(
            'SELECT icon, svg_sha256, reason, feedback, author, created_at FROM feedback ORDER BY id'):
        latest[(icon, sha)] = {'reason': reason, 'feedback': feedback, 'feedback_by': author, 'feedback_at': created_at}
    return latest


def icon_types(connection) -> dict:
    return dict(connection.execute("SELECT icon, icon_type FROM icon_types WHERE icon_type != ''").fetchall())


def queue_item(icon, decision, feedback, claim, state) -> dict:
    status, actor, stamp = decision
    source = icon.get('python_source')
    return {
        'key': icon['key'], 'icon_id': icon.get('icon_id'), 'name': icon.get('name'),
        'family': icon.get('family'), 'category': icon.get('category'),
        'svg_sha256': icon.get('svg_sha256'), 'python_source': source,
        'preview_url': icon.get('preview_url'), 'original_sources': icon.get('original_sources') or [],
        'status': 'disapprove' if status == 'pending' else status,
        'disapproved_by': actor, 'disapproved_at': stamp,
        'reason': (feedback or {}).get('reason'), 'feedback': (feedback or {}).get('feedback'),
        'feedback_by': (feedback or {}).get('feedback_by'),
        'icon_type': icon.get('icon_type'), 'work': work_field(claim, state),
    }


def queue(connection, catalog, decisions, query, now, *, claimable_only=True) -> dict:
    """Disapproved icons, oldest disapproval first: claimable ones, or all of them with their work state."""
    one = lambda name: (query.get(name) or [None])[0]  # noqa: E731
    try:
        limit = int(one('limit') or 50)
        offset = int(one('offset') or 0)
    except ValueError:
        raise WorkError('limit and offset must be integers.', 400)
    if not 1 <= limit <= MAX_QUEUE or offset < 0:
        raise WorkError(f'limit must be 1-{MAX_QUEUE} and offset nonnegative.', 400)
    family, category, wanted_type = one('family'), one('category'), one('type')
    claims, feedback, types = load_claims(connection), latest_feedback(connection), icon_types(connection)
    rows = []
    for key, decision in decisions.items():
        status, _, stamp = decision
        if status not in ('pending', 'disapprove'):
            continue
        icon = dict(catalog[key], icon_type=types.get(key))
        if family and icon.get('family') != family:
            continue
        if category and icon.get('category') != category:
            continue
        if wanted_type and icon.get('icon_type') != wanted_type:
            continue
        sha = icon.get('svg_sha256') or ''
        claim = claims.get((key, sha))
        state = work_state(claim, stamp, now)
        if claimable_only and state not in CLAIMABLE:
            continue
        rows.append(queue_item(icon, decision, feedback.get((key, sha)), claim, state))
    rows.sort(key=lambda item: (item['disapproved_at'] or '', item['key']))
    page = rows[offset:offset + limit]
    return {'total': len(rows), 'offset': offset,
            'next_offset': offset + limit if offset + limit < len(rows) else None, 'items': page}


def listing(connection, catalog, decisions, now) -> dict:
    """Every saved claim, joined to the current catalog for the review grid."""
    result = []
    for (key, sha), claim in sorted(load_claims(connection).items()):
        icon = catalog.get(key)
        current = bool(icon) and (icon.get('svg_sha256') or '') == sha
        decision = decisions.get(key) if current else None
        status = decision[0] if decision else None
        state = work_state(claim, decision[2] if decision else None, now) if current else 'superseded'
        result.append(dict(work_field(claim, state), icon=key, current=current,
                           status='disapprove' if status == 'pending' else status))
    return {'claims': result}


def _current(connection, key, sha, decision, now):
    """The claim and its effective state for an icon revision; the review row is the reference time."""
    claim = load_claim(connection, key, sha)
    stamp = decision[2] if decision else None
    return claim, work_state(claim, stamp, now)


def claim(connection, key, sha, worker, *, decision, now, record, user, lease_hours=None) -> dict:
    """disapprove + open/expired -> working. Runs inside the caller's write transaction."""
    worker, hours = validate_worker(worker), validate_lease(lease_hours)
    status = decision[0] if decision else 'ready'
    existing, state = _current(connection, key, sha, decision, now)
    if status not in ('pending', 'disapprove'):
        label = 'disapprove' if status == 'pending' else str(status)
        raise WorkError(f'Only disapproved icons can be claimed; this revision is {label}.', 409,
                        work_field(existing, state))
    if state not in CLAIMABLE:
        if state == 'working' and existing['worker'] == worker:
            raise WorkError('You already hold this claim; send a heartbeat to extend it.', 409, work_field(existing, state))
        message = {'working': f'{existing["worker"]} is working on this icon.',
                   'done': f'{existing["worker"]} already fixed this revision; it is waiting for review.',
                   'cannot-fix': f'{existing["worker"]} reported this revision cannot be fixed.'}[state]
        raise WorkError(message, 409, work_field(existing, state))
    stamp = now.isoformat()
    expires = (now + timedelta(hours=hours)).isoformat()
    if existing and state == 'expired':
        record(connection, user, 'work_expired', key, svg_sha256=sha, worker=existing['worker'],
               expired_at=existing['expires_at'], taken_by=worker)
    connection.execute('''INSERT INTO work_claims(icon, svg_sha256, state, worker, note, claimed_at, updated_at, expires_at)
        VALUES (?, ?, 'working', ?, '', ?, ?, ?)
        ON CONFLICT(icon, svg_sha256) DO UPDATE SET state='working', worker=excluded.worker, note='',
        claimed_at=excluded.claimed_at, updated_at=excluded.updated_at, expires_at=excluded.expires_at''',
                       (key, sha, worker, stamp, stamp, expires))
    record(connection, user, 'work_claim', key, svg_sha256=sha, worker=worker, expires_at=expires, lease_hours=hours)
    return work_field(load_claim(connection, key, sha), 'working')


def _own_working(connection, key, sha, worker, decision, now, verb):
    existing, state = _current(connection, key, sha, decision, now)
    if not existing or state != 'working':
        raise WorkError(f'No active claim to {verb}; this revision is {state}.', 409, work_field(existing, state))
    if existing['worker'] != worker:
        raise WorkError(f'This claim belongs to {existing["worker"]}, not {worker}.', 409, work_field(existing, state))
    return existing


def heartbeat(connection, key, sha, worker, *, decision, now, record, user, lease_hours=None) -> dict:
    worker, hours = validate_worker(worker), validate_lease(lease_hours)
    _own_working(connection, key, sha, worker, decision, now, 'extend')
    expires = (now + timedelta(hours=hours)).isoformat()
    connection.execute('UPDATE work_claims SET expires_at=?, updated_at=? WHERE icon=? AND svg_sha256=?',
                       (expires, now.isoformat(), key, sha))
    record(connection, user, 'work_heartbeat', key, svg_sha256=sha, worker=worker, expires_at=expires)
    return work_field(load_claim(connection, key, sha), 'working')


def finish(connection, key, sha, worker, outcome, *, decision, now, record, user, note=None) -> dict:
    """working -> done (revision returned to Ready, feedback kept) or cannot-fix."""
    if outcome not in ('done', 'cannot-fix'):
        raise WorkError('outcome must be done or cannot-fix.', 400)
    worker = validate_worker(worker)
    note = validate_note(note, required=outcome == 'cannot-fix')
    _own_working(connection, key, sha, worker, decision, now, 'finish')
    stamp = now.isoformat()
    connection.execute('UPDATE work_claims SET state=?, note=?, updated_at=?, expires_at=NULL WHERE icon=? AND svg_sha256=?',
                       (outcome, note, stamp, key, sha))
    record(connection, user, 'work_' + outcome.replace('-', '_'), key, svg_sha256=sha, worker=worker, note=note)
    result = {'work': work_field(load_claim(connection, key, sha), outcome)}
    if outcome == 'done':
        # Back to Ready for the reviewer. The disapproval feedback is deliberately
        # kept so the fix can be compared against the request.
        connection.execute('''INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, 'ready', ?, ?)
            ON CONFLICT(icon, svg_sha256) DO UPDATE SET status='ready', updated_at=excluded.updated_at, updated_by=excluded.updated_by''',
                           (key, sha, stamp, worker))
        record(connection, worker, 'review', key, status='ready', svg_sha256=sha, source='work_done', feedback_kept=True)
        result['status'] = 'ready'
    return result


def abandon(connection, key, sha, worker, *, decision, now, record, user, admin=False) -> dict:
    """Delete a working claim so the icon is open again; admins may release anyone's."""
    worker = validate_worker(worker)
    existing, state = _current(connection, key, sha, decision, now)
    if not existing:
        raise WorkError('There is no claim on this revision.', 404, work_field(None, state))
    if existing['worker'] != worker and not admin:
        raise WorkError(f'This claim belongs to {existing["worker"]}, not {worker}. Log in to release it.', 409,
                        work_field(existing, state))
    if existing['state'] != 'working' and not admin:
        raise WorkError(f'Only working claims can be abandoned; this revision is {state}.', 409, work_field(existing, state))
    connection.execute('DELETE FROM work_claims WHERE icon=? AND svg_sha256=?', (key, sha))
    record(connection, user, 'work_abandon', key, svg_sha256=sha, worker=existing['worker'], released_by=worker,
           previous_state=existing['state'])
    return {'work': work_field(None, 'open')}
