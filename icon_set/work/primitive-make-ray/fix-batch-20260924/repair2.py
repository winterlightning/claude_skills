from pathlib import Path
import json,textwrap
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924/manifest.json'
es={e['index']:e for e in json.loads(Path('icon_set/work/primitive-make-ray/fix-batch-20260924/manifest.json').read_text())}
def edit(i,a,b):
 p=Path(es[i]['module']);s=p.read_text();assert a in s;p.write_text(s.replace(a,b))
def body(i,s):
 p=Path(es[i]['module']);p.write_text(p.read_text().split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(s).strip()+'\n','        '))
edit(4,'p(6,22)','p(6,21)')
edit(6,"(24,14)","(24,16)");edit(6,"(24,34)","(24,32)")
edit(16,"(24,33)","(24,34)")
body(12,'''
# Circular jaw radius 10; coherent coiffure rises into the bun.
self.path('portrait',(18,10),[('A',(30,10),6,6,True),('C',(34,20),(32,13),(34,15)),('A',(14,20),10,10,True),('C',(18,10),(14,15),(16,13))],True)
self.add_line('pin-left',(8,4),(18,10));self.add_line('pin-right',(40,4),(30,10))
for n in ('pin-left','pin-right'):self.relate('connect',n,'portrait')
self.path('shoulders',(8,44),[('A',(14,38),6,6,True),('L',(34,38)),('A',(40,44),6,6,True)])
''')
body(18,'''
# Shared eye-stalk dimensions mirror about x=24; circularly rounded stalk caps.
self.path('face',(12,17),[('C',(16,6),(11,10),(12,6)),('C',(20,16),(20,6),(20,11)),('L',(28,16)),('C',(32,6),(28,11),(28,6)),('C',(36,17),(36,6),(37,10)),('C',(24,38),(37,31),(31,38)),('C',(12,17),(17,38),(11,31))],True)
for name,sgn in [('left',-1),('right',1)]:
    def p(x,y):return (24+sgn*x,y)
    self.path(name,p(12,17),[('C',p(18,42),p(17,26),p(18,35)),('L',p(10,42))])
    self.relate('connect',name,'face')
self.path('smile',(21,26),[('C',(27,26),(21,29),(27,29))])
''')
