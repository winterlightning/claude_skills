"""CLI offset forwarding without contacting a running gallery."""
import contextlib
import io
import json
import unittest
from unittest.mock import patch

from icon_set.scripts import generation_queue


class GenerationQueueCliTests(unittest.TestCase):
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
