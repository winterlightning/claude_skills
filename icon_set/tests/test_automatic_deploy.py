"""Release preparation must never mutate the active application or manual state."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

from icon_set.scripts import automatic_deploy as deploy


class AutomaticDeploymentTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        self.git('init', '-q')
        self.git('config', 'user.name', 'Deployment Test')
        self.git('config', 'user.email', 'deployment@example.invalid')
        self.write('icon.py', 'original')
        self.write('icon_set/scripts/build.py', '# builder\n')
        self.write('.gitignore', 'private/\nicon_set/dist/\n')
        self.first = self.commit()
        self.write('icon_set/dist/gallery/index.html', 'existing gallery')
        self.write('icon_set/dist/gallery/icons.json', '{"icons":[{"key":"sub/existing"}]}')
        self.releases = self.root / 'releases'
        self.releases.mkdir()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.repo, stderr=subprocess.DEVNULL).decode().strip()

    def write(self, path, text):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def fake_build(self, command, **kwargs):
        source = kwargs['cwd']
        if 'build' in command:
            build = source / 'published'
            (build / 'gallery').mkdir(parents=True, exist_ok=True)
            (build / 'gallery/icons.json').write_text(json.dumps({'icons': [{'key': 'sub/test'}], 'failed_icons': []}))
            (build / 'gallery/index.html').write_text('gallery')
        else:
            from icon_set.scripts.release import export_release
            export_release(source / 'published', Path(command[-1]))
        return subprocess.CompletedProcess(command, 0)

    def test_snapshot_uses_commit_not_dirty_or_private_files_and_keeps_unchanged_mtime(self):
        old = self.root / 'old'
        deploy.snapshot(self.repo, self.first, old)
        self.write('icon.py', 'dirty author work')
        self.write('private/feedback.sqlite3', 'production state')
        self.write('untracked.py', 'untracked')
        new = self.root / 'new'
        deploy.snapshot(self.repo, self.first, new, old)
        self.assertEqual((new/'icon.py').read_text(), 'original')
        self.assertEqual((new/'icon.py').stat().st_mtime, (old/'icon.py').stat().st_mtime)
        self.assertFalse((new/'private').exists())
        self.assertFalse((new/'untracked.py').exists())

    def test_symlink_in_archive_is_rejected(self):
        (self.repo/'escape').symlink_to('/tmp')
        revision = self.commit()
        with self.assertRaisesRegex(ValueError, 'Unsupported link'):
            deploy.snapshot(self.repo, revision, self.root/'new')

    def test_failed_build_keeps_active_release_and_saves_log(self):
        marker = self.releases/'active.json'
        marker.write_text('{"release":"existing"}')
        runner = Mock(return_value=subprocess.CompletedProcess([], 1))
        with self.assertRaisesRegex(RuntimeError, 'preparation failed'):
            deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=runner)
        self.assertEqual(marker.read_text(), '{"release":"existing"}')
        self.assertTrue((self.releases/'last-failed.log').exists())
        self.assertEqual(list(self.releases.glob('.preparing-*')), [])
        runner.assert_called_once()

    def test_release_reuses_previous_outputs_without_hardlinking_or_state(self):
        previous = deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=self.fake_build)
        cached = previous/'assets/cached.svg'
        cached.write_text('keep')
        cache = self.releases/'workspace/source/published/cached.svg'
        cache.write_text('keep')
        state = self.root/'state'
        state.mkdir()
        (state/'feedback.sqlite3').write_text('manual edits')
        self.write('icon.py', 'updated')
        revision = self.commit()
        def runner(command, **kwargs):
            if 'build' in command:
                copy = kwargs['cwd']/'published/cached.svg'
                self.assertEqual(copy.read_text(), 'keep')
                self.assertNotEqual(copy.stat().st_ino, cached.stat().st_ino)
                self.assertNotIn('--all', command)
                self.assertFalse((kwargs['cwd']/'published/release.json').exists())
            return self.fake_build(command, **kwargs)
        updated = deploy.prepare(self.repo, self.releases, revision, sys.executable, previous, runner)
        self.assertEqual(cached.read_text(), 'keep')
        self.assertEqual((updated/'assets/cached.svg').read_text(), 'keep')
        self.assertFalse((updated/'source/icon_set/.local').exists())
        self.assertEqual((state/'feedback.sqlite3').read_text(), 'manual edits')
        self.assertEqual(json.loads((updated/'deployment.json').read_text())['commit'], revision)
        self.assertFalse((self.releases/'active.json').exists())

    def test_shared_pipeline_change_does_not_force_full_revalidation(self):
        previous = deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=self.fake_build)
        self.write('icon_set/scripts/build.py', '# changed validation\n')
        revision = self.commit()
        runner = Mock(side_effect=self.fake_build)
        deploy.prepare(self.repo, self.releases, revision, sys.executable, previous, runner)
        self.assertNotIn('--all', runner.call_args_list[0].args[0])
        self.assertIn('--changed-only', runner.call_args_list[0].args[0])

    def test_unhealthy_new_server_restores_previous_without_switching_pointer(self):
        candidate = deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=self.fake_build)
        marker = self.releases/'active.json'
        marker.write_text('{"release":"previous", "commit":"old"}')
        before = marker.read_bytes()
        old, new = Mock(), Mock()
        with self.assertRaisesRegex(RuntimeError, 'unhealthy'):
            deploy.activate(self.releases, candidate, old, lambda _: new,
                            Mock(side_effect=RuntimeError('unhealthy')))
        old.stop.assert_called_once()
        old.start.assert_called_once()
        new.stop.assert_called_once()
        self.assertEqual(marker.read_bytes(), before)

    def test_success_marks_active_and_preserves_previous_reference(self):
        candidate = deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=self.fake_build)
        (self.releases/'active.json').write_text('{"release":"previous", "commit":"old"}')
        old, new, health = Mock(), Mock(), Mock()
        self.assertIs(deploy.activate(self.releases, candidate, old, lambda _: new, health), new)
        marker = deploy.read_active(self.releases)
        self.assertEqual(marker, {'release': candidate.name, 'commit': self.first, 'previous': 'previous'})
        health.assert_called_once_with(new)
        old.start.assert_not_called()

    def test_production_command_always_uses_external_persistent_state(self):
        state = self.root/'state/feedback.sqlite3'
        command = deploy.server_command(self.releases/'one', sys.executable, state, '127.0.0.1', 8000)
        self.assertIn('--production', command)
        self.assertEqual(command[command.index('--database')+1], str(state))
        self.assertEqual(command[command.index('--dist')+1], str(self.releases/'one/assets'))

    def test_path_overlap_and_traversal_rejected(self):
        for releases, db in [(self.repo/'releases', self.root/'state/db'),
                             (self.releases, self.repo/'state/db'),
                             (self.releases, self.releases/'state/db'),
                             (self.releases, self.root/'db')]:
            with self.assertRaises(ValueError):
                deploy.validate_paths(self.repo, releases, db)
        with self.assertRaises(ValueError):
            deploy.bundle_path(self.releases, '../outside')

    def test_health_requires_matching_release_and_live_process(self):
        from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
        from threading import Thread
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                body = {'/api/runtime': {'mode': 'production'},
                        '/gallery/icons.json': {'icons': [], 'failed_icons': [{'key': 'sub/invalid'}]},
                        '/gallery/index.html': {'ready': True},
                        '/release.json': {'deployment_id': 'expected'}}[self.path]
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(body).encode())
            def log_message(self, *args):
                pass
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            process = Mock()
            process.died.return_value = False
            port = server.server_address[1]
            deploy.wait_healthy(process, '127.0.0.1', port, 1, 'expected')
            with self.assertRaisesRegex(RuntimeError, 'timed out'):
                deploy.wait_healthy(process, '127.0.0.1', port, 0.05, 'wrong-release')
            process.died.return_value = True
            with self.assertRaisesRegex(RuntimeError, 'exited'):
                deploy.wait_healthy(process, '127.0.0.1', port, 1, 'expected')
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_real_subprocess_build_and_export_in_committed_workspace(self):
        # A small CLI fixture exercises subprocess cwd/import isolation and the
        # complete archive -> build -> export flow without a library-wide QA run.
        self.write('icon_set/__init__.py', '')
        self.write('icon_set/__main__.py', """
import json, pathlib, shutil, sys
assert not pathlib.Path('private').exists()
build = pathlib.Path('published')
if sys.argv[1] == 'build':
    (build/'gallery').mkdir(parents=True, exist_ok=True)
    (build/'gallery/index.html').write_text('gallery')
    (build/'gallery/icons.json').write_text(json.dumps({'icons':[{'key':'sub/test'}]}))
else:
    destination = pathlib.Path(sys.argv[2])
    shutil.copytree(build, destination)
    (destination/'release.json').write_text('{}')
""")
        revision = self.commit()
        self.write('private/feedback.sqlite3', 'manual data')
        with patch.dict('os.environ', {'PYTHONPATH': '/invalid/author/workspace'}):
            bundle = deploy.prepare(self.repo, self.releases, revision, sys.executable)
        self.assertTrue((bundle/'assets/gallery/index.html').is_file())
        self.assertTrue(json.loads((bundle/'assets/release.json').read_text())['deployment_id'].startswith(revision))
        self.assertFalse((bundle/'source/private').exists())

    def test_failed_drawings_are_released_for_review_including_failed_only_library(self):
        for passing in ([{'key': 'sub/valid'}], []):
            with self.subTest(passing=bool(passing)):
                def runner(command, **kwargs):
                    result = self.fake_build(command, **kwargs)
                    if 'build' in command:
                        self.assertIn('--allow-validation-failures', command)
                        catalog = kwargs['cwd']/'published/gallery/icons.json'
                        catalog.write_text(json.dumps({'icons': passing,
                                                       'failed_icons': [{'key': 'sub/invalid', 'errors': ['spacing']}]}))
                    return result
                bundle = deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=runner)
                catalog = json.loads((bundle/'assets/gallery/icons.json').read_text())
                self.assertEqual(catalog['failed_icons'][0]['errors'], ['spacing'])
                self.assertEqual(json.loads((bundle/'assets/release.json').read_text())['failed_icons'], 1)

    def test_build_tolerance_only_changes_validation_exit_not_crashes(self):
        from icon_set.scripts import build
        with patch.object(build, '_build_selected', return_value=(0, 3)):
            self.assertEqual(build.build(write_png=False), 1)
            self.assertEqual(build.build(write_png=False, allow_validation_failures=True), 0)
        with patch.object(build, '_build_selected', side_effect=OSError('disk full')):
            with self.assertRaisesRegex(OSError, 'disk full'):
                build.build(write_png=False, allow_validation_failures=True)
        with patch.object(build, 'build', return_value=0) as builder:
            self.assertEqual(build.main(['--no-png', '--allow-validation-failures']), 0)
            self.assertTrue(builder.call_args.kwargs['allow_validation_failures'])

    def test_no_seed_refuses_full_build(self):
        import shutil
        shutil.rmtree(self.repo/'icon_set/dist')
        runner = Mock()
        with self.assertRaisesRegex(ValueError, 'no full build was started'):
            deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=runner)
        runner.assert_not_called()

    def test_repeated_updates_use_two_slots_and_preserve_identical_files(self):
        previous = None
        slots = set()
        for number in range(4):
            self.write('icon.py', str(number))
            revision = self.commit()
            candidate = deploy.prepare(self.repo, self.releases, revision, sys.executable,
                                       previous, self.fake_build)
            slots.add(candidate.name)
            previous = candidate
        self.assertEqual(slots, {'slot-a', 'slot-b'})
        self.assertEqual({p.name for p in self.releases.iterdir() if p.is_dir()},
                         {'slot-a', 'slot-b', 'workspace'})
        source = self.root/'sync-source'
        target = self.root/'sync-target'
        source.mkdir()
        (source/'keep.svg').write_text('unchanged')
        deploy.sync_tree(source, target)
        before = (target/'keep.svg').stat()
        deploy.sync_tree(source, target)
        self.assertEqual(before.st_mtime_ns, (target/'keep.svg').stat().st_mtime_ns)
        self.assertEqual(before.st_ino, (target/'keep.svg').stat().st_ino)
        (source/'keep.svg').unlink()
        deploy.sync_tree(source, target)
        self.assertFalse((target/'keep.svg').exists())

    def test_cleanup_removes_old_releases_but_preserves_active_unknown_and_state(self):
        retired = self.releases/('a'*40+'-old')
        retired.mkdir()
        (retired/'deployment.json').write_text('{}')
        active = self.releases/('b'*40+'-active')
        active.mkdir()
        (active/'deployment.json').write_text('{}')
        (self.releases/'active.json').write_text(json.dumps({'release':active.name}))
        unknown = self.releases/'my-backup'
        unknown.mkdir()
        deploy.cleanup_releases(self.releases)
        self.assertFalse(retired.exists())
        self.assertTrue(active.exists())
        self.assertTrue(unknown.exists())

    def test_changed_only_reuses_existing_geometry_without_qa_even_if_inputs_are_newer(self):
        from icon_set.scripts import build
        from icon_set.model.icons.sub._base import Sub32
        from icon_set.model.keyshapes import Keyshape
        from contextlib import redirect_stdout
        import io
        class Fixture(Sub32):
            icon_id = 'workflow-check'
            keyshape = Keyshape.HRECT_XL
            def build(self):
                self.add_polyline('check', (2,18), (12,28), (30,4))
        def gallery(staged, published, folders):
            target = staged/'gallery'
            target.mkdir()
            (target/'index.html').write_text('gallery')
            (target/'icons.json').write_text('{}')
            return target
        output = self.root/'built'
        with patch.object(build, 'icons_in', return_value=[Fixture()]), \
             patch.object(build, 'stage_gallery', side_effect=gallery), redirect_stdout(io.StringIO()):
            self.assertEqual(build.build(output, None, only=['sub'], write_png=False, report=False), 0)
            with patch.object(build, '_source_mtime', return_value=10**12), \
                 patch.object(build, 'inspect_icon', side_effect=AssertionError('Unchanged icon was revalidated')):
                self.assertEqual(build.build(output, None, only=['sub'], write_png=False,
                                             report=False, changed_only=True), 0)
            # A missing export still requires validation/recreation.
            (output/'sub32/workflow-check.svg').unlink()
            with patch.object(build, 'inspect_icon', wraps=build.inspect_icon) as inspect:
                self.assertEqual(build.build(output, None, only=['sub'], write_png=False,
                                             report=False, changed_only=True), 0)
                self.assertGreater(inspect.call_count, 0)
            # A changed drawing hash cannot reuse the old validation either.
            with patch.object(build, '_drawing_sha', return_value='changed'), \
                 patch.object(build, 'inspect_icon', wraps=build.inspect_icon) as inspect:
                self.assertEqual(build.build(output, None, only=['sub'], write_png=False,
                                             report=False, changed_only=True), 0)
                self.assertGreater(inspect.call_count, 0)

    def test_empty_catalog_never_promoted(self):
        def runner(command, **kwargs):
            result = self.fake_build(command, **kwargs)
            if 'build' in command:
                (kwargs['cwd']/'published/gallery/icons.json').write_text('{"icons": []}')
            return result
        with self.assertRaisesRegex(ValueError, 'empty release'):
            deploy.prepare(self.repo, self.releases, self.first, sys.executable, runner=runner)
        self.assertFalse((self.releases/'active.json').exists())

    def test_missing_optional_report_inputs_does_not_block_clean_checkout(self):
        from icon_set.scripts.sub_profile_report import stage
        (self.repo/'icon_set/assets/sub-profiles').mkdir(parents=True)
        stage(self.root/'gallery', self.repo)
        self.assertFalse((self.root/'gallery').exists())


if __name__ == '__main__':
    unittest.main()
