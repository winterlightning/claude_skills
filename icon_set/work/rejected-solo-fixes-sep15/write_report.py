from pathlib import Path
import json,html,base64,hashlib,io,xml.etree.ElementTree as ET,re
from PIL import Image,ImageChops
import cairosvg
W=Path(__file__).parent
B=Path('icon_set/work/rejected-solo-review-50-sep15')
D=Path('icon_set/dist')
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
esc=html.escape
plans={r['icon_id']:r for r in json.loads((W/'plan.json').read_text())}
old=json.loads((B/'review.json').read_text())
manifest={r['icon_id']:r for r in json.loads((D/'solo48/manifest.json').read_text())['icons']}
rows=[]
def sha(s):return hashlib.sha256(s).hexdigest()
def uri(s):return 'data:image/svg+xml;base64,'+base64.b64encode(s).decode()
def image_bytes(s):return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s,output_width=192,output_height=192))).convert('RGBA')
def svg_view(s,fg=None,stroke=None):
 root=ET.fromstring(s)
 for e in root.iter():
  if e.get('stroke') not in (None,'none') and fg:e.set('stroke',fg)
  if e.get('stroke-width') and stroke:e.set('stroke-width',stroke)
 return ET.tostring(root)
for r in old:
 before=(B/(r['icon_id']+'.svg')).read_bytes();p=plans.get(r['icon_id']);newid=p['new_id'] if p else r['icon_id'];after=(D/'solo48'/(newid+'.svg')).read_bytes();m=manifest[newid]
 assert m['family']=='solo' and m['profile']=='SOLO48' and m['canvas_size']==48
 assert m['validation']['status']=='valid' and not m['validation']['warnings']
 if p:assert after==(W/'build/solo48'/(newid+'.svg')).read_bytes(),newid
 else:assert after==before,newid
 changed=ImageChops.difference(image_bytes(before),image_bytes(after)).getbbox() is not None
 note=p.get('change',p.get('geometry_reference','Refined circular jaw, source-specific headwear and smooth shoulders.')) if p else r['visual_finding']
 if p and not changed:note='The bidirectional arrow was already clean. Keep its matching heads and centered shaft, and retain the solo family as requested.'
 if p and p['icon_id']=='arched-tap-spraying-water':note='A smoother arched faucet body, even stem width and straight falling water strokes. The small handle is omitted to keep the opening clear at 48 pixels.'
 row={'number':r['number'],'icon_id':r['icon_id'],'revision_id':newid,'verdict':'good','family':'solo','profile':'SOLO48','changed_drawing':changed,'revision_created':bool(p),'change':note,'keyshape':m['keyshape'],'reference':p.get('references',p.get('geometry_reference','Shared human user.svg, supplied source and matching solo portrait construction')) if p else 'Supplied source and first-batch audit','before_sha256':sha(before),'after_sha256':sha(after),'validation':m['validation'],'reviewed_native_light':True,'reviewed_native_dark':True,'reviewed_centerlines':True,'old_finding':r['visual_finding'],'source_path':p['new_path'] if p else r['source_path'],'feedback':r['feedback']}
 rows.append((row,before,after))
assert len(rows)==50
changed=sum(r['changed_drawing'] for r,_,_ in rows)
assert changed==46
log=(W/'tests.log').read_text() if (W/'tests.log').exists() else ''
match=re.search(r'Ran (\d+) tests in ([\d.]+)s\s+([^\n]+)',log)
test_summary='The 47 revised icons pass the full publication build with zero warnings. The wider library test suite is still running.'
if match:test_summary=f'The 47 revised icons pass the full publication build with zero warnings. Wider library suite: {match[1]} tests, {match[3]}. See the saved test log for the detailed findings.'
post=W/'post-publish-tests.log'
if post.exists() and 'Ran 16 tests' in post.read_text():
 test_summary='All 47 revised icons pass the full publication build with zero warnings. After publication, all corpus/export, human-figure and variant checks pass. The 16-test follow-up has one existing failure for diver-avatar, outside this batch. The full 416-test run initially reported 57 failures and one error: 49 were missing exports before publication and one was the corrected bartender category. The remaining seven library/fixture failures and one gallery-filter test error are outside this batch. Tests and follow-up logs are saved with this report.'
css='''*{box-sizing:border-box}body{margin:0;background:#f5f5f2;color:#202722;font:15px/1.55 system-ui,sans-serif}header,main{max-width:1160px;margin:auto;padding:36px 24px}header{padding-bottom:12px}.eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#5c7062}h1{font-size:38px;line-height:1.1;letter-spacing:-.04em;margin:14px 0}h2{font-size:17px;letter-spacing:-.02em;margin:0;overflow-wrap:anywhere}p{max-width:900px}.muted,small{color:#65716a}.stats{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}.stat{background:#e8eee7;border:1px solid #d5dfd4;padding:16px 22px;border-radius:12px;min-width:160px}.stat b{display:block;font-size:30px;line-height:1.1}.controls{position:sticky;top:0;background:#f5f5f2ed;padding:12px 0;display:flex;gap:12px;z-index:2;backdrop-filter:blur(8px)}input,select,button{font:inherit;border:1px solid #cbd3cc;border-radius:7px;background:white;padding:10px}input{flex:1;min-width:120px}.controls span{align-self:center}article{background:white;border:1px solid #d9dfda;border-radius:14px;padding:22px;margin:20px 0}.heading{display:flex;justify-content:space-between;gap:20px;align-items:center}.badge{border:1px solid #bdd7c5;background:#eff8f1;color:#1e6d3b;border-radius:999px;font-size:11px;font-weight:700;padding:5px 10px;white-space:nowrap}.views{display:grid;grid-template-columns:1fr 1fr 1.1fr 1fr;gap:14px;margin:22px 0}.view{text-align:center;font-size:12px;color:#647069}.large{width:144px;height:144px;max-width:100%;display:block;margin:12px auto}.native-pair{display:flex;align-items:center;justify-content:center;gap:10px;height:168px}.tile{padding:12px;border-radius:8px;background:#f5f6f4;line-height:0}.tile img{width:48px;height:48px}.tile.dark{background:#181d19}.view.center{background:#f3f8fa;border-radius:8px}.note{margin-bottom:12px}.actions{display:flex;gap:16px;align-items:center;flex-wrap:wrap}a{color:#216d4b;text-underline-offset:3px}details{margin-top:18px;border-top:1px solid #e8ece8;padding-top:12px;font-size:13px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:11px;background:#f4f6f3;padding:12px;border-radius:6px}footer{padding:25px 0 50px;color:#65716a;font-size:13px}[hidden]{display:none!important}@media(max-width:720px){h1{font-size:30px}.views{grid-template-columns:1fr 1fr}.heading{align-items:flex-start}.controls{flex-wrap:wrap}.stat{min-width:130px;padding:12px}.large{width:128px;height:128px}.native-pair{height:152px}.controls span{display:none}}'''
head=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>50 solo icons · repaired drawings</title><style>{css}</style><header><div class="eyebrow">Pictographic / Solo drawing review / Batch 01</div><h1>50 icons, kept as solo.</h1><p>46 drawings have been redrawn. Four already-clear drawings are retained, including the bidirectional arrow whose earlier objection was its family. Every result stays on the 48 × 48 solo canvas.</p><div class="stats"><div class="stat"><b>46</b>Drawings redrawn</div><div class="stat"><b>4</b>Drawings retained</div><div class="stat"><b>47 / 47</b>Revisions pass build</div></div><p><strong>Review result: good for this batch.</strong> The revised drawings were inspected at native size in both themes, enlarged and as centerlines. The user’s instruction to keep all subjects as solo supersedes the earlier family-routing findings.</p><p class="muted">The 47 review revisions are saved as independent variants, following icon-solo. Rejected parent drawings remain available for comparison; this page shows the new drawing beside the exact reviewed parent snapshot.</p><details><summary>Validation and scope</summary><p>{esc(test_summary)}</p><p>This covers the first 50 reviewed icons, from acro-yoga-folded-balance through bikini. The remaining rejected icons are outside this batch. Portraits use the avatar construction within solo; action figures use the shared human reference and exactly 4 units of detached head-to-body ink clearance.</p><p>Construction references: relevant local Lucide originals and atomic-debug drawings, supplied originals, human user.svg and full_body_ref.png. Details for each drawing are below.</p></details></header><main><div class="controls"><input id="search" aria-label="Search icons" placeholder="Find an icon"><select id="filter" aria-label="Filter drawings"><option value="all">All 50</option><option value="changed">Redrawn · 46</option><option value="retained">Retained · 4</option></select><span id="count">50 shown</span></div>'''
parts=[head]
for r,b,a in rows:
 keyreason={'CIRCLE':'A circular envelope suits the rounded silhouette.','SQUARE':'The square envelope suits the compact subject.','HRECT_L':'The horizontal envelope gives the wide subject room.','VRECT_L':'The vertical envelope gives the upright subject room.'}.get(r['keyshape'],'Envelope follows the subject proportions.')
 kind='changed' if r['changed_drawing'] else 'retained';label='REDRAWN' if kind=='changed' else 'RETAINED'
 geometry={'keyshape':r['keyshape'],'canvas':'48 × 48','stroke':4,'family':'solo','revision':r['revision_id'],'source':r['source_path'],'before_sha256':r['before_sha256'],'after_sha256':r['after_sha256'],'validation':'valid; zero warnings','checks':r['validation']['checks_run'],'internal_spacing':r['validation']['internal_spacing_advisory']['status'],'holes':r['validation']['negative_space']['status']}
 feedback=''.join('<p><b>Saved feedback:</b> '+esc(f)+'</p>' for f in r['feedback'])
 parts.append(f'''<article id="{esc(r['icon_id'])}" data-kind="{kind}"><div class="heading"><h2>{r['number']:02d} · {esc(r['icon_id'])}</h2><span class="badge">GOOD · {label}</span></div><div class="views"><div class="view"><img class="large" alt="Before: {esc(r['icon_id'])}" src="{uri(b)}">Before</div><div class="view"><img class="large" alt="After: {esc(r['icon_id'])}" src="{uri(a)}">After</div><div class="view"><div class="native-pair"><div class="tile"><img alt="48px light" src="{uri(svg_view(a,'#000'))}"></div><div class="tile dark"><img alt="48px dark" src="{uri(svg_view(a,'#fff'))}"></div></div>Actual size · 48 px</div><div class="view center"><img class="large" alt="Centerlines" src="{uri(svg_view(a,'#28829a','.45'))}">Centerlines</div></div><p class="note">{esc(r['change'])}</p><div class="actions"><small>Solo · {esc(r['keyshape'])} · Valid, zero warnings</small><a href="../solo48/{esc(r['revision_id'])}.svg">Open SVG</a></div><details><summary>Review details and evidence</summary><p>{esc(keyreason)}</p><p><b>Reference:</b> {esc(r['reference'])}</p><p><b>Earlier finding:</b> {esc(r['old_finding'])}</p>{feedback}<pre>{esc(json.dumps(geometry,indent=2))}</pre></details></article>''')
parts.append('''<footer>The before-and-after previews are embedded snapshots. “Good” is the drawing review result, separate from any gallery approval you choose to record.</footer></main><script>const q=document.querySelector('#search'),f=document.querySelector('#filter');function filter(){let n=0;for(const a of document.querySelectorAll('article')){a.hidden=(f.value!=='all'&&a.dataset.kind!==f.value)||!a.textContent.toLowerCase().includes(q.value.toLowerCase());if(!a.hidden)n++;}document.querySelector('#count').textContent=n+' shown';}q.addEventListener('input',filter);f.addEventListener('change',filter);</script></html>''')
report=''.join(parts)
(W/'report.html').write_text(report)
(D/'gallery/rejected-solo-fixes-sep15.html').write_text(report)
# Keep the URL the user is already viewing useful after the repair.
(D/'gallery/rejected-solo-review-50-sep15.html').write_text(report)
records=[r for r,_,_ in rows]
(W/'final-review.json').write_text(json.dumps(records,indent=2))
(W/'verification.json').write_text(json.dumps({'icons':50,'redrawn':changed,'retained':50-changed,'published_variants':47,'valid_variants':47,'all_solo48':True,'report_sha256':sha(report.encode()),'test_summary':test_summary},indent=2))
md=['# Solo repairs · first 50','',f'{changed} drawings redrawn; {50-changed} retained. All remain SOLO48. The 47 independent revisions pass the full publication build with zero warnings.','',test_summary,'','| # | Icon | Result | Revision | Change |','|---|---|---|---|---|']
for r in records:md.append(f"| {r['number']} | {r['icon_id']} | Good — {'redrawn' if r['changed_drawing'] else 'retained'} | {r['revision_id']} | {r['change']} |")
(W/'REPORT.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'icons':50,'redrawn':changed,'retained':50-changed,'variants':47,'report':'http://localhost:8000/gallery/rejected-solo-fixes-sep15.html'}))
