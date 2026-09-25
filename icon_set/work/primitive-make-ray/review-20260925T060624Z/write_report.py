from pathlib import Path
import json,os
root=Path('icon_set/work/primitive-make-ray/review-20260925T060624Z');rows=json.loads((root/'batch.json').read_text())
def link(label,path):return '['+label+']('+os.path.relpath(path,root)+')'
lines=['# Primitive fix results — thuan-mac','', 'Request: 20 icons, offset 0, disapproval reason `manual-fix-request`. All 20 were claimed in this run and finished through `primitive_fix.finish`.','', 'All reviewer feedback was exactly **“Manual fix request”**; no specific geometric instruction was supplied. Revisions were based on the original reference and the rejected before drawing.','', 'All models validate as **valid with zero warnings**. Nineteen pass the full build gate without warnings. The broom passes with a user-authorized, SVG-hash-bound visual exception; its two bristle-spacing advisories are preserved. All are reported **done** and returned to **Ready**.','', 'Reviewed native 48px and 192px light/dark exports. '+link('Preview sheet 1',root/'after-0.png')+' · '+link('Preview sheet 2',root/'after-1.png')+'.','', '| Icon key | Revision | Validation / production outcome | RESULT_DIR and SVG |','|---|---|---|---|']
for r in rows:
 run=Path(r['run']);res=json.loads((run/'result.json').read_text());fix=json.loads((Path(r['fix'])/'result.json').read_text())
 assert fix['outcome']=='done' and fix['review_status']=='ready' and fix['finished_at']
 status='Valid; build pass; done → Ready'
 if res['exception']:status='Valid; build pass with bristle-spacing exception; done → Ready'
 lines.append('| `'+r['key']+'` | '+r['plan']+' | '+status+' | '+link('Run',run)+' · '+link('SVG',run/res['svg'])+' |')
lines+=['','## Construction and evidence','']
for r in rows:
 run=Path(r['run']);res=json.loads((run/'result.json').read_text())
 lines += ['### '+r['key'],'','Feedback: “Manual fix request”.','',f"Keyshape: **{res['keyshape']}**. {res['keyshape_reason']}",'',f"References: {r['lucide']}. Original: "+link('source reference',run/'reference.svg')+'. Rejected drawing: '+link('before',Path(r['fix'])/'before')+'.','', 'Reduction: '+res['omissions'],'',link('Validation',run/'validation.txt')+' · '+link('Result metadata',run/'result.json')+' · '+link('Production finish receipt',Path(r['fix'])/'result.json')+'.','']
 if res['exception']:lines+=['Exception: '+res['exception']['reason'],'','Preserved automatic findings:','']+['- '+w for w in res['build_gate']['warnings']]+['']
(root/'REPORT.md').write_text('\n'.join(lines)+'\n')
print('Verified 20 production finish receipts: done / ready. Report:',root/'REPORT.md')
