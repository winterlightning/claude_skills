"""Independent variants responding to the four specific review comments."""
import sys,json,ast,textwrap
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT));sys.path.insert(0,str(W.parent/'side-repair-50-priority-10'))
from glyph_fit import fit
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-final-68/audit.json'
AUTHOR='gpt-6'
helper=ast.parse((W.parent/'side-repair-50-priority-9/author.py').read_text())
# Reuse the established rounded box/circle construction helpers.
source=ast.parse((W.parent/'sub-failed-repair-50/repair.py').read_text())
HELPERS=next(ast.literal_eval(n.value) for n in source.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
plans={}
plans['baby-head-sub32-v3']=('Sub32',"""
self.add_bezier('head-right',(28,8),((29,10),(30,13),(30,16)))
self.add_arc('head-br',(30,16),(16,30),radius_x=14)
self.add_arc('head-bl',(16,30),(2,16),radius_x=14)
self.add_arc('head-tl',(2,16),(16,2),radius_x=14)
self.add_bezier('curl',(16,2),((22,2),(24,8),(18,8)))
self.add_contour('head','head-right','head-br','head-bl','head-tl','curl')
self.add_line('eye-left',(10,16),(10,16));self.add_line('eye-right',(22,16),(22,16))
self.add_bezier('smile',(12,22),((14,24),(18,24),(20,22)))
""")
shift="""
class Offset:
 def add_line(_,n,a,b):return self.add_line(n,(a[0],a[1]+13),(b[0],b[1]+13))
 def add_bezier(_,n,a,ps):return self.add_bezier(n,(a[0],a[1]+13),tuple((x,y+13) for x,y in ps))
 def add_arc(_,n,a,b,**kw):return self.add_arc(n,(a[0],a[1]+13),(b[0],b[1]+13),**kw)
 def __getattr__(_,n):return getattr(self,n)
g=Offset()
"""
for parent,gid in [('mobile-contactless-payment-solo-profile32','symbol-dollar'),('mobile-wireless-pound-payment-solo-profile32','symbol-pound')]:
 body,_=fit(gid,26 if gid=='symbol-dollar' else 18,16,16 if gid=='symbol-dollar' else 15.5,'currency')
 plans[parent]=('TallSideSub32',"self.add_arc('wireless',(4,6),(28,6),radius_x=12,radius_y=4)\nbox(self,'phone',2,12,30,46,4)\n"+shift+body.replace('self.','g.'))
 if gid=='symbol-dollar':
  plans[parent]=(plans[parent][0],plans[parent][1].replace("box(self,'phone',2,12,30,46,4)","self.add_line('lt',(10,12),(6,12));self.add_arc('tl',(6,12),(2,16),radius_x=4,sweep=False);self.add_line('l',(2,16),(2,42));self.add_arc('bl',(2,42),(6,46),radius_x=4,sweep=False);self.add_line('lb',(6,46),(10,46));self.add_contour('left','lt','tl','l','bl','lb')\nself.add_line('rt',(22,12),(26,12));self.add_arc('tr',(26,12),(30,16),radius_x=4);self.add_line('r',(30,16),(30,42));self.add_arc('br',(30,42),(26,46),radius_x=4);self.add_line('rb',(26,46),(22,46));self.add_contour('right','rt','tr','r','br','rb')"))
plans['money-bag-sub32']=('Sub32',"""
self.add_polyline('neck-left',(8,2),(12,6));self.add_polyline('neck-right',(24,2),(20,6))
self.add_bezier('left-top',(12,6),((8,10),(2,14),(2,20)))
self.add_line('left',(2,20),(2,24));self.add_arc('bl',(2,24),(8,30),radius_x=6,sweep=False)
self.add_line('bottom',(8,30),(24,30));self.add_arc('br',(24,30),(30,24),radius_x=6,sweep=False)
self.add_line('right',(30,24),(30,20));self.add_bezier('right-top',(30,20),((30,14),(24,10),(20,6)))
self.add_contour('bag','left-top','left','bl','bottom','br','right','right-top')
self.relate('connect','neck-left','bag');self.relate('connect','neck-right','bag')
self.add_line('dollar-top',(17,14),(16,14))
self.add_arc('dollar-upper',(16,14),(16,18),radius_x=4,radius_y=2,sweep=False)
self.add_arc('dollar-lower',(16,18),(16,22),radius_x=4,radius_y=2,sweep=True)
self.add_line('dollar-bottom',(16,22),(15,22));self.add_contour('dollar','dollar-top','dollar-upper','dollar-lower','dollar-bottom')
self.add_line('tick-top',(16,12),(16,14));self.add_line('tick-bottom',(16,22),(16,23))
self.relate('connect','tick-top','dollar');self.relate('connect','tick-bottom','dollar')
""")
rows=json.load(open(W.parent/'side-repair-final-68/audit.json'));lookup={r.get('candidate'):r for r in rows};lookup.update({r['icon']:r for r in rows})
out=json.load(open(W/'candidates.json')) if (W/'candidates.json').exists() else {}
for parent,(base,body) in plans.items():
 r=lookup[parent]
 if parent in out:dst=ROOT/out[parent]['python_source'];uid=out[parent]['icon'];code=dst.read_text()
 else:
  dst,uid,code=prepare_variant(parent,'sub','User review correction; preserve earlier variants')
  dst=dst.with_name(dst.stem+'_'+r['source_uuid'].replace('-','_')+'.py')
 tree=ast.parse(code);cl=next(n for n in tree.body if isinstance(n,ast.ClassDef));cl.bases=[ast.Name(base,ast.Load())]
 tree.body=[n for n in tree.body if not isinstance(n,ast.FunctionDef)]
 for n in tree.body:
  if isinstance(n,ast.ImportFrom) and n.module in ('_base','_tall_base'):
   n.module='_tall_base' if base=='TallSideSub32' else '_base';n.names=[ast.alias(base)]
 cl.body=[n for n in cl.body if not(isinstance(n,ast.FunctionDef) and n.name=='build')]
 for n in cl.body:
  if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='keyshape' for x in n.targets):n.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),'SQUARE',ast.Load())
 cl.body+=ast.parse('def build(self):\n'+textwrap.indent(textwrap.dedent(body),'    ')).body;tree.body+=ast.parse(HELPERS).body
 ast.fix_missing_locations(tree);dst.write_text(ast.unparse(tree)+'\n');out[parent]={'icon':uid,'python_source':str(dst.relative_to(ROOT)),'source_uuid':r['source_uuid'],'source_path':r['source_path'],'parent':parent,'tall':base=='TallSideSub32'}
(W/'candidates.json').write_text(json.dumps(out,indent=2))
