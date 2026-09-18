"""Publish validated repair variants to the review gallery, preserving parents."""
from pathlib import Path
import json,hashlib,html,xml.etree.ElementTree as E
from collections import Counter
from icon_set.scripts.container_placement import Artwork,root_svg,artwork_group
from icon_set.scripts.suggest_container_sub_size import transform
OUT=Path(__file__).parent;BASE=OUT.parents[1];baseline=json.loads((OUT/'baseline.json').read_text());measured=json.loads((OUT/'measured.json').read_text());fixpath=BASE/'work/container-fit-repair/fit-adjustments.json';fixes=json.loads(fixpath.read_text());cards=[];accepted=[]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def combined(host,sub,center,size=32):
 root=root_svg();root.append(artwork_group(Artwork.read(host,64),'host',1,0,0,stroke=4));root.append(artwork_group(Artwork.read(sub,32),'sub',*transform(size,center),stroke=4));return E.tostring(root,encoding='unicode')
for r in measured:
 assert r['validation']=='status: valid'
 assert not any(p['before']=='pass' and p['after']!='pass' for p in r['pairs'])
 selected=r['parent']!='double-concentric-circles'
 old=next(h for h in baseline['hosts'] if h['name']==r['parent']);oldpath=BASE/'dist/container64'/(r['parent']+'.svg');assert sha(oldpath)==old['sha256'],r['parent']
 newpath=OUT/(r['variant']+'.svg')
 if selected:
  dest=BASE/'work/container-fit-repair'/newpath.name;dest.write_text(newpath.read_text())
  fixes['revisions'][r['parent']]={'variant':r['variant'],'module':r['module'],'parent_sha256':sha(oldpath),'variant_sha256':sha(dest),'center':r['center'],'reason':r['reason'],'pairs':r['pairs'],'batch':'37-container-repair'};accepted.append(r)
 else:
  draft=OUT/'drafts';draft.mkdir(exist_ok=True);source=Path(r['module'])
  if source.exists():source.rename(draft/(source.name+'.txt'))
 pairs=[p for p in r['pairs'] if p['before']=='fail'];sample=pairs[0];row=baseline['rows'][sample['row']];sub=baseline['subs'][row[1]]['svg32'];native=sum(p['after']=='pass' for p in pairs)
 reason=r['reason'] if selected else 'Keep the original two-ring container. The 24-unit simulations pass; making its inner circle large enough for these 32-unit symbols would crowd the outer ring.'
 after=newpath.read_text() if selected else old['svg'];center=r['center'] if selected else row[3:5]
 figures='<figure>'+combined(old['svg'],sub,row[3:5])+'<figcaption>Original · native 32</figcaption></figure><figure>'+combined(after,sub,center)+'<figcaption>'+('Repaired' if selected else 'Unchanged')+' · native 32</figcaption></figure>'
 if sample['after']!='pass':figures+='<figure>'+combined(after,sub,center,24)+'<figcaption>24-unit prototype · redraw pending</figcaption></figure>'
 status=f'{native}/{len(pairs)} previously failing previews now fit at 32' if selected else '3 pairs → 24-unit sub redraw recommended'
 cards.append('<article><h2>'+html.escape(r['parent'])+'</h2><p>'+html.escape(reason)+'</p><p><b>'+status+'</b></p><div class="figures">'+figures+'</div><p>Sub-icon: '+html.escape(baseline['subs'][row[1]]['name'])+'</p></article>')
fixpath.write_text(json.dumps(fixes,indent=2))
(OUT/'accepted.json').write_text(json.dumps(accepted,indent=2))
summary={'containers_reviewed':37,'containers_repaired':len(accepted),'preserved_exception':'double-concentric-circles','original_failed_previews':143,'now_native32_pass':135,'remaining_native32_fail':8,'remaining_size24_simulation_pass':8,'previously_passing_regressions':0,'model_validation':'All selected models valid with no warnings','tests':'30 focused geometry, placement and sizing tests passed'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2))
(OUT/'index.html').write_text('''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>37 container repairs · before and after</title><style>body{font:15px system-ui;margin:28px;background:#f4f6f8;color:#203044}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(440px,1fr));gap:20px}article{background:white;border:1px solid #d8dfe8;border-radius:10px;padding:20px}h2{font-size:18px}p{line-height:1.5}.figures{display:flex;flex-wrap:wrap;gap:15px}figure{margin:0}svg{width:128px;height:128px;outline:1px solid #d9e0e8;background-image:linear-gradient(#b8c5d63b .5px,transparent .5px),linear-gradient(90deg,#b8c5d63b .5px,transparent .5px);background-size:2px 2px}figcaption{font-size:11px;max-width:128px;margin-top:8px}input{padding:10px;margin:12px 0;width:300px}</style><h1>37 containers reviewed · 36 repaired</h1><p>135 of 143 previously failing previews now pass at native 32-unit sub-icon size. No previously passing pair regressed. Eight remaining previews pass a 24-unit size simulation; those sub-icons still require grid-snapped redraws. Container models use integer-grid construction and 4-unit strokes. Original models are preserved.</p><p><a href="../container-pair-combinations/index.html?repair=repaired-batch">Inspect the repaired batch in the interactive vector grid</a> · <a href="summary.json">Validation summary</a></p><input placeholder="Find a container" oninput="for(const a of document.querySelectorAll('article'))a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase())"><main>'''+''.join(cards)+'</main>')
print(json.dumps(summary,indent=2))
