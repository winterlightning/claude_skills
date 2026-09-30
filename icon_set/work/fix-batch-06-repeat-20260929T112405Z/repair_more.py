from author import author,ROOT
import ast,json
src=(ROOT/'more.py').read_text();s=json.loads((ROOT/'specs.json').read_text())
for n in ast.parse(src).body:
 if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call):s[str(ast.literal_eval(n.value.args[0]))]=ast.get_source_segment(src,n)
H='Human full_body_ref.png: circular heads and exact 4-unit detached head gap'
edits={
5:[("(18,28)","(19,28)"),("(30,28)","(29,28)"),("6,6,True)],True)","5,6,True)],True)")],
7:[("(29,26)","(29,24)"),("(19,26)","(19,24)")],
8:[("('C',(36,25),(44,24),(40,25)),('L',(36,32)),('L',(40,32))","('C',(34,24),(44,24),(39,24)),('L',(34,32)),('L',(40,32))")],
11:[("('L',(30,20)),('L',(28,11))","('L',(31,20)),('L',(29,11))"),("('A',(38,11),5,5,True)","('A',(39,11),5,5,True)")],
12:[("('C',(38,36),(42,30),(40,34))","('C',(38,40),(42,32),(40,36))"),("('C',(16,40),(6,34),(10,40))","('C',(14,40),(6,34),(10,40))")],
13:[("(20,23)","(20,20)"),("(28,23)","(28,20)")],
14:[("path('left-body',(4,40),[('L',(4,38)),('A',(14,28),10,10,True)])","path('left-body',(4,40),[('L',(4,38)),('C',(14,28),(4,32),(8,28))])"),("path('embrace',(14,28),[('L',(31,37)),('A',(35,35),3,3,False)])","path('embrace',(14,28),[('C',(32,40),(20,30),(26,39))])")],
15:[("(8,31)","(8,34)"),("(4,31)","(4,34)"),("(44,31)","(44,34)"),("(40,31)","(40,34)"),("circle('wheel-left',12,34,4);circle('wheel-right',36,34,4)","circle('wheel-left',12,34,4);circle('wheel-right',36,34,4);join('body','wheel-left');join('body','wheel-right')")],
17:[("(38,12),(30,14)","(38,10),(30,12)")],
18:[("(24,28),(24,44)","(24,28),(24,42),(24,44)"),("path('snake',(40,12)","path('snake',(34,12)"),("path('head',(32,12),[('A',(40,12),4,4,True)]);join('head','snake')","circle('head',37,12,3);join('head','snake')")],
19:[("('C',(24,34),(42,33),(31,34)),('C',(10,23),(15,34),(10,30))","('C',(32,34),(42,32),(36,34)),('C',(18,34),(28,36),(22,36)),('C',(10,23),(12,33),(10,29))"),("(18,33)","(18,34)"),("(32,33)","(32,34)")]
}
for i,pairs in edits.items():
 code=s[str(i)]
 for old,new in pairs:
  assert old in code,(i,old);code=code.replace(old,new)
 s[str(i)]=code;exec(code)
author(16,'''
circle('left-head',9,15,3)
line('left-torso',(9,26),(9,32));poly('left-arms',(4,29),(9,26),(14,29));join('left-arms','left-torso')
poly('left-legs',(5,40),(9,32),(13,40));join('left-legs','left-torso')
self.mark_human_figure('left',head='left-head',torso='left-torso',torso_junction='start')
circle('right-head',36,11,3)
poly('dress',(36,22),(44,36),(40,36),(32,36),(28,36),(36,22))
line('right-leg-left',(32,36),(32,40));line('right-leg-right',(40,36),(40,40));join('right-leg-left','dress');join('right-leg-right','dress')
circle('note',23,18,2);poly('stem',(25,18),(25,8),(29,8));join('stem','note')
''','The rejected duet used two identical stick figures. Restored the right singer in a dress and the left singer in trousers with a central musical note. Both heads have an exact four-unit ink gap to their bodies; reduced two notes to one.','HRECT_L',H+'; Lucide music-2: note head, stem and flag')
(ROOT/'specs2.json').write_text(json.dumps(s,indent=2))
