import revise as r
import sys
a=r.a;D=a.DESIGNS;body=r.body
D[2]['body']=D[2]['body'].replace("('A',(20,30),4,4,True)","('A',(20,30),4,3,True)")
body(5, '''
path('cap',(8,16),[('A',(20,16),6,8,True)])
path('jaw',(20,16),[('A',(8,16),6,6,True)])
join('cap','jaw')
line('brim',(8,16),(22,16));join('brim','cap');join('brim','jaw')
path('shoulders',(4,40),[('A',(14,30),10,10,True),('A',(24,40),10,10,True)])
line('handle',(38,8),(38,30))
poly('broom',(38,30),(42,30),(44,40),(32,40),(34,30),(38,30),closed=True);join('handle','broom')
''')
body(8, '''
box('sausage',6,6,42,14,4)
line('score',(24,6),(28,14));join('score','sausage')
path('egg',(6,32),[('A',(16,23),10,9,True),('B',(24,32),(23,23),(24,26)),('A',(16,42),8,10,True),('A',(6,32),10,10,True)],True)
self.add_dot('yolk',(15,32))
path('bacon',(34,23),[('B',(34,42),(34,30),(30,34)),('L',(42,42)),('B',(42,23),(38,34),(42,30)),('L',(34,23))],True)
''')
D[12]['body']=D[12]['body'].replace('(24,25)','(24,24)').replace('(8,36)','(8,35)').replace('(19,34)','(19,33)').replace('(29,36)','(29,35)').replace('(40,34)','(40,33)')
body(15, '''
path('shell',(4,40),[('A',(44,40),20,20,True),('L',(4,40))],True)
path('lettuce',(4,40),[('L',(4,24)),('A',(12,16),8,8,True),('A',(24,8),12,8,True),('A',(36,16),12,8,True),('A',(44,24),8,8,True),('L',(44,40))])
join('lettuce','shell')
''')
D[16]['body']=D[16]['body'].replace('(6,29)','(6,26)').replace('(40,29)','(40,26)')
body(17, '''
path('shell',(24,42),[('L',(9,30)),('B',(6,24),(6,28),(6,26)),('A',(12,15),6,9,True),('A',(18,9),6,6,True),('A',(30,9),6,3,True),('A',(36,15),6,6,True),('A',(42,24),6,9,True),('B',(39,30),(42,26),(42,28)),('L',(24,42))],True)
line('rib-center',(24,15),(24,31))
line('rib-left',(12,15),(17,28));line('rib-right',(36,15),(31,28));join('rib-left','shell');join('rib-right','shell')
''')
body(19, '''
box('frame',6,6,42,42,4)
path('head',(18,22),[('A',(30,22),6,8,True),('A',(18,22),6,6,True)],True)
poly('hair-left',(18,22),(14,34),(19,34));poly('hair-right',(30,22),(34,34),(29,34))
join('hair-left','head');join('hair-right','head')
path('shoulders',(14,42),[('A',(24,36),10,6,True),('A',(34,42),10,6,True)])
join('shoulders','frame')
''')
body(20, '''
path('arch',(4,20),[('A',(24,8),20,12,True),('A',(44,20),20,12,True)])
line('tick',(24,8),(24,12));join('tick','arch')
for x in (4,44):line(f'end-{x}',(x,20),(x+(4 if x==4 else -4),20));join(f'end-{x}','arch')
circle('hub',24,23,3);line('needle',(27,23),(31,19));join('needle','hub')
for x in (6,34):
    poly(f'f-{x}',(x,40),(x,28),(x+8,28))
    line(f'fbar-{x}',(x,36),(x+6,36));join(f'fbar-{x}',f'f-{x}')
''')
if __name__=='__main__':
    for i in map(int,sys.argv[1:]):a.run(i)
