from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
a.BODIES[8]=a.BODIES[8].replace("14,14,27,28,3,{2:[(27,18),(27,24)]}","14,14,25,28,3,{2:[(25,18),(25,24)]}").replace('(27,18),(34,14),(34,28),(27,24)','(25,18),(32,16),(32,26),(25,24)')
a.BODIES[10]=a.BODIES[10].replace("(17,23),[('A',(31,23),7,7,True),('C',(28,31),(31,27),(28,28)),('L',(20,31)),('C',(17,23),(20,28),(17,27))]","(18,25),[('A',(30,25),6,6,True),('C',(28,32),(30,28),(28,29)),('L',(20,32)),('C',(18,25),(20,29),(18,28))]")
a.BODIES[11]=a.BODIES[11].replace("('C',(29,24),(28,20),(32,21))","('C',(31,25),(28,20),(35,22))")
a.BODIES[12]=a.BODIES[12].replace("self.node('upper-bowl',16,14,10,[(-6,8)])","self.circle('upper-bowl',16,13,9)")
a.BODIES[12]=a.BODIES[12].replace("(5,36),[('A',(16,28),11,8,True),('A',(27,36),11,8,True),('A',(16,44),11,8,True),('A',(5,36),11,8,True)]","(5,37),[('A',(16,30),11,7,True),('A',(27,37),11,7,True),('A',(16,44),11,7,True),('A',(5,37),11,7,True)]")
a.BODIES[12]=a.BODIES[12].replace("(10,22),[('C',(16,28),(7,27),(10,28))]","(16,22),[('C',(16,30),(9,23),(9,29))]")
a.author([8,10,11,12],rev=2);a.sheets()
