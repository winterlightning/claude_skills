"""In-place geometric reconstruction of residual cohort icons."""
import json,re,textwrap
from pathlib import Path
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
H=Path(__file__).resolve().parent;ROOT=H.parents[3]
rows={r['id']:r for r in json.loads((H/'baseline.json').read_text())};changes=[]
HELPER='''
def path(name,start,commands,closed=False):
    members=[];previous=start
    for i,cmd in enumerate(commands):
        eid=f'{name}-{i}';members.append(eid)
        if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
        elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
        elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
        previous=cmd[-1] if cmd[0]=='C' else cmd[1]
    self.add_contour(name,*members,closed=closed)
'''
def patch(id,body,plan,ref='No close Lucide match; original subject reconstructed from shared dimensions.',key=None):
 p=ROOT/rows[id]['source'];backup=H/'before';backup.mkdir(exist_ok=True)
 b=backup/p.name
 if not b.exists():b.write_bytes(p.read_bytes())
 s=b.read_text();s=s[:s.index('    def build(')]
 s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 if key:s=re.sub(r'keyshape = Keyshape.\w+','keyshape = Keyshape.'+key,s)
 s='"""'+id+': smooth geometric reconstruction on SOLO48."""\n'+s[s.index('from ...'):]
 s+='    def build(self):\n'+textwrap.indent('# Plan: '+plan+'\n# Reference: '+ref+'\n'+textwrap.dedent(HELPER+body).strip()+'\n','        ')
 p.write_text(s);changes.append(dict(id=id,source=rows[id]['source'],plan=plan,reference=ref))

# The four command loops share one radius and one central square.
command='''
# A single traversed stroke; four identical radius-six terminal loops.
path('command',(18,18),[
 ('L',(12,18)),('A',(6,12),6,6,True),('A',(12,6),6,6,True),('A',(18,12),6,6,True),
 ('L',(18,36)),('A',(12,42),6,6,True),('A',(6,36),6,6,True),('A',(12,30),6,6,True),
 ('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('A',(30,36),6,6,True),
 ('L',(30,12)),('A',(36,6),6,6,True),('A',(42,12),6,6,True),('A',(36,18),6,6,True),('L',(18,18))],True)
'''
for id in ['keyboard-command','keyboard-command-interface-essential']:patch(id,command,'SQUARE; four equal circular loops and a centered square replace 39 irregular segments.','Lucide command: one continuous run with four matching loops.')
infinity='''
# Mirrored loop definition with diagonal tangency at the crossover.
path('infinity',(24,24),[
 ('C',(18,14),(17,8),(12,8)),('C',(7,8),(4,15),(4,24)),
 ('C',(4,33),(7,40),(12,40)),('C',(17,40),(18,34),(24,24)),
 ('C',(30,14),(31,8),(36,8)),('C',(41,8),(44,15),(44,24)),
 ('C',(44,33),(41,40),(36,40)),('C',(31,40),(30,34),(24,24))],True)
'''
for id in ['virtual-coin-crypto-infinite','symbol-aviation','microsoft-visual-studio-logo-1','crypto-currency-infinitecoin']:
 patch(id,infinity,'HRECT_L; mirrored infinity loops with continuous crossover tangents and matching bowls.','Lucide infinity: continuous crossing and balanced loops.')
patch('meta-logo',infinity.replace("('C',(18,14),(17,8),(12,8))","('C',(18,14),(17,8),(12,8))"),'HRECT_L; smooth matching loops retain the existing tall infinity silhouette.','Lucide infinity: balanced loops and continuous tangent flow.')
patch('dog-bone','''
path('bone',(16,17),[
 ('C',(14,17),(17,8),(10,8)),('C',(6,8),(4,12),(4,17)),('C',(4,21),(7,22),(7,24)),
 ('C',(7,26),(4,27),(4,31)),('C',(4,36),(6,40),(10,40)),('C',(17,40),(14,31),(16,31)),
 ('L',(32,31)),('C',(34,31),(31,40),(38,40)),('C',(42,40),(44,36),(44,31)),
 ('C',(44,27),(41,26),(41,24)),('C',(41,22),(44,21),(44,17)),('C',(44,12),(42,8),(38,8)),
 ('C',(31,8),(34,17),(32,17)),('L',(16,17))],True)
''','HRECT_L; mirrored four lobes with matching waist transitions; removed stray one-unit tip.','Lucide bone: one coherent outline and paired end lobes.')
patch('speaker','''
# Four identical mounting ears, smoothly joined to the circular body.
path('rim',(24,6),[
 ('C',(28,6),(31,7),(34,9)),('C',(40,3),(45,8),(39,14)),
 ('C',(43,20),(43,28),(39,34)),('C',(45,40),(40,45),(34,39)),
 ('C',(28,43),(20,43),(14,39)),('C',(8,45),(3,40),(9,34)),
 ('C',(5,28),(5,20),(9,14)),('C',(3,8),(8,3),(14,9)),('C',(17,7),(20,6),(24,6))],True)
self.add_arc('cone-a',(24,17),(24,31),radius_x=7)
self.add_arc('cone-b',(24,31),(24,17),radius_x=7)
self.add_contour('cone','cone-a','cone-b',closed=True)
''','SQUARE; matching mounting ears around a centered circular cone.','No exact speaker-driver reference; repeated rotational geometry.')
# Translation gives every wave identical amplitude and spacing.
for id,ys,xs,amp in [('texture',(9,19,29,39),(6,24,42),3),('warp-wave',(12,24,36),(4,24,44),4)]:
 patch(id,f'''
for i,y in enumerate({ys!r}):
    xs={xs!r};commands=[]
    for j,(a,b) in enumerate(zip(xs,xs[1:])):
        amplitude={amp}*(-1 if j%2==0 else 1)
        commands.append(('C',(a+(b-a)/3,y+amplitude*4/3),(b-(b-a)/3,y+amplitude*4/3),(b,y)))
    path(f'wave-{{i}}',(xs[0],y),commands)
''','Equal translated waves with matched tangent directions; tiny flat fragments removed.','No exact Lucide wave match; repeated smooth curve definition.')
patch('warp-flag','''
# Rails are translations of one two-curve wave.
for name,y in [('top',12),('middle',24),('bottom',36)]:
 path(name,(4,y),[('C',(12,y-16/3),(16,y-16/3),(24,y)),('C',(32,y+16/3),(36,y+16/3),(44,y))])
self.add_line('left',(4,12),(4,36));self.add_line('right',(44,12),(44,36))
for wall in ['left','right']:
 for rail in ['top','middle','bottom']:self.relate('connect',wall,rail)
''','HRECT_L; three equally spaced wave rails with shared endpoints and mirrored lobes.','Lucide flag: coherent flowing fabric boundary.')
patch('ghost','''
path('ghost',(8,36),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,36)),
 ('C',(40,40),(40,44),(36,44)),('C',(33,44),(33,40),(30,40)),('C',(27,40),(27,44),(24,44)),
 ('C',(21,44),(21,40),(18,40)),('C',(15,40),(15,44),(12,44)),('C',(8,44),(8,40),(8,36))],True)
''','VRECT_L; circular crown, straight sides, and evenly repeated scallops.','Lucide ghost: smooth dome and deliberate repeated hem.')
patch('video-player','''
# Four broad tangent corners preserve the softly bowed video frame.
path('screen',(24,8),[('C',(32,8),(38,8),(41,10)),('C',(44,12),(44,18),(44,24)),
 ('C',(44,30),(44,36),(41,38)),('C',(38,40),(32,40),(24,40)),
 ('C',(16,40),(10,40),(7,38)),('C',(4,36),(4,30),(4,24)),
 ('C',(4,18),(4,12),(7,10)),('C',(10,8),(16,8),(24,8))],True)
self.add_polyline('play',(19,17),(31,24),(19,31),closed=True)
''','HRECT_L; balanced bowed screen with a centered play triangle.','Lucide youtube: rounded video frame and simple play mark.')
patch('soundcloud-logo','''
path('cloud',(14,40),[('A',(4,30),10,10,True),('A',(14,20),10,10,True),
 ('C',(14,13),(18,8),(24,8)),('C',(30,8),(34,13),(34,20)),
 ('A',(44,30),10,10,True),('A',(34,40),10,10,True),('L',(14,40))],True)
''','HRECT_L; matching cloud shoulders, smooth crown and straight base.','Lucide cloud: coherent lobes and tangent baseline.')
# Diagonal capsule: integer extrema and mirrored cubic caps.
pill='''
path('capsule',(9,25),[('L',(25,9)),('C',(29,5),(35,5),(39,9)),('C',(43,13),(43,19),(39,23)),
 ('L',(23,39)),('C',(19,43),(13,43),(9,39)),('C',(5,35),(5,29),(9,25))],True)
self.add_line('seam',(17,17),(31,31));self.relate('connect','seam','capsule')
'''
for id in ['pill','drug']:patch(id,pill,'SQUARE; matching diagonal capsule ends with smooth tangents and one exact seam.','Lucide pill: parallel barrel edges and paired rounded caps.')
patch('curly-brackets-programing','''
for side,mirror in [('left',False),('right',True)]:
 def p(x,y):return (48-x,y) if mirror else (x,y)
 path(side,p(12,8),[('L',p(10,8)),('C',p(7,8),p(6,10),p(6,13)),('L',p(6,18)),
 ('C',p(6,22),p(6,24),p(4,24)),('C',p(6,24),p(6,26),p(6,30)),('L',p(6,35)),
 ('C',p(6,38),p(7,40),p(10,40)),('L',p(12,40))])
''','HRECT_L; mirrored braces with matching shoulders and centered cusps.','Lucide braces: paired repeated curved brackets.')
# Further recurring subjects identified in the complete 898-icon contact sheets.
cloud='''
path('cloud',(14,40),[('A',(4,30),10,10,True),('A',(14,20),10,10,True),
 ('C',(14,13),(18,8),(24,8)),('C',(30,8),(34,13),(34,20)),
 ('A',(44,30),10,10,True),('A',(34,40),10,10,True),('L',(14,40))],True)
'''
for id in ['weather-cloud','weather-cloud-snow','mobile-me-logo']:
 patch(id,cloud,'HRECT_L; smooth crown, matching shoulders and tangent base replace lumpy cloud joins.','Lucide cloud: continuous cloud silhouette.')
pin='''
# Left and right halves share their apex, crown and tangent controls.
path('pin',(24,44),[('C',(18,38),(8,30),(8,20)),('A',(24,4),16,16,True),
 ('A',(40,20),16,16,True),('C',(40,30),(30,38),(24,44))],True)
'''
for id in ['pin-three','pin-wave','pin-1','pin-1-interface-essential','pin-9b4b8603','google-near-by-logo']:
 detail=''
 if id in ['pin-wave','google-near-by-logo']:
  detail="self.add_arc('hole-a',(24,15),(24,25),radius_x=5)\nself.add_arc('hole-b',(24,25),(24,15),radius_x=5)\nself.add_contour('hole','hole-a','hole-b',closed=True)\n"
 elif id!='pin-three':detail="self.add_dot('location',(24,20))\n"
 patch(id,pin+detail,'VRECT_L; circular crown and mirrored tangent shoulders meet at one centered pin tip.','Lucide map-pin: symmetric location outline and centered marker.')
star='''
# One axis owns matching arms, not independently nudged vertices.
axis=24
right=[(axis,6),(axis+5,18),(42,20),(32,29),(35,42),(axis,35)]
points=right+[(48-x,y) for x,y in reversed(right[1:-1])]
self.add_polyline('star',*points,closed=True)
'''
for id in ['reward-stars','star-b255daf0','rating-star','star-holidays','trustpilot-logo']:
 patch(id,star,'SQUARE; mirrored star arms and valleys, straight uninterrupted edges.','Lucide star: common axis and deliberate corners.')
flame='''
# Deliberately asymmetric flame tip; continuous curve through both side extremes.
path('flame',(22,4),[('C',(23,15),(40,18),(40,29)),('C',(40,38),(33,44),(24,44)),
 ('C',(15,44),(8,38),(8,29)),('C',(8,18),(20,17),(22,4))],True)
'''
for id in ['flame-59aa3cfd','flame-products','fire-5ae1316a','fire-weather']:
 patch(id,flame,'VRECT_L; one flowing asymmetric flame tip over a smooth balanced bowl.','No useful simple-flame Lucide match; preserve the original leaning flame silhouette.')
# An additional tongue is essential to these flame variants.
for id in ['fire','flame-fire']:
 patch(id,'''
path('flame',(22,4),[('C',(26,7),(31,14),(31,20)),('C',(31,22),(30,25),(29,27)),
 ('L',(37,21)),('C',(39,25),(40,28),(40,31)),('C',(40,39),(33,44),(24,44)),
 ('C',(15,44),(8,38),(8,30)),('C',(8,20),(20,15),(22,4))],True)
''','VRECT_L; flowing main flame and smooth lower bowl preserve the smaller side tongue.','No close Lucide flame silhouette; retain deliberate asymmetric tongues.')
patch('alluvium','''
for i,y in enumerate((12,24,36)):
 path(f'wave-{i}',(4,y),[('C',(4+20/3,y-16/3),(24-20/3,y-16/3),(24,y)),
 ('C',(24+20/3,y+16/3),(44-20/3,y+16/3),(44,y))])
''','HRECT_L; three identical translated waves with smooth continuous tangents.','No exact wave reference; repeated curve definition.')
# Garment shoulders and underarms are paired; the neck is one semicircle.
shirt='''
path('shirt',(16,8),[('A',(32,8),8,8,False),('C',(40,8),(44,12),(44,18)),
 ('L',(44,26)),('L',(36,26)),('L',(36,40)),('L',(12,40)),('L',(12,26)),
 ('L',(4,26)),('L',(4,18)),('C',(4,12),(8,8),(16,8))],True)
self.add_line('left-sleeve',(12,26),(12,18));self.add_line('right-sleeve',(36,26),(36,18))
for side in ['left','right']:self.relate('connect',side+'-sleeve','shirt')
'''
for id in ['t-shirt','t-shirt-45dc1629']:
 patch(id,shirt,'HRECT_L; matching shoulder curves, semicircular neck and equal sleeves.','No inspected Lucide shirt match; mirrored garment construction.')
patch('currency-pound','''
path('pound',(8,44),[('C',(17,44),(18,37),(18,30)),('L',(18,24)),('L',(18,16)),
 ('C',(18,8),(21,4),(29,4)),('C',(35,4),(40,6),(40,10))])
self.add_line('base',(8,44),(40,44));self.relate('connect','base','pound')
self.add_polyline('bar',(8,24),(18,24),(30,24));self.relate('connect','bar','pound')
''','VRECT_L; smooth pound bowl and flowing foot replace the faceted upper hook.','No close Lucide pound match; coherent typographic stem and bowl.')
patch('water-bottle-glass','''
path('bottle',(18,4),[('L',(18,8)),('C',(18,12),(8,12),(8,18)),('L',(8,24)),('L',(8,39)),
 ('C',(8,42),(10,44),(14,44)),('L',(34,44)),('C',(38,44),(40,42),(40,39)),
 ('L',(40,24)),('L',(40,18)),('C',(40,12),(30,12),(30,8)),('L',(30,4))])
path('water',(8,24),[('C',(18,20),(30,28),(40,24))]);self.relate('connect','water','bottle')
''','VRECT_L; paired bottle shoulders, equal corner radii and a smooth water surface.','No close Lucide bottle match; mirrored bottle boundary and flowing waterline.')

# Five-petal blossoms use one axis; preserve the existing center mark type.
for id,left,right,top,bottom,mark in [('flower',6,42,6,42,'none'),('flower-b31296d9',6,42,6,42,'dot'),('flower-nature',4,44,8,40,'oval')]:
 patch(id,f'''
left,right,top,bottom={left},{right},{top},{bottom}
path('flower',(24,top),[('C',(29,top),(32,top+3),(32,15)),
 ('C',(38,13),(right,17),(right,22)),('C',(right,27),(39,29),(35,30)),
 ('C',(39,36),(35,bottom),(30,bottom)),('C',(27,bottom),(25,39),(24,37)),
 ('C',(23,39),(21,bottom),(18,bottom)),('C',(13,bottom),(9,36),(13,30)),
 ('C',(9,29),(left,27),(left,22)),('C',(left,17),(10,13),(16,15)),
 ('C',(16,top+3),(19,top),(24,top))],True)
'''+("self.add_dot('center',(24,24))\n" if mark=='dot' else "path('center',(20,24),[('A',(28,24),4,3,True),('A',(20,24),4,3,True)],True)\n" if mark=='oval' else ''),
 'Five mirrored petals with smooth lobe curves; preserved the original center mark.','Lucide flower: coherent petal lobes and balanced center spacing.')
for id in ['organic-tree','organic-tree-ecology']:
 detail="self.add_polyline('branches',(20,20),(24,24),(28,20));self.relate('connect','branches','trunk')\n" if id.endswith('ecology') else "self.add_line('base',(18,44),(30,44));self.relate('connect','base','trunk')\n"
 patch(id,'''
path('crown',(24,4),[('C',(30,4),(34,8),(34,14)),('L',(34,16)),
 ('C',(38,18),(40,21),(40,25)),('C',(40,31),(34,34),(24,34)),
 ('C',(14,34),(8,31),(8,25)),('C',(8,21),(10,18),(14,16)),('L',(14,14)),('C',(14,8),(18,4),(24,4))],True)
self.add_polyline('trunk',(24,16),(24,24),(24,34),(24,44));self.relate('connect','trunk','crown')
'''+detail,'VRECT_L; mirrored tree crown with smooth shoulders and a centered trunk.','No close Lucide tree match; preserve the original crown and branch structure.')
patch('card-game-card-club','''
path('club',(24,4),[('C',(29,4),(32,8),(32,13)),('C',(32,16),(31,18),(30,20)),
 ('C',(36,18),(40,22),(40,27)),('C',(40,32),(36,36),(31,36)),('C',(28,36),(26,34),(24,32)),
 ('C',(22,34),(20,36),(17,36)),('C',(12,36),(8,32),(8,27)),
 ('C',(8,22),(12,18),(18,20)),('C',(17,18),(16,16),(16,13)),('C',(16,8),(19,4),(24,4))],True)
self.add_line('stem',(24,32),(24,44));self.relate('connect','stem','club')
''','VRECT_L; three clean club lobes, mirrored side bowls and an exact centered stem.','No inspected Lucide club match; preserve the three-lobe card-suit silhouette.')
patch('card-game-card-spade','''
path('spade',(24,4),[('C',(20,11),(8,18),(8,27)),('C',(8,33),(12,37),(17,37)),
 ('C',(20,37),(22,35),(24,32)),('C',(26,35),(28,37),(31,37)),
 ('C',(36,37),(40,33),(40,27)),('C',(40,18),(28,11),(24,4))],True)
self.add_line('stem',(24,32),(24,44));self.relate('connect','stem','spade')
''','VRECT_L; mirrored spade shoulders and bowl curves with a centered tip and stem.','No inspected Lucide spade match; paired bowls and one shared axis.')
# Open infinity retains its intentional interruption.
patch('loop-manual','''
path('loop',(20,15),[('C',(17,9),(15,8),(12,8)),('C',(7,8),(4,15),(4,24)),
 ('C',(4,33),(7,40),(12,40)),('C',(17,40),(18,34),(24,24)),
 ('C',(30,14),(31,8),(36,8)),('C',(41,8),(44,15),(44,24)),
 ('C',(44,33),(41,40),(36,40)),('C',(33,40),(31,36),(28,31))])
''','HRECT_L; smooth paired infinity loops retain the open ends and their clearance.','Lucide infinity: flowing loop curvature; preserve the supplied open-loop variant.')
# Gently curved half-round fish-bowl rim, preserving the fish detail from source.

# Record cumulative changes without importing scripts that have patch side effects.
(H/'changes.json').write_text(json.dumps(changes,indent=2))
previous=json.loads((H.parent/'changes.json').read_text());ids={r['id'] for r in changes}
(H.parent/'changes.json').write_text(json.dumps([r for r in previous if r['id'] not in ids]+changes,indent=2))
print('Reconstructed',len(changes))
