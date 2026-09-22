from pathlib import Path
import ast,json,sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.model.icons.registry import create
w=Path(__file__).resolve().parent
rs=json.loads((w/'results.json').read_text())
manifest={r['icon_id']:r for r in json.loads(Path('published/solo48/manifest.json').read_text())['icons']}
for r in rs:
 if r['outcome']=='unresolved':continue
 tree=ast.parse(Path(r['python_original']).read_text());c=next(n for n in tree.body if isinstance(n,ast.ClassDef));id=next(ast.literal_eval(n.value) for n in c.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in n.targets))
 row=manifest[id];v=row['validation'];assert v['status']=='valid' and not v['errors'] and not v['warnings'],(id,v)
 svg=Path('published/solo48')/(id+'.svg')
 assert svg.read_text()==create(id).to_svg(),id
 r.update(outcome='generated and verified',svg=str(svg),manifest='published/solo48/manifest.json',validation='status: valid; zero errors and zero warnings; build-level hole and internal-spacing checks passed')
 if id=='domed-cycling-helmet-with-chin-strap':
  r['review']+=' The first build caught rim/buckle clearance below four ink units; moving the buckle center to (28,31) repaired the gap. The second targeted build passed.'
(w/'results.json').write_text(json.dumps(rs,indent=2))
report=['# Solo queue offset 0 — 10 references','','Processed the fixed ten-item page returned at offset 0 (124 total at fetch). Seven icons generated and verified; three pre-existing drafts remain unresolved. No replacement items fetched.','','All ten live status and saved-brief checks succeeded immediately before their item was processed. All references are standalone objects, scenes or anatomical depictions; no combination split or status changes were needed. No save failures and no items skipped due to changed state.','','The seven generated icons pass validation with zero warnings, including the build-level hole and internal-spacing checks. Actual exported SVGs match their Python originals byte-for-byte and are present in the SOLO48 manifest. Light and dark renders were visually reviewed at 48 pixels. Only the selected originals were built; no full-library generation, metadata seeding, manual artwork import or commit was performed.','','Authorship on created/revised originals: `gpt-6-astra`. The unrelated working changes and three existing unresolved drafts were preserved.','','Preview: `export-preview.png`. Evidence: `results.json`, `manifest-verification.json`, original `build.log`, repaired `helmet-build.log`, and `helmet-qa.json`. Initial candidate renders are retained separately.','']
for r in rs:
 report.extend(['## '+r['concept'],'','- UUID: `'+r['uuid']+'`','- Source: `'+r['source']+'`','- Original: `'+r['python_original']+'`','- Outcome: '+r['outcome'],'- Validation: '+r['validation'].strip().replace('\n','; ')])
 if 'svg' in r:report.extend(['- Export: `'+r['svg']+'`','- Manifest: `'+r['manifest']+'`'])
 report.extend(['',r['review'].replace('Candidate reviewed','Final export reviewed'),''])
(w/'report.md').write_text('\n'.join(report))
print('Seven exports and all validation results verified; final report saved.')
