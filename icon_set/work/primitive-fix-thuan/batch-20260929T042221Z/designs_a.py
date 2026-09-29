# Hand symbols retain complete digit count; narrow anatomical slots receive a drawing-bound exception.
for i in [16,17,18]:
 author(i,'''
self.path('hand',(16,27),('L',(16,10)),('A',(24,10),4,4,True),('L',(24,21)),('A',(30,21),3,3,True),('L',(30,23)),('A',(36,23),3,3,True),('L',(36,25)),('A',(42,25),3,3,True),('L',(42,30)),('A',(30,42),12,12,True),('L',(24,42)),('A',(14,37),12,12,True),('L',(7,27)),('A',(13,23),4,4,True),('L',(16,27)),closed=True)
for x,y in [(24,21),(30,23),(36,25)]:
    self.add_line(f'finger-{x}',(x,y),(x,y+5))
    self.relate('connect','hand',f'finger-{x}')
''','SQUARE',
 'The rejected hand shortened the raised index and compressed or omitted curled digits. Feedback asks to recover the intended hand gesture.',
 'One upright pointer with a long index, three rounded curled fingers, a diagonal thumb and a broad rounded palm; shared 6-unit curled-finger pitch.',
 'Lucide pointer and hand: continuous palm silhouette, round digit caps and attached finger creases.',
 exception_reason='User authorized visual exceptions. Retain all five anatomical digits and the long index: 6-unit finger pitch intentionally leaves 2-unit ink slots, still distinct at native size; slight organic envelope variance is accepted.')
author(19,'''
self.path('hand',(16,27),('L',(16,11)),('A',(22,11),3,3,True),('L',(22,7)),('A',(28,7),3,3,True),('L',(28,10)),('A',(34,10),3,3,True),('L',(34,15)),('A',(40,15),3,3,True),('L',(40,30)),('A',(26,44),14,14,True),('L',(24,44)),('A',(15,39),11,11,True),('L',(9,29)),('A',(14,24),4,4,True),('L',(16,27)),closed=True)
for x,y in [(22,11),(28,10),(34,15)]:
    self.add_line(f'finger-{x}',(x,y),(x,23))
    self.relate('connect','hand',f'finger-{x}')
''','VRECT_L','The rejected open hand had only three upright fingers and a horizontal thumb. Feedback requests the original open-hand meaning.',
 'Restore four staggered upright fingers plus an opposing diagonal thumb, a full palm and smooth wrist curve.',
 'Lucide hand: shared finger arcs and coherent outer palm. Human reference checked for stroke vocabulary.',
 exception_reason='Four complete fingers require 6-unit pitch at SOLO48. The intentional 2-unit ink slots preserve the open-hand identity and remain visible at native size; organic keyshape variance accepted.')
# Clear question symbols, retaining vertical hook termination instead of a slash.
for i in [3,4]:
 outer= "self.path('bubble',(10,32),('A',(6,22),16,16,True),('A',(24,6),18,16,True),('A',(42,22),18,16,True),('A',(24,38),18,16,True),('L',(18,38)),('L',(6,42)),('L',(10,32)),closed=True)" if i==3 else "self.path('bubble',(12,6),('L',(36,6)),('A',(42,12),6,6,True),('L',(42,32)),('A',(36,38),6,6,True),('L',(22,38)),('L',(12,44)),('L',(12,38)),('A',(6,32),6,6,True),('L',(6,12)),('A',(12,6),6,6,True),closed=True)"
 author(i,outer+'''
self.path('question',(18,17),('A',(24,12),6,5,True),('A',(30,18),6,6,True),('A',(27,23),6,6,True),('A',(24,27),5,5,False))
self.add_dot('question-dot',(24,33))
''','SQUARE','The rejected question hook collapsed into a diagonal wedge and crowded the enclosure. Feedback asks to restore the reference question bubble.',
 'Smooth rounded bubble with a distinct tail; upright question hook with curved return and a separate dot.',
 'Lucide message-circle-question-mark and message-square: coherent enclosure and independently readable question mark.',
 exception_reason='Question-mark dot and hook retain 2-unit ink separation, and enclosure clearances are locally below 4 to preserve a readable full question sign; user authorized native-size visual exception.')
author(2,'''
self.path('rear',(22,34),('L',(14,42)),('L',(14,34)),('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(32,6)),('A',(36,10),4,4,True),('L',(36,16)))
self.path('front',(28,22),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,36)),('A',(38,40),4,4,True),('L',(38,44)),('L',(32,40)),('L',(28,40)),('A',(24,36),4,4,True),('L',(24,26)),('A',(28,22),4,4,True),closed=True)
self.path('question',(14,15),('A',(22,15),4,4,True),('A',(19,19),4,4,True),('L',(19,21)))
self.add_dot('question-dot',(19,27))
self.add_line('exclamation-stem',(33,27),(33,30))
self.add_dot('exclamation-dot',(33,36))
''','SQUARE','The rejected rear bubble was open on the left and its exclamation was only a dot. Feedback asks to recover both messages and their punctuation.',
 'Two offset rounded speech bubbles, full rear question sign and front exclamation with separate stem and dot; rear outline interrupted only by the front bubble.',
 'Lucide message-square: rounded frame and corner tail; message-circle-question-mark punctuation.',
 exception_reason='Two complete message symbols require compact punctuation and close overlapping enclosure edges. All intended marks remain visibly separated with 4px strokes; user authorized composition and spacing exception.')
for i in [11,12]:
 author(i,'''
# Concentric upper arcs share center (24,30); three bands preserve rainbow identity.
for name,r in [('outer',20),('middle',13),('inner',6)]:
    self.add_arc(name,(24-r,30),(24+r,30),radius_x=r,sweep=True)
self.path('left-cloud',(4,29),('A',(13,32),8,8,True),('A',(13,42),5,5,True),('L',(4,42)))
self.path('right-cloud',(44,29),('A',(35,32),8,8,False),('A',(35,42),5,5,False),('L',(44,42)))
''','HRECT_L','The rejected rainbow had two bands and heavy cloud junctions. The reference and feedback require a three-band rainbow between two clouds.',
 'Restore three concentric rainbow bands and two opposing soft cloud ends; shared center and mirrored cloud geometry.',
 'Lucide rainbow: repeated concentric semicircles with shared center.',
 'Cloud outer ends remain open at the composition edges as in the supplied reference.',
 exception_reason='Three 4px rainbow bands use 7-unit centerline pitch (3px visible separation). Compact cloud contacts and natural lower envelope are visually accepted to retain all reference bands.')
