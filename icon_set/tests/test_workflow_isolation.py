"""Production releases cannot mutate agent sources or consume local manual state."""
import inspect
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from icon_set.scripts import build, deploy
from icon_set.scripts.release import export_release
from icon_set.tests.test_icon_upload import IconUploadTests


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.source = self.root / 'build'
        (self.source / 'gallery').mkdir(parents=True)
        (self.source / 'gallery/index.html').write_text('gallery')
        (self.source / 'gallery/icons.json').write_text('{"icons": []}')
        self.target = self.root / 'releases/one'

    def test_export_isolated_and_never_overwrites(self):
        state = self.root / 'state/feedback.sqlite3'
        state.parent.mkdir()
        state.write_bytes(b'preserve production state')
        export_release(self.source, self.target)
        self.assertEqual((self.target / 'gallery/index.html').read_text(), 'gallery')
        self.assertFalse((self.target / 'feedback.sqlite3').exists())
        (self.source / 'gallery/index.html').write_text('changed development')
        self.assertEqual((self.target / 'gallery/index.html').read_text(), 'gallery')
        with self.assertRaises(ValueError):
            export_release(self.source, self.target)
        self.assertEqual(state.read_bytes(), b'preserve production state')

    def test_release_refuses_baked_manual_artwork(self):
        (self.source / 'manifest.json').write_text(json.dumps({'icons': [{'artwork_source': 'use_upload'}]}))
        with self.assertRaisesRegex(ValueError, 'manual artwork'):
            export_release(self.source, self.target)
        self.assertFalse(self.target.exists())

    def test_build_defaults_are_the_tracked_output_and_original_only(self):
        self.assertEqual(build.DEFAULT_DIST, deploy.DEFAULT_DIST)
        self.assertEqual(build.DEFAULT_DIST.name, 'published')
        self.assertEqual(build.DEFAULT_PNG, build.DEFAULT_DIST / 'previews-png')
        self.assertFalse(deploy.DEFAULT_DB.is_relative_to(build.DEFAULT_DIST))
        self.assertIsNone(inspect.signature(build.build).parameters['artwork_dir'].default)
        from icon_set.scripts.generation import GenerationManager
        manager = GenerationManager(self.root, self.source, self.root / 'jobs')
        with patch.object(manager, 'command') as command:
            manager.build(self.root, 'solo', self.root / 'log', icon=Path('sample.py'))
        self.assertNotIn('--artwork-dir', command.call_args.args[0])

    def test_active_build_blocks_release_without_partial_output(self):
        from icon_set.scripts.workspace import output_lock
        with output_lock(self.source):
            with self.assertRaisesRegex(ValueError, 'busy'):
                export_release(self.source, self.target)
        self.assertFalse(self.target.exists())
        export_release(self.source, self.target)
        self.assertTrue((self.target / 'release.json').is_file())

    def test_release_cannot_be_used_as_build_output(self):
        export_release(self.source, self.target)
        with self.assertRaisesRegex(ValueError, 'must be served with --production'):
            deploy.create_server(self.target, self.root/'state/feedback.sqlite3', port=0)
        before = (self.target / 'gallery/icons.json').read_bytes()
        with self.assertRaisesRegex(ValueError, 'production release'):
            build._build_selected([], self.target, None, write_png=False)
        self.assertEqual((self.target / 'gallery/icons.json').read_bytes(), before)

    def test_production_refuses_checkout_and_overlapping_state(self):
        with self.assertRaisesRegex(ValueError, 'outside the source checkout'):
            deploy.create_server(self.source, deploy.DEFAULT_DB, port=0, production=True)
        with self.assertRaisesRegex(ValueError, 'outside the persistent state'):
            deploy.create_server(self.source, self.root / 'feedback.sqlite3', port=0, production=True)


class ProductionTests(IconUploadTests):
    # Run the existing upload/edit/review/restart contract under production mode too.
    def start(self):
        self.server = deploy.create_server(self.dist, self.database, port=0, production=True)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def test_runtime_advertises_manual_only_capabilities(self):
        status, runtime = self.call('GET', '/api/runtime')
        self.assertEqual(status, 200)
        self.assertEqual(runtime, {'mode': 'production', 'can_generate': False,
                                  'can_edit': True, 'can_upload': True})

    def test_agent_and_source_mutations_are_disabled(self):
        self.assertFalse(hasattr(self.server, 'generation'))
        self.assertFalse(hasattr(self.server, 'ai_feedback'))
        for route in ('/api/generation', '/api/generation/accept', '/api/generation/discard',
                      '/api/ai-feedback', '/api/icons/discard', '/api/feedback-db/sync',
                      '/api/combination-refresh', '/api/combination-experiment'):
            for method in ('GET', 'POST'):
                with self.subTest(route=route, method=method):
                    self.assertEqual(self.call(method, route, {} if method == 'POST' else None)[0], 403)

    def test_manual_choice_survives_replacement_of_original(self):
        self.login()
        original = dict(self.icon)
        svg = self.svg.replace('48 48', '32 32').replace('r="16"', 'r="10"')
        status, saved = self.call('POST', '/api/icon-artwork', dict(
            icon=original['key'], svg_sha256=original['svg_sha256'], revision=0,
            source_mode='use_upload', svg=svg))
        self.assertEqual(status, 200, saved)
        selected_sha = saved['record']['svg_sha256']
        updated = dict(original, svg_sha256='new-python-original')
        (self.dist / 'gallery/icons.json').write_text(json.dumps({'icons': [updated]}))
        current = self.call('GET', '/gallery/icons.json')[1]['icons'][0]
        self.assertEqual(current['svg_sha256'], selected_sha)
        self.assertEqual(current['artwork_source'], 'use_upload')
        self.assertEqual(current['generated_svg_sha256'], 'new-python-original')
