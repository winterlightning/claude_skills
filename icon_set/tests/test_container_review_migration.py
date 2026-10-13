"""Reference registration tests against the actual D1 schema in temporary SQLite files."""
from copy import deepcopy
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from cloud.migrate import migrate_container_review as migration

SHA = 'a' * 64


def record(key='solo/example', source='original'):
    review = {'key': key, 'recommended_action': 'split_into_components',
              'combination_type': 'container_combination', 'source_reference_id': source,
              'current_effective_svg_sha256': SHA, 'current_state': 'rejected',
              'components': [{'role': role, 'reference_id': role, 'match_status': 'verified_existing',
                              'requires_role_adaptation': False} for role in migration.ROLES]}
    return {'icon': key, 'source_reference_id': source, 'svg_sha256': SHA,
            'concept': 'Example', 'review': review}


class ContainerMigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'snapshot.sqlite3'
        self.db = sqlite3.connect(self.path)
        self.addCleanup(self.db.close)
        migrations = migration.ROOT / 'cloud/worker/migrations'
        self.db.executescript((migrations / '0001_schema.sql').read_text())
        self.db.executescript(next(migrations.glob('0009*')).read_text())
        for ref in ['container', 'symbol', 'original']:
            self.db.execute('INSERT INTO "references"(reference_id,kind,source) VALUES (?,\'single\',\'test\')', (ref,))
        self.add_icon('solo/example', 'original')
        self.data = {'records': [record()]}
        self.db.commit()

    def add_icon(self, key, source):
        self.db.execute('INSERT INTO icons(key,name,family,svg_sha256,pushed_at) VALUES (?,\'Example\',\'solo\',?,\'now\')', (key, SHA))
        self.db.execute('INSERT INTO icon_references VALUES (?,?)', (key, source))
        self.db.execute('INSERT INTO reviews(icon,svg_sha256,status,updated_at) VALUES (?,?,\'rejected\',\'now\')', (key, SHA))

    def pair(self, ref, roles=('container', 'symbol')):
        self.db.execute('INSERT INTO "references"(reference_id,kind,source) VALUES (?,\'combination\',\'test\')', (ref,))
        for role, part in zip(roles, ('container', 'symbol')):
            self.db.execute('INSERT INTO reference_parts(reference_id,role,part_reference_id) VALUES (?,?,?)', (ref, role, part))

    def migrate(self):
        return migration.migrate_rows(self.db, self.data, 'digest', 'tester', {})

    def test_register_and_rerun_preserves_reviews_and_drawing(self):
        before = self.db.execute('SELECT * FROM reviews').fetchall()
        self.assertEqual(self.migrate()['counts'], {'registered': 1})
        self.assertEqual(self.migrate()['counts'], {'reused': 1})
        self.assertEqual(self.db.execute('SELECT count(*) FROM reference_parts').fetchone()[0], 2)
        self.assertEqual(self.db.execute('SELECT count(*) FROM activity_log').fetchone()[0], 1)
        self.assertEqual(self.db.execute('SELECT * FROM reviews').fetchall(), before)
        self.assertEqual(self.db.execute('SELECT svg_sha256 FROM icons').fetchone()[0], SHA)
        self.assertEqual(self.db.execute('SELECT icon FROM reference_parts').fetchall(), [(None,), (None,)])

    def test_existing_exact_pair_is_reused(self):
        self.pair('existing')
        row = self.migrate()['records'][0]
        self.assertEqual((row['status'], row['combination_reference_id']), ('reused', 'existing'))
        self.assertEqual(self.db.execute('SELECT kind FROM "references" WHERE reference_id=\'original\'').fetchone()[0], 'single')

    def test_side_pair_is_not_a_container_duplicate(self):
        self.pair('side', ('main', 'sub'))
        self.assertEqual(self.migrate()['counts'], {'registered': 1})

    def test_ambiguous_duplicate_pairs_held(self):
        self.pair('existing1')
        self.pair('existing2')
        self.assertIn('multiple_existing_combinations', self.migrate()['records'][0]['issues'])

    def test_same_batch_pair_created_only_once(self):
        self.add_icon('solo/second', 'second')
        self.data['records'].append(record('solo/second', 'second'))
        self.assertEqual(self.migrate()['counts'], {'registered': 1, 'reused': 1})

    def test_missing_original_reference_is_created(self):
        self.db.execute('DELETE FROM "references" WHERE reference_id=\'original\'')
        self.assertEqual(self.migrate()['records'][0]['operation'], 'created_reference')

    def test_stale_review_cannot_authorize_new_revision(self):
        self.db.execute('UPDATE reviews SET svg_sha256=?', ('b'*64,))
        self.assertIn('source_is_no_longer_rejected', self.migrate()['records'][0]['issues'])

    def test_changed_drawing_held(self):
        self.db.execute('UPDATE icons SET svg_sha256=?', ('b'*64,))
        self.assertIn('source_drawing_changed_or_missing', self.migrate()['records'][0]['issues'])

    def test_uncertain_component_is_held(self):
        for field, value in [('match_status', 'ambiguous'), ('match_limitation', 'near alternative'),
                             ('requires_role_adaptation', True), ('match_kind', 'functional_equivalent')]:
            with self.subTest(field=field):
                self.data = {'records': [record()]}
                self.data['records'][0]['review']['components'][0][field] = value
                self.assertEqual(self.migrate()['counts'], {'held': 1})
        self.assertEqual(self.db.execute('SELECT count(*) FROM reference_parts').fetchone()[0], 0)

    def test_dry_run_unchanged_apply_has_backup(self):
        original = self.path.read_bytes()
        report = migration.run(self.path, self.data, 'digest', 'tester')
        self.assertEqual(report['counts'], {'registered': 1})
        self.assertEqual(self.path.read_bytes(), original)
        report = migration.run(self.path, self.data, 'digest', 'tester', apply=True)
        with sqlite3.connect(report['backup']) as backup:
            self.assertEqual(backup.execute('SELECT count(*) FROM reference_parts').fetchone()[0], 0)
        self.assertEqual(self.db.execute('SELECT count(*) FROM reference_parts').fetchone()[0], 2)

    def test_failed_apply_rolls_back(self):
        self.db.execute("CREATE TRIGGER fail_log BEFORE INSERT ON activity_log BEGIN SELECT RAISE(ABORT, 'test failure'); END")
        self.db.commit()
        with self.assertRaises(sqlite3.IntegrityError):
            migration.run(self.path, self.data, 'digest', 'tester', apply=True)
        self.assertEqual(self.db.execute('SELECT count(*) FROM reference_parts').fetchone()[0], 0)
        self.assertEqual(self.db.execute('SELECT kind FROM "references" WHERE reference_id=\'original\'').fetchone()[0], 'single')

    def test_prepare_handoff_keeps_source_and_excludes_side(self):
        source = Path(self.tmp.name) / 'review.json'
        other = deepcopy(record()['review'])
        other.update(key='solo/other', combination_type='side_combination')
        raw = json.dumps({'schema': 'pictographic-correction-handoff/v1',
                          'source_metadata': {'schema': migration.SOURCE_SCHEMA},
                          'records': [record()['review'], other]}).encode()
        source.write_bytes(raw)
        out = Path(self.tmp.name) / 'prepared'
        migration.prepare(source, out, 1)
        loaded, _ = migration.load_input(out / 'input.json')
        self.assertEqual(len(loaded['records']), 1)
        self.assertEqual((out / 'source-review.json').read_bytes(), raw)
        migration.prepare(source, out, 1)
        with self.assertRaises(ValueError):
            migration.prepare(source, Path(self.tmp.name) / 'wrong-count', 2)


if __name__ == '__main__':
    unittest.main()
