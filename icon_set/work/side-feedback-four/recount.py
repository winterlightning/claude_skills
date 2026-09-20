"""Refresh the side-only inventory from verified repairs and unchanged geometry."""
import json,hashlib,sys
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
p=W.parent/'side-repair-priority';rows=json.loads((W/'inventory-before.json').read_text())
a={r['icon']:r for r in json.loads((W/'accepted.json').read_text())};canon=json.loads((ROOT/'icon_set/data/canonical-sub32.json').read_text())
for r in rows:
 if r['icon'] in a:
  v=a[r['icon']];r.update(previous_icon=r['icon'],icon=v['candidate'],python_source=v['candidate_python'],status='pass',freshly_validated=True)
 sha=hashlib.sha256(create(r['icon']).to_svg().encode()).hexdigest()
 expected=canon.get(r['icon'],{}).get('sha256',r.get('verified_svg_sha256'))
 assert sha==expected,(r['icon'],sha,expected)
 r.update(verified_svg_sha256=sha,hash_current=True)
(p/'inventory.json').write_text(json.dumps(rows,indent=2))
print('All',len(rows),'selected side drawings match recorded geometry.')
