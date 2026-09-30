from author import author
H='Human full_body_ref.png: circular heads and exact 4-unit detached head gap'
author(5,'''
path('face',(10,24),[('L',(10,18)),('A',(38,18),14,14,True),('L',(38,24)),('L',(38,30)),('A',(10,30),14,14,True),('L',(10,24))],True)
line('ear-left',(8,24),(10,24));line('ear-right',(38,24),(40,24));join('ear-left','face');join('ear-right','face')
self.add_dot('eye-left',(19,17));self.add_dot('eye-right',(29,17))
path('smile',(18,28),[('L',(30,28)),('A',(18,28),6,6,True)],True)
''','The rejected Saitama head was a generic round smiley. Restored the taller bald head and lower jaw proportions with small ears, understated eyes and an open smile. Omitted the fine nose and brows.','VRECT_L','Human user.svg: rounded head; Lucide face-slightly-smiling: sparse facial placement')
author(6,'''
path('pad',(10,18),[('A',(38,18),14,14,True),('L',(38,30)),('A',(10,30),14,14,True),('L',(10,18))],True)
path('panel',(20,18),[('A',(28,18),4,4,True),('L',(28,30)),('A',(20,30),4,4,True),('L',(20,18))],True)
''','The rejected diagonal pad was almost circular, with a short central opening. Reoriented it upright and elongated both the outer pad and inset absorbent panel so it reads as a pad.','VRECT_M','Lucide pill: tangent capsule ends; supplied reference: nested absorbent panel')
author(7,'''
path('fleece',(12,10),[('A',(24,10),6,4,True),('A',(36,10),6,4,True),('L',(38,12)),('A',(38,24),4,6,True),('A',(38,36),4,6,True),('L',(36,38)),('A',(24,38),6,4,True),('A',(12,38),6,4,True),('L',(10,36)),('A',(10,24),4,6,True),('A',(10,12),4,6,True),('L',(12,10))],True)
path('face',(19,19),[('L',(29,19)),('L',(29,26)),('A',(19,26),5,5,True),('L',(19,19))],True)
''','The rejected fleece looked like a rounded square with four notches. Restored repeated scallops around all four sides and retained a plain rounded face opening. Reduced the number of wool lobes to eight.',lucide='No useful direct Lucide match; shared elliptical scallops follow the source fleece')
author(8,'''
path('beaver',(14,32),[('C',(10,21),(10,29),(10,24)),('C',(28,14),(10,11),(21,14)),('C',(32,8),(28,10),(29,8)),('C',(36,12),(35,8),(36,10)),('C',(44,20),(41,13),(44,16)),('C',(36,25),(44,24),(40,25)),('L',(36,32)),('L',(40,32)),('A',(40,40),4,4,True),('L',(22,40)),('C',(14,32),(18,40),(14,37))],True)
path('tail',(14,32),[('L',(8,32)),('A',(8,40),4,4,False),('L',(22,40))]);join('tail','beaver')
''','The rejected beaver had a pointed muzzle and square forward foot. Rounded the muzzle into the chest and the forward foot while retaining the seated haunch, small ear and flat tail. Omitted tiny eye and claw lines.','HRECT_L','No useful direct Lucide beaver match; source rounded muzzle and seated haunch')
author(9,'''
path('dog',(24,6),[('C',(30,14),(28,6),(29,10)),('L',(34,14)),('C',(42,20),(38,18),(42,18)),('C',(34,28),(42,26),(38,28)),('L',(34,38)),('A',(38,42),4,4,False),('L',(24,42)),('L',(18,42)),('A',(10,34),8,8,True),('C',(22,18),(10,26),(20,25)),('C',(24,6),(24,14),(22,9))],True)
path('tail',(10,34),[('A',(6,26),4,8,True),('L',(6,20))]);join('tail','dog')
line('front-leg',(24,30),(24,42));join('front-leg','dog')
''','The rejected dog had a sharp triangular ear and angular back. Restored a rounded upright ear, flowing shoulder and softer muzzle while retaining the seated legs and raised tail.',lucide='Lucide dog: smooth muzzle and ears; supplied reference owns the seated profile')
author(10,'''
circle('head',24,9,5)
path('shoulders',(12,36),[('L',(12,26)),('A',(16,22),4,4,True),('L',(24,22)),('L',(32,22)),('A',(36,26),4,4,True),('L',(36,36))])
poly('left-leg',(12,36),(12,40),(12,44),(20,44));join('left-leg','shoulders')
poly('right-leg',(36,36),(36,44),(28,44));join('right-leg','shoulders')
line('belt',(36,26),(12,40));join('belt','shoulders');join('belt','left-leg')
line('seat-left',(8,36),(12,36));line('seat-right',(36,36),(40,36));join('seat-left','shoulders');join('seat-right','shoulders');join('seat-left','left-leg');join('seat-right','right-leg')
''','The rejected seated body looked like a square crossed-out symbol. Rounded the shoulders around the detached head and preserved the diagonal seatbelt, hanging legs and seat edges. Head outline y14 to shoulders y22 leaves exactly four ink units.','VRECT_L','Human user.svg: rounded shoulders and detached circular head; source diagonal restraint')
author(11,'''
path('rabbit',(14,22),[('L',(10,11)),('A',(20,11),5,5,True),('L',(22,20)),('L',(30,20)),('L',(28,11)),('A',(38,11),5,5,True),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,30)),('L',(34,34)),('L',(38,42)),('L',(14,42)),('A',(6,34),8,8,True),('A',(14,22),8,12,True)],True)
''','The rejected rabbit had two rigid vertical antenna-like ears. Tilted and rounded the ears to follow the reference direction while retaining its broad seated body and muzzle. Omitted the eye and small hind-leg loop.',lucide='Lucide rabbit: backward-leaning rounded ears and seated haunch')
author(12,'''
path('head',(6,24),[('A',(42,24),18,18,True),('C',(38,36),(42,30),(40,34))])
path('left-cheek',(6,24),[('C',(16,40),(6,34),(10,40))]);join('head','left-cheek')
path('hand',(22,42),[('L',(24,30)),('A',(32,30),4,4,True),('L',(32,36)),('L',(34,36)),('A',(38,40),4,4,True),('L',(38,42))]);join('hand','head')
self.add_dot('eye-left',(17,18));self.add_dot('eye-right',(31,18))
''','The rejected shushing hand was a squared arch with a rigid wrist. Tilted the raised index finger slightly and rounded the curled hand to restore the natural shushing gesture. Kept the lower face open around the hand.',lucide='Human user.svg: round head vocabulary; source-specific raised finger construction')
author(13,'''
path('fan',(6,10),[('A',(18,10),6,4,True),('A',(30,10),6,4,True),('A',(42,10),6,4,True),('L',(30,36)),('L',(18,36)),('L',(6,10))],True)
line('feather-left',(18,10),(20,23));line('feather-right',(30,10),(28,23));join('feather-left','fan');join('feather-right','fan')
path('cork',(18,36),[('A',(30,36),6,6,False)]);join('cork','fan')
''','The rejected shuttlecock had a flat fan edge and short internal stubs. Rounded the three feather tips, extended the feather separations and retained the rounded cork. Kept an upright arrangement for clear spacing.',lucide='No useful direct Lucide shuttlecock match; repeated rounded feather tips follow the original')
author(14,'''
for x in (14,34):circle(f'head-{x}',x,14,6)
path('left-body',(4,40),[('L',(4,38)),('A',(14,28),10,10,True)])
path('right-body',(34,28),[('A',(44,38),10,10,True),('L',(44,40))])
path('embrace',(14,28),[('L',(31,37)),('A',(35,35),3,3,False)]);join('embrace','left-body')
''','The rejected embrace was one straight diagonal stroke ending loosely. Curved the embracing arm into a rounded hand reaching across the other person, keeping the adjacent heads and broad shoulders. Both detached heads retain four ink units to their own shoulders.','HRECT_L','Human user.svg: round heads and broad shoulders; source arm crossing its neighbor')
author(15,'''
path('body',(8,31),[('L',(4,31)),('L',(4,22)),('A',(8,18),4,4,True),('L',(16,18)),('L',(24,10)),('L',(32,10)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,31)),('L',(40,31))])
circle('wheel-left',12,34,4);circle('wheel-right',36,34,4)
line('sill',(16,34),(32,34));join('sill','wheel-left');join('sill','wheel-right')
poly('hood',(16,18),(8,10),(4,10));join('hood','body')
''','The rejected car body floated far above its wheels and the hood was a short stub. Lowered and rounded the body around larger wheels, joined them with the sill, and gave the raised hood a clear hinged angle.','HRECT_M','Lucide car: wheels nested into an open lower body outline')
author(16,'''
for name,x in [('left',9),('right',39)]:
 circle(name+'-head',x,15,3)
 line(name+'-torso',(x,26),(x,32))
 poly(name+'-arms',(x-5,29),(x,26),(x+5,29));join(name+'-arms',name+'-torso')
 if name=='left':poly(name+'-legs',(x-4,40),(x,32),(x+4,40));join(name+'-legs',name+'-torso')
 else:
  poly('skirt',(34,38),(39,28),(44,38),(34,38));join('skirt','right-torso')
  line('leg-left',(36,38),(36,40));line('leg-right',(42,38),(42,40));join('leg-left','skirt');join('leg-right','skirt')
 self.mark_human_figure(name,head=name+'-head',torso=name+'-torso',torso_junction='start')
circle('note',23,18,2);poly('stem',(25,18),(25,8),(29,10));join('stem','note')
''','The rejected duet replaced both differently dressed singers with identical stick figures. Restored a skirt on the right singer while retaining the left trousered figure and a central musical note. Reduced two notes to one for spacing.','HRECT_L',H+'; Lucide music-2: note head, stem and flag')
author(17,'''
path('fruit',(24,20),[('A',(40,32),16,12,True),('A',(24,44),16,12,True),('A',(8,32),16,12,True),('A',(24,20),16,12,True)],True)
poly('stem',(24,20),(24,12),(20,4));join('stem','fruit')
path('leaf',(24,12),[('C',(40,4),(26,4),(34,4)),('C',(24,12),(38,12),(30,14))],True);join('leaf','stem')
''','The rejected tangerine was a very flat oval beneath an oversized leaf. Enlarged the fruit vertically and reduced the leaf and stem to restore a rounder fruit-dominant silhouette.','VRECT_L','Lucide sprout: pointed leaf attached at a stem node')
author(18,'''
poly('staff',(24,4),(24,12),(24,28),(24,44))
path('snake',(40,12),[('L',(24,12)),('C',(8,20),(12,12),(8,14)),('C',(24,28),(8,26),(15,28)),('C',(38,35),(35,28),(38,30)),('C',(24,42),(38,40),(28,42))]);join('snake','staff')
path('head',(32,12),[('A',(40,12),4,4,True)]);join('head','snake')
''','The rejected serpent was an undifferentiated S-shaped stroke resembling a currency symbol. Added a rounded snake head and lengthened the lower coil while keeping a single serpent around the upright staff. Omitted the tiny eye and staff finial.','VRECT_L','No useful direct Lucide match; source single winding serpent and upright staff')
author(19,'''
path('bird',(6,15),[('L',(12,11)),('C',(21,6),(13,8),(17,6)),('C',(30,15),(27,6),(30,9)),('C',(42,27),(36,19),(42,20)),('C',(24,34),(42,33),(31,34)),('C',(10,23),(15,34),(10,30)),('L',(10,18)),('L',(6,15))],True)
path('wing',(20,20),[('C',(30,25),(20,25),(26,25))])
poly('leg-left',(18,33),(18,40),(14,42));poly('leg-right',(32,33),(32,40),(28,42));join('leg-left','bird');join('leg-right','bird')
''','The rejected bird had a flat belly, long rigid legs and a tiny hooked wing. Rounded the belly, shortened and bent the legs, and broadened the folded wing into a smooth curve. Omitted the tiny eye.',lucide='Lucide bird: rounded body and flowing folded-wing curve')
