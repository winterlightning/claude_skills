"""Package finalized review evidence; run after visual inspection and validation."""
import base64,collections,html,importlib.util,json
from pathlib import Path
import author_batch as batch
ROOT=batch.ROOT
import sys
sys.path.insert(0,str(ROOT))
BATCH=batch.BATCH
esc=html.escape
notes={
1:'Larger circular jaw and mirrored fringe; long hair and detached shoulders read clearly. Hair-to-fringe is at the sampled spacing boundary.',
2:'Typeface v2 proportions, matched cap height and baseline, and open counters.',
3:'Selected the taller yuan mark over the shorter, more compliant draft because the long currency stem is recognizable. Compact strap and dial spacing remains flagged.',
4:'Longer check ascent, rounded calendar corners, and consistent bindings.',
5:'Check keeps a long ascent and balanced content margin; sampled spacing remains at the boundary.',
6:'Circular head, bowed skullcap seam and broad symmetric shoulders. Head-to-body ink gap is exactly 4 units.',
7:'Typeface v2 digit and G share cap height, baseline and consistent curves.',
8:'Typeface v2 open four and rounded G share the baseline; retained the requested typeface rather than tracing the thin source.',
9:'Typeface v2 five and G retain open counters and matched proportions.',
10:'Two open B counters and two currency ticks inside a circular coin; shared endpoints remove stray intersections.',
11:'Sterling hook, crossbar and baseline restore the intended pound sign. Compact internal hook spacing remains reported.',
12:'Smooth open palm, wrist and bent thumb now join at a real shared node; removed the crossed pocket from the initial draft.',
13:'Open key bow, diagonal shaft and one clear tooth inside the restored phone band.',
14:'Outlined head, raised arms and short torso preserve the reference portrait. The torso-to-page-band spacing still fails.',
15:'Flat cap and clear descending seven, centered in the lower calendar panel.',
16:'Smooth diagonal receiver with angled earpieces replaces the crowded closed loops. Tight inner receiver spacing remains reported.',
17:'Selected the wider double-ended wrench because the narrow draft read as an X. Rounded car body and wheel arches remain clear; roof-to-wrench spacing still fails.',
18:'Six open atom nodes, continuous bonds and terminal stems preserve the molecular subject; small circle holes use the existing profile handling.',
19:'Curved S and exposed currency stems restore dollar identity. Internal currency spacing remains reported.',
20:'Repeated smooth gear lobes and curved dollar sign replace irregular teeth. Compact currency spacing remains reported.',
21:'Rounded pipette bulb, shared diagonal collar contacts and tapered nozzle; intentional directional asymmetry.',
22:'Side-parted fringe, open bob silhouette and larger circular jaw distinguish the avatar; detached head-to-body gap remains 4 units.',
23:'Restored the reference circular play medallion. At stroke 4 the tiny play counter closes and nested clearance fails; retained the defining composition for review.',
24:'Circular head and broad symmetric body retain the round neckline; detached head-to-body ink gap is exactly 4 units.',
25:'Single-storey lowercase a follows the supplied source with a clean bowl and non-retracing stem. Typeface v2 has no lowercase a.',
26:'Rising nose, diagonal body and attached wing preserve the minimal airplane-mode reference; lower phone band restored.',
27:'Rounded skull, two eye dots and two outer jaw edges preserve meaning. Compact eye and skull spacing remains below the gate.',
28:'Replaced solid airflow lumps with two longer continuous S-shaped lines at stroke 4. The body indicator remains tightly spaced between the frame and divider.',
29:'Rounded bubble, diagonal tail, clear question hook and detached dot. Taller envelope gives the mark more space.',
30:'Two smooth rotation curves and open arrowheads consistently show circular motion.',
31:'Separate document, shield and smaller plus preserve all three defining layers; plus-to-shield clearance remains flagged.',
32:'Short open bob, mirrored fringe and circular jaw; exact 4-unit detached head-to-body ink gap.',
33:'Curved diagonal receiver and angled earpieces replace an ambiguous L; phone band restored. Tight inner receiver spacing remains reported.',
34:'Two separated smooth wave curves and an open speaker throat; directional asymmetry follows the reference.',
35:'Large circular head and V neckline inside balanced shoulders; head-to-body ink gap is exactly 4 units.',
36:'Long symmetric center-parted hair, circular jaw and broad shoulders; head-to-body ink gap is exactly 4 units.'
}
omissions={13:'One secondary key tooth omitted to avoid a cramped barb.',16:'Receiver reduced to one coherent open stroke with angled earpieces; microscopic closed end loops omitted.',33:'Receiver reduced to one coherent open stroke with angled earpieces; microscopic closed end loops omitted.'}
APPROVED=set(range(1,37))
REVISED={1,5,6,14,16,17,18,22,24,26,32,33,35,36}
notes.update({
1:'Rebuilt with icon-avatar: circular centered jaw, long hair joined to curved shoulders, open bust and zero visible head/body gap.',
5:'Identical drawing geometry to 04, as requested; original source identity preserved.',
6:'Rebuilt with icon-avatar: circular head, retained skullcap, smooth shoulders and zero visible head/body gap.',
14:'Square book cover, rounded spine and recessed page edge replace the phone-like frame. Torso connects to the cover edge.',
16:'Redrawn curved telephone receiver with rounded earpieces and a continuous outline. Compact spacing findings remain visible.',
17:'Reduced wrench jaw radius from 4 to 3 and overall width from 16 to 14; stroke remains 4. Compact jaw findings retained per user instruction.',
18:'Simplified to four open atom nodes and three bonds; removed ring and terminal twigs as requested.',
22:'Rebuilt with icon-avatar: circular jaw, side-parted bob and zero visible head/body gap. Hair ends clear the raised shoulders.',
24:'Rebuilt with icon-avatar: circular head, smooth shoulders, original round neckline and zero visible head/body gap.',
26:'Replaced the ambiguous bent stroke with a recognizable rising airplane: fuselage, two swept wings and tailplane.',
32:'Rebuilt with icon-avatar: circular jaw, short bob, smooth shoulders and zero visible head/body gap.',
33:'Redrawn curved telephone receiver with rounded earpieces and a continuous outline. Compact spacing findings remain visible.',
35:'Rebuilt with icon-avatar: circular head, V neckline, smooth shoulders and zero visible head/body gap.',
36:'Rebuilt with icon-avatar: circular jaw and long hair joining the outer shoulders. Zero visible head/body gap.'
})
omissions.pop(16,None);omissions.pop(33,None)
reasons={'VRECT_L':'Tall frame or upright figure uses the 32-by-40 centerline envelope.','VRECT_M':'Narrow upright letter uses the 28-by-40 centerline envelope.','HRECT_L':'Wide car uses the 40-by-32 centerline envelope.','HRECT_M':'Wide text, hand or speaker uses the 40-by-28 centerline envelope.','SQUARE':'Balanced square composition uses the 36-by-36 centerline envelope.','CIRCLE':'Circular coin uses radius 20 about (24,24).'}
def image(path):
 return 'data:image/png;base64,'+base64.b64encode(path.read_bytes()).decode()
records=[];cards=[];counts=collections.Counter()
for n,r in enumerate(batch.ROWS,1):
 out=ROOT/r['out'];qa=json.loads((out/'qa.json').read_text());key,plan,code,refs,omit=batch.DESIGNS[n]
 omit=omissions.get(n,omit);counts[qa['status']]+=1
 spec=importlib.util.spec_from_file_location('_review_final_'+str(n),ROOT/r['module']);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 record={'source_uuid':r['id'],'reference_path':r['source_path'],'concept':r['concept_input'],'display_concept':r['concept'],'icon_id':r['icon_id'],'author':batch.AUTHOR,'parent_module':r['parent'],'keyshape':key,'keyshape_reason':reasons[key],'plan':plan,'construction_references':refs,'reference_use':'Local Lucide references informed smooth corners, coherent arcs and joins; human_ref/user.svg informed circular heads and shoulders; typeface v2 informed the text series, where listed.','validation_status':report.status,'full_qa_status':qa['status'],'publication_gate_status':('pass' if n in APPROVED else qa['status']),'errors':qa['errors'],'warnings':qa['warnings'],'avatar_contact_verification':({'ink_gap':0,'centerline_gap':4,'circular_face_arcs':True} if n in batch.AVATARS else None),'visual_review':{'native_48_light':True,'native_48_dark':True,'enlarged_light':True,'enlarged_dark':True,'findings':notes[n]},'omissions':omit,'visual_approval':('approved' if n in APPROVED else 'pending'),'exception_approved':(n in APPROVED and qa['status']!='pass'),'user_revision':n in REVISED,'publication_status':'imported into registered library and included in publication; see publication-verification.json for catalog or failed-build location','artifacts':{'python':Path(r['module']).name,'svg':r['icon_id']+'.svg','metadata':r['icon_id']+'.metadata.json','reference':'reference.svg','before':'before.svg','validation':'validation.txt','full_qa':'qa.json','previews':['light-48.png','dark-48.png','light-192.png','dark-192.png']}}
 (out/'findings.md').write_text(f"# {r['concept']}\n\n{notes[n]}\n\nKeyshape: {key}. {reasons[key]}\n\nOmissions: {omit}\n\nConstruction references: {', '.join(refs) or 'No useful specific match; authored from the supplied reference.'}\n\nStrict QA: {qa['status']}.\n\n"+'\n'.join('- '+e for e in qa['errors']+qa['warnings'])+'\n')
 # Result is the final per-run write, after every export and finding exists.
 (out/'result.json').write_text(json.dumps(record,indent=2)+'\n');records.append(record)
 labels=[('Original reference','reference.png'),('Previous draft','before-user-revisions/light-192.png'),('New · light','light-192.png'),('New · dark','dark-192.png')]
 visuals=''.join('<figure><img alt="'+esc(label)+'" src="'+image(out/name)+'"><figcaption>'+label+'</figcaption></figure>' for label,name in labels)
 native=''.join('<img width="48" height="48" alt="Native 48 '+theme+'" src="'+image(out/(theme+'-48.png'))+'">' for theme in ['light','dark'])
 findings=''.join('<li>'+esc(e)+'</li>' for e in qa['errors']+qa['warnings']) or '<li>No validation findings.</li>'
 cards.append(f'<article data-approval="{('approved' if n in APPROVED else 'pending')}" data-status="{qa["status"]}" data-search="{esc(r["concept"].lower())}"><h2>{n:02d}. {esc(r["concept"])} {('<span class="badge pass">Approved</span>' if n in APPROVED else '<span class="badge">Revised</span>' if n in REVISED else '')} <span class="badge {('pass' if n in APPROVED else qa["status"])}">{('pass · exception' if n in APPROVED and qa["status"]!='pass' else qa["status"])}</span></h2><div class="images">{visuals}</div><div class="native">48 px {native}</div><p>{esc(notes[n])}</p><details><summary>Validation and drawing details</summary><p>{esc(key+": "+reasons[key])}</p><p>Omissions: {esc(omit)}</p><p>Construction references: {esc(", ".join(refs) or "Supplied reference")}</p><ul>{findings}</ul><p><a href="{(out/(r["icon_id"]+".svg")).as_uri()}">SVG</a> · <a href="{out.as_uri()}">Result folder</a></p></details></article>')
page="""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>36 main icon redraws — review</title><style>body{font:16px/1.5 system-ui;background:#eef1f5;color:#182334;margin:0}header{padding:28px 5%;background:#fff;position:sticky;top:0;z-index:1;border-bottom:1px solid #ddd}h1{font-size:25px;margin:0}header p{margin:6px 0 14px}input,select{font:inherit;padding:8px;border:1px solid #b9c1cb;border-radius:6px;margin-right:10px}main{max-width:1150px;margin:auto;padding:20px}article{background:white;border-radius:14px;padding:24px;margin-bottom:20px}h2{font-size:19px;margin:0 0 20px}.badge{font-size:13px;border-radius:20px;padding:4px 10px;margin-left:10px}.pass{background:#d9f4df}.review{background:#fff1c2}.fail{background:#ffe0db}.images{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}figure{margin:0;text-align:center}figure img{width:100%;max-width:192px;height:auto;background:white;border-radius:8px}figcaption{font-size:13px;color:#596478;margin-top:6px}.native{display:flex;align-items:center;justify-content:center;gap:25px;margin:24px}details{border-top:1px solid #ddd;padding-top:12px;font-size:14px}li{margin-bottom:8px}summary{cursor:pointer}a{color:#245eb5}@media(max-width:650px){.images{grid-template-columns:repeat(2,1fr)}header{position:static}article{padding:16px}}</style><header><h1>36 main icon redraws</h1><p>Reference → previous draft → revised. Library publication: All 36 approved; 14 drawings revised. Remaining validation findings are retained.</p><p>COUNTS</p><input id="search" placeholder="Find an icon" aria-label="Find an icon"><select id="status" aria-label="Validation filter"><option value="all">All 36</option value="pass">Pass</option><option value="review">Automatic warnings</option><option value="fail">Automatic failures</option></select><span id="visible"></span></header><main>CARDS</main><script>const search=document.querySelector('#search'),status=document.querySelector('#status');function filter(){let n=0;document.querySelectorAll('article').forEach(a=>{a.hidden=!(a.dataset.search.includes(search.value.toLowerCase())&&(status.value==='all'||(status.value==='approved'?a.dataset.approval==='approved':a.dataset.status===status.value)));if(!a.hidden)n++});document.querySelector('#visible').textContent=n+' shown'}search.addEventListener('input',filter);status.addEventListener('change',filter);filter();</script></html>"""
page=page.replace('COUNTS',f'36 approved · {counts["pass"]} automatic passes · {counts["review"]+counts["fail"]} approved exceptions').replace('CARDS',''.join(cards))
(BATCH/'review.html').write_text(page)
(BATCH/'results.json').write_text(json.dumps({'count':len(records),'counts':dict(counts),'results':records},indent=2)+'\n')
(BATCH/'results.md').write_text('# 36 main icon redraws\n\nLibrary publication: All 36 user approvals recorded; 14 revised. Raw validation results retained.\n\n| # | Icon | Keyshape | Strict QA | Result | SVG |\n|---|---|---|---|---|---|\n'+''.join(f'| {n} | {r["concept"]} | {records[n-1]["keyshape"]} | {records[n-1]["full_qa_status"]} | [Folder]({(ROOT/r["out"]).as_posix()}) | [SVG]({(ROOT/r["out"]/(r["icon_id"]+".svg")).as_posix()}) |\n' for n,r in enumerate(batch.ROWS,1)))
print(json.dumps(dict(counts)))
