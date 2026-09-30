from author import make
make(8,'SQUARE','The rejected pirate had a flat brim and a featureless mouth area. Restore a bowed hat brim and a wider round jaw around the wink; retain the broad straw crown.', '''
path('crown',(8,16),[('A',(24,6),16,10,True),('A',(40,16),16,10,True)])
path('brim',(6,16),[('L',(8,16)),('C',(24,20),(12,20),(18,20)),('C',(40,16),(30,20),(36,20)),('L',(42,16))]);join('crown','brim')
path('jaw',(8,16),[('C',(24,42),(8,34),(12,42)),('C',(40,16),(36,42),(40,34))]);join('jaw','brim');join('jaw','crown')
self.add_dot('eye',(19,29));line('wink',(28,29),(30,28))
''','Original straw hat and wink; circular-looking jaw, curved brim; tiny mouth and ears omitted for spacing.')
make(9,'SQUARE','The rejected USB mouse had a short square cable bend and blocklike plug. Restore a rounded mouse and a broad looping cable ending in a clear USB plug.', '''
box('mouse',24,20,42,42,9)
line('wheel',(33,29),(33,32))
path('cable',(33,20),[('L',(33,14)),('C',(20,6),(33,6),(27,6)),('C',(6,20),(10,6),(6,12)),('L',(6,26))]);join('cable','mouse')
poly('plug',(6,26),(14,26),(14,40),(6,40),closed=True);join('plug','cable')
''','Lucide mouse capsule and scroll mark; reference large looping cord retained.')
earbuds='''
path('device',(6,26),[('L',(12,26)),('L',(12,18)),('C',(6,14),(6,18),(6,16)),('C',(13,6),(6,8),(9,6)),('C',(20,14),(18,6),(20,9)),('L',(20,26)),('L',(28,26)),('L',(28,14)),('C',(35,6),(28,9),(30,6)),('C',(42,14),(39,6),(42,8)),('C',(36,18),(42,16),(42,18)),('L',(36,26)),('L',(42,26)),('L',(42,34)),('A',(34,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,26))],True)

'''
for n in (10,11):
 make(n,'SQUARE','The rejected earbuds used circular or split-ring heads. Restore opposed bulbous earpieces, full stems and a rounded charging case. Omit the tiny lightning bolt to preserve the case opening.',earbuds,'Original earbud case; paired bulbous earpieces and shared case outline.')
make(14,'VRECT_L','The rejected glasses merged into the face rim. Restore two small round lenses, a distinct bridge and cheek clearances beneath the bun; retain a circular lower jaw and touching shoulders.', '''
path('hair',(8,16),[('C',(16,10),(8,12),(12,10)),('A',(32,10),8,6,True),('C',(40,16),(36,10),(40,12))])
for side,x,end in [('left',8,(12,31)),('right',40,(36,31))]:
 line(f'side-{side}',(x,16),(x,24));join(f'side-{side}','hair')
 line(f'cheek-{side}',(x,24),end);join(f'side-{side}',f'cheek-{side}')
self.add_arc('jaw',(12,31),(36,31),radius_x=15,sweep=False);join('jaw','cheek-left');join('jaw','cheek-right')
circle('lens-left',18,22,2);circle('lens-right',30,22,2)
line('bridge',(20,22),(28,22));join('bridge','lens-left');join('bridge','lens-right')
path('body',(8,44),[('A',(24,41),16,3,True),('A',(40,44),16,3,True)]);join('jaw','body')
''','human_ref/user.svg circular jaw and broad shoulders; radius15 lower jaw has bottom37, shoulders41, so ink touches. Small lens circles follow the contract exception.',extra='    human_construction = "bust"')
make(15,'SQUARE','The rejected side-parted woman had helmet-like hair and a tiny face. Restore fuller circular cheeks, extended hair and an asymmetric swept fringe over broad curved shoulders.', '''
path('hair',(6,30),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,30))])
self.add_arc('jaw',(14,20),(34,20),radius_x=10,sweep=False)
path('fringe',(14,20),[('C',(27,16),(20,20),(24,18)),('C',(34,20),(29,19),(31,20))]);join('fringe','jaw')
line('temple-left',(6,24),(14,20));line('temple-right',(34,20),(42,24))
for n in ('temple-left','temple-right'):
 join(n,'hair');join(n,'jaw');join(n,'fringe')
path('body',(6,42),[('A',(24,34),18,8,True),('A',(42,42),18,8,True)]);join('body','jaw')
''','human_ref/user.svg circular jaw and broad shoulders; asymmetric hair part follows the source. Jaw30, shoulders34 give touching ink.',extra='    human_construction = "bust"')
make(16,'SQUARE','The rejected draped woman used a dot-like bun and generic circular head. Restore a rounded bun above the circular jaw and a clear diagonal garment fold across broad shoulders.', '''
path('hair',(14,18),[('A',(20,10),6,8,True),('A',(28,10),4,4,True),('A',(34,18),6,8,True)])
self.add_arc('jaw',(14,18),(34,18),radius_x=10,sweep=False);join('hair','jaw')
path('body',(6,42),[('L',(9,42)),('A',(15,34),15,10,True),('A',(24,32),15,10,True),('A',(33,34),15,10,True),('A',(39,42),15,10,True),('L',(42,42))]);join('jaw','body')
line('drape',(24,32),(14,42));join('drape','body')
''','human_ref/user.svg; circular jaw and rounded shoulders with true shared drape node. Jaw28, shoulder32 give touching ink.',extra='    human_construction = "bust"')
make(17,'SQUARE','The rejected masked woman had a central hanging bar. Restore a swept hairline, long side hair and a broad mask across the lower face.', '''
path('hair',(6,42),[('C',(6,22),(10,37),(6,30)),('A',(42,22),18,16,True),('C',(42,42),(42,30),(38,37))])
path('fringe',(14,22),[('C',(27,15),(21,22),(25,18)),('C',(34,22),(29,20),(31,22))])
self.add_arc('jaw',(14,22),(34,22),radius_x=10,sweep=False);join('jaw','fringe')
line('mask-edge',(14,22),(34,22));join('mask-edge','jaw');join('mask-edge','fringe')
''','Original swept hair and face mask; circular jaw per human_ref/user.svg.')
make(18,'SQUARE','The rejected conveyor had rectangular divisions and a T-shaped worker. Restore a curved upper torso beside the box and dot rollers inside a deeper conveyor bed.', '''
circle('head',15,10,4)
path('torso',(6,26),[('A',(15,22),9,4,True),('A',(24,26),9,4,True)])
box('belt',6,26,42,42,8);join('torso','belt')
poly('package',(32,26),(32,14),(42,14),(42,26));join('package','belt')
for i,x in enumerate((16,32)):self.add_dot(f'roller-{i}',(x,34))
''','human_ref/user.svg circular head and curved shoulders; exact4 ink gap from head14 to shoulder22. Rollers simplified to dots.')
make(19,'SQUARE','The rejected remote worker had a small bent stick torso. Restore a rounded seated shoulder silhouette under the roof and a distinct sloped laptop.', '''
poly('roof',(6,16),(24,6),(42,16))
circle('head',14,26,4)
path('body',(6,42),[('A',(14,38),8,4,True),('A',(22,42),8,4,True)])
poly('laptop',(22,42),(30,26),(42,26),(38,42),closed=True);join('laptop','body')
''','human_ref/user.svg round head and broad seated shoulders; head30 to shoulder38 gives exact4 ink gap.')
make(20,'VRECT_L','The rejected bob-haired portrait used a helmet-like arc and generic shoulders. Restore turned-out bob ends and a closed rounded blouse under the circular jaw.', '''
path('hair',(10,30),[('L',(8,28)),('L',(8,20)),('A',(40,20),16,16,True),('L',(40,28)),('L',(38,30))])
self.add_arc('jaw',(16,20),(32,20),radius_x=8,sweep=False)
path('fringe',(16,20),[('C',(27,12),(21,20),(25,15)),('C',(32,20),(28,16),(30,19))]);join('fringe','jaw')
line('temple-left',(8,20),(16,20));line('temple-right',(32,20),(40,20))
for n in ('temple-left','temple-right'):
 join(n,'hair');join(n,'jaw');join(n,'fringe')
path('body',(8,44),[('L',(8,40)),('A',(24,32),16,8,True),('A',(40,40),16,8,True),('L',(40,44)),('L',(8,44))],True);join('body','jaw')
''','human_ref/user.svg circular jaw and shoulders; original turned-out bob and closed blouse. Jaw28, shoulders32 give touching ink.',extra='    human_construction = "bust"')
