from author import make
make(14,'VRECT_L','The rejected glasses merged into the face rim. Restore two round lenses, a clear bridge, a rounded bun and larger cheek clearance.', '''
path('hair',(8,16),[('C',(16,10),(8,12),(12,10)),('A',(32,10),8,6,True),('C',(40,16),(36,10),(40,12))])
for side,x,end in [('left',8,(12,32)),('right',40,(36,32))]:
 line(f'side-{side}',(x,16),(x,26));join(f'side-{side}','hair')
 line(f'cheek-{side}',(x,26),end);join(f'side-{side}',f'cheek-{side}')
self.add_arc('jaw',(12,32),(36,32),radius_x=15,sweep=False);join('jaw','cheek-left');join('jaw','cheek-right')
circle('lens-left',18,22,2);circle('lens-right',30,22,2)
line('bridge',(20,22),(28,22));join('bridge','lens-left');join('bridge','lens-right')
path('body',(8,44),[('A',(24,42),16,2,True),('A',(40,44),16,2,True)]);join('jaw','body')
''','human_ref/user.svg circular lower jaw and broad shoulders; jaw38, shoulders42 give touching ink. Small round lens exception retains glasses.',extra='    human_construction = "bust"')
make(18,'SQUARE','The rejected worker had a T-shaped torso and divided conveyor. Restore curved shoulders next to the package and a shared rounded conveyor silhouette.', '''
circle('head',14,10,4)
path('assembly',(6,30),[('L',(6,28)),('A',(12,22),6,6,True),('L',(16,22)),('A',(22,28),6,6,True),('L',(22,30)),('L',(32,30)),('L',(32,14)),('L',(42,14)),('L',(42,36)),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,30))],True)
''','human_ref/user.svg curved shoulders; head14 to shoulder22 gives4 ink gap. Rounded conveyor and standing box share a connected outline. Tiny rollers omitted.')
