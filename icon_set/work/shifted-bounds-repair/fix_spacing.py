from pathlib import Path
import json,re,ast,textwrap
W=Path(__file__).parent;ROOT=W.resolve().parents[2]
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/shifted-bounds-repair/results.json'
AUTHOR='gpt-6'
for r in json.loads((W/'results.json').read_text()):
 p=ROOT/r['file'];s=p.read_text();backup=W/'before-spacing'/p.name;backup.parent.mkdir(exist_ok=True)
 if not backup.exists():backup.write_text(s)
 s=backup.read_text()
 if r['original']=='vulture':
  s=s.replace('(32, 17)','(34, 17)').replace('(32, 23)','(34, 23)').replace("radius_x=7, radius_y=7, sweep=True)","radius_x=7, radius_y=7, sweep=True)")
  s=s.replace("self.add_arc('throat', (34, 23), (25, 30), radius_x=7, radius_y=7", "self.add_arc('throat', (34, 23), (25, 30), radius_x=9, radius_y=7")
 elif r['original']=='chicken-face':
  s=s.replace('(16, 28)','(17, 28)').replace('(32, 28)','(31, 28)')
  s=re.sub(r"self.add_polyline\('beak'.*", "self.add_polyline('beak', (19, 38), (24, 44), (29, 38))",s)
 elif r['original']=='pipe-mounted-light-bulb':
  s=s.replace("self.add_line('filament', (28, 15), (28, 24))", "self.add_line('filament', (28, 15), (28, 20))")
  s=s.replace("self.add_line('socket-base', (34, 34), (22, 34))", "self.add_line('socket-base-r', (34, 34), (28, 34))\n        self.add_line('socket-base-l', (28, 34), (22, 34))").replace("'socket-base',", "'socket-base-r', 'socket-base-l',")
  s=s[:s.index("        self.add_line('pipe-top'")]+'''        # One tangent support bend ending in the flat foot; no doubled run.
        self.add_line('pipe-top', (28, 34), (28, 36))
        self.add_arc('pipe-bend', (28, 36), (20, 44), radius_x=8)
        self.add_line('foot', (20, 44), (8, 44))
        self.add_contour('support', 'pipe-top', 'pipe-bend', 'foot')
        self.relate('connect', 'support', 'bulb')
'''
 else:
  curve=r['original']=='hammerhead-shark'
  body='''# Broad 8-unit hammer bar, 12-unit body, one swept tail.
# Lucide fish informs the reduced continuous silhouette. Gill mark omitted
# to preserve body clearance; swept profile and fin points are intentional.
points = [(6,6),(34,6),(34,14),(26,14),(26,18),(34,24),(26,26)]
for i,(a,b) in enumerate(zip(points,points[1:]),1):
    self.add_line(f'head-{i}',a,b)
self.add_arc('inner-body',(26,26),(34,32),radius_x=8,radius_y=6,sweep=False)
'''
  if curve:body+='''self.add_line('tail-upper',(34,32),(40,22))
self.add_arc('tail-end',(40,22),(40,42),radius_x=26)
self.add_line('tail-bottom',(40,42),(30,42))
'''
  else:body+='''self.add_line('tail-upper',(34,32),(42,22))
self.add_line('tail-end',(42,22),(42,42))
self.add_line('tail-bottom',(42,42),(30,42))
'''
  body+='''self.add_arc('outer-body',(30,42),(14,26),radius_x=16,sweep=True)
points = [(14,26),(6,26),(14,18),(14,14),(6,14),(6,6)]
for i,(a,b) in enumerate(zip(points,points[1:]),1):
    self.add_line(f'left-{i}',a,b)
self.add_contour('body',*[f'head-{i}' for i in range(1,7)],'inner-body','tail-upper','tail-end','tail-bottom','outer-body',*[f'left-{i}' for i in range(1,6)],closed=True)
'''
  a=next(n for n in ast.walk(ast.parse(s)) if isinstance(n,ast.FunctionDef) and n.name=='build');s='\n'.join(s.splitlines()[:a.lineno-1])+'\n    def build(self):\n'+textwrap.indent(body,'        ')
 p.write_text(s)
