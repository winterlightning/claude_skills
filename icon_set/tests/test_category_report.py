"""Identity matching and snapshot correctness for the reusable review report."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.scripts.category_report import (
    digest, discover_sources, export_state, generate, main, match_models, model_catalog, render_html,
)

UID = '62d28cec-8386-49e8-9825-a759c8b2ae50'
OTHER = '00000000-0000-4000-8000-000000000001'
SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="10"/></svg>'


class MatchingTests(unittest.TestCase):
    def test_batch_copies_share_identity_but_equal_names_without_ids_do_not(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'batch-01').mkdir()
            for path in [root / f'usb_{UID}.svg', root / 'batch-01' / f'renamed_{UID}.svg', root / 'no-id.svg', root / 'batch-01/no-id.svg']:
                path.write_text(SVG)
            sources = discover_sources(root)
            self.assertEqual(len(sources), 3)
            self.assertEqual(len(next(r for r in sources if r['source_id'] == UID)['paths']), 2)

    def test_id_wins_over_manifest_name_and_keeps_multiple_families(self):
        source = dict(source_id=UID, paths=[Path('/tmp/original.svg')], proposed_icon_id='wrong-name')
        models = [dict(source_id=UID, source_path=None, icon_id='solo-usb'),
                  dict(source_id=UID, source_path=None, icon_id='sub-usb'),
                  dict(source_id=OTHER, source_path=None, icon_id='wrong-name')]
        result, method = match_models(source, models)
        self.assertEqual([r['icon_id'] for r in result], ['solo-usb', 'sub-usb'])
        self.assertEqual(method, 'source ID')

    def test_name_cannot_override_conflicting_source_metadata(self):
        source = dict(source_id=UID, paths=[Path('/tmp/usb.svg')], proposed_icon_id='usb')
        models = [dict(source_id=OTHER, source_path=Path('/tmp/usb.svg'), icon_id='usb')]
        self.assertEqual(match_models(source, models), ([], 'unmatched'))

    def test_explicit_reuse_matches_another_source_id(self):
        source = dict(source_id=OTHER, paths=[Path('/tmp/duplicate.svg')], proposed_icon_id='anything')
        model = dict(source_id=UID, source_path=Path('/tmp/primary.svg'), icon_id='usb',
                     source_references=[(OTHER, Path('/tmp/duplicate.svg'))])
        self.assertEqual(match_models(source, [model]), ([model], 'declared source reuse'))

    def test_primary_source_match_precedes_reuse(self):
        source = dict(source_id=OTHER, paths=[Path('/tmp/source.svg')], proposed_icon_id=None)
        primary = dict(source_id=OTHER, source_path=None, icon_id='primary')
        shared = dict(source_id=UID, source_path=None, icon_id='shared', source_references=[(OTHER, None)])
        self.assertEqual(match_models(source, [shared, primary]), ([primary], 'source ID'))

    def test_real_laptop_duplicate_is_covered_by_catalog_metadata(self):
        duplicate = '0eca8bb8-75fe-4501-aa58-53ce337798cc'
        source = dict(source_id=duplicate, paths=[Path('/unused.svg')], proposed_icon_id=None)
        matches, method = match_models(source, model_catalog())
        self.assertEqual([m['icon_id'] for m in matches], ['open-laptop'])
        self.assertEqual(method, 'declared source reuse')


class CliTests(unittest.TestCase):
    def test_all_discovers_categories_without_a_hardcoded_list(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ('computers', 'another-category'):
                (root / name).mkdir()
            with patch('icon_set.scripts.category_report.generate') as run:
                self.assertEqual(main(['--all', '--source-root', str(root), '--out', str(root / 'out')]), 0)
                self.assertEqual([p.name for p in run.call_args.args[0]], ['another-category', 'computers'])


class ExportTests(unittest.TestCase):
    def test_missing_stale_and_manifest_mismatch_are_separate(self):
        self.assertEqual(export_state(SVG, None, None), 'missing')
        self.assertEqual(export_state(SVG, SVG + '\n', None), 'stale')
        self.assertEqual(export_state(SVG, SVG, None), 'manifest mismatch')
        self.assertEqual(export_state(SVG, SVG, {'svg_sha256': 'incorrect'}), 'manifest mismatch')
        self.assertEqual(export_state(SVG, SVG, {'svg_sha256': digest(SVG)}), 'current')

    def test_embedded_metadata_cannot_end_json_script(self):
        html = render_html({'title': '</script><script>alert(1)</script>'})
        self.assertNotIn('</script><script>alert', html)
        self.assertIn('\\u003c/script\\u003e', html)

    def test_report_includes_ready_and_pending_without_modifying_dist(self):
        from icon_set.model.icons.registry import create
        icon = create('usb-symbol')
        with TemporaryDirectory() as temp:
            root = Path(temp)
            category = root / 'sources/computers'
            category.mkdir(parents=True)
            source = category / f'usb_{UID}.svg'
            source.write_text(SVG)
            (category / f'missing_{OTHER}.svg').write_text(SVG)
            dist = root / 'dist/solo48'
            dist.mkdir(parents=True)
            exported = dist / 'usb-symbol.svg'
            exported.write_text(icon.to_svg())
            (dist / 'manifest.json').write_text(json.dumps({'icons': [{'icon_id': 'usb-symbol', 'svg_sha256': digest(icon.to_svg())}]}))
            module = root / 'usb.py'
            module.write_text('# fixture module contents\n')
            catalog = [dict(icon_id='usb-symbol', factory=type(icon), source_id=UID,
                            source_path=source.resolve(), module_path=module, family='solo')]
            before = exported.read_bytes()
            with patch('icon_set.scripts.category_report.model_catalog', return_value=catalog):
                report = generate([category], root / 'report', root / 'sources', root / 'dist')
            self.assertEqual(report['source_count'], 2)
            self.assertEqual(report['counts'], {'pending': 1, 'ready': 1})
            self.assertEqual(before, exported.read_bytes())
            self.assertTrue((root / 'report/index.html').is_file())
            inventory = json.loads((root / 'report/report.json').read_text())
            self.assertNotIn('model_preview', inventory['rows'][1])


if __name__ == '__main__':
    unittest.main()
