"""Production builds must not depend on ignored historical report inputs."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from icon_set.scripts import side_combination_progress as progress
from icon_set.scripts import sub_repair_review as repair


class HistoricalReportTests(unittest.TestCase):
    def test_each_missing_input_is_optional(self):
        cases = (
            (repair, {'icon_set/data/canonical-sub32.json': {},
                      'icon_set/work/sub-profile-migration/qa.json': {}}, 'index.html'),
            (progress, {'output/combinations.json': {'rows': []},
                        'icon_set/data/combination-pairs.json': {'rows': []},
                        'icon_set/data/canonical-sub32.json': {}}, 'side-combination-progress.html'),
        )
        for module, inputs, page in cases:
            for missing in inputs:
                with self.subTest(module=module.__name__, missing=missing), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    for name, value in inputs.items():
                        if name != missing:
                            path = root/name
                            path.parent.mkdir(parents=True, exist_ok=True)
                            path.write_text(json.dumps(value))
                    with patch.object(module, 'ROOT', root):
                        self.assertIsNone(module.stage(root/'output'))
                    self.assertIn('unavailable', (root/'output'/page).read_text())
                    if module is progress:
                        self.assertEqual(json.loads((root/'output/side-combination-progress.json').read_text()),
                                         {'available': False})

    def test_existing_invalid_inputs_still_raise(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ('icon_set/data/canonical-sub32.json', 'icon_set/work/sub-profile-migration/qa.json'):
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('invalid json')
            with patch.object(repair, 'ROOT', root), self.assertRaises(json.JSONDecodeError):
                repair.stage(root/'output')

    def test_complete_empty_inputs_generate_reports(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, value in {'icon_set/data/canonical-sub32.json': {},
                                'icon_set/work/sub-profile-migration/qa.json': {},
                                'icon_set/data/combination-pairs.json': {'rows': []},
                                'output/combinations.json': {'rows': []}}.items():
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(value))
            with patch.object(repair, 'ROOT', root):
                self.assertEqual(repair.stage(root/'repair')['total'], 0)
            with patch.object(progress, 'ROOT', root), patch('icon_set.scripts.category_report.model_catalog', return_value=[]):
                self.assertEqual(progress.stage(root/'output')['side_combinations'], 0)
