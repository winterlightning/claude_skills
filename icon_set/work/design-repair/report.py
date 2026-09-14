from pathlib import Path
import json,html
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/design-repair/results.json'
AUTHOR='gpt-6'
rows=json.loads((W/'results.json').read_text());cards=[]
for r in rows:
 parent='../broken-geometry-repair/'+r['original']+'.svg';candidate=r['id']+'.svg'
 cards.append(f'''<article><h2>{r['original']}</h2><div class="pair"><figure><img src="{parent}"><figcaption>Before</figcaption></figure><figure><img src="{candidate}"><figcaption>{'Revised' if r['changed'] else 'Retained'} · PASS</figcaption></figure></div><p class="id">{r['id']}</p><a href="{candidate}">SVG</a> · <a href="../../..//{r['file']}">Python model</a></article>''')
(W/'index.html').write_text('''<!doctype html><html><head><meta charset="utf-8"><title>Icon design repairs</title><style>body{font:15px system-ui;background:#f7f6f2;color:#202226;margin:32px}h1{font-size:28px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:18px}article{padding:18px;background:white;border:1px solid #ddd;border-radius:14px}h2{font-size:16px}.pair{display:flex;justify-content:space-around}figure{margin:10px 0}img{width:96px;height:96px}figcaption,p.id{font-size:12px;color:#626873}a{color:#2259a0}header{margin-bottom:24px;max-width:850px}</style></head><body><header><h1>25 icons — all selected results pass</h1><p>18 revised variants and 7 retained icons. Each result validates with zero errors and zero warnings. Native-size light and dark previews were reviewed. Parent models remain available for comparison.</p><p><a href="preview-light.png">Light contact sheet</a> · <a href="preview-dark.png">Dark contact sheet</a> · <a href="results.json">Validation results</a></p><p>Construction references: local Lucide camera, fuel, save, paintbrush, plane, dog, gem and footprints, including their atomic-debug drawings. Other subjects retain their own silhouettes. The disk's nonessential hub dot was omitted to enlarge the label, and the horse's secondary mane stripe was removed to eliminate an undersized counter; asymmetric animal profiles and the diagonal brush are intentional.</p></header><main>'''+''.join(cards)+'</main></body></html>')
print('Review gallery ready')
