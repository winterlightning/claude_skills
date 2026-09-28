from pathlib import Path
import json,textwrap
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924/manifest.json'
es={e['index']:e for e in json.loads(Path('icon_set/work/primitive-make-ray/fix-batch-20260924/manifest.json').read_text())}
def edit(i,old,new):
 p=Path(es[i]['module']);s=p.read_text();assert old in s,(i,old);p.write_text(s.replace(old,new))
def body(i,s):
 p=Path(es[i]['module']);p.write_text(p.read_text().split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(s).strip()+'\n','        '))
body(4,'''
for name,flip in [('upper',False),('lower',True)]:
    def p(x,y):return (48-x,48-y) if flip else (x,y)
    self.path(name,p(6,22),[('C',p(24,6),p(6,13),p(14,6)),('C',p(42,18),p(32,6),p(38,12))])
    self.add_polyline(name+'-head',p(32,18),p(42,18),p(42,6))
    self.relate('connect',name,name+'-head')
''')
# Open gear inner radius by reducing scallop depth.
edit(6,"(30,11),(29,6),(28,10)","(30,9),(29,6),(28,9)")
edit(6,"(35,10),(32,12),(33,9)","(35,10),(32,9),(33,9)")
edit(6,"(37,18),(39,15),(36,16)","(39,18),(39,15),(39,16)")
edit(6,"(42,21),(38,20),(42,19)","(42,21),(39,20),(42,19)")
edit(9,"(24,27),(38,19),(29,20)","(24,27),(38,20),(29,22)")
edit(9,"(27,14),(25,18),(27,16)","(25,14),(24,16),(25,15)")
edit(9,"(22,8),(27,10),(25,8)","(21,8),(25,10),(24,8)")
edit(9,"(14,12),(18,8),(16,10)","(13,12),(17,8),(15,10)")
edit(9,"(37,29),(28,33),(34,33)","(37,27),(28,30),(33,30)")
body(11,'''
self.path('left',(7,10),[('C',(4,24),(5,13),(4,19)),('C',(7,38),(4,29),(5,35))])
self.path('right',(41,10),[('C',(44,24),(43,13),(44,19)),('C',(41,38),(44,29),(43,35))])
self.path('flame',(23,8),[('C',(30,22),(28,12),(30,17)),('C',(32,31),(31,25),(32,27)),('C',(24,40),(32,36),(29,40)),('C',(16,31),(19,40),(16,36)),('C',(23,8),(16,24),(26,19))],True)
''')
# A bun joins at top of head through a genuine shared node; pins join bun sides.
body(12,'''
self.path('head',(24,12),[('A',(33,21),9,9,True),('A',(15,21),9,9,True),('A',(24,12),9,9,True)],True)
self.path('bun',(24,12),[('C',(18,8),(20,12),(18,11)),('C',(24,4),(18,6),(21,4)),('C',(30,8),(27,4),(30,6)),('C',(24,12),(30,11),(28,12))],True)
self.add_line('pin-left',(8,4),(18,8));self.add_line('pin-right',(40,4),(30,8))
for n in ('pin-left','pin-right'):self.relate('connect',n,'bun')
self.relate('connect','head','bun')
self.path('shoulders',(8,44),[('A',(14,38),6,6,True),('L',(34,38)),('A',(40,44),6,6,True)])
''')
# Split tower at exact integer facade attachment nodes; tangent vectors aligned.
body(13,'''
self.path('tower',(24,4),[('C',(14,16),(21,4),(17,9)),('C',(10,28),(11,23),(10,24)),('C',(16,44),(10,34),(13,41)),('L',(26,44)),('L',(32,44)),('C',(37,35),(34,41),(36,39)),('C',(38,28),(38,31),(38,30)),('C',(34,16),(38,24),(37,23)),('C',(24,4),(31,9),(27,4))],True)
self.add_line('facade-one',(14,16),(37,35));self.add_line('facade-two',(10,28),(26,44))
self.relate('connect','tower','facade-one');self.relate('connect','tower','facade-two')
''')
body(14,'''
self.add_polyline('trend',(4,10),(22,28),(28,22),(44,38))
self.add_polyline('arrow',(32,38),(44,38),(44,26))
self.relate('connect','trend','arrow')
''')
edit(15,"(36,12)","(37,11)");edit(15,"(12,36)","(11,37)")
edit(16,"(17,30)","(16,28)");edit(16,"(8,30)","(8,28)");edit(16,"('A',(4,28),4,4,True)","('L',(4,28))")
# Put crossbar junctions at explicit endpoints; steep central stroke crosses without lingering near the bars.
body(17,'''
self.path('currency',(14,6),[('C',(24,4),(17,4),(20,4)),('C',(34,12),(30,4),(34,7)),('C',(27,20),(34,15),(30,18)),('C',(21,28),(24,22),(24,26)),('C',(14,36),(18,30),(14,33)),('C',(24,44),(14,41),(18,44)),('C',(34,42),(28,44),(31,44))])
self.add_polyline('upper',(8,20),(27,20),(40,20));self.add_polyline('lower',(8,28),(21,28),(40,28))
self.relate('connect','currency','upper');self.relate('connect','currency','lower')
''')
edit(18,"(22,13),(21,6),(22,10)","(21,15),(21,6),(21,11)")
edit(18,"(26,13),(23,11),(25,11)","(27,15),(23,13),(25,13)")
edit(18,"(31,6),(26,10),(27,6)","(31,6),(27,11),(27,6)")
edit(18,"(20,26)","(21,26)");edit(18,"(28,26),(20,30),(28,30)","(27,26),(21,29),(27,29)")
