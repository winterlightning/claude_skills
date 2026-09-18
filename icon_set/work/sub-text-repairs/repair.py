import json,io,math,shutil,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import Document,Path as SvgPath,Line,Arc
from icon_set.scripts.sub_ink32 import _snap,_bounds
D=Path('icon_set/work/sub-text-repairs');specs=json.loads((D/'specs.json').read_text());records=[]
for a in specs:
 old=Path(a['old']);shutil.copy2(old,D/'before'/old.name) if not (D/'before'/old.name).exists() else None
 raw=(D/(a['id']+'.raw.svg')).read_text()
 if '51708702' in a['id']:raw='<svg xmlns="http://www.w3.org/2000/svg" width="32"><path d="M2 16L30 16"/></svg>'
 paths=Document(io.StringIO(raw)).paths();width=math.ceil(float(ET.fromstring(raw).get('width')))
 # Cubic representation prevents SVG automatic radius correction. Points stay on grid.
 fitted=_snap(paths,preserve_arcs=False,width=width)
 if a['underline']:
  # Raw text already has 26-unit ink height. Leave 2 ink units above underline.
  fitted.append(SvgPath(Line(complex(2,30),complex(width-2,30))))
 if 'height-limit' in a['id']:
  # Retain the original opposed vertical chevrons, beside full-height lettering.
  x=width+6;fitted.append(SvgPath(Line(complex(x,2),complex(x+6,8)),Line(complex(x+6,8),complex(x+12,2))))
  fitted.append(SvgPath(Line(complex(x,30),complex(x+6,24)),Line(complex(x+6,24),complex(x+12,30))))
  width=x+14
 if 'wrench-size' in a['id']:
  source=Document(io.StringIO(Path(a['source']).read_text())).paths()[-1];l,t,r,b=source.bbox()[0],source.bbox()[2],source.bbox()[1],source.bbox()[3]
  factor=28/(b-t);part=source.scaled(factor).translated(complex(2-l*factor,2-t*factor));pw=math.ceil((r-l)*factor+4)
  parts=_snap([part],preserve_arcs=False,width=pw)
  fitted.extend(p.translated(complex(width+4,0)) for p in parts);width+=4+pw
 symbol='51708702' in a['id']
 if symbol:
  fitted=[SvgPath(Line(complex(x,16),complex(x,16))) for x in [2,16,30]];width=32
 l,t,r,b=_bounds(fitted)
 assert all(abs(z-round(z))<1e-7 for p in fitted for s in p for z in [s.start.real,s.start.imag,s.end.real,s.end.imag])
 assert l>=2-1e-7 and r<=width-2+1e-7 and t>=2-1e-7 and b<=30+1e-7
 assert symbol or abs(b-t+4-32)<1e-6,(a['id'],(l,t,r,b))
 root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(width),height='32',viewBox=f'0 0 {width} 32',fill='none',stroke='currentColor',**{'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
 ET.SubElement(root,'title').text=a['name']
 for p in fitted:ET.SubElement(root,'path',d=p.d())
 file=D/(a['id']+'.svg');file.write_text(ET.tostring(root,encoding='unicode'))
 records.append(dict(**a,repair_svg=str(file),symbol=symbol,ink32=dict(grid=1,stroke=4,canvas=32,canvas_width=width,ink_bounds=[l-2,t-2,r+2,b+2],ink_width=r-l+4,ink_height=b-t+4,bounds=[l,t,r,b])))
(D/'repairs.json').write_text(json.dumps(records,indent=2));print('Prepared',len(records),'repairs')
