import designs as a
from author import *
D=a.D
add('lightbulb-speech-bubble','SQUARE','Faceted speech outline and squat bulb lose the rounded message and bulb silhouette. Round the bubble and give bulb shoulders a clearer taper.','lightbulb and messages-square: round dome and curved enclosure', '''
path('bubble',(14,34),[('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(22,34)),('L',(14,42)),('L',(14,34))],True)
path('bulb',(18,20),[('A',(30,20),6,5,True),('C',(28,25),(30,23),(28,23)),('L',(20,25)),('C',(18,20),(20,23),(18,23))],True)
''','Bulb screw threads omitted at 48px.')
for key in ('magnifying-glass-batch-04-v2','magnifying-glass-batch-04'):
 add(key,'SQUARE','Original plus sign was omitted from the rejected magnifier. Restore an evenly centered plus inside the circular lens.','search: circular lens and diagonal handle', '''
self.add_arc('lens-main',(30,33),(6,21),radius_x=15,large_arc=True,sweep=False)
self.add_arc('lens-return',(6,21),(30,33),radius_x=15,sweep=False)
self.add_contour('lens','lens-main','lens-return',closed=True)
line('handle',(30,33),(42,42));join('handle','lens')
line('plus-horizontal',(15,21),(27,21));line('plus-vertical',(21,15),(21,27));join('plus-horizontal','plus-vertical')
''')
add('map-with-location-pin','VRECT_L','Broad shallow pin resembles a fan; restore rounded teardrop marker and a slightly tapered map.','map-pin: rounded crown tapering to a point', '''
path('pin',(14,14),[('A',(34,14),10,10,True),('C',(24,28),(34,19),(28,24)),('C',(14,14),(20,24),(14,19))],True)
self.add_dot('center',(24,14))
poly('map',(10,26),(8,44),(40,44),(38,26))
line('map-row',(9,36),(39,36));join('map-row','map')
for x in (18,30):line(f'fold{x}',(x,36),(x,44));join(f'fold{x}','map');join(f'fold{x}','map-row')
''','Fine upper map grid omitted for the pin.')
add('mobile-phone-outgoing-arrow','SQUARE','Phone frame is too narrow and arrowhead too short. Widen phone and enlarge the outgoing arrow while preserving side opening.','smartphone and arrow-up: rounded device, open arrowhead', '''
path('phone',(28,14),[('L',(28,10)),('A',(24,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(24,42)),('A',(28,38),4,4,False),('L',(28,30))])
line('bezel',(6,34),(28,34));join('bezel','phone')
line('shaft',(18,22),(42,22));poly('arrow',(34,14),(42,22),(34,30));join('shaft','arrow')
''')
add('person-with-halo','VRECT_L','Narrow halo opening and angular shoulders make the bust mechanical. Open halo ellipse and replace polygon shoulders with a smooth symmetric arc.','human_ref/user.svg: circular head and broad shoulders', '''
oval('halo',24,8,12,4)
oval('head',24,26,6,6)
path('shoulders',(8,44),[('A',(40,44),16,4,True)])
# Head bottom32; shoulder apex40: exactly8 centerline /4 ink.
''','Lower torso outline omitted to preserve halo/head/shoulder clearances.')
add('person-with-radiant-aura','SQUARE','Small head and short flat rays understate the radiant bust. Enlarge circular head and spread diagonal rays around it.','human_ref/user.svg: circular head with smooth shoulders; bust ink contact', '''
oval('head',24,24,8,8)
path('body',(10,42),[('A',(24,36),14,6,True),('A',(38,42),14,6,True)])
join('head','body')
for j,(p,q) in enumerate([((24,6),(24,8)),((6,12),(9,14)),((42,12),(39,14)),((6,28),(9,27)),((42,28),(39,27))]):line(f'ray{j}',p,q)
''')
add('person-with-spiritual-enlightenment-symbols','SQUARE','Tiny head above triangular shoulders loses the rounded portrait; restore a circular head and smooth shoulders under three inward marks.','human_ref/user.svg: circular head and smooth bust; source aura', '''
path('aura',(8,34),[('C',(6,24),(6,31),(6,27)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(40,34),(42,27),(42,31))])
poly('mark-center',(21,15),(24,18),(27,15))
line('mark-left',(14,21),(16,23));line('mark-right',(34,21),(32,23))
oval('head',24,30,4,4)
path('body',(14,42),[('A',(24,38),10,4,True),('A',(34,42),10,4,True)]);join('head','body')
''','Side inward chevrons reduced to one stroke each; open body.')
add('performance-decrease','SQUARE','Four solid lines lose the outlined bar-chart form. Restore three progressively shorter outlined bars beneath declining arrow.','No additional useful Lucide match; shared arrowhead construction.', '''
poly('baseline',(6,42),(42,42))
for j,(x,top) in enumerate([(6,20),(20,28),(34,34)]):
 poly(f'bar{j}',(x,42),(x,top),(x+8,top),(x+8,42));join(f'bar{j}','baseline')
line('trend',(6,6),(40,22));poly('arrow',(30,22),(40,22),(38,12));join('trend','arrow')
''','Four bars reduced to three to keep distinct hollow columns.')
add('person-magnifying-glass','SQUARE','Steep handle and narrow shoulders differ from diagonal magnifier and broad bust. Re-angle handle and broaden shoulder contour.','search plus human_ref/user.svg: circular head, exact detached gap', '''
# Lens center21,21,r15; integer diagonal handle attachment30,33.
self.add_arc('lens-main',(30,33),(6,21),radius_x=15,large_arc=True,sweep=False)
self.add_arc('lens-return',(6,21),(30,33),radius_x=15,sweep=False)
self.add_contour('lens','lens-main','lens-return',closed=True)
line('handle',(30,33),(42,42));join('handle','lens')
oval('head',21,18,4,4)
path('shoulders',(12,33),[('A',(30,33),9,3,True)]);join('shoulders','lens')
# Head bottom22; shoulder apex30: exact4-unit ink gap.
''')
add('person-in-car-seat-upload-fd4797857bc4b544','SQUARE','Current reference has a bulky enclosed seat and a disjoint angular body. Redraw seat as a smooth open profile with a recognizable seated torso and legs.','human_ref/full_body_ref.png: circular head, coherent torso and limbs', '''
oval('head',18,10,4,4)
poly('torso',(18,22),(24,30),(34,30),(42,36))
poly('arm',(24,30),(24,22),(34,18));join('arm','torso')
path('seat',(6,22),[('C',(14,38),(8,28),(8,34)),('C',(30,42),(18,42),(24,42)),('L',(34,42))])
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
''','Source is current drawing because production has no original. Seat interior outline omitted.')
add('person-snowboarding-downhill-upload-52ddb7b225333f49','SQUARE','Current skier-like angular torso has a floating head to the right. Rebuild a leaning snowboarder with head aligned to upper torso and bent knees over a curved board.','human_ref/full_body_ref.png: head aligned to torso, bent round-ended limbs', '''
oval('head',32,10,4,4)
poly('torso',(32,22),(24,30),(32,32),(28,40))
poly('back-arm',(32,22),(22,18),(14,26));join('back-arm','torso')
line('front-arm',(32,22),(40,26));join('front-arm','torso');join('front-arm','back-arm')
poly('rear-leg',(24,30),(16,30),(12,38));join('rear-leg','torso')
path('board',(6,36),[('C',(32,42),(14,40),(24,42)),('C',(42,40),(37,42),(40,41))]);join('board','rear-leg');join('board','torso')
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
''','Current drawing used as reference. Raised rear arm lowered to clarify the crouched pose.')
add('person-with-round-hat-and-bob','VRECT_L','Rejected portrait resembles headphones and bib; restore round hat brim with flared bob hair beside circular face.','human_ref/user.svg: circular face and smooth shoulders; source bob silhouette', '''
path('hat',(8,22),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,22))])
oval('head',24,21,7,7)
for s in (-1,1):
 x=lambda d:24+s*d
 path(f'hair{s}',(x(16),22),[('C',(x(16),34),(x(12),28),(x(14),32)),('L',(x(10),36))]);join(f'hair{s}','hat')
path('body',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('head','body')
''','Bib and small hairline strokes omitted; hat and bob retained.')
add('personal-hotspot-connection','HRECT_M','Vertical dumbbell links replace the horizontal interlocked chain. Restore two offset horizontal open capsules.','No useful exact match; source capsule links and shared rounded construction.', '''
path('upper-link',(8,28),[('A',(14,10),10,10,True),('L',(30,10)),('A',(30,30),10,10,True),('L',(26,30))])
path('lower-link',(22,18),[('L',(18,18)),('A',(18,38),10,10,False),('L',(34,38)),('A',(42,22),10,10,False)])
''')
# Repairs of the first six keep the owning contour and repeat definitions together.
D['hand-expansion-touch-gesture']['code']=D['hand-expansion-touch-gesture']['code'].replace("('L',(30,34)),('L',(32,34)),('L',(32,40))","('L',(30,32)),('L',(32,32)),('L',(32,40))").replace('(8,18),(4,22),(8,26)','(8,16),(4,20),(8,24)')
D['hand-swiping-up-gesture']['code']=D['hand-swiping-up-gesture']['code'].replace("(36,20),[('A',(36,40),8,10,True)]","(38,20),[('A',(38,40),6,10,True)]")
D['happy-chat-bubbles']['code']=D['happy-chat-bubbles']['code'].replace('(26,33)','(28,33)').replace('(26,24)','(28,24)').replace('(30,37)','(32,37)').replace('(30,20)','(32,20)').replace('4,4,True),\n','4,4,True),\n')
D['keypad-office-telephone']['code']=D['keypad-office-telephone']['code'].replace('(31,14)','(31,15)').replace('(17,14)','(17,15)').replace('(12,26)','(8,26)').replace('(36,26)','(40,26)')
D['interrupted-overlapping-square-outlines']['code']=D['interrupted-overlapping-square-outlines']['code'].replace("(38,18)","(39,18)").replace("('L',(39,18)),",'').replace('(30,26),(30,30),(26,30)','(30,27),(30,30),(27,30)')
D['kimono-sash-belt']['code']=D['kimono-sash-belt']['code'].replace("12,10,36,38","11,10,37,38").replace('(12,16)','(11,16)').replace('(12,32)','(11,32)').replace('(36,16)','(37,16)').replace('(36,32)','(37,32)')
if __name__=='__main__':
 import author
 author.D=D;generate(sys.argv[1:])
