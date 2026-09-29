from pathlib import Path
import json,hashlib,io
from PIL import Image,ImageDraw
import cairosvg
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
rows=json.loads((ROOT/'batch.json').read_text())
audit=[]
for i,r in enumerate(rows):
 fix=REPO/r['claim_dir'];f=json.loads((fix/'result.json').read_text());run=REPO/f['make_ray_run'];res=json.loads((run/'result.json').read_text());design=json.loads((run/'design.json').read_text())
 assert f['outcome']=='done' and f['review_status']=='ready'
 assert f['author']=='gpt-6' and f['author_ok'] and f['uploaded']
 assert f['build_gate']['status']=='pass'
 svg=run/(r['icon_id']+'.svg');sha=hashlib.sha256(svg.read_bytes()).hexdigest()
 assert svg.read_bytes()==(fix/'after'/svg.name).read_bytes()
 if f['accepted_exception']:assert f['build_gate']['exception']['svg_sha256']==sha
 else:assert f['validation_status']=='valid' and not f['validation_warnings']
 audit.append(dict(index=i,key=r['key'],author=f['author'],production_outcome=f['outcome'],production_review_status=f['review_status'],result_dir=str(run.relative_to(REPO)),svg=str(svg.relative_to(REPO)),svg_sha256=sha,accepted_exception=f['accepted_exception'],automatic_status=f['build_gate'].get('automatic_status','pass'),validation_status=f['validation_status'],build_gate_status=f['build_gate']['status'],finished_at=f['finished_at'],problem=design['problem'],feedback=r['feedback'],change=design['change']))
(ROOT/'audit.json').write_text(json.dumps(audit,indent=2)+'\n')
for start in range(0,20,5):
 sheet=Image.new('RGB',(1120,5*185+35),'#ededeb');draw=ImageDraw.Draw(sheet)
 for x,label in ((10,'Original'),(185,'Rejected'),(360,'Revision'),(540,'48px light'),(650,'48px dark')):draw.text((x,8),label,fill='#111')
 for idx in range(start,start+5):
  r=rows[idx];a=audit[idx];run=REPO/a['result_dir'];y=35+(idx-start)*185
  draw.text((10,y),r['key'],fill='#111')
  paths=[REPO/r['reference'],REPO/r['claim_dir']/'before'/(r['icon_id']+'.svg'),REPO/a['svg']]
  for col,p in enumerate(paths):
   data=p.read_text().replace('currentColor','#141413');im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=data.encode(),output_width=144,output_height=144,background_color='white'))).convert('RGB');sheet.paste(im,(10+col*175,y+24))
  for x,theme in ((550,'light'),(660,'dark')):sheet.paste(Image.open(run/f'preview-{theme}-48.png').convert('RGB'),(x,y+64))
  draw.text((760,y+55),'Ready | gpt-6',fill='#111')
  draw.text((760,y+78),'pass + exception' if a['accepted_exception'] else 'strict pass',fill='#111')
 sheet.save(ROOT/f'final-comparison-{start//5+1}.png')
exc=sum(a['accepted_exception'] for a in audit)
lines=['# Meaning fixes — 20 icons', '',f'All 20 claimed icons were fixed, uploaded using primitive_fix.py finish, and returned to **Ready** on production. Worker: `thuan-mac`. Author on every fixed module: `gpt-6`. {20-exc} strict passes; {exc} exact-SVG visual exceptions under the user\'s explicit authorization. Automatic findings are retained in every validation record.','', 'All original and rejected drawings were inspected before authoring. Final drawings were inspected at 48px and enlarged in light and dark themes. No registered modules, published assets or editorial catalogs were changed.','', '## Comparison sheets','']
for n in range(1,5):lines.append(f'- [Original / rejected / revision / native light and dark — icons {(n-1)*5+1}–{n*5}]({ROOT/f"final-comparison-{n}.png"})')
lines+=['','[Machine-readable completion and SVG integrity audit]('+str(ROOT/'audit.json')+')','']
for i,(r,a) in enumerate(zip(rows,audit)):
 run=REPO/a['result_dir'];d=json.loads((run/'design.json').read_text());fix=REPO/r['claim_dir'];f=json.loads((fix/'result.json').read_text())
 status='Strict pass: model valid, zero warnings, full QA pass.' if not a['accepted_exception'] else f'Accepted visual exception; full QA status **pass**, automatic status **{a["automatic_status"]}**, model status **{a["validation_status"]}**. Automatic findings remain recorded.'
 shape_reason='Tall natural subject; keep its narrow silhouette.' if d['keyshape'].startswith('VRECT') else 'Natural horizontal silhouette.' if d['keyshape'].startswith('HRECT') else 'Balanced footprint for the complete subject or reference composition.'
 lines += [f'## {i+1}. {r["key"]}','',f'**Original versus rejected:** {d["problem"]}',f'**Reviewer feedback:** {r["feedback"]}.',f'**Changed:** {d["change"]}',f'**Construction:** {d["refs"]}. Keyshape `{d["keyshape"]}`. {shape_reason}',f'**Omissions:** {"; ".join(d.get("omissions",[])) or "No defining reference feature omitted; small details simplified to 4px UI strokes."}',f'**AUTHOR:** `gpt-6`. **Production:** done → Ready.',f'**Validation:** {status}']
 if a['accepted_exception']:lines.append('**Exception reason:** '+f['build_gate']['exception']['reason'])
 lines+=['',f'- [RESULT_DIR]({run}) · [SVG]({REPO/a["svg"]}) · [Python module]({REPO/f["module"]})',f'- [Original]({REPO/r["reference"]}) · [Rejected SVG]({fix/"before"/(r["icon_id"]+".svg")})',f'- [Light preview]({run/"preview-light-48.png"}) · [Dark preview]({run/"preview-dark-48.png"}) · [Full validation and exception record]({fix/"validation.txt"}) · [Production completion]({fix/"result.json"})','']
(ROOT/'report.md').write_text('\n'.join(lines)+'\n')
print(f'Verified {len(audit)} done / Ready, {20-exc} strict passes, {exc} accepted exceptions, AUTHOR gpt-6, matching local/uploaded SVGs.')
print(ROOT/'report.md')
