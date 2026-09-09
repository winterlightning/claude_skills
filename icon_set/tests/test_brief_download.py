"""Download all active briefs, including references, as a portable folder tree."""
from io import BytesIO
import json
import sqlite3
import unittest
from zipfile import ZipFile
from icon_set.tests import test_split_briefs as split_tests
from icon_set.scripts.brief_queue import brief_archive


class BriefDownloadTests(unittest.TestCase):
    setUp = split_tests.SplitWorkflowTests.setUp
    request = split_tests.SplitWorkflowTests.request
    payload = split_tests.SplitWorkflowTests.payload

    def test_download_all_statuses_with_reference_and_restore(self):
        originals = self.dist / 'gallery/originals'
        originals.mkdir(exist_ok=True)
        source = b'<svg xmlns="http://www.w3.org/2000/svg"/>'
        (originals / 'source.svg').write_bytes(source)
        path = self.dist / 'gallery/icons.json'
        catalog = json.loads(path.read_text())
        catalog['icons'][0]['original_sources'] = [{'source_path': 'source.svg', 'url': 'originals/source.svg'}]
        path.write_text(json.dumps(catalog))
        self.assertEqual(self.request('GET', '/api/pending-briefs/download')[0], 404)
        self.assertEqual(self.request('POST', '/api/reject-combination', self.payload())[0], 201)
        with sqlite3.connect(self.database) as connection:
            connection.execute("UPDATE pending_briefs SET status='generated',generated_icon='solo/document' WHERE position=1")
        status, body = self.request('GET', '/api/pending-briefs/download?status=pending')
        self.assertEqual(status, 200)
        with ZipFile(BytesIO(body)) as archive:
            names = archive.namelist()
            metadata = [json.loads(archive.read(n)) for n in names if n.endswith('brief.json')]
            self.assertEqual({r['status'] for r in metadata}, {'pending', 'generated'})
            self.assertEqual({n.split('/')[1] for n in names if n.endswith('brief.md')}, {'solo', 'sub'})
            for name in names:
                if name.endswith('reference.svg'):
                    self.assertEqual(archive.read(name), source)
            self.assertEqual(sum(n.endswith('reference.svg') for n in names), 2)
        self.request('POST', '/api/reject-combination/restore', {'icon':'sub/square','svg_sha256':'abc'})
        self.assertEqual(self.request('GET', '/api/pending-briefs/download')[0], 404)

    def test_missing_or_escaping_reference_keeps_brief_without_leaking_file(self):
        self.request('POST', '/api/reject-combination', self.payload())
        rows = json.loads(self.request('GET', '/api/pending-briefs')[1])
        secret = self.root / 'secret.svg'
        secret.write_text('private source')
        for row in rows:
            row['reference_path'] = '../secret.svg'
            row['name'] = '../../same/name'
        body = brief_archive(rows, {}, self.dist, self.dist)
        with ZipFile(BytesIO(body)) as archive:
            names = archive.namelist()
            self.assertTrue(all('..' not in n.split('/') for n in names))
            self.assertFalse(any(n.endswith('.svg') for n in names))
            self.assertEqual(sum(n.endswith('brief.md') for n in names), 2)
            for name in names:
                if name.endswith('brief.md'):
                    self.assertIn('Unavailable on this server', archive.read(name).decode())
