import author_batch as a
import json,textwrap
from pathlib import Path
R=json.loads((a.ROOT/'runs.json').read_text())
# Carry the latest authored source forward into a new run; prior attempts stay intact.
for n in (9,15,17,19):
 s=Path(R[str(n)]['module']).read_text();body=textwrap.dedent(s.split('        join=lambda a,b:self.relate(\'connect\',a,b)\n',1)[1]);v=list(a.D[n]);v[4]=body;a.D[n]=tuple(v)
def code(n,new):
 d=list(a.D[n]);d[4]=new;a.D[n]=tuple(d)
def replace(n,old,new):
 d=list(a.D[n]);assert old in d[4],old;d[4]=d[4].replace(old,new);a.D[n]=tuple(d)
code(9,"""
path('plane',(9,14),[L((14,16)),L((18,24)),L((41,34)),C((38,40),(46,37),(44,43)),L((30,36)),L((14,43)),L((9,40)),L((22,32)),L((10,27)),C((9,24),(9,27),(9,26)),L((9,14))],True)
path('flame',(32,26),[C((30,16),(26,23),(29,20)),C((35,8),(34,19),(37,14)),C((42,25),(41,14),(45,20))])
path('smoke-one',(5,10),[C((6,4),(2,8),(7,7))])
path('smoke-two',(17,10),[C((18,4),(14,8),(19,7))])
""")
code(15,"""
poly('burst',(6,17),(3,14),(11,14),(8,7),(17,10),(23,3),(27,10),(37,7),(34,14),(44,14),(41,17))
path('left-car',(20,23),[L((13,23)),L((9,30)),L((6,31)),L((6,40)),L((8,40))])
poly('left-break',(20,23),(17,29),(23,34),(20,40),(16,40))
path('right-car',(29,23),[L((35,23)),L((39,30)),C((44,34),(44,30),(44,31)),L((44,40)),L((42,40))])
poly('right-break',(29,23),(26,29),(32,34),(29,40),(34,40))
circle('left-wheel',12,40,4);circle('right-wheel',38,40,4)
""")
replace(17,"path('pound',(28,15),[C((24,11),(28,12),(27,11)),C((20,16),(21,11),(20,13))","path('pound',(28,16),[C((24,12),(28,13),(27,12)),C((20,16),(21,12),(20,13))")
replace(17,"(18,21),(26,21)","(18,20),(26,20)")
replace(19,"rounded('plate',5,5,43,43,5)","rounded('plate',4,4,44,44,5)")
replace(19,"circle('recess',24,24,13)","circle('recess',24,24,14)")
replace(19,"(24,11),(24,16)","(24,10),(24,15)")
replace(19,"(24,32),(24,37)","(24,33),(24,38)")
code(20,"""
circle('hub',10,24,4)
path('upper',(28,14),[A((28,6),4,4,True),A((28,14),4,4,True)],True)
path('lower',(28,34),[A((28,42),4,4,True),A((28,34),4,4,True)],True)
circle('right',38,24,4)
line('horizontal',(14,24),(34,24));join('hub','horizontal');join('right','horizontal')
line('upper-spoke',(14,24),(28,14));join('hub','upper-spoke');join('upper','upper-spoke');join('horizontal','upper-spoke')
line('lower-spoke',(14,24),(28,34));join('hub','lower-spoke');join('lower','lower-spoke');join('horizontal','lower-spoke');join('upper-spoke','lower-spoke')
""")
a.generate([9,15,17,19,20])
