from author import *
DESIGNS.update({
11:('SQUARE','The rejected person had crossed legs compressed into a knot. Restore a jumping pose with raised arms and separated bent legs above a supported trampoline.','Round head, airborne torso and two bent legs above a broad elliptical trampoline.', '''
circle('head',24,9,5)
self.add_line('torso',(24,22),(24,26))
self.add_polyline('arms',(10,14),(15,21),(24,22),(33,20),(38,16))
self.add_polyline('leg-left',(24,26),(18,31),(13,29))
self.add_polyline('leg-right',(24,26),(30,30),(34,26))
path('trampoline',(6,39),[('A',(42,39),18,3,True),('A',(6,39),18,3,True)],True)
self.add_line('left-support',(6,39),(6,44));self.add_line('right-support',(42,39),(42,44))
join('torso','arms');join('torso','leg-left');join('torso','leg-right');join('leg-left','leg-right');join('trampoline','left-support');join('trampoline','right-support')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
12:('SQUARE','The rejected net became an angular flag and the butterfly became two dots. Restore an oval net with a hanging bag, raised handle and winged butterfly.','Asymmetric catcher bust at right, oval net above, butterfly at upper left.', '''
circle('head',34,26,5)
path('torso',(34,39),[('B',(41,39),(42,40),(42,44))])
self.add_polyline('arm',(34,39),(24,33),(20,26))
self.add_line('handle',(20,26),(28,14))
path('hoop',(25,10),[('A',(33,10),4,6,True),('A',(25,10),4,6,True)],True)
path('net-bag',(29,4),[('L',(42,10)),('B',(40,17),(34,20),(27,16))])
path('butterfly',(12,18),[('B',(2,6),(3,26),(12,18)),('B',(21,6),(23,26),(12,18))])
self.add_line('butterfly-body',(12,16),(12,22))
join('torso','arm');join('arm','handle');join('hoop','net-bag');join('butterfly','butterfly-body')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
'''),
13:('SQUARE','The rejected stairs were only one thick step and the body faced ambiguously. Restore a three-level staircase and a stepping-down pose.','Stepped baseline with a leaning walker; bent rear leg and extended lower foot.', '''
circle('head',19,11,5)
path('torso',(19,24),[('B',(19,27),(22,28),(23,31))])
self.add_polyline('arm-left',(19,24),(13,28),(9,28))
self.add_polyline('arm-right',(19,24),(28,26),(30,30))
self.add_polyline('leg-left',(23,31),(16,34),(14,42))
self.add_polyline('leg-right',(23,31),(28,31),(30,36))
self.add_polyline('stairs',(6,42),(18,42),(18,36),(30,36),(30,30),(42,30))
join('torso','arm-left');join('torso','arm-right');join('arm-left','arm-right');join('torso','leg-left');join('torso','leg-right');join('leg-left','leg-right');join('leg-left','stairs');join('leg-right','stairs');join('arm-right','stairs')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
'''),
14:('SQUARE','The rejected arm was a shelf attached to a bulky bottle. Restore a large bust, bent holding arm and a slender necked bottle with a cap.','Bust at left, bottle at right; rounded shoulder owns the arm that reaches the bottle.', '''
circle('head',15,14,7)
path('bust',(6,42),[('L',(6,36)),('B',(6,31),(10,29),(15,29)),('B',(21,29),(23,32),(24,36)),('L',(31,36))])
path('arm',(17,35),[('B',(17,41),(24,42),(31,40))])
path('bottle',(34,6),[('L',(40,6)),('L',(40,15)),('B',(40,19),(42,20),(42,24)),('L',(42,40)),('L',(32,40)),('L',(32,24)),('B',(32,20),(34,19),(34,15)),('L',(34,6))],True)
self.add_line('cap',(34,10),(40,10));join('bottle','cap')
'''),
15:('SQUARE','The rejected measuring device was a comb and the person resembled a shirt. Restore an outlined height ruler beside a complete standing silhouette.','Rectangular ruler with repeated inward ticks, larger head, shoulders and divided legs.', '''
self.add_polyline('ruler',(6,6),(16,6),(16,42),(6,42),closed=True)
for y in (14,22,30):
 self.add_line(f'tick-{y}',(6,y),(10,y));join('ruler',f'tick-{y}')
circle('head',31,12,6)
path('body',(31,26),[('B',(24,26),(23,29),(23,33)),('L',(26,33)),('L',(27,42)),('L',(35,42)),('L',(36,33)),('L',(39,33)),('B',(39,29),(38,26),(31,26))],True)
self.add_line('legs',(31,35),(31,42));join('body','legs')
'''),
16:('SQUARE','The rejected seat and person were square brackets. Restore a curved seat shell and a seated figure reaching forward with bent knees.','Rounded seat below a round head and bent torso; deliberate seated side view.', '''
circle('head',23,12,6)
self.add_polyline('torso',(23,26),(23,32),(33,32),(42,40))
self.add_polyline('arm',(23,26),(31,25),(39,20))
path('seat',(7,21),[('L',(8,32)),('B',(9,40),(15,42),(23,42)),('L',(32,42))])
join('torso','arm')
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
'''),
17:('SQUARE','The rejected hull lost the dragon silhouette and the person was a tiny vertical line. Restore a dragon prow, rounded hull, passenger bust and flag.','Dragon head at left; passenger and upright flag above a smooth bowl-like hull.', '''
path('boat',(6,22),[('L',(10,22)),('L',(11,18)),('L',(15,15)),('L',(15,27)),('L',(19,31)),('L',(35,31)),('L',(42,27)),('B',(42,39),(35,42),(25,42)),('B',(14,42),(10,36),(9,29)),('L',(6,29)),('L',(6,22))],True)
circle('head',25,17,4)
path('bust',(20,31),[('B',(20,29),(22,29),(25,29)),('B',(28,29),(30,29),(30,31))])
self.add_line('pole',(35,31),(35,6));self.add_polyline('flag',(35,6),(42,6),(42,14),(35,14))
join('boat','bust');join('boat','pole');join('pole','flag')
'''),
18:('SQUARE','The rejected person looked like a disconnected angular digit beside a bowl. Restore a bent back, reaching arm, kneeling leg and a small bucket.','Forward-bent kneeling figure at right with bucket at left; head-to-neck uses a 5-12-13 triangle.', '''
circle('head',17,12,5)
path('torso',(29,17),[('B',(37,20),(38,24),(35,32))])
self.add_polyline('arm',(29,17),(25,29),(20,34))
self.add_polyline('leg',(35,32),(31,42),(42,42))
path('bucket',(6,31),[('L',(18,31)),('L',(16,39)),('A',(8,39),4,3,True),('L',(6,31))],True)
join('torso','arm');join('torso','leg')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
'''),
19:('SQUARE','The rejected mop was just a short ground line and the hands did not clearly hold a handle. Restore a long diagonal handle, capsule mop head and a leaning cleaning pose.','Large mop pad at lower left, long shaft to both hands, upright head over a leaning torso.', '''
circle('head',28,11,5)
path('torso',(28,24),[('B',(28,27),(29,29),(31,32))])
self.add_polyline('arm',(28,24),(21,29),(16,29))
self.add_polyline('legs',(25,42),(31,32),(41,42))
self.add_line('handle',(16,29),(8,39))
rect('mop',6,39,20,44,2)
join('torso','arm');join('torso','legs');join('arm','handle');join('handle','mop')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
'''),
20:('VRECT_L','The rejected person looked like a squatting bowl with short legs. Restore an upright body, hands held at the groin and unmistakably crossed legs.','Symmetric round head and broad shoulders; hands converge centrally and long legs cross below.', '''
circle('head',24,9,5)
path('body',(24,22),[('B',(13,22),(10,24),(12,29)),('B',(13,33),(19,35),(24,35)),('B',(29,35),(35,33),(36,29)),('B',(38,24),(35,22),(24,22))],True)
self.add_polyline('hands',(18,28),(24,34),(30,28))
self.add_line('leg-left',(18,34),(30,44));self.add_line('leg-right',(30,34),(18,44))
join('body','hands');join('body','leg-left');join('body','leg-right');join('leg-left','leg-right')
'''),
})
if __name__=='__main__':author(range(11,21),'b')
