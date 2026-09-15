from pathlib import Path
exec(Path(__file__).with_name('repair.py').read_text().split("dollar='''")[0])
# This helper exposes every requested contact on a real circle.
HELPER+='''
def circle_nodes(name,cx,cy,r,nodes=()):
    import math
    pts=set(nodes)|{(cx-r,cy),(cx+r,cy),(cx,cy-r),(cx,cy+r)}
    assert all((x-cx)**2+(y-cy)**2==r*r for x,y in pts)
    pts=sorted(pts,key=lambda p:math.atan2(p[1]-cy,p[0]-cx))
    path(name,pts[0],[('A',pt,r,r,True) for pt in pts[1:]+pts[:1]],True)
'''
patch('workflow-exit-door','''
oval('left',13,15,5);oval('right',35,35,5)
self.add_line('above',(13,4),(13,10));self.add_line('below',(13,20),(13,44))
path('branch',(18,15),[('L',(31,15)),('A',(35,19),4,4,True),('L',(35,30))])
for s in ['above','below','branch']:self.relate('connect',s,'left')
self.relate('connect','branch','right')
''','VRECT_L; equal circular nodes, truly vertical rails and one tangent radius-four elbow.')
for id in ['workflow-merge-1','workflow-merge-interface-essential']:
 patch(id,'''
oval('top',24,9,5);oval('left',13,39,5);oval('right',35,39,5)
self.add_line('stem',(24,14),(24,20))
path('left-branch',(24,20),[('C',(24,26),(13,24),(13,34))])
path('right-branch',(24,20),[('C',(24,26),(35,24),(35,34))])
self.relate('connect','stem','top')
for side in ['left','right']:
 self.relate('connect',side+'-branch',side);self.relate('connect',side+'-branch','stem')
self.relate('connect','left-branch','right-branch')
''','VRECT_L; identical round nodes and mirrored continuous branches; tiny stem arc and mismatched bends removed.')
patch('molecule-bd75597b','''
circle_nodes('top',24,18,10,[(18,26),(30,26)])
circle_nodes('left',9,35,5,[(12,31)]);circle_nodes('right',39,35,5,[(36,31)])
self.add_line('left-bond',(18,26),(12,31));self.add_line('right-bond',(30,26),(36,31))
for side in ['left','right']:
 self.relate('connect',side+'-bond',side);self.relate('connect',side+'-bond','top')
''','HRECT_L; mirrored bonds end on exact circular nodes; internal bond protrusions removed.')
patch('science-molecule-strucutre','''
oval('top',24,11,5)
circle_nodes('left',11,37,5,[(15,34)]);circle_nodes('right',37,37,5,[(33,34)])
self.add_line('stem',(24,16),(24,27));self.add_polyline('bonds',(15,34),(24,27),(33,34))
self.relate('connect','stem','top');self.relate('connect','stem','bonds')
self.relate('connect','bonds','left');self.relate('connect','bonds','right')
''','SQUARE; equal circular terminals, reflected bonds, and exact 3:4 boundary contacts.')
patch('needles-two','''
oval('lower',37,37,5);circle_nodes('upper',21,11,5,[(18,15)])
self.add_line('lower-pin',(6,37),(32,37));self.add_line('upper-pin',(6,27),(18,15))
self.relate('connect','lower-pin','lower');self.relate('connect','upper-pin','upper')
''','SQUARE; both needle heads have the same radius; diagonal pin meets an explicit circle node.')
for id in ['gender-male','gender-male-users']:
 patch(id,'''
circle_nodes('ring',18,32,10,[(24,24)])
self.add_line('shaft',(24,24),(36,8));self.add_polyline('arrow',(26,8),(36,8),(36,18))
self.relate('connect','shaft','ring');self.relate('connect','shaft','arrow')
''','CIRCLE; true circular ring, exact shaft attachment and equal arrow arms.',key='CIRCLE')
patch('search','''
path('lens',(6,20),[('C',(6,12.268),(12.268,6),(20,6)),('C',(27.732,6),(34,12.268),(34,20)),
 ('C',(34,24),(33,27),(30,30)),('C',(27,33),(24,34),(20,34)),('C',(12.268,34),(6,27.732),(6,20))],True)
self.add_line('handle',(30,30),(42,42));self.relate('connect','handle','lens')
''','SQUARE; a tangent-continuous round lens with an exact diagonal handle node and no internal tip.')
patch('navigation-direction-right-forward','''
path('arrow',(28,8),[('L',(28,17)),('L',(20,17)),('A',(4,33),16,16,False),('L',(4,40)),
 ('C',(7,33),(12,31),(20,31)),('L',(28,31)),('L',(28,40)),('L',(44,24)),('L',(28,8))],True)
''','HRECT_L; one coherent closed arrow with a smooth return and no extra one-unit tail.')
patch('face','''
oval('head',24,24,20)
path('hair',(4,24),[('C',(12,24),(20,19),(24,12)),('C',(28,19),(36,24),(44,24))])
self.relate('connect','hair','head')
''','CIRCLE; mirrored hair sweeps and exact head contacts replace the uneven fitted arcs.')
patch('rectangle-with-circle','''
circle_nodes('circle',32,32,10,[(26,24),(24,26)])
self.add_polyline('triangle',(26,24),(17,6),(6,26),(24,26));self.relate('connect','triangle','circle')
''','SQUARE; two true shared overlap nodes eliminate both protruding triangle endpoints.')
patch('sliced-pie','''
circle_nodes('outer',24,24,20,[(12,40)]);circle_nodes('inner',24,24,5,[(21,28)])
for name,a,b in [('top',(24,4),(24,19)),('right',(29,24),(44,24)),('lower',(21,28),(12,40))]:
 self.add_line(name,a,b);self.relate('connect',name,'outer');self.relate('connect',name,'inner')
''','CIRCLE; concentric rings and an exactly radial lower spoke with shared circle nodes.')
for id,flip in [('soccer',False),('soccer-ball',True)]:
 patch(id,f'''
flip={flip!r}
def pt(p):return (p[0],48-p[1]) if flip else p
vertices=[(19,18),(29,18),(32,28),(24,34),(16,28)]
outer=[(12,8),(36,8),(40,36),(24,44),(8,36)]
circle_nodes('ball',24,24,20,[pt(p) for p in outer])
self.add_polyline('panel',*[pt(p) for p in vertices],closed=True)
for i,(a,b) in enumerate(zip(vertices,outer)):
 self.add_line(f'seam-{{i}}',pt(a),pt(b));self.relate('connect',f'seam-{{i}}','panel');self.relate('connect',f'seam-{{i}}','ball')
''','CIRCLE; reflected pentagonal panel and five seams ending on real circle nodes, without uneven edge intrusions.')
for id in ['earth','earth-maps']:
 patch(id,'''
circle_nodes('globe',24,24,20,[(8,12),(12,40),(36,8),(40,36)])
path('west',(8,12),[('C',(10,12),(13,14),(15,16)),('L',(13,24)),('C',(13,26),(18,27),(21,28)),('C',(21,34),(18,39),(12,40))])
path('east',(36,8),[('C',(30,9),(27,12),(27,16)),('C',(27,18),(31,20),(33,22)),('L',(34,29)),('C',(36,33),(37,35),(40,36))])
self.relate('connect','west','globe');self.relate('connect','east','globe')
''','CIRCLE; clean continent curves end exactly on the globe; fitted corner detours and partial contacts removed.')
patch('planting','''
path('left-leaf',(24,22),[('C',(13,22),(8,14),(8,4)),('C',(18,4),(24,12),(24,22))],True)
path('right-leaf',(24,22),[('C',(24,12),(30,4),(40,4)),('C',(40,14),(35,22),(24,22))],True)
self.add_line('stem',(24,22),(24,32))
path('soil',(8,44),[('C',(10,37),(16,32),(24,32)),('C',(32,32),(38,37),(40,44)),('L',(8,44))],True)
self.relate('connect','stem','soil');self.relate('connect','stem','left-leaf');self.relate('connect','stem','right-leaf');self.relate('connect','left-leaf','right-leaf')
''','VRECT_L; paired smooth leaves and a symmetric mound with an explicit stem node.')
patch('ecology-leaf','''
path('outline',(44,8),[('C',(44,24),(39,35),(27,39)),('C',(25,40),(22,40),(20,40)),
 ('C',(14,40),(10,38),(8,34)),('C',(2,24),(13,12),(23,12)),('L',(32,12)),('C',(38,12),(41,10),(44,8))],True)
path('vein',(4,38),[('L',(8,34)),('C',(14,28),(20,24),(27,21))])
self.relate('connect','vein','outline')
''','HRECT_L; a small set of continuous leaf curves owns the outline, with an exact vein/stem junction.')
patch('duster','''
self.add_line('handle',(6,42),(21,27))
path('head',(21,27),[('C',(17,23),(17,18),(23,17)),('C',(23,13),(25,11),(29,11)),
 ('C',(29,8),(30,6),(33,6)),('C',(35,6),(40,11),(42,14)),
 ('C',(42,17),(40,19),(37,19)),('C',(37,23),(34,25),(31,25)),
 ('C',(31,32),(25,31),(21,27))],True)
self.relate('connect','handle','head')
''','SQUARE; a smooth scalloped duster head and a single exact handle junction replace fragmented fitted curves.')
# Keep the recognizable three-blade organization while owning every circle contact.
patch('chrome-logo','''
# The integer contact nodes are explicit; every arc has a continuous radial tangent.
import math
def ring(name,cx,cy,nodes):
 commands=[]
 for a,b in zip(nodes,nodes[1:]+nodes[:1]):
  aa=math.atan2(a[1]-cy,a[0]-cx);bb=math.atan2(b[1]-cy,b[0]-cx)
  angle=(bb-aa)%(2*math.pi);ra=math.dist(a,(cx,cy));rb=math.dist(b,(cx,cy))
  f=4/3*math.tan(angle/4)*(.99 if name=='outer' else 1)
  commands.append(('C',(a[0]-math.sin(aa)*ra*f,a[1]+math.cos(aa)*ra*f),(b[0]+math.sin(bb)*rb*f,b[1]-math.cos(bb)*rb*f),b))
 path(name,nodes[0],commands,True)
ring('outer',24,24,[(24,4),(42,16),(44,24),(24,44),(4,24),(8,12)])
ring('inner',24,24,[(24,16),(32,24),(31,28),(24,32),(17,28),(16,24)])
for name,a,b in [('right',(24,16),(42,16)),('lower',(31,28),(24,44)),('left',(17,28),(8,12))]:
 self.add_line(name,a,b);self.relate('connect',name,'outer');self.relate('connect',name,'inner')
''','CIRCLE; three clean spinning blades meet explicit nodes on smooth concentric outlines, with continuous curve tangents.')
(H/'final-junctions.json').write_text(json.dumps(changes,indent=2))
print('Rebuilt junctions',len(changes))
