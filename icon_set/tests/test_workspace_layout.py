"""Guard source ownership, private agent workspaces and clean deployment updates."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.generation import GenerationManager
from icon_set.scripts.sub_profile_report import build as profile_report
from icon_set.scripts.experiment_gallery import stage_container_experiment


class WorkspaceLayoutTests(unittest.TestCase):
    def test_candidate_has_cli_and_editorial_sources_but_no_runtime_state(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ('icon_set/__init__.py', 'icon_set/__main__.py',
                         'icon_set/model/icons/example.py', 'icon_set/metadata/solo/example.json',
                         'AGENTS.md', 'docs/development-workflow.md',
                         'icon_set/state/feedback.sqlite3', 'icon_set/data/combination-pairs.json',
                         'published/gallery/icons.json'):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('fixture')
            manager = GenerationManager(root, root / 'build', root / 'jobs')
            target = root / 'candidate'
            baseline = manager.snapshot(target)
            self.assertIn('icon_set/__main__.py', baseline)
            self.assertIn('icon_set/metadata/solo/example.json', baseline)
            self.assertIn('AGENTS.md', baseline)
            self.assertFalse((target / 'icon_set/state').exists())
            self.assertFalse((target / 'icon_set/data').exists())
            self.assertFalse((target / 'published').exists())

    def test_profile_staging_writes_summary_only_inside_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixtures = {
                'icon_set/data/sub-profile-migration.json': {'icons': {}},
                'icon_set/data/canonical-sub32.json': {},
                'icon_set/data/icon-profile-links.json': {'links': []},
                'icon_set/work/sub-profile-migration/qa.json': {},
                'icon_set/work/sub-profile-migration/summary.json': {'keep': 'original'},
            }
            before = {}
            for name, document in fixtures.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(document))
                before[name] = path.read_bytes()
            target = root / 'output'
            target.mkdir()
            profile_report(root, target)
            self.assertTrue((target / 'sub-profiles-summary.json').is_file())
            self.assertEqual({name: (root/name).read_bytes() for name in fixtures}, before)

    def test_optional_experiments_do_not_require_old_builds(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest = root / 'icon_set/data/container-solo-trials.json'
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({'results': {'one': {
                'svg_file': 'one.svg', 'main_key': 'container/missing', 'sub_key': 'solo/missing'}}}))
            target = root / 'output'
            target.mkdir()
            with patch('icon_set.scripts.experiment_gallery.ROOT', root):
                result = json.loads(stage_container_experiment(target))
            self.assertEqual(result, {'icons': [], 'unavailable': 1})
            self.assertFalse((root / 'published').exists())

    def test_failed_gallery_does_not_publish_partial_qa(self):
        from icon_set.scripts import build
        from contextlib import redirect_stdout
        import io
        with tempfile.TemporaryDirectory() as temporary:
            dist = Path(temporary) / 'dist'
            previous = dist / 'qa/results.json'
            previous.parent.mkdir(parents=True)
            previous.write_text('{"marker": "previous QA"}')
            with patch.object(build, 'icons_in', return_value=[]), \
                 patch('icon_set.model.icons.registry.all_icons', return_value=[]), \
                 patch.object(build, 'stage_gallery', side_effect=ValueError('broken gallery')), \
                 redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(ValueError, 'broken gallery'):
                    build.build(dist, None, write_png=False, only=['solo'], report=True)
            self.assertEqual(previous.read_text(), '{"marker": "previous QA"}')

    def test_deployment_watcher_refuses_dirty_authoring_checkout(self):
        import watch_deploy
        with patch('sys.argv', ['watch_deploy.py', '--', '--production']), \
             patch.object(watch_deploy, 'git', return_value=' M icon.py'), \
             patch.object(watch_deploy.Deployment, 'start') as start:
            self.assertEqual(watch_deploy.main(), 1)
            start.assert_not_called()
