from pathlib import Path
import json
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
def replace(i,a,b):
 p=next(Path(rows[i]['result_dir']).glob('*.py'));s=p.read_text();assert a in s,(i,a);p.write_text(s.replace(a,b))
def geometry(i,s):
 p=next(Path(rows[i]['result_dir']).glob('*.py'));t=p.read_text();t=t[:t.index("        join=lambda")]+"        join=lambda a,b:self.relate('connect',a,b)\n"+'\n'.join('        '+l for l in s.strip().splitlines())+'\n';p.write_text(t)
geometry(0,"""
path('head',(42,16),[('C',(38,6),(42,12),(40,8)),('L',(34,14)),('L',(24,14)),('L',(16,14)),('A',(16,22),4,4,False),('L',(28,22)),('A',(28,32),5,5,True),('L',(26,34)),('A',(30,40),5,4,False),('L',(36,36)),('L',(42,42))])
circle('ball',12,36,6)
""")
geometry(2,"""
path('dog',(28,18),[('C',(24,6),(28,12),(28,6)),('L',(20,12)),('L',(10,14)),('A',(16,22),6,8,False),('L',(20,22)),('L',(20,30)),('L',(12,26)),('C',(6,30),(8,24),(6,26)),('C',(10,34),(6,32),(8,33)),('L',(20,38)),('L',(26,38)),('C',(20,42),(24,40),(20,38)),('L',(32,42)),('A',(38,30),6,12,False),('L',(28,18))],True)
path('tail',(38,30),[('A',(42,18),4,12,False)]);join('dog','tail')
""")
geometry(6,"""
path('mouse',(6,28),[('A',(18,16),12,12,True),('A',(30,28),12,12,True),('L',(30,30)),('A',(6,30),12,12,True),('L',(6,28))],True)
poly('button',(18,16),(18,28),(30,28));join('button','mouse')
path('wave-inner',(26,6),[('C',(32,14),(30,7),(32,10))])
path('wave-outer',(38,6),[('C',(42,22),(42,12),(42,18))])
""")
geometry(7,"""
for x in (12,36):
 n=f'earring-{x}'
 path(n+'-hook',(x-6,10),[('A',(x+6,10),6,6,True),('A',(x,16),6,6,True)])
 circle(n+'-bead',x,19,3)
 poly(n+'-drop',(x,24),(x+6,32),(x,40),(x-6,32),(x,24))
 line(n+'-link',(x,22),(x,24));join(n+'-link',n+'-bead');join(n+'-link',n+'-drop')
 join(n+'-hook',n+'-bead')
""")
replace(7,'Keyshape.VRECT_L','Keyshape.HRECT_L')
# hooks currently y4, drops y40 need square x6..42 y6..42 instead
replace(7,'Keyshape.HRECT_L','Keyshape.SQUARE')
replace(7,"(x-6,10),[('A',(x+6,10),6,6,True),('A',(x,16),6,6,True)]","(x-6,12),[('A',(x+6,12),6,6,True),('A',(x,18),6,6,True)]")
replace(7,"x,19,3","x,21,3")
replace(7,"(x,24),(x+6,32),(x,40),(x-6,32),(x,24)","(x,26),(x+6,34),(x,42),(x-6,34),(x,26)")
replace(7,"(x,22),(x,24)","(x,24),(x,26)")
geometry(8,"""
circle('globe',19,15,11)
path('meridian',(34,4),[('A',(40,20),22,22,True),('A',(24,36),16,16,True),('C',(8,32),(18,36),(12,35))])
line('stem',(24,36),(24,44));poly('base',(12,44),(24,44),(36,44));join('stem','base');join('stem','meridian')
""")
replace(9,'p(14,24),p(18,22)','p(14,19),p(18,19)')
replace(9,'p(14,24),p(18,26)','p(14,29),p(18,29)')
replace(10,"('A',(36,6),6,5,True)","('C',(36,6),(30,8),(32,6))")
replace(10,"('C',(32,22),(42,16),(34,19))","('C',(33,22),(42,16),(35,19))")
geometry(11,"""
path('eye',(18,14),[('C',(30,6),(22,8),(26,6)),('C',(42,18),(36,6),(40,12)),('C',(30,30),(38,26),(34,30))])
circle('iris',30,17,2)
circle('lens',15,33,9)
""")
# separated eye endpoint and lens need more separation; shorten eye lower limb
replace(11,"('C',(30,30),(38,26),(34,30))","('C',(32,28),(38,26),(36,28))")
replace(12,"('A',(36,8),4,4,True)","('C',(36,8),(34,6),(35,6))")
replace(12,"('A',(40,24),4,4,True)","('C',(40,24),(42,22),(42,23))")
geometry(13,"""
path('tool',(24,14),[('L',(30,8)),('C',(40,18),(38,0),(48,10)),('L',(34,24)),('L',(16,34)),('L',(6,36)),('L',(8,26)),('L',(24,14))],True)
poly('collar',(18,6),(24,14),(34,24));join('collar','tool')
circle('sample',38,38,4)
""")
# coherent quarter round bulb touching exact top and right bounds
replace(13,"('C',(40,18),(38,0),(48,10))","('A',(42,18),12,12,True)")
# top of quadrant is 6 when start 30,6; use aligned quarter
replace(13,"('L',(30,8)),('A',(42,18),12,12,True)","('L',(30,6)),('A',(42,18),12,12,True)")
geometry(14,"""
path('tool',(24,14),[('L',(32,6)),('A',(42,16),10,10,True),('L',(28,30)),('L',(20,32)),('L',(22,24)),('L',(24,14))],True)
poly('collar',(20,10),(24,14),(34,24));join('collar','tool')
path('outline',(12,22),[('A',(6,28),6,6,False),('C',(16,42),(6,34),(12,40))])
""")
replace(15,"(18,36),[('C',(38,8),(30,30),(38,18))]","(22,34),[('C',(38,8),(32,28),(38,18))]")
replace(15,"(4,40),(6,40)","(4,40),(5,40)")
replace(15,"(12,38),(13,38)","(13,38),(14,38)")
replace(16,"(26,24)","(24,24)");replace(16,"('L',(26,10))","('L',(24,10))");replace(16,"('A',(36,10),5,6,True)","('A',(36,10),6,6,True)")
geometry(17,"""
path('body',(6,18),[('L',(6,38)),('A',(10,42),4,4,False),('L',(30,42)),('A',(34,38),4,4,False),('L',(34,30)),('L',(34,18))])
path('foam',(6,18),[('C',(10,10),(6,14),(6,10)),('C',(22,6),(10,6),(18,6)),('C',(30,10),(26,6),(30,6)),('A',(34,14),4,4,True),('L',(34,18)),('L',(18,18)),('C',(6,18),(14,22),(6,22))])
path('handle',(34,18),[('A',(34,30),8,6,True)])
join('body','foam');join('body','handle');join('foam','handle')
for x in (15,25):line(f'rib-{x}',(x,29),(x,33))
""")
replace(18,"('C',(16,38),(4,42),(10,40))","('A',(10,40),6,6,False),('C',(16,38),(12,40),(14,39))")
geometry(19,"""
path('sole',(10,14),[('A',(16,4),6,10,True),('A',(22,10),6,6,True),('A',(30,10),4,4,True),('A',(38,18),8,8,True),('L',(36,24)),('L',(34,32)),('A',(24,44),10,12,True),('A',(10,32),14,12,True),('L',(10,24)),('L',(10,14))],True)
path('arch',(10,24),[('C',(24,20),(16,24),(20,24)),('C',(36,24),(28,24),(32,24))]);join('arch','sole')
line('heel',(10,32),(34,32));join('heel','sole')
""")
