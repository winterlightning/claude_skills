from contextlib import closing
import sqlite3
import tempfile
import unittest
from pathlib import Path
from icon_set.scripts.deploy import init_database
from icon_set.scripts.progression import export_snapshot, import_snapshot

class ProgressionTests(unittest.TestCase):
    def test_snapshot_merge_and_restores(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); local=root/'local.sqlite3'; remote=root/'remote.sqlite3'; snapshot=root/'progression.sqlite3'
            init_database(local); init_database(remote)
            with closing(sqlite3.connect(local)) as db, db:
                db.execute("INSERT INTO primitive_status(uuid,status,reason,note,updated_by,updated_at,sub_position) VALUES ('a','skip','combination','review','agent','2026-01-01','right')")
            export_snapshot(local,snapshot)
            with closing(sqlite3.connect(snapshot)) as db:
                self.assertEqual({r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")},{'decisions','reviews'})
            with closing(sqlite3.connect(remote)) as db, db:
                self.assertEqual(import_snapshot(db,snapshot),1)
                self.assertEqual(import_snapshot(db,snapshot),0)
                self.assertEqual(db.execute('SELECT sub_position FROM primitive_status').fetchone()[0],'right')
                db.execute("DELETE FROM primitive_status WHERE uuid='a'")
                db.execute("INSERT INTO activity_log(username,action,icon,created_at) VALUES ('human','primitive_todo','primitive:a','2026-03-01')")
                self.assertEqual(import_snapshot(db,snapshot),0)
                self.assertEqual(db.execute('SELECT count(*) FROM primitive_status').fetchone()[0],0)
            with closing(sqlite3.connect(local)) as db, db:
                db.execute("DELETE FROM primitive_status WHERE uuid='a'")
                db.execute("INSERT INTO activity_log(username,action,icon,created_at) VALUES ('human','primitive_todo','primitive:a','2026-04-01')")
            export_snapshot(local,snapshot)
            with closing(sqlite3.connect(remote)) as db, db:
                self.assertEqual(import_snapshot(db,snapshot),1)
                self.assertEqual(import_snapshot(db,snapshot),0)

if __name__=='__main__':unittest.main()
