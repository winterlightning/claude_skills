"""Saved reference briefs, independent of a primitive's remake status."""
from datetime import datetime, timezone

FAMILIES = ('sub', 'solo', 'container', 'avatar')
MAX_BRIEF = 20000


def init_primitive_briefs(connection):
    connection.execute('''CREATE TABLE IF NOT EXISTS primitive_briefs (
        uuid TEXT PRIMARY KEY, family TEXT NOT NULL, brief TEXT NOT NULL,
        updated_by TEXT NOT NULL, updated_at TEXT NOT NULL)''')


def load_primitive_briefs(connection):
    return {uid: dict(family=family, brief=brief, updated_by=user, updated_at=at)
            for uid, family, brief, user, at in connection.execute(
                'SELECT uuid, family, brief, updated_by, updated_at FROM primitive_briefs')}


def save_primitive_brief(connection, uid, family, brief, *, known, user, record):
    if not isinstance(uid, str) or uid not in known:
        raise ValueError('Choose a known primitive.')
    if family not in FAMILIES:
        raise ValueError('Choose an icon family: sub, solo, container or avatar.')
    if not isinstance(brief, str) or not brief.strip() or len(brief) > MAX_BRIEF:
        raise ValueError(f'Enter a brief of 1–{MAX_BRIEF:,} characters.')
    brief = brief.strip()
    previous = connection.execute('SELECT family, brief FROM primitive_briefs WHERE uuid=?', (uid,)).fetchone()
    if previous != (family, brief):
        now = datetime.now(timezone.utc).isoformat()
        connection.execute('INSERT INTO primitive_briefs VALUES (?,?,?,?,?) ON CONFLICT(uuid) DO UPDATE SET '
                           'family=excluded.family, brief=excluded.brief, updated_by=excluded.updated_by, '
                           'updated_at=excluded.updated_at', (uid, family, brief, user, now))
        record(connection, user, 'primitive_brief', 'primitive:' + uid, family=family, brief=brief)
    return load_primitive_briefs(connection)[uid]
