from pathlib import Path
import sys,json,textwrap
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
for r in a.claims:a.BODIES[r['index']]=textwrap.dedent(Path(r['module']).read_text().split('    def build(self):\n',1)[1])
a.BODIES[2]=a.BODIES[2].replace('(34,31)','(34,32)').replace('(33,24)','(32,24)')
a.SHAPES[2]='SQUARE'
a.BODIES[4]=a.BODIES[4].replace('(31,11)','(30,12)').replace('(37,17)','(36,18)').replace('(38,22)','(37,22)')
a.author([2,4],rev=3);a.sheets()
from icon_set.scripts.build_gate import gate
for r in a.claims:
 if r['index'] in [2,4]:
  g=gate(Path(r['module']));(Path(r['run'])/'automatic-gate.json').write_text(json.dumps(g,indent=2));print(r['index'],g['status'],g['errors'],g['warnings'],flush=True)
