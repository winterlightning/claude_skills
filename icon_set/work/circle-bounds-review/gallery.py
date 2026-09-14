from pathlib import Path
import json,io,html
from PIL import Image,ImageDraw
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/circle-bounds-review/results.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;rows=json.loads((w/'results.json').read_text());assert len(rows)==6 and all(r['qa']['status']=='pass' for r in rows)
notes=['Outer radius corrected; the spindle hole stays the same.','Rim corrected and sector arc moved outward slightly to retain clearance around the hub.','Rim corrected; smaller hub and matching reflection arcs leave clear space on both sides.','The open rim follows one exact circle; the jagged crack remains.','Face rim corrected; paired lenses are slightly smaller and closer to the center, with a rebalanced smile.','Rim corrected; the three slot marks are repositioned between the hub and rim.']
parts=[];im=Image.new('RGB',(1200,650),'#f5f4ef');d=ImageDraw.Draw(im)
for j,(r,note) in enumerate(zip(rows,notes)):
 n=r['original'];before=(w/(n+'-before.svg')).read_text();after=(w/(r['candidate']+'.svg')).read_text()
 def figure(svg,label):
  guide='<svg class="guide" viewBox="0 0 48 48"><circle cx="24" cy="24" r="22" fill="none" stroke="#d67838" stroke-width=".4" stroke-dasharray="1 1"/></svg>'
  return '<div class="sample"><small>'+label+'</small><div class="large">'+svg+guide+'</div><div class="native">'+svg+'<small>48 px</small></div></div>'
 parts.append('<article><h2>'+html.escape(n)+'</h2><div class="pair">'+figure(before,'Before')+figure(after,'Repaired')+'</div><p>'+note+'</p><span>Bounds · spacing · holes pass</span></article>')
 x=j%3*400;y=j//3*325;d.text((x+8,y+5),n[:46],fill='#222')
 for k,s in enumerate([before,after]):
  png=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor','#242521').encode(),output_width=160,output_height=160)));im.paste(png,(x+15+k*195,y+35),png)
  for theme,col in enumerate(['#242521','#edf1e9']):
   if theme:d.rectangle((x+85+k*195,y+220,x+151+k*195,y+285),fill='#202720')
   png=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor',col).encode(),output_width=48,output_height=48)));im.paste(png,(x+20+k*195+theme*75,y+228),png)
im.save(w/'preview.png')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Circle bounds — six repairs</title><style>
:root{--bg:#f5f4ef;--card:#fff;--ink:#242521;--muted:#6d736b;--line:#dce0d7;--badge:#e9f4eb;--green:#22623d}body.dark{--bg:#171c18;--card:#242b25;--ink:#eef2e9;--muted:#acb8ab;--line:#3b483d;--badge:#304936;--green:#b1dbbb}*{box-sizing:border-box}body{font:14px/1.5 system-ui;margin:0;background:var(--bg);color:var(--ink)}header,main,footer{max-width:1360px;margin:auto;padding:24px}h1{font-size:32px;margin:6px 0}header p{max-width:900px;color:var(--muted)}button{background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:7px;padding:8px 14px;cursor:pointer}main{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}article{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}h2{font-size:14px;overflow-wrap:anywhere;min-height:42px;margin:0}.pair{display:grid;grid-template-columns:1fr 1fr}.sample{text-align:center}.sample+.sample{border-left:1px solid var(--line)}small{font-size:11px;color:var(--muted)}.large{height:180px;position:relative;display:flex;align-items:center;justify-content:center}.large>svg{width:160px;height:160px}.large .guide{position:absolute;pointer-events:none}.native{display:flex;justify-content:center;align-items:center;gap:6px}.native svg{width:48px;height:48px}article p{font-size:12px;color:var(--muted);min-height:54px}article>span{background:var(--badge);color:var(--green);font-size:11px;padding:5px 8px;border-radius:5px}footer{font-size:12px;color:var(--muted)}@media(max-width:1050px){main{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:670px){main{grid-template-columns:1fr}}
</style><body><header><small>PICTOGRAPHIC · SOLO48 · REVIEW</small><h1>Six circles, fitted to the envelope.</h1><p>All six repaired versions pass bounds, spacing and hole checks with zero warnings. The orange dashed circle marks the required visible-ink envelope. Each repaired rim reaches radius 22, including the 4-pixel stroke.</p><p>Review versions are ready below. Original icons remain unchanged until you approve these repairs.</p><button id="theme">Dark theme</button></header><main>__CARDS__</main><footer>All six retain the CIRCLE keyshape. Local Lucide disc, disc-3 and glasses originals and atomic geometry informed shared-center circles, opposing reflection curves and paired lenses. No validation rules changed.</footer><script>document.querySelector('#theme').onclick=e=>{const dark=document.body.classList.toggle('dark');e.target.textContent=dark?'Light theme':'Dark theme'};</script></body></html>'''
(w/'review.html').write_text(page.replace('__CARDS__',''.join(parts)))
(w/'manifest.json').write_text(json.dumps({'status':'awaiting visual approval','count':6,'full_passes':6,'originals_modified':False,'notes':dict(zip([r['original'] for r in rows],notes))},indent=2))
