from pathlib import Path
import json,html,io,xml.etree.ElementTree as E
import cairosvg
from PIL import Image,ImageDraw
from icon_set.scripts.container_placement import Artwork,root_svg,artwork_group
from icon_set.scripts.suggest_container_sub_size import transform
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,vector_zone,check_pair
out=Path(__file__).parent;base=out.parents[1];data=json.load(open(base/'work/container-pair-combinations/results.json'))
items=[('gift-box-container','two-standing-people-sub32',[32,42],'New gift box and newly drawn people'),('liquid-soap-dispenser-bottle','geometric-three-toed-paw-sub32',[32,40],'Restored slim soap bottle'),('right-pointing-label-tag','cross-mark-state-231',[28,32],'Restored horizontal tag'),('simple-folded-booklet','cake-sub32',[32,38],'Restored slim booklet')];cards=[];stats=[];im=Image.new('RGB',(840,760),'#f5f7fa');draw=ImageDraw.Draw(im)
def combo(doc,sub,center,size):
 root=root_svg();root.append(artwork_group(Artwork.read(doc,64),'host',1,0,0,stroke=4));root.append(artwork_group(Artwork.read(sub,32),'sub',*transform(size,center),stroke=4));return E.tostring(root,encoding='unicode')
for i,(name,sn,center,label) in enumerate(items):
 row=next(r for r in data['rows'] if data['hosts'][r[0]].get('parent',data['hosts'][r[0]]['name'])==name and data['subs'][r[1]]['name']==sn);h=data['hosts'][row[0]];s=data['subs'][row[1]]
 doc=(out/'gift-box-container-v3.svg').read_text() if i==0 else (base/'dist/container64'/(name+'.svg')).read_text();sub=(out/'two-standing-people-sub32-v2.svg').read_text() if i==0 else s['svg32'];a=Artwork.read(sub,32);ink=VectorInk.from_art(read_art(doc));x,y=center;_,inner,outer=vector_zone(ink,{'kind':'safe-zone','method':'selected semantic enclosed face','polygon':[[x-1,y-1],[x+1,y-1],[x+1,y+1],[x-1,y+1]]});m=check_pair(ink,VectorInk.from_art(a,transform(24,center)),inner,outer);stats.append(dict(container=name,size24_fit=m['status'],gap=m['ink_gap_lower_units']))
 figures=[]
 for j,(content,caption) in enumerate([(combo(h['svg'],s['svg32'],row[3:5],32),'Previous · oversized container'),(combo(doc,sub,center,32),'Corrected container · native sub'),(combo(doc,sub,center,24),'Corrected · 24-unit prototype')]):
  figures.append('<figure>'+content+'<figcaption>'+caption+'</figcaption></figure>');pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=content.encode(),output_width=128,output_height=128)));im.paste(pic,(j*270+64,i*190+25),pic);draw.text((j*270+12,i*190+162),caption,fill='black')
 draw.text((12,i*190+4),label,fill='black');cards.append('<article><h2>'+label+'</h2><div class="figures">'+''.join(figures)+'</div><p>24-unit fit: '+m['status']+' · minimum gap ≈ '+str(round(m['ink_gap_lower_units'],2))+' units.</p></article>')
im.save(out/'comparison.png');(out/'measurements.json').write_text(json.dumps(stats,indent=2));print(stats)
page='''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Recognizable proportions first</title><style>body{font:15px system-ui;margin:28px;background:#f4f6f8;color:#253248}article{background:white;border:1px solid #dbe1e9;padding:20px;margin:20px 0;border-radius:12px}h2{font-size:20px}.figures{display:flex;flex-wrap:wrap;gap:30px}figure{margin:0}svg{width:192px;height:192px;outline:1px solid #d9e0e8;background-image:linear-gradient(#b8c5d644 1px,transparent 1px),linear-gradient(90deg,#b8c5d644 1px,transparent 1px);background-size:3px 3px}figcaption{font-size:13px;margin-top:10px;max-width:192px}p{line-height:1.6}</style><h1>Recognizable proportions first</h1><p>The gift box and its two-person symbol are redrawn. The soap bottle, label tag and booklet return to their original slender proportions. All original assets remain available.</p><p>The smaller versions shown here are 24-unit scaling prototypes with 4-unit strokes, not final grid-snapped 24-unit sub-icon drawings. The new two-person source is authored on the 32-unit grid with circular heads and open limbs.</p><p><a href="../container-pair-combinations/index.html">Inspect all defined pairs</a></p>'''+''.join(cards)
(out/'index.html').write_text(page)
