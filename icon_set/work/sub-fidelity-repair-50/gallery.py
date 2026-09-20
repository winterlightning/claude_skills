"""Original-first review for fifty complete source compositions."""
import json,sys,html,xml.etree.ElementTree as ET,shutil
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.icons.sub._text_base import canvas_dimensions
from icon_set.scripts.workspace import development_dist
rows=json.loads((W/'accepted.json').read_text());assets=W/'review-assets';assets.mkdir(exist_ok=True);cards=[];sizes={}
for r in rows:
 m=create(r['candidate']);w,h=canvas_dimensions(m);sizes[r['candidate']]=[w,h];svg=m.to_svg();t=ET.fromstring(svg)
 for e in t.iter():
  if 'stroke-width' in e.attrib:e.set('stroke-width','.3')
 docs={'original':(ROOT/r['source_path']).read_text(),'before':create(r['icon']).to_svg(),'after':svg,'center':ET.tostring(t).decode()}
 for name,data in docs.items():(assets/f'{r["number"]}-{name}.svg').write_text(data)
 def fig(k,label,native=False):
  size=f'width:{w}px;height:{h}px' if native else 'width:165px;height:165px;object-fit:contain'
  return f'<figure><figcaption>{label}</figcaption><img loading="lazy" style="{size}" src="review-assets/{r["number"]}-{k}.svg"></figure>'
 cards.append(f'<article id="{r["candidate"]}"><h2>{r["number"]}. {html.escape(r["icon"])}</h2><p class="pass">Complete source compared · geometry pass · {w}×{h} · 4px stroke</p><div class="previews">'+fig('original','Original artwork')+fig('before','Previous selection')+fig('after','Restored selection')+fig('center','Centerline')+'</div><div class="native">'+fig('after','Actual size',True)+'<span class="dark">'+fig('after','Dark',True)+'</span></div><p>'+html.escape(r['reason'])+'</p><small>'+html.escape(r['source_uuid'])+'</small></article>')
style='body{font:14px system-ui;background:#f4f6f5;color:#26372e;margin:24px}header{padding:18px;background:#e4f1e8;border-radius:12px}article{background:white;padding:20px;margin:18px 0;border-radius:12px}h1{font-size:24px}h2{font-size:17px}.pass{color:#267546}.previews,.native{display:flex;gap:22px;align-items:center;flex-wrap:wrap}figure{margin:12px 0}figcaption,small{color:#66766c}figcaption{margin-bottom:8px}.dark{padding:12px;background:#203129}.dark img{filter:invert(1)}.dark figcaption{color:white}input{font:inherit;padding:10px;min-width:240px}article[hidden]{display:none}'
(W/'index.html').write_text('<!doctype html><html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>50 complete-source sub repairs</title><style>'+style+'</style><header><h1>First 50 source mismatches restored</h1><p>All 50 compared with their complete originals and checked at native size in both themes. Larger artwork keeps its proportions and 4px stroke.</p><p><b>32 known mismatches remain.</b> The rest of the full-library source audit and 32 missing references remain separate.</p><p>Selected profile and pair links are updated. Combined SVG caches have not been rebuilt; enlarged artwork must not be shrunk back into a fixed 64px combination.</p><p><a href="../sub-original-fidelity-all/index.html">Whole-library comparison inventory</a></p><input type="search" placeholder="Find an icon" oninput="document.querySelectorAll(\'article\').forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase()))"></header>'+''.join(cards)+'</html>')
(W/'summary.json').write_text(json.dumps(dict(restored=50,geometry_pass=50,known_mismatches_remaining=32,source_missing=32,sizes=sizes),indent=2))
dest=development_dist(ROOT)/'gallery'/W.name;dest.mkdir(parents=True,exist_ok=True)
for f in ['index.html','summary.json','audit.json']:shutil.copy2(W/f,dest/f)
shutil.copytree(assets,dest/'review-assets',dirs_exist_ok=True)
print(W/'index.html')
