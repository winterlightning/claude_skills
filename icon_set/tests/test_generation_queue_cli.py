"""CLI offset forwarding without contacting a running gallery."""
import contextlib
import io
import json
import unittest
import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch

from icon_set.scripts import generation_queue


class GenerationQueueCliTests(unittest.TestCase):
    def test_offline_reads_saved_state_without_network_or_writes(self):
        from icon_set.scripts.primitive_briefs import init_primitive_briefs
        from icon_set.scripts.primitive_status import init_primitive_status
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'gallery').mkdir()
            rows = [dict(uuid=str(i), path=f'{i}.svg', concept=f'Object {i}',
                         category='Objects', state='todo') for i in range(3)]
            (root / 'gallery/primitives.json').write_text(json.dumps({'rows': rows}))
            database = root / 'review.sqlite3'
            with sqlite3.connect(database) as connection:
                init_primitive_status(connection)
                init_primitive_briefs(connection)
                connection.execute('CREATE TABLE activity_log (id INTEGER, username TEXT, action TEXT, icon TEXT, details TEXT, created_at TEXT)')
                connection.execute("INSERT INTO primitive_briefs VALUES ('1','solo','Keep the editorial detail.','editor','today')")
                connection.execute("INSERT INTO activity_log VALUES (1,'editor','primitive_todo','primitive:1',?, 'today')",
                                   (json.dumps({'authority': 'user'}),))
            connection.close()
            before = database.read_bytes()
            with patch.object(generation_queue, 'urlopen', side_effect=AssertionError('Network used')), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(generation_queue.main(['1', '--offline', '--limit', '1',
                                 '--dist', str(root), '--database', str(database)]), 0)
            result = json.loads(output.getvalue())
            self.assertEqual(result['total'], 3)
            self.assertEqual(result['next_offset'], 2)
            self.assertEqual(result['briefs'][0]['uuid'], '1')
            self.assertIn('Keep the editorial detail.', result['briefs'][0]['brief'])
            self.assertTrue(result['briefs'][0]['classification_decision']['authoritative'])
            self.assertEqual(database.read_bytes(), before)

    def test_offline_missing_database_fails_without_creating_it(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'gallery').mkdir()
            (root / 'gallery/primitives.json').write_text('{"rows": []}')
            database = root / 'missing.sqlite3'
            with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(generation_queue.main(['--offline', '--dist', str(root),
                                                       '--database', str(database)]), 1)
            self.assertEqual(output.getvalue(), '')
            self.assertFalse(database.exists())

    def test_offset_forms_preserve_queue_response(self):
        response = {'briefs': [{'uuid': 'source-id', 'brief': 'Keep editorial detail.'}]}
        for argv, offset in [([], 0), (['10'], 10), (['0'], 0), (['--offset', '50'], 50),
                             (['10', '--limit', '3'], 10)]:
            with self.subTest(argv=argv), patch.object(
                generation_queue, 'fetch_generation_queue', return_value=response
            ) as fetch, contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(generation_queue.main(argv), 0)
                self.assertEqual(fetch.call_args.args[3], offset)
                self.assertEqual(fetch.call_args.args[2], 3 if '--limit' in argv else 10)
                self.assertEqual(json.loads(output.getvalue()), response)

    def test_bad_or_duplicate_offsets_fail_before_fetch(self):
        for argv in [['-1'], ['no'], ['--offset', '-1'], ['10', '--offset', '20']]:
            with self.subTest(argv=argv), patch.object(
                generation_queue, 'fetch_generation_queue'
            ) as fetch, contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    generation_queue.main(argv)
                self.assertEqual(error.exception.code, 2)
                fetch.assert_not_called()


if __name__ == '__main__':
    unittest.main()
