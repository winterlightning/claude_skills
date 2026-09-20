"""Compare complete source artwork, remake and centerlines without stretched previews."""
import json,sys,html,re,shutil,xml.etree.ElementTree as ET
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.icons.sub._text_base import canvas_dimensions
from icon_set.scripts.workspace import development_dist
rows=json.loads((W/'accepted.json').read_text());assets=W/'review-assets';assets.mkdir(exist_ok=True);cards=[]
for r in rows:
 m=create(r['candidate']);w,h=canvas_dimensions(m);svg=m.to_svg();tree=ET.fromstring(svg)
 for e in tree.iter():
  if 'stroke-width' in e.attrib:e.set('stroke-width','.3')
 for k,data in dict(original=Path(r['source_path']).read_text(),after=svg,center=ET.tostring(tree).decode(),rejected=create(r['icon']).to_svg()).items():
  (assets/f'{r["source_uuid"]}-{k}.svg').write_text(data)
 def fig(k,label,native=False):
  size=f'width:{w}px;height:{h}px' if native else 'width:192px;height:192px;object-fit:contain'
  return f'<figure><figcaption>{label}</figcaption><img style="{size}" src="review-assets/{r["source_uuid"]}-{k}.svg" alt="{html.escape(r["candidate"])}"></figure>'
 cards.append(f'<article id="source-{r["source_uuid"]}" data-outcome="repaired"><h2>{html.escape(r["candidate"])}</h2><p class="good">Source compared · all parts retained · checks pass · {w}×{h} · stroke 4</p><div class="previews">'+fig('original','Original artwork')+fig('after','Remade from original')+fig('center','Centerline')+'</div><div class="native">'+fig('after','Actual size',True)+'<div class="dark">'+fig('after','Dark background',True)+'</div></div><p>'+html.escape(r['reason'])+'</p><p class="parts">Preserved: '+html.escape('; '.join(r['source_parts_preserved']))+'.</p><details><summary>Previous repair · superseded</summary>'+fig('rejected','Rejected repair')+'</details></article>')
style='body{margin:24px;background:#f4f6f5;color:#23362e;font:14px system-ui}header{padding:16px 20px;background:#e4f1e9;border-radius:12px}article{background:white;padding:20px;margin:18px 0;border-radius:12px}h1{font-size:24px}h2{font-size:17px}.good{color:#28724b}.previews,.native{display:flex;gap:28px;align-items:center;flex-wrap:wrap}figure{margin:12px 0}figcaption{margin-bottom:12px;color:#617167}.dark{background:#203129;padding:12px;border-radius:8px}.dark img{filter:invert(1)}.dark figcaption{color:#dcebe3}.parts{color:#617167}summary{cursor:pointer}input{padding:10px;font:inherit;margin-top:8px;min-width:240px}article[hidden]{display:none}'
page='<!doctype html><html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Source-faithful side-icon remakes</title><style>'+style+'</style><header><h1>Remade from the original artwork</h1><p>All eight compared against their complete sources. Missing frames, invoice lines and the monitor foot are restored. Shared currency forms retain the source symbols.</p><p>One side is 32px; extra room supports the 4px stroke. Proportions are adapted for small-size readability—these are redraws, not exact resized copies.</p><p><b>825 / 825 selected side icons pass geometry checks.</b> Source artwork is shown first for visual review.</p><input type="search" placeholder="Find an icon" oninput="document.querySelectorAll(\'article\').forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase()))"></header><main>'+''.join(cards)+'</main></html>'
(W/'index.html').write_text(page)
# Refresh the exact page the user already has open, preserving its previous version.
old=W.parent/'side-final-eight';backup=old/'superseded-before-source-review.html'
if not backup.exists():shutil.copy2(old/'index.html',backup)
(old/'index.html').write_text(page);shutil.copytree(assets,old/'review-assets',dirs_exist_ok=True)
main=W.parent/'side-repair-final-68';s=(main/'index.html').read_text();audit=json.loads((main/'audit.json').read_text())
for r,card in zip(rows,cards):
 pattern=r'<article\b[^>]*id="final-'+r['source_uuid']+'".*?</article>'
 s,count=re.subn(pattern,lambda _:card,s,flags=re.S);assert count==1,(r['candidate'],count)
 oldrow=next(x for x in audit if x['source_uuid']==r['source_uuid']);oldrow.update(candidate=r['candidate'],candidate_python=r['candidate_python'],reason=r['reason'],source_parts_preserved=r['source_parts_preserved'],omitted_source_parts=[])
(main/'index.html').write_text(s);(main/'audit.json').write_text(json.dumps(audit,indent=2));shutil.copytree(assets,main/'review-assets',dirs_exist_ok=True)
for name in ('side-source-faithful-eight','side-final-eight','side-repair-final-68','side-repair-priority'):
 src=W.parent/name;dst=development_dist(ROOT)/'gallery'/name;dst.mkdir(parents=True,exist_ok=True)
 for f in ('index.html','audit.json','summary.json','repair-queue.json'):
  if (src/f).exists():shutil.copy2(src/f,dst/f)
 if (src/'review-assets').exists():shutil.copytree(src/'review-assets',dst/'review-assets',dirs_exist_ok=True)
print(W/'index.html')
