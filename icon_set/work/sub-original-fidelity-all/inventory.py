"""Inventory every canonical sub and its independently selected usage variants."""
import ast,hashlib,json,re,sys,html
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));W=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/data/canonical-sub32.json'
AUTHOR='gpt-6'
load=lambda p:json.loads((ROOT/p).read_text())
canonical=load('icon_set/data/canonical-sub32.json');roles=load('icon_set/model/catalog/sub-usage-categories.json')['icons'];history=load('icon_set/data/sub-reference-fidelity.json');sources=defaultdict(list)
for base in ('pictographic-primitives','pictographic-combinations'):
 for p in (ROOT/base).rglob('*.svg'):
  ids=re.findall(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',p.name)
  for uid in ids:sources[uid].append(p)
rows={}
for key,v in canonical.items():rows[v['python_source']]=dict(icon=v['icon'],family=v['family'],python_source=v['python_source'],svg=v['svg'],roles=['canonical'],source_id=None,geometry_status=v.get('model_validation','unknown'))
for entry in roles:
 for role,v in entry['versions'].items():
  path=v['python_source'];row=rows.setdefault(path,dict(icon=v['icon_id'],family=v.get('family',role),python_source=path,svg=v['svg'],roles=[],geometry_status=v.get('model_validation','unknown')))
  if role not in row['roles']:row['roles'].append(role)
  row['source_id']=entry.get('source_icon_id')
for row in rows.values():
 p=ROOT/row['python_source'];row['model_sha256']=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None;meta={}
 if p.exists():
  for n in ast.parse(p.read_text()).body:
   if isinstance(n,ast.Assign):
    for t in n.targets:
     if isinstance(t,ast.Name) and t.id in ('SOURCE_PATH','SOURCE_ICON_ID','SOURCE_REFERENCES'):
      try:meta[t.id]=ast.literal_eval(n.value)
      except (ValueError,TypeError):pass
 row['source_id']=meta.get('SOURCE_ICON_ID') or row.get('source_id');candidates=[]
 for value in [meta.get('SOURCE_PATH')]+[v[1] for v in meta.get('SOURCE_REFERENCES',()) if len(v)>1]:
  if not value:continue
  q=Path(value);q=q if q.is_absolute() else ROOT/q
  if q.exists() and q.suffix=='.svg' and any(x in q.parts for x in ('pictographic-primitives','pictographic-combinations')):candidates.append(q)
 candidates+=sources.get(row['source_id'],[]);candidates=list(dict.fromkeys(candidates));row['source_candidates']=[str(q.relative_to(ROOT)) for q in candidates];row['source_path']=row['source_candidates'][0] if candidates else None
 row['source_sha256']=hashlib.sha256(candidates[0].read_bytes()).hexdigest() if candidates else None
 row['fidelity_status']='pending' if candidates else 'source-missing';row['finding']='Not yet visually compared against the complete original.' if candidates else 'No original SVG resolved; geometry checks do not establish source fidelity.'
 old=history.get(row['icon'],{})
 if old.get('model_sha256')==row['model_sha256'] and old.get('status')=='superseded':row.update(fidelity_status='known-difference',finding=old['finding'])
 if old.get('model_sha256')==row['model_sha256'] and old.get('source_sha256')==row['source_sha256'] and old.get('status')=='redrawn':
  row.update(fidelity_status='reviewed-restored',finding=old['finding'],review_url='../'+old.get('review_url','sub-fidelity-repair-50/index.html#'+row['icon']))
 row['source_url']=('../../../'+row['source_path']) if row['source_path'] else None;row['current_url']='../../../'+row['svg'] if (ROOT/row['svg']).exists() else None
 row['review_key']=row['family']+'/'+row['icon']
ordered=sorted(rows.values(),key=lambda r:('side' not in r['roles'],r['fidelity_status']!='known-difference',r['icon']))
summary=dict(canonical_profiles=len(canonical),usage_origins=len(roles),distinct_current_models=len(ordered),side_versions=sum('side' in r['roles'] for r in ordered),symbol_versions=sum('symbol' in r['roles'] for r in ordered),fidelity_statuses=dict(Counter(r['fidelity_status'] for r in ordered)),policy='Preserve complete source composition, direction, count, text and proportions. No added or omitted parts. Use larger proportionate canvases when required; retain 4px strokes. Geometry pass is separate from visual source fidelity.')
(W/'inventory.json').write_text(json.dumps(ordered,indent=2));(W/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
# Inline JSON works in file:// galleries without fetch permissions.
data=json.dumps(ordered).replace('</','<\\/');stats=html.escape(f"{len(canonical):,} base profiles · {len(ordered):,} current models across roles · {summary['side_versions']} side versions")
page='''<!doctype html><html><meta charset="utf-8"><title>All sub icons · original fidelity</title><style>body{font:14px system-ui;background:#f4f6f5;color:#26382f;margin:24px}header{position:sticky;top:0;background:#f4f6f5;padding:12px 0;z-index:2}h1{font-size:24px}input,select,button{font:inherit;padding:9px;margin-right:8px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(370px,1fr));gap:16px}article{background:white;padding:16px;border-radius:12px}h2{font-size:14px;overflow-wrap:anywhere}.pair{display:flex;gap:16px}figure{margin:8px 0;flex:1;text-align:center}img{width:140px;height:140px;object-fit:contain}figcaption{color:#66786c;margin:8px 0}.status{color:#8b5b14}small{display:block;color:#69756b;line-height:1.5}</style><header><h1>All sub icons · preserve the complete original</h1><p>STATS</p><p><a href="../sub-fidelity-repair-50/index.html">First 50 restored — compare originals and results</a></p><p>No added or missing parts. Larger canvases are allowed. Geometry-passing icons are not automatically source-approved.</p><input id="q" placeholder="Find an icon"><select id="role"><option value="">All roles</option><option value="side" selected>Side first</option><option value="symbol">Container symbols</option></select><select id="status"><option value="">All fidelity states</option><option value="known-difference">Known differences</option><option value="pending">Pending source comparison</option><option value="reviewed-restored">Reviewed and restored</option><option value="source-missing">Missing source</option></select><button id="prev">Previous 50</button><button id="next">Next 50</button><p id="count"></p></header><main></main><script>const rows=DATA;let offset=0;const $=x=>document.getElementById(x);function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}function show(){const matches=rows.filter(r=>(!$('role').value||r.roles.includes($('role').value))&&(!$('status').value||r.fidelity_status===$('status').value)&&r.icon.includes($('q').value.toLowerCase()));offset=Math.min(offset,Math.max(0,Math.floor((matches.length-1)/50)*50));$('count').textContent=`${matches.length} models · showing ${matches.length?offset+1:0}–${Math.min(offset+50,matches.length)} · source comparison pending unless explicitly reviewed`;document.querySelector('main').innerHTML=matches.slice(offset,offset+50).map(r=>`<article><h2>${esc(r.icon)}</h2><small>${esc(r.roles.join(' · '))} · geometry: ${esc(r.geometry_status)}</small><p class="status">${esc(r.fidelity_status)}</p><div class="pair"><figure>${r.source_url?`<img loading="lazy" src="${esc(r.source_url)}">`:'Source unavailable'}<figcaption>Complete original</figcaption></figure><figure>${r.current_url?`<img loading="lazy" src="${esc(r.current_url)}">`:'Preview unavailable'}<figcaption>Current drawing</figcaption></figure></div><p>${esc(r.finding)}</p><small>${esc(r.source_id)}</small></article>`).join('');}for(const id of ['q','role','status'])$(id).oninput=()=>{offset=0;show();};$('prev').onclick=()=>{offset=Math.max(0,offset-50);show();};$('next').onclick=()=>{offset+=50;show();};show();</script></html>'''.replace('STATS',stats).replace('DATA',data)
(W/'index.html').write_text(page)
