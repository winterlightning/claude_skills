from pathlib import Path
import json,hashlib,html
b=Path(__file__).parent;root=Path.cwd();rs=json.loads((b/'batch.json').read_text())
rows=[]
for r in rs:
 p=Path(r['run']);d=json.loads((p/'result.json').read_text());f=json.loads((Path(r['fix'])/'result.json').read_text())
 assert f['outcome']=='done' and f['review_status']=='ready' and f['reported']['worker']=='thuan-mac'
 assert f['author']=='gpt-6' and f['accepted_exception'] and f['build_gate']['status']=='pass'
 svg=p/d['svg'];after=Path(r['fix'])/'after'/d['svg'];assert svg.read_bytes()==after.read_bytes()
 assert hashlib.sha256(svg.read_bytes()).hexdigest()==f['build_gate']['exception']['svg_sha256']
 assert f['uploaded']['has_python'] and f['uploaded']['has_validation']
 rows.append((r,d,f))
assert len(rows)==20
lines=['# Meaning-disapproved icon repairs — 20 completed','',
'Worker: **thuan-mac** · Author: **gpt-6** · Requested: **20, offset 0, meaning**.',
'',
'All 20 were claimed, compared with their original and rejected drawings, revised through primitive-make-ray, inspected at native 48px in light and dark themes, uploaded through primitive_fix.py finish, and returned to **Ready**.',
'',
'**Validation:** all 20 release gates pass via exact-SVG visual exceptions authorized by the user. Their automatic validation is still **invalid / fail**; errors and warnings were retained, not erased. Each exception is bound to the SHA-256 of that drawing. Structural canvas/profile/stroke requirements remain enforced. All modules record `AUTHOR = "gpt-6"`.',
'',
'User authorization: “If you think an icon needs to be exceptional, make it an exception, but make sure the icon quality is still good for UI/UX.”',
'',
'No registered icon module, published output, library metadata, build, publish, commit or push was changed by this repair batch. Earlier attempts remain in their standalone work folders.',
'',
'## Visual comparisons','']
for i in range(1,5):lines.append(f'- [Reference / rejected / revision / both themes, page {i}]({(root/b/f"final-review-{i}.png").as_posix()})')
for r,d,f in rows:
 p=root/r['run'];fix=root/r['fix'];g=f['build_gate']
 lines += ['',f'## {r["key"]}','',f'**What was wrong:** {d["comparison"]}', '',f'**Reviewer feedback:** {r["feedback"]}', '',f'**Revision:** {d["plan"]}', '',f'**Construction:** {d["construction_references"]}', '',f'**Keyshape:** {d["keyshape"]} — {d["keyshape_rationale"]}', '',f'**Omissions:** {d["omissions"] or "No defining features omitted."}', '',f'**Exception:** {g["exception"]["reason"]}', '',f'**Validation:** automatic `{f["validation_status"]}` / `{g["automatic_status"]}`; release gate **pass · exception**. Findings preserved: {len(f["validation_errors"])} model errors, {len(f["validation_warnings"])} model warnings. **AUTHOR:** `gpt-6`. **Production:** `done`, review `ready`.', '',f'**RESULT_DIR:** [Open run]({p.as_posix()}) · [SVG]({(p/d["svg"]).as_posix()}) · [Python]({(root/r["module"]).as_posix()}) · [Validation]({(p/"validation.txt").as_posix()}) · [Production receipt]({(fix/"result.json").as_posix()})']
(b/'REPORT.md').write_text('\n'.join(lines)+'\n')
summary={'requested':20,'claimed':20,'done':20,'ready':20,'worker':'thuan-mac','author':'gpt-6','pass_with_exception':20,'strict_automatic_pass':0,'verified_svg_hashes':20,'report':'REPORT.md'}
(b/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
