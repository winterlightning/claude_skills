"""Standalone results advance retrieval without mutating gallery state."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts import next_icon


class StandaloneResultTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def bundle(self, uid='source-a', run='run-1', **changes):
        folder = self.root / 'results' / uid / run
        folder.mkdir(parents=True)
        artifacts = ['sample.py', 'sample.svg', 'sample.metadata.json']
        for name in artifacts:
            (folder / name).write_text('{}')
        result = dict(source_uuid=uid, icon_id='sample', validation_status='valid',
                      visual_review={'status': 'reviewed'}, artifacts=artifacts)
        result.update(changes)
        (folder / 'result.json').write_text(json.dumps(result))
        return folder

    def test_only_complete_valid_reviewed_bundles_count(self):
        self.bundle()
        self.bundle('invalid', validation_status='invalid')
        self.bundle('warning', validation_warnings=['uncertified'])
        self.bundle('unreviewed', visual_review={})
        missing = self.bundle('missing')
        (missing / 'sample.svg').unlink()
        broken = self.bundle('broken')
        (broken / 'result.json').write_text('{')
        self.assertEqual(next_icon.completed_result_sources(self.root / 'results'), {'source-a'})

    def test_successful_retry_counts_and_read_is_nonmutating(self):
        self.bundle(validation_status='invalid')
        self.bundle(run='run-2')
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(next_icon.completed_result_sources(self.root / 'results'), {'source-a'})
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_parameter_free_retrieval_advances_and_explicit_uuid_explains(self):
        self.bundle()
        gallery = self.root / 'gallery'
        gallery.mkdir()
        rows = [dict(uuid=uid, path=f'{uid}.svg', concept=uid, category='Other')
                for uid in ('source-a', 'source-b')]
        (gallery / 'primitives.json').write_text(json.dumps({'rows': rows}))
        for row in rows:
            (self.root / row['path']).write_text('<svg/>')
        with patch.object(next_icon, 'DEFAULT_DIST', self.root), \
                patch.object(next_icon, 'load_decisions', return_value=({}, {}, True)), \
                patch.object(next_icon, 'originals_by_source', return_value={}), \
                patch.object(next_icon, 'primitive_results_dir', return_value=self.root / 'results'), \
                patch.object(next_icon, 'primitives_root', return_value=self.root):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(next_icon.main([]), 0)
            self.assertIn('source UUID: source-b', output.getvalue())
            with self.assertRaisesRegex(SystemExit, 'completed valid standalone result'):
                next_icon.main(['--uuid', 'source-a'])
