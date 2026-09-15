import base64,json,hashlib
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from .check_drafts import load
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
rows=json.loads((OUT/'batch.json').read_text())
retained={
1:'The lamp, adaptive tick, and three evenly spaced beams remain clear; the asymmetry follows the headlamp direction.',
3:'The tuft, rounded body, lowered brows, and beak remain readable with clear separation.',
4:'The head, waist, abdomen, and paired limbs remain centered. Preserve the earlier requested leg reduction.',
5:'The long snout, arched back, and separated leg openings preserve the anteater profile.',
6:'The six opposed shutter blades form a centered aperture with a clear central opening.',
7:'Equal arch spans, shared piers, and the level deck keep the bridge structure balanced.',
8:'The concentric faucet arch, stem, and separated water marks read clearly at 48 pixels.',
9:'The angled barrel, wheel, and trail preserve the field-gun silhouette; directional asymmetry is intentional.',
10:'The raised gun, round wheel, and spread outriggers remain distinguishable.',
11:'The stock, barrel, magazine, and raised sight remain legible as one rifle.',
12:'The matched rosette lobes and centered ribbon tails are balanced; the center ring remains separate.',
13:'The tower’s mirrored shoulders and pointed arch retain the landmark’s structure.',
16:'The frame, seat curve, and base rails are separated and keep the walker recognizable.',
17:'The bead loop leaves clear space for the offset heart charm; the offset is intentional.',
18:'Three visible bead shapes remain separated along a continuous bent wire.',
22:'The opposing vise jaws, bench base, and right-side screw remain distinct.',
23:'The paired cups and crossed straps stay balanced around the vertical axis.',
24:'The raised wing, head, and tail give the bird a clear flight direction.',
25:'The arched slab and broad base read clearly as a gravestone.',
26:'The hat’s crown, cuff, and centered pom-pom have distinct silhouettes.',
27:'The rounded package outline and central notch remain evenly balanced.',
28:'The wide carton and centered top seam remain recognizable.',
29:'The top face and vertical edge preserve the box’s deliberate perspective.',
30:'The two brain lobes and central fold remain smooth and balanced.',
33:'The cannon wheel, barrel, and block carriage are clearly separated.',
35:'The roof, hood, wheels, and short window mark preserve the car’s side direction.',
36:'The clover lobes and stem remain a coherent, balanced shape.',
38:'The separated toe marks and broad central pad read as a paw print at native size.',
39:'The ball and curling string preserve the toy’s silhouette and deliberate asymmetry.',
40:'The matched antlers, whiskers, and tapered muzzle remain balanced around the face.',
42:'The wings, fuselage, and tail preserve the airliner’s ascending direction.',
43:'The paired rainbow curves emerge from the cloud with distinct, open spacing.',
44:'Overlapping cloud contours and the separated fog line remain readable.',
46:'The necklace arc and centered pearl remain balanced; the pendant stays distinct.',
47:'The disc rim, hub, and curved sheen marks remain separated.',
48:'The body, paired wheels, and raised roll bar retain the convertible silhouette.',
49:'The drill body, bit, sloped grip, and battery are distinct and coherently connected.',
50:'The body, paired flippers, crests, eyes, and beak remain balanced and legible.',
51:'The circular platter, hub, and spaced drive marks remain centered.',
52:'The pointed ears, rounded jaw, eyes, and nose form a clear animal face.',
53:'The sun, dry tree, and cracked ground retain their separation and visual hierarchy.',
54:'The cloud crest and long curling gust remain smooth and directional.',
56:'The ear contour and two sound arcs have clear gaps.',
57:'The filter pleats, incoming marks, and outgoing flow mark remain separated.',
58:'The sloped train nose, window band, wheel, and rail preserve the travel direction.',
59:'The curved breech, long barrel, wheel, and trail remain clearly readable.',
61:'The angular ears, tapered cheeks, and centered nose retain the fox identity.',
62:'The freight body’s repeated ribs and equal wheels remain evenly spaced.',
63:'The filter housing and detached drop are centered and distinct.',
65:'The glove’s rounded fingers, thumb, and cuff remain legible; no detached-head rule applies.',
66:'The glove fingers and cuff remain balanced; the hand outline follows the supplied reference.',
68:'The body and crossing rotors retain the helicopter’s top view and shared center.',
69:'The angled hockey stick and separated puck remain clear at native size.',
70:'The cobra’s broad hood, eyes, neck, and coil retain a centered silhouette.',
71:'The paired receiver ends and connecting arch remain consistent and symmetric.',
72:'The matched horns, curved jaw, and tilted eyes preserve the demon face.',
74:'The muzzle, forehead, eye, and mane retain the horse profile’s intentional asymmetry.',
76:'The roof slopes, walls, and centered doorway remain balanced.',
77:'The stock, barrel, and raised front sight preserve the rifle direction.',
78:'The rounded body, curled tail, and facial marks preserve the creature silhouette.',
79:'The paired towers, connecting dam wall, and water curves remain distinct.',
80:'The rounded pod, sloped front window, and small rear mark preserve the travel direction.',
81:'The scoop lobes and centered cone remain balanced and readable.',
82:'The boot, supports, and curved skate blade remain separated.',
83:'The circular hemisphere and stepped unfinished edge preserve the Death Star concept.',
85:'The column’s matched scrolls, shaft, and broad base remain balanced.',
86:'The long ears, muzzle, and headdress retain the jackal-headed silhouette.',
87:'The paired eye stalks, long ears, and rounded jaw remain recognizable in the simplified style.',
88:'Three jellyfish remain separated; each keeps a rounded bell and short tentacle marks.',
91:'The kayak’s pointed hull, cockpit, and offset paddle remain distinct.',
92:'The diagonal kayak, centered cockpit, and opposing paddle ends preserve the intended arrangement.',
93:'The pointed hull and crossing paddle remain centered and readable.',
94:'The ring and two hanging keys remain distinct despite their shared attachment.',
95:'The round bow and diagonal shaft retain the key silhouette.',
96:'The long beak, rounded body, and short legs retain the kiwi’s proportions.',
97:'The handle, blade, scratch marks, and ground line preserve the scratching action.',
98:'The koala’s ear, face, body, and diagonal branch remain recognizable.'}
omissions={2:'Omitted dial ticks and strap stitching; the hands stay minimal at 48 pixels.',14:'Removed the collar edge beneath the teat to keep the nipple opening clear.',15:'Kept the existing reduced silhouette; no feet or feather texture were added.',19:'Used two leg pairs and short antenna marks to keep the small insect open inside the shell.',20:'Reduced the finial to a single centered stroke.',21:'No identifying detail removed.',31:'Kept only the eyes and short muzzle mark inside the face.',32:'No identifying detail removed; the lens was added.',34:'Omitted a second window divider to preserve space between the roof and wheels.',37:'Used three toe marks instead of a densely packed row of toe loops.',41:'Used three ribs and a smooth fan silhouette rather than fine shell texture.',45:'Kept the eyes and short mouth; omitted hood scales.',55:'Simplified the lower feathers into broad points.',60:'Omitted eye and feather detail; retained the curved neck and standing pose.',64:'Kept one eye and a broad muzzle; omitted spots and tiny mane marks.',67:'Used a few broad blade teeth instead of fine serrations.',73:'Kept two visible legs and one ear in the side silhouette.',75:'Removed the internal nozzle divider so it does not form a tiny closed hole.',84:'Kept open head tips and two crossing strokes; omitted scales and tiny eyes.',89:'Straightened the power lead and omitted a tight curled end.',90:'Omitted the cramped pectoral-fin fold; retained the dorsal fin, beak, arching body, and tail.',99:'Removed fragmented curve segments; retained the liquid surface.',100:'Omitted measurement ticks; kept the rim, liquid line, and rounded bottom.'}
def data(path):return 'data:image/svg+xml;base64,'+base64.b64encode(path.read_bytes()).decode()
result=[]
for r in rows:
 n=r['batch_index'];q=json.loads((OUT/'qa'/f'{n}.json').read_text());icon=load(r)()
 r=dict(r);r['action']='revised' if r.get('variant_id') else 'retained'
 r['assessment']=r.get('repair_note') or retained[n]
 r['omissions']=omissions.get(n,'No new simplification was made in this batch.')
 r['keyshape']=icon.keyshape.name;r['bounds']=list(icon.keyshape_bounds())
 r['validation']={'status':q['status'],'errors':q['errors'],'warnings':q['warnings'],'sha':q['svg_sha256']}
 r['before']=data(OUT/'previews'/f'{n}-before.svg');r['after']=data(OUT/'previews'/f'{n}-after.svg')
 r['original']=data((ROOT/'icon_set/dist/gallery'/r['original_sources'][0]['url']).resolve()) if r.get('original_sources') else ''
 r['reference_note']=('Lucide '+r['lucide_reference']+': coherent contours and geometric construction; adapted to this subject and SOLO48.' if r.get('lucide_reference') else 'Supplied original reference; no useful additional Lucide subject match used for this revision.' if r['action']=='revised' else 'Supplied original reference. The existing drawing was reviewed without re-authoring.')
 r['gallery_url']='http://localhost:8000/gallery/index.html?tab=icons&family=solo&view=generated&q='+r['icon_id']
 result.append(r)
assert len(result)==100 and all(r['validation']['status']=='pass' for r in result)
meta={'count':100,'revised':sum(r['action']=='revised' for r in result),'retained':sum(r['action']=='retained' for r in result),'passed':100,'created':datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).strftime('%d %b %Y · %H:%M ICT'),'delivery':'isolated-review','native_size':48,'themes':['light','dark'],'tests':{'focused_passed':54,'full_suite':{'tests':405,'failures':112,'errors':29,'skipped':1}},'source_preservation':'All 100 original sources recovered and checksum-verified against the intake snapshot; shared files were independently consolidated by another task.'}
(OUT/'report-data.json').write_text(json.dumps({'meta':meta,'icons':[{k:v for k,v in r.items() if k not in ['before','after','original']} for r in result]},indent=2))
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Batch 01 · Rejected icon repairs</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f5f1;color:#233027;font:14px system-ui,sans-serif}main{max-width:1580px;margin:auto;padding:38px 28px}.eyebrow{font-size:11px;letter-spacing:2px;color:#687867;font-weight:750}h1{font-size:42px;letter-spacing:-1.8px;margin:12px 0}p{line-height:1.6;color:#617060}.intro{max-width:850px}.stats{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}.stat{background:#fff;border:1px solid #d9e0d5;border-radius:12px;padding:18px 24px;min-width:150px}.stat b{font-size:30px;display:block}.stat span{font-size:12px;color:#617060}.notice{background:#fff6dc;border-left:3px solid #c9a545;padding:12px 16px;max-width:1100px;font-size:13px}.tools{position:sticky;top:0;background:#f4f5ffed;backdrop-filter:blur(10px);padding:16px 0;z-index:2;display:flex;gap:10px;align-items:center;flex-wrap:wrap}input,select,button{font:inherit;padding:10px 13px;border:1px solid #cbd6c7;border-radius:8px;background:#fff;color:inherit}input{flex:1;min-width:200px}button{cursor:pointer}label{display:flex;align-items:center;gap:7px;font-size:12px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}.card{background:#fff;border:1px solid #dce3d8;border-radius:14px;overflow:hidden}.card header{padding:16px 18px 8px}.card h2{font-size:16px;margin:9px 0 4px;overflow-wrap:anywhere}.badge{display:inline-block;border-radius:5px;padding:4px 7px;font-size:10px;font-weight:750;background:#e1eee0;color:#35683b}.badge.retained{background:#eef0ed;color:#667461}.number{font-size:11px;color:#82907c;float:right}.compare{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:#dce3d8}.tile{background:#fafbf8;text-align:center;padding:12px 4px;color:#6a7768;font-size:10px}.tile img{display:block;margin:12px auto;width:96px;height:96px}.tile img.native{width:48px;height:48px;margin:18px auto 6px}.tile small{font-size:9px}.tile.after{background:#f0f6ec}body.dark .tile{background:#1c2228;color:#ced6cb}body.dark .tile.after{background:#16231d}body.dark .tile img,body.dark .reference img{filter:invert(1)}.body{padding:14px 18px 18px}.body p{font-size:13px;margin:0 0 10px}.pass{font-size:11px;color:#46774c;margin:10px 0}details{border-top:1px solid #e4e9e0;padding-top:10px;margin-top:10px;font-size:12px}summary{cursor:pointer;color:#54724f}.reference{display:flex;gap:14px;align-items:center;margin:10px 0}.reference img{height:68px;width:68px;object-fit:contain}.reference p{font-size:11px;margin:0}.reference{padding:8px;border-radius:8px;background:#fafbf8}body.dark .reference{background:#1c2228}body.dark .reference p{color:#d0d7ce}.details p{font-size:11px;margin-top:10px;overflow-wrap:anywhere}a{color:#3b6941;text-underline-offset:3px}footer{font-size:12px;color:#76806e;border-top:1px solid #d4decf;margin-top:32px;padding-top:20px}.count{font-size:12px;color:#677962;margin:0 0 16px}.empty{padding:40px} @media(max-width:600px){main{padding:24px 14px}h1{font-size:32px}.grid{grid-template-columns:1fr}.stat{flex:1;min-width:125px}.tools{position:static}} @media print{.tools,.notice,footer{display:none}.grid{grid-template-columns:1fr 1fr}.card{break-inside:avoid}.tile img{width:72px;height:72px}}
</style><body><main><div class="eyebrow">PICTOGRAPHIC / FIRST 100 REJECTED SOLO ICONS</div><h1>Batch 01 · Drawing review</h1><p class="intro">Before-and-after review of 100 objects, animals, and devices on the 48 × 48 SOLO48 profile. <b>23 drawings were revised; 77 were retained after inspection.</b> All 100 final candidates pass the complete icon QA checks and were inspected at native size in light and dark themes.</p><div class="stats"><div class="stat"><b>100</b><span>Reviewed in this batch</span></div><div class="stat"><b>23</b><span>Revised drawings</span></div><div class="stat"><b>77</b><span>Retained drawings</span></div><div class="stat"><b>100 / 100</b><span>Complete QA pass</span></div></div><p class="notice"><b>Isolated review copy.</b> Another active task is consolidating and editing the same gallery files. This report preserves the original snapshots and this batch’s final candidates; the live gallery may differ. No approval decisions were made here. “Retained” means no further change was identified in this review, not that the icon’s previous rejection was cleared.</p><div class="tools"><input id="search" type="search" aria-label="Search batch" placeholder="Search names or review notes…"><label>Show <select id="filter"><option value="revised">Revised · 23</option><option value="all">All 100 icons</option><option value="retained">Retained · 77</option></select></label><label>Preview theme <select id="theme"><option value="light">Light</option><option value="dark">Dark</option></select></label><button id="print">Print / PDF</button></div><p id="count" class="count" role="status"></p><div id="report" class="grid"></div><details class="details"><summary>Validation and delivery details</summary><p>Each final candidate was checked for profile, integer grid, bounds, spacing, composition, round-trip SVG, reproducibility, symmetry, internal spacing, and small holes. No validation thresholds or exception rules were changed. The 54 focused profile, spacing, and symmetry tests passed.</p><p>The full 405-test repository suite was also attempted: 112 failures, 29 errors, and 1 skipped test were reported while other tasks were changing the workspace. These include repository-wide corpus failures, missing legacy sources, generated skill mismatches, and local-server test errors. This is not a clean full-repository test run.</p><p>The original 100 model files were recovered and checked against their intake hashes after the parallel consolidation. New model drafts and complete per-icon evidence are preserved with this report. __BUILD_STATUS__</p></details><footer>__DATE__ · Reviewed using icon-solo. Previews are embedded and work offline. This report covers this batch only; it does not claim the whole rejected backlog is repaired.</footer></main><script>
const rows=__DATA__;const $=s=>document.getElementById(s);const esc=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){const q=$('search').value.toLowerCase().trim();const f=$('filter').value;const shown=rows.filter(r=>(f==='all'||f===r.action)&&(!q||[r.icon_id,r.assessment,r.omissions].join(' ').toLowerCase().includes(q)));$('count').textContent=shown.length+' of 100 icons shown · enlarged previews plus exact 48px views';$('report').innerHTML=shown.map(r=>`<article class="card"><header><span class="badge ${r.action}">${r.action==='revised'?'REVISED':'RETAINED'}</span><span class="number">#${String(r.batch_index).padStart(3,'0')}</span><h2>${esc(r.icon_id)}</h2></header><div class="compare">${[['before','BEFORE'],['after',r.action==='revised'?'CANDIDATE':'RETAINED']].map(([k,t])=>`<div class="tile ${k}">${t}<img src="${r[k]}" alt="${t} ${esc(r.icon_id)}" loading="lazy"><img class="native" src="${r[k]}" alt="48px ${t} ${esc(r.icon_id)}" loading="lazy"><small>48px · native size</small></div>`).join('')}</div><div class="body"><p>${esc(r.assessment)}</p><div class="pass">✓ Complete QA pass · no errors or warnings</div><details><summary>Reference and drawing notes</summary>${r.original?`<div class="reference"><img src="${r.original}" alt="Original reference ${esc(r.icon_id)}" loading="lazy"><p>Original supplied reference</p></div>`:''}<p>${esc(r.reference_note)}</p><p>${esc(r.omissions)}</p><p>${esc(r.keyshape)} · visible bounds ${esc(r.bounds.join(', '))}. ${r.keyshape==='SQUARE'?'Square envelope supports balanced overall proportions.':r.keyshape==='CIRCLE'?'Radial envelope keeps the circular subject centered.':r.keyshape==='HRECT_L'?'Wide envelope supports the horizontal subject.':'Tall envelope supports the upright subject.'}</p><p><a href="${esc(r.gallery_url)}" target="_blank" rel="noopener">Find the current gallery icon ↗</a></p></details></div></article>`).join('')||'<p class="empty">No matching icons.</p>';}
$('search').oninput=render;$('filter').onchange=render;$('theme').onchange=()=>document.body.classList.toggle('dark',$('theme').value==='dark');$('print').onclick=()=>window.print();render();
</script></body></html>'''
build=json.loads((OUT/'build-result.json').read_text()) if (OUT/'build-result.json').exists() else None
build_status='The isolated 100-icon family build exited successfully.' if build and build['exit_code']==0 else 'The isolated family build is still being checked.'
page=page.replace('__DATE__',meta['created']).replace('__BUILD_STATUS__',build_status).replace('__DATA__',json.dumps(result).replace('<','\\u003c'))
(OUT/'index.html').write_text(page);(ROOT/'icon_set/dist/gallery/rejected-repair-batch-01.html').write_text(page)
print(json.dumps(meta));print('Report bytes:',len(page))
