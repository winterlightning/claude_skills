import json,sys,io,xml.etree.ElementTree as ET
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W.parents[2]))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
out={};im=Image.new('RGB',(1440,300),'white');d=ImageDraw.Draw(im)
for i,(k,r) in enumerate(json.load(open(W/'candidates.json')).items()):
 m=create(r['icon']);svg=m.to_svg();q=inspect_icon(m);q.pop('_svg',None);out[k]=q;(W/(r['icon']+'.svg')).write_text(svg);print(k,q['status'],q['errors'],q['warnings'],flush=True)
 x=i*360;d.text((x+5,5),r['icon'][:45],fill='black')
 for sw,xx,size in [(4,x+5,160),(.25,x+175,160),(4,x+15,48 if r['tall'] else 32)]:
  tree=ET.fromstring(svg)
  for e in tree.iter():
   if 'stroke-width' in e.attrib:e.set('stroke-width',str(sw))
  p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(tree),output_height=size))).convert('RGBA');im.paste(p,(xx,50 if size==160 else 235),p)
(W/'qa.json').write_text(json.dumps(out,indent=2));im.save(W/'review.png')
