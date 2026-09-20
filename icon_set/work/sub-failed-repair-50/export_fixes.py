import ast,json
from pathlib import Path
W=Path(__file__).parent;c=json.loads((W/'candidates.json').read_text())
def fix(n,changes=None,new_body=None,shape=None):
 p=Path(c[str(n)]['python_source']);s=p.read_text()
 for old,new in (changes or {}).items():
  assert old in s,(n,old);s=s.replace(old,new)
 t=ast.parse(s);cl=next(x for x in t.body if isinstance(x,ast.ClassDef))
 if new_body:
  b=next(x for x in cl.body if isinstance(x,ast.FunctionDef) and x.name=='build');b.body=ast.parse(new_body).body
 if shape:
  for x in cl.body:
   if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='keyshape' for y in x.targets):x.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),shape,ast.Load())
 ast.fix_missing_locations(t);p.write_text(ast.unparse(t)+'\n')
fix(1,{"box(self, 'nozzle', 8, 2, 16, 12, 2)":"self.add_line('nozzle-left',(8,12),(8,4))\n        self.add_arc('nozzle-tl',(8,4),(10,2),radius_x=2)\n        self.add_line('nozzle-top',(10,2),(14,2))\n        self.add_arc('nozzle-tr',(14,2),(16,4),radius_x=2)\n        self.add_line('nozzle-right',(16,4),(16,12))\n        self.add_contour('nozzle','nozzle-left','nozzle-tl','nozzle-top','nozzle-tr','nozzle-right')"})
fix(28,{"box(self, 'handle', 10, 2, 22, 10, 3)":"self.add_line('handle-left',(10,10),(10,5))\n        self.add_arc('handle-tl',(10,5),(13,2),radius_x=3)\n        self.add_line('handle-top',(13,2),(19,2))\n        self.add_arc('handle-tr',(19,2),(22,5),radius_x=3)\n        self.add_line('handle-right',(22,5),(22,10))\n        self.add_contour('handle','handle-left','handle-tl','handle-top','handle-tr','handle-right')"})
fix(8,new_body="""
self.add_polyline('bag',(4,12),(28,12),(30,30),(2,30),closed=True)
self.add_line('handle-left',(11,16),(11,7))
self.add_arc('handle-top',(11,7),(21,7),radius_x=5)
self.add_line('handle-right',(21,7),(21,16))
self.add_contour('handle','handle-left','handle-top','handle-right')
self.relate('connect','bag','handle')
""",shape='SQUARE')
fix(9,new_body="""
self.add_line('top',(4,12),(28,12))
self.add_bezier('right',(28,12),((28,17),(30,22),(30,26)))
self.add_arc('corner-r',(30,26),(26,30),radius_x=4)
self.add_line('base',(26,30),(6,30))
self.add_arc('corner-l',(6,30),(2,26),radius_x=4)
self.add_bezier('left',(2,26),((2,22),(4,17),(4,12)))
self.add_contour('bag','top','right','corner-r','base','corner-l','left',closed=True)
self.add_line('handle-left',(11,16),(11,7))
self.add_arc('handle-top',(11,7),(21,7),radius_x=5)
self.add_line('handle-right',(21,7),(21,16))
self.add_contour('handle','handle-left','handle-top','handle-right')
self.relate('connect','bag','handle')
""",shape='SQUARE')
fix(39,new_body="""
self.add_line('roof-lower-left',(7,13),(10,7))
self.add_bezier('roof-left',(10,7),((11,5),(12,4),(14,4)))
self.add_line('roof-top',(14,4),(18,4))
self.add_bezier('roof-right',(18,4),((20,4),(21,5),(22,7)))
self.add_line('roof-lower-right',(22,7),(25,13))
self.add_contour('roof','roof-lower-left','roof-left','roof-top','roof-right','roof-lower-right')
self.add_bezier('rear',(5,24),((2,24),(2,21),(2,18)))
self.add_arc('rear-top',(2,18),(7,13),radius_x=5)
self.add_line('hood',(7,13),(25,13))
self.add_arc('front-top',(25,13),(30,18),radius_x=5)
self.add_bezier('front',(30,18),((30,21),(30,24),(27,24)))
self.add_contour('body','rear','rear-top','hood','front-top','front')
for cx in (9,23):
    circle(self,f'wheel-{cx}',cx,24,4)
    self.relate('connect','body',f'wheel-{cx}')
self.add_line('chassis',(13,24),(19,24))
self.relate('connect','chassis','wheel-9');self.relate('connect','chassis','wheel-23')
self.relate('connect','roof','body')
""")
