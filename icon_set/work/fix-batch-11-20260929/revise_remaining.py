from pathlib import Path
import json,shutil
root=Path(__file__).parent;rs=json.loads((root/'runs.json').read_text())
changes={
'paint-spray-gun-bottle':[("(10,18),(6,34),(14,34),(18,18)","(10,18),(6,34),(15,34),(19,18)"),("(26,18),(26,26),(34,26),(34,30)","(26,18),(34,22),(34,30)")],
'pomegranate-crown-inner-stem':[("(29,24)","(28,26)")],
'pomelo-with-single-leaf':[("(36,14),(27,15)","(36,11),(27,11)")],
'standing-cow-profile':[("(8,40),[('L',(8,22)),('A',(16,14),8,8,True)","(4,40),[('L',(4,22)),('A',(12,14),8,8,True)"),("('L',(16,31)),('L',(12,37)),('L',(14,40)),('L',(8,40))","('L',(12,31)),('L',(12,40)),('L',(4,40))"),("        path('tail',(8,22),[('C',(4,32),(6,23),(4,28))]);join('tail','cow')","")],
'scissors-cutting-film':[("        box('film-bottom',30,30,42,42,0);join('blade-down','film-bottom')","        box('film-bottom',30,30,42,42,0);join('blade-down','film-bottom')\n        self.add_line('film-right-rail',(42,18),(42,30));join('film-right-rail','film-top');join('film-right-rail','film-bottom')")],
'strapped-suitcase-above-a-conveyor':[("keyshape=Keyshape.SQUARE","keyshape=Keyshape.VRECT_L"),("box('case',8,14,42,30,3)","box('case',8,12,40,27,3)"),("(18,14),[('L',(18,10)),('A',(22,6),4,4,True),('L',(28,6)),('A',(32,10),4,4,True),('L',(32,14))]","(17,12),[('L',(17,8)),('A',(21,4),4,4,True),('L',(27,4)),('A',(31,8),4,4,True),('L',(31,12))]"),("for x in (18,32):self.add_line(f'strap-{x}',(x,14),(x,30))","for x in (17,31):self.add_line(f'strap-{x}',(x,12),(x,27))"),("(42,34),[('L',(10,34)),('A',(10,42),4,4,False),('L',(42,42))]","(40,36),[('L',(12,36)),('A',(12,44),4,4,False),('L',(40,44))]")],
'square-neck-pinafore-dress':[("(12,4),(20,4)","(10,4),(20,4)"),("(28,4),(36,4)","(28,4),(38,4)")],
 'three-sugar-cubes-above-deep-spoon':[("(6,34),[('A',(28,34),11,4,True),('A',(6,34),11,8,True)]","(6,35),[('A',(28,35),11,4,True),('A',(6,35),11,7,True)]"),("(28,34),(42,34)","(28,35),(42,35)")]
}
replace_body={
 'tapered-bucket-with-a-side-handle':('HRECT_L',"""        path('rim',(4,13),[('A',(34,13),15,5,True),('A',(4,13),15,5,True)],True)
        path('body',(4,13),[('L',(8,35)),('C',(19,40),(9,40),(15,40)),('C',(30,35),(23,40),(29,40)),('L',(32,24)),('L',(34,13))]);join('body','rim')
        circle('pivot',20,29,2)
        path('handle',(22,29),[('L',(40,35)),('A',(44,31),4,4,False),('L',(44,28)),('A',(40,24),4,4,False),('L',(32,24))]);join('handle','pivot');join('handle','body')
"""),
 'tapping-finger-with-contact-arc':('CIRCLE',"""        path('contact-outer',(4,24),[('A',(24,4),20,20,True),('A',(44,24),20,20,True)])
        path('contact-inner',(13,24),[('A',(24,13),11,11,True),('A',(35,24),11,11,True)])
        path('hand',(16,42),[('L',(10,36)),('A',(16,32),5,5,True),('L',(20,36)),('L',(20,28)),('A',(28,28),4,4,True),('L',(28,36)),('L',(32,38)),('L',(32,42))])
"""),
 'tea-leaves-beside-pearl-cluster':('SQUARE',"""        path('leaf-left',(14,18),[('C',(6,6),(6,18),(6,12)),('C',(14,18),(14,7),(15,12))],True)
        path('leaf-right',(14,18),[('C',(32,6),(19,11),(27,13)),('C',(14,18),(30,18),(23,21))],True);join('leaf-left','leaf-right')
        self.add_line('stem',(14,18),(6,22));join('stem','leaf-left');join('stem','leaf-right')
        for x in (12,24,36):circle(f'pearl-{x}',x,36,6)
        join('pearl-12','pearl-24');join('pearl-24','pearl-36')
""")}
for r in rs:
 ident=r['icon_id']
 if ident not in changes and ident not in replace_body:continue
 old=Path(r['run']);new=old.parent/'20260929-batch11-attempt02';new.mkdir(exist_ok=False)
 for f in old.glob('*.metadata.json'):shutil.copy(f,new/f.name)
 shutil.copy(old/'comparison.txt',new/'comparison.txt');f=next(old.glob('*.py'));s=f.read_text()
 for a,b in changes.get(ident,[]):
  assert a in s,(ident,a);s=s.replace(a,b)
 if ident in replace_body:
  key,body=replace_body[ident]
  s=s[:s.index('        path(\'rim\'') if ident=='tapered-bucket-with-a-side-handle' else s.index("        path('contact-left'") if ident=='tapping-finger-with-contact-arc' else s.index("        path('leaf-left'")]+body
  import re
  s=re.sub(r'keyshape=Keyshape.\w+',f'keyshape=Keyshape.{key}',s)
 (new/f.name).write_text(s);r['run']=str(new)
(root/'runs.json').write_text(json.dumps(rs,indent=2))
