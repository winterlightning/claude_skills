from pathlib import Path
import json,sys,ast,html,subprocess
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'mapping.json').read_text());results={r['original']:r for r in json.loads((W/'results.json').read_text())}
blocked={'end-point-none','subtract','subtract-interface-essential'}
notes={
'burning-crashed-aircraft':'Broadened the damaged wings and removed pinched folded fins.',
'fighter-jet':'Extended the nose and tail; broadened the wing and tail openings.',
'military-drone-overhead':'Extended the airframe and broadened both wing tips.',
'money-plant':'Adjusted both leaf curves with the longer stem.',
'hand-holding-remote-with-signal':'Extended the wrist and opened the thumb-to-hand gap.',
'moving-server-stack':'Raised the first server to the envelope and opened the gap between servers.',
'head-with-drinking-straw':'Extended the straw and neck; rebuilt the chin with an exact quarter circle.',
}
for r in rows:
 if r['original'] in blocked:continue
 q=results[r['original']];assert q['validation']=='status: valid' and q['qa']['status']=='pass' and not q['qa']['needs_review'],r['id']
 p=ROOT/r['file'];s=p.read_text();t=ast.parse(s);c=next(n for n in t.body if isinstance(n,ast.ClassDef));build=next(n for n in c.body if isinstance(n,ast.FunctionDef) and n.name=='build')
 # Record the envelope and review provenance beside the construction it owns.
 lines=s.splitlines(keepends=True);lines.insert(build.lineno,'        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.\n')
 s=''.join(lines);p.write_text(s)
# Keep unsuccessful drafts outside the registry; originals retain their honest bounds failures.
(W/'unresolved').mkdir(exist_ok=True)
for r in rows:
 if r['original'] in blocked:
  p=ROOT/r['file'];dest=W/'unresolved'/p.name;p.rename(dest);r['draft_file']=str(dest.relative_to(ROOT));r['blocked']=True
  r['reason']='A horizontal 4-unit stroke cannot meet the standard rectangular height while retaining its meaning. No keyshape exception or validation waiver was added.'
(W/'mapping.json').write_text(json.dumps(rows,indent=2))
# An embedded comparison page works locally without a server or network requests.
cards=[]
for r in rows:
 before=render_svg(create(r['original']));after=before if r.get('blocked') else render_svg(create(r['id']));label='Unresolved · original retained' if r.get('blocked') else 'Revised · all icon checks pass';note=r.get('reason',notes.get(r['original'],'Adjusted the height to the exact envelope; checked geometry, spacing, openings and internal spacing.'))
 cards.append(f'<article data-name="{html.escape(r["original"])}" data-blocked="{str(bool(r.get("blocked"))).lower()}"><h2>{html.escape(r["original"])}</h2><div class="pair"><div><span>Before</span>{before}</div><div><span>{label}</span>{after}</div></div><div class="native">48 px {after}</div><p>{html.escape(note)}</p></article>')
(W/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Height repairs · 126 icons</title><style>*{box-sizing:border-box}body{margin:0;background:#f7f6f2;color:#17191d;font:15px system-ui}body.dark{background:#17191d;color:#f7f6f2}header{padding:28px 32px;background:inherit;position:sticky;top:0;z-index:2;border-bottom:1px solid #8884}h1{font-size:25px;margin:0 0 10px}header p{margin:0 0 18px}button,input,select{background:transparent;color:inherit;border:1px solid #8886;border-radius:10px;padding:10px;margin-right:8px}button{cursor:pointer}input{width:260px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:20px;padding:25px}article{border:1px solid #8884;border-radius:14px;padding:22px}article[data-blocked=true]{border-color:#c78138}h2{font-size:16px;min-height:38px}.pair{display:flex;justify-content:space-around}.pair div{display:flex;flex-direction:column;align-items:center;gap:15px}.pair svg{width:120px;height:120px}.pair span{font-size:11px;opacity:.7;text-align:center}.native{display:flex;align-items:center;justify-content:center;gap:15px;margin:20px;font-size:12px}.native svg{width:48px;height:48px}p{font-size:13px;line-height:1.6}footer{padding:32px;font-size:13px;line-height:1.7;opacity:.7}[hidden]{display:none}</style><header><h1>123 repaired · 3 unresolved</h1><p>126 current gallery matches · all 123 revisions pass every icon check · originals preserved</p><input id="search" placeholder="Find an icon" oninput="filter()"><select id="status" onchange="filter()"><option value="all">All icons</option><option value="false">Repaired</option><option value="true">Unresolved (3)</option></select><button onclick="document.body.classList.toggle('dark')">Light / dark</button></header><main>'''+''.join(cards)+'''</main><footer>Construction references: local Lucide bell, tower-control, plane, scissors, map-pin, user, person-standing, hand, tram-front, sprout, pound-sterling and trophy; shared human user.svg and full_body_ref.png. Detached heads were checked against the four-unit visible gap. Three horizontal-line entries retain their original failures: the keyshape-fitting guide identifies stroke-defined one-dimensional marks as unsuitable for the standard rectangle envelopes. Validation rules were not changed.</footer><script>function filter(){const q=document.getElementById('search').value.toLowerCase(),s=document.getElementById('status').value;document.querySelectorAll('article').forEach(e=>e.hidden=!e.dataset.name.includes(q)||(s!=='all'&&s!==e.dataset.blocked))}</script></html>''')
cmd=[sys.executable,'icon_set/scripts/build.py','--family','solo']
for r in rows:
 if not r.get('blocked'):cmd+=['--icon',r['file']]
with (W/'build.log').open('w') as f:result=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT)
print('Build exit',result.returncode);sys.exit(result.returncode)
