from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon,public_row
W=Path(__file__).parent;rows=[]
for m in json.loads((W/'revision-2-mapping.json').read_text()):
 r=inspect_icon(create(m['candidate']));svg=r.pop('_svg',None)
 if svg:(W/(m['candidate']+'.svg')).write_text(svg)
 rows.append({**m,'qa':public_row(r)})
 print(m['original'],r['status'],r['errors'],r['warnings'],flush=True)
(W/'revision-2-results.json').write_text(json.dumps(rows,indent=2))
