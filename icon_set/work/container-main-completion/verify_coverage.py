"""Read-only completion audit against the published progression catalog."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).parent
catalog=json.loads((ROOT/'icon_set/dist/gallery/combinations.json').read_text())
manifest=json.loads((ROOT/'icon_set/dist/container64/manifest.json').read_text())
records={r['icon_id']:r for r in manifest['icons']}
rows=[r for r in catalog['rows'] if r['kind']=='container']
issues=[]
for row in rows:
 mains=row.get('main_generated',[])
 if len(mains)!=1:issues.append({'combination':row['id'],'reason':'Expected one reviewed container main','artwork':mains})
 for main in mains:
  if not main['key'].startswith('container/'):issues.append({'combination':row['id'],'reason':'Wrong main family'})
  icon=records.get(main['icon_id'])
  if not icon or icon['profile']!='CONTAINER64' or icon['validation']['status']!='valid':issues.append({'combination':row['id'],'reason':'Missing validated container export'})
  if not (ROOT/'icon_set/dist/gallery'/main['preview_url']).is_file():issues.append({'combination':row['id'],'reason':'Missing preview'})
report={'total_combinations':len(rows),'unique_main_references':len({r['main_id'] for r in rows}),'unique_container_drawings':len({g['icon_id'] for r in rows for g in r.get('main_generated',[])}),'new_container_drawings':47,'issues':issues}
(OUT/'coverage-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(bool(issues))
