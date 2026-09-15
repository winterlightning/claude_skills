"""Geometric repairs for individually reviewed members of the fixed cohort."""
from repair import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
main()

def body(id):
 s=Path(byid[id]['python_source']['path']).read_text();return textwrap.dedent(s[s.index('    def build(self):')+len('    def build(self):'):]).strip()
def save(): (HERE/'changes.json').write_text(json.dumps(list({r['id']:r for r in changes}.values()),indent=2))
box='''
def box(name,l,t,r,b,corner):
    points=[(l+corner,t),(r-corner,t),(r,t+corner),(r,b-corner),(r-corner,b),(l+corner,b),(l,b-corner),(l,t+corner)]
    members=[]
    for i,a in enumerate(points):
        z=points[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
        if i%2:self.add_arc(eid,a,z,radius_x=corner)
        else:self.add_line(eid,a,z)
    self.add_contour(name,*members,closed=True)
'''
circle='''
def circle(name,cx,cy,r):
    self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    self.add_contour(name,name+'-top',name+'-bottom',closed=True)
'''
# Finish the K without crowding its frame.
p=Path(byid['amazon-elastic-kubernetes-service']['python_source']['path']);s=p.read_text().replace("(29,16),(20,24),(29,32)","(28,17),(20,24),(28,31)");p.write_text(s)
patch('acrobatic-hanging','''
self.add_line('rope',(24,4),(24,14))
self.add_arc('ring-upper-left',(8,29),(24,14),radius_x=16,radius_y=15)
self.add_arc('ring-upper-right',(24,14),(40,29),radius_x=16,radius_y=15)
self.add_arc('ring-lower',(40,29),(8,29),radius_x=16,radius_y=15)
self.add_contour('ring','ring-upper-left','ring-upper-right','ring-lower',closed=True)
self.relate('connect','rope','ring')
''','VRECT_L; split the oval at its exact rope attachment, eliminating the interior tip.','Geometric ellipse; no useful Lucide subject match.')
patch('amazon-web-service-app-mesh',circle+'''
circle('hub',24,27,5)
for name,cx,cy in [('top',24,9),('left',9,39),('right',39,39)]:circle(name,cx,cy,3)
self.add_line('top-link',(24,12),(24,22))
# Integer 3-4-5 contact points on the hub; smooth curves land on outer-node apices.
self.add_bezier('left-link',(20,30),((16,33),(12,34),(9,36)))
self.add_bezier('right-link',(28,30),((32,33),(36,34),(39,36)))
for name in ['top','left','right']:
    self.relate('connect',name+'-link',name)
    self.relate('connect',name+'-link','hub')
''','SQUARE; symmetric links terminate on node circles; remove the tiny top-link arc.','Geometric node circles and shared contacts; no exact Lucide brand match.')
patch('controls-rewind-video',"self.add_polyline('triangle',(40,4),(8,24),(40,44),closed=True)",'VRECT_L; three clean sides and exact horizontal symmetry.','Lucide pencil: deliberate straight edges; simple geometric triangle.')
drop='''
axis = 24
self.add_bezier('left',(axis,4),((19,11),(8,22),(8,28)))
self.add_arc('bowl',(8,28),(40,28),radius_x=16,sweep=False)
self.add_bezier('right',(40,28),((40,22),(29,11),(axis,4)))
self.add_contour('outline','left','bowl','right',closed=True)
'''
for id in ['dew','drop','drop-b2007152','fat-liquid-drop','oil','water-protection-drop']:
 patch(id,drop,'VRECT_L; mirrored shoulders meet a circular bowl with vertical tangents.','Lucide droplet: a coherent pointed crest and round bowl.')
shield='''
self.add_bezier('upper-left',(24,4),((19,7),(14,9),(8,10)))
self.add_line('left-wall',(8,10),(8,20))
self.add_bezier('left-base',(8,20),((8,31),(15,40),(24,44)))
self.add_bezier('right-base',(24,44),((33,40),(40,31),(40,20)))
self.add_line('right-wall',(40,20),(40,10))
self.add_bezier('upper-right',(40,10),((34,9),(29,7),(24,4)))
self.add_contour('outline','upper-left','left-wall','left-base','right-base','right-wall','upper-right',closed=True)
'''
patch('defense-shield-ability',shield,'VRECT_L; mirrored shield shoulders, tangent vertical walls and curved base.','Lucide shield: symmetric protective silhouette.')
patch('shield-ee28756e',shield.replace("((19,7),(14,9),(8,10))","((19,4),(14,6),(8,8))").replace("((34,9),(29,7),(24,4))","((34,6),(29,4),(24,4))").replace('(8,10)','(8,8)').replace('(40,10)','(40,8)'), 'VRECT_L; smooth crowned top, mirrored lower bowl.','Lucide shield: matched sides and coherent curves.')
# A smooth symmetric eye lens; retain each icon's original inner feature.
eye='''
self.add_bezier('upper',(4,24),((9,15),(15,8),(24,8)),((33,8),(39,15),(44,24)))
self.add_bezier('lower',(44,24),((39,33),(33,40),(24,40)),((15,40),(9,33),(4,24)))
self.add_contour('outline','upper','lower',closed=True)
'''
for id in ['eye-1','eye-1-container','eye-1-state']:
 patch(id,eye+("\nself.add_dot('pupil',(24,24))" if id=='eye-1-state' else ''),'HRECT_L; four mirrored curves and balanced lens negative space.','Geometric lens; no pupil added to outline-only source.')
# Full oval mirror with exact shared division positions from Panoramic.
patch('horizontal',body('panoramic').split('for i,x in enumerate(panel_x):')[0], 'HRECT_L; opposed bowed rails are exact reflections.','Shared parabola construction, as in Panoramic.')
heart='''
axis = 24
self.add_bezier('left-inner',(axis,13),((21,10),(18,8),(14,8)))
self.add_arc('left-lobe',(14,8),(4,18),radius_x=10,sweep=False)
self.add_bezier('left-lower',(4,18),((4,23),(7,25),(10,28)))
self.add_line('left-point',(10,28),(axis,40))
self.add_line('right-point',(axis,40),(38,28))
self.add_bezier('right-lower',(38,28),((41,25),(44,23),(44,18)))
self.add_arc('right-lobe',(44,18),(34,8),radius_x=10,sweep=False)
self.add_bezier('right-inner',(34,8),((30,8),(27,10),(axis,13)))
self.add_contour('outline','left-inner','left-lobe','left-lower','left-point','right-point','right-lower','right-lobe','right-inner',closed=True)
'''
for id in ['heart-0104273d','heart-romance','hearts-card','heart-check']:
 extra="\nself.add_polyline('check',(16,22),(22,28),(32,18))" if id=='heart-check' else ''
 patch(id,heart+extra,'HRECT_L; paired circular lobes and mirrored point; remove conversion kinks.','Lucide heart: rounded lobes flow into deliberate pointed base.')
patch('specialty-heart','''
self.add_bezier('left-lobe',(24,12),((20,8),(17,6),(14,6)),((9,6),(6,11),(6,17)))
self.add_bezier('left-side',(6,17),((6,26),(17,36),(24,42)))
self.add_bezier('right-side',(24,42),((31,36),(42,26),(42,17)))
self.add_bezier('right-lobe',(42,17),((42,11),(39,6),(34,6)),((31,6),(28,8),(24,12)))
self.add_contour('outline','left-lobe','left-side','right-side','right-lobe',closed=True)
''','SQUARE; preserve tall heart proportions with mirrored smooth lobes.','Lucide heart: shared lobe construction.')
# Match smooth pen cap while retaining the two icons' separate nib seam.
pen=body('pen-4d7410cc')+"\nself.add_line('nib-seam',(12,28),(20,36))\nself.relate('connect','nib-seam','outline')\n"
for id in ['pen-50e47373','pen-7927e987']:
 patch(id,pen,'SQUARE; diagonal symmetry, smooth rounded cap, parallel barrel, shared nib seam.','Lucide pencil: cap flow and exact seam contacts.')
patch('embassy','''
self.add_arc('dome',(7,24),(41,24),radius_x=17,radius_y=16)
self.add_line('lintel',(41,24),(7,24))
self.add_contour('roof','dome','lintel',closed=True)
self.add_line('base',(4,40),(44,40))
for i,x in enumerate((9,19,29,39)):
    self.add_line(f'column-{i}',(x,24),(x,40))
    self.relate('connect',f'column-{i}','roof')
    self.relate('connect',f'column-{i}','base')
''','HRECT_L; one symmetric elliptical dome and four equally spaced columns.','Geometric arch; no close embassy match.')
patch('monument','''
self.add_line('base',(6,42),(42,42))
self.add_bezier('right-base',(42,42),((41,35),(39,29),(35,29)))
self.add_line('ledge',(35,29),(13,29))
self.add_bezier('left-base',(13,29),((9,29),(7,35),(6,42)))
self.add_contour('pedestal','base','right-base','ledge','left-base',closed=True)
self.add_line('left-wall',(13,29),(13,23))
self.add_arc('dome-left',(13,23),(24,12),radius_x=11)
self.add_arc('dome-right',(24,12),(35,23),radius_x=11)
self.add_line('right-wall',(35,23),(35,29))
self.add_contour('dome','left-wall','dome-left','dome-right','right-wall')
self.add_line('finial',(24,6),(24,12))
self.relate('connect','dome','pedestal')
self.relate('connect','finial','dome')
''','SQUARE; circular dome centered on a mirrored base; exact finial contact.','Geometric dome and shared axis.')
patch('mushroom-portobello','''
self.add_arc('cap',(4,26),(44,26),radius_x=20,radius_y=18)
self.add_bezier('underside-right',(44,26),((39,26),(35,24),(30,24)))
self.add_line('underside-middle',(30,24),(18,24))
self.add_bezier('underside-left',(18,24),((13,24),(9,26),(4,26)))
self.add_contour('cap-outline','cap','underside-right','underside-middle','underside-left',closed=True)
self.add_bezier('stem',(18,24),((17,32),(18,40),(24,40)),((30,40),(31,32),(30,24)))
self.relate('connect','stem','cap-outline')
''','HRECT_L; symmetric elliptical cap and smoothly mirrored stem.','Geometric dome; retain the source mushroom silhouette.')
patch('led-light','''
self.add_line('left-wall',(10,28),(10,18))
self.add_arc('dome',(10,18),(38,18),radius_x=14)
self.add_line('right-wall',(38,18),(38,28))
self.add_contour('housing','left-wall','dome','right-wall')
self.add_line('flange',(8,28),(40,28))
self.relate('connect','housing','flange')
for name,x in [('left',17),('right',31)]:
    self.add_line(name+'-lead',(x,28),(x,44))
    self.relate('connect',name+'-lead','flange')
self.add_polyline('filament',(20,18),(24,20),(28,18))
self.add_line('filament-stem',(24,20),(24,28))
self.relate('connect','filament-stem','filament')
self.relate('connect','filament-stem','flange')
''','VRECT_L; one semicircular dome, paired leads, and shared filament junction.','Geometric capsule construction.')
patch('ice-cream-stick-1','''
self.add_arc('top',(8,18),(40,18),radius_x=16,radius_y=14)
self.add_polyline('body',(40,18),(40,32),(8,32),(8,18))
self.add_contour('outline','top','body-1','body-2','body-3',closed=True)
self.contours.pop(0)
self.add_line('seam',(8,18),(40,18))
self.add_line('stick',(24,32),(24,44))
self.relate('connect','seam','outline')
self.relate('connect','stick','outline')
''','VRECT_L; symmetric elliptical crest and centered stick.','Geometric half ellipse; retain source seam.')
# Mirror clean U-turns rather than patch individual radius fragments.
patch('u-turn-left','''
self.add_line('right',(42,42),(42,20))
self.add_arc('turn',(42,20),(14,20),radius_x=14,sweep=False)
self.add_line('left',(14,20),(14,34))
self.add_contour('run','right','turn','left')
self.add_polyline('head',(6,26),(14,34),(22,26))
self.relate('connect','run','head')
''','SQUARE; one circular turn with vertical tangents and equal arrowhead arms.','Lucide undo-2: continuous bend and clean head.')
patch('u-turn-arrow','''
self.add_line('left',(8,44),(8,16))
self.add_arc('turn',(8,16),(32,16),radius_x=12)
self.add_line('right',(32,16),(32,38))
self.add_contour('run','left','turn','right')
self.add_polyline('head',(24,30),(32,38),(40,30))
self.relate('connect','run','head')
''','VRECT_L; one semicircle joins parallel legs; equal arrowhead arms.','Lucide undo-2: tangent circle-to-line construction.')
for id in ['unlock','unlock-90a6ff07']:
 patch(id,box+'''
box('body',8,22,40,44,4)
self.add_line('shackle-side',(14,22),(14,14))
self.add_arc('shackle-arch',(14,14),(34,14),radius_x=10)
self.add_contour('shackle','shackle-side','shackle-arch')
self.relate('connect','shackle','body')
''','VRECT_L; equal body corners and one circular open shackle.','Geometric rounded box and tangent arch.')
patch('unlock-symbol',box+'''
box('body',16,22,40,44,4)
self.add_line('shackle-left',(8,18),(8,14))
self.add_arc('shackle-top',(8,14),(28,14),radius_x=10)
self.add_line('shackle-right',(28,14),(28,22))
self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
self.relate('connect','shackle','body')
''','VRECT_L; coherent open circular shackle and equal corner radii.','Geometric rounded box and tangent arch.')
# Exact wave mirrors; remove duplicate degenerate curves at the center.
for id,mirror in [('wave-backward',False),('wave-backward-interface-essential',False),('wave-forward',True)]:
 patch(id,f'mirror = {mirror}\n'+'''
def p(x,y):return (48-x,y) if mirror else (x,y)
self.add_bezier('outer',p(22,4),(p(14,9),p(8,16),p(8,24)),(p(8,32),p(14,39),p(22,44)))
self.add_bezier('inner',p(40,10),(p(34,14),p(30,19),p(30,24)),(p(30,29),p(34,34),p(40,38)))
''','VRECT_L; each wave is a single smooth run mirrored about its horizontal axis.','Geometric mirrored cubic wave construction.')
# The existing centerline envelope determines each crown; mirrored cubics own both halves.
wavehelper='''
def crown(name,left,edge_y,top):
    right=48-left;half=(right-left)/2
    self.add_bezier(name,(left,edge_y),((left+half*.35,edge_y-(edge_y-top)*.7),(24-half*.4,top),(24,top)),((24+half*.4,top),(right-half*.35,edge_y-(edge_y-top)*.7),(right,edge_y)))
'''
for id in ['wifi','wifi-f683dd0c']:
 patch(id,wavehelper+"\ncrown('outer',4,17,8)\ncrown('inner',14,27,23)\nself.add_dot('signal',(24,40))",'HRECT_L; mirror each crest from one shared definition, retaining two bands.','Geometric repeated arcs with shared symmetry.')
patch('wifi-networks',wavehelper+"\ncrown('outer',4,16,8)\ncrown('middle',10,24,18)\ncrown('inner',17,31,28)\nself.add_dot('signal',(24,40))",'HRECT_L; three coherent mirrored crests with evenly separated apices.','Geometric repeated arcs with shared symmetry.')
patch('smart',wavehelper+"\ncrown('outer',4,19,8)\ncrown('middle',10,30,23)\ncrown('inner',18,40,37)",'HRECT_L; three mirrored crowns, no tiny cusp at the outer apex.','Geometric repeated crests.')
patch('rss-logo','''
for name,r in [('outer',36),('middle',23),('inner',10)]:
    self.add_arc(name,(6,42-r),(6+r,42),radius_x=r)
''','SQUARE; three concentric quarter circles with shared origin and uniform spacing.','Geometric concentric arcs.')
patch('wine-glass','''
self.add_line('rim',(11,4),(37,4))
self.add_bezier('right-wall',(37,4),((38,8),(40,12),(40,17)))
self.add_arc('bowl-right',(40,17),(24,29),radius_x=16,radius_y=12)
self.add_arc('bowl-left',(24,29),(8,17),radius_x=16,radius_y=12)
self.add_bezier('left-wall',(8,17),((8,12),(10,8),(11,4)))
self.add_contour('bowl','rim','right-wall','bowl-right','bowl-left','left-wall',closed=True)
self.add_line('stem',(24,29),(24,44))
self.add_line('foot',(13,44),(35,44))
self.relate('connect','stem','bowl')
self.relate('connect','stem','foot')
''','VRECT_L; mirrored bowl, exact shared stem attachment and centered foot.','Geometric ellipse-to-wall tangency.')
patch('fragile-break','''
self.add_polyline('right-rim',(25,4),(37,4))
self.add_bezier('right-wall',(37,4),((38,8),(40,12),(40,17)))
self.add_arc('bowl-right',(40,17),(24,29),radius_x=16,radius_y=12)
self.add_arc('bowl-left',(24,29),(8,17),radius_x=16,radius_y=12)
self.add_bezier('left-wall',(8,17),((8,12),(10,8),(11,4)))
self.add_polyline('crack',(11,4),(19,4),(17,9),(23,13),(18,16))
self.add_contour('bowl','right-rim-1','right-wall','bowl-right','bowl-left','left-wall','crack-1','crack-2','crack-3','crack-4')
self.contours=self.contours[2:]
self.add_line('stem',(24,29),(24,44))
self.add_line('foot',(16,44),(32,44))
self.relate('connect','stem','bowl')
self.relate('connect','stem','foot')
''','VRECT_L; symmetric bowl and centered stem; retain the intentional crack.','Geometric wine bowl with a deliberate broken rim.')
save()
