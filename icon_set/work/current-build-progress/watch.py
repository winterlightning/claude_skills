from pathlib import Path
import json,time,datetime,collections
ROOT=Path(__file__).resolve().parents[3];W=Path(__file__).parent;D=ROOT/'icon_set/dist'
page='''<!doctype html><meta charset="utf-8"><title>Current build progress</title><style>body{font:17px system-ui;max-width:850px;margin:60px auto;padding:20px;color:#253044;background:#f7f8fa}h1{font-size:30px}table{width:100%;border-collapse:collapse;background:white}td,th{text-align:left;padding:14px;border-bottom:1px solid #ddd}p{line-height:1.6}a{color:#2563eb}.muted{color:#667085}</style><h1>Current icon build</h1><p id="stage">Loading…</p><table><thead><tr><th>Family</th><th>Measured</th><th>Overlay pass</th><th>Overlay fail</th><th>Errors</th></tr></thead><tbody id="rows"></tbody></table><p>Production reference: <strong>4,192 icons</strong>. Previous local release: <strong>5,542 solo icons</strong>. Overlay results below are checks in progress; the final build determines the released count.</p><p id="final"></p><p class="muted" id="time"></p><p><a href="index.html">Icon gallery</a> · <a href="../qa/index.html">Build QA report</a></p><script>async function refresh(){const d=await(await fetch('../build-progress.json?t='+Date.now())).json();document.querySelector('#stage').textContent=d.stage;document.querySelector('#rows').innerHTML=d.families.map(r=>`<tr><td>${r.family}</td><td>${r.measured} / ${r.total}</td><td>${r.pass}</td><td>${r.fail}</td><td>${r.error}</td></tr>`).join('');document.querySelector('#time').textContent='Updated '+d.updated;document.querySelector('#final').textContent=d.released?'Final release: '+Object.entries(d.released).map(([k,v])=>k+': '+v).join(' · '):''}refresh();setInterval(refresh,10000)</script>'''
folders=['solo48','container64','sub32'];inputs={f:{p.stem for p in (W/'inputs'/f).glob('*.svg')} for f in folders}
while True:
 rows=[]
 for folder in folders:
  counts=collections.Counter()
  for ident in inputs[folder]:
   p=ROOT/'icon_set/work/qa_overlays'/folder/(ident+'.metrics.json')
   if not p.exists():continue
   try:q=json.loads(p.read_text())
   except (ValueError,OSError):continue
   status='error' if q.get('distance_passed') is None or q.get('negative_space_passed') is None else 'fail' if q.get('distance_passed') is False or q.get('negative_space_passed') is False else 'pass'
   counts[status]+=1
  rows.append(dict(family=folder,total=len(inputs[folder]),measured=sum(counts.values()),**{k:counts[k] for k in ['pass','fail','error']}))
 done=(W/'build-exit.json').exists();stage='Complete — final build results are available' if done else 'Full build and QA evidence are running' if (W/'build.log').exists() else 'Measuring distance, holes and pinches; generating QA overlays'
 
 if not done and (W/'full-qa-progress.json').exists():
  progress=json.loads((W/'full-qa-progress.json').read_text());stage=f"Full build QA: {progress['checked']} / {progress['total']} checked"
 payload={'stage':stage,'families':rows,'updated':datetime.datetime.now().strftime('%H:%M:%S')}
 if done:payload['released']={f:len(json.loads((D/f/'manifest.json').read_text())['icons']) for f in folders}
 (D/'build-progress.json').write_text(json.dumps(payload));(D/'gallery').mkdir(exist_ok=True)
 if not (D/'gallery/build-progress.html').exists():(D/'gallery/build-progress.html').write_text(page)
 if done:break
 time.sleep(10)
