import author_batch as a

def replace(n,old,new):
 d=list(a.D[n]);assert old in d[4],(n,old);d[4]=d[4].replace(old,new);a.D[n]=tuple(d)
def code(n,new):
 d=list(a.D[n]);d[4]=new;a.D[n]=tuple(d)
replace(1,"[C((42,13),(28,6),(36,6))]","[C((31,6),(22,6),(27,6)),C((42,13),(36,6),(42,9))]")
replace(1,"(22,24)","(22,23)")
replace(1,"(42,29)","(42,31)")
replace(1,"self.mark_human_figure('upper'","join('upper-leg','lower-torso');join('upper-leg','lower-leg')\nself.mark_human_figure('upper'")
replace(2,"circle('lower-head',38,42,4)","circle('lower-head',38,40,4)")
replace(2,"[C((23,12),(31,20),(22,16)),C((26,5),(19,5),(23,3)),C((28,9),(29,5),(30,8))]","[C((22,13),(26,19),(22,17)),C((24,6),(20,9),(20,6)),L((28,6))]")
replace(2,"line('lower-torso',(26,42),(12,42))","line('lower-torso',(26,40),(12,40))")
replace(2,"path('lower-leg',(26,42),[C((26,25),(28,38),(26,30))])","path('lower-leg',(26,40),[L((26,24))])")
replace(2,"join('lower-torso','lower-leg')","join('lower-torso','lower-leg');join('upper-torso','lower-leg');join('upper-leg','lower-leg')")
# Better outer margins and contour-to-score attachment on the loaf.
replace(4,"(18,1),(28,1)","(18,5),(28,5)")
replace(4,"C((4,38),(3,41),(3,40)),C((26,38),(6,26),(24,26)),C((26,42),(27,40),(27,41))","C((15,30),(4,35),(9,30)),C((26,42),(21,30),(26,35))")
replace(4,"line('score',(15,31),(15,35))","line('score',(15,30),(15,35));join('score','loaf')")
# Smooth ear tips, clearer paw and egg contour, no tiny reversing curves.
code(8,"""
path('rabbit',(12,34),[C((9,20),(5,30),(6,24)),C((7,5),(4,10),(3,5)),C((18,17),(12,5),(15,10)),C((24,17),(20,16),(22,16)),C((35,5),(27,10),(30,5)),C((33,20),(39,5),(38,10)),C((35,26),(35,22),(35,24))])
path('cheek',(12,34),[C((23,35),(15,37),(19,37))])
self.add_dot('eye-left',(14,25));self.add_dot('eye-right',(25,25));self.add_dot('nose',(19,30))
path('body',(12,34),[C((10,43),(10,37),(10,40))])
path('egg-upper',(28,35),[C((35,27),(29,31),(32,27)),C((42,39),(39,27),(42,35)),C((32,44),(42,45),(36,45)),C((29,42),(30,44),(29,43))])
path('paw',(21,39),[L((27,38)),C((27,42),(31,38),(31,41)),L((23,43))])
""")
# A single continuous plane outline includes its lower wing; reduce the narrow outlined tail to one coherent fin.
code(9,"""
path('plane',(9,20),[L((15,23)),L((15,29)),L((22,32)),L((9,40)),L((14,43)),L((30,36)),L((38,40)),C((41,34),(44,43),(46,37)),L((18,24)),L((14,16)),L((9,14)),L((9,20))],True)
path('flame',(32,26),[C((30,16),(26,23),(29,20)),C((35,8),(34,19),(37,14)),C((42,25),(41,14),(45,20))])
path('smoke-one',(5,10),[C((6,4),(2,8),(7,7))])
path('smoke-two',(17,10),[C((18,4),(14,8),(19,7))])
""")
replace(11,"C((43,31),(33,22),(43,24))","C((37,25),(32,25),(34,25)),C((43,31),(41,25),(43,27))")
replace(11,"(36,42)","(35,42)")
# Head center to torso junction is (5,-12), distance 13 minus radius 5 = 8 centerline / 4 ink.
code(12,"""
circle('head',23,9,5)
line('torso',(18,21),(14,32))
poly('arm',(18,21),(26,23),(33,17));join('torso','arm')
line('paddle',(38,7),(24,35))
path('canoe',(4,32),[L((34,32)),C((41,27),(39,32),(40,30)),C((44,36),(44,29),(45,33))])
path('water',(4,41),[C((16,40),(9,44),(12,44)),C((28,40),(20,44),(24,44)),C((40,41),(32,44),(36,44))])
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
""")
# Brim sits tangent to the head instead of cutting its small opening in half.
replace(14,"line('cap-brim',(23,7),(34,7))","line('cap-brim',(26,4),(34,4))")
replace(14,"rounded('parcel',5,18,17,28,2)","rounded('parcel',5,18,17,30,2)")
replace(14,"C((13,31),(4,32),(7,31)),L((25,31))","C((13,30),(4,32),(7,30)),L((25,30))")
# Avoid wheels on the canvas edge and open up the jagged break.
replace(15,"(12,42,4)","(12,40,4)") if '(12,42,4)' in a.D[15][4] else None
replace(15,"circle('left-wheel',12,42,4);circle('right-wheel',38,42,4)","circle('left-wheel',12,40,4);circle('right-wheel',38,40,4)")
replace(15,"(18,33),(24,37),(20,44),(16,44)","(16,33),(21,37),(18,42),(16,42)")
replace(15,"(26,33),(32,37),(28,44),(34,44)","(27,33),(32,37),(29,42),(34,42)")
# Pound keeps its curve but gains room to the frame and lower separator.
replace(17,"(17,29)","(18,28)")
replace(17,"(19,29)","(19,28)")
replace(17,"L((29,29))","L((29,28))")
replace(17,"(17,21)","(18,21)")
# Retain open pin circles while giving the two pins separate ink at native size.
replace(19,"circle('pin-left',19,24,3);circle('pin-right',29,24,3)","circle('pin-left',18,24,3);circle('pin-right',30,24,3)")
# Exact 3-4-5 circle attachment nodes, shared endpoints on each circle.
code(20,"""
path('hub',(16,24),[A((14,28),5,5,True),A((6,24),5,5,True),A((14,20),5,5,True),A((16,24),5,5,True)],True)
path('upper',(24,15),[A((30,7),5,5,True),A((24,15),5,5,True)],True)
path('lower',(24,33),[A((30,41),5,5,True),A((24,33),5,5,True)],True)
circle('right',37,24,5)
line('horizontal',(16,24),(32,24));join('hub','horizontal');join('right','horizontal')
line('upper-spoke',(14,20),(24,15));join('hub','upper-spoke');join('upper','upper-spoke')
line('lower-spoke',(14,28),(24,33));join('hub','lower-spoke');join('lower','lower-spoke')
""")
a.generate([1,2,4,8,9,11,12,14,15,17,19,20])
