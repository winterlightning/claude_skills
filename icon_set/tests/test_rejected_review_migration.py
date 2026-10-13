"""All-case migration tests, with real D1 schemas and state-preservation checks."""
from copy import deepcopy
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from cloud.migrate import migrate_rejected_review as migration
from icon_set.tests.test_container_review_migration import record, SHA


class AllReviewMigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'snapshot.sqlite3'
        self.db = sqlite3.connect(self.path)
        self.addCleanup(self.db.close)
        m = migration.ROOT / 'cloud/worker/migrations'
        for prefix in ['0001', '0002', '0003', '0009_combination', '0015', '0017', '0018', '0019']:
            self.db.executescript(next(m.glob(prefix+'*')).read_text())
        self.source = record()['review']
        self.source.update(current_name='Example', current_family='solo', work_group='font48_routing',
                           recommended_action='retain_family_review', components=[])
        self.source['latest_diagnosis'] = {'proposed_section': 'Font 48', 'execution_lane': 'routing_plan_ready',
                                         'text_identity': {'character_count': 1}, 'required_fix': 'Route existing A'}
        raw = json.dumps({'key': 'solo/example', 'icon_id': 'example', 'name': 'Example', 'family': 'solo',
                          'canvas_size': 48, 'profile': 'SOLO48'})
        self.db.execute("INSERT INTO icons(key,icon_id,name,family,canvas_size,svg_sha256,record,card,pushed_at,state,profile) VALUES ('solo/example','example','Example','solo',48,?,?,?,'now','rejected','SOLO48')", (SHA,raw,raw))
        self.db.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at) VALUES ('solo/example',?,'rejected','now')", (SHA,))
        self.db.commit()

    def run_migration(self, source=None):
        return migration.migrate_all(self.db, {'records': [source or self.source]}, 'digest', 'tester', {})

    def test_font_routing_updates_card_counts_preserves_artwork_and_reviews(self):
        before = self.db.execute('SELECT * FROM reviews').fetchall()
        self.assertEqual(self.run_migration()['counts'], {'routed': 1})
        row = self.db.execute('SELECT family,card,record,svg_sha256,canvas_size,profile FROM icons').fetchone()
        self.assertEqual(row[0], 'font-48')
        self.assertEqual(json.loads(row[1])['family'], 'font-48')
        self.assertEqual(json.loads(row[2])['family'], 'font-48')
        self.assertEqual(row[3:], (SHA, 48, 'SOLO48'))
        self.assertEqual(self.db.execute('SELECT * FROM reviews').fetchall(), before)
        self.assertEqual(self.db.execute('SELECT family,n FROM icon_counts').fetchall(), [('font-48', 1)])
        self.assertEqual(self.run_migration()['counts'], {'already_routed': 1})
        self.assertEqual(self.db.execute('SELECT count(*) FROM review_data_migrations').fetchone()[0], 1)

    def test_multi_character_routing_preserves_native_size_and_repair(self):
        d=self.source['latest_diagnosis']
        d.update(proposed_section='Sub-icon',text_identity={'character_count': 4},artwork_required_fix='Separate four letters')
        report=self.run_migration()
        self.assertEqual(report['counts'], {'routed': 1})
        self.assertIn('artwork_repair_still_required',report['records'][0]['issues'])
        self.assertEqual(self.db.execute('SELECT family,side_role,canvas_size FROM icons').fetchone(), ('solo','sub',48))

    def test_stale_approved_claimed_and_changed_family_are_held(self):
        for change in ["UPDATE icons SET svg_sha256='changed'", "UPDATE reviews SET status='approve'",
                       "UPDATE reviews SET status='claimed'", "UPDATE icons SET family='upload'"]:
            with self.subTest(change=change):
                self.db.execute('SAVEPOINT test')
                self.db.execute(change)
                self.assertEqual(self.run_migration()['counts'], {'held': 1})
                self.assertEqual(self.db.execute('SELECT count(*) FROM upload_families').fetchone()[0],0)
                self.db.execute('ROLLBACK TO test')
                self.db.execute('RELEASE test')

    def test_artwork_decisions_and_no_defect_do_not_change_status(self):
        for group,lane,status in [('missing_extra_detail','artwork_fix_brief_ready','artwork_required'),
                                  ('uncertain_intended_usage','decision_required','held'),
                                  ('plausible_mistaken_rejection','human_reverification_no_redraw','human_reverification')]:
            self.source.update(work_group=group,latest_diagnosis={'execution_lane':lane,'required_fix':'Preserved brief'})
            self.assertEqual(self.run_migration()['counts'], {status:1})
        self.assertEqual(self.db.execute('SELECT status FROM reviews').fetchone()[0],'rejected')
        self.assertEqual(self.db.execute('SELECT count(*) FROM activity_log').fetchone()[0],0)

    def test_side_pair_roles_and_deduplication(self):
        r=deepcopy(record()['review'])
        r.update(current_name='Example',current_family='solo',work_group='side_combination',combination_type='side_combination')
        for c,role in zip(r['components'],['main','side_sub']): c['role']=role
        for ref in ['original','container','symbol']:
            self.db.execute('INSERT INTO "references"(reference_id,kind,source) VALUES (?,\'single\',\'test\')',(ref,))
        self.db.execute("INSERT INTO icon_references VALUES ('solo/example','original')")
        del r['source_reference_id']  # resolved from the unique actual database link
        self.assertEqual(self.run_migration(r)['counts'],{'registered':1})
        self.assertEqual(self.db.execute('SELECT role FROM reference_parts ORDER BY role').fetchall(),[('main',),('sub',)])
        self.assertEqual(self.run_migration(r)['counts'],{'reused':1})

    def test_all_case_apply_rollback(self):
        self.db.execute("CREATE TRIGGER fail_activity BEFORE INSERT ON activity_log BEGIN SELECT RAISE(ABORT,'test failure'); END")
        self.db.commit()
        with self.assertRaises(sqlite3.IntegrityError):
            migration.combinations.run(self.path,{'records':[self.source]},'digest','tester',apply=True,runner=migration.migrate_all)
        self.assertEqual(self.db.execute('SELECT family FROM icons').fetchone()[0],'solo')
        self.assertEqual(self.db.execute('SELECT count(*) FROM upload_families').fetchone()[0],0)

if __name__ == '__main__':
    unittest.main()
