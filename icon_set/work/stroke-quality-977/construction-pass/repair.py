"""Explicit per-symbol repair of the stroke graph; keep source identity."""
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
        if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
        elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
        elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
        previous=cmd[-1] if cmd[0]=='C' else cmd[1]
    self.add_contour(name,*members,closed=closed)
def oval(name,cx,cy,rx,ry=None):
    ry=rx if ry is None else ry
    path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
'''
def patch(id,body,plan,reference='No close Lucide match; reconstruct the supplied subject from its owning geometry.',key=None):
 p=ROOT/rows[id]['source'];s=(H/'before'/p.name).read_text();s=s[:s.index('    def build(')]
 s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 if key:s=re.sub(r'keyshape = Keyshape.\w+','keyshape = Keyshape.'+key,s)
 s='"""'+id+': reconstructed stroke graph on SOLO48."""\n'+s[s.index('from ...'):]
 s+='    def build(self):\n'+textwrap.indent('# Plan: '+plan+'\n# Reference: '+reference+'\n'+textwrap.dedent(HELPER+body).strip()+'\n','        ')
 p.write_text(s);changes.append(dict(id=id,source=rows[id]['source'],plan=plan,reference=reference))

dollar='''
path('s',(38,14),[('C',(36,10),(30,8),(24,8)),('C',(15,8),(8,10),(8,16)),
 ('C',(8,22),(16,23),(24,24)),('C',(32,25),(40,26),(40,32)),
 ('C',(40,38),(33,40),(24,40)),('C',(18,40),(12,38),(10,34))])
self.add_polyline('stem',(24,4),(24,8),(24,24),(24,40),(24,44));self.relate('connect','stem','s')
'''
for id in ['dollar-sign','dollar']:
 patch(id,dollar,'VRECT_L; one tangent-continuous S, paired bowls, exact intersections at three shared stem nodes.','Lucide dollar-sign: coherent bowl and stem geometry.')
patch('side-road-angle-right-transportation','''
self.add_polyline('road',(18,4),(18,20),(18,44))
self.add_polyline('arrowhead',(8,9),(18,4),(28,9))
self.add_line('branch',(18,20),(40,34))
self.relate('connect','road','arrowhead');self.relate('connect','road','branch')
''','VRECT_L; equal arrowhead arms, one straight stem and exact branch node; duplicate arc removed.','Lucide signpost: shared attachment node and uninterrupted straight stem.')
patch('unity-logo','''
# Both right corners derive from reflection about y=24.
self.add_polyline('left-tip',(16,16),(4,24),(16,32))
self.add_polyline('top-tip',(26,12),(40,8),(44,20))
self.add_polyline('bottom-tip',(26,36),(40,40),(44,28))
self.add_polyline('spokes',(40,8),(29,24),(40,40))
self.add_line('left-spoke',(4,24),(29,24))
for tip in ['top-tip','bottom-tip']:self.relate('connect',tip,'spokes')
self.relate('connect','left-spoke','spokes');self.relate('connect','left-spoke','left-tip')
''','HRECT_L; symmetric upper/lower facets, straight sides and shared central spoke node; kinked two-piece side removed.')
patch('angry-face-symbol','''
# Detached expression only: no head/body proportions to alter.
self.add_line('brow-left',(6,6),(18,13));self.add_line('brow-right',(42,6),(30,13))
self.add_line('eye-left',(9,18),(12,20));self.add_line('eye-right',(39,18),(36,20))
path('frown',(8,42),[('C',(11,33),(12,26),(24,26)),('C',(36,26),(37,33),(40,42))])
''','SQUARE; each eye is drawn once; mirrored brows and a smooth continuous frown replace retraced eyes and kinked mouth joins.','Shared human_ref/user.svg: simple clean facial vocabulary; this icon has no head/body pair.')
patch('trash-symbol','''
# One mirrored bucket, one lid, one radius-four handle.
self.add_polyline('bucket',(12,14),(16,44),(32,44),(36,14))
self.add_polyline('lid',(8,14),(12,14),(18,14),(30,14),(36,14),(40,14))
path('handle',(18,14),[('L',(18,8)),('A',(22,4),4,4,True),('L',(26,4)),('A',(30,8),4,4,True),('L',(30,14))])
self.relate('connect','bucket','lid');self.relate('connect','handle','lid')
''','VRECT_L; equal bucket slopes and a tangent rounded handle attached exactly to a straight lid.','Lucide trash-2: shared lid/handle nodes and matched corner radii.')
patch('virtual-coin-crypto-theta','''
path('frame',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),
 ('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
for name,y,tip in [('upper',18,13),('lower',30,35)]:
 self.add_polyline(name,(18,y),(24,y),(30,y));self.add_line(name+'-stem',(24,y),(24,tip));self.relate('connect',name,name+'-stem')
''','VRECT_L; four identical tangent corners; equal bars and mirrored central stems replace mismatched chamfers and arm lengths.')
patch('slider','''
# Every rail stops exactly at its own circular knob's extreme.
for i,cx,y in [(0,16,13),(1,32,27)]:
 oval(f'knob-{i}',cx,y,5)
 self.add_line(f'left-{i}',(4,y),(cx-5,y));self.add_line(f'right-{i}',(cx+5,y),(44,y))
 self.relate('connect',f'left-{i}',f'knob-{i}');self.relate('connect',f'right-{i}',f'knob-{i}')
self.add_line('base',(4,40),(44,40))
''','HRECT_L; identical round knobs and rails ending exactly on their boundaries; removed one-unit intrusions.','Lucide sliders-horizontal: a common rail definition and exact knob placement.')
patch('flow','''
# Three equal nodes and a smooth return path with exact circle contacts.
for name,cx,cy in [('start',9,13),('top',27,13),('bottom',27,35)]:oval(name,cx,cy,5)
self.add_line('forward',(14,13),(22,13));self.relate('connect','forward','start');self.relate('connect','forward','top')
path('return',(32,13),[('C',(39,13),(44,17),(44,24)),('C',(44,31),(39,35),(32,35))])
self.relate('connect','return','top');self.relate('connect','return','bottom')
self.add_line('back',(22,35),(8,35));self.add_polyline('arrowhead',(13,30),(8,35),(13,40))
self.relate('connect','back','bottom');self.relate('connect','back','arrowhead')
''','HRECT_L; three equal circular nodes, tangent return bend and exact boundary contacts; stray tip and inward hooks removed.','Lucide git-compare-arrows: clean circular nodes and coherent connector runs.')
patch('crossed-arrow','''
# Mirrored hollow arrowheads, centered shafts, and paired circular tails.
self.add_polyline('head-left',(6,6),(20,8),(8,20),closed=True)
self.add_polyline('head-right',(42,6),(28,8),(40,20),closed=True)
self.add_polyline('shaft-left',(14,14),(24,24),(34,34))
self.add_polyline('shaft-right',(34,14),(24,24),(14,34))
self.relate('connect','head-left','shaft-left');self.relate('connect','head-right','shaft-right');self.relate('connect','shaft-left','shaft-right')
path('tail-left',(6,36),[('C',(6,32),(10,30),(14,34)),('C',(18,38),(16,42),(12,42))])
path('tail-right',(42,36),[('C',(42,32),(38,30),(34,34)),('C',(30,38),(32,42),(36,42))])
self.relate('connect','tail-left','shaft-right');self.relate('connect','tail-right','shaft-left')
''','SQUARE; matching arrowheads with centered shafts and mirrored smooth tail curls; no broken arc/line tail.','Lucide move-up-right: straight arrow direction and shared attachment points.')
patch('fragmented-brain','''
# Preserve the supplied oblique fragmented silhouette, but keep facets coherent.
path('outline',(8,20),[('C',(12,12),(22,8),(30,8)),('C',(34,8),(35,9),(38,12)),('C',(41,15),(44,14),(44,18)),
 ('C',(44,22),(40,25),(36,27)),('L',(12,39)),('C',(10,40),(9,40),(8,40)),('C',(5,40),(4,38),(4,34)),('C',(4,29),(5,25),(8,20))],True)
self.add_polyline('facet-cross',(8,20),(26,23),(36,27))
self.add_polyline('facet-spine',(12,39),(26,23),(38,12))
self.relate('connect','facet-cross','facet-spine');self.relate('connect','facet-cross','outline');self.relate('connect','facet-spine','outline')
''','HRECT_L; coherent oblique outline and shared facet intersections replace jagged perimeter fragments.','Human reference vocabulary inspected; supplied symbol is an abstract fragmented form, not an anatomical brain silhouette.')
# Related controller definitions: correct every rail/knob attachment.
for id,knobs,xlo,xhi in [('filter-setting-three-controller',[(32,11),(17,24),(32,37)],6,42),('filter-setting-two-controller',[(17,13),(32,35)],4,44)]:
 patch(id,f'''
for i,(cx,cy) in enumerate({knobs!r}):
 oval(f'knob-{{i}}',cx,cy,5)
 self.add_line(f'left-{{i}}',({xlo},cy),(cx-5,cy));self.add_line(f'right-{{i}}',(cx+5,cy),({xhi},cy))
 self.relate('connect',f'left-{{i}}',f'knob-{{i}}');self.relate('connect',f'right-{{i}}',f'knob-{{i}}')
''','Shared circular knobs with exact rail endpoints; no intrusions or misaligned one-unit caps.','Lucide sliders-horizontal: one owning definition for each rail and knob.')
patch('graph-finance','''
self.add_polyline('baseline',(4,40),(10,40),(24,40),(38,40),(44,40))
for i,x,top in [(0,10,8),(1,24,17),(2,38,22)]:
 self.add_line(f'bar-{i}',(x,top),(x,40));self.relate('connect',f'bar-{i}','baseline')
''','HRECT_L; three bars with exact baseline nodes; removed duplicate foot segment.')
patch('sound-interface-essential','''
for i,x,y0,y1 in [(0,6,17,31),(1,18,6,42),(2,30,13,35),(3,42,22,26)]:self.add_line(f'level-{i}',(x,y0),(x,y1))
''','SQUARE; equally spaced level bars, one stroke per bar; removed retraced first four units.')
patch('expand-horizontal-left-right','''
for side,x,tip,inner in [('left',20,4,9),('right',28,44,39)]:
 self.add_polyline(side+'-wall',(x,8),(x,24),(x,40))
 self.add_line(side+'-shaft',(x,24),(tip,24))
 self.add_polyline(side+'-head',(inner,19),(tip,24),(inner,29))
 self.relate('connect',side+'-shaft',side+'-wall');self.relate('connect',side+'-shaft',side+'-head')
''','HRECT_L; equal centered walls and arrowheads; duplicated one-unit arcs replaced by a straight shared stem node.')
smile='''
oval('face',24,24,20)
for name,cx in [('left',16),('right',32)]:
 path(name+'-eye',(cx-3,20),[('A',(cx+3,20),3,3,True)])
path('smile',(14,29),[('C',(16,33),(20,35),(24,35)),('C',(28,35),(32,33),(34,29))])
'''
for id in ['happy','happy-smileys','smile-fd6ce47d','smile-smileys','smile-867b755e','smile-e10e2f0e','blushing']:
 patch(id,smile,'CIRCLE; identical smooth closed-eye arches and one symmetric smile; remove tiny loops, retraced cubics and asymmetric eye ends.','Shared human_ref/user.svg: circular head vocabulary; supplied expression has no body.')
patch('workflow-merge','''
for name,cx,cy in [('top',13,9),('bottom',13,39),('branch',35,26)]:oval(name,cx,cy,5)
self.add_polyline('stem',(13,14),(13,26),(13,34));self.add_line('branch-rail',(13,26),(30,26))
self.relate('connect','stem','top');self.relate('connect','stem','bottom');self.relate('connect','branch-rail','stem');self.relate('connect','branch-rail','branch')
''','VRECT_L; three equal circular nodes with connector ends precisely at circle extremes; no one-unit pseudo-arc.','Lucide git-compare-arrows: exact node-boundary contacts.')
patch('database-connect','''
# Radius-five circles have exact integer 3:4 attachment points.
for i,flipx,flipy in [(0,False,False),(1,True,False),(2,False,True),(3,True,True)]:
 def p(x,y):return (48-x if flipx else x,48-y if flipy else y)
 sweep=not (flipx ^ flipy)
 commands=[('A',p(x,y),5,5,sweep) for x,y in [(14,15),(11,16),(6,11),(11,6),(16,11)]]
 path(f'node-{i}',p(16,11),commands,True)
 self.add_line(f'spoke-{i}',p(14,15),(24,24));self.relate('connect',f'spoke-{i}',f'node-{i}')
for a in range(4):
 for b in range(a):self.relate('connect',f'spoke-{a}',f'spoke-{b}')
''','SQUARE; four identical circles with exact Pythagorean boundary attachments, matched spokes, and no inward hooks.','Lucide node construction principles; original four-node network retained.')
for id in ['truck-3','truck-3-transportation']:
 patch(id,'''
for name,cx in [('front',13),('back',35)]:oval(name,cx,35,5)
path('cab',(8,35),[('L',(7,35)),('A',(4,32),3,3,True),('L',(4,23)),('C',(4,18),(7,14),(12,14)),('L',(20,14))])
path('cargo',(20,21),[('L',(20,14)),('L',(20,8)),('L',(44,8)),('L',(44,32)),('A',(41,35),3,3,True),('L',(40,35))])
self.add_polyline('chassis',(18,35),(20,35),(30,35))
self.relate('connect','cab','cargo');self.relate('connect','cab','front');self.relate('connect','cargo','back')
self.relate('connect','chassis','front');self.relate('connect','chassis','back')
''','HRECT_L; equal round wheels with chassis rails stopping exactly at their extremes; a tangent cab corner and shared cargo seam.','No exact inspected Lucide truck match; matched wheel definition and exact axle-height contacts.')
patch('minibus-symbol','''
for name,cx in [('front',13),('back',35)]:oval(name,cx,35,5)
path('body',(8,35),[('L',(7,35)),('A',(4,32),3,3,True),('L',(4,20)),('L',(10,8)),
 ('L',(40,8)),('A',(44,12),4,4,True),('L',(44,20)),('L',(44,32)),('A',(41,35),3,3,True),('L',(40,35))])
self.add_line('window',(4,20),(44,20));self.relate('connect','window','body')
self.add_line('chassis',(18,35),(30,35))
for name in ['front','back']:self.relate('connect','chassis',name);self.relate('connect','body',name)
''','HRECT_L; equal circular wheels, exact chassis contacts, clean body corners and a shared straight window rail.')

def save():
 (H/'changes.json').write_text(json.dumps(changes,indent=2))
 previous=json.loads((H.parent/'changes.json').read_text());ids={r['id'] for r in changes}
 (H.parent/'changes.json').write_text(json.dumps([r for r in previous if r['id'] not in ids]+changes,indent=2))
 print('Reconstructed',len(changes))
save()
