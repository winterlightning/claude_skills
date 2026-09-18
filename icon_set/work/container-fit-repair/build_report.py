from pathlib import Path
import json,base64,html,hashlib
import xml.etree.ElementTree as ET
from shapely.geometry import shape
from icon_set.scripts.container_placement import Artwork
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,check_pair
ROOT=Path(__file__).resolve().parent;BASE=ROOT.parents[1]
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
rows=json.loads((ROOT/'revisions-measured.json').read_text());search=json.loads((ROOT/'placement-search.json').read_text());before={r['container']:r for r in search};vector={c['container']:c for c in json.loads((BASE/'work/container-vector-report/results.json').read_text())['containers']}
subs=['check-mark','add-sub32','heart-state-63'];subpaths={n:BASE/f'dist/sub32/{n}.svg' for n in subs}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def uri(p):return 'data:image/svg+xml;base64,'+base64.b64encode(p.read_bytes()).decode()
def combination(host,sub,center,file):
 root=ET.Element('{'+NS+'}svg',{'viewBox':'0 0 64 64','width':'256','height':'256'})
 for p,x,y,size in [(host,0,0,64),(sub,center[0]-16,center[1]-16,32)]:ET.SubElement(root,'{'+NS+'}image',{'href':uri(p),'x':str(x),'y':str(y),'width':str(size),'height':str(size)})
 (ROOT/file).write_text(ET.tostring(root,encoding='unicode'));return file

def comparison(parent,sub,old,new,center_old,center_new,kind,metrics,reason):
 a=combination(old,subpaths[sub],center_old,f'{parent}--{sub}-before.svg')
 b=combination(new,subpaths[sub],center_new,f'{parent}--{sub}-after.svg')
 gap=metrics['ink_gap_lower_units'];hi=metrics['ink_gap_upper_units']
 return f'<article data-name="{parent}" data-kind="{kind}"><h2>{html.escape(parent)}</h2><p>{html.escape(sub)} · {html.escape(reason)}</p><div class="pair"><figure><a href="{a}"><img src="{a}" loading="lazy"></a><figcaption>Before</figcaption></figure><figure><a href="{b}"><img src="{b}" loading="lazy"></a><figcaption>After · gap {gap:.4f}–{hi:.4f} u</figcaption></figure></div><p class="meta">Center {center_old} → {center_new}. Native sub size: 32 × 32.</p></article>'

cards=[];adjustments={'version':1,'symbols':subs,'revisions':{},'placements':{}}
for r in rows:
 assert r['validation']=='status: valid',r['variant']
 for p in r['pairs'].values():assert p['status']=='pass',r['variant']
 parent=r['parent'];old=BASE/f'dist/container64/{parent}.svg';new=ROOT/(r['variant']+'.svg')
 adjustments['revisions'][parent]={'variant':r['variant'],'module':r['module'],'parent_sha256':digest(old),'variant_sha256':digest(new),'center':r['center'],'reason':r['reason'],'pairs':r['pairs']}
 for sub in subs:cards.append(comparison(parent,sub,old,new,before[parent]['center'],r['center'],'revision',r['pairs'][sub],r['reason']))
shifted=[]
for r in search:
 name=r['container'];path=BASE/f'dist/container64/{name}.svg'
 if not r['shifted']:continue
 host=VectorInk.from_art(read_art(path.read_text()));zone=vector[name];inner=shape(zone['safe_zone_inner']);outer=shape(zone['safe_zone_outer'])
 for sub,center in r['shifted'].items():
  art=Artwork.read(subpaths[sub].read_text(),32);ink=VectorInk.from_art(art,(1,center[0]-16,center[1]-16))
  metrics=check_pair(host,ink,inner,outer);assert metrics['status']=='pass',(name,sub,metrics)
  item={'container':name,'sub':sub,'center':center,'host_sha256':digest(path),'sub_sha256':digest(subpaths[sub]),'measurements':metrics,'visual_status':'centerline-priority' if abs(center[0]-r['center'][0])<0.001 else 'off-axis-needs-visual-review'}
  shifted.append(item);adjustments['placements'].setdefault(name,{})[sub]=item
  cards.append(comparison(name,sub,path,path,r['center'],center,'placement',metrics,('Centered placement; container artwork unchanged.' if item['visual_status']=='centerline-priority' else 'Off-axis clearance candidate — still needs visual review.')))
remaining=[{'container':r['container'],'symbols':r['unresolved'],'area_status':vector[r['container']]['status']} for r in search if r['unresolved'] and r['container'] not in adjustments['revisions']]
summary={'revised_containers':len(rows),'revised_pairs':len(rows)*3,'placement_only_pairs':len(shifted),'placement_only_containers':len({r['container'] for r in shifted}),'remaining_containers_with_failed_pairs':len(remaining),'remaining':remaining}
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2));(ROOT/'fit-adjustments.json').write_text(json.dumps(adjustments,indent=2))
remaining_html=''.join(f'<tr><td>{html.escape(r["container"])}</td><td>{html.escape(", ".join(r["symbols"]))}</td><td>{r["area_status"]}</td></tr>' for r in remaining)
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Container fit revisions — before and after</title><style>body{font:15px system-ui;margin:28px;background:#f5f7fa;color:#202630}header{max-width:1050px}h1{font-size:30px}p{line-height:1.55}h2{font-size:16px}a{color:#235da6}nav{position:sticky;top:0;padding:14px 0;background:#f5f7fa;z-index:1;display:flex;gap:12px;align-items:center}input,select{font:inherit;padding:9px;border:1px solid #cbd3dd;border-radius:7px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:18px}article{background:white;border:1px solid #dce2e9;border-radius:12px;padding:20px}article[hidden]{display:none}.pair{display:flex;gap:20px}figure{margin:0;flex:1;min-width:0}img{width:100%;max-width:192px}figcaption{font-size:13px}.meta{font-size:12px;color:#657184}details{margin:24px 0}summary{cursor:pointer}td,th{text-align:left;padding:8px;border-bottom:1px solid #dce2e9}table{border-collapse:collapse;font-size:13px}body.dark{background:#141922;color:#eef2f7}body.dark article,body.dark nav{background:#202733}body.dark img{filter:invert(1)}body.native img{width:64px}</style><header><h1>Container fit revisions</h1><p><a href="../container-size-suggestions/index.html"><b>Compare centered 32 × 32 and suggested 24 × 24 sub-icons</b></a></p>'''+f'<p><b>{len(rows)} revised containers · {len(shifted)} placement-only corrections · native 32 × 32 symbols</b></p>'+'''<p>The revised containers keep their defining details and are saved as independent variants. Original drawings remain available. Every “After” combination here passes the 2-unit vector clearance, containment and canvas checks for the symbol shown. These checks cover the check mark, plus and heart only—not all 266 sub-icons.</p><p>Centered placement has priority. The placement search first preserves the content centerline and adjusts vertical position for balance and clearance. Off-axis fallback candidates are explicitly marked for visual review. The placement corrections preserve the existing container shape. Width, height and stroke are unchanged. Open interiors and distinctive shapes without a verified fit remain explicitly unresolved.</p>'''+f'<details><summary>{len(remaining)} containers still have at least one unresolved sample combination</summary><p>These were not automatically reshaped. This list is a review queue, not proof that no possible placement or careful redesign exists. “Overlay” entries are intentional overlapping compositions, not ordinary empty enclosures.</p><table><tr><th>Container</th><th>Unresolved symbols</th><th>Interior status</th></tr>{remaining_html}</table></details>'+'''<p><a href="fit-adjustments.json">Measured revisions and placement coordinates</a> · <a href="../container-sub-preview/index.html">Original comparison gallery</a></p></header><nav><input id="q" placeholder="Find container…" aria-label="Find container"><select id="kind" aria-label="Change type"><option value="all">All changes</option><option value="revision">Revised containers</option><option value="placement">Placement only</option></select><label><input id="dark" type="checkbox"> Dark</label><label><input id="native" type="checkbox"> Native size</label><span id="count"></span></nav><main>'''+''.join(cards)+'''</main><script>const cards=[...document.querySelectorAll('article')],q=document.querySelector('#q'),kind=document.querySelector('#kind');function filter(){let n=0;for(const c of cards){c.hidden=!(c.dataset.name.includes(q.value.toLowerCase())&&(kind.value==='all'||kind.value===c.dataset.kind));if(!c.hidden)n++}document.querySelector('#count').textContent=n+' combinations'}q.oninput=filter;kind.onchange=filter;document.querySelector('#dark').onchange=e=>document.body.classList.toggle('dark',e.target.checked);document.querySelector('#native').onchange=e=>document.body.classList.toggle('native',e.target.checked);filter()</script></html>'''
(ROOT/'index.html').write_text(page)
print(json.dumps({k:v for k,v in summary.items() if k!='remaining'},indent=2))
