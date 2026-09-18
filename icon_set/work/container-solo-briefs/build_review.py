"""Review artifact for the source-linked solo generation batch."""
from pathlib import Path
import json,html,base64,io
from icon_set.model.icons.registry import create
from PIL import Image,ImageDraw
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/container-solo-briefs/briefs.json'
AUTHOR='gpt-6'
w=Path(__file__).resolve().parent;rows=json.loads((w/'generation-results.json').read_text());briefs=json.loads((w/'briefs.json').read_text());done={r['index'] for r in rows}
esc=html.escape
out=['''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Container sub icons · Solo generation</title><style>*{box-sizing:border-box}body{font:15px system-ui;background:#f5f5f0;color:#252822;max-width:1200px;margin:40px auto;padding:0 24px}h1{font-size:32px}input{font:inherit;padding:13px;width:100%;margin:20px 0;border:1px solid #bbb;border-radius:8px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}article{background:white;border:1px solid #ddd;border-radius:12px;padding:18px}h2{font-size:16px;margin:0 0 14px}.previews{display:flex;justify-content:space-around;align-items:center;gap:8px}.sample{width:76px;height:90px;display:grid;place-items:center;border-radius:8px;background:#fafafa;color:#111}.sample.dark{background:#171717;color:white}.sample.dark img{filter:invert(1)}.sample svg,.sample img{width:48px;height:48px}.sample small{font-size:10px}p{line-height:1.5}.muted,summary{font-size:12px;color:#596454}pre{font:12px system-ui;white-space:pre-wrap;overflow-wrap:anywhere}a{color:#356342}[hidden]{display:none!important}li{margin-bottom:8px}</style><h1>Container sub icons · Solo generation</h1><p><a href="../container-pair-trials/index.html">Preview container pairings</a></p><p><strong>80 references covered by 78 unique solo icons.</strong> 37 new drawings + 41 existing drawings reused across 43 references. All tagged <strong>sub icon</strong>.</p><p>SOLO48 · stroke 4 · Current exported icons in both themes; reload after rebuilding to see changes. Reference drawings appear first. Each reference remains linked by its source ID to the solo model.</p><details><summary>8 references still pending</summary><ul>''']
for i,r in enumerate(briefs):
 if i not in done:
  why='Component split required; preserve the prepared component briefs.' if i!=29 else 'Plain horizontal dots cannot fill a SOLO48 keyshape without changing the subject; pending envelope or family decision.'
  out.append(f'<li><b>{esc(r["concept"])}</b> — {why}</li>')
out.append('</ul></details><input type="search" aria-label="Filter icons" placeholder="Search name, icon ID, or new/reused"><div class="grid">')
for r in rows:
 b=briefs[r['index']];o=create(r['icon_id']);assert o.validate_icon().status=='valid';svg=o.to_svg();r['validation']='valid';r['keyshape']=o.keyshape.name
 source=base64.b64encode(cairosvg.svg2png(url=b['source_path'],output_width=48,output_height=48)).decode()
 out.append(f'<article data-search="{esc((b["concept"]+" "+r["icon_id"]+" "+r["method"]).lower())}"><h2>{esc(b["concept"])}</h2><div class="previews"><div class="sample"><img alt="Original reference" src="data:image/png;base64,{source}"><small>Reference</small></div><a class="sample" href="http://localhost:8000/gallery/index.html?q={r["icon_id"]}"><img alt="Current solo icon" src="../../dist/solo48/{r["icon_id"]}.svg"><small>Solo · light</small></a><a class="sample dark" href="http://localhost:8000/gallery/index.html?q={r["icon_id"]}"><img alt="Current solo icon, dark theme" src="../../dist/solo48/{r["icon_id"]}.svg"><small>Solo · dark</small></a></div><p class="muted">{esc(r["method"].capitalize())} · {r["keyshape"]} · sub icon · valid</p><a href="http://localhost:8000/gallery/primitives.html?status=all&amp;q={b["uuid"]}">Reference in Progression</a> · <a href="http://localhost:8000/gallery/index.html?q={r["icon_id"]}">Linked solo icon</a><p class="muted">Source: {b["uuid"]}<br>Model: solo/{esc(r["icon_id"])}</p><details><summary>Brief and construction</summary><p>{esc(r.get("plan","Reused an existing native SOLO48 drawing after reference comparison and validation."))}</p><p>Icon: {esc(r["icon_id"])}</p><pre>{esc(b["brief"])}</pre></details></article>')
out.append('</div><script>document.querySelector("input").addEventListener("input",e=>{const q=e.target.value.toLowerCase();document.querySelectorAll("article").forEach(a=>a.hidden=!a.dataset.search.includes(q))})</script></html>')
(w/'index.html').write_text(''.join(out));(w/'generation-results.json').write_text(json.dumps(rows,indent=2))
# Save final native-size visual evidence after final repairs.
for page in range(4):
 im=Image.new('RGB',(1000,640),'#ddd');d=ImageDraw.Draw(im)
 for j,r in enumerate(rows[page*20:page*20+20]):
  x=j%5*200;y=j//5*160;svg=create(r['icon_id']).to_svg()
  for bg,fg,dx in [('#fff','#111',0),('#151515','#fff',98)]:
   d.rectangle((x+dx,y,x+dx+96,y+100),fill=bg)
   p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),output_width=48,output_height=48)));im.paste(p,(x+dx+24,y+20),p)
  d.text((x+3,y+106),f"{r['index']}: {briefs[r['index']]['concept'][:27]}",fill='black')
 im.save(w/f'final-native-{page}.png')
print(w/'index.html')
