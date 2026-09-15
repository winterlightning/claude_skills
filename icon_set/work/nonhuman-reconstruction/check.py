import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
from qa_overlays import analyze_distance
W=Path(__file__).parent
items=[i for i in json.loads((W/'audit.json').read_text()) if i['audit_status']=='reconstructed' and (len(sys.argv)==1 or i['icon_id'] in sys.argv[1:])]
for i in items:
 icon=create(i['icon_id']);r=inspect_icon(icon);p=W/(i['icon_id']+'.svg');p.write_text(icon.to_svg());a,*_=analyze_distance(str(p),8)
 print(i['icon_id'],r['status'],'distance',a['lowest_distance'],flush=True)
 print('\n'.join(r['errors']+r['warnings']),flush=True)
 (W/(i['icon_id']+'.check.json')).write_text(json.dumps({k:v for k,v in r.items() if k!='_svg'},indent=2))
