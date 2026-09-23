"""The committed publication is validated and compacted in place, never carrying runtime state."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.publish import finalize_publication, publication_plan
from icon_set.scripts import deploy


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.dist = self.root / 'published'
        (self.dist / 'gallery').mkdir(parents=True)
        (self.dist / 'solo48').mkdir()
        self.row = {'icon_id': 'sample', 'family': 'solo', 'artwork_source': 'use_org'}
        (self.dist / 'gallery/index.html').write_text('gallery')
        (self.dist / 'gallery/icons.json').write_text(json.dumps({'icons': [self.row]}, indent=2))
        (self.dist / 'solo48/manifest.json').write_text(json.dumps({'icons': [self.row]}))
        (self.dist / 'solo48/sample.svg').write_text('<svg/>')

    def test_finalize_compacts_catalogs_and_ignores_regenerated_qa(self):
        (self.dist / 'qa').mkdir()
        (self.dist / 'qa/temporary.png').write_bytes(b'temporary')
        marker = finalize_publication(self.dist)
        catalog = (self.dist / 'gallery/icons.json').read_bytes()
        self.assertEqual(catalog, b'{"icons":[{"icon_id":"sample","family":"solo","artwork_source":"use_org"}]}\n')
        self.assertEqual(marker['catalog_sha256'], hashlib.sha256(catalog).hexdigest())
        self.assertEqual((self.dist / 'solo48/sample.svg').read_text(), '<svg/>')
        self.assertTrue((self.dist / 'qa/temporary.png').exists())
        self.assertEqual(json.loads((self.dist / 'release.json').read_text())['publication'], 'git')

    def test_manual_artwork_rejected_without_touching_previous_marker(self):
        finalize_publication(self.dist)
        previous = (self.dist / 'release.json').read_bytes()
        self.row['artwork_source'] = 'use_edited'
        (self.dist / 'solo48/manifest.json').write_text(json.dumps({'icons': [self.row]}))
        with self.assertRaisesRegex(ValueError, 'Manual artwork'):
            finalize_publication(self.dist)
        self.assertEqual((self.dist / 'release.json').read_bytes(), previous)

    def test_runtime_state_is_rejected_before_any_rewrite(self):
        (self.dist / 'gallery/reviews.sqlite3').write_bytes(b'private')
        pretty = (self.dist / 'gallery/icons.json').read_text()
        with self.assertRaisesRegex(ValueError, 'Runtime state'):
            finalize_publication(self.dist)
        self.assertEqual((self.dist / 'gallery/icons.json').read_text(), pretty)
        self.assertFalse((self.dist / 'release.json').exists())

    def test_symlink_rejected(self):
        (self.dist / 'gallery/link.svg').symlink_to(self.dist / 'solo48/sample.svg')
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            finalize_publication(self.dist)

    def test_empty_catalog_rejected(self):
        (self.dist / 'gallery/icons.json').write_text('{"icons":[]}')
        with self.assertRaisesRegex(ValueError, 'empty'):
            finalize_publication(self.dist)

    def test_review_drafts_are_not_counted_as_release_icons(self):
        draft = {**self.row, 'icon_id': 'draft', 'release_eligible': False, 'managed_draft': True}
        (self.dist / 'gallery/icons.json').write_text(json.dumps({'icons': [self.row, draft]}))
        marker = finalize_publication(self.dist)
        self.assertEqual((marker['icons'], marker['release_icons'], marker['managed_drafts']), (2, 1, 1))

    def test_production_does_not_import_local_progression_snapshot(self):
        finalize_publication(self.dist)
        with patch.object(deploy, 'import_snapshot') as snapshot:
            server = deploy.create_server(self.dist, self.root / 'state/feedback.sqlite3',
                                          production=True, port=0)
            server.server_close()
        snapshot.assert_not_called()

    def test_development_server_serves_the_publication_directly(self):
        finalize_publication(self.dist)
        with patch('icon_set.scripts.workspace.PUBLISHED_DIST', self.dist):
            server = deploy.create_server(self.dist, self.root / 'state/feedback.sqlite3', port=0)
            server.server_close()
        exported = self.root / 'release'
        exported.mkdir()
        for name in ('gallery/index.html', 'gallery/icons.json', 'release.json'):
            (exported / name).parent.mkdir(exist_ok=True)
            (exported / name).write_text((self.dist / name).read_text())
        with self.assertRaisesRegex(ValueError, 'must be served with --production'):
            deploy.create_server(exported, self.root / 'state/feedback.sqlite3', port=0)

    def test_committed_publication_allowed_with_external_state(self):
        finalize_publication(self.dist)
        with patch.object(deploy, 'PACKAGE_ROOT', self.root / 'icon_set'), \
             patch('icon_set.scripts.workspace.PUBLISHED_DIST', self.dist):
            external = tempfile.TemporaryDirectory()
            self.addCleanup(external.cleanup)
            server = deploy.create_server(self.dist, Path(external.name) / 'state/feedback.sqlite3',
                                          production=True, port=0)
            server.server_close()
            with self.assertRaisesRegex(ValueError, 'database.*outside'):
                deploy.create_server(self.dist, self.root / 'state/feedback.sqlite3', production=True, port=0)

    def test_publication_plan_detects_new_changed_missing_and_unchanged(self):
        class FakeIcon:
            family = 'solo'

            def __init__(self, icon_id, document):
                self.icon_id = icon_id
                self.document = document

            def to_svg(self):
                return self.document

        def factory(icon_id, document):
            class Factory:
                family = 'solo'

                def __new__(cls):
                    return FakeIcon(icon_id, document)
            return Factory

        current = '<svg>current</svg>'
        digest = hashlib.sha256(current.encode()).hexdigest()
        rows = [
            {'icon_id': 'changed', 'svg_sha256': 'old'},
            {'icon_id': 'missing', 'svg_sha256': digest},
            {'icon_id': 'unchanged', 'svg_sha256': digest},
        ]
        (self.dist / 'solo48/manifest.json').write_text(json.dumps({'icons': rows}))
        failed = self.dist / 'failed/solo48'
        failed.mkdir(parents=True)
        (failed / 'manifest.json').write_text(json.dumps({'icons': [
            {'icon_id': 'failed', 'svg_sha256': digest, 'svg': 'failed.svg', 'errors': ['too close']},
        ]}))
        (failed / 'failed.svg').write_text(current)
        for suffix in ('svg', 'metadata.json'):
            path = self.dist / 'solo48' / f'unchanged.{suffix}'
            path.write_text(current if suffix == 'svg' else '{}')
        preview = self.dist / 'previews-png/solo48/unchanged.png'
        preview.parent.mkdir(parents=True)
        preview.write_bytes(b'png')
        registered = {
            'new': factory('new', current),
            'changed': factory('changed', current),
            'failed': factory('failed', current),
            'missing': factory('missing', current),
            'unchanged': factory('unchanged', current),
        }

        plan = publication_plan(
            self.dist, registered=registered, folder_for_family=lambda family: 'solo48'
        )

        self.assertEqual([row['icon_id'] for row in plan['new']], ['new'])
        self.assertEqual([row['icon_id'] for row in plan['changed']], ['changed'])
        self.assertEqual([row['icon_id'] for row in plan['missing']], ['missing'])
        self.assertEqual([row['icon_id'] for row in plan['unchanged']], ['unchanged'])
        self.assertEqual([row['icon_id'] for row in plan['failed']], ['failed'])
        self.assertEqual(plan['failed'][0]['validation'], ['too close'])
        self.assertEqual(plan['errors'], [])
