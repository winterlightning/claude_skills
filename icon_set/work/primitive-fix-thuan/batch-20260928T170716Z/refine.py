from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
# Recover the actual latest body from its standalone Python source.
for r in a.claims:
 a.BODIES[r['index']]=__import__('textwrap').dedent(Path(r['module']).read_text().split('    def build(self):\n',1)[1])
a.BODIES[0]=a.BODIES[0].replace("('L',(29,22))","('L',(29,19)),('L',(29,22))").replace("('L',(19,16))","('L',(19,19)),('L',(19,16))")
a.BODIES[6]=a.BODIES[6].replace('(22,12),(26,12)','(22,13),(26,13)')
for i in [7,9]:a.BODIES[i]=a.BODIES[i].replace('(24,28)','(24,27)')
a.BODIES[14]=a.BODIES[14].replace("('L',(18,27))","('L',(18,28)),('L',(18,27))")
a.BODIES[15]=a.BODIES[15].replace("(10,27),(16,11),(22,27)","(10,28),(12,22),(16,10),(20,22),(22,28)")
a.author([0,6,7,9,14,15],rev=3);a.sheets()
