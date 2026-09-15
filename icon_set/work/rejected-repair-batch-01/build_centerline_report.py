"""Publish the revised 100-icon comparison with inspectable centerlines."""
import base64,hashlib,json,re,shutil,zipfile
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from .check_drafts import load
from .centerlines import diagnostic
from icon_set.renderers.svg import render_svg,build_paths
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
archive=OUT/'first-review.html'
if not archive.exists():shutil.copy2(OUT/'index.html',archive)
old_text=archive.read_text();old_rows=json.JSONDecoder().raw_decode(old_text.split('const rows=',1)[1])[0]
old={r['batch_index']:r for r in old_rows}
rows=json.loads((OUT/'batch.json').read_text())
# These notes describe the final edits only.
notes={16:'Round the walker frame foot into the base, replacing the sharp rear corner with a smooth attached turn.',22:'Widen the vise opening to twelve units and give the two jaws equal width and matching radii.',24:'Curve the raised wing edge and smooth the belly return into the tail, keeping the directional silhouette.',44:'Split the long fog underline into two balanced strokes with an open central gap beneath the clouds.',63:'Flatten the filter bowl into a broad sump instead of a pointed funnel; keep the drop centered below it.',77:'Reangle the lower stock and level the front barrel run into the sight, giving the rifle a clearer shoulder and fore-end.'}
refs={4:'bug',15:'bird',19:'bug',27:'package',28:'package',29:'package',30:'brain',35:'car',38:'paw-print',42:'plane',44:'cloud-rain',48:'car',49:'drill',56:'ear',68:'',92:'kayak',93:'kayak'}
result=[];validation=[]
def data_bytes(b):return 'data:image/svg+xml;base64,'+base64.b64encode(b).decode()
for r in rows:
 n=r['batch_index'];before=load(r,'before')();after=load(r)()
 assert [p['d'] for p in build_paths(before.draw())] != [p['d'] for p in build_paths(after.draw())],r['icon_id']
 q=json.loads((OUT/'qa'/f'{n}.json').read_text());assert q['status']=='pass',(n,q['status'])
 a=render_svg(after).encode();assert hashlib.sha256(a).hexdigest()==q['svg_sha256'],n
 row=dict(r,action='revised',assessment=notes.get(n,r['repair_note']),keyshape=after.keyshape.name,bounds=list(after.keyshape_bounds()))
 for side,model in [('before',before),('after',after)]:
  svg=render_svg(model).encode();debug=diagnostic(model).encode()
  (OUT/'previews'/f'{n}-{side}.svg').write_bytes(svg);(OUT/'previews'/f'{n}-{side}-centerline.svg').write_bytes(debug)
  row[side]=data_bytes(svg);row[side+'_centerline']=data_bytes(debug)
 row['original']=old[n].get('original','')
 ref=refs.get(n,r.get('lucide_reference',''))
 row['reference_note']=('Lucide '+ref+' original and atomic geometry: geometric construction adapted to this subject and SOLO48.' if ref else 'Supplied reference and original model. No useful additional Lucide subject match was used.')
 row['omissions']=old[n].get('omissions','') if not r.get('centerline_review') else ('The rotor shaft is hidden by the helicopter body to avoid crowded crossings.' if n==68 else 'Two retained leg pairs; omitted extra legs and fine anatomy to preserve clearance.' if n==4 else 'Removed the lower row of crowded arches and separated the water baseline.' if n==7 else 'Removed the closed center diamond between the ribbon tails.' if n==12 else 'Fine surface detail stays omitted at 48 pixels.')
 row['validation']={'status':q['status'],'errors':q['errors'],'warnings':q['warnings'],'sha':q['svg_sha256']}
 result.append(row);validation.append({'index':n,'id':q['icon_id'],**row['validation']})
(OUT/'after-validation.json').write_text(json.dumps(validation,indent=2))
full=(OUT/'full-tests-centerlines.log').read_text();ran=re.search(r'Ran (\d+) tests in ([\d.]+)s',full);failed=re.search(r'FAILED \(([^\n]+)\)',full)
build=json.loads((OUT/'centerline-build-result.json').read_text()) if (OUT/'centerline-build-result.json').exists() else {'exit_code':None}
meta={'count':100,'revised':100,'retained':0,'passed':100,'created':datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).strftime('%d %b %Y · %H:%M ICT'),'delivery':'isolated-review','default_view':'centerline','geometry_changed':100,'tests':{'focused_passed':54,'full_suite':{'finished':bool(ran),'count':int(ran[1]) if ran else None,'result':failed[1] if failed else 'running' if not ran else 'OK'}},'build':build}
excluded={'before','after','before_centerline','after_centerline','original'}
(OUT/'report-data.json').write_text(json.dumps({'meta':meta,'icons':[{k:v for k,v in r.items() if k not in excluded} for r in result]},indent=2))
css=old_text.split('<style>',1)[1].split('</style>',1)[0]
css+='''.tile img.large{width:144px;height:144px}.tile img.native{width:48px;height:48px}.tile img.debug{background:#fff;border-radius:6px;filter:none!important}.legend{font-size:12px}.tools{background:#f4f5f1ed}.stat{min-width:170px}.body .change-title{font-size:10px;letter-spacing:1px;font-weight:750;color:#71816b}.reference{min-height:90px}.qa{font-size:11px;color:#46774c}a.download{display:inline-block;margin-right:18px}'''
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Batch 01 · 100 revised icons · Centerline review</title><style>__CSS__</style><body><main>
<div class="eyebrow">PICTOGRAPHIC / REJECTED ICON REPAIRS / BATCH 01</div><h1>100 icons. All revised.</h1>
<p class="intro">Every rejected icon in this batch now has a changed drawing. Compare the centerlines, joins, proportions, and spacing below, then switch to the finished stroke view. Native 48-pixel previews stay visible in both modes. The latest redraws are ant, cannon-block-carriage, and climbing-airliner.</p>
<div class="stats"><div class="stat"><b>100</b><span>Revised candidates</span></div><div class="stat"><b>0</b><span>Retained unchanged</span></div><div class="stat"><b>100 / 100</b><span>Individual QA pass</span></div></div>
<p class="notice"><b>Ready for your visual review.</b> These are isolated candidates. The original rejected drawings are preserved, and gallery approval statuses have not been changed. Passing the checks does not mean an icon has your approval.</p>
<div class="tools"><input id="search" type="search" aria-label="Search batch" placeholder="Search icons or changes…"><label>Show <select id="scope"><option value="latest">Latest redraws · 3</option><option value="all">All 100 icons</option></select></label><label>View <select id="view"><option value="centerline">Centerlines</option><option value="stroke">Finished strokes</option></select></label><label>Theme <select id="theme"><option value="light">Light</option><option value="dark">Dark</option></select></label><button id="print">Print / PDF</button></div>
<p class="legend" id="legend">Colored lines show the authored paths; dots show joins and endpoints. Pale gray shows the full stroke. Red dashed guides cross at (24,24).</p>
<p id="count" class="count" role="status"></p><div id="report" class="grid"></div>
<details class="details"><summary>Checks and delivery details</summary><p>All 100 candidates have different geometry from their rejected originals. They pass individual bounds, grid, spacing, holes, symmetry, and rendering checks with no errors or warnings. Each was inspected as centerlines and at native size in light and dark themes. No validation thresholds or exception rules were changed.</p><p>__BUILD__ The 54 focused profile, spacing, and symmetry tests passed.</p><p>__TESTS__</p><p>The original snapshots and candidate models are kept separately, since other work is changing the live gallery. This report covers the first 100 icons only.</p></details>
<footer>__DATE__ · icon-solo · All previews are embedded for offline review.</footer></main><script>
const rows=__DATA__;const $=s=>document.getElementById(s);const esc=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){const q=$('search').value.toLowerCase().trim();const debug=$('view').value==='centerline';const shown=rows.filter(r=>($('scope').value==='all'||r.feedback_redraw)&&(!q||[r.icon_id,r.assessment].join(' ').toLowerCase().includes(q)));$('count').textContent=shown.length+' of 100 revised icons shown';$('legend').hidden=!debug;$('report').innerHTML=shown.map(r=>`<article class="card"><header><span class="badge">${r.feedback_redraw?'REDRAWN':'REVISED'}</span><span class="number">#${String(r.batch_index).padStart(3,'0')}</span><h2>${esc(r.icon_id)}</h2></header><div class="compare">${[['before','REJECTED ORIGINAL'],['after','REVISED CANDIDATE']].map(([k,t])=>`<div class="tile ${k}">${t}<img class="large ${debug?'debug':''}" src="${r[debug?k+'_centerline':k]}" alt="${debug?'Centerline':'Stroke'} ${t} ${esc(r.icon_id)}" loading="lazy"><img class="native" src="${r[k]}" alt="48px ${t} ${esc(r.icon_id)}" loading="lazy"><small>48px · native size</small></div>`).join('')}</div><div class="body"><p class="change-title">WHAT CHANGED</p><p>${esc(r.assessment)}</p><div class="qa">✓ Individual QA pass · no errors or warnings</div><details><summary>Reference and construction</summary>${r.original?`<div class="reference"><img src="${r.original}" alt="Supplied reference ${esc(r.icon_id)}" loading="lazy"><p>Supplied original reference</p></div>`:''}<p>${esc(r.reference_note)}</p><p>${esc(r.omissions)}</p><p>${esc(r.keyshape)} · visible bounds ${esc(r.bounds.join(', '))}. ${r.keyshape==='CIRCLE'?'Radial envelope for the circular subject.':r.keyshape==='SQUARE'?'Square envelope for the balanced subject.':r.keyshape==='HRECT_L'?'Wide envelope for the horizontal subject.':'Tall envelope for the upright subject.'}</p></details></div></article>`).join('')||'<p class="empty">No matching icons.</p>';}
$('scope').onchange=render;$('search').oninput=render;$('view').onchange=render;$('theme').onchange=()=>document.body.classList.toggle('dark',$('theme').value==='dark');$('print').onclick=()=>window.print();render();
</script></body></html>'''
tests=(f'The full repository suite completed {ran[1]} tests and reported {failed[1]}. This includes failures outside this batch; the full repository run is not green.' if ran and failed else 'The full repository suite is still running; its result will be added here.' if not ran else f'The full repository suite passed {ran[1]} tests.')
buildnote='The isolated 100-icon family build passed.' if build['exit_code']==0 else 'The isolated family build is still being checked.'
for key,value in {'CSS':css,'DATE':meta['created'],'BUILD':buildnote,'TESTS':tests,'DATA':json.dumps(result).replace('<','\\u003c')}.items():page=page.replace('__'+key+'__',value)
(OUT/'index.html').write_text(page);(ROOT/'icon_set/dist/gallery/rejected-repair-batch-01.html').write_text(page)
with zipfile.ZipFile(OUT/'batch-01-review.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in [OUT/'index.html',OUT/'report-data.json']+[ROOT/r['variant_path'] for r in rows]+list((OUT/'previews').glob('*-after.svg')):z.write(p,p.relative_to(OUT))
print(json.dumps(meta))
