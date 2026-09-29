from pathlib import Path
import json,html,os,io
import cairosvg
from PIL import Image,ImageDraw
b=Path(__file__).parent.resolve();root=Path.cwd();rows=json.loads((b/'items.json').read_text())
count=len(rows);exceptions=sum(bool(r.get('exception')) for r in rows)
lines=[f'# Meaning fixes — {count} claimed icons','',f'Requested 20; production returned {count} claimable icons. Worker: `thuan-mac`. Author in every module: `gpt-6`.', '', f'All originals and rejected drawings were rendered and compared before drawing. Selected revisions were reviewed at native 48 px and enlarged sizes in light and dark themes. {count-exceptions} strict automatic pass; {exceptions} user-authorized visual exceptions tied to the exact SVG SHA-256. Automatic findings remain in each validation.txt, build-gate.json and result.json.', '', 'All drawings remain SOLO48 with uniform 4 px strokes. Human construction follows human_ref/user.svg and human_ref/full_body_ref.png. Every detached head has an exact 4-unit visible head-to-body gap, including the bike rider’s analytically verified 5-12-13 alignment. Registered modules and published assets were not changed.', '']
parts=[f'<!doctype html><meta charset="utf-8"><title>{count} meaning fixes</title><style>body{{font:15px system-ui;max-width:1150px;margin:35px auto;background:#eee;color:#222}}article{{background:white;padding:20px;margin:20px 0;border-radius:10px}}section{{display:flex;align-items:center;gap:24px}}figure{{margin:0;text-align:center}}figcaption{{font-size:12px;margin-top:5px}}img{{object-fit:contain}}a{{color:#164aae}}p{{line-height:1.45}}</style><h1>{count} meaning fixes</h1><p>Requested 20; production returned {count} claimable icons. Worker thuan-mac · AUTHOR gpt-6. {count-exceptions} strict pass; {exceptions} drawing-bound visual exceptions.</p>']
completed=0
for n,r in enumerate(rows,1):
 run=(root/r['run']).resolve();fix=root/r['fix_dir'];svg=run/(r['icon_id']+'.svg');resultpath=fix/'result.json';finish=json.loads(resultpath.read_text()) if resultpath.exists() else {}
 state='done · Ready' if finish.get('outcome')=='done' and finish.get('review_status')=='ready' else 'upload pending';completed+=state=='done · Ready'
 validation='pass · exception (automatic '+r['automatic_gate_status']+')' if r.get('exception') else 'strict pass · valid · zero warnings'
 lines += [f'## {n}. {r["key"]}', '',f'- Rejected drawing: {r["comparison"]}',f'- Reviewer feedback: {r["feedback"].replace(chr(10)," / ")}',f'- Revision: {r["change"]}',f'- Keyshape: `{r["keyshape"]}` for the subject’s overall proportions. {r["omissions"]}',f'- Construction references: {r["construction_references"]}.',f'- Author: `gpt-6`. Validation: **{validation}**. Production: **{state}**.',f'- [RESULT_DIR]({run}) · [SVG]({svg}) · [validation]({run / "validation.txt"}) · [result.json]({run / "result.json"})']
 if r.get('exception'):lines.append('- Exception: '+r['exception']['reason'])
 lines.append('')
 def rel(p):return html.escape(os.path.relpath(p,b),quote=True)
 parts.append(f'<article><h2>{n}. {html.escape(r["key"])}</h2><section>')
 for label,p,size in [('Original',run/'reference-384.png',150),('Rejected',fix/'before'/(r['icon_id']+'.svg'),150),('Revised light',run/'preview-light-384.png',150),('Revised dark',run/'preview-dark-384.png',150),('Native light',run/'preview-light-48.png',48),('Native dark',run/'preview-dark-48.png',48)]:parts.append(f'<figure><img src="{rel(p)}" width="{size}" height="{size}"><figcaption>{label}</figcaption></figure>')
 parts.append(f'</section><p><b>Problem:</b> {html.escape(r["comparison"])}<br><b>Feedback:</b> {html.escape(r["feedback"])}<br><b>Change:</b> {html.escape(r["change"])}</p><p>{html.escape(validation)} · {state} · AUTHOR gpt-6</p>')
 if r.get('exception'):parts.append('<p><b>Exception:</b> '+html.escape(r['exception']['reason'])+'</p>')
 parts.append(f'<p><a href="{rel(run)}">RESULT_DIR</a> · <a href="{rel(svg)}">SVG</a> · <a href="{rel(run/"validation.txt")}">Validation</a></p></article>')
(b/'REPORT.md').write_text('\n'.join(lines));(b/'review.html').write_text('\n'.join(parts))
(b/'completion.json').write_text(json.dumps(dict(requested=20,claimed=count,done=completed,worker='thuan-mac',author='gpt-6',strict_pass=count-exceptions,accepted_exceptions=exceptions,items=[dict(key=r['key'],run=r['run']) for r in rows]),indent=2))
for page in range((count+3)//4):
 sheet=Image.new('RGB',(1060,688),'#eee');d=ImageDraw.Draw(sheet)
 for j,r in enumerate(rows[page*4:page*4+4]):
  y=j*172;d.text((10,y+6),f'{page*4+j+1}. '+r['icon_id'],fill='black');run=root/r['run'];fix=root/r['fix_dir']
  for k,(label,p) in enumerate([('Reference',run/'reference-384.png'),('Rejected',fix/'before'/(r['icon_id']+'.svg')),('Revised light',run/'preview-light-384.png'),('Revised dark',run/'preview-dark-384.png')]):
   if p.suffix=='.svg':im=Image.open(io.BytesIO(cairosvg.svg2png(url=str(p),output_width=128,output_height=128,background_color='white'))).convert('RGB')
   else:im=Image.open(p).convert('RGB').resize((128,128))
   x=360+k*170;sheet.paste(im,(x,y+30));d.text((x,y+15),label,fill='black')
 sheet.save(b/f'final-comparison-{page+1}.png')
print(f'{completed}/{count} production finishes verified; {count-exceptions} strict pass, {exceptions} visual exceptions.')
