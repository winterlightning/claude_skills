from author import make
make(1,'VRECT_L','The rejected waist had straight angular sides and a triangular crotch. Restore the curved waist, bowed waistband and two rounded leg openings from the original. No written feedback.', '''
path('left',(12,4),[('C',(14,18),(15,10),(16,13)),('C',(10,26),(13,22),(11,24)),('C',(8,34),(9,28),(8,31)),('L',(8,44))])
path('right',(36,4),[('C',(34,18),(33,10),(32,13)),('C',(38,26),(35,22),(37,24)),('C',(40,34),(39,28),(40,31)),('L',(40,44))])
path('band',(10,26),[('C',(38,26),(19,28),(29,28))])
# Side band attaches at exactly authored points on the waist curves.
path('leg-left',(8,34),[('C',(20,44),(14,34),(19,39))])
path('leg-right',(40,34),[('C',(28,44),(34,34),(29,39))])
join('left','leg-left');join('right','leg-right');join('left','band');join('right','band')
''', 'Original waist; paired cubic sides and mirrored leg openings.')
make(2,'SQUARE','The rejected tactile paving became two uninterrupted bars. Restore separate dashed paving tracks and a bent-arm walking pose.', '''
circle('head',31,10,4)
line('torso',(31,22),(31,32))
poly('arms',(25,27),(31,22),(38,26),(42,26));join('arms','torso')
poly('legs',(25,42),(31,32),(40,42));join('legs','torso')
self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
for x in (6,14):
 for j,y in enumerate((6,22,38)):line(f'paving-{x}-{j}',(x,y),(x,y+4))
''','human_ref/full_body_ref.png: outlined head, articulated limbs, head outline14 to torso22 gives exact4 ink gap. Two dashed tracks retain tactile paving.')
make(3,'SQUARE','The rejected bust had a narrow vertical neck and steep shoulders. Restore a round head, a short gently curved neck and broad sloping shoulders in one continuous silhouette.', '''
path('bust',(6,42),[('C',(18,30),(10,40),(18,37)),('C',(15,23),(18,27),(17,25)),('A',(12,16),10,10,True),('A',(36,16),12,10,True),('A',(33,23),10,10,True),('C',(30,30),(31,25),(30,27)),('C',(42,42),(30,37),(38,40))])
''','human_ref/user.svg for broad shoulders; original continuous-neck silhouette retained.')
make(4,'HRECT_L','The rejected unicorn was blocky, with an extra left-pointing spike and fused rectangular legs. Restore the single upright horn, long muzzle, rounded back and four separated stepping legs.', '''
path('horse',(10,18),[('L',(4,20)),('L',(4,16)),('L',(12,10)),('L',(12,8)),('L',(18,12)),('C',(24,22),(21,13),(20,22)),('L',(34,22)),('C',(40,28),(38,22),(40,24)),('L',(44,40)),('L',(36,40)),('L',(32,30)),('L',(23,30)),('L',(20,40)),('L',(12,40)),('L',(16,26)),('L',(10,28)),('L',(10,18))],True)
''','Original unicorn; smooth cubic back and shared leg junctions; simplified mane and tail.')
make(5,'SQUARE','The rejected commuter carried a tiny square case and raised a rigid horizontal arm. Widen the case, bend the carrying arm and angle the forward arm down as in the reference.', '''
circle('head',29,11,5)
line('torso',(29,24),(29,33))
poly('legs',(23,42),(29,33),(39,42));join('legs','torso')
path('front',(29,24),[('C',(42,28),(34,24),(36,28))]);join('front','torso')
poly('back',(29,24),(16,24),(12,29));join('back','torso')
poly('case',(6,29),(12,29),(16,29),(16,37),(6,37),closed=True);join('case','back')
self.mark_human_figure('commuter',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png; outlined head and round-ended moving limbs; exact4 ink gap at actual torso junction.')
make(6,'HRECT_L','The rejected wallet became a tall bag. Restore a wider rectangular wallet with a folded upper edge and a large inset clasp on the right.', '''
path('body',(8,8),[('L',(36,8)),('A',(40,12),4,4,True),('L',(40,16)),('L',(44,20)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
line('fold',(4,16),(31,16));join('body','fold')
path('clasp',(44,24),[('L',(32,24)),('A',(32,32),4,4,False),('L',(44,32))]);join('clasp','body')
''','Lucide wallet original and atoms: rounded wallet body, folded upper edge and side clasp.')
make(7,'SQUARE','The rejected warrior pose had a very short torso and a nearly horizontal rear leg. Lengthen the torso and open a clear bent forward knee and diagonal straight rear leg.', '''
circle('head',24,10,4)
line('torso',(24,22),(24,32))
poly('arms',(6,22),(24,22),(42,22));join('arms','torso')
poly('legs',(10,42),(10,34),(24,32),(38,42));join('legs','torso')
self.mark_human_figure('warrior',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: round-ended limbs and circle head; head bottom14 to torso22 gives4 ink gap.')
controller='''
path('body',(8,18),[('A',(24,4),16,14,True),('A',(40,18),16,14,True),('C',(32,28),(40,24),(37,26)),('L',(32,38)),('C',(18,44),(32,44),(24,44)),('C',(8,36),(12,44),(8,42)),('C',(12,25),(8,32),(11,28)),('C',(8,18),(10,23),(8,21))],True)
path('window',(18,17),[('A',(30,17),6,4,True),('A',(18,17),6,4,True)],True)
'''
make(8,'VRECT_L','The rejected tracking window was a solid bar. Restore the oval opening and a rounded handle, keeping the lower button.',controller+"self.add_dot('button',(20,33))",'Original VR controller; shared oval window and curved handle.')
make(9,'VRECT_L','The rejected direction-pad controller lost its large upper oval window and moved the plus into that area. Restore the window above a separate lower direction pad.',controller+"poly('pad-h',(18,33),(20,33),(22,33))\npoly('pad-v',(20,31),(20,33),(20,35));join('pad-h','pad-v')",'Original VR controller; Lucide gamepad-2 informs crossed pad strokes.')
make(10,'HRECT_L','The rejected headset used small top and bottom semicircles and a sharp central notch. Restore a broad head strap, a wide visor and a rounded nose opening.', '''
path('visor',(10,18),[('L',(38,18)),('A',(44,24),6,6,True),('L',(44,29)),('A',(38,35),6,6,True),('L',(32,35)),('C',(24,30),(28,35),(29,30)),('C',(16,35),(19,30),(20,35)),('L',(10,35)),('A',(4,29),6,6,True),('L',(4,24)),('A',(10,18),6,6,True)],True)
path('strap',(8,18),[('C',(24,8),(9,9),(16,8)),('C',(40,18),(32,8),(39,9))]);join('strap','visor')
path('lower',(12,35),[('C',(24,40),(14,40),(19,40)),('C',(36,35),(29,40),(34,40))]);join('lower','visor')
''','Original headset; mirrored visor corners and rounded symmetric nose notch.')
make(11,'SQUARE','The rejected hand was an ordinary closed-finger palm. Restore the identifying V separation between paired fingers and a projecting thumb.', '''
path('palm',(8,24),[('L',(8,30)),('A',(20,42),12,12,False),('L',(26,42)),('C',(42,26),(36,42),(42,33)),('L',(39,29))])
line('little',(8,24),(6,12));join('little','palm')
poly('inner-left',(8,24),(16,24),(14,6));join('inner-left','palm');join('inner-left','little')
poly('inner-right',(16,24),(27,24),(32,6));join('inner-right','inner-left')
poly('outer-right',(27,24),(36,24),(40,12));join('outer-right','inner-right')
''','Lucide hand original and atoms for round finger tips; source paired-finger V separation retained with single strokes.')
make(12,'VRECT_L','The rejected trigger controller replaced the oval tracking window with a bar and used an angular grip. Restore the open window and a smooth handle with a lower trigger mark.',controller+"line('trigger',(18,35),(20,31))",'Original VR controller with shared oval tracking window and lower trigger stroke.')
make(13,'SQUARE','The rejected detector omitted the beep rays and reduced the person to a head over a tiny cup. Restore a recognisable central standing figure and side sound marks in an open portal.', '''
line('wall-left',(14,42),(14,10));line('wall-right',(34,10),(34,42))
path('portal',(14,10),[('A',(18,6),4,4,True),('L',(30,6)),('A',(34,10),4,4,True)])
join('portal','wall-left');join('portal','wall-right')
circle('head',24,18,2)
line('torso',(24,28),(24,34))
poly('legs',(23,42),(24,34),(25,42));join('torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
for x in (6,42):
 line(f'beep-{x}',(x,22),(x,28))
''','human_ref/full_body_ref.png: round outlined head and minimal body; head bottom20 to torso28 exact4 ink gap.')
make(14,'SQUARE','The rejected voodoo doll was an upright broad-headed ornament with the pin missing. Restore the diagonally tilted sewn doll, cross eyes, and the pin entering from the upper left.', '''
path('doll',(26,23),[('C',(25,13),(24,20),(25,15)),('C',(33,6),(25,9),(28,6)),('C',(42,14),(39,6),(42,8)),('C',(35,23),(42,20),(40,23)),('L',(41,29)),('A',(35,35),4,4,True),('L',(30,30)),('L',(21,42)),('L',(15,37)),('L',(11,40)),('A',(6,34),4,4,True),('L',(18,23)),('L',(12,17)),('A',(18,11),4,4,True),('L',(26,23))],True)
# One crossed eye preserves the sewn-toy expression at this scale.
poly('eye-h',(31,14),(33,16),(35,18))
poly('eye-v',(31,18),(33,16),(35,14));join('eye-h','eye-v')
circle('pin-head',8,8,2)
line('pin',(10,10),(20,20));join('pin','pin-head');join('pin','doll')
''','Original tilted sewn doll; round-ended toy contours and pin; no useful exact Lucide match.')
make(15,'CIRCLE','The rejected coin used an upright closed D and a single tick. Restore the slanted D stem and two currency ticks, keeping the coin rim.', '''
circle('coin',24,24,20)
path('d',(16,16),[('L',(25,16)),('A',(25,32),8,8,True),('L',(16,32)),('L',(20,21))])
for x in (20,28):
 line(f'top-{x}',(x,13),(x,16));join(f'top-{x}','d')
 line(f'bottom-{x}',(x,32),(x,35));join(f'bottom-{x}','d')
''','Original Digibyte currency mark: open slanted stem, smooth D bowl and paired ticks.')
make(16,'HRECT_M','The rejected infinity symbol had tall narrow loops. Restore broad horizontal bowls and a smooth diagonal crossover, preserving exact mirrored loops.', '''
path('infinity',(24,24),[('C',(13,10),(19,18),(18,10)),('C',(4,24),(7,10),(4,15)),('C',(13,38),(4,33),(7,38)),('C',(24,24),(18,38),(19,30)),('C',(35,10),(29,18),(30,10)),('C',(44,24),(41,10),(44,15)),('C',(35,38),(44,33),(41,38)),('C',(24,24),(30,38),(29,30))],True)
''','Original infinity; shared mirrored bowls with continuous crossover tangents.')
make(17,'HRECT_L','The rejected vibration controller lost its controls and moved the vibration arcs above and below. Restore the gamepad controls and side vibration marks.', '''
path('body',(16,16),[('L',(32,16)),('A',(36,20),4,4,True),('L',(36,36)),('A',(32,40),4,4,True),('L',(28,32)),('L',(20,32)),('L',(16,40)),('A',(12,36),4,4,True),('L',(12,20)),('A',(16,16),4,4,True)],True)
poly('pad-h',(19,24),(21,24),(23,24));poly('pad-v',(21,22),(21,24),(21,26));join('pad-h','pad-v')
self.add_dot('button',(30,24))
path('buzz-left',(6,8),[('C',(4,24),(4,12),(4,18)),('C',(6,38),(4,30),(4,34))])
path('buzz-right',(42,8),[('C',(44,24),(44,12),(44,18)),('C',(42,38),(44,30),(44,34))])
''','Lucide gamepad-2 original and atoms for paired controls and rounded grips; reference side vibration arcs.')
make(18,'HRECT_L','The rejected watermelon was an upright bowl with one seed. Restore the diagonal cut edge, curved rind and separated seeds in the flesh.', '''
path('wedge',(4,30),[('L',(36,8)),('C',(44,22),(42,12),(44,17)),('C',(25,40),(44,34),(36,40)),('C',(4,30),(16,40),(8,37))],True)
path('rind',(11,25),[('C',(34,13),(22,42),(43,29))]);join('rind','wedge')
self.add_dot('seed',(24,22))
''','Original diagonal melon wedge; smooth curved rind, simplified seed detail.')
make(19,'SQUARE','The rejected Iota mark used four short inward hooks around an empty center. Restore four longer sweeping open arcs with a consistent rotational flow.', '''
for j in range(4):
 def p(x,y):
  for _ in range(j):x,y=48-y,x
  return x,y
 self.add_bezier(f'arm-{j}',p(18,6),(p(31,6),p(42,10),p(42,20)),(p(42,27),p(39,31),p(33,33)))
''','Original rotational mark; one shared sweeping curve rotated through four quarter turns.')
make(20,'SQUARE','The rejected profile-selection icon lost the hair, leaving a generic broken circle and cursor. Restore a swept hair division and an unmistakable selection pointer.', '''
path('head',(19,32),[('A',(6,19),15,13,True),('A',(34,19),14,13,True)])
path('hair',(7,14),[('C',(21,9),(12,17),(18,14)),('C',(32,14),(24,14),(28,15))]);join('hair','head')
poly('cursor',(27,26),(42,33),(35,35),(32,42),closed=True)
''','Original head/cursor; Lucide user supporting round head construction; hair retained to identify a profile.')
