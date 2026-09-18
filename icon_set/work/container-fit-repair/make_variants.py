"""Create independent container fit revisions from source models, preserving parents."""
import ast,json
from pathlib import Path
from icon_set.scripts.create_variant import prepare_variant
AUTHOR='gpt-6'
# Coordinates are edited on owning frame definitions; strokes remain 4 units.
configs={
'browser-window':('SQUARE',{}, {6:2,10:6,14:10,22:18,54:58,58:62},[32,40],'Taller browser body; retained the full title bar and its three indicators.'),
'mobile-phone-device':('VRECT_XL',{14:6,20:12,44:52,50:58},{},[32,25],'Wider phone display; retained bottom navigation band and equal corner radii.'),
'horizontal-mobile-phone':('HRECT_XL',{}, {14:6,20:12,44:52,50:58},[37,32],'Taller landscape display; retained left bezel divider.'),
'landscape-mobile-phone':('HRECT_XL',{}, {14:6,20:12,44:52,50:58},[39,32],'Taller landscape display; retained sensor and bezel.'),
'rounded-rectangular-frame':('HRECT_L',{}, {14:10,18:14,46:50,50:54},[32,32],'Increased frame height one keyshape step, preserving width and corner radii.'),
'rectangular-sign-board':('SQUARE',{}, {10:2,14:6,32:42,36:46,54:62},[32,24],'Taller sign panel with a shorter, still distinct centered post.'),
'blank-calendar-container':('SQUARE',{}, {},[32,41],'Raised calendar header; retained two binding posts and the rounded page.'),
'square-front-smartwatch-container':('VRECT_L',{}, {},[32,32],'Taller watch face with matching shorter strap ends.'),
}
class Remap(ast.NodeTransformer):
 def __init__(self,x,y):self.x=x;self.y=y
 def visit_Tuple(self,node):
  if len(node.elts)==2 and all(isinstance(e,ast.Constant) and type(e.value) in (int,float) for e in node.elts):
   a,b=[e.value for e in node.elts];node.elts=[ast.Constant(self.x.get(a,a)),ast.Constant(self.y.get(b,b))]
   return node
  return self.generic_visit(node)
records=[]
for parent,(key,x,y,center,reason) in configs.items():
 path,new_id,text=prepare_variant(parent,'container','Native SUB32 clearance')
 tree=ast.parse(text)
 cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and any(isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in a.targets) for a in n.body))
 for node in tree.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in node.targets):node.value=ast.Constant(AUTHOR)
 for node in cls.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='keyshape' for t in node.targets):node.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),key,ast.Load())
  if isinstance(node,ast.FunctionDef) and node.name=='build':Remap(x,y).visit(node)
 if parent=='blank-calendar-container':
  code="""def build(self):
    # Page owns the header; two matching posts keep a six-unit centerline gap.
    rect(self, 'page', 2, 8, 62, 62, 4)
    self.add_line('header', (2, 20), (62, 20))
    self.relate('connect', 'header', 'page')
    for x in (18, 46):
        self.add_line(f'post-{x}', (x, 2), (x, 14))
        self.relate('connect', f'post-{x}', 'page')
"""
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef) or n.name!='build']+[ast.parse(code).body[0]]
 if parent=='square-front-smartwatch-container':
  code="""def build(self):
    # One symmetric face definition; both strap attachments follow its edges.
    face_top, face_bottom = 10, 54
    rect(self, 'face', 10, face_top, 54, face_bottom, 6)
    self.add_polyline('top-strap', (20,face_top),(22,2),(42,2),(44,face_top))
    self.add_polyline('bottom-strap', (20,face_bottom),(22,62),(42,62),(44,face_bottom))
    self.relate('connect','face','top-strap')
    self.relate('connect','face','bottom-strap')
"""
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef) or n.name!='build']+[ast.parse(code).body[0]]
 # All new variants explicitly carry provenance; original IDs retained where supplied.
 defined={t.id for n in tree.body if isinstance(n,ast.Assign) for t in n.targets if isinstance(t,ast.Name)}
 for key_name in ('SOURCE_ICON_ID','SOURCE_PATH'):
  if key_name not in defined:tree.body.insert(0,ast.Assign([ast.Name(key_name,ast.Store())],ast.Constant(None)))
 # Replace outdated prose rather than leaving old coordinate/hosting claims.
 tree.body=[n for n in tree.body if not (isinstance(n,ast.Expr) and isinstance(n.value,ast.Constant) and isinstance(n.value.value,str))]
 doc=f'{reason}\nIndependent review variant of {parent}. {key} CONTAINER64, 4-unit strokes.\nConstruction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.\nNative SUB32 trial center: {center}. See container-fit-repair report for measured hosting results.'
 tree.body.insert(0,ast.Expr(ast.Constant(doc)))
 future=[n for n in tree.body if isinstance(n,ast.ImportFrom) and n.module=="__future__"]
 tree.body=[n for n in tree.body if n not in future]
 tree.body[1:1]=future
 ast.fix_missing_locations(tree)
 with path.open('x') as f:f.write(ast.unparse(tree)+'\n')
 records.append({'parent':parent,'variant':new_id,'module':str(path),'center':center,'reason':reason})
Path('icon_set/work/container-fit-repair/variants.json').write_text(json.dumps(records,indent=2))
print(json.dumps(records,indent=2))
