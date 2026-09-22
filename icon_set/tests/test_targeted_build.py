"""Single-icon output must not refresh or delete unrelated published material."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.scripts import build


class SelectedSquare(Solo48):
    icon_id = 'targeted-build-square'
    keyshape = Keyshape.SQUARE
    broken = False

    def build(self):
        edge = 40 if self.broken else 42
        self.add_polyline('outline', (6,6), (edge,6), (edge,42), (6,42), closed=True)


class TargetedBuildTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.dist = self.root / 'output'
        self.dist.mkdir()
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        registered = {SelectedSquare.icon_id: SelectedSquare}
        for location in ('icon_set.scripts.build.factories', 'icon_set.model.icons.registry.factories'):
            self.stack.enter_context(patch(location, return_value=registered))
        SelectedSquare.broken = False

    def run_build(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return build._build_selected(['solo'], self.dist, None, write_png=False,
                                         report=False, only={SelectedSquare.icon_id})

    def test_targeted_build_preserves_unregistered_records_and_assets(self):
        family = self.dist / 'solo48'; family.mkdir()
        gallery = self.dist / 'gallery'; gallery.mkdir()
        old = {'icon_id':'absent-original', 'family':'solo', 'name':'Edited title',
               'key':'solo/absent-original', 'author':'editor', 'category':'Custom',
               'preview_url':'../solo48/absent-original.svg'}
        (family / 'manifest.json').write_text(json.dumps({'icons':[old]}))
        (gallery / 'icons.json').write_text(json.dumps({'icons':[old], 'failed_icons':[]}))
        preserved = {'solo48/absent-original.svg': b'old svg',
                     'solo48/absent-original.metadata.json': b'{\n "editorial": true\n}\n',
                     'solo48/unindexed.svg': b'unindexed artwork',
                     'gallery/index.html': b'custom UI',
                     'gallery/originals/old.svg': b'old source reference',
                     'gallery/experiment.json': b'{\n "keep": true\n}\n',
                     'other-family/catalog.json': b'{\n "untouched": true\n}\n'}
        for path, content in preserved.items():
            dest=self.dist/path; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(content)
        self.assertEqual(self.run_build(), (2,0))
        for path, content in preserved.items():
            self.assertEqual((self.dist/path).read_bytes(), content, path)
        rows=json.loads((family/'manifest.json').read_text())['icons']
        self.assertEqual(next(r for r in rows if r['icon_id']=='absent-original'), old)
        rows=json.loads((gallery/'icons.json').read_text())['icons']
        self.assertEqual(next(r for r in rows if r['icon_id']=='absent-original'), old)
        self.assertTrue((family/f'{SelectedSquare.icon_id}.svg').exists())

    def test_failure_removes_selected_export_and_recovery_clears_failure(self):
        self.assertEqual(self.run_build(), (1,0))
        SelectedSquare.broken=True
        self.assertEqual(self.run_build(), (0,1))
        self.assertFalse((self.dist/'solo48'/f'{SelectedSquare.icon_id}.svg').exists())
        failed=self.dist/'failed/solo48'/f'{SelectedSquare.icon_id}.svg'
        self.assertTrue(failed.exists())
        data=json.loads((self.dist/'gallery/icons.json').read_text())
        self.assertEqual(len(data['failed_icons']),1)
        self.assertEqual(data['icons'],[])
        SelectedSquare.broken=False
        self.assertEqual(self.run_build(), (1,0))
        self.assertFalse(failed.exists())
        self.assertEqual(json.loads((self.dist/'gallery/icons.json').read_text())['failed_icons'],[])

    def test_helper_renders_only_selected_export_and_reports_failure(self):
        from icon_set.scripts.finish_icon import main
        out=self.root/'previews'
        # This source contains exactly one registered factory in this test registry.
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code=main([__file__, '--dist',str(self.dist),'--out',str(out)])
        self.assertEqual(code,0,output.getvalue())
        self.assertTrue((out/'review.png').exists())
        from PIL import Image
        with Image.open(out/'light.png') as image:
            self.assertEqual(image.size,(48,48))
        self.assertLess(len(output.getvalue()),1500)
        SelectedSquare.broken=True
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code=main([__file__, '--dist',str(self.dist),'--out',str(out)])
        self.assertNotEqual(code,0)
        self.assertIn('error',output.getvalue())

    def test_selected_primitive_links_update_without_refreshing_other_rows(self):
        gallery=self.dist/'gallery'; gallery.mkdir()
        selected={'uuid':'selected-source', 'path':'selected.svg', 'category':'Custom',
                  'models':[], 'generated':[], 'state':'none', 'match':'unmatched'}
        other={'uuid':'other-source', 'path':'other.svg', 'category':'Custom',
               'models':['external-model'], 'generated':[], 'state':'model_only', 'editorial':'keep'}
        catalog={'rows':[selected,other], 'categories':{'Custom':{'total':2,'none':1,'model_only':1}}}
        (gallery/'primitives.json').write_text(json.dumps(catalog))
        (gallery/'combinations.json').write_text(json.dumps({'rows':[], 'references':{
            'selected-source':{'generated':[], 'editorial':'keep'},
            'other-source':{'generated':[], 'editorial':'untouched'}}}))
        links=dict(by_id={'selected-source':[SelectedSquare.icon_id]}, by_reference_id={},
                   by_path={}, by_reference_path={}, anonymous={})
        with patch('icon_set.scripts.primitives_catalog.model_links',return_value=links):
            self.run_build()
        result=json.loads((gallery/'primitives.json').read_text())
        self.assertEqual(result['rows'][1],other)
        self.assertEqual(result['rows'][0]['state'],'generated')
        self.assertEqual(result['rows'][0]['models'],[SelectedSquare.icon_id])
        self.assertEqual(result['categories']['Custom'],{'total':2,'none':0,'model_only':1,'generated':1})
        combinations=json.loads((gallery/'combinations.json').read_text())
        self.assertEqual(combinations['references']['other-source'],{'generated':[],'editorial':'untouched'})
        self.assertEqual(combinations['references']['selected-source']['generated'][0]['icon_id'],SelectedSquare.icon_id)

    def test_unselected_failure_is_preserved_without_its_original(self):
        failed=self.dist/'failed/solo48'; failed.mkdir(parents=True)
        row={'icon_id':'old-failure', 'family':'solo', 'profile':'SOLO48',
             'errors':['old failure'], 'warnings':[], 'status':'fail', 'svg':'old-failure.svg'}
        (failed/'manifest.json').write_text(json.dumps({'icons':[row]}))
        (failed/'old-failure.svg').write_text('preserve failing artwork')
        (failed/'old-failure.metadata.json').write_text('{"editorial":"preserve"}\n')
        self.run_build()
        self.assertEqual(json.loads((failed/'manifest.json').read_text())['icons'],[row])
        self.assertEqual((failed/'old-failure.svg').read_text(),'preserve failing artwork')
        self.assertEqual((failed/'old-failure.metadata.json').read_text(),'{"editorial":"preserve"}\n')
