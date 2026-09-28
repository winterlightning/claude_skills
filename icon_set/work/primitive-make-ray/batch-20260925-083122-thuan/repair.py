from pathlib import Path
import json,textwrap
root=Path('icon_set/work/primitive-make-ray/batch-20260925-083122-thuan');rows=json.loads((root/'manifest.json').read_text())
def replace(i,a,b):
 p=Path(rows[i-1]['module']);s=p.read_text();assert a in s;p.write_text(s.replace(a,b))
def body(i,s):
 p=Path(rows[i-1]['module']);t=p.read_text();prefix=t[:t.index('        join=lambda')]+"        join=lambda a,b:self.relate('connect',a,b)\n";p.write_text(prefix+textwrap.indent(textwrap.dedent(s),'        '))
replace(1,"(20,15)","(20,13)")
replace(1,"(11,14),(8,11)","(11,12),(8,9)")
replace(3,"(24,31),(29,29),(32,36)","(24,30),(29,28),(31,33)")
body(7,'''
# Exact 9:12:15 globe-axis attachment vectors; support uses 12:16:20.
path('globe',(17,7),[('A',(26,4),15,15,True),('A',(41,19),15,15,True),('A',(35,31),15,15,True),('A',(26,34),15,15,True),('A',(11,19),15,15,True),('A',(17,7),15,15,True)],True)
path('support',(14,3),[('A',(6,19),20,20,False),('A',(26,39),20,20,False),('A',(38,35),20,20,False)])
line('axis-top',(14,3),(17,7));join('axis-top','globe');join('axis-top','support')
line('axis-bottom',(35,31),(38,35));join('axis-bottom','globe');join('axis-bottom','support')
path('land',(26,4),[('C',(20,11),(26,9),(20,7)),('C',(25,16),(20,15),(25,12)),('C',(26,26),(29,20),(29,26)),('C',(20,22),(22,26),(20,25)),('C',(11,19),(20,18),(15,21))]);join('land','globe')
line('post',(26,39),(26,44));join('post','support')
poly('foot',(14,44),(26,44),(38,44));join('post','foot')
''')
body(8,'''
# Radius 13 roll and radius 5 hub give exactly 4px ink clearance analytically.
path('roll',(6,21),[('A',(19,8),13,13,True),('A',(32,21),13,13,True),('A',(31,26),13,13,True),('A',(19,34),13,13,True),('A',(7,26),13,13,True),('A',(6,21),13,13,True)],True)
circle('hub',19,21,5)
poly('body',(7,26),(4,26),(4,42),(44,42),(44,26),(31,26));join('body','roll')
''')
rows[6]['note']='Restore recognizable land detail within the tilted desk globe, exact axis connections and a stable foot.'
rows[6]['omissions']='Fine coastline detail reduced to one continuous land boundary; shallow outlined pedestal reduced to a clear horizontal foot.'
(root/'manifest.json').write_text(json.dumps(rows,indent=2))
