"""Missing side mains come from side-components.json; saved attempts advance retrieval."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import unittest.mock

from icon_set.scripts import next_side_main


class NextSideMainTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.dist = self.root / 'published'
        self.results = self.root / 'results'
        gallery = self.dist / 'gallery'
        (gallery / 'combination-originals').mkdir(parents=True)
        (self.root / 'prims' / 'other').mkdir(parents=True)
        mains = [
            self.main('done-main', 'Done', status='done'),
            self.main('globe', 'Globe', aliases=['globe-alias'], uses=3),
            self.main('cup', 'Cup'),
            self.main('bare', 'Bare', source=False),
        ]
        (gallery / 'side-components.json').write_text(json.dumps({'mains': mains, 'subs': []}))
        (gallery / 'combination-originals' / 'bare.svg').write_text('<svg/>')

    def main(self, uid, concept, status='missing', aliases=(), uses=1, source=True):
        path = f'prims/other/{concept}_{uid}.svg'
        if source:
            (self.root / path).write_text('<svg/>')
        return dict(id=uid, concept=concept, status=status, uses=uses,
                    source_ids=[uid, *aliases], source_path=path if source else None,
                    reference_url=f'combination-originals/{uid}.svg',
                    pairs=[dict(id=f'{uid}-pair', concept=f'{concept} pair'),
                           dict(id=f'{uid}-pair2', concept='second'), dict(id=f'{uid}-pair3', concept='third')])

    def bundle(self, folder_uid, source_uuid=None, result=True):
        folder = self.results / folder_uid / 'run-1'
        folder.mkdir(parents=True)
        (folder / 'sample.py').write_text('')
        if result:
            (folder / 'result.json').write_text(json.dumps({'source_uuid': source_uuid or folder_uid}))

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = next_side_main.main(list(argv), root=self.root, dist=self.dist, results=self.results)
            except SystemExit as error:
                code = error.code
        return code, out.getvalue()

    def test_first_missing_main_in_file_order_with_context(self):
        code, text = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn('concept: Globe\nsource UUID: globe\nreference: prims/other/Globe_globe.svg\n', text)
        self.assertIn('category: other\naliases: globe-alias\nuses: 3\n', text)
        self.assertIn('published/gallery/combination-originals/globe-pair.svg — Globe pair', text)
        self.assertIn('globe-pair2.svg', text)
        self.assertNotIn('globe-pair3', text)

    def test_saved_attempts_skip_by_id_or_alias_and_unfinished_retry(self):
        self.bundle('globe-alias')
        self.assertIn('source UUID: cup', self.run_main()[1])
        self.bundle('cup', result=False)
        self.assertIn('source UUID: cup', self.run_main()[1])

    def test_offset_uuid_and_reference_fallback(self):
        self.assertIn('source UUID: cup', self.run_main('--offset', '1')[1])
        code, text = self.run_main('--uuid', 'bare')
        self.assertIn('reference: published/gallery/combination-originals/bare.svg', text)
        self.assertIn('not missing', self.run_main('--uuid', 'done-main')[0])
        self.bundle('globe')
        self.assertIn('already has a saved', self.run_main('--uuid', 'globe')[0])
        self.assertIn('only 2 missing', self.run_main('--offset', '2')[0])

    def test_read_is_nonmutating(self):
        self.bundle('cup')
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.run_main()
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})


class NextSideSubTests(NextSideMainTests):
    """Subs share retrieval; text/number marks from the review database stay out."""

    def setUp(self):
        super().setUp()
        staged = self.dist / 'gallery' / 'side-components.json'
        data = json.loads(staged.read_text())
        data['subs'], data['mains'] = data['mains'], []
        staged.write_text(json.dumps(data))
        self.database = self.root / 'feedback.sqlite3'

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = next_side_main.main(list(argv), role='sub', root=self.root, dist=self.dist,
                                           results=self.results, database=self.database)
            except SystemExit as error:
                code = error.code
        return code, out.getvalue()

    def test_text_marks_are_excluded(self):
        statuses = {'globe-alias': {'reason': 'text_number'}}
        with unittest.mock.patch.object(next_side_main, 'load_decisions', return_value=(statuses, {}, True)):
            self.assertIn('source UUID: cup', self.run_main()[1])
            self.assertIn('text/number', self.run_main('--uuid', 'globe')[0])


if __name__ == '__main__':
    unittest.main()
