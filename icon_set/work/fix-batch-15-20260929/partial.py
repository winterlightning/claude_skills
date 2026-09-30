import json
from pathlib import Path
B=Path(__file__).parent
claims=json.loads((B/'claims.json').read_text());rows=[]
for c in claims:
 i=c['item'];key=i['key']
 for p in (Path('icon_set/work/primitive-fix-thuan')/key.replace('/','__')).glob('*/claim.json'):
  d=json.loads(p.read_text())
  if d['work']['claimed_at']!=c['work']['claimed_at']:continue
  refs=list((p.parent/'reference').glob('*.svg'));before=p.parent/'before'/(i['icon_id']+'.svg')
  if not refs or not before.exists():continue
  rows.append({'key':key,'item':i,'reference':str(refs[0]),'result_dir':str(p.parent)})
(B/'staged.json').write_text(json.dumps(rows,indent=2));print(len(rows),'staged')
