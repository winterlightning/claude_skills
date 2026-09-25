"""Metadata migration, edits, publication, and validation regressions."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from icon_set.model import metadata
from icon_set.model.icons.registry import factories


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'source'
        self.patch = patch.object(metadata, 'ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.icon = SimpleNamespace(icon_id='sample-icon', family='solo',
                                    keywords=('sample',), aliases=('example',), category='objects')

    def test_seed_and_preserve_editorial_fields(self):
        original = metadata.load_metadata(self.icon, create=True)
        self.assertEqual(original['tags'], ['sample'])
        path = metadata.metadata_path(self.icon)
        original.update(name='Custom name', description='Custom description', tags=['custom'], extra={'future': True})
        path.write_text(json.dumps(original))
        self.assertEqual(metadata.load_metadata(self.icon, create=True), original)
        self.assertEqual(metadata.record_metadata(self.icon)['description'], 'Custom description')

    def test_categories_default_to_the_model_and_fill_old_sidecars(self):
        self.assertEqual(metadata.defaults(self.icon)['categories'], ['objects'])
        many = SimpleNamespace(**{**vars(self.icon), 'category': 'health', 'categories': ('health', 'state')})
        self.assertEqual(metadata.defaults(many)['categories'], ['health', 'state'])
        document = metadata.load_metadata(self.icon, create=True)
        del document['categories']
        document['category'] = 'food'
        metadata.metadata_path(self.icon).write_text(json.dumps(document))
        self.assertEqual(metadata.load_metadata(self.icon)['categories'], ['food'])
        self.assertEqual(metadata.record_metadata(self.icon)['categories'], ['food'])

    def test_read_does_not_write(self):
        metadata.load_metadata(self.icon)
        self.assertFalse(self.root.exists())

    def test_bad_metadata_fails_with_path(self):
        valid = metadata.load_metadata(self.icon, create=True)
        path = metadata.metadata_path(self.icon)
        for changes in ({'icon_id': 'wrong'}, {'tags': 'sample'}, {'tags': [{}]},
                        {'tags': ['same', 'same']}, {'categories': 'food'}, {'name': ' '}, {'schema_version': True}):
            with self.subTest(changes=changes):
                path.write_text(json.dumps({**valid, **changes}))
                with self.assertRaisesRegex(ValueError, 'sample-icon.json'):
                    metadata.load_metadata(self.icon)
        path.write_text('{')
        with self.assertRaisesRegex(ValueError, 'sample-icon.json'):
            metadata.load_metadata(self.icon)

    def test_cached_records_refresh_and_stale_sidecars_are_pruned(self):
        out = Path(self.tmp.name) / 'dist'
        record = {'icon_id': self.icon.icon_id, 'family': self.icon.family, 'name': 'Old name', 'svg_sha256': 'unchanged'}
        registered = {self.icon.icon_id: self.icon}
        metadata.publish_metadata([record], out, registered)
        path = metadata.metadata_path(self.icon)
        self.assertFalse(path.exists(), 'Publishing must not seed source metadata')
        document = metadata.load_metadata(self.icon, create=True)
        document.update(name='Edited name', description='Search description', tags=['new tag'])
        path.write_text(json.dumps(document))
        metadata.publish_metadata([record], out, registered)
        self.assertEqual(record['name'], 'Edited name')
        self.assertEqual(record['tags'], ['new tag'])
        self.assertEqual(record['svg_sha256'], 'unchanged')
        self.assertEqual(json.loads((out / 'sample-icon.metadata.json').read_text()), document)
        published = out / 'sample-icon.metadata.json'
        before = published.stat().st_mtime_ns
        metadata.publish_metadata([record], out, registered)
        self.assertEqual(published.stat().st_mtime_ns, before)
        metadata.publish_metadata([], out, registered)
        self.assertEqual(list(out.iterdir()), [])

    def test_all_registered_icons_have_valid_metadata(self):
        # Inspect the real corpus rather than the temporary store.
        root = Path(metadata.__file__).resolve().parents[1] / 'metadata'
        for icon in factories().values():
            metadata.load_metadata(icon, root=root)

    def test_to_record_reads_sidecar(self):
        icon = next(iter(factories().values()))()
        document = metadata.load_metadata(icon, create=True)
        document.update(name='Edited', description='Description', tags=['searchable'])
        metadata.metadata_path(icon).write_text(json.dumps(document))
        record = icon.to_record()
        self.assertEqual(record['name'], 'Edited')
        self.assertEqual(record['description'], 'Description')
        self.assertEqual(record['tags'], ['searchable'])


if __name__ == '__main__':
    unittest.main()
