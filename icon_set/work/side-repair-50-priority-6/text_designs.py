"""Reuse shared glyph definitions; only uniform sizing, layout and grid fitting."""
import json,math,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import parse_path, Path as SvgPath, Line, QuadraticBezier
from icon_set.scripts.sub_ink32 import _snap,_bounds
from icon_set.scripts.migrate_sub_profiles import primitive_calls
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/typeface/glyphs.json'
AUTHOR='gpt-6'
ROOT=Path(__file__).resolve().parents[3]
glyphs={g['icon_id']:g for g in json.loads((ROOT/SOURCE_PATH).read_text())['glyphs']}
TEXT={}
def make(n,ids):
 gs=[glyphs[i] for i in ids];top=min(g['bounds'][1] for g in gs);bottom=max(g['bounds'][3] for g in gs);scale=28/(bottom-top)
 paths=[];cursor=0
 for g in gs:
  l,t,r,b=g['bounds'];gw=math.ceil((r-l)*scale+4)
  raw=[parse_path(d).scaled(scale).translated(complex(2-l*scale,2-top*scale)) for d in g['paths']]
  # Snap each shared glyph once at the origin, then use integer translations.
  # Repeated shared glyphs retain identical curves in every text label.
  if g['icon_id'] in ('letter-a-uppercase','letter-w-uppercase'):
   # Center the symmetric shared A on an integer axis. Round its existing
   # quadratic control without clipping it: clipping destroys the round apex.
   axis=round(gw/2)
   centered=[parse_path(d).scaled(scale).translated(complex(axis-(l+r)*scale/2,2-top*scale)) for d in g['paths']]
   point=lambda z:complex(round(z.real),round(z.imag))
   fitted_glyph=[SvgPath(*[Line(point(v.start),point(v.end)) if isinstance(v,Line) else QuadraticBezier(point(v.start),point(v.control),point(v.end)) for v in path]) for path in centered]
  else:fitted_glyph=_snap(raw,preserve_arcs=False,width=gw)
  paths.extend(p.translated(complex(cursor,0)) for p in fitted_glyph)
  cursor+=gw+5
 width=cursor-5;fitted=paths;l,t,r,b=_bounds(fitted)
 assert abs(t-2)<1e-7 and abs(b-30)<1e-7
 root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',viewBox=f'0 0 {width} 32',width=str(width),height='32',fill='none',stroke='black',**{'stroke-width':'4'})
 for p in fitted:ET.SubElement(root,'path',d=p.d())
 body='\n'.join(primitive_calls(ET.tostring(root,encoding='unicode'),text=True))
 TEXT[n]=dict(width=width,bounds=(int(l-2),0,int(math.ceil(r+2)),32),glyphs=ids,body=body)
for n,ids in [(9,('letter-d-uppercase','letter-w-uppercase','letter-g-uppercase')),(10,('letter-w-uppercase','letter-a-uppercase','letter-v-uppercase'))]:make(n,ids)
