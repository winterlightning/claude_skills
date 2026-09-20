import json,re,html,shutil,sys,xml.etree.ElementTree as ET
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
MAIN=ROOT/'icon_set/work/side-repair-final-68';page=(MAIN/'index.html').read_text();(W/'previous-review.html').write_text(page) if not (W/'previous-review.html').exists() else None
rows=json.load(open(MAIN/'audit.json'));updates=json.load(open(W/'accepted.json'));assets=W/'review-assets';assets.mkdir(exist_ok=True);cards=[]
notes={
'baby-head-sub32-v3':'Restored a large baby face, circular jaw, curl, eyes and smile. Removed the rejected tiny-head-and-wrap repair.',
'mobile-contactless-payment-solo-profile32':'User-approved 32×48 side exception. Shared dollar glyph, 4px stroke, one wireless arc; frame openings give the currency stem room.',
'mobile-wireless-pound-payment-solo-profile32':'Similar layout: user-approved 32×48 side exception. Shared pound glyph and a closed phone frame, retaining the 4px stroke.',
'money-bag-sub32':'Kept the bag. Simplified the dollar to an open S curve with short top/bottom ticks; no heavy bar through the middle.'}
def card(r,before,after,desc,label,good=True,h=32):
 uid=r['icon'];stem=r['source_uuid'];original=Path(r['source_path']).read_text();svg=create(after).to_svg();tree=ET.fromstring(svg)
 for e in tree.iter():
  if 'stroke-width' in e.attrib:e.set('stroke-width','.3')
 docs={'original':original,'before':create(before).to_svg(),'after':svg,'center':ET.tostring(tree).decode()}
 for name,s in docs.items():
  (assets/f'{stem}-{name}.svg').write_text(s);(MAIN/'review-assets'/f'feedback-{stem}-{name}.svg').write_text(s)
 def fig(kind,title,css=''):
  return f'<figure class="{css}" style="--cw:32"><figcaption>{title}</figcaption><img src="review-assets/{stem}-{kind}.svg" style="height:{h if css.startswith("native") else 150}px;width:auto;max-width:100%" alt="{html.escape(uid)}"></figure>'
 status='repaired' if good else 'unresolved'
 return f'<article data-outcome="{status}" id="feedback-{stem}"><h2>{html.escape(uid)}</h2><span class="badge {status}">{html.escape(label)}</span><div class="previews">{fig("original","Original source")}{fig("before","Previous drawing")}{fig("after",f"Current · 32×{h}","grid")}{fig("center","Centerline","grid")}</div><div class="native">{fig("after",f"Native 32×{h}","native")}{fig("after","Dark","native dark")}</div><p>{html.escape(desc)}</p><button class="enlarge">Enlarge / compare</button><details><summary>Review details</summary><p>{html.escape(desc)} Source: {stem}. Previous model preserved.</p></details></article>'
for u in updates:
 r=next(r for r in rows if u['icon'] in (r['icon'],r.get('candidate')))
 htmlcard=card(r,u['icon'],u['candidate'],notes[u['icon']],'Corrected · checks pass',h=u['candidate_dimensions'][1]);cards.append(htmlcard)
 oldid=f'icon-{r["batch"]}-{r["number"]}'
 page,n=re.subn(r'<article\b[^>]*id="'+re.escape(oldid)+r'".*?</article>',lambda _:htmlcard.replace('review-assets/', 'review-assets/feedback-'),page,flags=re.S);assert n==1
 r.update(superseded_candidate=r.get('candidate'),candidate=u['candidate'],candidate_python=u['candidate_python'],outcome='repaired',reason=notes[u['icon']],candidate_status='pass',candidate_findings=[],feedback_corrected=True,canvas_height=u['candidate_dimensions'][1])
r=next(r for r in rows if r['icon']=='financial-dollar-sign-document-solo-profile32')
note='The earlier clipped-corner document and lighter dollar are retained, as requested. The rejected heavy-dollar draft is not selected. Existing geometry findings remain visible; visual preference is not a geometry pass.'
htmlcard=card(r,r['icon'],r['icon'],note,'Earlier drawing retained · user preference',good=False);cards.insert(1,htmlcard)
page,n=re.subn(r'<article\b[^>]*id="icon-9-17".*?</article>',lambda _:htmlcard.replace('review-assets/','review-assets/feedback-'),page,flags=re.S);assert n==1
r.update(rejected_candidate=r.get('candidate'),displayed_candidate=r['icon'],reason=note,user_preferred_before=True)
summary=json.load(open(ROOT/'icon_set/work/side-repair-priority/summary.json'))
page=page.replace('57 repaired and linked','60 repaired and linked').replace('11 still need repair','8 still need repair').replace('814 / 825','817 / 825').replace('29 pair records','28 pair records').replace('Nine pass; four layouts remain unresolved.','Ten pass; three layouts remain unresolved.')
(MAIN/'index.html').write_text(page);(MAIN/'audit.json').write_text(json.dumps(rows,indent=2));(MAIN/'unresolved.json').write_text(json.dumps([r for r in rows if r['outcome']!='repaired'],indent=2));(MAIN/'summary.json').write_text(json.dumps(summary,indent=2))
# Show the other two matching phone layouts without silently changing them.
related=[]
for uid in ('mobile-contactless-euro-payment-sub32','wireless-mobile-yuan-payment-sub32'):
 m=create(uid);(assets/(uid+'.svg')).write_text(m.to_svg());related.append(f'<figure><img src="review-assets/{uid}.svg" style="width:64px;height:64px"><figcaption>{uid}<br>Related 32×32 drawing · unchanged</figcaption></figure>')
style=re.search(r'<style>(.*?)</style>',page,re.S)[1];script=re.search(r'<script>(.*?)</script>',page,re.S)[1].replace('of 68 shown','of 5 shown')
(W/'index.html').write_text(f'<!doctype html><html><meta charset="utf-8"><title>Review corrections</title><style>{style}</style><header><h1>Your four review comments · corrected</h1><p>Baby redrawn; earlier dollar document retained; money bag simplified. Dollar and pound wireless phones use the approved 32×48 side exception, preserving 4px strokes.</p><p>817 / 825 side sub-icons pass; 8 remain unresolved.</p><div class="controls"><input id="search" placeholder="Search"><select id="filter"><option value="">All 5</option><option value="repaired">Corrected</option><option value="unresolved">Retained before</option></select></div><p id="visible"></p><details><summary>Two more similar phone layouts</summary><div class="native">'+''.join(related)+'</div></details></header><main>'+''.join(cards)+f'</main><dialog id="comparison"><button class="close">Close</button><div class="content"></div></dialog><script>{script}</script></html>')
print(W/'index.html')
