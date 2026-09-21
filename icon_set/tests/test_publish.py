"""The committed publication contains assets, never local runtime state."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.publish import publish_assets
from icon_set.scripts import deploy


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.source = self.root / 'build'
        self.destination = self.root / 'published'
        (self.source / 'gallery').mkdir(parents=True)
        (self.source / 'solo48').mkdir()
        self.row = {'icon_id': 'sample', 'family': 'solo', 'artwork_source': 'use_org'}
        (self.source / 'gallery/index.html').write_text('gallery')
        (self.source / 'gallery/icons.json').write_text(json.dumps({'icons': [self.row]}))
        (self.source / 'solo48/manifest.json').write_text(json.dumps({'icons': [self.row]}))
        (self.source / 'solo48/sample.svg').write_text('<svg/>')

    def test_publish_replace_and_exclude_temporary_output(self):
        (self.source / 'qa').mkdir()
        (self.source / 'qa/temporary.png').write_bytes(b'temporary')
        (self.source / 'feedback.sqlite3').write_bytes(b'private')
        state = self.root / 'state'
        state.mkdir()
        database = state / 'feedback.sqlite3'
        database.write_bytes(b'production reviews')
        marker = publish_assets(self.source, self.destination)
        self.assertFalse((self.destination / 'qa').exists())
        self.assertFalse((self.destination / 'feedback.sqlite3').exists())
        self.assertEqual(marker['catalog_sha256'], hashlib.sha256(
            (self.destination / 'gallery/icons.json').read_bytes()).hexdigest())
        (self.destination / 'stale.svg').write_text('old')
        publish_assets(self.source, self.destination)
        self.assertFalse((self.destination / 'stale.svg').exists())
        self.assertEqual(database.read_bytes(), b'production reviews')

    def test_manual_artwork_rejected_without_replacing_previous_catalog(self):
        publish_assets(self.source, self.destination)
        previous = (self.destination / 'release.json').read_bytes()
        self.row['artwork_source'] = 'use_edited'
        (self.source / 'solo48/manifest.json').write_text(json.dumps({'icons': [self.row]}))
        with self.assertRaisesRegex(ValueError, 'Manual artwork'):
            publish_assets(self.source, self.destination)
        self.assertEqual((self.destination / 'release.json').read_bytes(), previous)

    def test_nested_runtime_state_is_rejected(self):
        (self.source / 'gallery/reviews.sqlite3').write_bytes(b'private')
        with self.assertRaisesRegex(ValueError, 'Runtime state'):
            publish_assets(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_symlink_and_overlap_rejected(self):
        with self.assertRaises(ValueError):
            publish_assets(self.source, self.source / 'published')
        (self.source / 'gallery/link.svg').symlink_to(self.source / 'solo48/sample.svg')
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            publish_assets(self.source, self.destination)

    def test_empty_catalog_rejected(self):
        (self.source / 'gallery/icons.json').write_text('{"icons":[]}')
        with self.assertRaisesRegex(ValueError, 'empty'):
            publish_assets(self.source, self.destination)

    def test_review_drafts_are_not_counted_as_release_icons(self):
        draft = {**self.row, 'icon_id': 'draft', 'release_eligible': False, 'managed_draft': True}
        (self.source / 'gallery/icons.json').write_text(json.dumps({'icons': [self.row, draft]}))
        marker = publish_assets(self.source, self.destination)
        self.assertEqual((marker['icons'], marker['release_icons'], marker['managed_drafts']), (2, 1, 1))

    def test_production_does_not_import_local_progression_snapshot(self):
        publish_assets(self.source, self.destination)
        with patch.object(deploy, 'import_snapshot') as snapshot:
            server = deploy.create_server(self.destination, self.root / 'state/feedback.sqlite3',
                                          production=True, port=0)
            server.server_close()
        snapshot.assert_not_called()

    def test_committed_publication_allowed_with_external_state(self):
        publish_assets(self.source, self.destination)
        with patch.object(deploy, 'PACKAGE_ROOT', self.root / 'icon_set'), \
             patch('icon_set.scripts.workspace.PUBLISHED_DIST', self.destination):
            external = tempfile.TemporaryDirectory()
            self.addCleanup(external.cleanup)
            server = deploy.create_server(self.destination, Path(external.name) / 'state/feedback.sqlite3',
                                          production=True, port=0)
            server.server_close()
            with self.assertRaisesRegex(ValueError, 'database.*outside'):
                deploy.create_server(self.destination, self.root / 'state/feedback.sqlite3', production=True, port=0)
