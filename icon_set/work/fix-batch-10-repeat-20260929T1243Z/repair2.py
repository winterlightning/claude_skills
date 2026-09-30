from author import make
make(14,'SQUARE','The rejected glasses merged into the face rim. Restore two visibly round lenses, a separate bridge and ample cheek clearance beneath the rounded bun.', '''
path('hair',(6,20),[('C',(16,12),(6,14),(11,12)),('A',(32,12),8,6,True),('C',(42,20),(37,12),(42,14))])
line('side-left',(6,20),(6,28));line('side-right',(42,20),(42,28))
path('jaw',(6,28),[('A',(24,34),18,6,False),('A',(42,28),18,6,False)])
for n in ('side-left','side-right'):join(n,'hair');join(n,'jaw')
circle('lens-left',17,20,3);circle('lens-right',31,20,3)
line('bridge',(20,20),(28,20));join('bridge','lens-left');join('bridge','lens-right')
path('body',(6,42),[('A',(24,38),18,4,True),('A',(42,42),18,4,True)]);join('jaw','body')
''','Round lenses use the small circle exception; rounded jaw and shoulders based on human_ref/user.svg, with jaw34 and shoulder38 touching ink.',extra='    human_construction = "bust"')
make(17,'SQUARE','The rejected masked woman had a hanging central bar. Restore long side hair around a complete round face with a horizontal mask edge and curved lower mask.', '''
path('hair',(6,42),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,42))])
circle('face',24,24,9)
line('mask-edge',(15,24),(33,24));join('mask-edge','face')
''','human_ref/user.svg circular head; original long hair and lower-face mask. Fine swept fringe omitted to preserve the face and mask openings.')
make(18,'SQUARE','The rejected worker used a T-shaped torso and divided conveyor. Restore curved shoulders, an outlined package and a distinct rounded conveyor with two roller centers.', '''
circle('head',14,10,4)
path('torso',(6,26),[('A',(14,22),8,4,True),('A',(22,26),8,4,True)])
poly('package',(32,26),(32,14),(42,14),(42,26),closed=True)
path('belt',(12,30),[('L',(36,30)),('A',(36,42),6,6,True),('L',(12,42)),('A',(12,30),6,6,True)],True)
join('belt','torso');join('belt','package')
''','human_ref/user.svg curved shoulders; head14 to shoulders22 gives4 ink gap. Roller marks omitted to keep the narrow conveyor opening clear.')

make(16,'SQUARE','The rejected draped woman used a dotlike bun and generic body. Restore a rounded bun, curved shoulders and a clear diagonal fold across the garment.', """
path('hair',(16,14),[('A',(20,10),4,4,True),('A',(28,10),4,4,True),('A',(32,14),4,4,True)])
self.add_arc('jaw',(16,14),(32,14),radius_x=8,sweep=False);join('hair','jaw')
path('body',(6,42),[('L',(9,41)),('A',(15,29),15,15,True),('A',(24,26),15,15,True),('A',(33,29),15,15,True),('A',(39,41),15,15,True),('L',(42,42))]);join('body','jaw')
line('drape',(33,29),(20,42));join('drape','body')
""",'human_ref/user.svg circular jaw and curved shoulders; jaw22, shoulders26 give touching ink. Diagonal fold attaches at a true shoulder node.',extra='    human_construction = "bust"')
