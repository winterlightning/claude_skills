import io,json,xml.etree.ElementTree as ET
from pathlib import Path
import cairosvg,numpy as np
from PIL import Image
from scipy.ndimage import label,binary_fill_holes
from svgpathtools import Document,Arc
D=Path('icon_set/work/sub-text-repairs');rs=json.loads((D/'repairs.json').read_text());results=[]
holes=dict(A=1,B=2,D=1,O=1,P=1,Q=1,R=1,g=1)
holes.update({'0':1,'6':1,'8':2,'9':1,'%':2})
for a in rs:
 doc=Path(a['repair_svg']).read_text();root=ET.fromstring(doc);paths=Document(io.StringIO(doc)).paths();assert root.get('stroke-width')=='4'
 for p in paths:
  for s in p:
   assert not isinstance(s,Arc)
   for attr in ('start','end','control','control1','control2'):
    if hasattr(s,attr):
     z=getattr(s,attr);assert z.real==round(z.real) and z.imag==round(z.imag)
 boxes=[p.bbox() for p in paths];l=min(b[0] for b in boxes);r=max(b[1] for b in boxes);t=min(b[2] for b in boxes);b=max(b[3] for b in boxes)
 assert l>=2 and r<=float(root.get('width'))-2 and t>=2 and b<=30
 assert (a['symbol'] and r-l+4==32) or b-t+4==32
 mask=np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=doc.encode(),scale=16))))[:,:,3]>128
 components=label(mask)[1];counters=label(binary_fill_holes(np.pad(mask,2))^np.pad(mask,2))[1]
 expected_components=sum(3 if c=='%' else 2 if c=='!' else 1 for c in a['text'] if not c.isspace())+int(a['underline'])+ (2 if 'height-limit' in a['id'] else 0)+(1 if 'wrench-size' in a['id'] else 0)
 expected_counters=sum(holes.get(c,0) for c in a['text'])
 assert (components,counters)==(expected_components,expected_counters),(a['text'],(components,counters),(expected_components,expected_counters))
 results.append(dict(key=a['key'],grid=True,stroke=4,unclipped=True,ink_height=b-t+4,ink_width=r-l+4,components=components,expected_components=expected_components,openings=counters,expected_openings=expected_counters))
(D/'verification.json').write_text(json.dumps(results,indent=2));print('27 repairs pass: grid, stroke, bounds, expected connected parts and letter openings at 16x.')
