from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[3];sys.path.insert(0,str(root))
from icon_set.scripts.primitive_fix import run_module
from icon_set.scripts.build_gate import gate
batch=Path(__file__).parent;rows=json.loads((batch/'batch.json').read_text())
for i,r in enumerate(rows):
 p=Path(r['result_dir']);g=gate(run_module(p));(p/'automatic-gate.json').write_text(json.dumps(g,indent=2));print(i,r['icon_id'],g['status'],flush=True)
 for e in g['errors']+g['warnings']: print(' ',e,flush=True)
