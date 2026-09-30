from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
claims=json.loads((ROOT/'claims.json').read_text());runs=json.loads((ROOT/'runs.json').read_text());completed=json.loads((ROOT/'completion.json').read_text())
assert len(claims)==len(runs)==len(completed)==20
counts={e['key']:e['count'] for e in json.loads((ROOT/'eligibility.json').read_text())}
lines=['# Once-disapproved solo fix batch 11 of 34','', '20 requested, 20 claimed, 20 fixed and uploaded through primitive_fix.finish, 20 returned Ready. Offset 0; maximum disapprovals 1.','', 'Every claimed key had one effective disapproval after fresh history checks. Fixed-then-disapproved icons were counted as repeat disapprovals and excluded. All modules use AUTHOR = "gpt-6". Model validation: valid. Full build gate: pass. Zero errors, zero warnings; no validation exceptions.','', 'No written feedback or disapproval reason was recorded for these 20 icons. Each repair followed a comparison of the original reference with the rejected drawing and was reviewed at native 48 px and enlarged 384 px in light and dark themes.','', 'Comparison sheets: [1](final-review-1.png), [2](final-review-2.png), [3](final-review-3.png), [4](final-review-4.png).','']
summary=[]
for i,e in enumerate(claims,1):
 r=runs[str(i)];c=completed[e['key']];run=Path(r['run']).resolve();d=json.loads((run/'result.json').read_text())
 assert counts[e['key']]==1 and c['outcome']=='done' and c['review_status']=='ready' and c['author']=='gpt-6'
 assert c['validation_status']=='valid' and not c['validation_errors'] and not c['validation_warnings']
 assert c['build_gate']['status']=='pass' and not c['build_gate']['errors'] and not c['build_gate']['warnings']
 assert c.get('uploaded') and c.get('reported')
 lines += [f"## {i}. {e['key']}", '',d['review'], '', 'Feedback: none recorded. '+d['change'], '',f"Keyshape: {d['keyshape']} — {d['keyshape_reason']} Centerline envelope: {d['centerline_envelope']}.", '', 'Construction references: '+d['construction'], '', 'Reduction: '+d['omissions'], '', 'Visual review: '+d['visual_review']['findings'], '',f"AUTHOR: `{d['author']}`. Validation: **valid; full gate pass; zero warnings**. Production: **done / Ready**.", '',f"Artifacts: [RESULT_DIR]({run}) · [SVG]({run/d['svg']}) · [Python]({run/d['module']}) · [validation]({run/'validation.txt'}) · [production result]({Path(e['result_dir'])/'result.json'}).",'']
 summary.append({'key':e['key'],'disapprovals':counts[e['key']],'author':c['author'],'outcome':c['outcome'],'review_status':c['review_status'],'run':r['run'],'svg':str(run/d['svg']),'validation':'valid','build_gate':'pass','warnings':0})
(ROOT/'REPORT.md').write_text('\n'.join(lines))
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print('Verified and reported 20/20 done / Ready; zero warnings.')
