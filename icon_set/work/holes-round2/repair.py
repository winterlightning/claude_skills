from pathlib import Path
import ast,json,inspect,sys,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/hole-fix-plan.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
names=[n for n in json.loads((ROOT/SOURCE_PATH).read_text())['recommendations'] if n not in ['horse-head-v2','user-with-gear']]
if not (W/'mapping.json').exists():
 rows=[]
 for n in names:
  p,new,s=prepare_variant(n,'solo','Open counters and smoother curves');p.write_text(s);(W/(n+'-before.svg')).write_text(inspect_icon(create(n))['_svg']);rows.append({'original':n,'candidate':new,'file':str(p),'source':inspect.getsourcefile(type(create(n)))})
 (W/'mapping.json').write_text(json.dumps(rows,indent=2))
rows=json.loads((W/'mapping.json').read_text())
helper='''
def _circle(self, name, x, y, r, ry=None):
    # A shared center and two exact half ellipses own each opening.
    ry = r if ry is None else ry
    self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
    self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
    self.add_contour(name,name+'-a',name+'-b',closed=True)
def _path(self, name, start, parts, closed=False):
    ids=[];p=start
    for j,s in enumerate(parts):
        i=f'{name}-{j}';q=s[1]
        if s[0]=='L': self.add_line(i,p,q)
        else: self.add_arc(i,p,q,radius_x=s[2],radius_y=s[3],sweep=s[4])
        ids.append(i);p=q
    self.add_contour(name,*ids,closed=closed)
'''
bodies={}
def put(n,body,key=None):bodies[n]=(textwrap.dedent(body),key)
put('amazon-connect','''
# Three round nodes, with branches attached at their axial endpoints.
for name,x,y in [('top',24,13),('left',9,35),('right',39,35)]: self._circle(name,x,y,5)
self.add_polyline('branches',(9,30),(24,18),(39,30))
for n in ['top','left','right']: self.relate('connect',n,'branches')
''')
put('computer-chip-core','''
# Concentric squares and a shared eight-unit pin pitch.
self.add_polyline('body',(11,11),(37,11),(37,37),(11,37),closed=True)
self.add_polyline('core',(20,20),(28,20),(28,28),(20,28),closed=True)
for j,t in enumerate([16,24,32]):
 for side,a,b in [('t',(t,6),(t,11)),('b',(t,37),(t,42)),('l',(6,t),(11,t)),('r',(37,t),(42,t))]:
  n=f'pin-{side}-{j}';self.add_line(n,a,b);self.relate('connect',n,'body')
''')
put('canoe-paddles-outdoors','''
# Matching blades rotated around the canvas center. Crossbars divide roomy caps.
for j in range(2):
 def P(x,y): return (x,y) if j==0 else (48-x,48-y)
 n=f'blade-{j}'
 self._path(n,P(8,10),[('A',P(20,10),6,6,True),('L',P(20,19)),('L',P(14,25)),('L',P(8,19)),('L',P(8,10))],True)
 self.add_line(n+'-bar',P(8,14),P(20,14));self.add_line(n+'-shaft',P(14,25),P(14,44))
 self.relate('connect',n,n+'-bar');self.relate('connect',n,n+'-shaft')
''')
for n in ['cracked-shield','shield-c3034182']:
 put(n,'''
# Mirrored shoulder and side geometry; crest and lower tip retain deliberate corners.
self._path('shield',(24,4),[('L',(16,8)),('A',(8,10),16,16,True),('L',(8,22)),('A',(24,44),24,24,False),('A',(40,22),24,24,False),('L',(40,10)),('A',(32,8),16,16,True),('L',(24,4))],True)
'''+("self.add_polyline('crack',(32,8),(22,20),(30,24),(23,35));self.relate('connect','crack','shield')\n" if n=='cracked-shield' else ''))
put('floppy-disk-v2','''
self.add_polyline('case',(6,6),(42,6),(42,42),(6,42),closed=True)
for name,pts in [('shutter',[(15,6),(15,15),(33,15),(33,6)]),('label',[(15,42),(15,33),(33,33),(33,42)])]:
 self.add_polyline(name,*pts);self.relate('connect','case',name)
self.add_dot('hub',(24,24))
''')
put('round-cap','''
self._path('outer',(44,8),[('L',(20,8)),('A',(20,40),16,16,False),('L',(44,40))])
self._circle('loop',19,24,5)
self.add_line('rail',(24,24),(44,24));self.relate('connect','loop','rail')
''')
put('presentation','''
self.add_line('rail',(4,8),(44,8))
self.add_polyline('screen',(8,8),(8,25),(24,25),(40,25),(40,8))
self.relate('connect','screen','rail')
self._circle('pull',24,35,5)
self.add_line('cord',(24,25),(24,30));self.relate('connect','cord','screen');self.relate('connect','cord','pull')
''')
put('war-flag-guild-faction','''
self._circle('finial',13,9,5)
self.add_polyline('pole',(13,14),(13,18),(13,34),(13,44))
self.add_polyline('flag',(13,18),(40,18),(34,26),(40,34),(13,34))
self.relate('connect','finial','pole');self.relate('connect','pole','flag')
''')
put('picker-take','''
# Round bulb, compact nozzle, and a separate full-sized droplet.
self._path('bulb',(15,13),[('A',(33,13),9,9,True),('L',(15,13))],True)
self.add_line('rim',(8,13),(40,13));self.relate('connect','rim','bulb')
self.add_polyline('nozzle',(15,13),(15,21),(24,25),(33,21),(33,13));self.relate('connect','nozzle','rim');self.relate('connect','nozzle','bulb')
self._path('drop',(24,34),[('A',(30,39),7,7,True),('A',(18,39),6,5,True),('A',(24,34),7,7,True)],True)
''')
put('power-outlet-type-m','''
self._path('case',(12,6),[('L',(36,6)),('A',(42,12),6,6,True),('L',(42,36)),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,12)),('A',(12,6),6,6,True)],True)
for n,x,y,r in [('earth',24,16,4),('left',15,32,3),('right',33,32,3)]:self._circle(n,x,y,r)
''')
put('one-eye-smile','''
self._circle('face',24,24,20)
self._circle('eye',19,19,4)
self.add_polyline('wink',(33,17),(31,20),(33,23))
self.add_arc('smile',(16,32),(32,32),radius_x=10,radius_y=4,sweep=False)
''')
put('earth-model-1','''
# Offset globe and meridian preserve a larger globe with clear mounting space.
self._circle('globe',18,16,10)
self._path('meridian',(32,4),[('A',(40,20),20,20,True),('A',(22,34),18,14,True),('A',(8,32),24,24,True)])
self.add_line('stem',(22,34),(22,36));self.relate('connect','stem','meridian')
self._path('base',(13,44),[('A',(22,36),9,8,True),('A',(31,44),9,8,True),('L',(13,44))],True)
self.relate('connect','stem','base')
''')
put('diamond-shine','''
# Tall faceted crystal, symmetric facet junctions and detached rays.
self.add_polyline('outline',(24,4),(32,14),(32,30),(24,44),(16,30),(16,14),closed=True)
self.add_polyline('top',(16,14),(24,18),(32,14))
self.add_polyline('bottom',(16,30),(24,30),(32,30))
self.add_line('spine',(24,18),(24,30))
for a,b in [('outline','top'),('outline','bottom'),('top','spine'),('bottom','spine')]:self.relate('connect',a,b)
for j,x in enumerate([8,40]): self.add_line(f'ray-{j}',(x,19),(x,25))
''')
for n in ['nagras','nagras-money']:
 put(n,'''
# A shared N skeleton with crossbars at the same two heights.
self.add_polyline('letter',(10,44),(10,4),(38,44),(38,4))
for j,y in enumerate([20,28]):
 self.add_line(f'bar-{j}',(8,y),(40,y));self.relate('connect','letter',f'bar-{j}')
''')
put('legal-scale-1','''
self._circle('pivot',24,13,5)
self.add_line('post',(24,18),(24,40));self.add_line('foot',(16,40),(32,40))
self.relate('connect','post','pivot');self.relate('connect','post','foot')
for j,x in enumerate([10,38]):
 n=f'pan-{j}'
 self.add_polyline(n+'-cord',(x-6,27),(x,13),(x+6,27))
 self._path(n,(x-6,27),[('L',(x+6,27)),('A',(x-6,27),6,7,True)],True)
 self.add_line(n+'-beam',(x,13),(19 if j==0 else 29,13))
 self.relate('connect',n,n+'-cord');self.relate('connect',n+'-beam',n+'-cord');self.relate('connect',n+'-beam','pivot')
''')
put('meeting-headphone-wireless','''
# One signal arc leaves room for a broad headband and full earcup openings.
self.add_arc('signal',(14,8),(34,8),radius_x=10,radius_y=4)
self.add_arc('band',(8,29),(40,29),radius_x=16,radius_y=12)
for j,x in enumerate([8,32]):
 n=f'cup-{j}';self._path(n,(x,29),[('L',(x+8,29)),('L',(x+8,36)),('A',(x+4,40),4,4,True),('A',(x,36),4,4,True),('L',(x,29))],True);self.relate('connect',n,'band')
self._circle('mic',24,40,4)
self._path('boom',(36,40),[('A',(32,44),4,4,True),('L',(24,44))]);self.relate('connect','boom','cup-1');self.relate('connect','boom','mic')
''')
put('ghost-scare','''
# A semicircular head and matching broad arm pockets.
self._path('body',(15,17),[('A',(33,17),9,9,True),('L',(33,32)),('L',(38,40)),('L',(31,38)),('L',(24,40)),('L',(17,38)),('L',(10,40)),('L',(15,32)),('L',(15,17))],True)
for j in range(2):
 def P(x,y):return (x,y) if j==0 else (48-x,y)
 n=f'arm-{j}';self._path(n,P(15,20),[('L',P(4,15)),('A',P(15,32),11,17,j==1)])
 self.relate('connect',n,'body')
''')
put('strategy-split','''
# Broad matching arrowheads; the branch curves share one exact origin.
self.add_polyline('up',(17,18),(24,6),(31,18),closed=True)
self.add_polyline('left',(6,21),(18,23),(9,34),closed=True)
self.add_polyline('right',(42,21),(30,23),(39,34),closed=True)
self.add_polyline('stem',(24,42),(24,38),(24,18));self.relate('connect','stem','up')
for n,p,sweep in [('left',(14,28),False),('right',(34,28),True)]:
 self.add_arc(n+'-branch',(24,38),p,radius_x=10,radius_y=10,sweep=sweep);self.relate('connect','stem',n+'-branch');self.relate('connect',n,n+'-branch')
''')
put('power-outlet-type-m',"""
# Three open round sockets need the circular outlet envelope to retain clearance.
self._circle('case',24,24,20)
for n,x,y in [('earth',24,16),('left',16,28),('right',32,28)]:self._circle(n,x,y,3)
""",'CIRCLE')
put('skull-c8f4a237',"""
# Smooth cranium and jaw. Solid eye marks replace the crowded nested eye rings.
self._path('skull',(6,24),[('A',(42,24),18,18,True),('A',(34,34),8,10,True),('L',(34,38)),('A',(30,42),4,4,True),('L',(18,42)),('A',(14,38),4,4,True),('L',(14,34)),('A',(6,24),8,10,True)],True)
self.add_dot('left-eye',(16,20));self.add_dot('right-eye',(32,20))
self._circle('nose',24,28,3)
self.add_line('tooth',(24,40),(24,42));self.relate('connect','tooth','skull')
""",'SQUARE')
# Preserve these subjects closely, changing their owning local geometry.
for m in rows:
 n=m['original'];p=Path(m['file']);src=Path(m['source']).read_text();tree=ast.parse(p.read_text());cls=next(c for c in tree.body if isinstance(c,ast.ClassDef) and any(isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in a.targets) and isinstance(a.value,ast.Constant) and a.value.value==m['candidate'] for a in c.body))
 original=inspect.getsource(type(create(n)));oc=ast.parse(original).body[0]
 if n in bodies:
  body,key=bodies[n];methods=ast.parse(helper+'\ndef build(self):\n'+textwrap.indent(body,'    ')).body
 else:
  methods=[a for a in oc.body if isinstance(a,ast.FunctionDef)];s=ast.unparse(ast.Module(body=methods,type_ignores=[]))
  if n=='horse-head':s=s.replace('radius_x=8, sweep=True','radius_x=4, radius_y=8, sweep=True').replace('(25, 21)', '(21, 24)').replace('radius_x=60, radius_y=60','radius_x=30, radius_y=30').replace("radius_x=30, radius_y=30, sweep=True","radius_x=30, radius_y=30, sweep=False")
  if n=='pencil-sketch-design':s=s.replace('(39, 17)','(35, 21)').replace('(31, 9)','(27, 13)')
  if n=='megaphone-7a36c569':s=s.replace('(42, 31)','(42, 27)').replace('(8, 39)','(8, 35)').replace('(26, 35)','(29, 30)').replace('(15, 37)','(13, 34)').replace('radius_x=6','radius_x=10').replace('radius_x=8','radius_x=10')
  if n=='staffordshire-bull-terrier':s=s.replace('(10, 21)','(13, 21)').replace('(11, 17)','(14, 17)').replace('(11, 27)','(14, 27)').replace('(37, 17)','(34, 17)').replace('(37, 27)','(34, 27)').replace('(38, 18)','(34, 17)').replace("self.add_line('e0', (27, 30), (21, 30))","self.add_line('e0', (29, 27), (19, 27))").replace("self.add_arc('e10', (21, 30), (27, 30), radius_x=3, sweep=False)","self.add_arc('e10', (19, 27), (29, 27), radius_x=5, radius_y=7, sweep=False)").replace('(24, 33)','(24, 34)')
  if n=='skull-c8f4a237':
   start=s.index("    self.add_arc('sym-e32'");end=s.index("    self.add_contour('sym-c0'",start)
   s=s[:start]+"    self._circle('nose',24,32,4)\n"+s[end:]
   s='\n'.join(l for l in s.splitlines() if "self.add_contour('sym-c4'" not in l)
  methods=ast.parse(helper+'\n'+s).body;key=None
 cls.body=[a for a in cls.body if not isinstance(a,ast.FunctionDef)]+methods
 if n in bodies and bodies[n][1]:
  for a in cls.body:
   if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='keyshape' for t in a.targets):a.value=ast.parse('Keyshape.'+bodies[n][1],mode='eval').body
 for a in tree.body:
  if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in a.targets):a.value=ast.Constant('gpt-6')
 ast.fix_missing_locations(tree);p.write_text(ast.unparse(tree)+'\n')
print('Wrote',len(rows),'review variants')
