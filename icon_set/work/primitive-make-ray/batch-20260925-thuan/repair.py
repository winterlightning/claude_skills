from pathlib import Path
import json,textwrap
root=Path('icon_set/work/primitive-make-ray/batch-20260925-thuan');rows=json.loads((root/'manifest.json').read_text())
def replace(i,a,b):
 p=Path(rows[i-1]['module']);s=p.read_text();assert a in s,(i,a);p.write_text(s.replace(a,b))
def body(i,s):
 p=Path(rows[i-1]['module']);t=p.read_text();prefix=t[:t.index('        join=lambda')];prefix+='        join=lambda a,b:self.relate(\'connect\',a,b)\n';p.write_text(prefix+textwrap.indent(textwrap.dedent(s),'        '))
replace(2,"('L',(24,13))","('L',(24,12))")
replace(2,"line('base-seam'","join('finial','piece')\n        line('base-seam'")
replace(3,"('C',(16,41),(19,36),(19,42)),('C',(10,40),(13,44),(11,42))","('C',(15,42),(19,36),(19,42)),('C',(10,40),(12,42),(11,42))")
replace(4,"path('stem',(39,17)","path('stem',(41,21)")
replace(4,"(42,17),(44,15)","(43,19),(44,15)")
p=Path(rows[3]['module']);p.write_text(p.read_text()+"        join('stem','pepper')\n")
replace(7,"('L',(21,22)),('L',(30,22))","('L',(21,20)),('L',(30,20))")
body(8,'''
# Two diagonally aligned parts share a short exposed tang; blade stays above wood.
path('tool',(20,22),[('L',(29,13)),('L',(26,10)),('L',(34,2)),('A',(40,8),4,4,True),('L',(32,16)),('L',(29,13))])
path('blade',(20,22),[('L',(14,28)),('A',(8,22),4,4,True),('L',(14,16)),('L',(20,22))],True)
join('blade','tool')
path('wood',(6,34),[('L',(14,34)),('C',(24,37),(18,34),(19,37)),('C',(36,32),(29,37),(30,32)),('L',(42,32)),('L',(42,45)),('L',(6,45)),('L',(6,34))],True)
''')
for i in (9,10):
 body(i,'''
path('hinge',(35,10),[('A',(37,14),5,5,True),('A',(32,19),5,5,True),('A',(28,17),5,5,True),('A',(27,14),5,5,True),('A',(32,9),5,5,True),('A',(35,10),5,5,True)],True)
line('grip',(35,10),(42,6));join('grip','hinge')
poly('left-leg',(28,17),(17,25),(6,33));join('left-leg','hinge')
poly('right-leg',(32,19),(29,28),(24,42));join('right-leg','hinge')
line('brace',(17,25),(29,28));join('brace','left-leg');join('brace','right-leg')
''')
replace(12,"(42,12)","(40,12)")
body(15,'''
path('bow',(22,24),[('A',(26,32),10,10,True),('A',(16,42),10,10,True),('A',(6,32),10,10,True),('A',(16,22),10,10,True),('A',(22,24),10,10,True)],True)
poly('shaft',(22,24),(28,18),(38,6),(42,10))
line('inner-tooth',(28,18),(33,23));join('bow','shaft');join('shaft','inner-tooth')
''')
replace(17,"19,18,3","20,19,3")
replace(17,"31,29,3","30,28,3")
replace(18,"(37,30)","(37,32)")
replace(18,"('C',(37,32),(30,40),(37,36))","('C',(27,39),(23,40),(25,40)),('C',(37,32),(33,37),(37,36))")
p=Path(rows[17]['module']);p.write_text(p.read_text()+"        join('neck','face')\n")
body(19,'''
# Eye remains naturally shallow; exact named cubic endpoints own all five lashes.
path('lid',(4,13),[('C',(9,19),(6,16),(7,17)),('C',(16,23),(11,21),(13,22)),('C',(24,25),(19,24),(21,25)),('C',(32,23),(27,25),(29,24)),('C',(39,19),(35,22),(37,21)),('C',(44,13),(41,17),(42,16))])
for j,(a,b) in enumerate([((9,19),(4,24)),((16,23),(12,32)),((24,25),(24,35)),((32,23),(36,32)),((39,19),(44,24))]):
    line(f'lash-{j}',a,b);join('lid',f'lash-{j}')
''')
replace(20,"path('flap',(5,12)","path('flap',(4,13)")
replace(20,"('L',(43,12))","('L',(44,13))")
p=Path(rows[19]['module']);p.write_text(p.read_text()+"        join('flap','envelope')\n")
