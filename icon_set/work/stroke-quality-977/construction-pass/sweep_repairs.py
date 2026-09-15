from pathlib import Path
exec(Path(__file__).with_name('final_junctions.py').read_text().split("patch('workflow-exit-door'")[0])
HELPER+='''
def rounded(name,x1,y1,x2,y2,r):
    path(name,(x1+r,y1),[('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True),('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True),('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True),('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)],True)
'''
for id in ['underwear-bra','underwear-bra-clothes']:
 patch(id,'''
self.add_line('left-strap',(8,8),(8,21));self.add_line('right-strap',(40,8),(40,21))
path('left-cup',(8,21),[('C',(13,23),(21,26),(22,34)),('C',(23,38),(18,40),(14,40)),('C',(8,40),(4,36),(4,30)),('C',(4,26),(6,23),(8,21))],True)
path('right-cup',(40,21),[('C',(35,23),(27,26),(26,34)),('C',(25,38),(30,40),(34,40)),('C',(40,40),(44,36),(44,30)),('C',(44,26),(42,23),(40,21))],True)
self.add_line('bridge',(22,34),(26,34))
for side in ['left','right']:
 self.relate('connect',side+'-strap',side+'-cup');self.relate('connect','bridge',side+'-cup')
''','HRECT_L; mirrored cups, straight equal straps and a shared center bridge replace uneven fitted curvature.')
for id in ['bracket-code','curly-brackets-programing']:
 patch(id,'''
for side in ['left','right']:
 def p(x,y):return (x,y) if side=='left' else (48-x,y)
 path(side,p(15,8),[('C',p(5,8),p(11,20),p(4,24)),('C',p(11,28),p(5,40),p(15,40))])
''','HRECT_L; two smooth cubic sweeps per brace, reflected across both axes; jagged multi-arc bends removed.')
patch('gas-pollution-mask','''
path('head',(8,24),[('C',(8,13),(14,4),(24,4)),('C',(34,4),(40,13),(40,24)),('C',(40,28),(40,31),(38,34)),('C',(34,40),(30,44),(24,44)),('C',(18,44),(14,40),(10,34)),('C',(8,31),(8,28),(8,24))],True)
path('hair',(8,24),[('C',(12,23),(16,21),(19,16)),('C',(24,23),(33,24),(40,24))])
path('mask',(10,34),[('C',(17,32),(31,32),(38,34))])
self.relate('connect','hair','head');self.relate('connect','mask','head')
''','VRECT_L; smooth balanced head outline and continuous interior mask/hair curves.')
patch('python-logo','''
# Two interlocking smooth runs, related by a half-turn.
path('upper',(24,16),[('L',(16,16)),('L',(16,10)),('C',(16,7),(19,6),(24,6)),('C',(29,6),(32,7),(32,12)),('L',(32,17)),('C',(32,22),(29,24),(24,24)),('L',(22,24)),('C',(18,24),(16,26),(16,32)),('L',(12,32)),('C',(8,32),(6,29),(6,24)),('C',(6,19),(8,16),(12,16)),('L',(16,16))])
path('lower',(24,32),[('L',(32,32)),('L',(32,38)),('C',(32,41),(29,42),(24,42)),('C',(19,42),(16,41),(16,36)),('L',(16,32))])
path('right',(32,16),[('L',(36,16)),('C',(40,16),(42,19),(42,24)),('C',(42,29),(40,32),(36,32)),('L',(32,32))])
self.relate('connect','upper','lower');self.relate('connect','upper','right');self.relate('connect','lower','right')
''','SQUARE; smooth aligned interlocking runs with coherent corner tangents; subpixel undulations removed.')
patch('metal-sheet','''
path('front',(12,8),[('L',(44,8)),('L',(44,32)),('L',(16,32)),('L',(16,12)),('A',(12,8),4,4,False)])
path('back',(12,8),[('L',(8,8)),('A',(4,12),4,4,False),('L',(4,40)),('L',(25,40)),('A',(29,36),4,4,False),('L',(29,32))])
self.relate('connect','front','back')
''','HRECT_L; matched radius-four folds with exact attachment nodes and clean straight sheet edges.')
patch('make-up-brush','''
path('bristles',(8,12),[('C',(8,7),(17,4),(24,4)),('C',(31,4),(40,7),(40,12)),('L',(32,20)),('L',(24,20)),('L',(16,20)),('L',(8,12))],True)
path('handle',(16,20),[('C',(16,24),(18,27),(19,28)),('L',(19,39)),('A',(24,44),5,5,False),('A',(29,39),5,5,False),('L',(29,28)),('C',(30,27),(32,24),(32,20))])
self.add_line('bristle',(24,12),(24,20));self.relate('connect','bristle','bristles');self.relate('connect','handle','bristles')
''','VRECT_L; symmetric brush crown, paired handle shoulders and a true round handle end.')
patch('sock','''
rounded('cuff',8,4,32,12,4)
path('body',(12,12),[('L',(12,27)),('C',(12,33),(15,38),(20,40)),('L',(30,44)),('C',(36,44),(40,41),(40,36)),('C',(40,32),(38,29),(34,29)),('C',(30,29),(28,27),(28,24)),('L',(28,12))])
self.relate('connect','body','cuff')
''','VRECT_L; clean cuff radius and continuous toe/heel silhouette; the narrow internal heel pocket is removed.')
patch('fiber-access','''
for name,cy,top in [('upper',14,8),('lower',34,40)]:
 circle_nodes(name,22,cy,5,[(19,cy-4 if top<cy else cy+4)])
 # Each source line bends smoothly to an exact circle boundary.
 if top<cy:path(name+'-input',(4,8),[('L',(15,8)),('C',(17,8),(18,9),(19,10))])
 else:path(name+'-input',(4,40),[('L',(15,40)),('C',(17,40),(18,39),(19,38))])
 self.add_line(name+'-out',(27,cy),(44,cy));self.add_polyline(name+'-arrow',(40,cy-4),(44,cy),(40,cy+4))
 self.relate('connect',name+'-input',name);self.relate('connect',name+'-out',name);self.relate('connect',name+'-out',name+'-arrow')
''','HRECT_L; identical circle nodes, reflected smooth inputs, and equal arrowheads; tangled fitted loops removed.')
patch('twitter-logo-1','''
path('t',(20,23),[('L',(20,29)),('A',(25,34),5,5,False),('L',(35,34)),('A',(40,39),5,5,True),('A',(35,44),5,5,True),('L',(22,44)),('A',(8,30),14,14,True),('L',(8,10)),('A',(14,4),6,6,True),('A',(20,10),6,6,True),('L',(20,13)),('L',(35,13)),('A',(40,18),5,5,True),('A',(35,23),5,5,True),('L',(20,23))],True)
''','VRECT_L; tangent round terminals and a smooth shoulder replace the lopsided top and bottom corners.')
patch('house-7e1b4154','''
self.add_polyline('roof',(6,24),(10,20),(24,6),(38,20),(42,24))
path('walls',(10,20),[('L',(10,38)),('A',(14,42),4,4,False),('L',(20,42)),('L',(20,34)),('A',(24,30),4,4,True),('A',(28,34),4,4,True),('L',(28,42)),('L',(34,42)),('A',(38,38),4,4,False),('L',(38,20))])
self.relate('connect','roof','walls')
''','SQUARE; reflected roof/walls, matched lower corners and a centered semicircular door.')
patch('skate-1','''
path('boot',(8,6),[('L',(25,6)),('L',(25,15)),('C',(25,22),(32,21),(37,25)),('C',(40,27),(42,29),(42,32)),('L',(10,32)),('C',(7,32),(6,29),(6,26)),('C',(6,23),(8,21),(8,18)),('L',(8,6))],True)
for i,x in enumerate([10,25,40]):self.add_line(f'wheel-{i}',(x,42),(x,42))
''','SQUARE; continuous ankle and toe curves replace the polygonal boot bumps; sole and wheels stay aligned.')
patch('bookmarks-document','''
rounded('page',8,4,40,44,4)
self.add_polyline('bookmark',(26,4),(26,24),(33,19),(40,24));self.relate('connect','bookmark','page')
''','VRECT_L; four equal tangent page corners and a straight bookmark with exact page contacts.')
patch('pot','''
path('body',(8,19),[('L',(6,37)),('C',(6,40),(7,42),(10,42)),('L',(30,42)),('C',(33,42),(34,40),(34,37)),('L',(32,19))])
self.add_polyline('rim',(6,19),(8,19),(10,19),(30,19),(32,19))
path('lid',(10,19),[('C',(11,12),(14,8),(20,8)),('C',(26,8),(29,12),(30,19))])
self.add_line('knob',(20,6),(20,8))
path('handle',(32,19),[('C',(38,16),(42,21),(42,26)),('C',(42,30),(37,28),(33,28))])
self.relate('connect','body','rim');self.relate('connect','lid','rim');self.relate('connect','knob','lid');self.relate('connect','handle','body');self.relate('connect','handle','rim')
''','SQUARE; matched body corners, symmetric lid and a single smooth handle; rim kink removed.')
patch('ps','''
self.add_polyline('p-stem',(4,40),(4,25),(4,8),(14,8))
path('p-bowl',(14,8),[('C',(19,8),(23,12),(23,16)),('C',(23,21),(19,25),(14,25)),('L',(4,25))])
path('s',(44,24),[('C',(42,20),(33,19),(33,25)),('C',(33,29),(44,29),(44,35)),('C',(44,38),(42,40),(38,40)),('C',(35,40),(34,39),(33,36))])
self.relate('connect','p-stem','p-bowl')
''','HRECT_L; a round P bowl and a continuous S with smooth inflection replace jagged short arcs.')
patch('email-action-unread','''
rounded('envelope',4,8,44,40,4)
path('flap',(4,12),[('L',(21,25)),('C',(23,27),(25,27),(27,25)),('L',(44,12))])
self.relate('connect','flap','envelope')
''','HRECT_L; four equal corners and a centered smooth flap junction.')
patch('shapes-shape','''
self.add_polyline('square',(19,19),(32,19),(42,19),(42,42),(19,42),(19,32),closed=True)
path('circle',(32,19),[('A',(19,6),13,13,False),('A',(6,19),13,13,False),('A',(19,32),13,13,False)])
self.relate('connect','circle','square')
''','SQUARE; true circle ends exactly on the square; clipped circle and short overlap stubs removed.')
patch('split-transportation','''
self.add_line('stem',(4,24),(20,24))
for name,sgn in [('top',-1),('bottom',1)]:
 def p(x,y):return (x,24+sgn*y)
 path(name,p(20,0),[('C',p(26,0),p(26,12),p(35,12)),('L',p(44,12))])
 self.add_polyline(name+'-arrow',p(40,8),p(44,12),p(40,16));self.relate('connect',name,name+'-arrow');self.relate('connect',name,'stem')
self.relate('connect','top','bottom')
''','HRECT_L; reflected smooth branch curves, matching arrowheads and one shared fork node.')
patch('left-distance','''
self.add_line('limit',(4,8),(4,40));self.add_polyline('box',(26,24),(26,16),(44,16),(44,32),(26,32),closed=True)
self.add_line('shaft',(26,24),(12,24));self.add_polyline('head',(18,18),(12,24),(18,30))
self.relate('connect','shaft','head');self.relate('connect','shaft','box')
''','HRECT_L; straight square corners and equal arrow arms; hooked upper-left box corner removed.')
# A rounded cap owns the diagonal tangent; barrel sides remain straight.
patch('pencil-sketch','''
path('outline',(12,28),[('L',(30,10)),('C',(32,8),(33,6),(36,6)),('A',(42,12),6,6,True),('C',(42,15),(40,16),(38,18)),('L',(20,36)),('L',(6,42)),('L',(12,28))],True)
self.add_line('seam',(26,14),(34,22));self.relate('connect','seam','outline')
''','SQUARE; tangent rounded cap, parallel diagonal barrel and a seam ending exactly on its sides.','Lucide pencil and the validated diagonal pen construction.')
patch('stumble-upon-logo','''
path('s',(4,40),[('L',(18,40)),('C',(25,40),(25,32),(18,31)),('L',(15,30)),('C',(10,29),(10,21),(16,21)),('L',(31,21)),('L',(31,33)),('C',(31,37),(34,40),(37,40)),('C',(41,40),(44,37),(44,33)),('L',(44,8))])
''','HRECT_L; continuous S and U bowls with smooth inflection and matched bottom tangents.')
patch('area-chart','''
self.add_polyline('axes',(4,8),(4,34),(4,40),(44,40))
self.add_polyline('series',(4,34),(14,24),(18,27),(27,16),(35,21),(43,12));self.relate('connect','axes','series')
''','HRECT_L; one deliberate straight segment per chart leg; short inconsistent fitted bends removed.')
for id in ['dog','dog-c099ef25','dog-pets']:
 patch(id,'''
path('profile',(6,35),[('C',(10,24),(15,12),(21,6)),('L',(24,15)),('C',(25,18),(30,17),(35,18)),('C',(39,19),(42,21),(42,25)),('C',(42,31),(34,32),(25,33)),('L',(23,42))])
''','SQUARE; continuous muzzle and neck curves preserve the pointed ear while removing polygonal nose bumps.')
patch('filter','''
self.add_polyline('funnel',(6,6),(42,6),(28,25),(28,34),(20,42),(20,25),closed=True)
''','SQUARE; clean straight funnel rim and walls, with equal shoulder slopes.')
patch('pregnancy-ultrasound','''
path('sector',(17,8),[('C',(21,11),(27,11),(31,8)),('L',(44,30)),('C',(39,35),(30,40),(24,40)),('C',(18,40),(9,35),(4,30)),('L',(17,8))],True)
''','HRECT_L; mirrored scan sector with smooth centered upper and lower arcs.')
patch('common-file-horizontal','''
path('page',(4,8),[('L',(34,8)),('A',(44,18),10,10,True),('L',(44,40)),('L',(4,40)),('L',(4,8))],True)
''','HRECT_L; true tangent radius-ten page shoulder replaces an uneven corner fit.')
patch('symbol-artillery','''
path('body',(9,25),[('C',(9,22),(12,20),(15,19)),('C',(18,18),(21,17),(24,17)),('C',(27,17),(30,18),(33,19)),('C',(36,20),(39,22),(39,25)),('L',(39,36)),('C',(39,41),(31,44),(24,44)),('C',(17,44),(9,41),(9,36)),('L',(9,25))],True)
self.add_polyline('rays',(8,4),(24,14),(40,4))
self.add_polyline('center',(24,4),(24,14),(24,17))
path('left-ray',(8,4),[('L',(8,12)),('C',(8,15),(11,18),(15,19))])
path('right-ray',(40,4),[('L',(40,12)),('C',(40,15),(37,18),(33,19))])
self.relate('connect','rays','center');self.relate('connect','center','body')
for s in ['left-ray','right-ray']:self.relate('connect',s,'rays');self.relate('connect',s,'body')
''','VRECT_L; mirrored rays and a smooth symmetric shell body with exact shared central nodes.')
patch('instagram-logo-1','''
rounded('frame',6,6,42,42,8);oval('lens',24,24,8)
''','SQUARE; four identical tangent corners and a concentric round lens.')
for id,pts in [('rhombus-vertical-shape',[(24,4),(40,24),(24,44),(8,24)]),('rhombus-horizontal-shape',[(24,8),(44,24),(24,40),(4,24)])]:
 patch(id,f"self.add_polyline('diamond',*{pts!r},closed=True)",'Four mirrored straight edges replace short mismatched corner fragments.')
patch('paragraph-1','''
self.add_polyline('stem',(27,42),(27,26),(27,6),(42,6))
path('bowl',(27,6),[('L',(16,6)),('A',(6,16),10,10,False),('A',(16,26),10,10,False),('L',(27,26))])
self.relate('connect','bowl','stem')
''','SQUARE; true semicircular paragraph bowl and exact stem attachments.')
patch('rain-umbrella-closed','''
self.add_polyline('canopy',(8,31),(24,6),(40,31),(24,31),closed=True)
self.add_line('tip',(24,4),(24,6))
path('handle',(24,31),[('L',(24,40)),('A',(20,44),4,4,True),('A',(16,40),4,4,True)])
self.relate('connect','tip','canopy');self.relate('connect','handle','canopy')
''','VRECT_L; centered canopy and true round handle return; lopsided short arcs removed.')
patch('rss-feed-websites','''
path('outer',(6,6),[('A',(42,42),36,36,True)])
path('inner',(6,17),[('A',(31,42),25,25,True)])
self.add_line('dot',(10,38),(10,38))
''','SQUARE; concentric true quarter circles replace multi-arc approximations and terminal kinks.')
patch('phone-merge','''
self.add_polyline('arrow',(14,14),(24,4),(34,14));self.add_line('stem',(24,4),(24,28))
path('left',(24,28),[('C',(24,37),(16,42),(8,44))]);path('right',(24,28),[('C',(24,37),(32,42),(40,44))])
self.relate('connect','stem','arrow');self.relate('connect','left','stem');self.relate('connect','right','stem');self.relate('connect','left','right')
''','VRECT_L; mirrored continuous fork curves and equal arrow arms.')
patch('digg-logo','''
self.add_polyline('stem',(40,4),(40,18),(40,44))
path('bowl',(40,18),[('L',(14,18)),('A',(8,24),6,6,False),('L',(8,38)),('A',(14,44),6,6,False),('L',(40,44))])
self.relate('connect','stem','bowl')
''','VRECT_L; matched tangent corners replace the irregular fitted bowl.')
for id in ['pi','pi-math-symbol']:
 patch(id,'''
self.add_polyline('bar',(4,8),(16,8),(34,8),(44,8));self.add_line('left',(16,8),(10,40))
path('right',(34,8),[('L',(32,29)),('C',(31,39.5),(38,43),(43,37))])
self.relate('connect','bar','left');self.relate('connect','bar','right')
''','HRECT_L; straight stems and one tangent-continuous right foot replace the jagged cluster of arcs.')
patch('virtual-coin-crypto-ontology','''
self.add_line('diagonal',(6,6),(42,42))
path('lower',(6,6),[('L',(6,24)),('C',(6,39),(24,45),(36,36))])
path('upper',(12,12),[('C',(24,3),(42,9),(42,24)),('L',(42,42))])
self.relate('connect','diagonal','lower');self.relate('connect','diagonal','upper')
''','SQUARE; paired smooth opposing lobes meet exact diagonal nodes; top-arc kink removed.')
patch('two-image','''
self.add_polyline('frame',(4,8),(44,8),(44,40),(42,40),(8,40),(4,40),closed=True)
self.add_polyline('mountains',(4,40),(17,23),(23,35),(31,20),(44,40));self.relate('connect','mountains','frame')
''','HRECT_L; truly vertical frame sides and straight mountain edges.')
patch('graph-stats-descend','''
self.add_polyline('series',(4,8),(20,32),(31,19),(44,40));self.add_polyline('head',(34,40),(44,40),(44,30));self.relate('connect','series','head')
''','HRECT_L; clean straight chart legs and equal arrowhead arms.')
patch('line','''
circle_nodes('lower',11,37,5,[(14,33)]);circle_nodes('upper',37,11,5,[(34,15)])
self.add_line('link',(14,33),(34,15));self.relate('connect','link','lower');self.relate('connect','link','upper')
''','SQUARE; two exact equal circles and one straight link, with the extra attachment hooks removed.')
patch('navigation-direction-left-interface-essential','''
self.add_polyline('head',(19,4),(8,15),(19,26))
path('return',(8,15),[('L',(25,15)),('C',(34,15),(40,21),(40,30)),('C',(40,39),(34,44),(25,44)),('L',(21,44))])
self.relate('connect','head','return')
''','VRECT_L; a smooth return bend and equal arrowhead arms replace the three uneven circular fits.')
for id in ['power','power-f71eb996']:
 patch(id,'''
self.add_line('stem',(24,4),(24,23))
path('ring',(14,15),[('C',(10,18),(8,23),(8,28)),('C',(8,37),(15,44),(24,44)),('C',(33,44),(40,37),(40,28)),('C',(40,23),(38,18),(34,15))])
''','VRECT_L; one mirrored smooth power ring replaces the lopsided chain of arc pieces.')
patch('warp-arc-lower','''
path('bowl',(6,6),[('L',(42,6)),('L',(42,24)),('A',(24,42),18,18,True),('A',(6,24),18,18,True),('L',(6,6))],True)
''','SQUARE; equal walls and a true semicircular lower edge.')
patch('glass-blowing','''
self.add_line('pipe',(6,42),(18,30))
path('bulb',(18,30),[('C',(16,28),(16,25),(16,22)),('C',(16,13),(22,6),(31,6)),('C',(38,6),(42,11),(42,18)),('C',(42,27),(35,32),(26,32)),('C',(23,32),(20,32),(18,30))],True)
self.relate('connect','pipe','bulb')
''','SQUARE; tangent-continuous glass bulb and a shared pipe node; uneven neck fragments removed.')
patch('powder-detergent','''
self.add_polyline('rim',(4,8),(29,8),(44,8))
path('cup',(4,8),[('L',(6,36)),('C',(6.143,38),(7,40),(10,40)),('L',(24,40)),('C',(27,40),(27.929,38),(28,36)),('L',(29,8))])
self.relate('connect','cup','rim')
''','HRECT_L; clean paired scoop corners and uninterrupted walls.')
patch('text-format-capital','''
self.add_polyline('a',(8,44),(24,4),(40,44));self.add_line('bar',(14,29),(34,29));self.relate('connect','a','bar')
''','VRECT_L; symmetric A with a clean apex and exact bar junctions; tiny cap fragments removed.')
for id,mirror in [('sharp-turn',False),('left-curve',True)]:
 patch(id,f'''
mirror={mirror!r}
def p(x,y):return (48-x,y) if mirror else (x,y)
path('bend',p(8,44),[('L',p(8,24)),('A',p(20,12),12,12,not mirror),('L',p(40,12))])
self.add_polyline('head',p(32,4),p(40,12),p(32,20));self.relate('connect','head','bend')
''','VRECT_L; true tangent quarter-circle elbow and equal arrowhead arms.')
patch('navigation-right-circle-1','''
path('bend',(4,40),[('L',(4,27)),('A',(16,15),12,12,True),('L',(44,15))])
self.add_polyline('head',(37,8),(44,15),(37,22));self.relate('connect','head','bend')
''','HRECT_L; true radius-twelve elbow replaces the chamfered turn.')
patch('slide-left','''
path('turn',(8,4),[('L',(36,32)),('C',(38,34),(40,35),(40,37)),('C',(40,39),(38,40),(36,42)),('L',(34,44))])
self.add_polyline('head',(20,4),(8,4),(8,16));self.relate('connect','head','turn')
''','VRECT_L; a tangent continuous diagonal turn and equal arrow arms.')
patch('skate','''
path('deck',(4,8),[('C',(5,15),(7,21),(12,24)),('L',(36,24)),('C',(41,21),(43,15),(44,8))])
for i,x in enumerate([13,35]):self.add_line(f'wheel-{i}',(x,40),(x,40))
''','HRECT_L; mirrored smooth deck ends and aligned wheels.')
patch('parallelogram-shape','''
self.add_polyline('shape',(14,8),(44,8),(34,40),(4,40),closed=True)
''','HRECT_L; exact parallel sides and four clean corners; single rounded detour removed.')
patch('plane-travel','''
path('flight',(4,30),[('C',(8,36),(9,40),(13,40)),('C',(16,40),(18,36+7/3),(20,36)),('L',(44,8))])
self.add_line('wing',(14,8),(32,22));self.relate('connect','wing','flight')
''','HRECT_L; smooth flight-path return and an exact wing junction.')
patch('watch-time','''
oval('face',24,24,20);self.add_polyline('hands',(24,13),(24,24),(31,31))
''','CIRCLE; one clean shared clock-hand node replaces a small curved detour.')
patch('vortex','''
path('v',(8,4),[('L',(21,40)),('C',(21+13/12,43),(22,44),(24,44)),('C',(26,44),(27-13/12,43),(27,40)),('L',(40,4))])
''','VRECT_L; matched tangent return curves and a symmetric round bottom.')
(H/'sweep-repairs.json').write_text(json.dumps(changes,indent=2));print('Rebuilt sweep candidates',len(changes))
