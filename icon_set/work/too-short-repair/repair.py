from pathlib import Path
import json,ast
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;(W/'starting').mkdir(exist_ok=True)
queue={r['id']:r for r in json.loads((W/'queue.json').read_text())}
for row in json.loads((W/'mapping.json').read_text()):
 p=Path(row['file']);s=p.read_text();(W/'starting'/p.name).write_text(s);q=queue[row['original']];issue=next(i for i in q['issues'] if i.get('kind')=='Ink box too short');ov=issue['overlay'];
 # Extend extremal line endpoints; arc-owned extrema receive individual repair.
 import re
 nums=re.search(r'visible ink \(([^)]+)\).*envelope \(([^)]+)\)',issue['text']);ink=list(map(float,nums[1].split(',')));env=list(map(float,nums[2].split(',')));moves={}
 for idx in [1,3]:
  a=ink[idx]+(2 if idx==1 else -2);b=env[idx]+(2 if idx==1 else -2)
  if abs(a-round(a))<.001 and abs(a-b)>.001:moves[round(a)]=round(b)
 class Adjust(ast.NodeTransformer):
  def visit_FunctionDef(self,node):
   return self.generic_visit(node) if node.name=='build' else node
  def visit_Tuple(self,node):
   if len(node.elts)==2 and all(isinstance(e,ast.Constant) and isinstance(e.value,(int,float)) for e in node.elts):
    y=node.elts[1].value
    if y in moves:node.elts[1]=ast.Constant(moves[y])
   return self.generic_visit(node)
 t=Adjust().visit(ast.parse(s));ast.fix_missing_locations(t);s=ast.unparse(t)+'\n';s=s.replace('Keyshape.VRECT_XL','Keyshape.VRECT_L').replace('Keyshape.HRECT_XL','Keyshape.HRECT_L');p.write_text(s)
