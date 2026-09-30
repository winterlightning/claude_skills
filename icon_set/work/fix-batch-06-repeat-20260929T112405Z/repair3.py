from author import author,ROOT
import json
H='Human full_body_ref.png: circular heads and exact 4-unit detached head gap'
s=json.loads((ROOT/'specs2.json').read_text())
code=s['11'].replace("('L',(38,22))","('L',(40,22))");exec(code);s['11']=code
author(15,'''
path('body',(4,26),[('L',(4,22)),('A',(8,18),4,4,True),('L',(16,18)),('L',(24,8)),('L',(32,8)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,26)),('L',(36,26)),('L',(12,26)),('L',(4,26))],True)
for x in (12,36):
 circle(f'wheel-{x}',x,37,3)
 line(f'axle-{x}',(x,26),(x,34));join(f'axle-{x}','body');join(f'axle-{x}',f'wheel-{x}')
poly('hood',(16,18),(8,8),(4,8));join('hood','body')
''','The rejected car floated above detached wheels and had a short hood stub. Connected the wheels to the chassis, rounded the bumpers and raised a clearly hinged hood. Omitted window divisions.','HRECT_L','Lucide car: rounded body and matched wheels; source raised hood')
author(17,'''
path('fruit',(24,22),[('A',(38,33),14,11,True),('A',(24,44),14,11,True),('A',(10,33),14,11,True),('A',(24,22),14,11,True)],True)
poly('stem',(24,22),(20,14),(16,6));join('stem','fruit')
path('leaf',(20,14),[('C',(38,4),(20,4),(28,4)),('C',(20,14),(38,14),(28,14))],True);join('leaf','stem')
''','The rejected tangerine was flattened beneath a large leaf. Made the fruit rounder by narrowing its width and increasing its height, with a compact broad leaf and short stem.','VRECT_M','Lucide sprout: broad pointed leaf attached to stem')
code=s['19'].replace("('C',(32,34),(42,32),(36,34)),('C',(18,34),(28,36),(22,36)),('C',(10,23),(12,33),(10,29))","('C',(32,33),(42,31),(36,33)),('C',(24,34),(30,34),(27,34)),('C',(18,32),(21,34),(19,33)),('C',(10,23),(12,31),(10,29))")
code=code.replace('(18,34),(18,40),(14,42)','(18,32),(18,40),(16,42)').replace('(32,34),(32,40),(28,42)','(32,33),(32,40),(34,42)')
exec(code);s['19']=code
author(16,'''
circle('left-head',9,15,3)
line('left-torso',(9,26),(9,32));poly('left-arms',(4,29),(9,26),(14,29));join('left-arms','left-torso')
poly('left-legs',(5,40),(9,32),(13,40));join('left-legs','left-torso')
self.mark_human_figure('left',head='left-head',torso='left-torso',torso_junction='start')
circle('right-head',36,11,3)
poly('dress',(36,22),(44,36),(40,36),(32,36),(28,36),(36,22))
line('right-leg-left',(32,36),(32,40));line('right-leg-right',(40,36),(40,40));join('right-leg-left','dress');join('right-leg-right','dress')
circle('note',23,18,2);line('stem',(25,18),(25,8));join('stem','note')
''','The rejected duet used two identical stick figures. Restored the right singer in a dress and the left singer in trousers with a central musical note. Both heads have an exact four-unit ink gap to their bodies; reduced two notes to one.','HRECT_L',H+'; Lucide music-2: note head and stem')
(ROOT/'specs3.json').write_text(json.dumps(s,indent=2))
