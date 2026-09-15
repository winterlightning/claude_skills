"""Publish primitive decisions without copying feedback or authentication data.

Export: python3 -m icon_set.scripts.progression
The gallery imports the tracked snapshot at startup, preserving newer edits.
"""
import argparse
import json
import sqlite3
from contextlib import closing
from pathlib import Path

SNAPSHOT = Path(__file__).resolve().parents[1] / 'progression.sqlite3'
FIELDS = 'uuid,status,reason,note,updated_by,updated_at,main_brief,sub_brief,sub_position'


def export_snapshot(database, target=SNAPSHOT, reviews=None):
    target = Path(target)
    temporary = target.with_suffix('.tmp.sqlite3')
    if temporary.exists():
        temporary.unlink()
    with closing(sqlite3.connect(database)) as source, closing(sqlite3.connect(temporary)) as dest:
        source.execute('BEGIN')
        dest.execute('CREATE TABLE decisions(uuid TEXT PRIMARY KEY,status TEXT,reason TEXT,note TEXT,updated_by TEXT,updated_at TEXT,main_brief TEXT,sub_brief TEXT,sub_position TEXT)')
        dest.executemany('INSERT INTO decisions VALUES (?,?,?,?,?,?,?,?,?)', source.execute('SELECT '+FIELDS+' FROM primitive_status'))
        # TODO removes the live row; preserve those explicit restores as tombstones.
        for uid, user, at in source.execute("SELECT substr(icon,11),username,created_at FROM activity_log WHERE action='primitive_todo' ORDER BY id"):
            dest.execute("INSERT INTO decisions VALUES (?,'todo',NULL,'',?,?,NULL,NULL,NULL) ON CONFLICT(uuid) DO UPDATE SET status='todo',reason=NULL,note='',updated_by=excluded.updated_by,updated_at=excluded.updated_at,main_brief=NULL,sub_brief=NULL,sub_position=NULL WHERE excluded.updated_at>decisions.updated_at", (uid,user,at))
        dest.execute('CREATE TABLE reviews(path TEXT PRIMARY KEY,content TEXT NOT NULL)')
        if reviews and Path(reviews).exists():
            for path in sorted(Path(reviews).rglob('review.json')):
                content = json.loads(path.read_text())
                dest.execute('INSERT INTO reviews VALUES (?,?)', (str(path.relative_to(reviews)),json.dumps(content,ensure_ascii=False,sort_keys=True)))
        dest.execute('PRAGMA user_version=1')
        dest.commit()
        assert dest.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
    temporary.replace(target)


def import_snapshot(connection, snapshot=SNAPSHOT):
    snapshot = Path(snapshot)
    if not snapshot.exists():
        return 0
    connection.execute('CREATE TABLE IF NOT EXISTS progression_imports(uuid TEXT PRIMARY KEY,updated_at TEXT NOT NULL)')
    connection.execute('CREATE TABLE IF NOT EXISTS progression_reviews(path TEXT PRIMARY KEY,content TEXT NOT NULL)')
    changed = 0
    with closing(sqlite3.connect(snapshot.resolve().as_uri()+'?mode=ro',uri=True)) as source:
        if source.execute('PRAGMA user_version').fetchone()[0] != 1:
            raise ValueError('Unsupported progression snapshot version')
        for row in source.execute('SELECT '+FIELDS+' FROM decisions'):
            uid,status,reason,note,user,at,main,sub,position = row
            times = [r[0] for r in connection.execute('SELECT updated_at FROM primitive_status WHERE uuid=? UNION ALL SELECT updated_at FROM progression_imports WHERE uuid=? UNION ALL SELECT created_at FROM activity_log WHERE icon=? AND action IN (\'primitive_skip\',\'primitive_todo\')', (uid,uid,'primitive:'+uid))]
            if times and max(times) >= at:
                continue
            if status == 'todo':
                connection.execute('DELETE FROM primitive_status WHERE uuid=?',(uid,))
            elif status == 'skip':
                connection.execute('INSERT INTO primitive_status('+FIELDS+') VALUES (?,?,?,?,?,?,?,?,?) ON CONFLICT(uuid) DO UPDATE SET status=excluded.status,reason=excluded.reason,note=excluded.note,updated_by=excluded.updated_by,updated_at=excluded.updated_at,main_brief=excluded.main_brief,sub_brief=excluded.sub_brief,sub_position=excluded.sub_position,combination_brief=NULL',row)
            else:
                raise ValueError('Invalid progression status')
            connection.execute('INSERT INTO progression_imports VALUES (?,?) ON CONFLICT(uuid) DO UPDATE SET updated_at=excluded.updated_at',(uid,at))
            changed += 1
        for row in source.execute('SELECT path,content FROM reviews'):
            connection.execute('INSERT INTO progression_reviews VALUES (?,?) ON CONFLICT(path) DO UPDATE SET content=excluded.content',row)
    return changed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database',type=Path,default=SNAPSHOT.parent/'data/feedback.sqlite3')
    parser.add_argument('--output',type=Path,default=SNAPSHOT)
    parser.add_argument('--reviews',type=Path,default=SNAPSHOT.parents[1]/'work/primitives-review')
    args = parser.parse_args()
    export_snapshot(args.database,args.output,args.reviews)
    print(args.output)
