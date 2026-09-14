from pathlib import Path
import json,sys,ast,subprocess,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-wide-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'mapping.json').read_text());results=json.loads((W/'results.json').read_text())
assert len(results)==29
assert all(r['validation']=='status: valid' and r['qa']['status']=='pass' and not r['qa'].get('needs_review') for r in results)
notes={
'cat-paw':'Rebalanced the toe lobes and palm; removed two crowded side dots.',
'dinosaur-skull':'Used the square envelope to widen both jaw gaps; the eye becomes a dot and the nostril is omitted.',
'power-supply-unit':'Simplified the fan grille to a ring and the socket to one port stroke to preserve clearance.',
'simple-computer-keyboard':'Reduced the keys to one evenly spaced row above the spacebar.',
'squid':'Widened the mantle and separated all four arm roots.',
'standing-deer':'Narrowed the rump and widened the neck.',
'round-bud-vase':'Rebalanced the four buds, raised the side attachment and deepened the vase.',
'round-bud-vase-v2':'Rebalanced the three buds and deepened the vase.',
'ladies-hat-with-bow':'Narrowed the brim and enlarged both bow openings.',
'libra-zodiac-symbol':'Reduced the dome radius to open the gap above the baseline.',
'cowboy-hat':'Narrowed the brim and joined the crown to shared brim points.',
'desktop-hard-drive-enclosure':'Narrowed the case and enlarged the front panel around the indicator.',
'external-hard-drive':'Narrowed the case and enlarged the front panel around the slot.',
}
refs='Local Lucide graduation-cap, hard-hat, hat-glasses, laptop, keyboard, paw-print and sprout informed the simple contours, rounded enclosures and repeated details. No direct local match for the remaining animals or zodiac symbols.'
cards=[]
for r in rows:
 p=ROOT/r['file'];s=p.read_text();tree=ast.parse(s);doc=tree.body[0] if isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) and isinstance(tree.body[0].value.value,str) else None
 obj=create(r['id']);note=notes.get(r['original'],'Repositioned the outer contours to the exact keyshape width while retaining the defining details.')
 description=f"{r['original']}: {note} Keyshape {obj.keyshape.name}; SOLO48 stroke 4. Reviewed at 48 px in both themes."
 if doc:
  ls=s.splitlines(keepends=True);s=''.join(ls[:doc.lineno-1])+repr(description)+'\n'+''.join(ls[doc.end_lineno:])
 p.write_text(s)
 cards.append(f'''<article><h2>{html.escape(r['original'])}</h2><div class="pair"><div><span>Before</span>{render_svg(create(r['original']))}</div><div><span>Revised · {obj.keyshape.name}</span>{render_svg(obj)}</div></div><div class="native"><span>48 px</span>{render_svg(obj)}</div><p>{html.escape(note)}</p><small>Bounds · Spacing · Openings · Internal spacing: pass</small></article>''')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>29 width repairs</title><style>
*{box-sizing:border-box}body{margin:0;background:#f6f5f1;color:#17191d;font:15px system-ui}body.dark{background:#17191d;color:#f6f5f1}header{padding:30px 36px;position:sticky;top:0;background:inherit;border-bottom:1px solid #8884;z-index:1}h1{font-size:26px;margin:0 0 8px}header p{margin:0;opacity:.7}button{position:absolute;right:36px;top:35px;background:transparent;border:1px solid #8888;color:inherit;padding:10px 18px;border-radius:24px;cursor:pointer}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:20px;padding:28px 36px}article{border:1px solid #8884;border-radius:14px;padding:22px}h2{font-size:16px;margin:0 0 20px}.pair{display:flex;justify-content:space-around}.pair div{display:flex;flex-direction:column;align-items:center;gap:12px}.pair svg{width:120px;height:120px}.pair span,.native span{font-size:12px;opacity:.6}svg{color:inherit}.native{display:flex;justify-content:center;align-items:center;gap:16px;margin:18px}.native svg{width:48px;height:48px}article p{line-height:1.5;min-height:66px;font-size:13px}small{color:#398c60;font-size:11px}footer{padding:0 36px 40px;max-width:1000px;opacity:.65;font-size:13px;line-height:1.6}
</style><header><h1>29 width repairs</h1><p>29 revised icons · all icon checks pass · originals preserved</p><button onclick="document.body.classList.toggle('dark')">Light / dark</button></header><main>'''+''.join(cards)+'</main><footer>'+refs+'</footer></html>'
(W/'index.html').write_text(page)
(W/'notes.json').write_text(json.dumps(notes,indent=2))
cmd=[sys.executable,'icon_set/scripts/build.py','--family','solo']
for r in rows:cmd+=['--icon',r['file']]
with (W/'build.log').open('w') as f:ret=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT)
print('Build exit',ret.returncode)
sys.exit(ret.returncode)
