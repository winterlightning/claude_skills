"""Visual decisions expire on changed drawings, rules, or unreviewed pairs."""
import unittest
from types import SimpleNamespace

from icon_set.validation.spacing_reviews import apply_spacing_reviews


class SpacingReviewTests(unittest.TestCase):
    def setUp(self):
        self.icon = SimpleNamespace(family='solo', icon_id='fixture')
        self.result = {'status': 'review', 'findings': [
            {'elements': ['a', 'b'], 'status': 'review', 'ink_gap': 3.0}]}
        self.records = {'version': 1, 'icons': {'solo/fixture': {
            'svg_sha256': 'drawing', 'rules_sha256': 'rules',
            'elements': [['b', 'a']], 'reviewer': 'test-reviewer',
            'reason': 'Intentional tapered junction, visually inspected.'}}}

    def apply(self, drawing='drawing', rules='rules'):
        return apply_spacing_reviews(self.icon, self.result, drawing, rules, records=self.records)

    def test_review_preserves_measured_evidence(self):
        result = self.apply()
        self.assertEqual(result['status'], 'reviewed')
        self.assertEqual(result['measured_status'], 'review')
        self.assertEqual(result['findings'][0]['ink_gap'], 3.0)
        self.assertEqual(result['findings'][0]['status'], 'review')
        self.assertEqual(self.result['status'], 'review')
        self.assertNotIn('visual_review', self.result['findings'][0])

    def test_changed_drawing_or_rules_invalidates_decision(self):
        self.assertEqual(self.apply(drawing='changed')['status'], 'review')
        self.assertEqual(self.apply(rules='changed')['status'], 'review')

    def test_unreviewed_pair_still_blocks(self):
        self.result['findings'].append({'elements': ['a', 'c'], 'status': 'review'})
        result = self.apply()
        self.assertEqual(result['status'], 'review')
        self.assertEqual(result['reviewed_finding_count'], 1)
        self.assertNotIn('visual_review', result['findings'][1])

    def test_missing_evidence_identity_fails_closed(self):
        del self.records['icons']['solo/fixture']['reason']
        self.assertEqual(self.apply()['status'], 'review')
        self.records['version'] = 2
        self.assertEqual(self.apply()['status'], 'review')

    def test_review_cannot_waive_certified_failures(self):
        from unittest.mock import patch
        from icon_set.tests.test_internal_spacing import cramped_dress
        from icon_set.validation.library_qa import inspect_icon
        icon = cramped_dress()
        measured = inspect_icon(icon)
        records = {'version': 1, 'icons': {f'{icon.family}/{icon.icon_id}': {
            'svg_sha256': measured['svg_sha256'], 'rules_sha256': measured['rules_sha256'],
            'elements': [f['elements'] for f in measured['internal_spacing']['findings']],
            'reviewer': 'test-reviewer', 'reason': 'Test only.'}}}
        with patch('icon_set.validation.library_qa.apply_spacing_reviews',
                   side_effect=lambda icon, result, svg, rules: apply_spacing_reviews(
                       icon, result, svg, rules, records=records)):
            reviewed = inspect_icon(icon)
        self.assertEqual(reviewed['internal_spacing']['status'], 'reviewed')
        self.assertEqual(reviewed['status'], 'fail')
        self.assertEqual(reviewed['errors'], measured['errors'])
        self.assertTrue(any('parallel straight edges' in error for error in reviewed['errors']))


if __name__ == '__main__':
    unittest.main()
