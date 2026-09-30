from pathlib import Path
import json,re
OUT=Path(__file__).parent;ROOT=OUT.resolve().parents[2]
rows=json.loads((OUT/'claims.json').read_text())
lines=['# Once-disapproved solo fix batch 07','', '20 claimed at offset 0 using `--max-disapprovals 1`. Worker: `thuan-mac`. All 20 finished through `primitive_fix.py finish`, uploaded, and returned to **Ready**. Icons fixed and then disapproved again were excluded by the claim filter.','', 'Every module has `AUTHOR = "gpt-6"`. Every final geometry report is **valid**, and every full build gate is **pass**, with **zero errors and zero warnings**. No written reviewer feedback was present for these claims; revisions follow visual comparison with each original.','', 'Original, rejected and final drawings were inspected, including native 48px light/dark previews. Fresh attempts and failed validation evidence remain in separate run directories.','', '## Comparison sheets','']
for j in range(4):lines.append(f'- [Original / rejected / final, icons {j*5+1}–{j*5+5}]({(OUT/f"after-{j}.png").resolve()})')
audit=[]
for i,r in enumerate(rows):
 fix=ROOT/r['fix'];res=json.loads((fix/'result.json').read_text());run=Path(res['make_ray_run']);meta=json.loads((run/'result.json').read_text())
 assert res['outcome']=='done' and res['review_status']=='ready' and res['author']=='gpt-6'
 assert res['validation_status']=='valid' and not res['validation_errors'] and not res['validation_warnings']
 assert res['build_gate']['status']=='pass' and not res['build_gate']['errors'] and not res['build_gate']['warnings']
 assert meta['gate']['status']=='pass' and not meta['gate']['warnings'] and not meta['gate']['errors']
 module=run/meta['module'];svg=run/meta['svg']
 assert re.search(r'AUTHOR\s*=\s*["\']gpt-6["\']',module.read_text())
 keyshape=re.search(r'keyshape = Keyshape\.(\w+)',module.read_text()).group(1)
 lines+=['',f'## {i+1}. `{r["key"]}`','',meta['review'],'',f'Author: `gpt-6`. Keyshape: `{keyshape}`. Validation: **valid / build pass / zero warnings**. Production: **Ready**.','',f'[RESULT_DIR]({run.resolve()}) · [SVG]({svg.resolve()}) · [Module]({module.resolve()}) · [Finish receipt]({(fix/"result.json").resolve()})','',f'Construction reference: {meta["references"]}']
 audit.append(dict(key=r['key'],run=str(run),svg=str(svg),author=res['author'],validation_status=res['validation_status'],build_gate=res['build_gate']['status'],review_status=res['review_status'],finished_at=res['finished_at']))
assert len(audit)==20
(OUT/'REPORT.md').write_text('\n'.join(lines)+'\n');(OUT/'audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print('Verified 20 done / ready / valid / pass; zero errors and warnings.')
print((OUT/'REPORT.md').resolve())
