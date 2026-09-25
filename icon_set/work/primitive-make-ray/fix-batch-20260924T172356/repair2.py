from pathlib import Path
import json,textwrap
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924T172356/manifest.json'
B=Path('icon_set/work/primitive-make-ray/fix-batch-20260924T172356');es={e['index']:e for e in json.loads((B/'manifest.json').read_text())}
def edit(i,a,b):
 p=Path(es[i]['module']);s=p.read_text();assert a in s,(i,a);p.write_text(s.replace(a,b))
def body(i,s):
 p=Path(es[i]['module']);p.write_text(p.read_text().split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(s).strip()+'\n','        '))
edit(0,"('low',8,30),('high',20,18)","('low',8,32),('high',20,16)")
edit(0,"('L',(32,24)),('L',(36,24)),",'')
edit(0,"self.relate('connect','stem','bowls')","self.relate('connect','stem','bowls')\n        self.add_line('middle',(32,24),(36,24));self.relate('connect','middle','bowls');self.relate('connect','middle','stem')")
body(7,'''
self.circle('globe',24,24,20)
for n,x,y in [('a',24,16),('b',16,28),('c',32,28)]:self.circle(n,x,y,3)
for n,flip in [('ab',False),('ac',True)]:
    def p(x,y):return (48-x,y) if flip else (x,y)
    self.path(n,p(21,16),[('C',p(16,25),p(18,17),p(16,21))]);self.relate('connect',n,'a');self.relate('connect',n,'c' if flip else 'b')
self.add_line('bc',(19,28),(29,28));self.relate('connect','bc','b');self.relate('connect','bc','c')
''')
edit(9,"(11,12)","(10,12)")
body(14,'''
self.add_polyline('nib',(6,42),(14,22),(24,16),(32,24),(28,36),closed=True)
self.add_polyline('cap',(24,16),(34,6),(42,14),(32,24));self.relate('connect','nib','cap')
self.add_line('slit',(6,42),(20,28));self.relate('connect','slit','nib')
self.add_polyline('plus-h',(6,10),(10,10),(14,10));self.add_polyline('plus-v',(10,6),(10,10),(10,14));self.relate('connect','plus-h','plus-v')
''')
edit(15,"(37,32)","(38,32)")
edit(17,"self.path('dollar',(28,19),[('C',(24,18),(27,18),(25,18)),('C',(24,24),(17,18),(17,23)),('C',(24,30),(31,25),(31,30)),('C',(20,29),(22,30),(21,30))])","self.path('dollar',(28,18),[('C',(24,17),(27,17),(25,17)),('C',(24,24),(17,17),(17,23)),('C',(24,31),(31,25),(31,31)),('C',(20,30),(22,31),(21,31))])")
edit(17,"(24,16),(24,18)","(24,16),(24,17)");edit(17,"(24,30),(24,32)","(24,31),(24,32)")
for i in (18,19):
 edit(i,"self.path('face',(16,19),[('C',(24,12),(19,16),(22,14)),('C',(32,19),(26,14),(29,16)),('L',(32,21)),('A',(16,21),8,8,True),('L',(16,19))],True)","self.path('face',(17,20),[('C',(24,13),(20,18),(22,15)),('C',(31,20),(26,15),(28,18)),('L',(31,22)),('A',(17,22),7,7,True),('L',(17,20))],True)")
