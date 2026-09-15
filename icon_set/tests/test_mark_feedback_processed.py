import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from icon_set.scripts import mark_feedback_processed_sep15 as script
from icon_set.scripts.deploy import init_database


class MarkProcessedTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.database=self.root/'production.sqlite3'
        init_database(self.database)
        self.dist=self.root/'dist';(self.dist/'gallery').mkdir(parents=True);(self.dist/'solo48').mkdir()
        self.sha=hashlib.sha256(b'fixed').hexdigest()
        (self.dist/'solo48/castle.svg').write_bytes(b'fixed')
        (self.dist/'gallery/icons.json').write_text(json.dumps({'icons':[{'icon_id':'castle','family':'solo','svg_sha256':self.sha}]}))
        self.ids=patch.object(script,'CHANGED_ICONS',{'solo/castle':self.sha});self.ids.start();self.addCleanup(self.ids.stop)
        self.time=patch.object(script,'PROCESSED_AT','2026-09-15T12:00:00+00:00');self.time.start();self.addCleanup(self.time.stop)
        self.db=sqlite3.connect(self.database);self.addCleanup(self.db.close)
        with self.db:
            self.db.execute("INSERT INTO feedback(id,icon,feedback,svg_sha256,created_at) VALUES (987,'solo/castle','Widen it','old','2026-09-14T12:00:00+00:00')")
            self.db.execute("INSERT INTO reviews VALUES ('solo/unrelated','other','approve','2026-09-14T12:00:00+00:00','human')")

    def test_removes_processed_feedback_sets_ready_and_preserves_other_icons(self):
        with self.db:self.db.execute("INSERT INTO feedback(icon,feedback,svg_sha256,created_at) VALUES ('solo/unrelated','Keep this','other','2026-09-14T12:00:00+00:00')")
        comments=self.db.execute("SELECT * FROM feedback WHERE icon='solo/unrelated'").fetchall()
        self.assertEqual(script.mark_processed(self.database,self.dist)['updated'],['solo/castle'])
        self.assertEqual(self.db.execute('SELECT * FROM feedback').fetchall(),comments)
        self.assertEqual(self.db.execute("SELECT count(*) FROM feedback WHERE icon='solo/castle'").fetchone()[0],0)
        self.assertEqual(self.db.execute("SELECT status FROM reviews WHERE icon='solo/castle'").fetchone()[0],'ready')
        self.assertEqual(self.db.execute("SELECT status FROM reviews WHERE icon='solo/unrelated'").fetchone()[0],'approve')
        self.assertEqual(script.mark_processed(self.database,self.dist)['already_ready'],['solo/castle'])

    def test_old_deployment_is_skipped(self):
        (self.dist/'solo48/castle.svg').write_bytes(b'old')
        self.assertIn('solo/castle',script.mark_processed(self.database,self.dist)['skipped'])
        self.assertIsNone(self.db.execute("SELECT * FROM reviews WHERE icon='solo/castle'").fetchone())
        self.assertEqual(self.db.execute('SELECT id FROM feedback').fetchone()[0],987)

    def test_approval_rejection_and_newer_pending_survive(self):
        for status,at in [('approve','2026-09-14T00:00:00+00:00'),('rejected','2026-09-14T00:00:00+00:00'),('pending','2026-09-16T00:00:00+00:00')]:
            with self.subTest(status=status):
                with self.db:
                    self.db.execute("DELETE FROM reviews WHERE icon='solo/castle'")
                    self.db.execute('INSERT INTO reviews VALUES (?,?,?,?,?)',('solo/castle',self.sha,status,at,'human'))
                self.assertIn('solo/castle',script.mark_processed(self.database,self.dist)['skipped'])
                self.assertEqual(self.db.execute("SELECT status FROM reviews WHERE icon='solo/castle'").fetchone()[0],status)

    def test_newer_feedback_in_other_timezone_is_preserved(self):
        with self.db:self.db.execute("UPDATE feedback SET edited_at='2026-09-15T10:00:00-04:00'")
        self.assertIn('solo/castle',script.mark_processed(self.database,self.dist)['skipped'])
        self.assertIsNone(self.db.execute("SELECT * FROM reviews WHERE icon='solo/castle'").fetchone())
        self.assertEqual(self.db.execute('SELECT id FROM feedback').fetchone()[0],987)

    def test_regenerated_becomes_ready_and_backup_keeps_deleted_records(self):
        with self.db:self.db.execute("INSERT INTO reviews VALUES ('solo/castle',?,'re-generated',?,'feedback-script')",(self.sha,script.PROCESSED_AT))
        result=script.mark_processed(self.database,self.dist)
        self.assertEqual(result['feedback_deleted'],1)
        self.assertEqual(self.db.execute("SELECT status FROM reviews WHERE icon='solo/castle'").fetchone()[0],'ready')
        backup=sqlite3.connect(result['backup'])
        try:
            self.assertEqual(backup.execute('SELECT id FROM feedback').fetchone()[0],987)
            self.assertEqual(backup.execute("SELECT status FROM reviews WHERE icon='solo/castle'").fetchone()[0],'re-generated')
        finally:backup.close()
        again=script.mark_processed(self.database,self.dist)
        self.assertEqual(again['feedback_deleted'],0)
        self.assertEqual(again['already_ready'],['solo/castle'])
        init_database(self.database)
        self.assertEqual(self.db.execute("SELECT status FROM reviews WHERE icon='solo/castle' AND svg_sha256=?",(self.sha,)).fetchone()[0],'ready')

    def test_failed_status_write_rolls_back_feedback_deletion(self):
        with self.db:self.db.execute("CREATE TRIGGER fail_ready BEFORE INSERT ON reviews WHEN NEW.icon='solo/castle' BEGIN SELECT RAISE(ABORT,'test failure'); END")
        with self.assertRaises(sqlite3.IntegrityError):script.mark_processed(self.database,self.dist)
        self.assertEqual(self.db.execute('SELECT id FROM feedback').fetchone()[0],987)

    def test_alias_feedback_is_removed(self):
        with patch.object(script,'ICON_ALIASES',{'solo/old-castle':'solo/castle'}):
            with self.db:self.db.execute("UPDATE feedback SET icon='solo/old-castle'")
            self.assertEqual(script.mark_processed(self.database,self.dist)['feedback_deleted'],1)
            self.assertEqual(self.db.execute('SELECT count(*) FROM feedback').fetchone()[0],0)


if __name__=='__main__':unittest.main()
