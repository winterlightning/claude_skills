"""Keep the same serving process online while completed catalogs change."""
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch
from urllib.request import urlopen

from icon_set.scripts import automatic_deploy as updates
from icon_set.scripts import deploy


class LiveDeploymentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.releases = self.root/'releases'
        self.releases.mkdir()
        self.initial = self.root/'build'
        self.gallery(self.initial, 'old')

    def gallery(self, path, label):
        (path/'gallery').mkdir(parents=True)
        (path/'gallery/index.html').write_text(label)
        (path/'gallery/icons.json').write_text('{"icons":[],"failed_icons":[]}')

    def test_http_server_switches_and_rolls_back_without_socket_restart(self):
        database = self.root/'state/feedback.sqlite3'
        with patch.object(deploy, 'import_snapshot'):
            server = deploy.create_server(self.initial, database, port=0, production=True,
                                          live_release_root=self.releases)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            address = f'http://127.0.0.1:{server.server_address[1]}'
            def read():
                with urlopen(address+'/gallery/index.html') as response:
                    return response.read().decode()
            descriptor = server.socket.fileno()
            self.assertEqual(read(), 'old')
            updates.bootstrap(self.releases, self.initial)
            candidate = self.releases/'slot-b'
            self.gallery(candidate/'assets', 'new')
            (candidate/'assets/release.json').write_text('{"deployment_id":"new"}')
            (candidate/'deployment.json').write_text('{"commit":"new-commit"}')
            process = Mock()
            updates.promote_live(self.releases, candidate, process,
                                 lambda *_: self.assertEqual(read(), 'new'))
            self.assertEqual(read(), 'new')
            self.assertEqual(server.socket.fileno(), descriptor)
            process.start.assert_not_called()
            process.stop.assert_not_called()
            previous = updates.read_active(self.releases)
            rollback_candidate = self.releases/'slot-a'
            (rollback_candidate/'deployment.json').write_text('{"commit":"bad"}')
            with self.assertRaisesRegex(RuntimeError, 'bad response'):
                updates.promote_live(self.releases, rollback_candidate, process,
                                     Mock(side_effect=RuntimeError('bad response')))
            self.assertEqual(updates.read_active(self.releases), previous)
            self.assertEqual(read(), 'new')
            process.stop.assert_not_called()
            self.assertTrue(database.exists())
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_baseline_available_before_network_or_build(self):
        self.assertEqual(updates.select_baseline(self.root, self.releases, self.initial), self.initial.resolve())
        from types import SimpleNamespace
        import signal
        args = SimpleNamespace(seed_dist=self.initial, python='python3', host='127.0.0.1', port=8000,
                               health_timeout=1, primitives=None, remote='origin', branch='icon-lib',
                               interval=60, no_restart_on_crash=False)
        process = Mock()
        process.died.return_value = False
        sequence = []
        process.start.side_effect = lambda: sequence.append('server')
        def fetch(*_):
            sequence.append('fetch')
            self.assertEqual(sequence[0], 'server')
            self.assertTrue((self.releases/'active.json').is_file())
            signal.getsignal(signal.SIGINT)(signal.SIGINT, None)
            return 'revision'
        with patch.object(updates, 'wait_healthy'), \
             patch('concurrent.futures.ThreadPoolExecutor') as pool:
            self.assertEqual(updates._watch(args, self.root, self.releases, self.root/'state/db',
                                          Mock(return_value=process), fetch, Mock()), 0)
        self.assertEqual(sequence, ['server', 'fetch'])
        process.start.assert_called_once()
        pool.return_value.submit.assert_called_once()

    def test_bootstrap_freezes_existing_assets_without_building_or_state_copy(self):
        updates.bootstrap(self.releases, self.initial)
        (self.initial/'gallery/index.html').write_text('build in progress')
        live = deploy.live_directory(self.initial, self.releases)
        self.assertEqual((live/'gallery/index.html').read_text(), 'old')
        self.assertFalse((live/'feedback.sqlite3').exists())

    def test_client_disconnect_is_quiet_but_application_errors_are_not_hidden(self):
        from http.server import SimpleHTTPRequestHandler
        handler = object.__new__(deploy.GalleryHandler)
        for error in (BrokenPipeError(), ConnectionResetError()):
            with patch.object(SimpleHTTPRequestHandler, 'handle', side_effect=error):
                handler.handle()
                self.assertTrue(handler.close_connection)
        with patch.object(SimpleHTTPRequestHandler, 'handle', side_effect=ValueError('application bug')):
            with self.assertRaisesRegex(ValueError, 'application bug'):
                handler.handle()

    def test_health_check_consumes_complete_html_response(self):
        import io
        runtime = io.BytesIO(b'{"mode":"production"}')
        page = Mock()
        page.read.return_value = b'large page' * 10000
        page.__enter__ = Mock(return_value=page)
        page.__exit__ = Mock(return_value=False)
        process = Mock()
        process.died.return_value = False
        with patch.object(updates, 'urlopen', side_effect=[runtime, page]):
            updates.wait_healthy(process, '127.0.0.1', 8000, 1)
        page.read.assert_called_once_with()

    def test_live_pointer_cannot_escape_release_storage(self):
        updates.write_marker(self.releases, {'release':'../outside'})
        with self.assertRaises(ValueError):
            deploy.live_directory(self.initial, self.releases)


if __name__ == '__main__':
    unittest.main()
