import egg as r
import sys
a=r.a;D=a.DESIGNS;body=r.body
D[2]['body']=D[2]['body'].replace("('middle',27,10,27),('lower',30,10,34)","('middle',27,9,27),('lower',30,9,33)")
body(8, '''
box('sausage',6,6,42,14,4)
line('score',(24,6),(28,14));join('score','sausage')
path('egg',(6,32),[('A',(16,23),10,9,True),('B',(24,32),(23,23),(24,26)),('A',(16,42),8,10,True),('A',(6,32),10,10,True)],True)
self.add_dot('yolk',(15,32))
path('bacon',(34,23),[('B',(34,42),(34,30),(32,34)),('L',(42,42)),('B',(42,23),(42,34),(42,30)),('L',(34,23))],True)
''')
body(15, '''
path('shell',(4,40),[('A',(44,40),20,16,True),('L',(4,40))],True)
path('lettuce',(4,40),[('L',(4,24)),('A',(12,16),8,8,True),('A',(24,8),12,8,True),('A',(36,16),12,8,True),('A',(44,24),8,8,True),('L',(44,40))])
join('lettuce','shell')
''')
D[17]['body']=D[17]['body'].replace('(17,28)','(16,28)').replace('(31,28)','(32,28)')
body(19, '''
# Open lower frame behind shoulders avoids a narrow portrait/background strip.
path('frame',(14,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(34,42))])
path('crown',(18,22),[('A',(30,22),6,7,True)])
path('jaw',(30,22),[('A',(18,22),6,6,True)]);join('crown','jaw')
path('hair-left',(18,22),[('L',(14,34)),('L',(18,34))]);join('hair-left','jaw');join('hair-left','crown')
path('hair-right',(30,22),[('L',(34,34)),('L',(30,34))]);join('hair-right','jaw');join('hair-right','crown')
path('shoulders',(14,42),[('L',(18,34)),('L',(24,36)),('L',(30,34)),('L',(34,42))])
join('shoulders','frame');join('shoulders','hair-left');join('shoulders','hair-right')
''')
if __name__=='__main__':
    for i in map(int,sys.argv[1:]):a.run(i)
