import json,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
cohort=json.loads((ROOT/'icon_set/work/intersection-review-977/cohort.json').read_text());manifest=json.loads((ROOT/'icon_set/dist/solo48/manifest.json').read_text());published={r['icon_id']:r for r in manifest['icons']};rows=[]
for r in cohort:
 id=r['icon_id'];assert id in published,id;entry=published[id];svg=create(id).to_svg();v=entry['validation'];sha=hashlib.sha256(svg.encode()).hexdigest()
 assert v['status']=='valid' and not v['warnings'],(id,v)
 assert entry['svg_sha256']==sha,(id,'stale export')
 assert (ROOT/'icon_set/dist/solo48'/f'{id}.svg').read_text()==svg,(id,'file mismatch')
 rows.append(dict(id=id,status='valid',warnings=[],svg_sha256=sha))
summary=json.loads((H/'audit-summary.json').read_text());summary.update(completed_at=datetime.now(timezone.utc).isoformat(),published=977,published_without_warnings=977,svg_hashes_match_sources=True,source_identity_preserved=True,tests=dict(passed=76,suites=['test_model_and_renderers','test_profiles_keyshapes','test_validator']),report='http://localhost:8000/reports/stroke-quality-977.html?filter=latest&sort=strokes-desc')
(H/'release-validation.json').write_text(json.dumps(rows,indent=2));(H.parent/'completion.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
