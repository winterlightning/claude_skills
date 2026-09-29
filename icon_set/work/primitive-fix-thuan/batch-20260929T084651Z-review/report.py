from pathlib import Path
import json,html,os,base64,io
import cairosvg
B=Path(__file__).parent
R=B.parents[3]
runs=json.loads((B/'final-runs.json').read_text())
items={r['id']:r for r in json.loads((B/'items.json').read_text())}
def link(p): return os.path.relpath(p,B)
def data(p): return 'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()
def esc(v):return html.escape(str(v))
cards=[];md=['# Meaning fixes — thuan-mac','', '20 claimed icons. AUTHOR = `gpt-6` for every revision. Each original and rejected drawing was opened and compared before authoring. All revisions were inspected at 48px and enlarged in light and dark themes.','', 'Reviewer feedback for all 20: “Does not convey the intended meaning.”','', 'Five drawings passed the strict model and full build gate with zero warnings. Fifteen use the user-authorized drawing-specific exception mechanism; their original automatic errors and warnings remain in validation files. Exceptions retain 48×48 canvases and uniform 4px strokes.','', '[Visual comparison report](report.html)','']
count=0
for n,r in enumerate(runs,1):
 it=items[r['icon_id']];p=R/r['run'];f=R/it['fix'];receipt=json.loads((f/'result.json').read_text()) if (f/'result.json').exists() else None
 done=receipt and receipt.get('outcome')=='done' and receipt.get('review_status')=='ready'
 count+=bool(done)
 status=('Done · Ready' if done else 'Upload pending')+' · '+('pass with documented exception' if r['accepted_exception'] else 'strict pass; zero warnings')
 before=f/'before'/f"{r['icon_id']}.svg"
 bpng=p/'before-comparison.png'
 cairosvg.svg2png(url=str(before),write_to=str(bpng),output_width=192,output_height=192,background_color='white')
 images=''.join(f'<figure><img src="{data(img)}" width="{size}" height="{size}"><figcaption>{label}</figcaption></figure>' for img,label,size in [(p/'reference.png','Original reference' if n!=18 else 'Current drawing (no original available)',144),(bpng,'Rejected drawing',144),(p/'preview-light-384.png','Revision · light',144),(p/'preview-dark-384.png','Revision · dark',144),(p/'preview-light-48.png','Native 48px',48),(p/'preview-dark-48.png','Native 48px',48)])
 ex=(' Exception reason: '+r['exception']['reason']) if r['accepted_exception'] else ''
 md += [f'## {n}. {it["key"]}','',f'**{status}** · AUTHOR: `gpt-6` · keyshape: `{r["keyshape"]}`','',f'**Before / feedback:** {r["comparison"]} Reviewer asked to restore the intended meaning.','',f'**Changed:** {r["change"]}','',f'**Construction:** {r["construction_reference"]}','',f'**Validation:** model `{r["validation_status"]}`; full gate `{r["build_gate"]["status"]}`. {ex}','',f'[RESULT_DIR]({link(p)}/) · [SVG]({link(p/r["svg"])}) · [Python]({link(p/r["module"])}) · [Validation]({link(p/"validation.txt")}) · [Production receipt]({link(f/"result.json")})','']
 cards.append(f'<article id="icon-{n}"><h2>{n}. {esc(it["key"])}</h2><p class="status">{esc(status)} · AUTHOR: gpt-6</p><div class="images">{images}</div><p><b>Before:</b> {esc(r["comparison"])}</p><p><b>Changed:</b> {esc(r["change"])}</p><p>{esc(ex)}</p><p><a href="{esc(link(p/r["svg"]))}">SVG</a> · <a href="{esc(link(p/r["module"]))}">Python</a> · <a href="{esc(link(p/"validation.txt"))}">Validation</a> · <a href="{esc(link(p))}/">Result directory</a></p></article>')
(B/'report.md').write_text('\n'.join(md))
(B/'report.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>20 meaning fixes · thuan-mac</title><style>body{font:15px system-ui;background:#f1f2f3;color:#182028;margin:24px auto;max-width:1100px;padding:0 20px}h1{font-size:30px}h2{font-size:18px;overflow-wrap:anywhere}.status{color:#27614b}.images{display:flex;align-items:center;gap:16px;flex-wrap:wrap}figure{margin:0;text-align:center}figcaption{font-size:11px;color:#59636c;margin:6px 0}article{background:white;border:1px solid #dbe0e3;border-radius:10px;padding:22px;margin:20px 0}p{line-height:1.55}a{color:#135ca8}img{object-fit:contain}</style></head><body><h1>20 meaning fixes · thuan-mac</h1><p>'+str(count)+'/20 confirmed Done → Ready. Five strict passes; fifteen documented drawing-specific exceptions. All revisions retain a 48×48 canvas and 4px strokes, with automatic findings preserved.</p><p>Reviewer feedback: “Does not convey the intended meaning.” The laptop worker had no original reference; its current drawing and identity supplied the brief.</p>'+''.join(cards)+'</body></html>')
print('Report generated:',count,'/20 confirmed Done and Ready')
