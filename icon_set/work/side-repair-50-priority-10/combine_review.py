"""One portable review collection for the final 68 attempts and shared glyphs."""
from pathlib import Path
import re,json,shutil,html
ROOT=Path(__file__).resolve().parents[3]
W=ROOT/'icon_set/work/side-repair-final-68';W.mkdir(exist_ok=True);assets=W/'review-assets';assets.mkdir(exist_ok=True)
rows=[];cards=[]
for b in (9,10):
 p=ROOT/f'icon_set/work/side-repair-50-priority-{b}';doc=(p/'index.html').read_text();audit=json.loads((p/'audit.json').read_text())
 for f in (p/'review-assets').iterdir():shutil.copy2(f,assets/f'{b}-{f.name}')
 for card in re.findall(r'<article\b.*?</article>',doc,re.S):
  card=card.replace('review-assets/',f'review-assets/{b}-').replace('id="icon-',f'id="icon-{b}-')
  cards.append(card)
 for r in audit:rows.append(dict(r,batch=b))
summary=json.loads((ROOT/'icon_set/work/side-repair-priority/summary.json').read_text());fixed=sum(r['outcome']=='repaired' for r in rows)
style=re.search(r'<style>(.*?)</style>',doc,re.S)[1];script=re.search(r'<script>(.*?)</script>',doc,re.S)[1].replace('of 18 shown','of 68 shown')
glyphs=json.loads((ROOT/'icon_set/work/side-repair-50-priority-10/new-shared-glyphs.json').read_text());glyphcards=[]
for g in glyphs:
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+ ' '.join(str(v) for v in g['preview_box'])+'"><g stroke="currentColor" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">'+''.join('<path d="'+p+'"/>' for p in g['paths'])+'</g></svg>'
 glyphcards.append('<figure>'+svg+'<figcaption>'+html.escape(g['character'])+' · '+html.escape(g['icon_id'])+'</figcaption></figure>')
page=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Side icon repair · 68 reviewed</title><style>{style}.glyphs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:12px 0}}.glyphs svg{{width:72px;height:72px}}</style><header><h1>Side icon repairs · 68 reviewed</h1><div class="counts"><span class="good">{fixed} repaired and linked</span><span class="bad">{68-fixed} still need repair</span><span>{summary['statuses']['pass']} / 825 side sub-icons passing</span></div><p>All 68 have fresh Python repair attempts. Passing repairs use 4px strokes and were checked at native size in both themes and by their centerlines. Each card records the authorized simplifications. Unfinished drafts remain separate from the selected originals.</p><p>{summary['pairs_waiting_for_passing_sub']} pair records still wait for passing sub-icons; {summary['legacy_pairs_needing_mapping']} additional legacy records need mapping. Pair references are updated; cached combined SVGs have not been regenerated. Wide text keeps its natural width and needs placement space.</p><details><summary>Nine new shared typeface characters · existing 97 glyphs unchanged</summary><div class="glyphs">{''.join(glyphcards)}</div><p>All 13 affected icon drafts reference these shared glyphs. Nine pass; four layouts remain unresolved. Natural-width text uses 32px ink height with integer-grid fitting.</p></details><div class="controls"><input id="search" type="search" aria-label="Search" placeholder="Search icons or issues"><select id="filter" aria-label="Result"><option value="">All 68</option><option value="repaired">Repaired</option><option value="unresolved">Still need repair</option></select><a href="audit.json">Detailed audit</a></div><p id="visible"></p></header><main>{''.join(cards)}</main><dialog id="comparison"><button class="close">Close</button><div class="content"></div></dialog><script>{script}</script></html>'''
(W/'index.html').write_text(page);(W/'audit.json').write_text(json.dumps(rows,indent=2));(W/'summary.json').write_text(json.dumps(summary,indent=2));(W/'unresolved.json').write_text(json.dumps([r for r in rows if r['outcome']!='repaired'],indent=2))
assert len(cards)==68
assert len(re.findall('<img ',page))==408
for src in re.findall(r'<img[^>]+src="([^"]+)"',page):assert (W/src).exists()
print(W/'index.html')
