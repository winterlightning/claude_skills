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
import json
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
    # The drawing as it was when claimed, so a fix can be compared with what the reviewer saw.
    connection.execute('''CREATE TABLE IF NOT EXISTS work_snapshots (
        icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL, svg TEXT NOT NULL, saved_at TEXT NOT NULL,
        PRIMARY KEY(icon, svg_sha256))''')
    init_work_results(connection)


def init_work_results(connection) -> None:
    """Fix results a worker uploads for a claimed revision: the drawing before and after the fix."""
    connection.execute('''CREATE TABLE IF NOT EXISTS work_results (
        icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
        stage TEXT NOT NULL CHECK(stage IN ('before','after')),
        worker TEXT NOT NULL, svg TEXT NOT NULL, python_path TEXT, python_source TEXT,
        validation TEXT, note TEXT NOT NULL DEFAULT '', saved_at TEXT NOT NULL,
        PRIMARY KEY(icon, svg_sha256, stage))''')


RESULT_STAGES = ('before', 'after')
MAX_RESULT_TEXT = 512 * 1024


def validate_text(value, name, *, required=False):
    if value is None or value == '':
        if required:
            raise WorkError(f'{name} is required.', 400)
        return None
    if not isinstance(value, str) or len(value.encode('utf-8')) > MAX_RESULT_TEXT:
        raise WorkError(f'{name} must be text of at most {MAX_RESULT_TEXT // 1024} KB.', 400)
    return value


def save_result(connection, key, sha, stage, worker, *, svg, python_path=None, python_source=None,
                validation=None, note=None, decision, now, record, user) -> dict:
    """Store one stage of a fix for the worker's own claim; ``after`` may follow ``done``."""
    if stage not in RESULT_STAGES:
        raise WorkError('stage must be before or after.', 400)
    worker = validate_worker(worker)
    svg = validate_text(svg, 'svg', required=True)
    python_source, validation = validate_text(python_source, 'python_source'), validate_text(validation, 'validation')
    if python_path is not None and (not isinstance(python_path, str) or len(python_path) > 512):
        raise WorkError('python_path must be a short path string.', 400)
    note = validate_note(note)
    existing, state = _current(connection, key, sha, decision, now)
    allowed = ('working',) if stage == 'before' else ('working', 'done', 'cannot-fix')
    if not existing or state not in allowed:
        raise WorkError(f'Upload the {stage} result while you hold the claim; this revision is {state}.', 409,
                        work_field(existing, state))
    if existing['worker'] != worker:
        raise WorkError(f'This claim belongs to {existing["worker"]}, not {worker}.', 409, work_field(existing, state))
    stamp = now.isoformat()
    connection.execute('''INSERT INTO work_results(icon, svg_sha256, stage, worker, svg, python_path, python_source, validation, note, saved_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(icon, svg_sha256, stage) DO UPDATE SET worker=excluded.worker, svg=excluded.svg,
        python_path=excluded.python_path, python_source=excluded.python_source, validation=excluded.validation,
        note=excluded.note, saved_at=excluded.saved_at''',
                       (key, sha, stage, worker, svg, python_path, python_source, validation, note, stamp))
    record(connection, user, 'work_result', key, svg_sha256=sha, stage=stage, worker=worker, python_path=python_path,
           has_python=python_source is not None, has_validation=validation is not None, note=note)
    return {'stage': stage, 'worker': worker, 'saved_at': stamp, 'python_path': python_path, 'note': note,
            'has_python': python_source is not None, 'has_validation': validation is not None}


def load_result(connection, key, sha, stage):
    row = connection.execute('SELECT worker, svg, python_path, python_source, validation, note, saved_at FROM work_results '
                             'WHERE icon=? AND svg_sha256=? AND stage=?', (key, sha, stage)).fetchone()
    if not row:
        return None
    return dict(zip(('worker', 'svg', 'python_path', 'python_source', 'validation', 'note', 'saved_at'), row))


def result_summaries(connection, key=None) -> dict:
    """(icon, sha) -> {stage: summary} without the large text fields."""
    query = 'SELECT icon, svg_sha256, stage, worker, python_path, note, saved_at, python_source IS NOT NULL, validation IS NOT NULL FROM work_results'
    rows = connection.execute(query + (' WHERE icon=?' if key else ''), (key,) if key else ()).fetchall()
    summaries = {}
    for icon, sha, stage, worker, python_path, note, saved_at, has_python, has_validation in rows:
        summaries.setdefault((icon, sha), {})[stage] = {
            'worker': worker, 'python_path': python_path, 'note': note, 'saved_at': saved_at,
            'has_python': bool(has_python), 'has_validation': bool(has_validation)}
    return summaries


def save_snapshot(connection, key, sha, svg, now) -> None:
    connection.execute('INSERT OR IGNORE INTO work_snapshots(icon, svg_sha256, svg, saved_at) VALUES (?, ?, ?, ?)',
                       (key, sha, svg, now.isoformat()))


def load_snapshot(connection, key, sha):
    row = connection.execute('SELECT svg FROM work_snapshots WHERE icon=? AND svg_sha256=?', (key, sha)).fetchone()
    return row[0] if row else None


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
    family, category, wanted_type, reason = one('family'), one('category'), one('type'), one('reason')
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
        if reason and (feedback.get((key, sha)) or {}).get('reason') != reason:
            continue
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


def review_listing(connection, catalog, decisions, query, now) -> dict:
    """Every icon a reviewer may want to follow: disapproved now, or carrying any claim.

    Claims on a revision that is no longer current are reported as ``superseded``:
    the fix was deployed and the current revision is judged on its own.
    """
    disapproved = queue(connection, catalog, decisions, {'limit': [str(MAX_QUEUE)]}, now, claimable_only=False)
    rows = {item['key']: item for item in disapproved['items']}
    while disapproved['next_offset'] is not None:
        disapproved = queue(connection, catalog, decisions, {'limit': [str(MAX_QUEUE)], 'offset': [str(disapproved['next_offset'])]},
                            now, claimable_only=False)
        rows.update((item['key'], item) for item in disapproved['items'])
    feedback, types = latest_feedback(connection), icon_types(connection)
    snapshots = {(row[0], row[1]) for row in connection.execute('SELECT icon, svg_sha256 FROM work_snapshots')}
    for (key, sha), claim in load_claims(connection).items():
        icon = catalog.get(key)
        if not icon:
            continue
        current_sha = icon.get('svg_sha256') or ''
        if key in rows:
            rows[key]['work']['snapshot'] = (key, sha) in snapshots
            continue
        decision = decisions.get(key) or ('ready', None, None)
        if sha == current_sha:
            state = work_state(claim, decision[2], now)
        elif claim['state'] == 'working' and work_state(claim, None, now) == 'expired':
            state = 'superseded'
        else:
            state = 'superseded'
        item = queue_item(dict(icon, icon_type=types.get(key)), decision, feedback.get((key, sha)), claim, state)
        item['status'] = 'disapprove' if decision[0] == 'pending' else decision[0]
        item['work']['claimed_svg_sha256'] = sha
        item['work']['snapshot'] = (key, sha) in snapshots
        rows[key] = item
    summaries = result_summaries(connection)
    for item in rows.values():
        item['work'].setdefault('snapshot', False)
        sha = item['work'].get('claimed_svg_sha256') or item.get('svg_sha256') or ''
        item['work']['results'] = sorted(summaries.get((item['key'], sha), {}))
    ordered = sorted(rows.values(), key=lambda item: (item['work'].get('updated_at') or item['disapproved_at'] or '', item['key']), reverse=True)
    one = lambda name: (query.get(name) or [None])[0]  # noqa: E731
    family, state, status, reason = one('family'), one('state'), one('status'), one('reason')
    if reason:
        ordered = [item for item in ordered if item.get('reason') == reason]
    if family:
        ordered = [item for item in ordered if item.get('family') == family]
    if state:
        ordered = [item for item in ordered if item['work']['state'] == state]
    if status:
        ordered = [item for item in ordered if item['status'] == status]
    try:
        limit, offset = int(one('limit') or MAX_QUEUE), int(one('offset') or 0)
    except ValueError:
        raise WorkError('limit and offset must be integers.', 400)
    if not 1 <= limit <= MAX_QUEUE or offset < 0:
        raise WorkError(f'limit must be 1-{MAX_QUEUE} and offset nonnegative.', 400)
    counts = {}
    for item in rows.values():
        counts[item['work']['state']] = counts.get(item['work']['state'], 0) + 1
    return {'total': len(ordered), 'offset': offset, 'next_offset': offset + limit if offset + limit < len(ordered) else None,
            'counts': counts, 'items': ordered[offset:offset + limit]}


def history(connection, catalog, decisions, key, now) -> dict:
    """Everything that happened to one icon: revisions, reviews, feedback, claims and the event log."""
    icon = catalog[key]
    current_sha = icon.get('svg_sha256') or ''
    decision = decisions.get(key) or ('ready', None, None)
    revisions = {}

    def revision(sha):
        return revisions.setdefault(sha, {'svg_sha256': sha, 'current': sha == current_sha, 'review': None, 'claim': None,
                                          'feedback': [], 'snapshot': False, 'results': {}, 'first_seen': None})

    def seen(entry, stamp):
        if stamp and (entry['first_seen'] is None or stamp < entry['first_seen']):
            entry['first_seen'] = stamp

    for sha, status, actor, stamp in connection.execute('SELECT svg_sha256, status, updated_by, updated_at FROM reviews WHERE icon=?', (key,)):
        entry = revision(sha)
        entry['review'] = {'status': 'disapprove' if status == 'pending' else ('ready' if status == 're-generated' else status),
                           'updated_by': actor, 'updated_at': stamp}
        seen(entry, stamp)
    for row in connection.execute('SELECT id, svg_sha256, reason, feedback, author, created_at, edited_by, edited_at FROM feedback WHERE icon=? ORDER BY id', (key,)):
        entry = revision(row[1])
        entry['feedback'].append({'id': row[0], 'reason': row[2], 'feedback': row[3], 'author': row[4], 'created_at': row[5],
                                  'edited_by': row[6], 'edited_at': row[7]})
        seen(entry, row[5])
    for (icon_key, sha), claim in load_claims(connection).items():
        if icon_key != key:
            continue
        entry = revision(sha)
        state = work_state(claim, decision[2] if sha == current_sha else None, now) if sha == current_sha else 'superseded'
        entry['claim'] = work_field(claim, state)
        seen(entry, claim['claimed_at'])
    for sha, saved_at in connection.execute('SELECT svg_sha256, saved_at FROM work_snapshots WHERE icon=?', (key,)):
        entry = revision(sha)
        entry['snapshot'] = True
        seen(entry, saved_at)
    for (_, sha), stages in result_summaries(connection, key).items():
        entry = revision(sha)
        entry['results'] = stages
        for summary in stages.values():
            seen(entry, summary['saved_at'])
    current = revision(current_sha)
    if current['review'] is None:
        current['review'] = {'status': 'disapprove' if decision[0] == 'pending' else decision[0], 'updated_by': decision[1], 'updated_at': decision[2]}
    events = []
    for username, action, details, created_at in connection.execute(
            'SELECT username, action, details, created_at FROM activity_log WHERE icon=? ORDER BY id', (key,)):
        try:
            payload = json.loads(details) if details else {}
        except ValueError:
            payload = {}
        events.append({'at': created_at, 'user': username, 'action': action, 'details': payload})
    ordered = sorted(revisions.values(), key=lambda entry: (entry['current'], entry['first_seen'] or ''))
    for entry in ordered:
        entry.pop('first_seen', None)
    return {'icon': key, 'name': icon.get('name'), 'family': icon.get('family'), 'preview_url': icon.get('preview_url'),
            'python_source': icon.get('python_source'),
            'current': {'svg_sha256': current_sha, 'status': current['review']['status'],
                        'updated_by': current['review']['updated_by'], 'updated_at': current['review']['updated_at'],
                        'work': current['claim'] or {'state': 'open' if current['review']['status'] == 'disapprove' else 'none'}},
            'revisions': ordered, 'events': events}
