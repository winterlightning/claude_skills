import io,json,math,xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import cairosvg
from scipy.ndimage import label,binary_fill_holes
from svgpathtools import Document,Arc
ROOT=Path.cwd();OUT=ROOT/'icon_set/work/sub-text-audit'
inv=json.load(open('icon_set/work/combination-sub-review/inventory.json'))
manifest=json.load(open('icon_set/data/combination-sub32.json'))
rows=[];images=[]
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',13)
def render(svg):return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),scale=4))).convert('RGBA')
def topology(im):
 a=np.array(im)[:,:,3]>128
 # Ignore specks below one-quarter square unit.
 _,n=label(a);holes=binary_fill_holes(np.pad(a,2))^np.pad(a,2);_,h=label(holes)
 return n,h
for key,a in sorted(inv['assets'].items(),key=lambda kv:kv[1]['name'].lower()):
 if a['family']!='text':continue
 rec=manifest[key.split('/',1)[1]];svg=Path(rec['svg']).read_text();root=ET.fromstring(svg);paths=Document(io.StringIO(svg)).paths();sw=float(root.get('stroke-width'));w=float(root.get('width'));h=float(root.get('height'))
 source=Path(a['source_path']).read_text();srcpaths=Document(io.StringIO(source)).paths();boxes=[p.bbox() for p in srcpaths];l=min(b[0] for b in boxes);r=max(b[1] for b in boxes);t=min(b[2] for b in boxes);b=max(b[3] for b in boxes)
 factor=28/(b-t) if b>t else 1;pw=(r-l)*factor+4
 pre=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(pw),height='32',viewBox=f'0 0 {pw} 32',fill='none',stroke='black',**{'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
 for p in srcpaths:ET.SubElement(pre,'path',d=p.scaled(factor).translated(complex(2-l*factor,2-t*factor)).d())
 preimage=render(ET.tostring(pre,encoding='unicode'));postimage=render(svg)
 pts=[];radii=[]
 for p in paths:
  for s in p:
   for attr in ('start','end','control','control1','control2'):
    if hasattr(s,attr):pts.extend([getattr(s,attr).real,getattr(s,attr).imag])
   if isinstance(s,Arc):radii.extend([s.radius.real,s.radius.imag])
 boxes=[p.bbox() for p in paths];bounds=[min(b[0] for b in boxes)-sw/2,min(b[2] for b in boxes)-sw/2,max(b[1] for b in boxes)+sw/2,max(b[3] for b in boxes)+sw/2]
 oldtop,newtop=topology(preimage),topology(postimage)
 flags=[]
 if any(abs(x-round(x))>1e-7 for x in pts):flags.append('off-grid points')
 if any(abs(x-round(x))>1e-7 for x in radii):flags.append('fractional arc radii')
 if abs(bounds[3]-bounds[1]-32)>1e-6:flags.append('ink height')
 if min(bounds[:2])<-1e-6 or bounds[2]>w+1e-6 or bounds[3]>h+1e-6:flags.append('clipping')
 if sw!=4:flags.append('stroke not 4')
 if oldtop[0]>newtop[0]:flags.append('components joined after snapping')
 if oldtop[1]!=newtop[1]:flags.append('openings changed after snapping')
 if w>200:flags.append('very wide')
 import base64
 preuri='data:image/svg+xml;base64,'+base64.b64encode(ET.tostring(pre)).decode()
 posturi='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
 if oldtop!=newtop:
  hi_before=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(pre),scale=16))).convert('RGBA')
  hi_after=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),scale=16))).convert('RGBA')
  hi_top=[topology(hi_before),topology(hi_after)]
 else:hi_top=None
 rows.append(dict(high_resolution_topology=hi_top,before_uri=preuri,after_uri=posturi,key=key,name=a['name'],width=w,height=h,ink=bounds,stroke=sw,before_topology=oldtop,after_topology=newtop,flags=flags,source=a['source_path'],export=rec['svg']))
 cell=Image.new('RGB',(360,170),'white');d=ImageDraw.Draw(cell)
 d.text((8,5),f'{len(rows):03} '+a['name'][:43],fill='black',font=font)
 for im,y,title in [(preimage,36,'Before'),(postimage,100,'Grid')]:
  target=(min(296,im.width//2),64);ratio=min(target[0]/im.width,target[1]/im.height);im=im.resize((round(im.width*ratio),round(im.height*ratio)),Image.Resampling.LANCZOS)
  d.text((5,y+18),title,fill='#67717b',font=font);cell.paste(im,(59,y),im)
 if flags:d.text((8,153),', '.join(flags)[:52],fill='#b34020',font=font)
 images.append(cell)
for offset in range(0,len(images),40):
 sheet=Image.new('RGB',(1440,1700),'#d8dde2')
 for i,im in enumerate(images[offset:offset+40]):sheet.paste(im,((i%4)*360,(i//4)*170))
 sheet.save(OUT/f'sheet-{offset//40+1}.png')
(OUT/'audit.json').write_text(json.dumps(rows,indent=2))
from collections import Counter
print(json.dumps({'count':len(rows),'flags':dict(Counter(f for r in rows for f in r['flags'])),'flagged':[{k:r[k] for k in ['key','name','flags']} for r in rows if r['flags']]},indent=2))
