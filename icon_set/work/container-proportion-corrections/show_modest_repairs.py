from pathlib import Path
import json,hashlib,html,xml.etree.ElementTree as E,io
import cairosvg
from PIL import Image,ImageDraw
from icon_set.scripts.container_placement import Artwork,root_svg,artwork_group
out=Path(__file__).parent;base=out.parents[1];data=json.load(open(base/'work/container-pair-combinations/results.json'));rows=json.load(open(out/'modest-measured.json'));fixpath=base/'work/container-fit-repair/fit-adjustments.json';fixes=json.load(open(fixpath));None # Keep the selected gift revision.
def combo(doc,sub,center):
 root=root_svg();root.append(artwork_group(Artwork.read(doc,64),'container',1,0,0,stroke=4));root.append(artwork_group(Artwork.read(sub,32),'sub',1,center[0]-16,center[1]-16,stroke=4));return E.tostring(root,encoding='unicode')
def fig(doc,caption):return '<figure>'+doc+'<figcaption>'+caption+'</figcaption></figure>'
gift=(base/'dist/container64/gift-box-container.svg').read_text();people=(out/'two-standing-people-sub32-v2.svg').read_text();cards=['<article><h2>gift-box-container · original restored</h2><div class="figures">'+fig(gift,'Exact original container')+fig(people,'Revised people · separate option')+'</div><p>The original gift-box geometry is restored unchanged. The current people symbol still needs a separately considered compact layout to fit this shallow box; it is not forced into the container here.</p></article>'];cards[0]=(out/'gift-v7-card.html').read_text() if (out/'gift-v7-card.html').exists() else cards[0];cards[0]=(out/'gift-v7-card.html').read_text() if (out/'gift-v7-card.html').exists() else cards[0];cards[0]=(out/'gift-v7-card.html').read_text() if (out/'gift-v7-card.html').exists() else cards[0];pics=[]
for r in rows:
 assert r['validation']=='pass' and all(p['status']=='pass' for p in r['pairs'])
 path=out/(r['variant']+'.svg');doc=path.read_text();dest=base/'work/container-fit-repair'/path.name;dest.write_text(doc);orig=base/'dist/container64'/(r['parent']+'.svg');old=orig.read_text()
 fixes['revisions'][r['parent']]={'variant':r['variant'],'module':r['module'],'parent_sha256':hashlib.sha256(orig.read_bytes()).hexdigest(),'variant_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'center':r['center'],'reason':r['reason'],'batch':'modest-expansion'}
 row=next(a for a in data['rows'] if data['hosts'][a[0]].get('parent')==r['parent']);sub=data['subs'][row[1]]['svg32'];before=combo(old,sub,row[3:5]);after=combo(doc,sub,r['center']);pics.append((r['parent'],before,after))
 description='4 units added above and below; still horizontal.' if 'label-tag' in r['parent'] else '4 units added on the left and right; still slender.'
 cards.append('<article><h2>'+r['parent']+'</h2><p>'+description+' Native 32-unit sub-icon retained.</p><div class="figures">'+fig(before,'Original · native sub')+fig(after,'Modest expansion · same native sub')+'</div><p>All '+str(len(r['pairs']))+' current mapped previews pass padding; minimum gap ≈ '+str(round(min(p['gap'] for p in r['pairs']),2))+' units.</p></article>')
fixpath.write_text(json.dumps(fixes,indent=2));previous=out/'before-modest-expansion.html'
if not previous.exists():previous.write_text((out/'index.html').read_text())
page='''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Original gift and modest expansions</title><style>body{font:15px system-ui;margin:28px;background:#f4f6f8;color:#253248}article{background:white;border:1px solid #dbe1e9;padding:20px;margin:20px 0;border-radius:12px}h2{font-size:20px}.figures{display:flex;flex-wrap:wrap;gap:30px}figure{margin:0}svg{width:192px;height:192px;outline:1px solid #d9e0e8;background-image:linear-gradient(#b8c5d644 1px,transparent 1px),linear-gradient(90deg,#b8c5d644 1px,transparent 1px);background-size:3px 3px}figcaption{font-size:13px;margin-top:10px;max-width:192px}p{line-height:1.6}</style><h1>Reworked gift · modest expansions</h1><p>Preserve the subject first. Try a small grid-snapped container adjustment before reducing the sub-icon. The three modest expansions below keep the sub-icons unchanged at their native 32-unit size.</p><p><a href="../container-pair-combinations/index.html">Interactive pair grid</a></p>'''+''.join(cards)
(out/'index.html').write_text(page)
# Update the old batch page too, so rejected versions do not remain its current examples.
p=base/'work/container-repair-batch/index.html';text=p.read_text();import re
labels=['New gift box and newly drawn people','Restored slim soap bottle','Restored horizontal tag','Restored slim booklet']
for label,card in zip(labels,cards):text=re.sub(r'<article><h2>'+re.escape(label)+r'</h2>.*?</article>',lambda _:card,text,flags=re.S)
text=text.replace('The gift and its two-person sub-icon have been reworked. The bottle, tag and booklet use their original slim proportions, with smaller sub-icon prototypes where necessary.','The original gift container is restored. The bottle, tag and booklet now use modest four-unit expansions and retain their native 32-unit sub-icons.');p.write_text(text)
for theme,bg,fg in [('light','white','#202630'),('dark','#202833','white')]:
 im=Image.new('RGB',(700,570),bg);draw=ImageDraw.Draw(im)
 for i,(name,before,after) in enumerate(pics):
  draw.text((10,i*190+3),name,fill=fg)
  for j,svg in enumerate([before,after]):
   root=E.fromstring(svg);root.set('color',fg)
   for sz,xx,yy in [(112,j*350+20,i*190+27),(64,j*350+170,i*190+55)]:
    tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=E.tostring(root),output_width=sz,output_height=sz)));im.paste(tile,(xx,yy),tile)
   draw.text((j*350+20,i*190+151),'Original' if j==0 else 'Modest expansion · same sub',fill=fg)
 im.save(out/('modest-'+theme+'.png'))
print('Original gift restored; three modest candidates selected.')
