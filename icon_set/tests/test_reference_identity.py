"""Identical art must not erase distinct source-to-model links."""
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from icon_set.scripts.gallery import original_sources, copy_originals


class ReferenceIdentityTests(unittest.TestCase):
    def test_distinct_ids_survive_while_batch_copies_collapse(self):
        ids = ['11111111-1111-4111-8111-111111111111',
               '22222222-2222-4222-8222-222222222222']
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            sources = root / 'pictographic-primitives'
            sources.mkdir()
            paths = [sources / f'first_{ids[0]}.svg',
                     sources / f'second_{ids[1]}.svg',
                     sources / 'batch' / f'copy_{ids[0]}.svg']
            for path in paths:
                path.parent.mkdir(exist_ok=True)
                path.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
            module = SimpleNamespace(SOURCE_ICON_ID=ids[0], SOURCE_PATH=str(paths[0]),
                                     SOURCE_REFERENCES=[(ids[1], str(paths[1]))])
            factory = SimpleNamespace(__module__='_reference_identity_fixture')
            with patch('icon_set.scripts.gallery.REPO_ROOT', root), \
                 patch('icon_set.model.icons.registry.factories', return_value={'example': factory}), \
                 patch.dict(sys.modules, {'_reference_identity_fixture': module}):
                selected = original_sources()['example']
                self.assertEqual(len(selected), 2)
                for uid in ids:
                    self.assertEqual(sum(uid in path.name for path in selected), 1)
                target = root / 'gallery'
                target.mkdir()
                records = copy_originals(selected, target)
                self.assertEqual(len(records), 2)
                self.assertNotEqual(records[0]['source_path'], records[1]['source_path'])
                self.assertEqual(records[0]['url'], records[1]['url'])
