import json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from icon_set.scripts.sub_usage_categories import stage_catalog,geometry,MANIFEST
class SubUsageTests(unittest.TestCase):
 def test_geometry_ignores_identity_but_not_paths(self):
  a='<svg><title>a</title><path d="M0 0L1 1"/></svg>'
  self.assertEqual(geometry(a),geometry(a.replace('>a<','>b<')))
  self.assertNotEqual(geometry(a),geometry(a.replace('L1 1','L2 2')))
 def test_routes_roles_and_is_idempotent(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);p=root/MANIFEST;p.parent.mkdir(parents=True)
   versions={r:dict(icon_id=i,preview_url=i+'.svg',model_validation='pass',python_source=i+'.py',svg=i+'.svg',sha256='hash') for r,i in [('side','plus'),('symbol','plus-symbol')]}
   p.write_text(json.dumps({'icons':[dict(original_icon_id='plus',related_group='group',versions=versions)]}))
   fix=root/'icon_set/work/container-fit-repair/fit-adjustments.json';fix.parent.mkdir(parents=True);fix.write_text('{}')
   gallery=root/'icon_set/.local/dist/gallery';gallery.mkdir(parents=True)
   for v in versions.values():(gallery/v['preview_url']).write_text('<svg/>')
   data={'rows':[dict(kind=k,sub_generated=[dict(icon_id='plus',key='sub/plus'),dict(icon_id='plus-symbol',key='sub/plus-symbol')]) for k in ['side','container']]}
   with patch('icon_set.scripts.sub_usage_categories.refresh', side_effect=AssertionError('Build refreshed source state')):
    stage_catalog(data,root);once=json.dumps(data,sort_keys=True);stage_catalog(data,root)
   self.assertEqual(once,json.dumps(data,sort_keys=True))
   self.assertEqual(json.loads(p.read_text())['icons'][0]['versions'],versions)
   self.assertEqual([r['sub_generated'][0]['icon_id'] for r in data['rows']],['plus','plus-symbol'])
   self.assertEqual([len(r['sub_generated']) for r in data['rows']],[1,1])
   self.assertEqual(data['rows'][0]['sub_generated'][0]['related_icon_ids'],['plus-symbol'])
 def test_no_manifest_leaves_catalog_unchanged(self):
  with tempfile.TemporaryDirectory() as tmp:
   data={'rows':[{'kind':'side'}]};stage_catalog(data,Path(tmp));self.assertEqual(data,{'rows':[{'kind':'side'}]})
 def test_repaired_side_variant_keeps_origin_and_independent_symbol(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);p=root/MANIFEST;p.parent.mkdir(parents=True)
   versions={r:dict(icon_id=i,family=f,preview_url=i+'.svg',model_validation='pass',python_source=i+'.py',svg=i+'.svg',sha256='hash') for r,i,f in [('side','plus-v2','sub'),('symbol','plus-symbol','symbol')]}
   p.write_text(json.dumps({'icons':[dict(original_icon_id='plus',related_group='group',versions=versions)]}))
   fix=root/'icon_set/work/container-fit-repair/fit-adjustments.json';fix.parent.mkdir(parents=True);fix.write_text('{}')
   for v in versions.values():(root/v['svg']).write_text('<svg/>')
   data={'rows':[dict(kind=k,sub_generated=[dict(icon_id='plus',key='sub/plus')],sub_exports=[dict(icon='plus')]) for k in ['side','container']]}
   stage_catalog(data,root);once=json.dumps(data,sort_keys=True);stage_catalog(data,root)
   self.assertEqual(once,json.dumps(data,sort_keys=True))
   self.assertEqual([r['sub_generated'][0]['icon_id'] for r in data['rows']],['plus-v2','plus-symbol'])
   self.assertEqual([r['sub_exports'][0]['icon'] for r in data['rows']],['plus-v2','plus-symbol'])
   self.assertEqual(data['rows'][1]['sub_generated'][0]['related_icon_ids'],['plus-v2'])
   self.assertEqual(json.loads(p.read_text())['icons'][0]['versions'],versions)
