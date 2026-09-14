from pathlib import Path
import sys,ast,json,textwrap,re
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons import registry
from icon_set.validation.library_qa import inspect_icon
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/shifted-bounds-repair/results.json'
AUTHOR='gpt-6'
rows=[]
for parent in ['vulture-v3','hammerhead-shark-v5','hammerhead-shark-v6']:
 dest,ident,src=prepare_variant(parent,'solo','Connected neck' if parent.startswith('vulture') else 'Smaller body with open tail clearance')
 sid=re.search(r"SOURCE_ICON_ID = ['\"]([^'\"]+)",src)[1];dest=dest.with_name(dest.stem+'_'+sid.replace('-','_')+'.py')
 if parent.startswith('vulture'):
  start=next(n.lineno for n in ast.walk(ast.parse(src)) if isinstance(n,ast.FunctionDef) and n.name=='build')
  body='''# One continuous silhouette joins nape, back, wing and head.
# Remove the redundant closed wing boundary; preserve the standing profile.
self.add_arc('head',(26,11),(40,11),radius_x=7)
self.add_line('beak',(40,11),(40,17))
self.add_line('chin',(40,17),(34,17))
self.add_line('neck',(34,17),(34,23))
self.add_arc('throat',(34,23),(25,30),radius_x=9,radius_y=7)
self.add_arc('wing-front',(25,30),(23,36),radius_x=10,sweep=True)
self.add_line('wing-tip',(23,36),(8,42))
self.add_arc('back',(8,42),(18,18),radius_x=40,sweep=True)
self.add_line('shoulder',(18,18),(26,19))
self.add_line('nape',(26,19),(26,11))
self.add_contour('silhouette','head','beak','chin','neck','throat','wing-front','wing-tip','back','shoulder','nape',closed=True)
self.add_polyline('leg',(23,36),(26,44),(34,44))
self.relate('connect','silhouette','leg')
'''
  src='\n'.join(src.splitlines()[:start-1])+'\n    def build(self):\n'+textwrap.indent(body,'        ')
 else:
  src=src.replace('(26, 14)', '(24, 14)').replace('(26, 18)', '(24, 18)').replace('(34, 24)', '(28, 22)').replace('(26, 26)', '(24, 26)').replace("radius_x=8, radius_y=6", "radius_x=10, radius_y=6")
 with dest.open('x') as f:f.write(src)
 registry._FACTORIES=None
 o=registry.create(ident);qa=inspect_icon(o);qa.pop('_svg',None);rows.append({'original':parent,'id':ident,'file':str(dest.relative_to(ROOT)),'qa':qa})
 print(ident,qa['status'],qa['errors'],qa['warnings'],[(f['elements'],f['ink_gap']) for f in qa.get('internal_spacing',{}).get('findings',[])])
(W/'results.json').write_text(json.dumps(rows,indent=2))
