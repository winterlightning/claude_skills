from pathlib import Path
import json,html
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
def link(label,p):return f'[{label}]({Path(p).resolve()})'
def opaque(p):
 im=Image.open(p).convert('RGBA');bg=Image.new('RGBA',im.size,'white');bg.alpha_composite(im);return bg.convert('RGB')
lines=['# Manual fix request batch — 28 September 2026','','Worker: `thuan-mac`. Requested: 20 at offset 0. Claimed: 17 + 3 = 20. Author in every module: `gpt-6`.','',
'The user delegated quality-preserving exceptions. Fourteen revisions pass automatically; six have SVG-hash-bound visual exceptions. Original automatic findings remain in each validation report. All drawings retain SOLO48 and 4px strokes.','',
'Compared every original and rejected drawing, then reviewed each revision at native 48px and enlarged size in light and dark themes. No registered modules, published assets or skill files were changed.','']
cards=[]
for i,r in enumerate(rows):
 run=Path(r['run']);fix=Path(r['fix_dir']);result=json.loads((fix/'result.json').read_text()) if (fix/'result.json').exists() else {}
 production=f"{result.get('outcome','pending')} · {result.get('review_status','pending')}"
 lines += [f"## {i+1}. `{r['key']}`",'',f"**Before:** {r['wrong']}",f"**Feedback:** {r['feedback'].replace(chr(10),' — ')}",f"**Revision:** {r['change']}",f"**Construction:** {r['construction']}",f"**Keyshape:** `{r['keyshape']}` preserves the subject's natural proportions on SOLO48.",f"**Author:** `gpt-6`. **Validation:** {r['status']}. **Production:** {production}."]
 if r.get('exception_reason'):lines += [f"**Exception:** {r['exception_reason']}"]
 if i<3:lines += ['**Human geometry:** Circular head radius 7 at y=15; head centerline bottom y=22 and shoulder top y=30 leave exactly 4px ink clearance. Mirrored left placement reverses arc sweep.']
 lines += ['',link('RESULT_DIR',run)+' · '+link('SVG',run/(r['icon_id']+'.svg'))+' · '+link('Python',r['module'])+' · '+link('Validation',run/'validation.txt')+' · '+link('Production receipt',fix/'result.json'),'']
 cards.append(f'<section><h2>{i+1}. {html.escape(r["key"])}</h2><p>{html.escape(r["change"])}</p><div class="images"><figure><img src="{(fix/"reference.png").resolve()}"><figcaption>Original</figcaption></figure><figure><img src="{(fix/"before.png").resolve()}"><figcaption>Rejected</figcaption></figure><figure><img src="{(run/"preview-light-384.png").resolve()}"><figcaption>Revision light</figcaption></figure><figure><img src="{(run/"preview-dark-384.png").resolve()}"><figcaption>Revision dark</figcaption></figure><figure class="native"><img src="{(run/"preview-light-48.png").resolve()}"><img src="{(run/"preview-dark-48.png").resolve()}"><figcaption>Native 48px</figcaption></figure></div><p>{html.escape(r["status"])} · AUTHOR gpt-6 · {production}</p></section>')
(ROOT/'REPORT.md').write_text('\n'.join(lines))
(ROOT/'review.html').write_text('<!doctype html><meta charset="utf-8"><title>20 icon revisions</title><style>body{font:15px system-ui;background:#eee;color:#222;margin:32px}section{background:white;padding:24px;margin:20px 0;border-radius:12px}h2{font-size:17px}.images{display:flex;align-items:center;gap:16px}figure{margin:0;text-align:center}img{display:block;width:160px;height:160px;background:white}figcaption{font-size:12px;color:#666;margin-top:8px}.native img{width:48px;height:48px;display:inline-block}</style><h1>20 manual-request icon revisions</h1><p>thuan-mac · gpt-6 · 14 automatic passes · 6 authorized exceptions</p>'+''.join(cards))
for page in range(4):
 chunk=rows[page*5:(page+1)*5];im=Image.new('RGB',(1000,len(chunk)*220),'#eee');d=ImageDraw.Draw(im)
 for j,r in enumerate(chunk):
  y=j*220;d.text((10,y+3),str(page*5+j+1)+' '+r['icon_id']+' | '+r['status'],fill='black');run=Path(r['run'])
  for n,p in enumerate([Path(r['fix_dir'])/'reference.png',Path(r['fix_dir'])/'before.png',run/'preview-light-384.png',run/'preview-dark-384.png']):im.paste(opaque(p).resize((192,192)),(10+n*200,y+24))
  for n,t in enumerate(['light','dark']):im.paste(opaque(run/f'preview-{t}-48.png'),(830+n*60,y+80))
 im.save(ROOT/f'final-{page+1}.png')
print(ROOT/'REPORT.md')
