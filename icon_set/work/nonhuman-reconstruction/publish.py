"""Refresh overlays and publish only reviewed canonical reconstructions."""
import json,subprocess,os
from pathlib import Path
W=Path(__file__).parent
A=json.loads((W/'audit.json').read_text())
items=[i for i in A if i['audit_status']=='reconstructed' and Path(i['source_path']).exists()]
svgs=[str(W/(i['icon_id']+'.svg')) for i in items]
with (W/'overlays.log').open('w') as f:
 r=subprocess.run(['python3','qa_overlays.py',*svgs,'--out-dir','icon_set/work/qa_overlays/solo48','--jobs','4','--force'],stdout=f,stderr=subprocess.STDOUT)
 print('Overlay process',r.returncode,flush=True)
args=['python3','icon_set/scripts/build.py','--debug']
for i in items:args+=['--icon',i['source_path']]
with (W/'build.log').open('w') as f:r=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT)
print('Build process',r.returncode,flush=True)
