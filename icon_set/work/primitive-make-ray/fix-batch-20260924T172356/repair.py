from pathlib import Path
import json,textwrap
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924T172356/manifest.json'
B=Path('icon_set/work/primitive-make-ray/fix-batch-20260924T172356');es={e['index']:e for e in json.loads((B/'manifest.json').read_text())}
def edit(i,a,b):
 p=Path(es[i]['module']);s=p.read_text();assert a in s,(i,a);p.write_text(s.replace(a,b))
def body(i,s):
 p=Path(es[i]['module']);p.write_text(p.read_text().split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(s).strip()+'\n','        '))
edit(0,'Keyshape.SQUARE','Keyshape.HRECT_L')
body(0,'''
for n,x,y in [('low',8,30),('high',20,18)]:
    self.path(n,(x,y-4),[('L',(x+4,y-4)),('L',(x+4,y+4)),('L',(x,y+4)),('L',(x-4,y+4)),('L',(x-4,y-4)),('L',(x,y-4))],True)
    self.add_line(n+'-up',(x,8),(x,y-4));self.add_line(n+'-down',(x,y+4),(x,40))
    self.relate('connect',n,n+'-up');self.relate('connect',n,n+'-down')
self.add_polyline('stem',(32,8),(32,12),(32,24),(32,36),(32,40))
self.path('bowls',(32,12),[('L',(36,12)),('A',(36,24),8,6,True),('L',(32,24)),('L',(36,24)),('A',(36,36),8,6,True),('L',(32,36))])
self.relate('connect','stem','bowls')
''')
body(1,'''
self.path('frame',(12,8),[('L',(16,8)),('L',(32,8)),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,17)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,17)),('L',(8,12)),('A',(12,8),4,4,True)],True)
self.add_line('header',(8,17),(40,17));self.relate('connect','header','frame')
for x in (16,32):
    self.add_line('binding-'+str(x),(x,4),(x,8));self.relate('connect','binding-'+str(x),'frame')
self.path('phone',(20,26),[('L',(17,29)),('C',(27,35),(19,33),(24,35)),('L',(31,31)),('L',(29,29))])
''')
body(3,'''
for n,x,y,r in [('top',13,9,5),('bottom',13,39,5),('center',24,24,5),('right',37,14,3)]:self.circle(n,x,y,r)
for n,a,b,left,right in [('top-link',(16,13),(20,21),'top','center'),('bottom-link',(16,35),(24,29),'bottom','center'),('right-link',(28,21),(34,14),'center','right')]:
    self.add_line(n,a,b);self.relate('connect',n,left);self.relate('connect',n,right)
''')
edit(5,"('L',(24,28))","('L',(24,27))")
# Remove zero-length last question segment by omitting the redundant command.
edit(5,",('L',(24,27))",'');edit(5,"(24,36)","(24,35)")
body(7,'''
self.circle('globe',24,24,20)
for n,x,y in [('a',24,15),('b',16,27),('c',32,28)]:self.circle(n,x,y,3)
self.path('ab',(21,15),[('C',(16,24),(18,16),(16,20))]);self.relate('connect','ab','a');self.relate('connect','ab','b')
self.path('ac',(27,15),[('C',(32,25),(30,17),(32,21))]);self.relate('connect','ac','a');self.relate('connect','ac','c')
self.path('bc',(19,27),[('C',(29,28),(22,27),(26,28))]);self.relate('connect','bc','b');self.relate('connect','bc','c')
''')
body(8,'''
self.path('handle',(6,6),[('L',(8,6)),('C',(11,10),(10,6),(11,8)),('L',(15,30))])
self.circle('wheel',15,36,6);self.relate('connect','handle','wheel')
self.add_polyline('load',(25,16),(38,12),(42,25),(29,29),closed=True)
self.add_polyline('platform',(21,36),(29,29),(42,25))
self.relate('connect','wheel','platform');self.relate('connect','load','platform')
''')
edit(9,"(19,42)","(16,42)")
edit(10,"(16,28)","(18,27)")
body(14,'''
self.add_polyline('nib',(6,42),(16,26),(24,18),(32,26),(28,36),closed=True)
self.add_polyline('cap',(24,18),(34,8),(42,16),(32,26));self.relate('connect','nib','cap')
self.add_line('slit',(6,42),(20,28));self.relate('connect','slit','nib')
self.add_polyline('plus-h',(6,12),(12,12),(18,12));self.add_polyline('plus-v',(12,6),(12,12),(12,18));self.relate('connect','plus-h','plus-v')
''')
edit(15,"(35,31)","(37,32)")
# Give the nail a 9-unit vertical margin while preserving its rounded end.
edit(15,"(4,12)","(4,11)");edit(15,"(18,12)","(18,11)");edit(15,"(18,36),12,12", "(18,37),13,13");edit(15,"(4,36)","(4,37)")
edit(16,'Keyshape.CIRCLE','Keyshape.SQUARE')
body(16,'''
for n,flip in [('top',False),('bottom',True)]:
    def p(x,y):return (48-x,48-y) if flip else (x,y)
    self.path(n,p(40,12),[('C',p(24,6),p(36,8),p(31,6)),('A',p(6,24),18,18,False)])
    self.add_polyline(n+'-head',p(6,18),p(6,24),p(12,24));self.relate('connect',n,n+'-head')
self.add_polyline('hands',(24,16),(24,28),(28,28))
''')
edit(17,'Keyshape.HRECT_L','Keyshape.SQUARE')
body(17,'''
self.path('bill',(6,8),[('C',(15,6),(9,6),(12,6)),('C',(33,8),(21,6),(27,8)),('C',(42,6),(37,8),(39,7)),('L',(42,40)),('C',(33,42),(39,42),(36,42)),('C',(15,40),(27,42),(21,40)),('C',(6,42),(11,40),(9,41)),('L',(6,8))],True)
self.path('dollar',(28,19),[('C',(24,18),(27,18),(25,18)),('C',(24,24),(17,18),(17,23)),('C',(24,30),(31,25),(31,30)),('C',(20,29),(22,30),(21,30))])
for n,a,b in [('top',(24,16),(24,18)),('bottom',(24,30),(24,32))]:
    self.add_line(n,a,b);self.relate('connect',n,'dollar')
''')
for i in (18,19):
 edit(i,"(16,18)","(16,19)");edit(i,"(32,18)","(32,19)")
