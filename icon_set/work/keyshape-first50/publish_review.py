"""Render a self-contained before/after review from Python models and frozen originals."""
SOURCE_ICON_ID = None
SOURCE_PATH = 'selection.json'
AUTHOR = 'gpt-6'
import json,sys,html,re,hashlib,difflib
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.icons.solo._base import Solo48
from icon_set.validation.library_qa import inspect_icon
s=json.loads((W/'selection.json').read_text());rows=[];cards=[];patch=[]
# Build results are read, not modified. A fresh build must precede this report.
for n,item in enumerate(s,1):
 p=ROOT/item['file'];before=(W/'before-models'/p.name).read_text()
 ns={'__name__':'icon_set.model.icons.solo._frozen_review','__package__':'icon_set.model.icons.solo'}
 exec(compile(before,str(W/'before-models'/p.name),'exec'),ns)
 cls=next(v for v in ns.values() if isinstance(v,type) and issubclass(v,Solo48) and v is not Solo48)
 old=cls();new=create(item['id'])
 metrics=json.loads((ROOT/'icon_set/dist/qa/solo'/item['id']/'metrics.json').read_text())
 assert metrics['status']=='pass',(item['id'],metrics['status'])
 changed=old.keyshape.bounds_for(old.profile)!=new.keyshape.bounds_for(new.profile)
 row={'number':n,'id':item['id'],'python':item['file'],'before_keyshape':old.keyshape.name,'keyshape':new.keyshape.name,'status':metrics['status'],'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 rows.append(row)
 patch.extend(difflib.unified_diff(before.splitlines(True),p.read_text().splitlines(True),fromfile='before/'+p.name,tofile=item['file']))
 def preview(o,label):
  svg=o.to_svg();l,t,r,b=o.keyshape.bounds_for(o.profile)
  frame=f'<i class="envelope" style="left:{l/48*100}%;top:{t/48*100}%;width:{(r-l)/48*100}%;height:{(b-t)/48*100}%"></i>'
  return f'<div class="version"><div class="label">{label}</div><div class="large"><div class="drawing">{svg}{frame}</div></div><div class="native">{svg}</div><small>{o.keyshape.name}</small></div>'
 label='Envelope changed' if changed else 'Curve / boundary repair'
 cards.append(f'<article data-name="{item["id"]}"><div class="card-head"><span class="number">{n:02}</span><h2>{html.escape(item["id"])}</h2><span class="pass">Pass</span></div><div class="pair">{preview(old,"Before")}{preview(new,"After")}</div><footer>{label} · 48 px below, 144 px above</footer></article>')
(W/'model-changes.patch').write_text(''.join(patch));(W/'release-results.json').write_text(json.dumps(rows,indent=2))
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Keyshape repair · first 50</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f5f6;color:#17191d;font:14px system-ui,sans-serif;--panel:#fff;--line:#dfe3e6;--muted:#65717d}body.dark{background:#101215;color:#edf1f4;--panel:#1b1f24;--line:#343a43;--muted:#a0aab6}header{max-width:1450px;margin:auto;padding:40px 32px 24px}h1{font-size:32px;letter-spacing:-1px;margin:10px 0}header p{color:var(--muted);max-width:780px;line-height:1.6}.eyebrow{font-size:12px;letter-spacing:2px;color:var(--muted)}.tools{display:flex;gap:18px;align-items:center;flex-wrap:wrap;margin-top:24px}input[type=search]{border:1px solid var(--line);background:var(--panel);color:inherit;padding:12px 14px;border-radius:8px;min-width:260px}button{border:1px solid var(--line);background:var(--panel);color:inherit;padding:12px 16px;border-radius:8px;cursor:pointer}.summary{color:#218454;font-weight:650}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:18px;padding:0 32px 40px;max-width:1450px;margin:auto}article{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:20px}.card-head{display:flex;gap:10px;align-items:center;min-height:34px}.number{color:var(--muted);font-size:12px}h2{font-size:14px;font-weight:600;flex:1;margin:0;overflow-wrap:anywhere}.pass{font-size:11px;color:#218454;border:1px solid #21845477;border-radius:20px;padding:3px 7px}.pair{display:flex;padding:18px 0 12px}.version{width:50%;text-align:center}.version+.version{border-left:1px solid var(--line)}.label{color:var(--muted);font-size:12px;margin-bottom:12px}.large{width:144px;height:144px;margin:auto}.drawing{position:relative;width:100%;height:100%}svg{display:block;width:100%;height:100%;overflow:visible}.envelope{position:absolute;border:1px dashed #40978f;pointer-events:none;display:none}body.guides .envelope{display:block}.native{width:48px;height:48px;margin:18px auto 9px}small,footer{font-size:10px;color:var(--muted)}footer{border-top:1px solid var(--line);padding-top:12px}.notes{max-width:1386px;margin:0 auto 36px;padding:22px;background:var(--panel);border:1px solid var(--line);border-radius:12px;color:var(--muted);line-height:1.7}.notes strong{color:inherit}.hidden{display:none}@media(max-width:600px){header{padding:24px 18px}.grid{padding:0 12px 24px;grid-template-columns:1fr}.notes{margin:0 12px 24px}h1{font-size:26px}article{padding:16px}}
</style><header><div class="eyebrow">PICTOGRAPHIC / REVIEW SAMPLE</div><h1>Keyshape bounds · first 50</h1><p>Compare the first 50 icons from the 261-icon “Curve extreme off the grid” group, in the gallery’s default order. Repairs are saved directly in the Python models.</p><div class="summary">50 / 50 pass full icon build checks</div><div class="tools"><input id="search" type="search" placeholder="Find an icon…" aria-label="Find an icon"><label><input id="guides" type="checkbox"> Show keyshape envelopes</label><button id="theme">Switch to dark</button><span id="count">50 icons</span></div></header><main class="grid">'''+''.join(cards)+'''</main><aside class="notes"><strong>Review notes.</strong> Boundary nodes and curve radii were repaired together. The window, potty, bear face and eagle head now use SQUARE because it matches their natural proportions. The account profile and camel pose have a 4-unit head/body ink gap. The airplane’s far wing joins the silhouette without a redundant crossing seam; the vine retains all five leaves with open interiors. The other 211 icons from this group were outside this repair sample.<br><br><strong>Validation.</strong> All 50 pass the full build, including exact bounds, grid, spacing, round-trip, reproducibility, and hole/pinch checks. The repository-wide run reported 505 failures and 26 errors across 339 tests; these include other failing library icons and sandbox-blocked server tests. This sample’s focused release checks are recorded separately.</aside><script>
const search=document.querySelector('#search');search.oninput=()=>{let count=0;document.querySelectorAll('article').forEach(a=>{const show=a.dataset.name.includes(search.value.toLowerCase());a.classList.toggle('hidden',!show);if(show)count++});document.querySelector('#count').textContent=count+' icons'};document.querySelector('#guides').onchange=e=>document.body.classList.toggle('guides',e.target.checked);document.querySelector('#theme').onclick=e=>{document.body.classList.toggle('dark');e.target.textContent=document.body.classList.contains('dark')?'Switch to light':'Switch to dark'};
</script></html>'''
(W/'review.html').write_text(page)
(ROOT/'icon_set/dist/gallery/keyshape-first50.html').write_text(page)
print('Review ready: 50 passing icons')
