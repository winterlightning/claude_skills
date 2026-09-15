"""Version lineage and non-destructive variant creation."""
import ast
from contextlib import redirect_stdout
import inspect
import io
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from icon_set.model.icons.registry import factories, validate_variants
from icon_set.scripts import create_variant


class LineageTests(unittest.TestCase):
    def icon(self, family='sub', parent=None, label='Version'):
        return SimpleNamespace(family=family, variant_of=parent, variant_label=label)

    def test_valid_branching_and_nested_versions(self):
        validate_variants({'root': self.icon(), 'v2': self.icon(parent='root'),
                           'v3': self.icon(parent='v2'), 'alternative': self.icon(parent='root')})

    def test_missing_parent_family_cycle_and_empty_label_rejected(self):
        cases = [
            {'root': self.icon(parent='missing')},
            {'root': self.icon(), 'v2': self.icon(family='solo', parent='root')},
            {'root': self.icon(parent='v2'), 'v2': self.icon(parent='root')},
            {'root': self.icon(), 'v2': self.icon(parent='root', label='')},
        ]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                validate_variants(case)


class ScaffoldTests(unittest.TestCase):
    def test_clone_preserves_parent_geometry_and_allocates_unique_file(self):
        registered = dict(factories())
        factory = registered['square']
        original = Path(inspect.getsourcefile(factory)).read_text()
        with TemporaryDirectory() as temp:
            source = Path(temp) / 'square.py'
            source.write_text(original)
            with patch.object(create_variant, 'factories', return_value=registered), \
                 patch.object(create_variant.inspect, 'getsourcefile', return_value=str(source)):
                target, name, text = create_variant.prepare_variant('square', 'sub', 'Softer corners')
                self.assertNotEqual(target, source)
                self.assertEqual(name, 'square-v2')
                self.assertRegex(name, r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$')
                self.assertEqual(source.read_text(), original)
                ast.parse(text)
                namespace = {'__name__': 'icon_set.model.icons.sub._variant_test', '__package__': 'icon_set.model.icons.sub'}
                exec(compile(text, str(target), 'exec'), namespace)
                variant_factory = next(value for value in namespace.values()
                                       if isinstance(value, type) and getattr(value, 'icon_id', None) == name)
                parent, variant = factory(), variant_factory()
                self.assertEqual(parent.primitives, variant.primitives)
                self.assertEqual(variant.family, parent.family)
                self.assertEqual(variant.to_record()['variant_of'], 'square')
                self.assertEqual(variant.to_record()['variant_label'], 'Softer corners')
                self.assertNotIn('variant_of', parent.to_record())
                target.write_text(text)
                next_target, next_name, _ = create_variant.prepare_variant('square', 'sub', 'Another option')
                self.assertEqual(next_name, 'square-v3')
                self.assertNotEqual(next_target, target)
                self.assertEqual(target.read_text(), text)

    def test_family_mismatch_and_empty_label_fail(self):
        for family, label in [('solo', 'new'), ('sub', ' ')]:
            with self.assertRaises(ValueError):
                create_variant.prepare_variant('square', family, label)

    def test_exclusive_creation_never_overwrites_existing_file(self):
        with TemporaryDirectory() as temp:
            target = Path(temp) / 'existing.py'
            target.write_text('keep me')
            with patch.object(create_variant, 'prepare_variant', return_value=(target, 'test-v2', 'replace me')), \
                 redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
                create_variant.main(['--icon', 'square', '--family', 'sub', '--label', 'new'])
            self.assertEqual(target.read_text(), 'keep me')


if __name__ == '__main__':
    unittest.main()
