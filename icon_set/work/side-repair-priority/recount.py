import sys,json,hashlib
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
W=Path(__file__).parent
load=lambda name:json.loads((ROOT/name).read_text())
roles=load('icon_set/model/catalog/sub-usage-categories.json');canon=load('icon_set/data/canonical-sub32.json');aliases=load('icon_set/data/sub-profile-aliases.json');pairs=load('icon_set/data/combination-pairs.json')['rows'];rows=[]
for e in roles['icons']:
 if 'side' not in e['versions']:continue
 v=e['versions']['side'];original=v['icon_id'];uid=aliases.get(original,original);rec=canon.get(uid,v);m=create(uid);sha=hashlib.sha256(m.to_svg().encode()).hexdigest()
 rows.append(dict(icon=uid,previous_icon=original,status=rec['model_validation'],hash_current=rec['sha256']==sha,python_source=rec['python_source'],pair_ids=e.get('pair_ids',{}).get('side',[]),source_uuid=e['source_icon_id']))
print('Side models',len(rows),'counts',dict(Counter(x['status'] for x in rows)),'stale',[(x['icon'],x['status']) for x in rows if not x['hash_current']],flush=True)
(W/'inventory.json').write_text(json.dumps(rows,indent=2))
from icon_set.validation.library_qa import inspect_icon
for r in rows:
 if r['status'] not in ('pass','fail','review') or not r['hash_current']:
  q=inspect_icon(create(r['icon']));r['status']=q['status'];r['findings']=q['errors']+q['warnings'];r['freshly_validated']=True
  print(r['icon'],r['status'],flush=True)
(W/'inventory.json').write_text(json.dumps(rows,indent=2))
print('Resolved counts',dict(Counter(x['status'] for x in rows)),flush=True)
