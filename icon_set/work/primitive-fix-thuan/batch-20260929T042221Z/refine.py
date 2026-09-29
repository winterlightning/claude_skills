import ast

def revise(i,replacements,plan=None,reason=None):
 r=records[i];run=Path(r['run']);meta=json.loads((run/'candidate.json').read_text());source=Path(r['module']).read_text();tree=ast.parse(source)
 cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));method=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='build')
 lines=source.splitlines();body='\n'.join(line[8:] for line in lines[method.body[0].lineno-1:method.end_lineno])
 for a,b in replacements:
  assert a in body,(i,a);body=body.replace(a,b)
 return author(i,body,next(n.value.attr for n in cls.body if isinstance(n,ast.Assign) and n.targets[0].id=='keyshape'),meta['comparison'],plan or meta['plan'],meta['construction_references'],meta['omissions'],reason or meta['gate'].get('exception',{}).get('reason'))

revise(1,[("(28,43),('A',(4,24)","(22,43),('A',(4,24)")],plan='Closed queasy eyelids and pursed mouth with an organic breath puff fully separated from the lower-right face opening.')
revise(5,[("self.path('steering',(8,40)","self.path('steering',(8,36)"),("self.add_line('deck',(12,40),(35,40))","self.path('deck',(12,40),('L',(21,40)),('L',(29,40)),('L',(35,40)))")],plan='Left-facing scooter with two open wheel centers; swept rabbit ear, distinct muzzle, curved haunch, reaching arm and feet on a deck with explicit shared foot junctions.')
# Replace uneven polygon by an eight-tooth rotationally symmetric gear built from shared quarter-pattern.
author(10,'''
# Each quarter is rotated about (24,24); one shared tooth definition prevents asymmetry.
quarter=[(21,12),(27,12),(28,16),(32,16),(32,20),(36,21)]
points=[]
for turn in range(4):
    for x,y in quarter:
        dx,dy=x-24,y-24
        for _ in range(turn): dx,dy=-dy,dx
        p=(24+dx,24+dy)
        if not points or p!=points[-1]:points.append(p)
self.add_polyline('gear',*points,closed=True)
for name,p,q in [('top',(24,3),(24,6)),('bottom',(24,42),(24,45)),('left',(3,24),(6,24)),('right',(42,24),(45,24)),('nw',(7,7),(10,10)),('ne',(38,10),(41,7)),('sw',(7,41),(10,38)),('se',(38,38),(41,41))]:
    self.add_line(name,p,q)
''','SQUARE','The rejected cog used four dots instead of radiating strokes and lost its tooth rhythm. Feedback asks to recover the radiating cog meaning.',
 'Rotationally symmetric eight-tooth gear surrounded by eight short radial strokes. Shared quarter-pattern controls tooth equality and spacing.',
 'Lucide settings: repeating toothed silhouette; supplied reference controls surrounding radiance.',
 'Tooth count regularized to eight for a balanced native-size gear; source has no central hub.',
 exception_reason='Eight rays and cog require compact gaps and a radial envelope slightly larger than SQUARE. All strokes remain4px inside48px; user authorized native-size visual exception.')
