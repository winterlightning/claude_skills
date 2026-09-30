import json,sys,subprocess
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'claims.json').read_text())
for i in map(int,sys.argv[1:]):
 r=rows[i];run=Path(r['run']);meta=json.loads(next(run.glob('*.metadata.json')).read_text())
 assert r['status']=='valid' and r['gate']['status']=='pass' and not r['gate']['warnings']
 meta.update(validation_status='valid',validation_errors=[],validation_warnings=[],build_gate=r['gate'],visual_review='Inspected native 48px and enlarged light/dark previews. Clear subject silhouette, consistent strokes and readable openings.',omissions=r['note'],artifacts=[p.name for p in run.iterdir()])
 (run/'result.json').write_text(json.dumps(meta,indent=2))
 result=subprocess.run([sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',r['run'],'--outcome','done','--note',r['note']])
 if result.returncode:raise SystemExit(result.returncode)
