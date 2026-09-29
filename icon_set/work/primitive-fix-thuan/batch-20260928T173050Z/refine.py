from author import *
import textwrap
runs=json.loads((BATCH/'runs.json').read_text())
changes={
5:'''self.path('tag',(28,6),(38,6),(42,10,4,4,True),(42,21),
          (40,25,42,23,42,23),(23,42),(19,42,22,43,20,43),(6,29),
          (6,25,5,28,5,26),(24,8),(28,6,25,7,26,6),closed=True)
self.ring('eye',34,14,3)
self.path('g',(26,22),(22,20,25,20,24,20),(17,26,19,20,17,23),
          (23,32,17,30,20,32),(29,26,27,32,29,30),(24,26))''',
11:'''self.path('board',(12,20),(12,8),(19,8),(29,8,5,5,True),(36,8),(36,20))
self.add_line('board-bottom',(15,38),(33,38))
self.add_line('text-1',(19,15),(29,15));self.add_line('text-2',(22,22),(26,22))
for side,s in [('left',1),('right',-1)]:
    def p(x,y):return (24+s*(x-24),y)
    def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
    self.path(side+'-outer',p(5,43),p(5,30),c(12,20,5,25,9,23))
    self.path(side+'-grip',p(10,30),p(15,25),c(19,29,18,22,22,25),p(16,34),
              c(15,38,15,35,15,37),c(12,44,15,40,14,43))
    self.relate('connect',side+'-outer','board')
    self.relate('connect',side+'-grip','board-bottom')''',
12:'''self.path('piece',(22,6),(27,11),
          (35,10,28,4,35,4),(30,15,35,14,32,16),(35,20),(24,31),(11,18),(15,14),
          (20,9,22,21,27,13),(22,6),closed=True)
self.cups(27,44)''',
14:'''self.ring('rim',24,8,9,4)
self.path('pot',(15,8),(15,18,16,12,14,14),(24,27,15,24,19,27),
          (33,18,29,27,33,24),(33,8,34,14,32,12))
self.relate('connect','rim','pot')
self.cups(25,44)''',
19:'''self.path('head',(22,6),(15,13),(19,17),(25,23),(29,34,28,26,29,30),
          (42,21,37,32,40,27),(31,17,38,20,34,19),(22,6),closed=True)
self.path('handle',(19,17),(7,35),(6,38,6,36,6,37),
          (10,42,6,40,8,42),(13,41,11,42,12,42),(25,23))
self.relate('connect','head','handle')'''
}
for n,body in changes.items():
 prev=ROOT/runs[n-1]['module'];helpers=prev.read_text().split('    def path(self, name, start, *steps, closed=False):')[1]
 run,module=create(n,3,textwrap.dedent(body).strip())
 code=module.read_text().split('    def path(self, name, start, *steps, closed=False):')[0]
 module.write_text(code+'    def path(self, name, start, *steps, closed=False):'+helpers)
 runs[n-1]=dict(n=n,run=str(run.relative_to(ROOT)),module=str(module.relative_to(ROOT)))
(BATCH/'runs.json').write_text(json.dumps(runs,indent=2))
print('Refined',len(changes),'candidates')
