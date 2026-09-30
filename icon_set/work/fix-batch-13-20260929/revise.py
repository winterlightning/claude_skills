import author as a
import sys
D=a.DESIGNS
def body(i,s):D[i]['body']=a.textwrap.dedent(s).strip()
body(2, '''
path('dome',(6,42),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,42)),('L',(6,42))],True)
path('body',(20,24),[('A',(28,24),4,7,True),('L',(28,30)),('A',(20,30),4,4,True),('L',(20,24))],True)
for side in (-1,1):
    x=24+side*4
    for k,y,ox,oy in [('upper',24,8,19),('middle',27,10,27),('lower',30,10,34)]:
        line(f'leg-{side}-{k}',(x,y),(24+side*ox,oy));join(f'leg-{side}-{k}','body')
''')
D[3]['keyshape']='SQUARE'
body(3, '''
path('loop',(24,42),[('A',(42,24),18,18,False),('A',(24,6),18,18,False),('A',(6,24),18,18,False)])
poly('head',(6,16),(6,24),(12,24));join('head','loop')
circle('hub',24,24,4)
''')
body(4, '''
path('upper',(6,15),[('A',(24,6),18,9,True),('A',(42,24),18,18,True)])
poly('upper-head',(32,24),(42,24),(42,14));join('upper-head','upper')
path('lower',(42,33),[('A',(24,42),18,9,True),('A',(6,24),18,18,True)])
poly('lower-head',(16,24),(6,24),(6,34));join('lower-head','lower')
''')
# Detached head has circular jaw bottom 22, shoulder top30: 8 centerline /4 ink.
D[5]['body']=D[5]['body'].replace('(4,36)','(4,40)').replace('(14,26),10,10','(14,30),10,10').replace('(24,36)','(24,40)')
body(6, '''
nodes=[((24,24),(24,6)),((24,24),(42,14)),((24,24),(42,34)),((24,24),(24,42)),((24,24),(6,34)),((24,24),(6,14))]
for i,(p,q) in enumerate(nodes): line(f'ray-{i}',p,q)
for i in range(6):
    for j in range(i):join(f'ray-{i}',f'ray-{j}')
for n,p in [('top',[(17,7),(24,14),(31,7)]),('bottom',[(17,41),(24,34),(31,41)]),('ul',[(6,23),(15,19),(15,11)]),('ur',[(33,11),(33,19),(42,23)]),('ll',[(6,25),(15,29),(15,37)]),('lr',[(33,37),(33,29),(42,25)])]:poly(n,*p)
for x,y in [('top','ray-0'),('bottom','ray-3'),('ul','ray-5'),('ur','ray-1'),('ll','ray-4'),('lr','ray-2')]:join(x,y)
''')
D[7]['body']=D[7]['body'].replace('(4,10)','(4,9)').replace('(10,10)','(10,9)')
body(8, '''
box('sausage',6,6,42,14,4)
line('score',(24,6),(28,14));join('score','sausage')
path('egg',(6,32),[('A',(16,23),10,9,True),('B',(24,32),(23,23),(24,26)),('A',(16,42),8,10,True),('A',(6,32),10,10,True)],True)
self.add_dot('yolk',(15,32))
path('bacon-left',(34,23),[('B',(34,42),(40,29),(28,35))])
path('bacon-right',(42,23),[('B',(42,42),(48,29),(36,35))])
''')
# Pin fit: tall crown above map, open center omitted rather than pinching it.
body(12, '''
path('pin',(24,25),[('L',(16,15)),('A',(32,15),8,11,True),('L',(24,25))],True)
poly('map',(8,36),(19,34),(29,36),(40,34),(40,42),(29,44),(19,42),(8,44),closed=True)
line('fold-left',(19,34),(19,42));line('fold-right',(29,36),(29,44));join('fold-left','map');join('fold-right','map')
''')
D[12]['omissions']='Pin center mark omitted to keep the tall pointed silhouette and full clearance to map.'
D[13]['body']=D[13]['body'].replace('(14,24)','(12,24)')
D[14]['body']=D[14]['body'].replace('(22,17),(31,17)','(23,17),(30,17)')
body(15, '''
path('shell',(4,40),[('A',(44,40),20,20,True),('L',(4,40))],True)
path('lettuce',(4,28),[('A',(12,16),8,12,True),('A',(24,8),12,8,True),('A',(36,16),12,8,True),('A',(44,28),8,12,True)])
''')
D[15]['omissions']='Detached scalloped lettuce crest leaves explicit separation from the shell; tiny bumps omitted.'
body(16, '''
box('cap',18,8,30,16,4)
line('column',(24,16),(24,32));join('column','cap')
line('rib',(18,24),(30,24));join('rib','column')
poly('base',(14,40),(14,32),(24,32),(34,32),(34,40),(14,40),closed=True);join('column','base')
poly('left-bolt',(8,8),(4,19),(10,19),(6,29))
poly('right-bolt',(42,8),(38,19),(44,19),(40,29))
''')
body(17, '''
path('shell',(24,42),[('L',(9,30)),('A',(6,24),6,6,True),('A',(12,15),6,9,True),('A',(18,9),6,6,True),('A',(30,9),6,3,True),('A',(36,15),6,6,True),('A',(42,24),6,9,True),('A',(39,30),6,6,True),('L',(24,42))],True)
line('rib-center',(24,16),(24,31))
line('rib-left',(14,20),(16,24));line('rib-right',(34,20),(32,24))
''')
D[20]['body']=D[20]['body'].replace('(32,18)','(31,19)')
if __name__=='__main__':
    for i in map(int,sys.argv[1:]):a.run(i)
