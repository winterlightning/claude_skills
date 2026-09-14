import ast,json,sys,textwrap
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/circle-bounds-review/queue.json'
AUTHOR='gpt-6'
w=Path(__file__).parent
if not (w/'mapping.json').exists():
 rows=[]
 for r in json.loads((w/'queue.json').read_text()):
  p,n,s=prepare_variant(r['id'],'solo','Exact circle envelope and clear internal spacing');p.write_text(s);rows.append({'original':r['id'],'candidate':n,'file':str(p),'source':r['file']})
 (w/'mapping.json').write_text(json.dumps(rows,indent=2))
helper='''
def _circle(self,name,x,y,r):
    # Shared center and radius keep the four quarters tangent-continuous.
    pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
    for i in range(4):self.add_arc(f'{name}-{i}',pts[i],pts[i+1],radius_x=r,radius_y=r)
    self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
'''
bodies={
'compact-disc':"self._circle('rim',24,24,20)\nself._circle('hub',24,24,6)",
'compact-disc-with-partition-segment':"""
self._circle('rim',24,24,20)
self._circle('hub',24,24,4)
self.add_line('sector-right',(44,24),(37,24))
self.add_arc('sector-turn',(37,24),(24,37),radius_x=13)
self.add_line('sector-bottom',(24,37),(24,44))
self.add_contour('sector','sector-right','sector-turn','sector-bottom')
self.relate('connect','rim','sector')
""",
'compact-disc-with-sheen-arcs':"""
self._circle('rim',24,24,20)
self._circle('hub',24,24,3)
self.add_arc('sheen-upper',(25,13),(35,23),radius_x=10)
self.add_arc('sheen-lower',(23,35),(13,25),radius_x=10)
""",
'cracked-compact-disc':"""
# The open rim uses one circle, including the integer 3:4:5 point at (12,8).
pts=[(12,8),(4,24),(24,44),(44,24),(24,4)]
for i in range(4):self.add_arc(f'rim-{i}',pts[i],pts[i+1],radius_x=20,sweep=False)
self.add_contour('rim',*[f'rim-{i}' for i in range(4)])
self.add_polyline('crack',(24,4),(16,18),(29,18),(18,34))
self.relate('connect','rim','crack')
""",
'face-wearing-round-glasses':"""
self._circle('face',24,24,20)
for name,x in [('lens-left',17),('lens-right',31)]:self._circle(name,x,21,4)
self.add_line('bridge',(21,21),(27,21))
for n in ['lens-left','lens-right']:self.relate('connect','bridge',n)
self.add_arc('smile',(18,33),(30,33),radius_x=8,radius_y=4,sweep=False)
""",
'disk-platter-with-drive-slots':"""
self._circle('rim',24,24,20)
self._circle('hub',24,24,3)
self.add_arc('slot-top',(22,13),(26,13),radius_x=3)
self.add_line('slot-left',(14,29),(15,31))
self.add_line('slot-right',(34,29),(33,31))
"""}
for m in json.loads((w/'mapping.json').read_text()):
 p=Path(m['file']);t=ast.parse(p.read_text());c=next(c for c in t.body if isinstance(c,ast.ClassDef));c.body=[a for a in c.body if not isinstance(a,ast.FunctionDef)]+ast.parse(helper+'\ndef build(self):\n'+textwrap.indent(textwrap.dedent(bodies[m['original']]),'    ')).body
 for a in t.body:
  if isinstance(a,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='AUTHOR' for v in a.targets):a.value=ast.Constant(AUTHOR)
 if isinstance(t.body[0],ast.Expr) and isinstance(t.body[0].value,ast.Constant):t.body[0].value=ast.Constant('CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction.')
 ast.fix_missing_locations(t);p.write_text(ast.unparse(t)+'\n')
