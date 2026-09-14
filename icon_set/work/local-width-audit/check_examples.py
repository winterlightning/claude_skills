from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from detector import analyze
from icon_set.model.icons.registry import create
W=Path(__file__).parent
for name in ['anteater-v5','winged-totem-pole','hooded-cobra-v2','hatching-dinosaur-egg-v2']:
 r=analyze(create(name));(W/(name+'.json')).write_text(json.dumps(r,indent=2));print(name,r['status'],[(f['elements'],f['ink_gap'],f['sustained_length']) for f in r['findings']])
