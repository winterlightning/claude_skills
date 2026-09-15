"""Publish the reviewed before/after centerlines and unresolved findings."""
from pathlib import Path
import json,base64,html,io,xml.etree.ElementTree as ET
from collections import Counter
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/nonhuman-reconstruction/audit.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
A=json.loads((W/'audit.json').read_text())
counts=Counter(i['audit_status'] for i in A)
escape=html.escape

def image_data(p,centerline=False):
 if not p.exists():return ''
 if centerline:
  root=ET.fromstring(p.read_text())
  for e in root.iter():
   if e.get('stroke-width'):e.set('stroke-width','0.5')
   if e.get('stroke') and e.get('stroke')!='none':e.set('stroke','#1687c2')
  data=cairosvg.svg2png(bytestring=ET.tostring(root),output_width=160,output_height=160)
  return 'data:image/png;base64,'+base64.b64encode(data).decode()
 return 'data:image/svg+xml;base64,'+base64.b64encode(p.read_bytes()).decode()

cards=[]
for i in A:
 status=i['audit_status'];name=i['icon_id']
 if status in ('skipped-human','removed-elsewhere'):continue
 repaired=status=='reconstructed'
 old=W/'before-svg'/i['svg']
 if not old.exists():old=Path('icon_set/dist/failed/solo48')/i['svg']
 current=W/(name+'.svg') if repaired else old
 before=image_data(old);after=image_data(current);thin=image_data(current,True)
 visuals=f'<div class="drawings"><figure><img src="{before}" alt="Previous {escape(name)}"><figcaption>Before</figcaption></figure><figure><img src="{after}" alt="Current {escape(name)}"><figcaption>{"Rebuilt" if repaired else "Original retained"}</figcaption></figure><figure><img src="{thin}" alt="Centerline of {escape(name)}"><figcaption>Centerline</figcaption></figure></div>'
 natives=f'<div class="native"><span>48 px</span><img src="{after}" alt="Light theme"><span class="dark"><img src="{after}" alt="Dark theme"></span></div>'
 note=i.get('plan','') if repaired else i.get('blocker','Manual review required.')
 errors='' if repaired else '<details><summary>Validation evidence</summary><ul>'+''.join('<li>'+escape(e)+'</li>' for e in i.get('errors',[]))+'</ul></details>'
 cards.append(f'<article data-state="{"repaired" if repaired else "held"}" data-name="{escape(name)}"><header><h2>{escape(name)}</h2><span class="badge {"pass" if repaired else "hold"}">{"Rebuilt · QA passed" if repaired else "Still needs review"}</span></header>{visuals}{natives}<p>{escape(note)}</p>{errors}</article>')
manual=sum(counts[s] for s in ('held-visual','blocked-geometry'))
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nonhuman icon reconstruction review</title><style>
*{box-sizing:border-box}body{margin:0;padding:28px;background:#f4f4f2;color:#212121;font:15px/1.5 system-ui,sans-serif}main{max-width:1500px;margin:auto}h1{font-size:30px;margin:8px 0}h2{font-size:15px;overflow-wrap:anywhere;margin:0 0 8px}a{color:#23629b}p{max-width:900px}.summary{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}.summary div{background:white;border:1px solid #ddd;border-radius:10px;padding:12px 20px}.summary strong{display:block;font-size:25px}.filters{display:flex;gap:12px;margin:20px 0;position:sticky;top:0;background:#f4f4f2;padding:12px 0;z-index:1}input,select{font:inherit;padding:10px;border:1px solid #bbb;border-radius:6px}input{min-width:0;flex:1}#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(390px,1fr));gap:18px}article{background:white;border:1px solid #ddd;border-radius:12px;padding:18px;min-width:0}article[hidden]{display:none}.badge{font-size:12px;padding:3px 8px;border-radius:20px;display:inline-block}.pass{background:#e6f4e9;color:#236038}.hold{background:#fff0d2;color:#785b15}.drawings{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin:12px 0}figure{margin:0;text-align:center}figure img{display:block;width:100%;height:145px;object-fit:contain}figcaption{font-size:12px;color:#666}.native{display:flex;align-items:center;gap:14px}.native img{width:48px;height:48px}.dark{display:inline-flex;background:#18181b;padding:5px;border-radius:5px}.dark img{filter:invert(1)}article p{font-size:13px;color:#555}details{font-size:12px;overflow-wrap:anywhere}footer{margin:32px 0;color:#666;font-size:13px}@media(max-width:480px){body{padding:14px}#grid{grid-template-columns:1fr}figure img{height:110px}}
</style><main><a href="index.html?tab=failed&family=solo">← Failed icons</a><h1>Nonhuman icon reconstruction</h1><p>Reviewed the current failed batch using its rendered strokes and centerlines. Originals were updated in place. Human figures were set aside. Only reconstructions that passed both visual review and geometry QA were retained.</p>'''
page+=f'<div class="summary"><div><strong>{counts["reconstructed"]}</strong>Rebuilt and passed</div><div><strong>{manual}</strong>Still need review</div><div><strong>{counts["skipped-human"]}</strong>Human icons skipped</div><div><strong>{counts["removed-elsewhere"]}</strong>Removed elsewhere during review</div></div>'
page+='<p>Curves use coherent arcs and Bézier paths; intentional corners remain. Lucide armchair, shopping bag, battery, fish, dog, flame, plane, shirt and box references informed the relevant constructions. Each card records the simplification and spacing change. Held designs retain their originals and failed evidence.</p><div class="filters"><input id="search" type="search" placeholder="Find an icon" aria-label="Find an icon"><select id="state" aria-label="Review status"><option value="all">All reviewed icons</option><option value="repaired">Rebuilt and passed</option><option value="held">Still need review</option></select></div><section id="grid">'+''.join(cards)+'</section>'
page+='<footer>Review scope: '+str(len(A))+' icons in the captured Failed batch. No human drawings were revised and no versioned icon modules were created. The full library still contains unrelated failed icons. QA summaries and source plans are retained in the reconstruction audit.</footer><script>function filter(){const q=document.querySelector("#search").value.toLowerCase(),s=document.querySelector("#state").value;document.querySelectorAll("article").forEach(a=>a.hidden=!a.dataset.name.includes(q)||(s!=="all"&&a.dataset.state!==s));}document.querySelector("#search").addEventListener("input",filter);document.querySelector("#state").addEventListener("change",filter);</script></main></html>'
(W/'review.html').write_text(page)
Path('icon_set/dist/gallery/nonhuman-reconstruction-review.html').write_text(page)
print(dict(counts))
