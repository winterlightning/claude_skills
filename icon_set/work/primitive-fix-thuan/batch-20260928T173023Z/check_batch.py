from pathlib import Path
import json,sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.build_gate import gate
B=Path(__file__).parent
rows=json.loads((B/'authored.json').read_text())
for r in rows:
 g=gate(Path(r['module']));(Path(r['run'])/'automatic-gate.json').write_text(json.dumps(g,indent=2))
 print(r['index'],r['icon_id'],g['status'],len(g['errors']),len(g['warnings']),flush=True)
 print('\n'.join((g['errors']+g['warnings'])[:2]),flush=True)
