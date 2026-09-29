from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
a.BODIES[6]=a.BODIES[6].replace("(36,13),(36,19)","(36,13),(36,18)").replace("self.add_line('wrist',(36,19),(36,18));self.relate('connect','forearm','wrist');self.relate('connect','wrist','gripper')","self.relate('connect','forearm','gripper')")
a.BODIES[7]=a.BODIES[7].replace("('L',(17,21)),('C',(31,21),(21,23),(27,23))","('L',(17,18)),('L',(17,20)),('C',(31,20),(21,21),(27,21)),('L',(31,18))")
a.BODIES[7]=a.BODIES[7].replace("[('L',(9,16)),('A',(6,23),4,4,False),('L',(11,25)),('L',(14,17))]","[('L',(14,17)),('L',(8,15)),('C',(5,20),(3,13),(3,19)),('L',(11,21)),('L',(14,17))]")
a.BODIES[7]=a.BODIES[7].replace('(44,23)','(44,21)').replace('cx,29,3','cx,30,3').replace('(cx-5,44)','(cx-5,45)').replace('(cx,40)','(cx,41)').replace('(cx+5,44)','(cx+5,45)')
a.BODIES[8]=a.BODIES[8].replace("4,14,24,34,3,{2:[(24,26)],4:[(14,34)]}","4,16,24,36,3,{2:[(24,26)],4:[(14,36)]}").replace("('L',(14,34))","('L',(14,36))")
a.BODIES[8]=a.BODIES[8].replace("(28,8),(40,20),radius_x=12","(24,8),(40,24),radius_x=16").replace("(32,4),(28,8),(32,12)","(30,2),(24,8),(30,14)").replace("(36,16),(40,20),(44,16)","(34,18),(40,24),(46,18)")
a.author([6,7,8],rev=2);a.sheets()
