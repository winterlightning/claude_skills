for i in [11,12]:
 author(i,'''
self.add_arc('outer',(4,26),(44,26),radius_x=20,radius_y=18,sweep=True)
self.add_arc('middle',(11,27),(37,27),radius_x=13,radius_y=12,sweep=True)
self.add_arc('inner',(18,28),(30,28),radius_x=6,radius_y=6,sweep=True)
self.path('left-cloud',(4,33),('A',(12,35),8,8,True),('A',(12,43),4,4,True),('L',(4,43)))
self.path('right-cloud',(44,33),('A',(36,35),8,8,False),('A',(36,43),4,4,False),('L',(44,43)))
''','HRECT_L','The rejected rainbow had two bands and heavy cloud junctions. Feedback asks to restore its intended meaning.',
 'Three concentric-looking upper bands separated from two mirrored cloud ends; preserve all three bands and airy source composition.',
 'Lucide rainbow: nested semicircular bands; reference defines opposing open cloud ends.',
 'Cloud ends remain open as in source.',
 exception_reason='Three bands keep at least approximately 2px visible gaps while retaining 4px strokes. Natural cloud placement slightly exceeds the selected vertical envelope but stays inside 48px; authorized visual exception.')
# Pruner blades and outlined handles distinguish a cutting tool from a letter R.
author(0,'''
self.add_line('stem',(13,24),(13,44))
self.path('top-leaf',(13,24),('A',(13,4),13,14,True),('A',(13,24),13,14,True),closed=True)
self.path('side-leaf',(12,31),('A',(4,19),12,12,True),('A',(12,31),12,12,True),closed=True)
self.relate('connect','stem','top-leaf')
self.path('blade',(29,24),('L',(34,6)),('A',(34,23),14,14,True),('L',(32,25)))
self.path('left-grip',(29,24),('L',(23,40)),('A',(28,42),3,3,False),('L',(33,28)))
self.path('right-grip',(32,25),('A',(37,28),5,5,True),('L',(43,40)),('A',(38,42),3,3,True),('L',(33,31)))
self.relate('connect','blade','left-grip');self.relate('connect','blade','right-grip')
''','HRECT_L','The rejected pruner looked like an R beside a single leaf: its cutting jaws, outlined grips and second leaf were lost.',
 'Restore a two-leaf stem beside curved pruning jaws with two individually outlined angled grips; deliberately asymmetric natural plant and tool.',
 'Lucide scissors: pivot-based cutting tool silhouette and separated grips. Supplied pruner defines curved blade and leaf arrangement.',
 'Tiny pivot hardware omitted to avoid a dark blob.',
 exception_reason='Narrow outlined grips and leaf tips are essential to distinguish pruning shears. Local spacing and keyshape variance accepted under user authorization after native-size review.')
# Queasy face: closed downcast eyes and a detached breath cloud, not a tongue fused to the jaw.
author(1,'''
self.path('face',(28,43),('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('L',(44,27)))
self.add_arc('left-eye',(12,18),(20,18),radius_x=5,radius_y=4,sweep=False)
self.add_arc('right-eye',(28,18),(36,18),radius_x=5,radius_y=4,sweep=False)
self.add_arc('mouth',(19,32),(23,29),radius_x=5,radius_y=5,sweep=True)
self.path('queasy-puff',(29,30),('A',(35,29),4,4,True),('A',(39,32),5,5,False),('A',(44,36),5,5,True),('A',(35,43),9,7,True),('A',(28,36),8,8,True),('A',(29,30),6,6,True),closed=True)
''','CIRCLE','The rejected face had angry eyes and a mouth-like shape fused to its jaw. The source shows closed queasy eyes, pursed mouth and a separate breath puff.',
 'Downcast curved eyelids, a small pursed mouth, open lower-right face outline and a detached organic queasy puff.',
 'Supplied face defines expression; Lucide circular construction informs the head outline.',
 exception_reason='Expressive mouth and puff require local spacing below 4px and an open circular envelope; all marks stay in canvas and use 4px stroke. User authorized expression-preserving exception.')
# Cog radiates with actual strokes, not four dots.
author(10,'''
# Symmetric six-tooth cog with alternating rounded lobes and valleys.
self.path('gear',(21,13),('L',(27,13)),('L',(28,17)),('L',(32,17)),('L',(35,22)),('L',(32,25)),('L',(34,29)),('L',(30,33)),('L',(26,31)),('L',(24,35)),('L',(19,33)),('L',(19,29)),('L',(14,28)),('L',(13,23)),('L',(17,21)),('L',(17,17)),('L',(21,16)),closed=True)
for name,p,q in [('top',(24,4),(24,7)),('bottom',(24,41),(24,44)),('left',(4,24),(7,24)),('right',(41,24),(44,24)),('nw',(8,8),(11,11)),('ne',(37,11),(40,8)),('sw',(8,40),(11,37)),('se',(37,37),(40,40))]:
    self.add_line(name,p,q)
''','SQUARE','The rejected gear replaced the radial light strokes with four dots and used a coarse hexagonal outline. Feedback asks to recover the radiating cog.',
 'A toothed central cog surrounded by eight short radial strokes; preserve the reference absence of a central hub.',
 'Lucide settings: coherent toothed silhouette; supplied reference specifies eight radiating strokes.',
 exception_reason='Eight radial rays require a compact cog-to-ray gap and non-square radial envelope. These remain legible with uniform 4px strokes under the authorized exception.')
for i in [13,14]:
 body='''
self.path('fist',(10,27),('L',(10,15)),('A',(16,15),3,3,True),('L',(16,12)),('A',(22,12),3,3,True),('L',(22,10)),('A',(28,10),3,3,True),('L',(28,12)),('A',(34,12),3,3,True),('L',(34,20)),('L',(38,25)),('A',(38,33),8,8,True),('L',(33,40)),('L',(33,44)),('L',(15,44)),('L',(15,39)),('A',(10,27),18,18,True),closed=True)
self.path('thumb',(34,20),('L',(26,20)),('A',(26,28),4,4,False),('L',(30,28)),('A',(24,34),9,9,False))
self.relate('connect','fist','thumb')
for x,y,end in [(16,15,25),(22,12,22),(28,12,19)]:
    self.add_line(f'knuckle-{x}',(x,y),(x,end));self.relate('connect','fist',f'knuckle-{x}')
'''
 if i==13:
  # Lift the fist slightly less; short protest rays above the knuckles.
  body+='''
self.add_line('ray-left',(6,6),(9,9))
self.add_line('ray-right',(39,6),(42,3))
self.add_line('ray-top',(24,2),(24,3))
'''
 author(i,body,'VRECT_L','The rejected fist lost its curled-finger anatomy and wrist; the thumb became a slash or a flat capsule. Feedback asks for the raised closed-fist meaning.',
 'Four staggered knuckle caps, attached vertical finger divisions, an opposing folded thumb, curved palm and narrowed wrist'+('; restore protest emphasis rays.' if i==13 else '.'),
 'Lucide hand-fist: knuckle construction, opposing thumb and rounded palm; source controls upright pose.',
 'Minor palm crease simplified to one curved run.',
 exception_reason='Clenched fingers have 6-unit pitch and thumb overlaps; anatomical slots below MIC are intentionally retained and readable. User authorized complete-gesture exception.')
# Waving hand: all fingers and wrist, with two separate motion arcs.
author(15,'''
self.path('hand',(23,29),('L',(23,12)),('A',(29,12),3,3,True),('L',(29,8)),('A',(35,8),3,3,True),('L',(35,12)),('A',(41,12),3,3,True),('L',(41,17)),('A',(46,17),3,3,True),('L',(46,29)),('A',(41,39),13,13,True),('L',(41,44)),('L',(29,44)),('L',(29,40)),('L',(17,28)),('A',(22,23),4,4,True),('L',(23,29)),closed=True)
for x,y in [(29,12),(35,12),(41,17)]:
    self.add_line(f'finger-{x}',(x,y),(x,25));self.relate('connect','hand',f'finger-{x}')
self.add_arc('motion-outer',(14,8),(8,35),16,16,False) if False else None
self.add_arc('motion-outer',(14,8),(8,35),radius_x=16,radius_y=16,sweep=False)
self.add_arc('motion-inner',(14,17),(12,28),radius_x=7,radius_y=7,sweep=False)
''','SQUARE','The rejected hand was broken at the wrist, had only two clear fingers and tiny partial motion curves. Feedback asks to recover the raised hand beside curved motion lines.',
 'Restore a continuous four-finger hand with opposing thumb and wrist, beside two broad nested motion arcs; intentional right-weighted composition.',
 'Lucide hand: digit hierarchy and continuous palm. Original controls left-side motion arcs.',
 exception_reason='Full hand plus motion arcs requires anatomical 6-unit finger pitch and narrow local gaps. The 48px silhouette and 4px strokes remain intact; user authorized visual exception.')
