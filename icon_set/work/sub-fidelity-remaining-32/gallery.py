"""Show remaining recorded source mismatches without changing artwork."""
import html,json,shutil,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
W=Path(__file__).resolve().parent
rows=[r for r in json.loads((ROOT/'icon_set/work/sub-original-fidelity-all/inventory.json').read_text()) if r['fidelity_status']=='known-difference']
assets=W/'review-assets';assets.mkdir(exist_ok=True)
assessments={r['icon']:r for r in json.loads((W/'size-review.json').read_text())}
cards=[]
for i,r in enumerate(rows,1):
    original=ROOT/r['source_path']; current=ROOT/r['svg']
    for label,path in [('original',original),('current',current)]:
        ET.parse(path)
        shutil.copy2(path,assets/f'{i}-{label}.svg')
    figs=''.join(f'<figure><figcaption>{label}</figcaption><img src="review-assets/{i}-{key}.svg" loading="lazy" alt="{html.escape(r["icon"])} — {label}"></figure>' for key,label in [('original','Original artwork'),('current','Current sub icon')])
    a=assessments[r['icon']]
    finding=a['note']
    trial='Try repair at 32×32 first' if a['size_trial']=='try-32' else 'Test crowded details at 32×32 before choosing size'
    cards.append(f'<article><h2>{i}. {html.escape(r["icon"])}</h2><p class="trial">{trial}</p><div class="previews">{figs}</div><p>{html.escape(finding)}</p><small>Geometry: {html.escape(r["geometry_status"])} · Original fidelity: needs repair/review</small></article>')
style='body{font:14px system-ui;background:#f4f6f5;color:#26372e;margin:24px}header{background:#fff;padding:18px;border-radius:12px;position:sticky;top:0;z-index:1;border-bottom:1px solid #ddd}h1{font-size:23px;margin:0 0 8px}h2{font-size:16px;overflow-wrap:anywhere}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:16px;margin-top:16px}article{background:white;padding:20px;border-radius:12px}article[hidden]{display:none}.previews{display:flex;gap:20px;justify-content:space-around}figure{margin:8px 0;text-align:center}img{width:170px;height:170px;object-fit:contain}figcaption,small{color:#66766c}figcaption{margin-bottom:12px}input{font:inherit;padding:8px;width:240px;max-width:80%}p{line-height:1.5}@media(max-width:480px){main{grid-template-columns:1fr}img{width:120px;height:120px}body{margin:12px}}'
(W/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Remaining 32 sub icon mismatches</title><style>'+style+'</style></head><body><header><h1>32 remaining sub icon mismatches</h1><p>Original on the left · current sub icon on the right. All 32 pairs have now been visually checked. Each card explains what must be restored and what to test at 32×32. Size recommendations are provisional until the complete redraw passes spacing checks; no automatic enlargement. Artwork is unchanged in this review.</p><input type="search" placeholder="Find an icon" aria-label="Find an icon" oninput="let n=0;document.querySelectorAll(\'article\').forEach(a=>{a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase());if(!a.hidden)n++});document.getElementById(\'count\').textContent=n+\' / 32 shown\'"><span id="count">32 / 32 shown</span></header><main>'+''.join(cards)+'</main></body></html>')
(W/'inventory.json').write_text(json.dumps(rows,indent=2))
assert len(rows)==32
assert len(list(assets.glob('*.svg')))==64
print(f'Created {W / "index.html"}: 32 cards, 64 verified SVG assets.')
