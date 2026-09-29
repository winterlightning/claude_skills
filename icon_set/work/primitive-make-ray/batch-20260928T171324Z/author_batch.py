from engine import *
def add(n,key,problem,change,code,ref,omissions='None.'):
    SPECS[n]=dict(keyshape=key,problem=problem,change=change,code=textwrap.dedent(code).strip(),construction_reference=ref,omissions=omissions)
add(1,'SQUARE','The rejected heart has a deep angular cleft and uneven flanks; the feedback explicitly asks to fix the heart.','Rebuilt a balanced heart with paired smooth lobes and a clean lower point; retained the piercing diagonal arrow.', '''
# Heart owns shared arrow contact nodes (34,16) and (14,34).
self.path('heart',(21,15),[('C',(13,10),(18,12),(16,10)),('C',(6,20),(8,10),(6,14)),('C',(14,34),(6,26),(10,30)),('L',(21,40)),('C',(36,20),(29,33),(36,26)),('C',(34,16),(36,18),(35,17)),('C',(29,10),(33,12),(31,10)),('C',(21,15),(26,10),(23,12))],True)
self.add_polyline('arrow-front',(28,22),(34,16),(42,8),(42,6))
self.add_polyline('arrow-head',(34,6),(42,6),(42,14))
self.relate('connect','heart','arrow-front');self.relate('connect','arrow-front','arrow-head')
self.add_polyline('arrow-tail',(6,42),(12,36),(14,34))
self.add_polyline('feather',(6,36),(12,36),(12,42))
self.relate('connect','heart','arrow-tail');self.relate('connect','arrow-tail','feather')
''','Lucide heart: paired lobes flowing into tapered sides; source: diagonal arrow.','Fine closed feather panels replaced by two clear fletching strokes.')
add(2,'HRECT_L','The eye is rounder than the reference, and the diagonal crosses without stable shared geometry.','Restored a flatter almond with a straight ascending slash and exact shared crossing nodes.', '''
self.path('eye',(4,24),[('C',(24,10),(10,16),(17,10)),('C',(34,14),(28,10),(32,12)),('C',(44,24),(38,17),(41,20)),('C',(24,38),(38,32),(31,38)),('C',(14,34),(20,38),(16,36)),('C',(4,24),(10,31),(7,28))],True)
self.add_polyline('slash',(8,40),(14,34),(34,14),(40,8))
self.relate('connect','eye','slash')
''','Lucide eye-off: almond silhouette and diagonal state stroke; supplied source uses the opposite slash direction and no pupil.')
add(3,'VRECT_M','The current thermometer has a thick bulb and broad column, equal stub ticks, and a solid-looking mercury bulb.','Slimmed the stem, restored a small outlined mercury bulb and differentiated long and short scale ticks.', '''
self.path('outline',(14,10),[('A',(26,10),6,6,True),('L',(26,26)),('C',(30,35),(29,29),(30,32)),('A',(20,44),10,9,True),('A',(10,35),10,9,True),('C',(14,26),(10,32),(11,29)),('L',(14,10))],True)
self.circle('mercury-bulb',20,34,3)
self.add_line('mercury',(20,12),(20,31));self.relate('connect','mercury','mercury-bulb')
for j,(x,y) in enumerate(((34,8),(36,17),(34,26))):self.add_line(f'tick-{j}',(x,y),(38,y))
''','Lucide thermometer: rounded connected stem and bulb; source: high mercury and three alternating-length ticks.')
add(4,'HRECT_M','The displayed ruler is a chunky rectangle with four ticks; the reference is a slender ruler with five ticks.','Restored a shallow rounded ruler and all five equally spaced top graduations.', '''
top,bottom=17,31
self.path('case',(7,top),[('L',(10,top)),('L',(17,top)),('L',(24,top)),('L',(31,top)),('L',(38,top)),('L',(41,top)),('A',(44,20),3,3,True),('L',(44,28)),('A',(41,bottom),3,3,True),('L',(7,bottom)),('A',(4,28),3,3,True),('L',(4,20)),('A',(7,top),3,3,True)],True)
for j in range(5):
    x=10+7*j;self.add_line(f'tick-{j}',(x,top),(x,23));self.relate('connect','case',f'tick-{j}')
''','Lucide ruler: repeated edge graduations and rounded case; source controls horizontal proportions.')
add(5,'VRECT_L','The current glass closes into an X and lacks the narrow open neck and projecting end caps of the source.','Opened the waist, restored curved chambers and added short projecting top and bottom caps.', '''
self.path('glass',(12,4),[('L',(36,4)),('L',(36,12)),('C',(28,24),(36,18),(28,19)),('C',(36,36),(28,29),(36,30)),('L',(36,44)),('L',(12,44)),('L',(12,36)),('C',(20,24),(12,30),(20,29)),('C',(12,12),(20,19),(12,18)),('L',(12,4))],True)
for y in (4,44):
    for a,b in ((8,12),(36,40)):
        n=f'cap-{y}-{a}';self.add_line(n,(a,y),(b,y));self.relate('connect','glass',n)
''','Lucide hourglass: paired chambers and projecting caps; source: continuous open waist.')
add(6,'VRECT_L','The current rocket looks bell-shaped: the fins merge into the body, the nose seam is missing and the exhaust is a small triangle.','Restored the pointed nose seam, straight hull, separately readable side fins, oval window and flowing exhaust.', '''
self.path('hull',(24,4),[('C',(34,14),(29,8),(33,11)),('L',(34,24)),('L',(34,36)),('L',(28,36)),('L',(20,36)),('L',(14,36)),('L',(14,24)),('L',(14,14)),('C',(24,4),(15,11),(19,8))],True)
self.add_line('nose-seam',(14,14),(34,14));self.relate('connect','hull','nose-seam')
self.path('window',(21,24),[('A',(27,24),3,4,True),('A',(21,24),3,4,True)],True)
for s in (-1,1):
    inner,outer=24+s*10,24+s*16;n=f'fin-{s}'
    self.add_polyline(n,(inner,24),(outer,32),(outer,36),(inner,36));self.relate('connect','hull',n)
self.path('flame',(20,36),[('C',(24,44),(20,40),(22,42)),('C',(28,36),(26,42),(28,40))])
self.relate('connect','flame','hull')
''','Lucide rocket: pointed hull, explicit fins and rounded window; original: upright symmetric layout.','Exhaust reduced to one clear flame instead of three disconnected wisps.')
add(7,'SQUARE','The target circle is horizontally compressed and the arrow is too dominant relative to the source node.','Made the outer target rounder, enlarged its left node and reduced the arrow to a balanced centered control.', '''
self.path('target',(10,17),[('C',(26,6),(13,10),(19,6)),('A',(44,24),18,18,True),('A',(26,42),18,18,True),('C',(10,31),(19,42),(13,38))])
self.circle('node',10,24,7);self.relate('connect','target','node')
self.add_polyline('arrow-head',(29,20),(25,24),(29,28))
self.add_line('arrow-shaft',(25,24),(35,24));self.relate('connect','arrow-head','arrow-shaft')
''','Lucide circle-arrow-left: circular boundary and compact arrow; original: attached left node.')
bulb='''
# Shared axis24, circular upper globe radius16, mirrored necks and equal socket corners.
self.path('bulb',(8,20),[('A',(40,20),16,16,True),('C',(30,36),(40,29),(31,29)),('L',(30,40)),('A',(26,44),4,4,True),('L',(22,44)),('A',(18,40),4,4,True),('L',(18,36)),('C',(8,20),(17,29),(8,29))],True)
self.add_line('socket-seam',(18,36),(30,36));self.relate('connect','bulb','socket-seam')
'''
for n in (8,14):add(n,'VRECT_L','The rejected bulb has a squat mushroom-like globe instead of the reference tall rounded bulb.','Restored a taller circular globe, smooth narrowing neck and rounded closed socket.',bulb,'Lucide lightbulb: circular glass transitioning to a narrow socket; source retains a closed base.')
for n,tops,bottoms in ((9,(18,30),(14,26)),(10,(22,38),(10,26))):
    add(n,'HRECT_M','The current loading bar is tall and boxy; the source has semicircular ends and a shallow capsule.','Restored a shallow capsule with true semicircular ends and two parallel stripes at the source-specific angle.',f'''
tops={tops};bottoms={bottoms}
commands=[('L',(x,18)) for x in tops if x!=10]
if tops[-1]!=38:commands.append(('L',(38,18)))
commands += [('A',(44,24),6,6,True),('A',(38,30),6,6,True)]
commands += [('L',(x,30)) for x in reversed(bottoms) if x!=38]
if bottoms[0]!=10:commands.append(('L',(10,30)))
commands += [('A',(4,24),6,6,True),('A',(10,18),6,6,True)]
self.path('capsule',(10,18),commands,True)
for j,(a,b) in enumerate(zip(tops,bottoms)):
    self.add_line(f'stripe-{{j}}',(a,18),(b,30));self.relate('connect','capsule',f'stripe-{{j}}')
''','No useful Lucide loading-bar match (loader is a spinner); source owns the capsule and stripes. Rounded enclosure technique follows the inspected smartphone reference.')
add(11,'VRECT_M','The lower phone band is missing and the wrench jaws point vertically rather than following its diagonal axis.','Restored the lower band, narrowed the handset and rebuilt diagonal open wrench jaws.', '''
self.phone(True)
self.path('jaw-bottom',(16,25),[('C',(22,25),(17,23),(20,23)),('C',(22,30),(24,27),(24,29))])
self.path('jaw-top',(26,14),[('C',(26,21),(24,16),(24,19)),('C',(32,20),(28,23),(31,22))])
self.add_line('shaft',(22,25),(26,21))
self.relate('connect','shaft','jaw-bottom');self.relate('connect','shaft','jaw-top')
''','Lucide smartphone: matched rounded frame; wrench: diagonal shaft and coherent open jaws.')
add(12,'SQUARE','The displayed barrel is lopsided and only one graduation remains; the source has a coherent rounded diagonal barrel and multiple marks.','Rebuilt the barrel as a balanced diagonal rounded shape, aligned needle and plunger and restored two graduations.', '''
self.path('barrel',(24,12),[('L',(30,18)),('L',(36,24)),('L',(21,39)),('C',(15,39),(19,41),(17,41)),('L',(12,36)),('L',(9,33)),('C',(9,27),(7,31),(7,29)),('L',(11,25)),('L',(16,20)),('L',(24,12))],True)
self.add_line('needle',(6,42),(12,36));self.relate('connect','needle','barrel')
self.add_line('plunger',(30,18),(38,10));self.relate('connect','plunger','barrel')
self.add_polyline('handle',(34,6),(38,10),(42,14));self.relate('connect','handle','plunger')
for j,(x,y) in enumerate(((11,25),(16,20))):
    self.add_line(f'tick-{j}',(x,y),(x+4,y+4));self.relate('connect','barrel',f'tick-{j}')
''','Lucide syringe: aligned diagonal barrel, plunger and needle with repeated graduation strokes.','Three reference marks reduced to two at 48 px.')
add(13,'VRECT_L','The mortarboard is reduced to a roof-like pentagon and the card is square; the reference has a diamond board and a lower crown on a portrait card.','Restored the complete diamond mortarboard over a curved crown within an upright rounded card.', '''
self.box('card',8,4,40,44,4)
self.add_polyline('board',(24,14),(34,20),(31,22),(24,26),(17,22),(14,20),closed=True)
self.path('crown',(17,22),[('L',(17,31)),('C',(24,34),(20,33),(22,34)),('C',(31,31),(26,34),(28,33)),('L',(31,22))])
self.relate('connect','board','crown')
''','Lucide graduation-cap: diamond board distinct from its curved crown; source: enclosing portrait card.')
add(15,'VRECT_M','The rejected map pin is short and broad with a tiny inner ring and an excessive gap above the ground.','Elongated the tapered pin, enlarged its circular opening and brought the ground line closer to its point.', '''
self.path('pin',(10,18),[('A',(38,18),14,14,True),('C',(24,38),(38,25),(29,34)),('C',(10,18),(19,34),(10,25))],True)
self.circle('opening',24,18,6)
self.add_line('ground',(16,44),(32,44))
''','Lucide map-pin: round cap, circular opening and taper to a centered point.')
add(16,'HRECT_M','The rejected open infinity loop is tall and narrow, reading like an S rather than the horizontal reference.','Flattened both lobes into a horizontal open infinity stroke with balanced paired curves.', '''
self.path('loop',(20,18),[('C',(12,12),(17,14),(15,12)),('C',(4,24),(7,12),(4,17)),('C',(12,36),(4,31),(7,36)),('C',(24,24),(17,36),(21,28)),('C',(36,12),(27,20),(31,12)),('C',(44,24),(41,12),(44,17)),('C',(36,36),(44,31),(41,36)),('C',(28,30),(33,36),(31,34))])
''','Lucide infinity: tangent loop curves joined by a diagonal transition; source keeps two open ends.')
add(17,'SQUARE','The plug and prongs dominate the current drawing and the cable loop is flattened and shortened.','Shortened the prongs, rebuilt a rounder cable loop and preserved an open cable end clear of the plug.', '''
self.path('plug',(26,4),[('L',(32,4)),('L',(32,6)),('L',(32,14)),('L',(32,16)),('L',(26,16)),('A',(20,10),6,6,True),('A',(26,4),6,6,True)],True)
for y in (6,14):
    self.add_line(f'prong-{y}',(32,y),(38,y));self.relate('connect','plug',f'prong-{y}')
self.path('cable',(20,10),[('C',(6,26),(12,10),(6,17)),('A',(24,44),18,18,False),('A',(42,26),18,18,False),('C',(42,24),(42,25),(42,25))])
self.relate('connect','cable','plug')
''','Lucide plug: rounded plug head and equal paired prongs; original: circular looping cable.')
battery='''
self.path('case',(8,14),[('L',(34,14)),('A',(38,18),4,4,True),('L',(38,20)),('L',(42,20)),('A',(44,22),2,2,True),('L',(44,26)),('A',(42,28),2,2,True),('L',(38,28)),('L',(38,30)),('A',(34,34),4,4,True),('L',(8,34)),('A',(4,30),4,4,True),('L',(4,18)),('A',(8,14),4,4,True)],True)
'''
add(18,'HRECT_M','The battery is too tall and its charge marks dominate the interior; the source has a wider body and two low-charge marks grouped left.','Restored a wider battery silhouette, integrated rounded terminal and two compact left-aligned charge marks.',battery+'''
for x in (12,20):self.add_line(f'charge-{x}',(x,20),(x,28))
''','Lucide battery-low: rounded body and left charge mark; source: two marks and integrated terminal.')
add(19,'HRECT_M','The current low battery is tall and boxy relative to the wide source.','Made the body shallower, rounded its terminal transitions and retained one clear left-side charge mark.',battery+'''
self.add_line('charge',(12,20),(12,28))
''','Lucide battery-low: rounded outline and minimal left charge indicator.')
add(20,'HRECT_M','The rejected charge block has become a single stroke and the battery is too tall.','Restored the outlined low-charge block, a shallower case and a separately outlined rounded terminal.', '''
self.path('case',(8,14),[('L',(32,14)),('A',(36,18),4,4,True),('L',(36,20)),('L',(36,28)),('L',(36,30)),('A',(32,34),4,4,True),('L',(8,34)),('A',(4,30),4,4,True),('L',(4,18)),('A',(8,14),4,4,True)],True)
self.path('terminal',(36,20),[('L',(42,20)),('A',(44,22),2,2,True),('L',(44,26)),('A',(42,28),2,2,True),('L',(36,28))])
self.relate('connect','case','terminal')
self.add_polyline('charge',(12,20),(20,20),(20,28),(12,28),closed=True)
''','Lucide battery-low: rounded case; supplied source specifically requires an outlined charge block.')
if __name__=='__main__':
    records=[author(n,'r1') for n in range(1,21)]
    (Path(__file__).parent/'runs.json').write_text(json.dumps(records,indent=2))
