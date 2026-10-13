"""Offline rejection import: preserve evidence, route decisions, and never mutate shared state."""
from copy import deepcopy
import contextlib
import io
import json
from pathlib import Path
import socket
import sqlite3
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.scripts import import_rejected_review as importer

FIXTURE = Path(__file__).parent / 'fixtures/rejected_review_representative.json'


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.data, self.digest = importer.read_review(FIXTURE)
        self.record = self.data['records'][0]

    def plan(self, expected=None):
        return importer.build_plan(self.data, self.digest, expected)

    def add(self, key, action, kind=None):
        record = deepcopy(self.record)
        record.update(key=key, recommended_action=action, combination_type=kind)
        self.data['records'].append(record)
        return record

    def test_parent_example_preserves_identity_without_claiming_readiness(self):
        before = deepcopy(self.data)
        plan = self.plan()
        row = plan['groups']['container_combinations'][0]
        self.assertEqual(row['review'], self.record)
        self.assertEqual(self.data, before)
        self.assertEqual(row['status'], 'pending_human_review')
        self.assertIn('human_review_required', row['issues'])
        self.assertIn('reference_mapping_requires_api_support', row['issues'])
        self.assertEqual([p['role'] for p in row['component_checks']], ['container', 'symbol'])
        for part in row['component_checks']:
            self.assertIn('assembly_readiness_unverified', part['issues'])
        self.assertIn('functional_equivalent_contour_review', row['component_checks'][0]['issues'])
        self.assertIn('reference_limitation_review', row['component_checks'][0]['issues'])
        refs = plan['reference_index']
        self.assertFalse(refs['independently_rechecked'])
        self.assertEqual(set(refs['references']), {p['reference_id'] for p in self.record['components']})

    def test_action_drives_split_counts_not_combination_type(self):
        for action in ('retain_family_review', 'author_new_drawing', 'recategorize_family', 'unknown'):
            self.add('solo/' + action, action, 'container_combination')
        side = self.add('solo/side', importer.SPLIT, 'side_combination')
        side['components'][0]['role'] = 'main'
        side['components'][1]['role'] = 'side_sub'
        self.add('solo/unresolved', importer.SPLIT, None)
        plan = self.plan({'total': 7, 'split_into_components': 3, 'container_combinations': 1,
                          'side_combinations': 1, 'other_recommendations': 4, 'unresolved_splits': 1})
        row = plan['groups']['side_combinations'][0]
        self.assertEqual([p['role'] for p in row['component_checks']], ['main', 'sub'])
        self.assertEqual(row['review']['components'][1]['role'], 'side_sub')
        self.assertNotIn('split_roles_require_review', row['issues'])

    def test_nested_and_ambiguous_components_remain_unresolved(self):
        parent = self.record['components'][0]
        parent['components'] = [{
            'role': 'main', 'match_status': 'ambiguous', 'reference_id': 'not-verified',
            'candidate_reference_ids': ['candidate-a', 'candidate-b'],
            'absence_proven': False, 'visual_description': 'Unresolved nested component',
        }]
        row = self.plan()['groups']['container_combinations'][0]
        self.assertIn('nested_split_requires_review', row['issues'])
        child = row['component_checks'][1]
        self.assertEqual(child['path'], 'components[0].components[0]')
        self.assertIsNone(child['verified_reference_id'])
        self.assertIn('ambiguous_reference', child['issues'])
        self.assertIn('reference_absence_not_proven', child['issues'])
        self.assertEqual(row['review']['components'][0]['components'], parent['components'])
        self.assertNotIn('not-verified', self.plan()['reference_index']['references'])

    def test_container_sub_is_not_silently_changed_to_symbol(self):
        self.record['components'][1]['role'] = 'sub'
        row = self.plan()['groups']['container_combinations'][0]
        self.assertIn('split_roles_require_review', row['issues'])
        self.assertIn('component_role_review', row['component_checks'][1]['issues'])
        self.assertEqual(row['component_checks'][1]['role'], 'sub')

    def test_reference_reuse_retains_every_occurrence_and_adaptation(self):
        other = self.add('container/second', importer.SPLIT, 'container_combination')
        other['components'][0]['requires_role_adaptation'] = True
        plan = self.plan()
        uses = plan['reference_index']['references'][self.record['components'][0]['reference_id']]
        self.assertEqual([use['key'] for use in uses], [self.record['key'], other['key']])
        self.assertIn('role_adaptation_required', uses[1]['issues'])

    def test_unknown_fields_and_unknown_action_survive(self):
        self.record['future_field'] = {'reviewer_text': 'Preserve verbatim', 'nested': [1, 2]}
        self.record['recommended_action'] = 'future_action'
        self.record['existing_human_review'] = {'status': 'rejected', 'feedback': 'Keep feedback'}
        row = self.plan()['groups']['other_recommendations'][0]
        self.assertEqual(row['review'], self.record)
        self.assertIn('unrecognized_action', row['issues'])

    def test_missing_revisions_refs_and_readiness_are_not_inferred(self):
        self.record.pop('current_effective_svg_sha256')
        self.record['source_reference_id'] = None
        self.record['current_state'] = 'ready'
        self.record['components'][0].pop('reference_id')
        row = self.plan()['groups']['container_combinations'][0]
        self.assertIn('source_revision_missing_or_invalid', row['issues'])
        self.assertIn('source_reference_missing', row['issues'])
        self.assertIn('source_state_is_not_rejected', row['issues'])
        self.assertIsNone(row['component_checks'][0]['verified_reference_id'])

    def test_all_ready_claims_still_require_human_review(self):
        for part in self.record['components']:
            part.update(assembly_readiness_verified=True, requires_role_adaptation=False,
                        match_kind='exact', limitation=None)
        row = self.plan()['groups']['container_combinations'][0]
        self.assertEqual(row['status'], 'pending_human_review')
        self.assertIn('human_review_required', row['issues'])

    def test_schema_duplicate_keys_and_non_recommendations_are_rejected(self):
        for change in ('schema', 'duplicate', 'authorization', 'components'):
            with self.subTest(change=change):
                data = deepcopy(self.data)
                if change == 'schema':
                    data['metadata']['schema'] = 'another-schema'
                elif change == 'duplicate':
                    data['records'].append(deepcopy(self.record))
                elif change == 'authorization':
                    data['records'][0]['recommendation_only'] = False
                else:
                    data['records'][0]['components'] = {'main': 'not an array'}
                with self.assertRaises(ValueError):
                    importer.build_plan(data, self.digest)

    def test_only_encoded_existing_get_routes_are_suggested(self):
        self.record['key'] = 'solo/a & b?#'
        row = self.plan()['groups']['container_combinations'][0]
        self.assertEqual(row['read_checks'], [
            {'method': 'GET', 'path': '/api/icon?key=solo%2Fa+%26+b%3F%23'},
            {'method': 'GET', 'path': '/api/review-detail?icon=solo%2Fa+%26+b%3F%23'},
        ])

    def test_cli_is_offline_atomic_and_preserves_edited_work(self):
        with TemporaryDirectory() as temp:
            out = Path(temp) / 'bundle'
            argv = ['--file', str(FIXTURE), '--out', str(out), '--expect-count', 'total=1']
            with patch.object(socket, 'socket', side_effect=AssertionError('network forbidden')), \
                 patch.object(sqlite3, 'connect', side_effect=AssertionError('database forbidden')), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(importer.main(argv), 0)
                first = {path.name: path.read_bytes() for path in out.iterdir()}
                self.assertEqual(importer.main(argv), 0)
                self.assertEqual(first, {path.name: path.read_bytes() for path in out.iterdir()})
                self.assertEqual((out / 'source-review.json').read_bytes(), FIXTURE.read_bytes())
                (out / 'container_combinations.json').write_text('human edit')
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    importer.main(argv)
                self.assertEqual((out / 'container_combinations.json').read_text(), 'human edit')
            self.assertEqual(sorted(p.name for p in Path(temp).iterdir()), ['bundle'])

    def test_count_mismatch_and_bad_json_write_nothing(self):
        with TemporaryDirectory() as temp:
            out = Path(temp) / 'not-created'
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                importer.main(['--file', str(FIXTURE), '--out', str(out), '--expect-count', 'total=379'])
            self.assertFalse(out.exists())
            source = Path(temp) / 'bad.json'
            for content in ('{"metadata":{},"metadata":{}}', '{"value":NaN}'):
                source.write_text(content)
                with self.assertRaises(ValueError):
                    importer.read_review(source)

    def test_staging_failure_leaves_no_partial_bundle(self):
        with TemporaryDirectory() as temp:
            out = Path(temp) / 'bundle'
            with patch.object(Path, 'write_bytes', side_effect=OSError('disk full')):
                with self.assertRaises(OSError):
                    importer.write_bundle(out, {'manifest.json': b'{}'})
            self.assertFalse(out.exists())
            self.assertEqual(list(Path(temp).iterdir()), [])


if __name__ == '__main__':
    unittest.main()
