"""fix_model_categories: a model's category comes from its source pictoicon record."""
from pathlib import Path
import tempfile
import unittest

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

    def test_pictoicon(self):
        self.assertEqual(fix.resolve('u1', 'objects/food', self.records, VALID), ('food', 'pictoicon'))

    def test_no_topic_keeps_valid_else_uncategorized(self):
        self.assertEqual(fix.resolve('u2', 'avatars', self.records, VALID), ('avatars', 'kept'))
        self.assertEqual(fix.resolve('u2', 'objects', self.records, VALID),
                         ('Uncategorized', 'pictoicon has no topic or type'))

    def test_no_record(self):
        self.assertEqual(fix.resolve('', 'avatars', self.records, VALID), ('avatars', 'kept'))
        self.assertEqual(fix.resolve('', 'nature/animals', self.records, VALID), ('animals', 'alias'))
        self.assertEqual(fix.resolve('', 'objects/misc', self.records, VALID), (None, 'no SOURCE_ICON_ID'))


class RewriteTests(unittest.TestCase):
    def test_every_line_keeps_quotes(self):
        text = "class A:\n    category = \"objects/general\"\n\nclass B:\n    category='objects/food'\n"
        self.assertEqual(fix.rewrite(text, 'food'),
                         "class A:\n    category = \"food\"\n\nclass B:\n    category = 'food'\n")

    def test_inserted_after_icon_id(self):
        self.assertEqual(fix.rewrite("class A:\n    icon_id = 'a'\n", 'food'),
                         "class A:\n    icon_id = 'a'\n    category = 'food'\n")


class RunTests(unittest.TestCase):
    def test_dry_run_then_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'solo').mkdir()
            model = root / 'solo' / 'bread_u1.py'
            model.write_text(MODEL.format(uuid='u1', category="    category = 'objects/food'"))
            (root / 'solo' / '_base.py').write_text("category = 'objects'\n")
            report = root / 'report.csv'
            counts = fix.run(root, {'u1': ['food']}, VALID, report, apply=False)
            self.assertEqual(counts['changed'], 1)
            self.assertIn("'objects/food'", model.read_text())
            fix.run(root, {'u1': ['food']}, VALID, report, apply=True)
            self.assertIn("    category = 'food'\n", model.read_text())
            self.assertEqual(fix.run(root, {'u1': ['food']}, VALID, report, apply=False)['unchanged'], 1)


if __name__ == '__main__':
    unittest.main()
