import json
from pathlib import Path
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
w=Path('icon_set/work/parallel-spacing-repair'); notes=json.loads((w/'notes.json').read_text()); results={}
for name in notes:
 icon=create(name); report=icon.validate_icon(); q=inspect_icon(icon)
 results[name]={'validation':report.describe(),'qa':q.get('status'),'errors':q.get('errors'),'warnings':q.get('warnings'),'internal':q.get('internal_spacing',{}).get('status')}
 if q.get('status')!='pass':print(name, report.describe(),q.get('errors'),q.get('warnings'))
(w/'results.json').write_text(json.dumps(results,indent=2))
print('PASS',sum(r['qa']=='pass' for r in results.values()),'OF',len(results))
