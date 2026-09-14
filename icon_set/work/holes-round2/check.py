from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon,public_row
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-round2/mapping.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;rows=[]
for m in json.loads((w/'mapping.json').read_text()):
 try:
  q=inspect_icon(create(m['candidate']));(w/(m['candidate']+'.svg')).write_text(q.pop('_svg'));q=public_row(q);rows.append({**m,'qa':q});print(m['original'],q['negative_space']['status'],q['errors'],q['warnings'],flush=True)
 except Exception as e:print(m['original'],'EXCEPTION',repr(e),flush=True)
(w/'results.json').write_text(json.dumps(rows,indent=2))
