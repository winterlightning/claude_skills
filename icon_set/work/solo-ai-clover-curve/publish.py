from pathlib import Path
import sys,re,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-clover-curve/batch.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;row=json.loads((w/'batch.json').read_text())[0];latest=create(row['icon_id']).to_svg();previous=create(row['previous']).to_svg()
shapes=ROOT/'icon_set/work/solo-ai-shapes-refine';base=(shapes/'review.html').read_text()
card=next(m.group() for m in re.finditer(r'<article\b[^>]*>.*?</article>',base,re.S) if '<h2>casino-clover</h2>' in m.group())
newcard=card.replace(previous,latest).replace('Three heart-shaped leaves','Soft curved shamrock')
newcard=re.sub(r'<details>.*?</details>',f'<details><summary>What changed</summary><p>{row["plan"]}</p></details>',newcard,flags=re.S)
updated=base.replace(card,newcard)
(shapes/'review-current.html').write_text(updated);(ROOT/'icon_set/dist/gallery/solo-ai-shapes-refine.html').write_text(updated)
focus=updated[:updated.index('<section class="grid">')]+'<section class="grid">'+newcard.replace(create('casino-clover-v2').to_svg(),previous)+updated[updated.index('</section>'):]
focus=focus.replace('Three subjects, restored.','A softer curved clover.').replace('Three corrections: heart-shaped clover leaves, eight cog teeth, and a broader corn cob with overlapping husks.','Rounded leaf notches, a soft center and a flowing curved stem.').replace('Subject refinements','Curved clover')
(w/'review.html').write_text(focus);(ROOT/'icon_set/dist/gallery/solo-ai-clover-curve.html').write_text(focus)
p=ROOT/'icon_set/work/solo-ai-next100/review-current.html';page=p.read_text();assert previous in page;page=page.replace(previous,latest);p.write_text(page);(ROOT/'icon_set/dist/gallery/solo-ai-next100.html').write_text(page)
print('Updated clover preview and both existing review pages.')
