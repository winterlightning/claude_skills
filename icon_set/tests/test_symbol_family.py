import unittest
from icon_set.model.profiles import Profile
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.symbol._base import Symbol32
from icon_set.model.icons.symbol._text_base import TextSymbol32
from icon_set.model.icons.sub._text_base import canvas_dimensions
from icon_set.model import contracts
from icon_set.scripts.sub_usage_categories import geometry
import xml.etree.ElementTree as ET
class SymbolFamilyTests(unittest.TestCase):
 def test_symbol_owns_profile_with_same_geometry_rules(self):
  self.assertEqual(Profile.for_family('symbol'),Profile.SYMBOL32)
  self.assertEqual(Symbol32.family,'symbol')
  for field in ('canvas_size','mic','grid'):
   if field=='grid':continue
   self.assertEqual(getattr(Profile.SYMBOL32.spec,field),getattr(Profile.SUB32.spec,field))
  for key in Keyshape:
   if key.name=='FREE':continue
   self.assertEqual(key.bounds_for(Profile.SYMBOL32),key.bounds_for(Profile.SUB32))
 def test_text_symbol_keeps_natural_width(self):
  class Wide(TextSymbol32):
   text_canvas_width=72
   def build(self):pass
  self.assertEqual(canvas_dimensions(Wide()),(72,32));self.assertEqual(Wide().profile,Profile.SYMBOL32)
 def test_symbol_is_allowed_as_standalone_and_hosted_content(self):
  classes=contracts.composition_templates()['classes']
  self.assertIn('SYMBOL32',classes['SOLO']['output_profiles'])
  self.assertEqual(classes['CONTAINER_COMBINE']['children'][1]['profile'],'SYMBOL32')
 def test_geometry_hash_independent_of_namespace_registration(self):
  doc='<svg xmlns="http://www.w3.org/2000/svg"><path d="M2 2L30 30"/></svg>'
  before=geometry(doc);ET.register_namespace('','http://www.w3.org/2000/svg');self.assertEqual(before,geometry(doc))

class PortableSymbolCatalogTests(unittest.TestCase):
 def test_catalog_and_previews_do_not_depend_on_ignored_runtime_data(self):
  import json, tempfile
  from pathlib import Path
  from unittest.mock import patch
  from icon_set.scripts.symbol_family import stage
  from icon_set.scripts.sub_usage_categories import MANIFEST, annotate_records
  from icon_set.model.icons.registry import create
  model=create('add-sub32-symbol')
  with tempfile.TemporaryDirectory() as temporary:
   root=Path(temporary);target=root/'gallery'
   manifest=root/MANIFEST;manifest.parent.mkdir(parents=True)
   manifest.write_text(json.dumps({'icons':[{'original_icon_id':'add-sub32','related_group':'sub-origin/add-sub32',
    'versions':{'side':{'icon_id':'add-sub32','family':'sub','model_validation':'pass'},
                'symbol':{'icon_id':'add-sub32-symbol','family':'symbol','model_validation':'pass'}}}]}))
   from icon_set.scripts import symbol_family
   with patch('icon_set.model.icons.registry.create', return_value=model), \
        patch.object(symbol_family.inspect,'getsourcefile',return_value=str(root/'icon.py')):
    records=[];stage(target,records,root)
   annotate_records(records,root)
   symbol=next(r for r in records if r['family']=='symbol')
   self.assertEqual(symbol['key'],'symbol/add-sub32-symbol')
   self.assertEqual(symbol['related_role_icons'][0]['key'],'sub/add-sub32')
   self.assertTrue((target/'sub-usage/symbol/add-sub32-symbol.svg').is_file())
   self.assertFalse((root/'icon_set/data').exists())
