from pathlib import Path
import json,re,html,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-cars-refine/batch.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;rows=json.loads((w/'batch.json').read_text());old=ROOT/'icon_set/work/solo-ai-next100';base=(old/'review.html').read_text();current=base
for r in rows:
 for match in re.finditer(r'<article\b[^>]*>.*?</article>',current,re.S):
  card=match.group()
  if f'<h2>{r["parent"]}</h2>' not in card:continue
  replacement=re.sub(r'(<figure>.*?</figure><figure>).*?(<figcaption>)',lambda m:m[1]+create(r['icon_id']).to_svg()+m[2],card,count=1,flags=re.S)
  replacement=replacement.replace('<figcaption>Revised</figcaption>','<figcaption>Latest revision</figcaption>')
  replacement=re.sub(r'<details>.*?</details>',f'<details><summary>Construction notes</summary><p>{html.escape(r["plan"])}</p><p>HRECT_L · Valid, no warnings</p></details><a href="solo-ai-cars-refine.html">Compare car revisions ↗</a>',replacement,flags=re.S)
  current=current.replace(card,replacement,1);break
current=current.replace('<div class="toolbar">','<p><a href="solo-ai-cars-refine.html">Compare the 11 corrected cars: original, previous and latest ↗</a></p><div class="toolbar">',1)
(old/'review-current.html').write_text(current)
css=re.search(r'<style>(.*?)</style>',base,re.S)[1].replace('minmax(240px,1fr)','minmax(400px,1fr)').replace('grid-template-columns:1fr 1fr;','grid-template-columns:1fr 1fr 1fr;')
cards=[]
for r in rows:
 figs=''.join('<figure>'+create(n).to_svg()+'<figcaption>'+label+'</figcaption></figure>' for n,label in [(r['parent'],'Original'),(r['previous'],'Previous pass'),(r['icon_id'],'Latest revision')])
 cards.append(f'<article data-name="{r["parent"]}"><header><h2>{r["parent"]}</h2></header><div class="pair">{figs}</div><p>{r["label"]}</p><details><summary>What changed</summary><p>{html.escape(r["plan"])}</p></details></article>')
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Solo icons · Car refinements</title><style>'+css+'</style><body><main><div class="eyebrow">PICTOGRAPHIC / CAR REFINEMENTS</div><h1>Fuller bodies. Proper wheels.</h1><p class="intro">Eleven cars corrected: larger round wheels, fuller bodywork and roofs closer to the originals. All previous versions are preserved.</p><p><a href="solo-ai-next100.html">Back to all 100 icons ↗</a></p><div class="toolbar"><input id="search" type="search" aria-label="Find a car" placeholder="Find a car…"><button id="theme">Dark theme</button><button id="size">Enlarge to 96 px</button><span id="caption">Native size · 48 px</span></div><section class="grid">'+''.join(cards)+'''</section></main><script>
document.querySelector('#theme').onclick=function(){document.body.classList.toggle('dark');this.textContent=document.body.classList.contains('dark')?'Light theme':'Dark theme'};
document.querySelector('#size').onclick=function(){let large=document.body.classList.toggle('large');this.textContent=large?'Return to 48 px':'Enlarge to 96 px';document.querySelector('#caption').textContent=large?'Enlarged · 96 px':'Native size · 48 px'};
document.querySelector('#search').oninput=function(){document.querySelectorAll('article').forEach(a=>a.hidden=!a.dataset.name.includes(this.value.toLowerCase()))};
</script></body></html>'''
(w/'review.html').write_text(page)
(ROOT/'icon_set/dist/gallery/solo-ai-next100.html').write_text(current)
(ROOT/'icon_set/dist/gallery/solo-ai-cars-refine.html').write_text(page)
print('Published 11 car refinements and updated all-100 review.')
