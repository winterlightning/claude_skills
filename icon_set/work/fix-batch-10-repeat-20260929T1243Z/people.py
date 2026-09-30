from author import make
bun='''
path('hair',(12,24),[('A',(18,14),6,10,True),('L',(18,12)),('A',(30,12),6,8,True),('L',(30,14)),('A',(36,24),6,10,True)])
self.add_arc('jaw',(12,24),(36,24),radius_x=12,sweep=False);join('hair','jaw')
path('fringe',(12,24),[('C',(24,20),(18,24),(21,22)),('C',(36,24),(27,22),(30,24))]);join('hair','fringe');join('jaw','fringe')
path('body',(8,44),[('A',(24,40),16,4,True),('A',(40,44),16,4,True)]);join('jaw','body')
'''
make(12,'VRECT_L','The rejected blank-faced woman lost her parted hair and collar shape. Restore a parted fringe below a distinct bun, a circular jaw and broad shoulders touching the jaw.',bun,'human_ref/user.svg circular head and broad shoulders; original bun and parted hair. Jaw bottom36 to shoulders40 gives zero visible gap.',extra='    human_construction = "bust"')
make(13,'VRECT_L','The rejected bun portrait had a triangular peak and a tiny shieldlike face. Restore a rounded bun, fuller circular jaw and swept fringe above broad shoulders.',bun.replace("(24,20),(18,24),(21,22)","(24,19),(18,24),(22,21)").replace("(36,24),(27,22),(30,24)","(36,24),(26,21),(30,24)"),'human_ref/user.svg circular jaw and broad shoulders; original bun and swept fringe; tiny expression omitted.',extra='    human_construction = "bust"')
make(14,'VRECT_L','The rejected glasses were oversized blocks joined to the face rim. Restore small round lenses and a fuller circular face under a bun, with broad touching shoulders.', '''
path('hair',(8,22),[('C',(16,10),(8,14),(11,10)),('A',(32,10),8,6,True),('C',(40,22),(37,10),(40,14))])
self.add_arc('jaw',(8,22),(40,22),radius_x=16,sweep=False);join('jaw','hair')
circle('lens-left',18,22,2);circle('lens-right',30,22,2)
line('bridge',(20,22),(28,22));join('bridge','lens-left');join('bridge','lens-right')
path('body',(8,44),[('A',(24,42),16,2,True),('A',(40,44),16,2,True)]);join('body','jaw')
''','human_ref/user.svg; circular jaw and gently curved shoulders. Small complete-circle lens exception is part of the shared contract.',extra='    human_construction = "bust"')
make(15,'VRECT_L','The rejected side-parted portrait looked like a helmet over a tiny face. Enlarge the circular jaw, extend the hair sides, and give the fringe a clear side sweep.', '''
path('hair',(8,29),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,29))])
self.add_arc('jaw',(14,20),(34,20),radius_x=10,sweep=False)
path('fringe',(14,20),[('C',(27,12),(21,20),(24,16)),('C',(34,20),(28,17),(30,19))]);join('fringe','jaw')
line('temple-left',(8,20),(14,20));line('temple-right',(34,20),(40,20))
for n in ('temple-left','temple-right'):
 join(n,'hair');join(n,'jaw');join(n,'fringe')
path('body',(8,44),[('A',(20,34),12,10,True),('L',(28,34)),('A',(40,44),12,10,True)]);join('body','jaw')
''','human_ref/user.svg circular jaw and shoulders; original deliberately asymmetric side fringe, extended hair.',extra='    human_construction = "bust"')
make(16,'SQUARE','The rejected draped portrait used a dot for a bun and lost the hairline. Restore the bun as a rounded upper lobe, circular jaw, swept hair and a diagonal garment fold.', '''
path('hair',(14,18),[('A',(20,10),6,8,True),('A',(28,10),4,4,True),('A',(34,18),6,8,True)])
self.add_arc('jaw',(14,18),(34,18),radius_x=10,sweep=False);join('hair','jaw')
path('body',(6,42),[('A',(20,32),14,10,True),('L',(28,32)),('A',(42,42),14,10,True)]);join('jaw','body')
path('drape',(34,33),[('C',(17,42),(29,38),(23,40))]);join('body','drape')
''','human_ref/user.svg circular jaw and shoulders; original bun and diagonal drape. Jaw28 and body32 make touching ink.',extra='    human_construction = "bust"')
make(17,'SQUARE','The rejected masked woman had a vertical center bar and circular medallion-like face. Restore a swept hair part and a larger jaw with a face-mask upper edge.', '''
path('hair',(6,42),[('C',(6,22),(10,37),(6,30)),('A',(42,22),18,16,True),('C',(42,42),(42,30),(38,37))])
path('fringe',(14,22),[('C',(27,14),(21,22),(25,17)),('C',(34,22),(29,19),(31,21))])
self.add_arc('jaw',(14,22),(34,22),radius_x=10,sweep=False);join('jaw','fringe')
path('mask',(14,22),[('C',(24,21),(18,23),(21,21)),('C',(34,22),(27,21),(30,23))]);join('mask','jaw');join('mask','fringe')
''','Original side-parted hair and mask; circular jaw follows human_ref/user.svg.')
make(18,'SQUARE','The rejected conveyor worker was a T stick behind a belt divided into rectangles. Restore rounded shoulders and circular conveyor rollers beside the box.', '''
circle('head',15,10,4)
path('torso',(6,30),[('L',(6,28)),('A',(15,22),9,6,True),('A',(24,28),9,6,True),('L',(24,30))])
box('belt',6,30,42,42,6);join('torso','belt')
poly('package',(32,30),(32,14),(42,14),(42,30));join('package','belt')
for i,x in enumerate((16,30)):circle(f'roller-{i}',x,36,2);join(f'roller-{i}','belt')
''','human_ref/user.svg for round head and shoulders; head bottom14 to shoulder22 is exactly4 ink units. Circular rollers restore conveyor identity.')
make(19,'SQUARE','The rejected remote worker had a tiny bent torso disconnected visually from the laptop. Restore broad seated shoulders under the roof and a clear laptop screen and keyboard.', '''
poly('roof',(6,16),(24,6),(42,16))
circle('head',14,26,4)
path('body',(6,42),[('A',(14,38),8,4,True),('A',(22,42),8,4,True)])
poly('laptop',(24,42),(30,26),(42,26),(38,42),closed=True)
line('keyboard',(14,42),(24,42));join('keyboard','body');join('keyboard','laptop')
''','human_ref/user.svg round head and seated shoulders; exact4 ink gap from head30 to shoulders38; original roof and laptop.')
make(20,'VRECT_L','The rejected bob-haired woman had a helmet outline and generic open shoulders. Restore flared bob ends and a broader closed blouse below a circular jaw.', '''
path('hair',(8,28),[('L',(10,18)),('A',(38,18),14,14,True),('L',(40,28))])
self.add_arc('jaw',(16,18),(32,18),radius_x=8,sweep=False)
path('fringe',(16,18),[('C',(27,11),(21,18),(25,14)),('C',(32,18),(28,15),(30,17))]);join('fringe','jaw')
line('temple-left',(10,18),(16,18));line('temple-right',(32,18),(38,18))
for n in ('temple-left','temple-right'):
 join(n,'hair');join(n,'jaw');join(n,'fringe')
path('body',(8,44),[('L',(8,40)),('A',(20,30),12,10,True),('L',(28,30)),('A',(40,40),12,10,True),('L',(40,44)),('L',(8,44))],True);join('jaw','body')
''','human_ref/user.svg circular jaw and shoulders; original flared bob and closed blouse. Jaw26 and shoulder30 make zero visible gap.',extra='    human_construction = "bust"')
