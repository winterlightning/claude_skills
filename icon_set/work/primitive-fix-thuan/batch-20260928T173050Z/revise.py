from author import *
import textwrap
# Every revised candidate gets a fresh run. Shared hand ownership changes all corresponding instances.
HELPERS_NEW=HELPERS[:HELPERS.index('    def cups')]+'''
    def cups(self,top=24,bottom=44):
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            self.path(side+'-hand',p(11,bottom),c(4,top+9,11,bottom-4,4,top+14),p(4,top),
                      (*p(10,top),3,3,s==1),p(10,top+7),
                      c(14,top+5,10,top+4,12,top+3),p(18,top+10),
                      c(20,top+14,19,top+11,20,top+12),p(20,bottom))
            self.add_line(side+'-thumb-crease',p(10,top+7),p(14,top+12))
            self.relate('connect',side+'-hand',side+'-thumb-crease')
'''
updates={}
updates[1]=D[1]['body'].replace("('upper',20,6,22,23),('lower',10,23,17,19)","('upper',21,6,21,20),('lower',11,25,15,17)")
updates[2]='''
self.path('g',(29,7),(24,5,28,5,26,5),(16,13,19,5,16,8),
          (24,21,16,18,19,21),(32,13,29,21,32,18),(25,13))
self.path('p',(4,44),(4,30),(8,30),(8,38,4,4,True),(4,38))
self.ring('a',25,39,4)
self.path('a-stem',(29,35),(29,39),(29,43));self.relate('connect','a','a-stem')
self.path('y',(37,32),(41,38),(45,32))
self.add_line('y-tail',(41,38),(37,44));self.relate('connect','y','y-tail')
'''
D[2]['change']='Redrew G and Pay with rounded readable letters on two rows; retained every letter and deliberately reflowed the long wordmark for the 48px UI canvas.'
D[2]['plan']='Two-row G Pay wordmark with curved G and P, circular a, and descending y; deliberate UI reflow.'
updates[4]=D[4]['body'].replace('(16,23)','(16,22)').replace('(24,23)','(24,22)').replace('(32,23)','(32,22)').replace('(32,37)','(32,38)').replace('(24,37)','(24,38)').replace('(16,37)','(16,38)')
updates[5]='''
self.path('tag',(28,6),(38,6),(42,10,4,4,True),(42,21),
          (40,25,42,23,42,23),(23,42),(19,42,22,43,20,43),(6,29),
          (6,25,5,28,5,26),(24,8),(28,6,25,7,26,6),closed=True)
self.ring('eye',34,14,3)
self.path('g',(27,21),(22,20,25,19,23,19),(16,27,18,20,16,23),
          (23,34,16,31,19,34),(30,27,27,34,30,31),(24,27))
'''
updates[7]='''
self.ring('rim',24,24,20)
self.path('wave',(4,24),(17,12,9,24,9,12),(38,29,25,12,26,29),(44,24,41,29,44,27))
self.relate('connect','rim','wave')
'''
updates[8]='''
# Concentric contours split at mirrored integer diagonal nodes; cubic tangents preserve circular flow.
for name,points,controls in [
 ('outer',[(10,10),(38,10),(38,38),(10,38)],[(18,2,30,2),(46,18,46,30),(30,46,18,46),(2,30,2,18)]),
 ('inner',[(15,15),(33,15),(33,33),(15,33)],[(20,10,28,10),(38,20,38,28),(28,38,20,38),(10,28,10,20)])]:
    steps=[(*points[(i+1)%4],*controls[i]) for i in range(4)]
    self.path(name,points[0],*steps,closed=True)
for name,a,b in [('nw',(10,10),(15,15)),('ne',(38,10),(33,15)),('se',(38,38),(33,33)),('sw',(10,38),(15,33))]:
    self.add_line(name,a,b)
    self.relate('connect','outer',name);self.relate('connect','inner',name)
self.path('loop',(27,28),(24,19,31,23,29,19),(21,28,19,19,17,25))
'''
updates[10]=D[10]['body']
updates[11]='''
self.path('board',(12,20),(12,8),(19,8),(29,8,5,5,True),(36,8),(36,20))
self.add_line('board-bottom',(14,39),(34,39))
self.add_line('text-1',(19,15),(29,15));self.add_line('text-2',(22,22),(26,22))
for side,s in [('left',1),('right',-1)]:
    def p(x,y):return (24+s*(x-24),y)
    def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
    self.path(side+'-outer',p(5,43),p(5,30),c(12,20,5,25,9,23))
    self.path(side+'-grip',p(10,30),p(15,25),c(20,29,18,22,23,25),p(16,35),p(14,39),p(11,44))
    self.relate('connect',side+'-outer','board')
    self.relate('connect',side+'-grip','board-bottom')
'''
updates[12]=D[12]['body'].replace('self.cups(28,44)','self.cups(27,44)')
updates[13]='''
self.path('heart',(18,22),(11,22,15,18,11,18),(18,30,9,24,13,27),
          (25,22,23,27,27,24),(18,22,25,18,21,18),closed=True)
self.path('lower',(4,34),(11,34),(19,37,15,34,17,35),(29,37),
          (37,44,34,37,36,41),(4,44))
self.add_line('palm',(12,37),(19,37));self.relate('connect','lower','palm')
self.path('upper',(44,4),(33,4),(24,10,29,4,26,7))
self.path('upper-thumb',(44,13),(40,13),(35,19),
          (31,15,31,23,28,18),(34,11),(29,10,32,9,31,9))
'''
updates[14]=D[14]['body'].replace('self.cups(27,44)','self.cups(26,44)')
updates[15]='''
self.path('car',(11,13),(15,5),(33,5),(37,13),(37,22),(34,25,3,3,True),
          (14,25),(11,22,3,3,True),(11,13),closed=True)
self.add_line('windshield',(11,13),(37,13));self.relate('connect','car','windshield')
for name,x in [('left',16),('right',30)]:
    self.add_line(name+'-wheel',(x,25),(x,28));self.relate('connect','car',name+'-wheel')
    self.add_dot(name+'-lamp',(x,19))
self.cups(29,44)
'''
# Handshake palm and finger rhythm improved: reduce crowded thumb/left knuckle overlap.
for n in (16,17,18):
 updates[n]=D[n]['body'].replace("self.path('left-top',(9,17),(18,13,12,17,15,13),(23,14,20,13,21,13))", "self.path('left-top',(9,17),(16,12,12,17,14,12),(23,14,19,12,21,13))")
updates[19]=D[19]['body'].replace('(5,35),(11,41,2,40,7,44)','(7,35),(13,41,3,39,9,45)')
# Avoid a tiny closed accent counter: two continuous boundaries imply the brand accent.
updates[20]=D[20]['body'].replace("self.path('accent',(29,16),(32,10),(36,10),(33,15,36,13,35,15),(29,16),closed=True)","self.path('accent',(30,16),(34,10),(36,10))")
import author
author.HELPERS=HELPERS_NEW
runs=json.loads((BATCH/'runs.json').read_text())
for n,body in updates.items():
 run,module=create(n,2,textwrap.dedent(body).strip())
 runs[n-1]=dict(n=n,run=str(run.relative_to(ROOT)),module=str(module.relative_to(ROOT)))
(BATCH/'runs.json').write_text(json.dumps(runs,indent=2))
print('Revised',len(updates),'candidates')
