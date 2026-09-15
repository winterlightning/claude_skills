from pathlib import Path
import sys,json,html,shutil
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/solo-ai-number-arrows/batch.json'
w=Path(__file__).parent;rows=json.loads((w/'batch.json').read_text());cards=[]
for r in rows:
 figures=''.join('<figure><div class="large">'+create(n).to_svg()+'</div><div class="native">'+create(n).to_svg()+'</div><figcaption>'+label+'</figcaption></figure>' for n,label in [(r['parent'],'Original'),(r['previous'],'Previous pass'),(r['icon_id'],'Latest revision')])
 note='The 1 and 9 now share the same height and stroke weight, with a clear rounded bowl on the 9.' if r['parent']=='arrange-number' else 'The open end and arrow tip now have 6 units of visible clearance. The required minimum is 4.'
 cards.append('<article><h2>'+html.escape(r['parent'])+'</h2><div class="figures">'+figures+'</div><p>'+note+'</p></article>')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Solo · Number and arrow refinements</title><style>
:root{font-family:system-ui,sans-serif;color:#17252c;background:#f4f5f6;--card:white;--line:#dde2e5;--muted:#647079}body{margin:0;padding:30px 20px}body.dark{background:#171c23;color:#f0f3f7;--card:#202732;--line:#364150;--muted:#b1bac7}header,main{max-width:1100px;margin:auto}h1{font-size:30px;letter-spacing:-.03em}h2{font-size:17px}p{color:var(--muted);font-size:14px;line-height:1.6}.eyebrow{font-size:11px;letter-spacing:.15em;font-weight:700;color:#35816d}a{color:inherit}button{padding:10px 14px;border:1px solid var(--line);background:var(--card);color:inherit;border-radius:8px;cursor:pointer;margin:10px 0 22px}article{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px;margin-bottom:20px}.figures{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}figure{margin:0;text-align:center;display:flex;flex-direction:column;align-items:center;gap:18px;padding:20px 0}.large svg{width:96px;height:96px;display:block}.native svg{width:48px;height:48px;display:block}figcaption{font-size:12px;color:var(--muted)}@media(max-width:480px){body{padding:20px 12px}article{padding:16px}.figures{gap:4px}.large svg{width:80px;height:80px}h1{font-size:25px}}
</style><header><div class="eyebrow">PICTOGRAPHIC / REFINEMENTS</div><h1>A clearer 9. More room around the arrows.</h1><p>Original, previous pass, and revised drawing. Each appears enlarged and at its native 48 px size.</p><p><a href="solo-ai-full-set.html">Back to the full set ↗</a></p><button id="theme">Dark background</button></header><main>CARDS</main><script>document.getElementById('theme').onclick=()=>{document.body.classList.toggle('dark');document.getElementById('theme').textContent=document.body.classList.contains('dark')?'Light background':'Dark background'}</script></html>'''.replace('CARDS',''.join(cards))
(w/'review-current.html').write_text(page)
for folder in (ROOT/'icon_set/work').glob('solo-ai-*'):
 src=folder/'review-current.html'
 if not src.exists():src=folder/'review.html'
 if src.exists():shutil.copyfile(src,ROOT/'icon_set/dist/gallery'/f'{folder.name}.html')
print('Published 3 refinements and restored earlier review pages')
