from pathlib import Path
import sys,json,ast,re
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons import registry
from icon_set.validation.envelope import visible_bounds
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/dist/gallery/failures.html'
AUTHOR='gpt-6'
class TranslatePoints(ast.NodeTransformer):
 def visit_Call(self,node):
  self.generic_visit(node)
  if isinstance(node.func,ast.Attribute) and node.func.attr in ['add_arc','add_line','add_polyline','add_dot','add_anchor']:
   for p in node.args[1:]:
    if isinstance(p,ast.Tuple) and len(p.elts)==2 and all(isinstance(v,ast.Constant) and isinstance(v.value,(int,float)) for v in p.elts):p.elts[1].value+=2
  return node
rows=json.loads(Path('/tmp/shifted-icons.json').read_text());mapping=[]
for row in rows:
 original=registry.create(row['id']);before=visible_bounds(list(original.draw().primitives));dest,ident,source=prepare_variant(row['id'],'solo','Exact keyshape bounds')
 sid=re.search(r"SOURCE_ICON_ID = ['\"]([^'\"]+)",source)[1];dest=dest.with_name(dest.stem+'_'+sid.replace('-','_')+'.py')
 tree=ast.parse(source)
 if row['id'].startswith('hammerhead-shark'):
  for node in ast.walk(tree):
   if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr=='add_arc' and node.args[0].value=='body-14':
    next(k for k in node.keywords if k.arg=='radius_y').value=ast.Constant(value=15)
  note='Keep the SQUARE centerline box (6,6)-(42,42). Body-14 is an exact rx=16, ry=15 quarter ellipse; it meets the tail at y=42 without overshoot. Original swept profile retained.'
 else:
  tree=TranslatePoints().visit(tree)
  note='Move every authored point down by 2 units together. Keep dimensions, arcs, shared endpoints and spacing unchanged. VRECT_L centerline box (8,4)-(40,44), ink (6,2)-(42,46).'
 ast.fix_missing_locations(tree)
 # Replace stale generated docstrings with the scoped repair description.
 for n in ast.walk(tree):
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(value=AUTHOR)
 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) and isinstance(tree.body[0].value.value,str):tree.body[0].value=ast.Constant(value=note)
 source='# Bounds-only review variant; parent preserved.\n'+ast.unparse(tree)+'\n';source=source.replace('    def build(self)', '    def build(self)')
 with dest.open('x') as f:f.write(source)
 registry._FACTORIES=None
 obj=registry.create(ident);after=visible_bounds(list(obj.draw().primitives));report=obj.validate_icon();assert not any(f.check=='canvas/keyshape bounds' for f in report.findings),(ident,report.describe())
 mapping.append({'original':row['id'],'id':ident,'file':str(dest.relative_to(ROOT)),'before':before,'after':after,'note':note,'validation':report.describe()})
(W/'results.json').write_text(json.dumps(mapping,indent=2));print('Bounds corrected:',len(mapping))
for r in mapping:print(r['original'],'->',r['id'],r['after'])
