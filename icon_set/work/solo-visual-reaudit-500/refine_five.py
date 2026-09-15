from repair import *
for n in [13,14,17]:
 r=next(r for r in records if r['number']==n);s=(ROOT/r['file']).read_text();t=ast.parse(s);cl=next(x for x in t.body if isinstance(x,ast.ClassDef));b=next(x for x in cl.body if isinstance(x,ast.FunctionDef) and x.name=='build')
 for c in ast.walk(b):
  if isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and c.func.attr=='add_arc' and isinstance(c.args[0],ast.Constant) and c.args[0].value=='torso':
   start=ast.literal_eval(c.args[1]);end=ast.literal_eval(c.args[2]);sx,sy=start;ex,ey=end
   c.func.attr='add_bezier';c.args=[c.args[0],c.args[1],ast.parse(repr(((sx,sy+3),(ex,ey-3),end)),mode='eval').body];c.keywords=[]
 if n==13:
  # Water wave now sits under the bow with legal separation from the hull.
  for c in ast.walk(b):
   if isinstance(c,ast.Tuple) and ast.literal_eval(c) if False else False:pass
  s=ast.unparse(b).replace("('water', [(6, 42), (14, 42)])","('water', [(6, 42), (10, 42)])")
  b=ast.parse(s).body[0]
 body='\n'.join(ast.unparse(x) for x in b.body[1:]);save(n,body,r['reason'].replace('arc radius10','curve').replace('Torso arc','Torso curve'))
for n in [15]:
 r=next(r for r in records if r['number']==n);t=ast.parse((ROOT/r['file']).read_text());b=next(x for x in ast.walk(t) if isinstance(x,ast.FunctionDef) and x.name=='build');body='\n'.join(ast.unparse(x) for x in b.body[1:]);body=body.replace("self.ring('cockpit', 16, 24, 3)","""self.add_arc('cockpit-t',(13,22),(19,22),radius_x=3)
self.add_line('cockpit-r',(19,22),(19,26))
self.add_arc('cockpit-b',(19,26),(13,26),radius_x=3)
self.add_line('cockpit-l',(13,26),(13,22))
self.add_contour('cockpit','cockpit-t','cockpit-r','cockpit-b','cockpit-l',closed=True)""");save(n,body,r['reason'])
