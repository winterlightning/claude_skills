"""Second visual pass; updates only fresh modules listed in this batch."""
from pathlib import Path
import json
HERE=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=str(HERE/'batch.json')
rows=json.loads((HERE/'batch.json').read_text())
def replace(i, old, new):
    p=Path(rows[i]['module']);s=p.read_text();assert old in s,(i,old);p.write_text(s.replace(old,new))
def body(i, text):
    p=Path(rows[i]['module']);s=p.read_text();p.write_text(s[:s.index("        def join(a,b):")]+"        def join(a,b): self.relate('connect',a,b)\n"+text)

body(1,'''        # Shared tower widths leave a wider nave for the door and window.
        poly('outline',(6,42),(6,18),(10,13),(14,18),(14,24),(24,14),(34,24),(34,18),(38,13),(42,18),(42,42),(28,42),(20,42),(6,42))
        for x in (14,34):
            line(f'wall-{x}',(x,24),(x,42));join('outline',f'wall-{x}')
        for l,r in ((6,14),(34,42)):
            line(f'roof-{l}',(l,22),(r,22));join('outline',f'roof-{l}')
        circle('window',24,25,3)
        path('entry',(20,42),[('L',(20,37)),('A',(28,37),4,4,True),('L',(28,42))]);join('entry','outline')
        poly('cross-stem',(10,6),(10,9),(10,13));line('cross-bar',(7,9),(13,9));join('cross-stem','cross-bar');join('cross-stem','outline')
''')
for i in (3,4):
    replace(i,"tr((26,31))","tr((25,32))")
    replace(i,"(6,16),(10,16)","(6,17),(9,17)")
    replace(i,"(16,6),(16,10)","(17,6),(17,9)")
    replace(i,"(7,7),(10,10)","(6,6),(9,9)")
replace(6,"circle('bubble',13,8,3)","circle('bubble',13,9,3)")
replace(6,"(34,5),(34,8),(34,11)","(34,6),(34,9),(34,12)")
replace(6,"(31,8),(34,8),(37,8)","(31,9),(34,9),(37,9)")
# Lift flame, keep a visible gap over the candle.
replace(8,"('A',(20,10),4,4,True)","('A',(20,10),4,2,True)")
body(9,'''        # End the barrel exactly on the wheel, exposing its front rim.
        path('barrel',(12,30),[('C',(10,21),(8,29),(8,24)),('C',(16,16),(11,18),(13,17)),('L',(44,8)),('L',(44,18)),('L',(30,24))])
        path('wheel',(12,30),[('A',(22,20),10,10,True),('A',(30,24),10,10,True),('A',(32,30),10,10,True),('A',(22,40),10,10,True),('A',(12,30),10,10,True)],True);join('wheel','barrel')
        circle('axle',22,30,2)
        poly('carriage',(12,30),(4,35),(4,40),(22,40));join('wheel','carriage');join('barrel','carriage')
''')
replace(10,"poly('stem',(24,34),(22,44),(26,44),(24,34))","line('stem',(24,34),(24,44))")
replace(11,"path('handle',(6,9),[('A',(12,6),4,4,True)","path('handle',(6,10),[('C',(12,6),(6,6),(9,4))")
replace(11,"(18,40),(18,44),(30,44),(30,40)","(18,40),(18,42),(30,42),(30,40)")
replace(11,"('C',(36,20),(32,20),(35,21))])","('C',(36,20),(32,20),(35,21))]);join('shaving','bowl')")
replace(13,"7,7,not swap","7,7,False")
replace(13,"tr((14,23))","tr((13,23))")
replace(13,"tr((9,28))","tr((8,28))")
replace(13,"tr((25,34))","tr((25,35))")
for i in (16,17):
    # The crown and cuff need breathing room more than they need tiny pleats.
    replace(i,"('L',(38,27)),('L',(10,27))","('L',(38,25)),('L',(10,25))")
    replace(i,"line('cuff',(10,21),(38,21))","line('cuff',(10,19),(38,19))")
    replace(i,"        for x in (18,30):line(f'pleat-{x}',(x,16),(x,21));join(f'pleat-{x}','cuff')\n","")
    replace(i,"Restore cuff and pleat detail","Restore cuff detail") if i==16 else replace(i,"Restore the outlined moustache lobes and pleats","Restore the outlined moustache lobes")
    replace(i,"p(3,31),p(7,32)","p(3,33),p(7,33)")
body(18,'''        # Head's cardinal apex is exactly y=4. Shared neck and base nodes.
        path('pawn',(18,20),[('C',(15,13),(16,18),(15,16)),('A',(24,4),9,9,True),('A',(33,13),9,9,True),('C',(30,20),(33,16),(32,18)),('L',(29,23)),('C',(34,36),(28,28),(30,32)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True),('L',(14,36)),('C',(19,23),(18,32),(20,28)),('L',(18,20))],True)
        line('collar',(19,23),(29,23));join('collar','pawn')
        line('base-seam',(14,36),(34,36));join('base-seam','pawn')
''')
