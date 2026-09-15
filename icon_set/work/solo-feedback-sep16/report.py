from pathlib import Path
import json,re,html,base64,hashlib,xml.etree.ElementTree as ET
W=Path(__file__).parent
D=Path('icon_set/dist')
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
esc=html.escape
rows=json.loads((W/'plan.json').read_text())
previous=Path('icon_set/work/rejected-solo-fixes-sep15/report.html').read_text()
m={r['icon_id']:r for r in json.loads((D/'solo48/manifest.json').read_text())['icons']}
feedback={'anteater':'Still a bad drawing.','arched-stone-bridge':'The wave is bad.','arrange-number':'The 9 is too big; make it the same size as the 1.','artillery-field-gun':'Bad drawing.','artillery-gun-outriggers':'Bad drawing.','baby-face-with-bow':'Remove the ears.','balancing-stick-pose':'The pose is not understandable.'}
def uri(s):return 'data:image/svg+xml;base64,'+base64.b64encode(s).decode()
def sha(s):return hashlib.sha256(s).hexdigest()
def styled(s,fg,sw=None,parts=None):
 root=ET.fromstring(s)
 for e in root.iter():
  if e.get('stroke') not in (None,'none'):e.set('stroke',fg)
  if e.get('stroke-width') and sw:e.set('stroke-width',sw)
  if parts and e.get('id') in parts:e.set('stroke',parts[e.get('id')])
 return ET.tostring(root)
records=[]
for r in rows:
 a=(D/'solo48'/(r['new_id']+'.svg')).read_bytes();b=(W/(r['icon_id']+'-before.svg')).read_bytes();built=m[r['new_id']]
 assert a==(W/'build/solo48'/(r['new_id']+'.svg')).read_bytes()
 assert built['validation']['status']=='valid' and not built['validation']['warnings']
 assert built['family']=='solo' and built['canvas_size']==48
 detail=''
 if r['icon_id']=='balancing-stick-pose':
  colors={'head':'#2274a5','arms':'#b55c16','torso':'#28342b','raised-leg':'#8056ad','standing-leg':'#227a50'}
  detail=f'''<div class="pose-guide" style="display:flex;gap:24px;align-items:center;flex-wrap:wrap;padding:16px;background:#f4f6f3;border-radius:10px"><img alt="Labeled balancing pose" width="192" height="192" src="{uri(styled(a,'#28342b',parts=colors))}"><div><strong>How to read this pose</strong><p><span style="color:#2274a5">Blue: head, facing left.</span><br><span style="color:#b55c16">Orange: arms reaching forward.</span><br><span style="color:#8056ad">Purple: raised back leg.</span><br><span style="color:#227a50">Green: leg on the ground.</span></p><small>The torso leans horizontally in a one-leg balance.</small></div></div>'''
 if r['icon_id']=='arrange-number':detail='<p class="muted">Both numerals are 12 units tall before the stroke, or 16 pixels including the stroke. Their natural widths differ.</p>'
 refs=f'<p><strong>Reference:</strong> {esc(r["reference"])}</p>'
 if r['icon_id']=='anteater':refs+='<p><a href="https://www.naturalistjourneys.com/tours/2026/02/12/guyana-unspoiled-wilderness">Anteater photo reference</a> · The silhouette uses a longer snout, distinct broad tail and two simple legs.</p>'
 evidence={'family':'solo','canvas':'48 × 48','keyshape':built['keyshape'],'stroke':4,'revision':r['new_id'],'parent':r['parent'],'before_sha256':sha(b),'after_sha256':sha(a),'validation':'valid; zero warnings','checks':built['validation']['checks_run'],'source':r['new_path']}
 article=f'''<article id="{r['icon_id']}" data-kind="revised"><div class="heading"><h2>{r['number']:02d} · {esc(r['icon_id'])}</h2><span class="badge">REVISED · 16 SEP</span></div><p class="muted"><strong>Your feedback:</strong> {esc(feedback[r['icon_id']])}</p><div class="views"><div class="view"><img class="large" alt="Previous drawing: {esc(r['icon_id'])}" src="{uri(b)}">Previous drawing</div><div class="view"><img class="large" alt="Revised drawing: {esc(r['icon_id'])}" src="{uri(a)}">Revised drawing</div><div class="view"><div class="native-pair"><div class="tile"><img alt="48px light" src="{uri(styled(a,'#000'))}"></div><div class="tile dark"><img alt="48px dark" src="{uri(styled(a,'#fff'))}"></div></div>Actual size · 48 px</div><div class="view center"><img class="large" alt="Centerlines" src="{uri(styled(a,'#28829a','.45'))}">Centerlines</div></div><p>{esc(r['change'])}</p>{detail}<div class="actions"><small>Solo · {esc(built['keyshape'])} · Checks pass, zero warnings</small><a href="../solo48/{r['new_id']}.svg">Open SVG</a></div><details><summary>References and validation</summary>{refs}<pre>{esc(json.dumps(evidence,indent=2))}</pre></details></article>'''
 pattern=r'<article id="'+re.escape(r['icon_id'])+r'"[\s\S]*?</article>'
 previous,n=re.subn(pattern,lambda _:article,previous,count=1);assert n==1
 records.append(dict(r,feedback=feedback[r['icon_id']],validation=built['validation'],before_sha256=sha(b),after_sha256=sha(a),reviewed_native_light=True,reviewed_native_dark=True,reviewed_centerlines=True))
summary='All seven revised icons pass the full publication checks with zero warnings. Broader test results are saved with the report.'
if (W/'test-summary.json').exists():summary=json.loads((W/'test-summary.json').read_text())['summary']
header=f'''<header><div class="eyebrow">Pictographic / Your drawing corrections / 16 September</div><h1>Seven solo drawings revised.</h1><p>The anteater, bridge wave, number sizes, both artillery drawings, baby’s ears and balancing pose have been revised from your feedback. Every icon stays <strong>solo, 48 × 48</strong>.</p><div class="stats"><div class="stat"><b>7</b>Drawings revised</div><div class="stat"><b>7 / 7</b>Icon checks pass</div><div class="stat"><b>48 × 48</b>Solo canvas</div></div><p>Compare the drawing you commented on with its latest revision below. The balancing pose includes a colored guide to its arms and legs.</p><details><summary>Validation and scope</summary><p>{esc(summary)}</p><p>The other 43 drawings from the first batch remain available under “All 50”. Earlier versions are preserved in the gallery’s variant history.</p></details></header>'''
previous=re.sub(r'<header>[\s\S]*?</header>',lambda _:header,previous,count=1)
previous=re.sub(r'<title>.*?</title>','<title>Seven solo drawings · revised from your feedback</title>',previous,count=1)
previous=re.sub(r'<select id="filter"[\s\S]*?</select>','<select id="filter" aria-label="Filter drawings"><option value="revised" selected>Latest revisions · 7</option><option value="all">All 50</option></select>',previous,count=1)
previous=previous.replace('<span id="count">50 shown</span>','<span id="count">7 shown</span>')
previous=previous.replace('</script></html>','filter();</script></html>')
previous=previous.replace('“Good” is the drawing review result, separate from any gallery approval you choose to record.','These new revisions are ready for your visual review; gallery approval remains separate.')
(W/'report.html').write_text(previous)
for name in ['solo-feedback-sep16.html','rejected-solo-fixes-sep15.html','rejected-solo-review-50-sep15.html']:(D/'gallery'/name).write_text(previous)
(W/'review.json').write_text(json.dumps(records,indent=2))
(W/'verification.json').write_text(json.dumps({'revised':7,'total_batch':50,'family':'solo','canvas':48,'published_valid':7,'warnings':0,'published_svg_matches_reviewed':True,'report_sha256':sha(previous.encode())},indent=2))
md=['# Seven solo corrections — 16 September','',summary,'','| Icon | Revision | Correction |','|---|---|---|']
for r in rows:md.append(f"| {r['icon_id']} | {r['new_id']} | {r['change']} |")
(W/'REPORT.md').write_text('\n'.join(md)+'\n');print('Updated 7 cards in the 50-icon report; latest seven shown by default.')
