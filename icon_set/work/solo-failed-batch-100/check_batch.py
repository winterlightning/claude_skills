from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-failed-batch-100/before.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'before.json').read_text());repairs=json.loads((W/'repairs.json').read_text());results=[]
for a in repairs:
 row=inspect_icon(create(a['icon_id']));row.pop('_svg',None);results.append(row);print(a['number'],a['icon_id'],row['status'],row['errors'],flush=True)
(W/'checks.json').write_text(json.dumps(results,indent=2))
