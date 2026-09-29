from pathlib import Path
import sys,json,textwrap
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
for r in a.claims:a.BODIES[r['index']]=textwrap.dedent(Path(r['module']).read_text().split('    def build(self):\n',1)[1])
for i in [2,3]:
 s=a.BODIES[i]
 # Translate housing one unit left; extend tape two units to obtain 2px tick gaps.
 for old,new in [('(12,','(11,'),('(20,','(19,'),('(28,','(27,'),('(8,','(7,'),('(4,','(3,')]:s=s.replace(old,new)
 s=s.replace("'hub',16,","'hub',15,")
 s=s.replace('(44,','(45,').replace('(40,40)','(39,40)').replace('(34,40)','(33,40)').replace('(40,38)','(39,38)').replace('(34,38)','(33,38)').replace('for x in (34,40)','for x in (33,39)')
 a.BODIES[i]=s
s=a.BODIES[8]
s=s.replace("('L',(33,26)),('A',(36,29)","('L',(31,26)),('A',(34,29)").replace("('L',(36,41)),('A',(33,44)","('L',(34,41)),('A',(31,44)")
s=s.replace('(24,8),(40,24)','(23,9),(39,25)').replace('(30,2),(24,8),(30,14)','(29,3),(23,9),(29,15)').replace('(34,18),(40,24),(46,18)','(33,19),(39,25),(45,19)')
a.BODIES[8]=s
a.author([2,3],rev=2);a.author([8],rev=3);a.sheets()
