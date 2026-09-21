import collections
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
sources = json.loads((OUT / 'sources.json').read_text())
evidence = {x['icon_id']: x for x in json.loads((OUT / 'candidate-evidence.json').read_text())}

# Explicit decisions after viewing all 100 source renders and candidate sheets.
container_ids = {
 7:'container-rounded-square',8:'container-rounded-square',9:'container-rounded-square',10:'upward-pointing-tag',
 14:'simple-house-outline',15:'simple-house-outline',17:'scalloped-circular-badge',18:'empty-rounded-rectangle',19:'rounded-rectangular-frame',20:'open-envelope-with-letter',21:'hand-holding-smartphone',22:'open-book-container',24:'payment-card-container',25:'rounded-chat-message-bubble',26:'rounded-chat-message-bubble',27:'document-with-folded-corner',28:'round-smartwatch',29:'round-smartwatch',30:'round-smartwatch',31:'square-front-smartwatch-container',
 32:'desktop-monitor',33:'desktop-monitor-bottom-bezel',34:'desktop-monitor-bottom-bezel',35:'desktop-monitor-flared-stand',36:'desktop-monitor-flared-stand',37:'desktop-monitor-bottom-bezel',38:'desktop-monitor-bottom-bezel',39:'desktop-monitor',40:'film-frame-container',41:'presentation-board',42:'cloud-speech-bubble',43:'monitor-keyboard',44:'monitor-webcam',45:'desktop-monitor',46:'desktop-monitor',47:'desktop-monitor-flared-stand',48:'double-speech-bubbles',49:'eight-pointed-star-badge',50:'empty-battery-level-indicator',51:'framed-achievement-certificate',52:'hanging-pennant-banner',53:'hanging-shop-sign',54:'horizontal-ticket-voucher',55:'horizontal-mobile-phone',56:'horizontal-ticket-voucher',57:'landscape-mobile-phone',58:'landscape-mobile-phone',59:'horizontal-mobile-phone',60:'mail-envelope',61:'mobile-phone-device',62:'movie-film-frame',63:'movie-film-frame',64:'movie-film-frame',65:'open-envelope-with-letter',66:'oval-speech-bubble',67:'pair-of-square-brackets',68:'pair-of-square-brackets',69:'rectangular-picture-frame',70:'retro-television-with-antenna',71:'retro-television-with-antenna',72:'right-pointing-label-tag',73:'right-pointing-label-tag',74:'right-pointing-label-tag',75:'round-smartwatch',76:'round-smartwatch',77:'rounded-rectangular-frame',78:'pair-of-square-brackets',79:'simple-house-icon',80:'simple-house-icon',81:'square-alignment-measurement-frame',82:'square-artboard-with-corner-indicators',83:'square-alignment-measurement-frame',84:'square-alignment-measurement-frame',85:'square-note-with-top-hole',86:'square-selection-box',87:'square-selection-box',88:'square-smartwatch-device',89:'stacked-browser-windows',90:'stacked-browser-windows',91:'stacked-browser-windows',92:'smartphone-home-bar-container',93:'upward-pointing-tag',94:'vertical-admission-ticket',95:'vertical-admission-ticket',96:'vertical-admission-ticket',97:'web-browser-window',98:'web-browser-window',99:'clipboard',100:'bottom-fold-note-container'
}
adapt = {
 15:'Add the chimney; the available house container has none.',
 21:'Adapt the hand pose to tapping from below/right; the available hand grips from the side.',
 22:'Add the three intrinsic left-page lines while keeping the right page empty.',
 24:'Add the upper stripe divider and second lower mark; the available card has only one lower mark.',
 25:'Add the distinctive jagged top crack; an ordinary message bubble is only a starting point.',
 35:'Add the bottom bezel divider to the flared-stand monitor.',
 36:'Add the bottom bezel divider to the flared-stand monitor.',
 37:'Remove the bezel divider while retaining the trapezoidal stand.',
 91:'Add the other two header controls; the existing stacked-browser container has one.'
}
new_notes = {
 1:'No sidebar container found. Can share a newly prepared left-sidebar frame with source 5; two versus three short navigation lines is a variant.',
 2:'No container with a hand gripping the top of a card found. A hand holding a phone changes the object and grip.',
 3:'No central hexagon with four external round nodes found. The existing molecular hexagon has three nodes on the perimeter, so it is not the same structure.',
 4:'No dashed-sidebar container found.',5:'No left-sidebar container found; share the new frame concept with source 1.',
 6:'No right-sidebar container found; a future left-sidebar frame could be mirrored.',
 11:'No empty earbuds-in-charging-case container found.',
 12:'No left-handle sliding-door container found.',13:'No right-handle sliding-door container found; a new left-handle version could be mirrored.',
 16:'No inset entrance-door container found.',23:'No stacked, gridded table container found.'
}
sub_ids = {2:'user-bust-sub-state-202',3:'padlock-state-167',7:'arrow-angle-up-sub32',8:'arrow-angle-up-sub32',9:'arrow-angle-up-sub32',10:'arrow-angle-up-sub32',11:'lightning-bolt-sub',14:'flame-sub32-v2',15:'open-full-torso-person-sub',17:'check-mark',19:'check-mark',20:'heart-state-63',21:'rising-candlestick-chart-batch-023-03-sub32',22:'dollar-sign-sub',28:'yuan-sign-state-92',29:'dollar-sign-sub',30:'pound-sign-sub',31:'yuan-sign-state-92',39:'arrow-down-arrows-sub32-v2',100:'menu-lines'}
sub_missing = {
 1:'No isolated pair of stacked outlined content tiles found.',
 18:'No isolated tall rectangular portrait placeholder with two lines found. The existing profile-with-text-lines symbol contains a person instead of the rectangular placeholder.',
 26:'No exact isolated check-plus-two-message-lines asset found. Assemble check-mark and text-lines into a new content asset; do not reuse a glyph that already includes a speech bubble.',
 99:'No isolated two-item checklist with diagonal strokes found. Existing checklist assets include an unwanted outer page border; extract/adapt content or assemble existing checks and line strokes.'
}
special = {
 7:'Rotate the up-chevron draft 90 degrees counterclockwise.',8:'Rotate the up-chevron draft 180 degrees.',
 14:'Use the standard complete house outline; source eaves/proportions differ.',
 15:'The available person uses the same head/shoulder/torso concept with a stylized open bottom.',
 17:'Standard scalloped seal differs in lobe count; same empty seal concept.',
 19:'Special layout: two long empty input frames and one small check button, not one outer container. Reuse three instances of the rounded rectangle plus check-mark. Layout work remains.',
 21:'The three-candlestick draft matches the content. Its valid v2 has only TWO candlesticks, so v2 was rejected for faithful reuse.',
 26:'Mirror the standard speech-bubble container horizontally for the lower-right tail.',
 28:'Standard round watch has rounded straps rather than tapered straps; same container concept.',
 29:'Standard round watch has rounded straps rather than tapered straps; same container concept.',
 30:'Standard round watch has rounded straps rather than tapered straps; same container concept.',
 69:'Standard frame has different aspect ratio; reuse if the standard library proportions are acceptable.',
 92:'Complete the cropped phone using the whole existing smartphone; the full model adds lower bezel/home details absent from the crop.',
 100:'The visual source has three equal-length lines; use menu-lines rather than the old brief’s shorter-bottom-line description.'
}
rows=[]
for n, source in enumerate(sources,1):
    cid=container_ids.get(n)
    cs='adapt_existing' if n in adapt else 'reuse' if cid else 'new_asset'
    content=bool(source['decision']['sub_brief']) or n==19
    sid=sub_ids.get(n)
    ss='not_needed' if not content else 'new_asset' if n in sub_missing else 'existing_draft' if evidence[sid]['draft'] else 'reuse'
    cb=source['decision']['main_brief']
    sb=source['decision']['sub_brief']
    if n==19:
        cb={'name':'Rounded input/button frame','family':'container','description':'An empty horizontal rounded rectangular frame. Reuse at two input-field sizes and a smaller check-button size; exclude the checkmark.'}
        sb={'name':'Checkmark','family':'sub','description':'An isolated angled checkmark. Exclude the three rounded form frames.'}
    row={'number':n,'source_uuid':source['uuid'],'source_name':source['concept'],'source_category':source['category'],
         'reference_path':str((ROOT/'pictographic-primitives'/source['path']).resolve()),
         'container':{'status':cs,'candidate_id':cid,'candidate':evidence.get(cid),'brief':cb,'note':adapt.get(n,new_notes.get(n,'Visually matched standard library container concept.'))},
         'content':{'status':ss,'candidate_id':sid,'candidate':evidence.get(sid),'brief':sb,'note':sub_missing.get(n,'No separate content in this source.' if not content else 'Existing draft must be validated/repaired before reuse.' if ss=='existing_draft' else 'Visually matched isolated content concept.')},
         'visual_notes':special.get(n,'')}
    rows.append(row)

cc=collections.Counter(r['container']['status'] for r in rows)
sc=collections.Counter(r['content']['status'] for r in rows)
pairs=[r for r in rows if r['content']['status']!='not_needed']
both=sum(r['container']['status']=='reuse' and r['content']['status']=='reuse' for r in pairs)
summary={'reviewed':100,'selection':'First 100 effective container SKIPs in the local catalog order; not a random or representative sample.',
 'source_pool_count_at_prior_count':850,'empty_sources':100-len(pairs),'sources_with_content':len(pairs),
 'container':dict(cc),'content':dict(sc),'both_ready_among_content_sources':both,
 'unique_reusable_container_ids':len({r['container']['candidate_id'] for r in rows if r['container']['status']=='reuse'}),
 'unique_reusable_content_ids':len({r['content']['candidate_id'] for r in rows if r['content']['status']=='reuse'}),
 'unique_draft_content_ids':len({r['content']['candidate_id'] for r in rows if r['content']['status']=='existing_draft'}),
 'sources_all_needed_assets_reusable':sum(r['container']['status']=='reuse' and r['content']['status'] in ['reuse','not_needed'] for r in rows)}
(OUT/'audit.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2))

intro=f'''# Container reuse audit — 100 sources

Reviewed all 100 source renders and the candidate artwork linked below.

- Container: **{cc['reuse']} reusable**, **{cc['adapt_existing']} require changes to an existing container**, **{cc['new_asset']} have no matching container asset found**.
- Content: **{sc['reuse']} reusable**, **{sc['existing_draft']} have an existing draft to repair/validate**, **{sc['new_asset']} have no matching isolated content asset found**, **{sc['not_needed']} need no content icon**.
- **{both} of the {len(pairs)} content-bearing sources** already have both reusable container and content assets.
- **{summary['sources_all_needed_assets_reusable']} of 100 sources** have all needed artwork available, allowing standard layout/placement work.
- Reusable matches use **{summary['unique_reusable_container_ids']} distinct container IDs** and **{summary['unique_reusable_content_ids']} distinct content IDs**. The five draft matches use two distinct existing drafts.

## Scope and counting

The first 100 of the previously counted 850 effective container SKIPs, in local catalog order. This is not a random sample and must not be extrapolated to the other 750. The skip category includes empty frames/devices: 76 sources have no separate content, and 24 have content. Source 19 is a multi-frame form layout, not an ordinary container/content pair.

Selection: `icon_set/.local/dist/gallery/primitives.json` plus read-only `icon_set/.local/state/feedback.sqlite3`. Reuse search: the fuller `icon_set/.local/combined-dist/gallery/icons.json` catalog (277 container entries), including preserved existing exports. Presence here is local library availability, not proof of production deployment. Selected files were rendered and their stored validation status inspected; no new builds or placement/clearance tests were performed.

“Reusable” means an existing visually compatible standard-library concept, with valid stored validation and an available SVG. It is not pixel-identical tracing. Cosmetic proportions and ordinary mirroring/placement are allowed; structural changes are recorded as adaptation. A draft does not count as ready. “New asset” means no suitable isolated match found in the audited catalog, not proof that no such drawing exists anywhere. Counts are per source; duplicates and mirror variants must be consolidated before generating.

Original references use the current `primitives_root()` implementation, which resolves the repository’s `pictographic-primitives` directory. No source SVG, model, gallery decision, or generation queue was changed. Existing saved briefs are retained in the snapshot; suggested component descriptions here are audit handoffs, not gallery writes.

## Generation/reuse handoff

- Reuse ready candidates before considering generation.
- Adapt the nine listed container occurrences; two of them share the same flared-monitor change.
- Repair/validate the single-chevron symbol for four sources. Reuse the three-candlestick draft for one source after repair; its valid v2 has only two candles and is not equivalent.
- Prepare missing container concepts for 11 occurrences; left/right sidebar and sliding-door variants can share/mirror new base geometry.
- Four sources lack a matching isolated content asset. Two can be assembled/extracted from existing checks and lines. Generate components independently, never the full combination.

## Per-source results

| # | Source | Container | Inner content | Notes |
|---|---|---|---|---|
'''
for r in rows:
    def cell(v):return v['status']+((': '+v['candidate_id']) if v['candidate_id'] else '')
    intro+=f"| {r['number']} | {r['source_name']} | {cell(r['container'])} | {cell(r['content'])} | {r['visual_notes'] or r['container']['note']} |\n"
(OUT/'report.md').write_text(intro)

esc=html.escape
cards=[]
for r in rows:
    pieces=[f'<div><img src="previews/{r["number"]:03}.png"><b>Original</b></div>']
    for key in ['container','content']:
        v=r[key];c=v['candidate']
        img=f'<img src="{esc(c["path"])}">' if c else '<div class="blank">No candidate</div>'
        pieces.append(f'<div>{img}<b>{key}: {esc(v["status"])}</b><p>{esc(v["candidate_id"] or "—")}</p><p>{esc(v["note"])}</p></div>')
    cards.append(f'<article data-status="{r["container"]["status"]} {r["content"]["status"]}"><h2>{r["number"]}. {esc(r["source_name"])}</h2><div class="row">{"".join(pieces)}</div><p>{esc(r["visual_notes"])}</p><small>{esc(r["source_uuid"])}</small></article>')
page=f'''<!doctype html><meta charset="utf-8"><title>100 container reuse checks</title><style>body{{font:16px system-ui;margin:40px;background:#f4f5f7;color:#172030}}header{{max-width:1000px}}article{{background:white;padding:24px;margin:20px 0;border-radius:12px}}.row{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px}}img,.blank{{width:240px;height:240px;object-fit:contain;display:block;margin-bottom:16px}}.blank{{background:#f3f3f3;display:grid;place-items:center}}small{{color:#657080}}select{{padding:10px}}p{{max-width:900px}}b{{display:block}}@media(max-width:800px){{.row{{grid-template-columns:1fr}}}}</style><header><h1>100 container reuse checks</h1><p>Containers: {cc['reuse']} reuse · {cc['adapt_existing']} adapt · {cc['new_asset']} new.</p><p>Inner content: {sc['reuse']} reuse · {sc['existing_draft']} existing draft · {sc['new_asset']} new isolated asset · {sc['not_needed']} not needed.</p><p>First 100 local container SKIPs, not a random sample. Standard-library concept matches; inspect notes for differences. No generation or gallery changes performed.</p><label>Show <select id="filter"><option value="">All 100</option><option value="new_asset">Needs a new isolated asset</option><option value="adapt_existing">Container adaptation</option><option value="existing_draft">Existing draft needs work</option></select></label></header>{''.join(cards)}<script>document.querySelector('#filter').onchange=e=>document.querySelectorAll('article').forEach(a=>a.hidden=e.target.value&&!a.dataset.status.split(' ').includes(e.target.value));</script>'''
(OUT/'index.html').write_text(page)
assert len(rows)==100 and len({r['source_uuid'] for r in rows})==100
assert sum(cc.values())==100 and sum(sc.values())==100
for r in rows:
    for key in ['container','content']:
        v=r[key]
        if v['candidate']:
            assert Path(v['candidate']['path']).is_file()
        if v['status']=='reuse':
            assert not v['candidate']['draft']
            assert v['candidate']['validation']['status']=='valid'
print(json.dumps(summary,indent=2))
