import json,hashlib,sys,xml.etree.ElementTree as E
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
rows=json.loads((W/'candidates.json').read_text());prior=W.parent/'sub-fidelity-repair-32'
for r in rows:
 svg=create(r['compact']).to_svg();(prior/'review-assets'/f'{r["number"]}-after.svg').write_text(svg)
 root=E.fromstring(svg)
 for e in root.iter():
  if 'stroke-width' in e.attrib:e.set('stroke-width','.3')
 (prior/'review-assets'/f'{r["number"]}-center.svg').write_text(E.tostring(root).decode())
p=prior/'gallery.py';s=p.read_text()
s=s.replace("rows=json.loads((W/'accepted.json').read_text());cards=[];sizes={}","rows=json.loads((W/'accepted.json').read_text());cards=[];sizes={}\ncompact_overrides={r['number']:r for r in json.loads((W.parent/'sub-compact-feedback/candidates.json').read_text())}\nfrom icon_set.model.icons.sub._text_base import canvas_dimensions")
s=s.replace("i=r['number'];m=create(r['candidate']);w,h=m.canvas_width,m.canvas_height;sizes[r['candidate']]=[w,h]", "i=r['number'];r=dict(r)\n if i in compact_overrides:r['candidate']=compact_overrides[i]['compact']\n m=create(r['candidate']);w,h=canvas_dimensions(m);sizes[r['candidate']]=[w,h]\n status='4px frame / 2px inner · approved compact exception' if i in compact_overrides else '4px stroke · geometry pass'")
s=s.replace('4px stroke · geometry pass</p>', '{status}</p>')
s=s.replace('All 32 pass geometry checks; ', '29 pass standard geometry checks; 3 use your approved compact exceptions. ')
s=s.replace('Other drawings use explicit larger canvases with 4px strokes.', 'HI, Bitcoin and O₂ now use 32×32 with 4px frames and smaller 2px inner characters. Other drawings retain their current dimensions.')
s=s.replace('geometry_pass=32,compact_32=compact','geometry_pass=29,approved_compact_exceptions=3,compact_32=compact')
p.write_text(s)
# Keep source fidelity and compact exception records distinct from standard geometry results.
hp=ROOT/'icon_set/data/sub-reference-fidelity.json';history=json.loads(hp.read_text())
for r in rows:
 sha=hashlib.sha256((ROOT/r['compact_python']).read_bytes()).hexdigest();svgsha=hashlib.sha256(create(r['compact']).to_svg().encode()).hexdigest()
 history[r['compact']]=dict(status='redrawn',model_sha256=sha,svg_sha256=svgsha,source_sha256=r['source_sha256'],source_id=r['source_id'],finding='Complete compact composition; user-approved 4px frame / 2px inner-symbol exception. Human feedback remains open.',review_url='sub-compact-feedback/index.html',compact_exception_approved=True)
hp.write_text(json.dumps(history,indent=2)+'\n')
p=ROOT/'icon_set/work/side-repair-priority/inventory.json';data=json.loads(p.read_text());mapping={r['parent']:r for r in rows}
for r in data:
 if r['icon'] in mapping:
  a=mapping[r['icon']];r.update(previous_icon=r['icon'],icon=a['compact'],python_source=a['compact_python'],status='review',compact_exception_approved=True,verified_svg_sha256=history[a['compact']]['svg_sha256'])
p.write_text(json.dumps(data,indent=2))
print('Updated three actual artworks and recorded their compact exceptions.')
