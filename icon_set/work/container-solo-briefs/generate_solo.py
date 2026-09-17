"""Source-specific native SOLO48 authoring for container sub-icon briefs."""
from pathlib import Path
import json, re, textwrap
SOURCE_ICON_ID = None  # Per-icon values are emitted below from the brief inventory.
SOURCE_PATH = 'icon_set/work/container-solo-briefs/briefs.json'
AUTHOR = 'gpt-6'
ROOT=Path(__file__).resolve().parents[3]
rows=json.loads((ROOT/SOURCE_PATH).read_text())
D={}
def add(i,name,shape,plan,code,ref=None): D[i]=(name,shape,plan,textwrap.dedent(code).strip(),ref)
add(0,'active-sporting-figure','SQUARE','A leaning active stick figure; circular head and crossed extended arms. Head follows the vertical tangent of the curved upper torso.', '''
circle('head',34,11,5)
self.add_bezier('torso',(34,24),((34,28),(28,32),(24,32)))
poly('arms',(6,24),(34,24),(42,24))
poly('legs',(6,42),(24,32),(30,42))
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(1,'airplane-flying-over-globe','SQUARE','Open globe behind a diagonal passenger airplane; equator and meridian preserve globe identity.', '''
circle('globe',16,16,10)
poly('latitude',(6,16),(16,16),(26,16))
poly('longitude',(16,6),(16,16),(16,26))
poly('fuselage',(28,42),(34,36),(42,28))
poly('wings',(27,31),(34,36),(40,42))
line('tail',(24,42),(28,42))
''','plane, earth')
add(3,'three-toed-animal-paw','SQUARE','Three circular toe pads above a smooth rounded central pad; bilateral symmetry.', '''
circle('toe-top',24,10,4)
circle('toe-left',10,19,4)
circle('toe-right',38,19,4)
path('pad',(24,27),('C',(19,27),(20,32),(15,34)),('C',(6,42),(15,42),(24,42)),('C',(33,42),(42,42),(33,34)),('C',(28,32),(29,27),(24,27)),closed=True)
''')
add(4,'diagonal-arrow-pointing-to-dot','SQUARE','One southwest-pointing straight arrow and a detached destination dot; deliberate diagonal.', '''
line('shaft',(42,6),(15,33))
poly('head',(15,21),(15,33),(27,33))
self.add_dot('destination',(6,42))
''')
add(8,'biometric-fingerprint','SQUARE','Nested fingertip arches and interrupted ridge tails; shared axis and clear ridge spacing.', '''
path('outer',(6,30),('L',(6,24)),('A',18,18,True,(42,24)),('L',(42,30)))
path('inner',(14,36),('C',(16,30),(15,24),(16,22)),('C',(16,13),(33,13),(33,22)),('L',(33,30)),('C',(33,36),(34,39),(36,42)))
path('ridge',(24,26),('C',(24,32),(24,38),(20,42)))
''')
add(14,'close-and-cancel-symbol','SQUARE','Two diagonal strokes cross at the shared center.', '''
poly('falling',(6,6),(24,24),(42,42))
poly('rising',(6,42),(24,24),(42,6))
''','x')
add(15,'crescent-moon-with-cross-star','SQUARE','Crescent night moon and a four-armed star in its opening; the cross is a celestial star per saved brief.', '''
path('moon',(26,6),('C',(14,6),(6,14),(6,26)),('C',(6,36),(14,42),(24,42)),('C',(32,42),(38,38),(42,30)),('C',(29,35),(17,21),(26,6)),closed=True)
poly('star-horizontal',(33,14),(38,14),(42,14))
poly('star-vertical',(38,10),(38,14),(38,18))
''','moon-star')
add(19,'digital-facial-recognition','VRECT_L','Symmetric face outline, scan cross through upper face, and curved smile. The cross is the scan detail.', '''
path('face',(8,20),('A',16,16,True,(40,20)),('L',(40,28)),('A',16,16,True,(8,28)),('L',(8,20)),closed=True)
line('scan-horizontal',(8,20),(40,20))
line('scan-vertical',(24,4),(24,24))
path('smile',(19,32),('C',(22,35),(26,35),(29,32)))
''','scan-face')
add(20,'downward-trend-arrow','HRECT_L','Three descending trend segments with arrowhead sharing the endpoint.', '''
poly('trend',(4,8),(17,22),(26,13),(44,40))
poly('arrowhead',(32,40),(44,40),(44,28))
''','trending-down')
for i,name in [(21,'emergency-medical-first-aid-kit'),(22,'first-aid-medical-case')]:
 add(i,name,'SQUARE','Rounded medical case and raised handle; centered medical cross with generous interior spacing.', '''
box('case',6,14,42,42,4,xs=(16,32))
path('handle',(16,14),('L',(16,10)),('A',4,4,True,(20,6)),('L',(28,6)),('A',4,4,True,(32,10)),('L',(32,14)))
poly('cross-h',(18,28),(24,28),(30,28))
poly('cross-v',(24,23),(24,28),(24,33))
''','briefcase-medical')
add(23,'front-view-bathroom-toilet','VRECT_L','Front-view cistern above a broad bowl and tapered pedestal; shared bowl rim.', '''
poly('tank',(14,24),(12,4),(36,4),(34,24))
path('bowl',(8,24),('L',(40,24)),('C',(40,33),(34,34),(32,36)),('L',(35,44)),('L',(13,44)),('L',(16,36)),('C',(14,34),(8,33),(8,24)),closed=True)
''','toilet')
add(24,'geometric-three-toed-paw','SQUARE','Three equal circles and one triangular pad; mirrored toes and centered triangle.', '''
circle('top-toe',24,10,4)
circle('left-toe',10,22,4)
circle('right-toe',38,22,4)
poly('pad',(24,26),(12,42),(36,42),closed=True)
''')
add(25,'happy-face-with-closed-eyes','SQUARE','Two mirrored arched eyes and a wide smile, without an enclosing face circle.', '''
path('left-eye',(6,14),('A',6,8,True,(18,14)))
path('right-eye',(30,14),('A',6,8,True,(42,14)))
path('smile',(8,28),('A',16,14,False,(40,28)))
''','smile')
add(30,'horned-bull-head','VRECT_L','Broad symmetric bull face, tapered muzzle and upward horns. Omit eyes to protect negative space.', '''
path('face',(12,24),('C',(12,13),(36,13),(36,24)),('L',(36,32)),('L',(29,37)),('L',(29,39)),('A',5,5,True,(19,39)),('L',(19,37)),('L',(12,32)),('L',(12,24)),closed=True)
path('horn-left',(12,24),('C',(8,23),(8,20),(8,16)),('L',(8,4)))
path('horn-right',(36,24),('C',(40,23),(40,20),(40,16)),('L',(40,4)))
''')
add(33,'judicial-gavel-and-block','SQUARE','Diagonal rectangular hammer head, long handle, and separate low sounding block.', '''
poly('head',(6,17),(18,6),(30,18),(18,30),closed=True)
line('handle',(24,24),(42,42))
poly('block',(6,42),(6,38),(20,38),(20,42))
''','gavel')
add(34,'two-left-aligned-text-lines','HRECT_L','Two horizontal lines share their left origin; lower line is shorter.', '''
line('first',(4,8),(44,8))
line('second',(4,40),(30,40))
''')
add(35,'three-left-aligned-text-lines','HRECT_L','Three evenly spaced horizontal lines share left alignment and alternate length.', '''
for n,y,end in [('top',8,44),('middle',24,33),('bottom',40,44)]:line(n,(4,y),(end,y))
''')
add(36,'speaker-with-one-sound-wave','HRECT_L','Speaker horn and one detached circular sound arc; no extra outer wave.', '''
poly('speaker',(4,18),(12,18),(26,8),(26,40),(12,30),(4,30),closed=True)
path('wave',(36,12),('A',8,12,True,(36,36)))
''','volume-1')
add(38,'minimal-happy-smiling-face','HRECT_L','Two vertical eyes above one broad smile, without added face enclosure.', '''
line('left-eye',(12,8),(12,14));line('right-eye',(36,8),(36,14))
path('smile',(4,26),('A',20,14,False,(44,26)))
''','smile')
add(42,'person-digging-with-shovel','SQUARE','Forward-leaning worker grips diagonal shovel; circular head and spread legs preserve digging pose.', '''
circle('head',29,11,5)
self.add_bezier('torso',(29,24),((29,30),(22,34),(16,34)))
poly('arms',(29,24),(34,30))
poly('legs',(6,42),(16,34),(22,42))
poly('shaft',(6,24),(29,24),(34,34))
poly('spade',(34,34),(40,30),(42,42),(30,40),closed=True)
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(44,'person-in-car-seat','SQUARE','Seated figure with circular head, bent knees and supporting seat back; exact detached head gap.', '''
path('head',(24,16),('A',5,5,True,(24,6)),('A',5,5,True,(24,16)),closed=True)
line('torso',(24,24),(24,32))
poly('legs',(24,32),(34,32),(42,40))
poly('arm',(24,24),(33,24),(39,18))
path('seat',(6,23),('L',(6,34)),('A',8,8,False,(14,42)),('L',(32,42)))
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(45,'person-at-information-stand','SQUARE','Standing reader beside a small sign on a tall post; bent arm points toward sign.', '''
box('sign',6,6,18,16,2,xs=(12,))
line('post',(12,16),(12,42))
circle('head',36,10,4)
line('torso',(36,22),(36,32))
poly('arm',(36,22),(28,27),(24,22))
poly('legs',(27,42),(36,32),(42,42))
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(49,'person-with-presentation-board','HRECT_L','Presenter bust beside a blank board; person and board retained from the saved standalone scene brief.', '''
box('board',4,8,20,22,2)
circle('head',36,16,5)
path('shoulders',(28,40),('L',(28,33)),('A',8,8,True,(44,33)),('L',(44,40)))
self.human_construction = 'bust'
self.relate('connect','head','shoulders')
''','user')
add(50,'pie-chart-with-summary-lines','HRECT_L','Three-sector pie at left, two short summary rules at right; descriptive marks are not typeface glyphs.', '''
path('chart',(28,24),('A',12,16,True,(16,40)),('A',12,16,True,(4,24)),('A',12,16,True,(16,8)),('A',12,16,True,(28,24)),closed=True)
poly('sectors',(16,8),(16,24),(28,24))
line('third',(16,24),(7,35))
line('summary-top',(37,17),(44,17));line('summary-bottom',(37,31),(44,31))
''','chart-pie')
add(52,'prohibition-sign-solo','CIRCLE','Circle with a continuous diagonal strike; shared endpoints at integer circle points.', '''
path('ring',(12,8),('A',20,20,True,(40,12)),('A',20,20,True,(36,40)),('A',20,20,True,(8,36)),('A',20,20,True,(12,8)),closed=True)
line('slash',(8,36),(40,12))
''')
add(54,'three-rising-steam-waves','SQUARE','Three identical vertical S-curves with a shared 14-unit repeat spacing.', '''
for n,x in enumerate((10,24,38)):
 path(f'wave-{n}',(x+4,6),('C',(x-9,18),(x+9,30),(x-4,42)))
''','waves')
add(55,'selection-list-with-checkmark','HRECT_L','Two rows of list dots with a large selection tick at the upper right; no enclosing checklist box.', '''
for row,y in enumerate((8,40)):
 for col,x in enumerate((4,16,28)):
  if row==0 and col==2:continue
  self.add_dot(f'mark-{row}-{col}',(x,y))
poly('check',(30,17),(35,22),(44,8))
self.add_dot('last',(44,40))
''')
add(59,'standing-human-figure','VRECT_M','Circular head and compact shirt-like body with short squared sleeves and tapered base; exact head gap.', '''
circle('head',24,10,6)
path('body',(10,32),('A',14,8,True,(24,24)),('A',14,8,True,(38,32)),('L',(38,35)),('L',(32,35)),('L',(30,44)),('L',(18,44)),('L',(16,35)),('L',(10,35)),('L',(10,32)),closed=True)
''')
add(63,'single-roasted-coffee-bean','VRECT_L','Oval coffee bean with a long S-shaped seam; mirrored hull and coherent seam.', '''
ellipse(self,'bean',24,24,16,20)
path('seam',(24,4),('C',(35,16),(13,32),(24,44)))
''','coffee')
add(64,'six-dot-drag-handle','HRECT_L','Six round dots, two evenly spaced rows of three; no enclosing border.', '''
for row,y in enumerate((8,40)):
 for col,x in enumerate((4,24,44)):self.add_dot(f'dot-{row}-{col}',(x,y))
''','grip')
add(69,'swimmer-with-cap-and-water','SQUARE','Capped swimmer bust over water; one head, shoulder curve, and a single wave.', '''
circle('head',24,15,9)
line('cap',(15,15),(33,15))
path('shoulders',(14,32),('A',10,4,True,(24,28)),('A',10,4,True,(34,32)))
path('water',(6,42),('C',(12,42),(12,40),(18,40)),('C',(24,40),(24,42),(30,42)),('C',(36,42),(36,40),(42,40)))
self.human_construction='bust'
self.relate('connect','head','shoulders')
''')
add(71,'text-wrap-right-layout','HRECT_L','Right-side rectangular object and left/underneath text rules; wide document layout.', '''
box('object',28,8,44,24,0)
line('short-top',(4,8),(18,8));line('short-middle',(4,24),(18,24))
line('bottom',(4,40),(44,40))
''')
add(73,'three-segment-pie-chart','CIRCLE','Circle divided into three unequal sectors by up, right, and lower-left spokes.', '''
path('pie',(24,4),('A',20,20,True,(44,24)),('A',20,20,True,(24,44)),('A',20,20,True,(12,40)),('A',20,20,True,(4,24)),('A',20,20,True,(24,4)),closed=True)
poly('upper',(24,4),(24,24),(44,24))
line('lower',(24,24),(12,40))
''','chart-pie')
for i,name in [(76,'two-people-figures'),(77,'two-person-user-group')]:
 add(i,name,'HRECT_M','Two equal outlined heads and open shoulder arches, horizontally repeated without merging bodies.', '''
for n,cx in enumerate((12,36)):
 circle(f'head-{n}',cx,14,4)
 path(f'body-{n}',(cx-8,38),('L',(cx-8,30)),('A',8,8,True,(cx+8,30)),('L',(cx+8,38)))
 self.relate('connect',f'head-{n}',f'body-{n}')
self.human_construction='bust'
''','users')
add(78,'two-prong-electrical-plug','VRECT_L','Two equal plug pins, bowl-shaped plug body and short central cord.', '''
path('body',(8,16),('L',(16,16)),('L',(32,16)),('L',(40,16)),('L',(40,25)),('A',16,11,True,(24,36)),('A',16,11,True,(8,25)),('L',(8,16)),closed=True)
line('left-pin',(16,4),(16,16));line('right-pin',(32,4),(32,16))
line('cord',(24,36),(24,44))
''','plug')
# Emit new source-specific modules, never overwrite a different source module.
written=[]
for i,(name,shape,plan,code,ref) in D.items():
 r=rows[i];uid=r['uuid'];filename=name.replace('-','_')+'_'+uid.replace('-','_')+'.py'
 p=ROOT/'icon_set/model/icons/solo'/filename
 meta=f'''"""{r['concept']}.\nPlan: {plan}\nReferences: supplied source; {('Lucide original and atomic-debug '+ref) if ref else 'no useful exact Lucide match'}.\nNative SOLO48 construction, no cross-family scaling.\n"""\nfrom ...keyshapes import Keyshape\nfrom ._base import Solo48\nfrom ._symmetry_curves import path as _path, ellipse, box as _box, contacts\nSOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {r['source_path']!r}\nAUTHOR = 'gpt-6'\n\nclass Drawing(Solo48):\n    icon_id = {name!r}\n    keyshape = Keyshape.{shape}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'objects/container-components'\n    aliases = ()\n    keywords = {tuple(dict.fromkeys(['sub icon']+name.split('-')))!r}\n    def build(self):\n        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)\n        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)\n        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)\n        line, poly = self.add_line, self.add_polyline\n'''
 # radius zero uses polyline rather than degenerate arc helper
 code=code.replace("box('object',28,8,44,24,0)","poly('object',(28,8),(44,8),(44,24),(28,24),closed=True)")
 p.write_text(meta+textwrap.indent(code,'        ')+'\n        contacts(self)\n')
 written.append({'index':i,'uuid':uid,'icon_id':name,'module':str(p),'plan':plan,'reference':ref})
(ROOT/'icon_set/work/container-solo-briefs/new-models.json').write_text(json.dumps(written,indent=2))
print('Authored',len(written),'models')
