from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon,public_row
W=Path(__file__).parent
rows=[]
for i,m in enumerate(json.loads((W/'mapping.json').read_text())):
 r=inspect_icon(create(m['candidate'])); svg=r.pop('_svg',None)
 if svg:(W/(m['candidate']+'.svg')).write_text(svg)
 row={**m,'qa':public_row(r)};rows.append(row)
 (W/'results.json').write_text(json.dumps(rows,indent=2))
 print(i+1,m['original'],r['negative_space'].get('status'),r['status'],r['errors'],flush=True)
