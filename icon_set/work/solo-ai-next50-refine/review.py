"""Publish the feedback revision comparison without replacing earlier models."""
from pathlib import Path
import sys,json,html,re
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
WORK=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-next50-refine/batch.json'
AUTHOR='gpt-6'
rows=json.loads((WORK/'batch.json').read_text())
oldwork=ROOT/'icon_set/work/solo-ai-next50'
# Keep the original page layout; every inline SVG is an untouched model export.
base=(oldwork/'review.html').read_text()
start=base.index('<section class="grid">');end=base.index('</section>',start)
cards=[]
for r in rows:
 figs=''.join('<figure>'+create(i).to_svg()+'<figcaption>'+label+'</figcaption></figure>' for i,label in [(r['parent'],'Original'),(r['previous'],'Previous pass'),(r['icon_id'],'New revision')])
 cards.append(f'<article><header><h2>{html.escape(r["parent"])}</h2></header><p class="variant-label">{html.escape(r["label"])}</p><div class="pair">{figs}</div><details><summary>What changed</summary><p>{html.escape(r["plan"])}</p><p>{r["keyshape"]} · Valid, no warnings · '+('Lucide '+r['reference'] if r['reference'] else 'Original bread slice; no useful exact Lucide match')+f'</p></details><a href="index.html?tab=icons&family=solo&view=versions&q={r["parent"]}">All versions in the library ↗</a></article>')
page=base[:start]+'<section class="grid">'+''.join(cards)+base[end:]
page=page.replace('Solo icons · Next 50 AI reviews','Solo icons · Proportion refinements').replace('The next 50 solo icons.','Three proportions, restored.')
page=re.sub(r'<p class="intro">.*?</p>', '', page, flags=re.S)
page=page.replace('<div class="toolbar">','<p class="intro">Binoculars, bread and brain: original proportions restored with consistent strokes. Compare the original, previous pass and latest revision.</p><div class="toolbar">')
page=page.replace('index.html?tab=ai&family=solo&q=solo-ai-next50&page_size=96','index.html?tab=icons&family=solo&q=solo-ai-next50-refine&page_size=96&view=versions').replace('Open all 50 in the library ↗','Review these three in the library ↗')
page=page.replace('grid-template-columns:repeat(auto-fit,minmax(240px,1fr))','grid-template-columns:repeat(auto-fit,minmax(350px,1fr))').replace('grid-template-columns:1fr 1fr;','grid-template-columns:1fr 1fr 1fr;')
page=page.replace('</style>','.variant-label{color:var(--muted);font-size:12px;margin:8px 0}.pair figure:last-child figcaption{font-weight:700;color:var(--ink)}@media(max-width:450px){main{padding:20px 10px}.grid{grid-template-columns:1fr}body.large figure svg{width:80px;height:80px}}</style>')
page=page.replace('<div class="toolbar">','<p><a href="solo-ai-next50.html">Back to the complete 50-icon review ↗</a></p><div class="toolbar">')
(WORK/'review.html').write_text(page)
# Refresh the current 50-icon page with the latest version for these thirteen.
for r in rows:
 pattern=r'(<article>.*?<h2>'+re.escape(r['parent'])+r'</h2>.*?</article>)'
 # Isolate each article before replacement to avoid crossing earlier cards.
 for match in list(re.finditer(r'<article>.*?</article>',base,flags=re.S)):
  card=match.group()
  if f'<h2>{r["parent"]}</h2>' not in card:continue
  updated=re.sub(r'(<figure>.*?</figure><figure>).*?(<figcaption>)',lambda m:m.group(1)+create(r['icon_id']).to_svg()+m.group(2),card,count=1,flags=re.S)
  updated=updated.replace('<figcaption>Revised</figcaption>','<figcaption>New revision</figcaption>')
  updated=re.sub(r'<details>.*?</details>',f'<details><summary>Construction notes</summary><p>{html.escape(r["plan"])}</p><p>{r["keyshape"]} · valid · '+('Lucide '+r['reference'] if r['reference'] else 'Original bread slice; no useful exact Lucide match')+'</p></details>',updated,flags=re.S)
  base=base.replace(card,updated,1);break
base=base.replace('index.html?tab=ai&family=solo&q=solo-ai-next50&page_size=96','index.html?tab=icons&family=solo&q=solo-ai-next50&page_size=96&view=versions')
base=base.replace('<div class="toolbar">','<p><a href="solo-ai-next50-refine.html">See the 3 latest feedback revisions: previous pass versus new ↗</a></p><div class="toolbar">')
(oldwork/'review-current.html').write_text(base)
for name,content in [('solo-ai-next50-refine.html',page),('solo-ai-next50.html',base)]:
 (ROOT/'icon_set/dist/gallery'/name).write_text(content)
print('Published focused review and refreshed the original 50-icon page')
