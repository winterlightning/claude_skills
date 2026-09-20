"""Read-only report of current, geometry-passing oversized side sub icons."""
import json,sys,hashlib,html,csv,shutil,collections
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.icons.sub._text_base import canvas_dimensions
from icon_set.scripts.workspace import development_dist
raw=json.loads((ROOT/'icon_set/work/side-repair-priority/inventory.json').read_text());unique={}
for r in raw:
 e=unique.setdefault(r['icon'],dict(r,pair_ids=[]));e['pair_ids']=sorted(set(e['pair_ids'])|set(r.get('pair_ids',[])))
classification=json.loads((W/'classification.json').read_text())
assets=W/'assets';assets.mkdir(exist_ok=True);rows=[]
for uid,r in unique.items():
 if r['status']!='pass':continue
 m=create(uid);width,height=canvas_dimensions(m)
 if width<=32 and height<=32:continue
 svg=m.to_svg();sha=hashlib.sha256(svg.encode()).hexdigest()
 assert sha==r['verified_svg_sha256'],uid
 (assets/(uid+'.svg')).write_text(svg)
 module=sys.modules[type(m).__module__];source=getattr(module,'SOURCE_PATH',None)
 p=Path(source) if source else None
 if p and not p.is_absolute():p=ROOT/p
 source_asset=None
 if p and p.is_file() and p.suffix=='.svg':
  source_asset=uid+'-original.svg';shutil.copy2(p,assets/source_asset)
 rows.append(dict(kind=classification[uid]['kind'],icon=uid,width=width,height=height,status='pass',pair_count=len(r['pair_ids']),pair_ids=r['pair_ids'],python_source=r['python_source'],source_path=source,source_asset=source_asset,svg_sha256=sha,excess=max(width,height)-32))
rows.sort(key=lambda r:(-max(r['width'],r['height']),-r['width']*r['height'],r['icon']))
counts=collections.Counter((r['width'],r['height']) for r in rows)
summary=dict(scope='Unique currently selected side sub icons with geometry pass and either canvas dimension above 32px',total=len(rows),both_axes_over_32=sum(r['width']>32 and r['height']>32 for r in rows),one_axis_over_32=sum((r['width']>32)!=(r['height']>32) for r in rows),sizes=[dict(width=w,height=h,count=n) for (w,h),n in counts.most_common()],largest_width=max(r['width'] for r in rows),largest_height=max(r['height'] for r in rows),excluded_compact_exceptions=3)
summary['icons']=sum(r['kind']=='icon' for r in rows)
summary['pure_text']=sum(r['kind']=='text' for r in rows)
(W/'inventory.json').write_text(json.dumps(rows,indent=2));(W/'summary.json').write_text(json.dumps(summary,indent=2))
with (W/'oversized-sub-icons.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['kind','icon','width','height','pair_count','status','python_source','source_path']);writer.writeheader();writer.writerows({k:r[k] for k in writer.fieldnames} for r in rows)
cards=[]
for i,r in enumerate(rows,1):
 uid=r['icon'];w,h=r['width'],r['height'];esc=html.escape
 original=(f'<figure><figcaption>Original</figcaption><img loading="lazy" src="assets/{uid}-original.svg" alt="Original for {esc(uid)}"></figure>' if r['source_asset'] else '')
 cards.append(f'<article data-kind="{r["kind"]}" data-name="{esc(uid)}" data-width="{w}" data-height="{h}"><h2>{i}. {esc(uid)}</h2><div class="dimensions">{w} × {h}px · {"Pure text" if r['kind']=='text' else "Icon"} <span>· {r["pair_count"]} linked pairs</span></div><div class="comparison">{original}<figure><figcaption>Current artwork</figcaption><img loading="lazy" src="assets/{uid}.svg" alt="{esc(uid)}"></figure></div><details><summary>Show actual size · scroll for wide icons</summary><div class="actual"><img loading="lazy" src="assets/{uid}.svg" width="{w}" height="{h}" alt="Actual size"></div></details><p><a href="assets/{uid}.svg" download>SVG</a></p></article>')
style='body{font:14px system-ui;color:#23342d;background:#f3f5f4;margin:20px}header{background:#fff;padding:18px;border-radius:12px}h1{font-size:24px;margin:0 0 8px}h2{font-size:15px;overflow-wrap:anywhere}.stats{display:flex;gap:24px;flex-wrap:wrap;margin:14px 0}.stats b{font-size:23px;display:block}.stats span{color:#647269}.tabs{display:flex;gap:8px;margin:16px 0}.tabs button{font:inherit;padding:10px 18px;border:1px solid #ccd4ce;border-radius:7px;background:white;cursor:pointer}.tabs button[aria-pressed=true]{background:#236946;color:white;border-color:#236946}.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center}input,select{font:inherit;padding:9px;border:1px solid #ccd4ce;border-radius:6px}input{min-width:220px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:14px;margin-top:16px}article{background:white;border-radius:10px;padding:16px;min-width:0}article[hidden]{display:none}.dimensions{color:#a4591a;font-weight:650}.dimensions span{font-weight:400;color:#68766d}.comparison{display:flex;gap:14px;justify-content:space-around}figure{margin:16px 0;min-width:0;flex:1;text-align:center}figure img{width:100%;height:155px;object-fit:contain}figcaption{font-size:12px;color:#65756b;margin-bottom:8px}.actual{overflow:auto;margin-top:12px;padding:12px;background:#f2f5f3}.actual img{max-width:none;display:block}summary{cursor:pointer;color:#5e7064}a{color:#236946}p{line-height:1.5}#shown{color:#65756b}'
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Oversized sub icons</title><style>'+style+'</style></head><body><header><h1>Oversized sub icons</h1><p>Current side sub icons with width or height above 32px. Largest first. Artwork is unchanged.</p><div class="stats"><div><b>'+str(len(rows))+'</b><span>oversized icons</span></div><div><b>'+str(summary['both_axes_over_32'])+'</b><span>both dimensions over 32</span></div><div><b>'+str(summary['one_axis_over_32'])+'</b><span>one dimension over 32</span></div></div><p>These drawings pass their recorded geometry checks, but need placement checks before use in a fixed-size combination. This is the side-icon collection, not a full-library size audit. The three compact exceptions are excluded.</p><p>Pure text includes bare letters, numbers, currency signs and operators. Text inside a circle, bubble, card or another drawing is grouped as an icon. Classification follows the current artwork.</p><div class="tabs" aria-label="Artwork type"><button type="button" data-kind="icon" aria-pressed="true">Icons ('+str(summary['icons'])+')</button><button type="button" data-kind="text" aria-pressed="false">Pure text ('+str(summary['pure_text'])+')</button><button type="button" data-kind="all" aria-pressed="false">All ('+str(len(rows))+')</button></div><div class="controls"><input id="search" type="search" placeholder="Find an icon" aria-label="Find an icon"><select id="filter" aria-label="Filter size"><option value="all">All oversized</option><option value="both">Both dimensions above 32</option><option value="one">Only one dimension above 32</option><option value="large">Any dimension above 64</option></select><span id="shown"></span><a href="oversized-sub-icons.csv" download>Download CSV</a></div></header><main>'+''.join(cards)+'''</main><script>const cards=[...document.querySelectorAll('article')],q=document.getElementById('search'),f=document.getElementById('filter');let kind='icon';function update(){let n=0;cards.forEach(c=>{const w=+c.dataset.width,h=+c.dataset.height,v=f.value,ok=v==='all'||v==='both'&&w>32&&h>32||v==='one'&&((w>32)!==(h>32))||v==='large'&&Math.max(w,h)>64;c.hidden=!((kind==='all'||c.dataset.kind===kind)&&ok&&c.dataset.name.includes(q.value.toLowerCase()));if(!c.hidden)n++;});document.getElementById('shown').textContent=n+' / '+cards.length+' shown';}document.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{kind=b.dataset.kind;document.querySelectorAll('.tabs button').forEach(t=>t.setAttribute('aria-pressed',String(t===b)));update();});q.oninput=f.onchange=update;update();</script></body></html>'''
(W/'index.html').write_text(page)
dest=development_dist(ROOT)/'gallery'/W.name;dest.mkdir(parents=True,exist_ok=True)
for filename in ['index.html','summary.json','inventory.json','oversized-sub-icons.csv']:shutil.copy2(W/filename,dest/filename)
shutil.copytree(assets,dest/'assets',dirs_exist_ok=True)
assert all(r['width']>32 or r['height']>32 for r in rows)
print(json.dumps(summary,indent=2));print('REPORT',W/'index.html')
