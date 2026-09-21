"""Produce a self-contained local visual review, with frozen reuse previews."""
import html,json,os
from pathlib import Path
from urllib.parse import quote
P=Path(__file__).resolve().parent
data=json.loads((P/'review.json').read_text()); summary=data['summary']
rows=data['rows']; plans=json.loads((P/'authoring-plans.json').read_text())
def link(path): return quote(os.path.relpath(path,P),safe='/')
cards=[]
labels={'reuse_existing_solo':'Reuse now','adapt_existing_artwork':'Adapt existing artwork','convert_existing_container':'Convert to solo','new_solo_brief':'New solo brief'}
for r in rows:
    n=r['number']; route=r['route']; action=r.get('reuse_action','') if route=='solo' else route
    preview=P.parent/'container-classification-rest-20260921/previews'/f'{n:03}.png'
    target=r.get('existing_target'); plan=r.get('authoring_plan'); artwork=''
    if target:
        transform={'rotate-90':'rotate(90deg)','flip-vertical':'scaleY(-1)'}.get(target.get('transform'),'none')
        artwork=f'<figure><img loading="lazy" src="{link(target["preview"])}" style="transform:{transform}"><figcaption>Existing {target["family"]}<br>{html.escape(target["icon_id"])}</figcaption></figure>'
    elif route=='solo': artwork='<div class="empty">No suitable existing whole icon found.<br>Solo brief prepared.</div>'
    else:
        artwork='<div class="components">'+''.join(f'<p><b>{html.escape(c["name"])}</b><br><small>{c["family"]}</small> · {html.escape(c["description"])}</p>' for c in r['components'])+'</div>'
    badge=labels.get(action,'Centered container combination' if route=='container' else 'Side combination')
    note=r.get('notes','') if route=='solo' else r.get('centered_review_note','')
    brief=f'<a class="button" href="{link(plan["brief_path"])}">Open solo brief</a>' if plan else ''
    shared=f'<p class="shared">Shared authoring target with #{r["canonical_source_number"]} — one icon for these references.</p>' if route=='solo' and r.get('canonical_source_number')!=n else ''
    details=plan['subject']['description'] if plan else r['visual_reason']
    meta=(r['name']+' '+str(n)+' '+(target['icon_id'] if target else '')).lower()
    cards.append(f'''<article data-route="{route}" data-action="{action}" data-original="{str(r.get('source_was_solo',False)).lower()}" data-search="{html.escape(meta,quote=True)}">
      <div class="heading"><span class="pill {route}">{badge}</span><span class="number">#{n}</span></div>
      <h2>{html.escape(r['name'])}</h2><div class="comparison"><figure><img loading="lazy" src="{link(preview)}"><figcaption>Original reference</figcaption></figure>{artwork}</div>
      <p>{html.escape(details)}</p><p class="note">{html.escape(note)}</p>{shared}{brief}</article>''')
s=summary['solo_actions']; a=summary['original_205_actions']
page='''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Solo reuse and centered-container review</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f5f7;color:#17202d;font:15px/1.5 system-ui,sans-serif}header,main{max-width:1320px;margin:auto;padding:28px}h1{font-size:32px;line-height:1.15;margin:0 0 14px}header p{max-width:950px;color:#465365}.stats{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0}.stat{background:white;border:1px solid #dde2e8;border-radius:14px;padding:13px 18px;min-width:160px}.stat b{display:block;font-size:28px}.stat small{color:#546172}.toolbar{position:sticky;top:0;z-index:2;background:#f4f5f7ed;border-block:1px solid #dde2e8;padding:14px 0;display:flex;gap:10px;flex-wrap:wrap;backdrop-filter:blur(8px)}input,select{font:inherit;padding:10px;border:1px solid #ccd3dd;border-radius:8px;background:white}input{flex:1;min-width:180px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}article{background:white;padding:22px;border:1px solid #dde2e8;border-radius:16px;min-width:0}h2{font-size:20px;margin:12px 0}.heading{display:flex;justify-content:space-between;align-items:center}.number{color:#7b8796}.pill{font-size:12px;border-radius:16px;padding:5px 10px;background:#e6edf8;color:#264b81}.container{background:#eaf0e7;color:#476137}.side{background:#fff0d7;color:#806123}.comparison{display:grid;grid-template-columns:1fr 1fr;gap:12px;min-height:245px;align-items:center}figure{margin:0;min-width:0;text-align:center}figure img{width:170px;height:170px;object-fit:contain;max-width:100%}figcaption{font-size:11px;color:#6b7482;overflow-wrap:anywhere;min-height:38px}.empty{font-size:14px;text-align:center;background:#f6f7f9;border-radius:12px;padding:30px 15px;color:#687487}.components{font-size:12px;max-height:240px;overflow:auto}.components p{margin:8px 0}.note,.shared{font-size:13px;color:#606d7b}.button{display:inline-block;text-decoration:none;color:#25519a;font-weight:600}a{color:#25519a}.count{margin:18px 0;color:#667085}article[hidden]{display:none}footer{padding:30px;color:#738092;font-size:12px}@media(max-width:760px){header,main{padding:18px}.grid{grid-template-columns:1fr}h1{font-size:26px}}
</style></head><body><header><h1>Reuse first. Brief what is missing.</h1>
'''
page+=f'''<p>The remaining 750 references have been rechecked. Empty hosts and devices are solo; a container combination needs an independent glyph centered in its usable hosting area. Distributed layouts, attached artwork and the examples you flagged stay together as solo subjects.</p>
<div class="stats"><div class="stat"><b>382</b><small>solo references</small></div><div class="stat"><b>365</b><small>centered combinations</small></div><div class="stat"><b>3</b><small>side combinations</small></div><div class="stat"><b>177</b><small>additional solo corrections</small></div></div>
<p><b>Of the original 205 solos:</b> {a['reuse_existing_solo']} reuse now · {a['adapt_existing_artwork']} adapt existing artwork · {a['convert_existing_container']} convert existing containers · {a['new_solo_brief']} need a new solo brief.</p>
<p><b>Across all 382 solos:</b> {s['reuse_existing_solo']} reuse now · {s['adapt_existing_artwork']} adapt · {s['convert_existing_container']} convert · {s['new_solo_brief']} new-brief references. Repeated concepts share targets: <b>{summary['distinct_authoring_briefs']} distinct authoring briefs</b>, including eight repairs to already-drawn source matches. No icons were generated or queued.</p>
<p>Original and existing artwork are shown side by side. An adaptation is a starting point, not a finished match. The first 100 references are outside this second-pass scope.</p>
<p><a href="solo-briefs/index.html">Browse solo briefs and 48 px previews</a> · <a href="authoring-references/manifest.json">Solo manifest</a> · <a href="review.json">Complete reuse map</a></p>
</header><main><div class="toolbar"><input id="search" placeholder="Find a name, reference number or existing icon"><select id="filter"><option value="original">Original 205 solos</option value="solo">All 382 solos</option><option value="reuse_existing_solo">Reuse now</option><option value="adapt_existing_artwork">Adapt existing artwork</option><option value="convert_existing_container">Convert to solo</option><option value="new_solo_brief">New solo briefs</option><option value="container">365 container combinations</option><option value="side">3 side combinations</option><option value="all">All 750 references</option></select></div><p class="count" id="count"></p><div class="grid">'''
page+='\n'.join(cards)+'''</div></main><footer>Source SVGs are preserved unchanged. Existing previews are frozen for this review. Standalone briefs use the solo family at 48 px.</footer><script>
const cards=[...document.querySelectorAll('article')],f=document.querySelector('#filter'),q=document.querySelector('#search');function update(){let count=0;for(const c of cards){const a=f.value,show=(a==='all'||a==='original'&&c.dataset.original==='true'||a===c.dataset.route||a===c.dataset.action)&&c.dataset.search.includes(q.value.toLowerCase());c.hidden=!show;if(show)count++}document.querySelector('#count').textContent=count+' references shown'}f.onchange=update;q.oninput=update;update();
</script></body></html>'''
(P/'index.html').write_text(page)
print('Report written:',P/'index.html')
