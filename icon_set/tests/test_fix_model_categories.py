"""fix_model_categories: a model's categories come from its source pictoicon record."""
import io
import json
from pathlib import Path
import tempfile
import unittest
import unittest.mock

from icon_set.scripts import fix_model_categories as fix

VALID = {'food', 'animals', 'avatars', 'symbol', 'state', 'container', 'primitives-generate', 'Uncategorized'}
MODEL = '''SOURCE_ICON_ID = {uuid!r}


class Drawing(Solo48):
    icon_id = 'bread'
{category}
    def build(self):
        pass
'''


class CategoryFromTokensTests(unittest.TestCase):
    def test_topic_wins(self):
        self.assertEqual(fix.category_from_tokens('food primitives primitives-generate'.split()), 'food')
        self.assertEqual(fix.category_from_tokens('war container-combination bottom-right'.split()), 'war')

    def test_type_fallback(self):
        self.assertEqual(fix.category_from_tokens('other state'.split()), 'primitives-generate')
        self.assertEqual(fix.category_from_tokens('primitives primitives-generate'.split()), 'primitives-generate')
        self.assertEqual(fix.category_from_tokens('state symbol'.split()), 'symbol')
        self.assertEqual(fix.category_from_tokens(['container']), 'container')
        self.assertIsNone(fix.category_from_tokens('primitive primitives'.split()))


class ResolveTests(unittest.TestCase):
    records = {'u1': ['food', 'primitives'], 'u2': ['primitive', 'primitives']}

    def test_pictoicon_keeps_every_token(self):
        self.assertEqual(fix.resolve('u1', 'objects/food', self.records, VALID),
                         ('food', ('food', 'primitives'), 'pictoicon'))

    def test_no_topic_keeps_valid_else_uncategorized(self):
        self.assertEqual(fix.resolve('u2', 'avatars', self.records, VALID),
                         ('avatars', ('primitive', 'primitives'), 'kept'))
        self.assertEqual(fix.resolve('u2', 'objects', self.records, VALID),
                         ('Uncategorized', ('primitive', 'primitives'), 'pictoicon has no topic or type'))

    def test_concept_name_category_goes_first(self):
        self.assertEqual(fix.resolve('u2', 'objects', self.records, VALID, {'u2': 'animals'}),
                         ('animals', ('animals', 'primitive', 'primitives'), 'concept name'))
        self.assertEqual(fix.resolve('u1', 'objects', self.records, VALID, {'u1': 'animals'})[0], 'food')

    def test_no_record(self):
        self.assertEqual(fix.resolve('', 'avatars', self.records, VALID), ('avatars', ('avatars',), 'kept'))
        self.assertEqual(fix.resolve('', 'nature/animals', self.records, VALID), ('animals', ('animals',), 'alias'))
        self.assertEqual(fix.resolve('', 'objects/misc', self.records, VALID), (None, (), 'no SOURCE_ICON_ID'))


class RewriteTests(unittest.TestCase):
    def test_every_class_keeps_quotes(self):
        text = "class A:\n    category = \"objects/general\"\n\nclass B:\n    category='objects/food'\n"
        self.assertEqual(fix.rewrite(text, 'food', ('food', 'state')),
                         "class A:\n    category = \"food\"\n    categories = (\"food\", \"state\")\n\n"
                         "class B:\n    category = 'food'\n    categories = ('food', 'state')\n")

    def test_rewrite_replaces_old_categories_and_is_stable(self):
        once = fix.rewrite("class A:\n    category = 'x'\n    categories = ('x',)\n", 'food', ('food',))
        self.assertEqual(once, "class A:\n    category = 'food'\n    categories = ('food',)\n")
        self.assertEqual(fix.rewrite(once, 'food', ('food',)), once)

    def test_inserted_after_icon_id(self):
        self.assertEqual(fix.rewrite("class A:\n    icon_id = 'a'\n", 'food', ('food',)),
                         "class A:\n    icon_id = 'a'\n    category = 'food'\n    categories = ('food',)\n")


class MetadataTests(unittest.TestCase):
    def test_sidecar_gets_both_fields_in_place(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'bread.json'
            path.write_text(json.dumps({'icon_id': 'bread', 'category': 'objects/food', 'keywords': []}))
            self.assertTrue(fix.update_metadata(path, 'food', ('food', 'state'), apply=True))
            document = json.loads(path.read_text())
            self.assertEqual(list(document), ['icon_id', 'category', 'categories', 'keywords'])
            self.assertEqual((document['category'], document['categories']), ('food', ['food', 'state']))
            self.assertFalse(fix.update_metadata(path, 'food', ('food', 'state'), apply=True))
            self.assertFalse(fix.update_metadata(Path(tmp) / 'missing.json', 'food', ('food',), apply=True))


class RunTests(unittest.TestCase):
    def test_dry_run_then_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'solo').mkdir()
            model = root / 'solo' / 'bread_u1.py'
            model.write_text(MODEL.format(uuid='u1', category="    category = 'objects/food'"))
            (root / 'solo' / '_base.py').write_text("category = 'objects'\n")
            report = root / 'report.csv'
            meta = root / 'metadata'
            (meta / 'solo').mkdir(parents=True)
            (meta / 'solo' / 'bread.json').write_text(json.dumps({'icon_id': 'bread', 'category': 'objects'}))
            records = {'u1': ['food', 'state', 'primitives']}
            registered = {'bread': ('solo', model)}
            counts = fix.run(root, records, VALID, report, apply=False, metadata=meta, registered=registered)
            self.assertEqual((counts['changed'], counts['metadata changed']), (1, 1))
            self.assertIn("'objects/food'", model.read_text())
            fix.run(root, records, VALID, report, apply=True, metadata=meta, registered=registered)
            self.assertIn("    category = 'food'\n    categories = ('food', 'state', 'primitives')\n", model.read_text())
            self.assertEqual(json.loads((meta / 'solo' / 'bread.json').read_text())['categories'],
                             ['food', 'state', 'primitives'])
            again = fix.run(root, records, VALID, report, apply=False, metadata=meta, registered=registered)
            self.assertEqual((again['unchanged'], again['metadata changed']), (1, 0))

    def test_sourceless_sidecar_gets_alias_fixed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'container').mkdir()
            model = root / 'container' / 'box.py'
            model.write_text("class Box(Container64):\n    icon_id = 'box'\n")
            (root / 'metadata' / 'container').mkdir(parents=True)
            sidecar = root / 'metadata' / 'container' / 'box.json'
            sidecar.write_text(json.dumps({'icon_id': 'box', 'category': 'containers'}))
            counts = fix.run(root, {}, VALID, root / 'r.csv', apply=True, metadata=root / 'metadata',
                             registered={'box': ('container', model)})
            self.assertEqual(counts['metadata changed'], 1)
            self.assertEqual(json.loads(sidecar.read_text())['categories'], ['container'])


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = self.root = Path(self.tmp.name)
        (root / 'models' / 'solo').mkdir(parents=True)
        self.model = root / 'models' / 'solo' / 'bread_u2.py'
        self.model.write_text(MODEL.format(uuid='u2', category="    category = 'objects'"))
        (root / 'pictoicons.json').write_text(json.dumps([
            {'id': 'u2', 'concept': 'Bread Loaf', 'old_concept': 'bread 1', 'categories': 'primitive primitives'}]))
        (root / 'primitives.json').write_text(json.dumps({'categories': {c: {} for c in VALID}}))
        self.args = ['--pictoicons', str(root / 'pictoicons.json'), '--models', str(root / 'models'),
                     '--metadata', str(root / 'metadata'), '--catalog', str(root / 'primitives.json'),
                     '--concept-categories', str(root / 'concepts.json'), '--report', str(root / 'r.csv')]

    def main(self, *extra):
        with unittest.mock.patch.object(fix, 'registered_files', return_value={}), \
                unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as out:
            return fix.main(self.args + list(extra)), out.getvalue()

    def test_check_lists_needs_then_set_fixes(self):
        code, out = self.main('--check')
        self.assertEqual(code, 1)
        self.assertIn("u2  'Bread Loaf' (was 'bread 1')", out)
        self.assertIn("'objects'", self.model.read_text())
        self.assertEqual(self.main('--set', 'u2=food', '--apply')[0], 0)
        self.assertIn("categories = ('food', 'primitive', 'primitives')", self.model.read_text())
        self.assertEqual(json.loads((self.root / 'concepts.json').read_text())['categories']['u2']['concept'], 'Bread Loaf')
        code, out = self.main('--check')
        self.assertEqual(code, 0)
        self.assertIn('categories are up to date', out)

    def test_set_rejects_unknown_category(self):
        with self.assertRaises(SystemExit):
            self.main('--set', 'u2=bakery')


if __name__ == '__main__':
    unittest.main()
