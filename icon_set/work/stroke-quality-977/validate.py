import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
H=Path(__file__).parent
results=[]
for row in json.loads((H/'changes.json').read_text()):
 try:
  r=create(row['id']).validate_icon();out=dict(id=row['id'],status=r.status,errors=r.errors,warnings=r.warnings)
 except Exception as e:out=dict(id=row['id'],status='exception',errors=[str(e)],warnings=[])
 results.append(out)
 if out['status']!='valid' or out['warnings']:print(out,flush=True)
(H/'validation.json').write_text(json.dumps(results,indent=2))
print('Validated',len(results),'Valid:',sum(r['status']=='valid' and not r['warnings'] for r in results),flush=True)
