"""Display the changed artwork alongside complete originals and centerlines."""
import json,html,shutil,sys
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.scripts.workspace import development_dist
from icon_set.model.icons.registry import create
rows=json.loads((W/'accepted.json').read_text());cards=[];sizes={}
compact_overrides={r['number']:r for r in json.loads((W.parent/'sub-compact-feedback/candidates.json').read_text())}
from icon_set.model.icons.sub._text_base import canvas_dimensions
for r in rows:
 i=r['number'];r=dict(r)
 if i in compact_overrides:r['candidate']=compact_overrides[i]['compact']
 m=create(r['candidate']);w,h=canvas_dimensions(m);sizes[r['candidate']]=[w,h]
 status='4px frame / 2px inner · approved compact exception' if i in compact_overrides else '4px stroke · geometry pass'
 def fig(key,label,native=False):
  style=f'width:{w}px;height:{h}px' if native else 'width:180px;height:180px;object-fit:contain'
  return f'<figure><figcaption>{label}</figcaption><img style="{style}" src="review-assets/{i}-{key}.svg" loading="lazy" alt="{html.escape(label)}"></figure>'
 cards.append(f'<article id="{r["candidate"]}"><h2>{i}. {html.escape(r["icon"])}</h2><p class="pass">Artwork replaced · {w}×{h} · {status}</p><div class="previews">'+fig('original','Complete original')+fig('after','Repaired artwork')+fig('center','Repaired centerline')+'</div><div class="native">'+fig('after','Actual size',True)+'<div class="dark">'+fig('after','Actual size · dark',True)+'</div></div><p>'+html.escape(r['reason'])+'</p><details><summary>Earlier drawing</summary>'+fig('before','Superseded drawing')+'</details></article>')
 # Preserve frozen prior asset for honest before/after comparisons.
 shutil.copy2(ROOT/r['svg'],W/'review-assets'/f'{i}-before.svg')
style='body{font:14px system-ui;background:#f4f6f5;color:#26372e;margin:20px}header{padding:16px;background:#e4f1e8;border-radius:12px}article{background:white;padding:18px;margin:16px 0;border-radius:12px}h1{font-size:24px}h2{font-size:17px}.pass{color:#267546}.previews,.native{display:flex;gap:24px;align-items:center;flex-wrap:wrap}figure{margin:10px 0}figcaption{color:#66766c;margin-bottom:8px}.dark{padding:12px;background:#203129}.dark img{filter:invert(1)}.dark figcaption{color:white}input{font:inherit;padding:9px;min-width:240px}article[hidden]{display:none}details{color:#657169}'
compact=sum(v==[32,32] for v in sizes.values())
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>32 repaired sub icons</title><style>'+style+'</style></head><body><header><h1>32 sub icons — artwork repaired</h1><p>Complete original · repaired artwork · centerline. 29 pass standard geometry checks; 3 use your approved compact exceptions. '+str(compact)+' remain 32×32. HI, Bitcoin and O₂ now use 32×32 with 4px frames and smaller 2px inner characters. Other drawings retain their current dimensions.</p><p>Selected sub profiles are updated. No existing combination pairs referenced these 32 selections; combined SVG caches are unchanged. These are source-based redraws; human review remains open.</p><input type="search" aria-label="Find an icon" placeholder="Find an icon" oninput="document.querySelectorAll(\'article\').forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase()))"></header>'+''.join(cards)+'</body></html>'
(W/'index.html').write_text(page)
(W/'summary.json').write_text(json.dumps(dict(repaired=32,geometry_pass=29,approved_compact_exceptions=3,compact_32=compact,sizes=sizes,combined_svg_cache_rebuilt=False),indent=2))
# Update the user's existing page, retaining its original inventory and before assets.
old=W.parent/'sub-fidelity-remaining-32'
(old/'index-before-repairs.html').write_text((old/'index.html').read_text()) if not (old/'index-before-repairs.html').exists() else None
(old/'index.html').write_text(page)
shutil.copytree(W/'review-assets',old/'review-assets',dirs_exist_ok=True)
for name in [W.name,old.name]:
 dest=development_dist(ROOT)/'gallery'/name;dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(page);shutil.copytree(W/'review-assets',dest/'review-assets',dirs_exist_ok=True)
print('Updated repaired gallery and the existing review page;',compact,'icons at 32x32.')
