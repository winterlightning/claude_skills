"""fix_pictoicon_categories: every pictoicon record ends up with a type token."""
import csv
import json
from pathlib import Path
import tempfile
import unittest

from icon_set.scripts import fix_pictoicon_categories as fix


class FixCategoriesTests(unittest.TestCase):
    def test_untyped_gets_primitives(self):
        self.assertEqual(fix.fix_categories('combination'), ('combination primitives', 'added-primitives'))
        self.assertEqual(fix.fix_categories(''), ('primitives', 'added-primitives'))

    def test_role_types_are_not_primitives(self):
        for categories in ('symbol state', 'container', 'health text state'):
            self.assertEqual(fix.fix_categories(categories), (categories, 'unchanged'))

    def test_other_gets_generate(self):
        self.assertEqual(fix.fix_categories('travel other'), ('travel other primitives-generate', 'other-generate'))
        self.assertEqual(fix.fix_categories('state other'), ('state other primitives-generate', 'other-generate'))
        self.assertEqual(fix.fix_categories('other primitives-generate'), ('other primitives-generate', 'unchanged'))

    def test_combinations_left_alone(self):
        self.assertEqual(fix.fix_categories('container-combination other'),
                         ('container-combination other', 'skipped-combination-other'))
        self.assertEqual(fix.fix_categories('war side-combination bottom-right'),
                         ('war side-combination bottom-right', 'unchanged'))

    def test_typed_unchanged(self):
        self.assertEqual(fix.fix_categories('primitives primitives-generate'),
                         ('primitives primitives-generate', 'unchanged'))
        self.assertEqual(fix.fix_categories('logos primitives'), ('logos primitives', 'unchanged'))

    def test_no_duplicate_tokens(self):
        new, _ = fix.fix_categories('state state other')
        self.assertEqual(new.split(), ['state', 'other', 'primitives-generate'])


class RunTests(unittest.TestCase):
    def test_writes_fixed_json_and_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            records = [{'id': 'a', 'concept': 'A', 'categories': 'combination', 'tags': 'x'},
                       {'id': 'b', 'concept': 'B', 'categories': 'other'},
                       {'id': 'c', 'concept': 'C', 'categories': 'logos primitives'}]
            src = root / 'in.json'
            src.write_text(json.dumps(records))
            out, report = root / 'out.json', root / 'changes.csv'
            counts = fix.run(src, out, report, {'a': {'SUB32', 'SOLO48'}})
            fixed = json.loads(out.read_text())
            self.assertEqual([r['categories'] for r in fixed],
                             ['combination primitives', 'other primitives-generate', 'logos primitives'])
            self.assertEqual(fixed[0]['tags'], 'x')
            self.assertEqual(json.loads(src.read_text()), records)
            rows = list(csv.DictReader(report.open()))
            self.assertEqual([r['id'] for r in rows], ['a', 'b'])
            self.assertEqual(rows[0]['linked_profiles'], 'SOLO48 SUB32')
            self.assertEqual(counts['untyped'], 0)


if __name__ == '__main__':
    unittest.main()
