# Full-body action scenes use circular heads and round-ended limbs from human_ref/full_body_ref.png.
author(7,'''
self.circle('head',29,8,4)
self.circle('rear-wheel',10,36,8);self.circle('front-wheel',38,36,8)
# Neck junction is (29,20): 20-(8+4)=8 centerline / 4 ink gap.
self.add_bezier('torso',(29,20),((29,23),(19,20),(16,25)))
self.path('leg',(16,25),('L',(25,31)),('L',(22,39)))
self.path('arm',(29,20),('L',(34,25)),('L',(39,25)))
self.add_line('fork',(35,25),(38,36))
self.add_line('rear-frame',(10,36),(20,30))
self.add_line('pedal',(20,39),(24,39))
self.relate('connect','torso','leg');self.relate('connect','torso','arm');self.relate('connect','leg','pedal')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','SQUARE','The rejected cyclist used tiny wheels and an upright, broken pose that did not read as racing. The original has full bicycle wheels, a low back and a bent pedaling leg.',
 'Restore large paired wheels, low curved racing torso, forward hands, sloped fork and bent pedaling leg. Head (29,8), r4, neck (29,20) gives exact 4px detached ink gap.',
 'human_ref/full_body_ref.png circular head and simple action limbs; Lucide bike wheel/pose construction.',
 'Frame reduced to rear stay and fork; small shoe simplified to pedal stroke.',
 exception_reason='Complete cycling action requires wheel/frame overlaps and compact leg-to-wheel spacing. User authorized visual exception while head-to-torso gap stays exactly 4px and all strokes stay 4px.')
author(8,'''
self.circle('head',29,8,4)
# Large rear wheel and low forward outrigger are distinctive racing-wheelchair geometry.
self.circle('rear-wheel',14,33,11)
self.circle('front-wheel',39,38,6)
self.add_bezier('torso',(29,20),((29,23),(21,20),(18,23)))
self.path('pushing-arm',(25,21),('L',(21,28)),('L',(16,29)))
self.path('legs',(18,23),('L',(28,28)),('L',(29,35)),('L',(33,35)))
self.add_line('outrigger',(26,33),(39,38))
self.add_dot('rear-hub',(14,33))
self.relate('connect','torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','SQUARE','The rejected athlete was an isolated head over a thick wheel-and-bar symbol; the leaning torso, pushing arm and seated leg were lost.',
 'Large rear racing wheel, smaller forward wheel and long low outrigger beneath a leaning rider with a bent pushing arm and seated leg. Exact 4px head/body ink gap at (29,20).',
 'human_ref/full_body_ref.png action proportions; Lucide bike informs circular wheels; supplied reference owns wheelchair geometry.',
 'Fine clothing and wheel spokes omitted.',
 exception_reason='Racing wheelchair preserves true equipment overlap and compact bent limbs under the authorized visual exception. No false connection is used to hide spacing findings; native-size review verifies the silhouette.')
author(6,'''
self.circle('head',24,8,4)
self.path('arms',(6,4),('L',(11,17)),('L',(24,22)),('L',(37,17)),('L',(42,4)))
self.add_line('torso',(24,20),(24,23))
self.circle('medal',24,27,3)
# Front-facing racing chair: three wheel axes, not running legs.
self.path('central-wheel',(21,36),('A',(27,36),3,3,True),('L',(27,42)),('A',(21,42),3,3,True),('L',(21,36)),closed=True)
self.add_line('left-wheel',(12,33),(7,44));self.add_line('right-wheel',(36,33),(41,44))
self.add_line('axle-left',(11,38),(21,38));self.add_line('axle-right',(27,38),(37,38))
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','SQUARE','The rejected racer replaced the central front wheel with running legs and omitted the medal and chair axle. The original shows a celebrating seated racer.',
 'Raised symmetrical arms, circular head, central medal and a front-facing racing chair with three wheel axes and horizontal axle. Head bottom12 to torso20 gives exact 4px ink gap.',
 'human_ref/full_body_ref.png circular head and round-ended limbs; original controls raised-arm pose and chair.',
 'Outlined arms reduced to single strokes; retain medal and all three wheels.',
 exception_reason='Medal, chair wheels and axle need compact true overlaps and narrow wheel openings. User authorized meaning-preserving exception; head/torso spacing is retained exactly.')
author(9,'''
self.circle('head',24,20,6)
# Circular jaw bottom26 and shoulders apex30 leave touching 4px ink, as bust contract.
self.path('robe',(12,44),('L',(12,38)),('A',(24,30),12,8,True),('A',(36,38),12,8,True),('L',(36,44)),('L',(12,44)),closed=True)
self.add_line('sash',(12,42),(34,33))
self.relate('connect','head','robe')
self.add_line('top-ray',(24,3),(24,7))
self.add_line('left-ray',(6,22),(9,22));self.add_line('right-ray',(39,22),(42,22))
self.add_line('upper-left-ray',(10,7),(13,10));self.add_line('upper-right-ray',(35,10),(38,7))
self.human_construction='bust'
''','VRECT_L','The rejected monk had an off-center head, only three rays and an open generic bust. The original shows a centered radiant monk with a full robe and diagonal sash.',
 'Centered circular head above a closed robe, a diagonal shoulder sash and five balanced radiance strokes. Touching-ink bust construction: head bottom26, robe apex30.',
 'human_ref/user.svg circular head and broad shoulders; source specifies robe, sash and rays.',
 'Small robe seam omitted.',
 exception_reason='Five radiance rays and diagonal robe sash retain compact local gaps and organic bounds. User authorized the native-size visual exception; 4px strokes and circular head are preserved.')
author(5,'''
# Scooter faces left like the original: handle above the front wheel, rabbit behind it.
self.circle('front-wheel',8,40,4);self.circle('rear-wheel',39,40,4)
self.add_line('deck',(12,40),(35,40))
self.path('steering',(8,40),('L',(8,9)),('L',(4,7)))
# Tall backward-swept ear, snout and haunch are one coherent rabbit silhouette.
self.add_bezier('ear',(29,18),((20,12),(20,5),(24,5)),((29,5),(32,12),(34,15)))
self.add_bezier('face',(34,15),((41,16),(44,20),(41,24)),((39,26),(35,26),(34,26)))
self.add_bezier('back',(34,26),((35,32),(31,35),(29,36)))
self.add_line('hind-foot',(29,36),(29,40))
self.add_bezier('chest',(29,18),((28,23),(30,26),(25,26)))
self.add_line('reaching-arm',(25,26),(8,26))
self.add_line('front-leg',(25,26),(21,40))
self.add_contour('rabbit-outline','ear','face','back','hind-foot')
self.relate('connect','rabbit-outline','chest');self.relate('connect','chest','reaching-arm');self.relate('connect','chest','front-leg');self.relate('connect','front-leg','deck');self.relate('connect','rabbit-outline','deck')
''','SQUARE','The rejected scooter rabbit was reversed and its ear/body shape read like an abstract human. The reference shows a left-facing scooter with a rabbit behind the handlebar.',
 'Restore left-side steering stem and wheel, long swept rabbit ear, distinct snout, rounded haunch, reaching arm and feet on the deck.',
 'Lucide bike circular wheels and coherent equipment strokes; source rabbit silhouette defines long ear and head.',
 'Tiny eye omitted to keep the head open.',
 exception_reason='Rabbit and scooter use compact true overlaps and a narrow steering/body gap to keep the complete reference scene. User authorized native-size visual exception with 4px strokes and 48px canvas.')
