"""Recheck content matches and render direction-aware, current routing evidence."""
import collections
import html
import json
from pathlib import Path

OUT=Path(__file__).resolve().parent
data=json.loads((OUT/'audit.json').read_text())
rows=data['rows']
backup=OUT/'audit-before-content-recheck.json'
if not backup.exists():backup.write_text(json.dumps(data,indent=2))
extra={x['icon_id']:x for x in json.loads((OUT/'recheck-alternatives.json').read_text())}
notes={
1:'Two separate outlined tiles are required; no isolated matching asset was found. Keep as new content, not an arbitrary list glyph.',
2:'The original has a connected head/neck and a closed, flat-bottom bust. The previous match detached the head. Use the connected-bust candidate only as a starting point and close its bottom outline.',
3:'The original lock has a rounded bowl-shaped lower body and no keyhole dot. The candidate has a rectangular body and keyhole dot: adapt those features; not a ready match.',
7:'Expected: a single open LEFT chevron, no shaft. The preview now rotates the existing up-chevron 90 degrees counterclockwise. Its angle is narrower than the source; widen the angle and validate the existing draft before reuse.',
8:'Expected: a single open DOWN chevron, no shaft. The previous preview incorrectly showed UP. The preview now applies 180-degree rotation. Its angle is narrower than the source; widen the angle and validate the existing draft before reuse.',
9:'Expected: a single open UP chevron, no shaft. Direction is correct, but the existing draft has a narrower apex angle than the source. Adjust the angle and validate; not ready reuse.',
10:'Expected: a single open UP chevron inside the pointed badge. Existing draft direction is correct; its narrower apex angle needs adjustment and validation.',
11:'Single outlined lightning bolt, same direction and topology. Standardized rounded corners differ from the thin original; acceptable standard-library reuse.',
14:'Single flame with a taller left tip, inward notch and smaller right tip. Existing isolated flame preserves the visible structure.',
15:'Original torso closes at the base and the head joins the shoulders. The previous open-bottom torso was wrong. Replaced with the closed-torso symbol as a starting point; connect the head/neck to the shoulders before faithful reuse.',
17:'Single checkmark with short lower-left arm and longer upper-right arm. Direction and structure match.',
18:'One upright rectangular portrait placeholder plus two horizontal lines is required. A person portrait or two checkbox rows is not equivalent; retain as unmatched isolated content.',
19:'Checkmark matches. The original is a layout of two input frames and a smaller check button, so three frame instances still need layout.',
20:'Single symmetrical outlined heart with central notch and pointed lower tip. Structure and orientation match.',
21:'Three ascending candlesticks with bodies and wicks match. Preserve all THREE; the valid v2 has only TWO and is not a substitute. Existing three-candle draft still requires repair/validation.',
22:'The original dollar uses an S with short top/bottom stem extensions and no continuous center stroke. The candidate has a continuous vertical stroke through the S. Reuse only after adapting that glyph detail.',
26:'A checkmark beside two equal horizontal lines is required. No isolated complete content match found. Existing check and line assets can be assembled; do not reuse a speech-bubble glyph that includes its own enclosure.',
28:'Y-shaped currency glyph with one horizontal crossbar and a descending stem. Structure and orientation match.',
29:'As in source 22, adapt the dollar glyph to the original short stem extensions instead of the candidate continuous center stroke.',
30:'Replaced pound-sign-sub with pound-sign-sub32-v2: one crossbar and a curved foot joining the baseline match the source better than the earlier straight vertical stem.',
31:'Y-shaped currency glyph with one horizontal crossbar and a descending stem. Structure and orientation match.',
39:'A downward arrow WITH a long vertical shaft, distinct from source 8’s shaftless chevron. Existing downward-shaft arrow matches the structure; standard arrowhead proportions differ.',
99:'Two checks with short diagonal strokes are required. Existing checklist candidates include unwanted page borders; retain as content adaptation/assembly work, not ready reuse.',
100:'The bottom line IS shorter than the upper two. The earlier equal-line claim was wrong. Shorten the bottom stroke of menu-lines; the current candidate is not a ready match.'
}
adapt={2,3,15,22,29,100}
for r in rows:
    n=r['number']
    if n not in notes:continue
    c=r['content']
    if n in [2,15,30]:
        id={2:'user-bust-sub-state-199',15:'full-torso-person-sub',30:'pound-sign-sub32-v2'}[n]
        c['candidate_id']=id;c['candidate']=extra[id]
    if n in adapt:c['status']='adapt_existing'
    c['note']=notes[n]
    c['preview_rotation_degrees']={7:-90,8:180}.get(n,0)
    c['expected_direction']={7:'left',8:'down',9:'up',10:'up',39:'down'}.get(n)
    c['match_review']='needs_adaptation' if n in adapt else 'draft_needs_repair' if c['status']=='existing_draft' else 'no_match' if c['status']=='new_asset' else 'standard_library_match'
    c['expected_name']={7:'Left chevron',8:'Down chevron',9:'Up chevron',10:'Up chevron',39:'Downward shaft arrow'}.get(n,(c.get('brief') or {}).get('name','Inner content'))
    r['visual_notes']=notes[n]
    if n==26:r['container']['preview_mirror_horizontal']=True
    if n==19:r['container']['note']='Reuse three rounded frame instances in the input-field/button layout. The single preview shows the reusable base frame, not the completed layout.'
    if n==100:c['brief']['description']='Three left-aligned horizontal lines: two equally long upper lines and a shorter bottom line. Exclude the surrounding folded document.'

sc=collections.Counter(r['content']['status'] for r in rows)
data['summary']['content']=dict(sc)
data['summary']['both_ready_among_content_sources']=sum(r['container']['status']=='reuse' and r['content']['status']=='reuse' for r in rows if r['content']['status']!='not_needed')
data['summary']['sources_all_needed_assets_reusable']=sum(r['container']['status']=='reuse' and r['content']['status'] in ['reuse','not_needed'] for r in rows)
data['summary']['unique_reusable_content_ids']=len({r['content']['candidate_id'] for r in rows if r['content']['status']=='reuse'})
data['summary']['content_recheck']='All 24 content-bearing sources visually rechecked; candidate direction is explicit and applied in the preview. No model generation or fresh model QA performed.'
data['summary']['routing_note']='The 76 sources without content route to solo. See solo-routing.json; historical container counts are superseded for these sources.'
(OUT/'audit.json').write_text(json.dumps(data,indent=2))
assert sum(sc.values())==100
assert rows[7]['content']['preview_rotation_degrees']==180
assert rows[6]['content']['preview_rotation_degrees']==-90
assert rows[99]['content']['status']=='adapt_existing'

esc=html.escape
solo={r['number']:r for r in json.loads((OUT/'solo-routing.json').read_text())['rows']}
cards=[]
labels={'reuse':'Ready to reuse','adapt_existing':'Adapt existing artwork','existing_draft':'Draft — changes / validation needed','new_asset':'No isolated match found','not_needed':'Not needed'}
def candidate_card(v,label):
    c=v.get('candidate');transform=[]
    if v.get('preview_rotation_degrees'):transform.append(f'rotate({v["preview_rotation_degrees"]}deg)')
    if v.get('preview_mirror_horizontal'):transform.append('scaleX(-1)')
    style=f' style="transform:{" ".join(transform)}"' if transform else ''
    img=f'<img src="{esc(c["path"])}" alt="{esc(v.get("expected_name",label))}"{style}>' if c else '<div class="blank">No matching asset</div>'
    detail=f'<p class="transform">Preview: {v["preview_rotation_degrees"]}° rotation applied</p>' if v.get('preview_rotation_degrees') else '<p class="transform">Preview: horizontal mirror applied</p>' if v.get('preview_mirror_horizontal') else ''
    return f'<div>{img}<b>{esc(label)} · {esc(labels[v["status"]])}</b><p>{esc(v.get("expected_name", ""))}</p><small>{esc(v.get("candidate_id") or "—")}</small>{detail}<p>{esc(v["note"])}</p></div>'

for r in rows:
    n=r['number'];original=f'<div><img src="previews/{n:03}.png" alt="Original {esc(r["source_name"])}"><b>Original</b></div>'
    if n in solo:
        s=solo[n];status='solo';tag='SOLO · no inner icon needed'
        parts=original+f'<div><img src="{esc(s["reuse_svg_path"])}" alt="Existing solo route candidate"><b>{esc(s["action"].replace("_"," "))}</b><small>{esc(s["reuse_icon_id"])}</small><p>{esc(s["note"])}</p></div><div><h3>No sub icon</h3><p>Saved route: solo. Reuse the existing target; do not generate a duplicate.</p></div>'
    else:
        status='content '+r['content']['status'];tag='CONTENT MATCH RECHECKED'
        parts=original+candidate_card(r['container'],'Container')+candidate_card(r['content'],'Inner icon')
    cards.append(f'<article id="icon-{n}" data-status="{status}"><h2>{n}. {esc(r["source_name"])}</h2><p class="tag">{tag}</p><div class="row">{parts}</div><small>{esc(r["source_uuid"])}</small></article>')

page='''<!doctype html><meta charset="utf-8"><title>100 icon reuse checks — corrected</title><style>
body{font:16px system-ui;margin:32px;background:#f4f5f7;color:#172030}header{max-width:1050px}article{background:white;padding:24px;margin:24px 0;border-radius:12px;scroll-margin-top:12px}.row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}img,.blank{width:100%;height:240px;object-fit:contain;display:block;margin-bottom:18px}.blank{background:#f3f3f3;display:grid;place-items:center}small{color:#657080;overflow-wrap:anywhere}p{line-height:1.5}b{display:block}.tag{font-size:12px;font-weight:700;color:#526782}.transform{color:#785307;font-weight:600}select{padding:10px}a{color:#254fb3}@media(max-width:760px){.row{grid-template-columns:1fr}body{margin:16px}}
</style><header><h1>100 icon reuse checks — corrected</h1><p>All 24 inner-icon matches rechecked. Left/down chevron previews now show the required orientation. Drafts and shapes needing changes are not counted as ready.</p>'''
page+=f'<p>Inner icons: <b style="display:inline">{sc["reuse"]} ready · {sc["adapt_existing"]} adapt existing · {sc["existing_draft"]} existing drafts · {sc["new_asset"]} unmatched.</b> The other 76 sources route to solo and need no inner icon.</p>'
page+='''<p><a href="#icon-8">Go to #8 Square Down Arrow</a> · <a href="content-recheck.md">Review notes</a> · <a href="solo-routing-report.md">Solo routing report</a></p><label>Show <select id="filter"><option value="">All 100</option><option value="content">24 content-bearing sources</option><option value="adapt_existing">Inner icons needing adaptation</option><option value="existing_draft">Existing inner-icon drafts</option><option value="new_asset">No isolated inner-icon match</option><option value="solo">76 solo routes</option></select></label></header>'''+''.join(cards)+'''<script>document.querySelector('#filter').onchange=e=>document.querySelectorAll('article').forEach(a=>a.hidden=Boolean(e.target.value&&!a.dataset.status.split(' ').includes(e.target.value)));</script>'''
(OUT/'index.html').write_text(page)
md='# Inner-icon match recheck\n\nAll 24 content-bearing originals and their candidates were visually rechecked side by side. These are match-review results, not new model QA or generated artwork.\n\n'
md+=f"**{sc['reuse']} ready**, **{sc['adapt_existing']} require adaptation**, **{sc['existing_draft']} existing drafts requiring work**, **{sc['new_asset']} no isolated match found**. The other 76 remain solo routes.\n\n"
md+='The #7/#8 previews now apply the required left/down rotations. Both still use an existing up-chevron draft as the base and need its narrower angle adjusted; neither is presented as ready. Source #26 now previews the speech-bubble mirror explicitly.\n\n| # | Source | Decision | Review |\n|---|---|---|---|\n'
for r in rows:
    if r['number'] in notes:md+=f"| {r['number']} | {r['source_name']} | {r['content']['status']} | {r['content']['note']} |\n"
(OUT/'content-recheck.md').write_text(md)
# The previous report contained contradicted ready claims; replace it with current results.
(OUT/'report.md').write_text('# Current reuse audit\n\nThe 76 empty sources route to **solo**; see [solo routing](solo-routing-report.md).\n\n'+md.replace('# Inner-icon match recheck','## Inner-icon match recheck',1)+'\n[Open current visual comparisons](index.html) · [Machine-readable audit](audit.json)\n')
print(json.dumps(data['summary'],indent=2))
