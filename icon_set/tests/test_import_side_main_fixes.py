"""A promotion must not resurrect an older drawing or change its geometry."""
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts import import_side_main_fixes as importer


class ImportSideMainFixTests(unittest.TestCase):
    def test_incomplete_latest_run_blocks_older_complete_run(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old, new = root / 'test-id' / 'old', root / 'test-id' / 'new'
            for stamp, folder in enumerate((old, new), 1):
                folder.mkdir(parents=True)
                module = folder / 'test_id.py'
                module.write_text('')
                os.utime(module, ns=(stamp, stamp))
            (old / 'result.json').write_text('{}')
            with patch.object(importer, 'primitive_results_dir', return_value=root):
                with self.assertRaisesRegex(ValueError, 'no completed result'):
                    importer.newest_run({'id': 'test-id'})
                (new / 'result.json').write_text('{}')
                # Recording an approval for an old result must not supersede a redraw.
                os.utime(old / 'result.json', ns=(100, 100))
                self.assertEqual(importer.newest_run({'id': 'test-id'})[0], new)

    def test_preserves_registered_identity_without_rewriting_geometry_method(self):
        source = ('class Drawing:\n    icon_id = "new"\n    category = "general"\n'
                  '    def build(self):\n        return [(6, 6), (42, 42)]\n')
        edited = importer.override(source, {'icon_id': 'registered', 'category': 'travel'})
        cls = importer.load(edited, Path('fixture.py'))
        self.assertEqual(cls.icon_id, 'registered')
        self.assertEqual(cls.category, 'travel')
        self.assertEqual(cls().build(), [(6, 6), (42, 42)])


if __name__ == '__main__':
    unittest.main()
