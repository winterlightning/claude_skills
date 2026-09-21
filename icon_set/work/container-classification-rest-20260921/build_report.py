import collections,html,json
from pathlib import Path
P=Path(__file__).resolve().parent
data=json.loads((P/'review.json').read_text());s=data['summary'];rows=data['rows']
v=json.loads((P/'verification.json').read_text());assert v['saved']
corrected=sum(r['component_fields_corrected'] or r['extra_components_added'] for r in rows)
report=f'''# Remaining 750 container classifications — corrected

All **750 remaining sources** from the original group of 850 were visually reviewed. Changes are saved in the local gallery database and read back successfully.

| Classification | Remaining 750 | Full original 850 |
|---|---:|---:|
| Solo | 205 | 281 |
| Container combination | 542 | 566 |
| Side combination | 3 | 3 |
| Total | 750 | 850 |

**208 classifications corrected** in this pass. The earlier 100-source decisions were preserved. Empty devices/frames, structural layouts and intrinsic object parts route to SOLO48. A genuine frame with independently meaningful content remains a container combination.

The three side combinations are Medical Healthcare Message Envelope, Remote Video Meeting, and Team Approval and Disapproval Feedback. Their relative positions and separate component briefs are saved.

## Component corrections

**{corrected} combination sources** received corrected or additional component descriptions. This includes **15** corrections to the main/sub gallery fields and **37** sources with additional components recorded in the full reference brief; these groups overlap. Examples include missing crosses on ballots/capsules, hearts above couples, plus/check modifiers beside portraits, elevator arrows, and content on both laptop/phone screens. The laptop's circular trace was not incorrectly substituted with the phone's cloud.

All **750** sources now have saved reference briefs. The **557** sources still marked SKIP all have nonempty saved briefs (**557/557**). The export contains **1,342** individual component/solo briefs. For more than two components, the full reference brief contains all parts; the gallery's two component fields cannot represent the entire list.

## Reuse and generation status

- **9** solo sources have visually checked, source-linked solo artwork for reuse.
- **3** have visually checked, source-linked container artwork held for SOLO48 conversion.
- These **12** remain SKIP with reason `other` solely to prevent duplicate generation; their reference-brief family is `solo`.
- The other **193** are returned to TODO with saved solo briefs requiring library and within-batch duplicate checks before authoring. They are **not 193 confirmed new icons**.
- Semantic search suggestions are unverified leads, not approved reuse matches. The broader artwork reuse audit is not complete for these 193.
- **0** generation jobs were created; no artwork or model family was changed.

## Two naming/content questions

- Remaining #20 (overall #120), Geometric Shapes in Frame: its shallow bowl/angled-handle mark is visually ambiguous. Its visible geometry is preserved in a separate draft brief; identify the intended object before authoring.
- Remaining #640 (overall #740), Square Ant Farm Container: the image shows only a divided rectangle and central circle, with no ant. It routes to solo, preserving the visible layout; the title needs editorial review.

## Verification and scope

Every saved route, brief, component field and side position was read back and checked. Unrelated decisions, prior reference briefs and the first 100 sources were unchanged. Source snapshots and a rollback record are retained in this directory. This report concerns the local workspace gallery; it is not a production publication.

[Visual review](index.html) · [Full review data](review.json) · [Independent components](components.json) · [Verification](verification.json)

The table below uses **remaining-batch numbers 1–750**; add 100 for the original 850-source sequence.

| Remaining # | Source | Correct route | Reuse / preparation |
|---|---|---|---|
'''
for r in rows:
    report+=f"| {r['number']} | {r['name'].replace('|','/')} | {r['route']} | {r['reuse_action'].replace('_',' ')} |\n"
(P/'report.md').write_text(report)
compact=[]
for r in rows:
    x={k:r.get(k) for k in ['number','name','uuid','reference_path','route','visual_reason','notes','components','reuse_action','reuse_note','reuse_candidates','status','reason','sub_position']}
    compact.append(x)
payload=json.dumps(compact).replace('<','\\u003c')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>850 container classifications — corrected</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f5f6f8;color:#202938;font:16px/1.5 system-ui}main{max-width:1180px;margin:auto;padding:36px 24px}h1{font-size:32px;line-height:1.2;margin-bottom:12px}h2{font-size:21px}h3{font-size:16px;margin:12px 0 3px}p{max-width:950px}.muted,small{color:#626d7d}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:28px 0}.stat{background:white;padding:20px;border-radius:12px;border:1px solid #dde2e9}.stat strong{display:block;font-size:32px}.toolbar{display:flex;gap:12px;flex-wrap:wrap;position:sticky;top:0;background:#f5f6f8;padding:15px 0;z-index:1}input,select,button{font:inherit;padding:10px;border:1px solid #bbc4d1;border-radius:6px;background:white}input{flex:1;min-width:200px}button{cursor:pointer}button:disabled{opacity:.4;cursor:default}article{background:white;border:1px solid #dde2e9;border-radius:12px;margin:18px 0;padding:24px}.body{display:grid;grid-template-columns:240px 1fr;gap:28px}img{width:240px;height:240px;object-fit:contain;background:white}.badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:14px;background:#e5eefb}.solo{background:#def3e9}.side{background:#f9eacb}.components{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.component{border-top:1px solid #e0e5eb;padding-top:5px}.notice{border-left:3px solid #b07a23;padding:4px 14px;background:#fff9ec}.reuse{background:#f3f5f7;padding:12px;border-radius:6px}.nav{display:flex;gap:18px;align-items:center}a{color:#245ead}code{overflow-wrap:anywhere}details{margin-top:14px}summary{cursor:pointer}@media(max-width:650px){.body{grid-template-columns:1fr}.components{grid-template-columns:1fr}.stats{gap:6px}.stat{padding:12px}.stat strong{font-size:27px}}
</style><main><small>LOCAL GALLERY · REVIEW SAVED</small><h1>850 container classifications, corrected</h1><p>The remaining <strong>750 originals</strong> have been visually reviewed. Empty frames, devices and intrinsic layouts route to solo. Separate content inside an enclosure remains a container combination.</p>
<div class="stats"><div class="stat"><strong>281</strong>Solo <small>205 in this pass</small></div><div class="stat"><strong>566</strong>Container combinations <small>542 in this pass</small></div><div class="stat"><strong>3</strong>Side combinations <small>3 in this pass</small></div></div>
<p><strong>208 classifications corrected in this pass.</strong> All 750 saved briefs were verified. No icons were generated.</p><p class="notice">Reuse: 9 source-linked solo assets and 3 container assets were visually compared and held for reuse/conversion. The other 193 solo sources still require artwork reuse checks before generation. They are not confirmed missing icons.</p><p><a href="report.md">Full report</a> · <a href="components.json">Independent component briefs</a> · <a href="../container-reuse-audit-100-20260920/index.html">Earlier 100-source review</a></p>
<div class="toolbar"><input id="search" placeholder="Search name or source ID" aria-label="Search icons"><select id="route" aria-label="Classification"><option value="">All remaining 750</option><option value="solo">Solo — 205</option><option value="container">Container — 542</option><option value="side">Side — 3</option></select></div><p id="count" class="muted"></p><div class="nav"><button id="prev">Previous</button><span id="page"></span><button id="next">Next</button></div><section id="results"></section><p class="muted">Headings use the original 850-source sequence (#101–850). Each source also shows its remaining-batch number. Search suggestions are not approved artwork matches.</p></main>
<script id="data" type="application/json">PAYLOAD</script><script>
const rows=JSON.parse(document.querySelector('#data').textContent);let page=0;const size=25;
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){const q=document.querySelector('#search').value.toLowerCase(),route=document.querySelector('#route').value;const filtered=rows.filter(r=>(!route||r.route===route)&&(!q||(r.name+' '+r.uuid+' '+(r.number+100)).toLowerCase().includes(q)));const pages=Math.max(1,Math.ceil(filtered.length/size));page=Math.min(page,pages-1);document.querySelector('#count').textContent=filtered.length+' sources';document.querySelector('#page').textContent='Page '+(page+1)+' of '+pages;document.querySelector('#prev').disabled=page===0;document.querySelector('#next').disabled=page+1>=pages;
document.querySelector('#results').innerHTML=filtered.slice(page*size,(page+1)*size).map(r=>`<article><span class="badge ${r.route}">${r.route==='solo'?'Solo':r.route==='side'?'Side combination':'Container combination'}</span><h2>${r.number+100}. ${esc(r.name)}</h2><div class="body"><div><img loading="lazy" src="previews/${String(r.number).padStart(3,'0')}.png" alt="Original ${esc(r.name)}"><small>Original · remaining #${r.number}</small></div><div><p>${esc(r.visual_reason)}</p>${r.notes?`<p class="notice">${esc(r.notes)}</p>`:''}<div class="components">${r.components.map(c=>`<div class="component"><h3>${esc(c.name)}</h3><small>${esc(c.family)}</small><p>${esc(c.description)}</p></div>`).join('')}</div>${r.sub_position?`<p>Sub position: <strong>${esc(r.sub_position)}</strong></p>`:''}<div class="reuse"><strong>${esc(r.reuse_action.replaceAll('_',' '))}</strong><p>${esc(r.reuse_note)}</p>${(r.reuse_candidates||[]).filter(c=>c.source_linked).map(c=>`<p>${esc(c.icon_id)} · ${esc(c.family)}</p>`).join('')}</div><details><summary>Source identity and saved status</summary><p>${esc(r.uuid)}</p><p>${esc(r.reference_path)}</p><p>${esc(r.status)}${r.reason?' / '+esc(r.reason):''}</p></details></div></div></article>`).join('');}
document.querySelector('#search').oninput=()=>{page=0;render()};document.querySelector('#route').onchange=()=>{page=0;render()};document.querySelector('#prev').onclick=()=>{page--;render()};document.querySelector('#next').onclick=()=>{page++;render()};render();
</script></html>'''.replace('PAYLOAD',payload)
(P/'index.html').write_text(page)
assert len(compact)==750 and sum(collections.Counter(r['route'] for r in compact).values())==750
assert all((P/f"previews/{r['number']:03}.png").is_file() for r in rows)
print('Report and visual review written. Combination sources with brief corrections:',corrected)
