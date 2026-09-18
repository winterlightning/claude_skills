from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
OUT=Path(__file__).resolve().parent
records=json.loads((OUT/'complete-models.json').read_text());results=[]
for r in records:
 o=create(r['icon_id']);v=o.validate_icon();item={**r,'status':v.status,'details':v.describe()};results.append(item);print(r['number'],r['icon_id'],v.describe(),flush=True)
(OUT/'model-validation.json').write_text(json.dumps(results,indent=2)+'\n')
