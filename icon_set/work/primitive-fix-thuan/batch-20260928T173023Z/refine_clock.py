from pathlib import Path
import sys,json,textwrap
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
for r in a.claims:a.BODIES[r['index']]=textwrap.dedent(Path(r['module']).read_text().split('    def build(self):\n',1)[1])
a.BODIES[2]=a.BODIES[2].replace('(24,14)','(24,15)')
a.SHAPES[2]='SQUARE'
a.author([2],rev=4);a.sheets()
from icon_set.scripts.build_gate import gate
for r in a.claims:
 if r['index']==2:
  g=gate(Path(r['module']));(Path(r['run'])/'automatic-gate.json').write_text(json.dumps(g,indent=2));print(g['status'],g['errors'],g['warnings'])
