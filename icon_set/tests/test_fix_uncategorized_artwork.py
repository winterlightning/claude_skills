"""fix_uncategorized_artwork: database-held edits and uploads take their catalog category."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from icon_set.scripts import fix_uncategorized_artwork as fix
from icon_set.scripts.stroke_edits import effective_validation_status, graph_sha256

U1 = '00000000-0000-4000-8000-000000000001'


def edit_document(category):
    graph = {'category': category, 'contours': [[0, 0, 10, 10]]}
    return {'icon': 'solo/lever', 'edited': {'edited_graph': graph, 'source_svg_sha256': 'abc',
                                             'validation': {'status': 'pass', 'graph_sha256': graph_sha256(graph)}}}


class FixUncategorizedArtworkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.gallery = root / 'gallery'
        self.gallery.mkdir()
        (self.gallery / 'icons.json').write_text(json.dumps({'icons': [
            {'key': 'solo/lever', 'icon_id': 'lever', 'category': 'tools'}]}))
        (self.gallery / 'primitives.json').write_text(json.dumps({'rows': [
            {'uuid': U1, 'concept': 'Process Box', 'category': 'programing', 'path': 'programing/p.svg'},
            {'uuid': None, 'concept': 'Lever', 'category': 'primitives-generate', 'path': '_uncategorized_01/l.svg',
             'models': ['lever']},
            {'uuid': None, 'concept': 'Grid Layout', 'category': 'construction', 'path': 'construction/g.svg'},
            {'uuid': None, 'concept': 'Grid Layout', 'category': 'construction', 'path': 'construction/h.svg'},
            {'uuid': None, 'concept': 'grid layout', 'category': 'primitives-generate', 'path': '_uncategorized_02/g.svg'}]}))
        self.database = root / 'feedback.sqlite3'
        with sqlite3.connect(self.database) as connection:
            connection.execute('CREATE TABLE icon_artwork (icon TEXT PRIMARY KEY, revision INTEGER NOT NULL, source_mode TEXT, '
                               'updated_by TEXT, updated_at TEXT, document TEXT NOT NULL)')
            connection.execute('CREATE TABLE uploaded_icons (record TEXT, svg TEXT)')
            connection.execute("INSERT INTO icon_artwork VALUES ('solo/lever', 1, 'use_edited', '', '', ?)",
                               (json.dumps(edit_document('Uncategorized')),))
            for record in ({'icon_id': f'process-box-{U1}-upload-1', 'name': 'Box', 'family': 'solo', 'category': 'Uncategorized'},
                           {'icon_id': 'grid-upload-2', 'name': 'Grid Layout', 'family': 'solo', 'category': 'Uncategorized'},
                           {'icon_id': 'grid-upload-3', 'name': 'Grid Layout', 'family': 'icon-72', 'category': 'Uncategorized'},
                           {'icon_id': 'odd-upload-4', 'name': 'Nothing Like It', 'family': 'solo', 'category': 'Uncategorized'}):
                connection.execute('INSERT INTO uploaded_icons VALUES (?, ?)', (json.dumps(record), '<svg/>'))

    def tearDown(self):
        self.tmp.cleanup()

    def rows(self):
        with sqlite3.connect(self.database) as connection:
            edit = json.loads(connection.execute('SELECT document FROM icon_artwork').fetchone()[0])['edited']
            uploads = {json.loads(r)['icon_id']: json.loads(r)['category'] for (r,) in connection.execute('SELECT record FROM uploaded_icons')}
        return edit, uploads

    def test_dry_run_changes_nothing_and_apply_fixes_solo_records(self):
        fix.main(['--database', str(self.database), '--gallery', str(self.gallery)])
        self.assertEqual(self.rows()[0]['edited_graph']['category'], 'Uncategorized')
        fix.main(['--database', str(self.database), '--gallery', str(self.gallery), '--apply'])
        edit, uploads = self.rows()
        self.assertEqual(edit['edited_graph']['category'], 'primitives-generate')  # primitive link beats icons.json
        self.assertEqual(effective_validation_status(edit), 'pass')
        self.assertEqual(uploads, {f'process-box-{U1}-upload-1': 'programing', 'grid-upload-2': 'primitives-generate',
                                   'grid-upload-3': 'Uncategorized', 'odd-upload-4': 'Uncategorized'})
        self.assertEqual(len(list(self.database.parent.glob('feedback.before-categories-*.sqlite3'))), 1)

    def test_stale_category_is_fixed_only_with_stale(self):
        with sqlite3.connect(self.database) as connection:
            connection.execute('UPDATE icon_artwork SET document = ?', (json.dumps(edit_document('objects/tools')),))
        fix.main(['--database', str(self.database), '--gallery', str(self.gallery), '--apply'])
        self.assertEqual(self.rows()[0]['edited_graph']['category'], 'objects/tools')
        fix.main(['--database', str(self.database), '--gallery', str(self.gallery), '--stale', '--apply'])
        edit = self.rows()[0]
        self.assertEqual(edit['edited_graph']['category'], 'primitives-generate')
        self.assertEqual(effective_validation_status(edit), 'pass')

    def test_unaccepted_edit_stays_unaccepted(self):
        document = edit_document('Uncategorized')
        document['edited']['validation']['graph_sha256'] = 'stale'
        fix.recategorize_edit(document, 'tools')
        self.assertEqual(effective_validation_status(document['edited']), 'not-run')


if __name__ == '__main__':
    unittest.main()
