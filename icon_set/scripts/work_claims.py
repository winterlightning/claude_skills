"""Who is fixing which disapproved icon: a review status, kept on the review row itself.

There is one table. ``reviews`` holds the review status of every icon revision
(``icon`` + ``svg_sha256``) and, since claims moved onto it, who is working on
that revision. The review statuses are the ones reviewers know plus one::

    ready        nothing to do (a fixed revision reported ``done`` keeps its worker)
    pending      Disapproved by a reviewer (``disapprove`` in the API)
    claimed      a worker is on it; ``worker`` and ``claimed_at`` say who and since when
    approve / rejected   reviewer decisions, never claimable

The ``work.state`` the API reports is derived from that row and the clock:

    open        disapproved and nobody on it: claimable
    claimed     review status claimed, less than LEASE_HOURS ago
    done        ready, set by a worker's ``done`` report (feedback kept for review)
    cannot-fix  disapproved, but a worker gave up: ``worker`` and ``note`` stay on
                the row so the queue skips it until a reviewer decides again
    none        every other status

A claim older than LEASE_HOURS has expired: ``release_expired`` sets the row back
to Disapproved (worker cleared) and it is ``open`` again; no heartbeat exists. A
deployed fix changes the hash, so the new revision starts Ready with no row; the
old row stays as history. A reviewer who sets any status through the gallery
clears the claim columns, so disapproving a ``done`` or ``cannot-fix`` icon again
puts it straight back in the queue.

Every function takes an open connection and ``now`` so it can be tested without
HTTP. Only production writes these columns; development servers forward to it.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import json
import re

LEASE_HOURS = 6
DISAPPROVED = ('pending', 'claimed')  # the review statuses that mean "needs a fix"
CLAIMABLE = ('open',)
MAX_WORKER = 120
MAX_NOTE = 4000
MAX_QUEUE = 500
_WORKER = re.compile(r'^[^\x00-\x1f\x7f]{1,%d}$' % MAX_WORKER)
CLAIM_COLUMNS = (('worker', 'worker TEXT'), ('claimed_at', 'claimed_at TEXT'), ('note', "note TEXT NOT NULL DEFAULT ''"))
ROW_FIELDS = ('icon', 'svg_sha256', 'status', 'worker', 'note', 'claimed_at', 'updated_at', 'updated_by')


class WorkError(ValueError):
    """A refused transition; ``status`` is the HTTP code and ``work`` the current state."""

    def __init__(self, message, status=409, work=None):
        super().__init__(message)
        self.status, self.work = status, work


def init_work_claims(connection) -> None:
    """Add the claim columns to ``reviews`` and fold a legacy ``work_claims`` table into them."""
    columns = {row[1] for row in connection.execute('PRAGMA table_info(reviews)')}
    for column, ddl in CLAIM_COLUMNS:
        if column not in columns:
            connection.execute(f'ALTER TABLE reviews ADD COLUMN {ddl}')
    init_work_results(connection)
    migrate_claims_table(connection)


def release_expired(connection, now, record=None) -> int:
    """Claims older than LEASE_HOURS go back to Disapproved so the icon is open again; returns how many."""
    stale = (now - timedelta(hours=LEASE_HOURS)).isoformat()
    rows = connection.execute("SELECT icon, svg_sha256, worker, claimed_at FROM reviews WHERE status='claimed' AND claimed_at <= ?",
                              (stale,)).fetchall()
    for icon, sha, worker, claimed_at in rows:
        connection.execute("UPDATE reviews SET status='pending', worker=NULL, claimed_at=NULL, note='' "
                           "WHERE icon=? AND svg_sha256=? AND status='claimed' AND claimed_at=?", (icon, sha, claimed_at))
        if record is not None:
            record(connection, 'system', 'work_expired', icon, svg_sha256=sha, worker=worker, claimed_at=claimed_at)
    return len(rows)


def migrate_claims_table(connection) -> None:
    """One-time move of the old separate tables onto the review rows, then drop them."""
    tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if 'work_claims' in tables:
        for icon, sha, state, worker, note, claimed_at, updated_at in connection.execute(
                'SELECT icon, svg_sha256, state, worker, note, claimed_at, updated_at FROM work_claims').fetchall():
            row = connection.execute('SELECT status, updated_at FROM reviews WHERE icon=? AND svg_sha256=?', (icon, sha)).fetchone()
            if not row:
                continue
            status, decided = row
            if state == 'working' and status == 'pending':
                connection.execute("UPDATE reviews SET status='claimed', worker=?, claimed_at=?, note='' WHERE icon=? AND svg_sha256=?",
                                   (worker, claimed_at, icon, sha))
            elif state == 'cannot-fix' and status == 'pending' and not (decided and updated_at and decided > updated_at):
                connection.execute("UPDATE reviews SET worker=?, claimed_at=?, note=? WHERE icon=? AND svg_sha256=?",
                                   (worker, claimed_at, note or '', icon, sha))
            elif state == 'done' and status == 'ready':
                connection.execute('UPDATE reviews SET worker=?, claimed_at=?, note=? WHERE icon=? AND svg_sha256=?',
                                   (worker, claimed_at, note or '', icon, sha))
        connection.execute('DROP TABLE work_claims')
    if 'work_snapshots' in tables:
        # The drawing saved at claim time becomes the "before" result when the worker uploaded none.
        connection.execute('''INSERT OR IGNORE INTO work_results(icon, svg_sha256, stage, worker, svg, python_path, python_source, validation, note, saved_at)
            SELECT s.icon, s.svg_sha256, 'before', COALESCE(r.worker, 'snapshot'), s.svg, NULL, NULL, NULL,
                   'drawing as displayed when the icon was claimed', s.saved_at
            FROM work_snapshots s LEFT JOIN reviews r ON r.icon = s.icon AND r.svg_sha256 = s.svg_sha256''')
        connection.execute('DROP TABLE work_snapshots')


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
    row, state = _current(connection, key, sha, now)
    allowed = ('claimed',) if stage == 'before' else ('claimed', 'done', 'cannot-fix')
    if state not in allowed:
        raise WorkError(f'Upload the {stage} result while you hold the claim; this revision is {state}.', 409, work_field(row, state))
    if row['worker'] != worker:
        raise WorkError(f'This claim belongs to {row["worker"]}, not {worker}.', 409, work_field(row, state))
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


def public_status(status) -> str:
    """The database keeps the legacy ``pending``; the API and the gallery say ``disapprove``."""
    return 'disapprove' if status == 'pending' else ('ready' if status == 're-generated' else status)


# ---- the row and its derived work state ----

def load_row(connection, key, sha):
    row = connection.execute(f'SELECT {", ".join(ROW_FIELDS)} FROM reviews WHERE icon=? AND svg_sha256=?', (key, sha)).fetchone()
    return dict(zip(ROW_FIELDS, row)) if row else None


def load_rows(connection) -> dict:
    """(icon, sha) -> review row, for every revision that has one."""
    return {(row[0], row[1]): dict(zip(ROW_FIELDS, row)) for row in connection.execute(f'SELECT {", ".join(ROW_FIELDS)} FROM reviews')}


def expires_at(row):
    claimed = parse_time(row.get('claimed_at')) if row else None
    return (claimed + timedelta(hours=LEASE_HOURS)).isoformat() if claimed else None


def work_state(row, now) -> str:
    """The work state of one revision, from its review row and the clock."""
    if not row:
        return 'none'
    status = row['status']
    if status == 'pending':
        return 'cannot-fix' if row.get('worker') else 'open'
    if status == 'claimed':
        claimed = parse_time(row.get('claimed_at'))
        return 'claimed' if claimed and now < claimed + timedelta(hours=LEASE_HOURS) else 'open'  # expired: released on next write
    if status == 'ready' and row.get('worker'):
        return 'done'
    return 'none'


def work_field(row, state) -> dict:
    """What the API returns under ``work``."""
    field = {'state': state}
    if row and row.get('worker') and state != 'open':
        field.update(worker=row['worker'], note=row.get('note') or '', claimed_at=row.get('claimed_at'),
                     updated_at=row.get('updated_at'), svg_sha256=row['svg_sha256'])
        if row['status'] == 'claimed':
            field['expires_at'] = expires_at(row)
    return field


def _current(connection, key, sha, now):
    row = load_row(connection, key, sha)
    return row, work_state(row, now)


def latest_feedback(connection) -> dict:
    """(icon, sha) -> the newest feedback entry for that revision."""
    latest = {}
    for icon, sha, reason, feedback, author, created_at in connection.execute(
            'SELECT icon, svg_sha256, reason, feedback, author, created_at FROM feedback ORDER BY id'):
        latest[(icon, sha)] = {'reason': reason, 'feedback': feedback, 'feedback_by': author, 'feedback_at': created_at}
    return latest


def icon_types(connection) -> dict:
    return dict(connection.execute("SELECT icon, icon_type FROM icon_types WHERE icon_type != ''").fetchall())


def queue_item(icon, decision, feedback, row, state) -> dict:
    status, actor, stamp = decision
    source = icon.get('python_source')
    return {
        'key': icon['key'], 'icon_id': icon.get('icon_id'), 'name': icon.get('name'),
        'family': icon.get('family'), 'category': icon.get('category'),
        'svg_sha256': icon.get('svg_sha256'), 'python_source': source,
        'preview_url': icon.get('preview_url'), 'original_sources': icon.get('original_sources') or [],
        'status': public_status(status),
        'disapproved_by': actor, 'disapproved_at': stamp,
        'reason': (feedback or {}).get('reason'), 'feedback': (feedback or {}).get('feedback'),
        'feedback_by': (feedback or {}).get('feedback_by'),
        'icon_type': icon.get('icon_type'), 'work': work_field(row, state),
    }


def _paging(query):
    one = lambda name: (query.get(name) or [None])[0]  # noqa: E731
    try:
        limit = int(one('limit') or 50)
        offset = int(one('offset') or 0)
    except ValueError:
        raise WorkError('limit and offset must be integers.', 400)
    if not 1 <= limit <= MAX_QUEUE or offset < 0:
        raise WorkError(f'limit must be 1-{MAX_QUEUE} and offset nonnegative.', 400)
    return one, limit, offset


def _disapproved_items(connection, catalog, decisions, now, filters):
    """Every icon whose current revision needs a fix (pending, claimed, cannot-fix) or was just fixed (done)."""
    family, category, wanted_type, reason = filters
    rows, feedback, types = load_rows(connection), latest_feedback(connection), icon_types(connection)
    items = []
    for key, decision in decisions.items():
        status = decision[0]
        icon = catalog.get(key)
        if not icon:
            continue
        sha = icon.get('svg_sha256') or ''
        row = rows.get((key, sha))
        if status == 'disapprove':
            status = 'pending'
        if status in DISAPPROVED:
            row = row or {'icon': key, 'svg_sha256': sha, 'status': status, 'worker': None, 'note': '', 'claimed_at': None,
                          'updated_at': decision[2], 'updated_by': decision[1]}
        elif not (status == 'ready' and row and row.get('worker')):
            continue
        icon = dict(icon, icon_type=types.get(key))
        if family and icon.get('family') != family:
            continue
        if category and icon.get('category') != category:
            continue
        if wanted_type and icon.get('icon_type') != wanted_type:
            continue
        if reason and (feedback.get((key, sha)) or {}).get('reason') != reason:
            continue
        items.append(queue_item(icon, decision, feedback.get((key, sha)), row, work_state(row, now)))
    return items


def queue(connection, catalog, decisions, query, now, *, claimable_only=True) -> dict:
    """Disapproved icons, oldest disapproval first: claimable ones, or all of them with their work state."""
    one, limit, offset = _paging(query)
    items = _disapproved_items(connection, catalog, decisions, now, (one('family'), one('category'), one('type'), one('reason')))
    rows = [item for item in items if item['status'] != 'ready' and (not claimable_only or item['work']['state'] in CLAIMABLE)]
    rows.sort(key=lambda item: (item['disapproved_at'] or '', item['key']))
    page = rows[offset:offset + limit]
    return {'total': len(rows), 'offset': offset,
            'next_offset': offset + limit if offset + limit < len(rows) else None, 'items': page}


def listing(connection, catalog, decisions, now) -> dict:
    """Every current revision that carries a worker, joined to the catalog, for the gallery badges."""
    result = []
    for (key, sha), row in sorted(load_rows(connection).items()):
        icon = catalog.get(key)
        if not icon or (icon.get('svg_sha256') or '') != sha or not row.get('worker'):
            continue
        state = work_state(row, now)
        if state in ('none', 'open'):
            continue
        decision = decisions.get(key)
        result.append(dict(work_field(row, state), icon=key, current=True,
                           status=public_status(decision[0] if decision else row['status'])))
    return {'claims': result}


def review_listing(connection, catalog, decisions, query, now) -> dict:
    """Every icon a reviewer may want to follow: disapproved, claimed, cannot-fix, or fixed and awaiting review."""
    one, limit, offset = _paging(dict(query, limit=query.get('limit') or [str(MAX_QUEUE)]))
    items = _disapproved_items(connection, catalog, decisions, now, (one('family'), None, None, one('reason')))
    summaries = result_summaries(connection)
    for item in items:
        item['work']['results'] = sorted(summaries.get((item['key'], item.get('svg_sha256') or ''), {}))
    ordered = sorted(items, key=lambda item: (item['work'].get('claimed_at') or item['disapproved_at'] or '', item['key']), reverse=True)
    state, status = one('state'), one('status')
    if state:
        ordered = [item for item in ordered if item['work']['state'] == state]
    if status:
        ordered = [item for item in ordered if item['status'] == status]
    counts = {}
    for item in items:
        counts[item['work']['state']] = counts.get(item['work']['state'], 0) + 1
    return {'total': len(ordered), 'offset': offset, 'next_offset': offset + limit if offset + limit < len(ordered) else None,
            'counts': counts, 'items': ordered[offset:offset + limit]}


# ---- transitions; each runs inside the caller's write transaction ----

def claim(connection, key, sha, worker, *, decision, now, record, user) -> dict:
    """disapprove (open or expired) -> claimed. One conditional update, so two machines cannot both win."""
    worker = validate_worker(worker)
    status = decision[0] if decision else 'ready'
    row, state = _current(connection, key, sha, now)
    if status not in DISAPPROVED and status != 'disapprove':
        raise WorkError(f'Only disapproved icons can be claimed; this revision is {public_status(status)}.', 409, work_field(row, state))
    if state not in CLAIMABLE:
        if state == 'claimed' and row['worker'] == worker:
            raise WorkError('You already hold this claim.', 409, work_field(row, state))
        message = {'claimed': f'{row["worker"]} is working on this icon.',
                   'cannot-fix': f'{row["worker"]} reported this revision cannot be fixed.'}.get(state, f'This revision is {state}.')
        raise WorkError(message, 409, work_field(row, state))
    stamp = now.isoformat()
    stale = (now - timedelta(hours=LEASE_HOURS)).isoformat()
    changed = connection.execute('''UPDATE reviews SET status='claimed', worker=?, claimed_at=?, note=''
        WHERE icon=? AND svg_sha256=? AND ((status='pending' AND worker IS NULL) OR (status='claimed' AND claimed_at <= ?))''',
                                 (worker, stamp, key, sha, stale)).rowcount
    if not changed:
        row, state = _current(connection, key, sha, now)
        raise WorkError('Another worker claimed this icon just now.', 409, work_field(row, state))
    if row and row['status'] == 'claimed':
        record(connection, user, 'work_expired', key, svg_sha256=sha, worker=row['worker'], claimed_at=row['claimed_at'], taken_by=worker)
    fresh = load_row(connection, key, sha)
    record(connection, user, 'work_claim', key, svg_sha256=sha, worker=worker, expires_at=expires_at(fresh))
    return work_field(fresh, 'claimed')


def _own_claim(connection, key, sha, worker, now, verb):
    row, state = _current(connection, key, sha, now)
    if state != 'claimed':
        raise WorkError(f'No active claim to {verb}; this revision is {state}.', 409, work_field(row, state))
    if row['worker'] != worker:
        raise WorkError(f'This claim belongs to {row["worker"]}, not {worker}.', 409, work_field(row, state))
    return row


def finish(connection, key, sha, worker, outcome, *, decision, now, record, user, note=None) -> dict:
    """claimed -> ready (done: feedback kept for the reviewer) or cannot-fix."""
    if outcome not in ('done', 'cannot-fix'):
        raise WorkError('outcome must be done or cannot-fix.', 400)
    worker = validate_worker(worker)
    note = validate_note(note, required=outcome == 'cannot-fix')
    _own_claim(connection, key, sha, worker, now, 'finish')
    stamp = now.isoformat()
    if outcome == 'done':
        # Back to Ready for the reviewer, attributed to the worker. The disapproval
        # feedback is deliberately kept so the fix can be compared against the request.
        connection.execute("UPDATE reviews SET status='ready', note=?, updated_at=?, updated_by=? WHERE icon=? AND svg_sha256=?",
                           (note, stamp, worker, key, sha))
        record(connection, user, 'work_done', key, svg_sha256=sha, worker=worker, note=note)
        record(connection, worker, 'review', key, status='ready', svg_sha256=sha, source='work_done', feedback_kept=True)
        return {'work': work_field(load_row(connection, key, sha), 'done'), 'status': 'ready'}
    # Back to Disapproved, but the worker and note stay on the row: the queue skips it until a reviewer decides again.
    connection.execute("UPDATE reviews SET status='pending', note=? WHERE icon=? AND svg_sha256=?", (note, key, sha))
    record(connection, user, 'work_cannot_fix', key, svg_sha256=sha, worker=worker, note=note)
    return {'work': work_field(load_row(connection, key, sha), 'cannot-fix')}


def abandon(connection, key, sha, worker, *, decision, now, record, user) -> dict:
    """claimed or cannot-fix -> disapproved with no worker, by anyone; the icon is open at once."""
    worker = validate_worker(worker)
    row, state = _current(connection, key, sha, now)
    if state not in ('claimed', 'cannot-fix'):
        raise WorkError(f'There is no claim to release; this revision is {state}.', 409 if row else 404, work_field(row, state))
    connection.execute("UPDATE reviews SET status='pending', worker=NULL, claimed_at=NULL, note='' WHERE icon=? AND svg_sha256=?", (key, sha))
    record(connection, user, 'work_abandon', key, svg_sha256=sha, worker=row['worker'], released_by=worker, previous_state=state)
    return {'work': work_field(None, 'open')}


def history(connection, catalog, decisions, key, now) -> dict:
    """Everything that happened to one icon: revisions, reviews, feedback, claims, results and the event log."""
    icon = catalog[key]
    current_sha = icon.get('svg_sha256') or ''
    decision = decisions.get(key) or ('ready', None, None)
    revisions = {}

    def revision(sha):
        return revisions.setdefault(sha, {'svg_sha256': sha, 'current': sha == current_sha, 'review': None, 'claim': None,
                                          'feedback': [], 'results': {}, 'first_seen': None})

    def seen(entry, stamp):
        if stamp and (entry['first_seen'] is None or stamp < entry['first_seen']):
            entry['first_seen'] = stamp

    for (icon_key, sha), row in load_rows(connection).items():
        if icon_key != key:
            continue
        entry = revision(sha)
        entry['review'] = {'status': public_status(row['status']), 'updated_by': row['updated_by'], 'updated_at': row['updated_at']}
        seen(entry, row['updated_at'])
        state = work_state(row, now)
        if row.get('worker') and state not in ('none', 'open'):
            entry['claim'] = work_field(row, state)
            seen(entry, row['claimed_at'])
    for row in connection.execute('SELECT id, svg_sha256, reason, feedback, author, created_at, edited_by, edited_at FROM feedback WHERE icon=? ORDER BY id', (key,)):
        entry = revision(row[1])
        entry['feedback'].append({'id': row[0], 'reason': row[2], 'feedback': row[3], 'author': row[4], 'created_at': row[5],
                                  'edited_by': row[6], 'edited_at': row[7]})
        seen(entry, row[5])
    for (_, sha), stages in result_summaries(connection, key).items():
        entry = revision(sha)
        entry['results'] = stages
        for summary in stages.values():
            seen(entry, summary['saved_at'])
    current = revision(current_sha)
    if current['review'] is None or decision[0] == 'rejected':
        current['review'] = {'status': public_status(decision[0]), 'updated_by': decision[1], 'updated_at': decision[2]}
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
