"""Fit shared glyphs on expanded canvases without the 32px migration clip."""
import json,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import parse_path,Path as SvgPath,Line,CubicBezier,QuadraticBezier
from icon_set.scripts.migrate_sub_profiles import primitive_calls
ROOT=Path(__file__).resolve().parents[3]
GLYPHS={g['icon_id']:g for g in json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())['glyphs']}
def fit(gid,height,cx,cy,prefix='g',width=64):
 g=GLYPHS[gid];l,t,r,b=g['bounds'];scale=height/(b-t);paths=[]
 def snap(z):return complex(round(z.real),round(z.imag))
 for d in g['paths']:
  p=parse_path(d).scaled(scale).translated(complex(cx-(l+r)*scale/2,cy-(t+b)*scale/2));parts=[]
  for s in p:
   if isinstance(s,Line):parts.append(Line(snap(s.start),snap(s.end)))
   elif isinstance(s,CubicBezier):parts.append(CubicBezier(snap(s.start),s.control1,s.control2,snap(s.end)))
   elif isinstance(s,QuadraticBezier):parts.append(QuadraticBezier(snap(s.start),s.control,snap(s.end)))
   else:raise ValueError('Unsupported glyph segment')
  paths.append(SvgPath(*parts))
 root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',viewBox=f'0 0 {width} 32')
 for p in paths:ET.SubElement(root,'path',d=p.d())
 body='\n'.join(primitive_calls(ET.tostring(root,encoding='unicode'),text=True)).replace("'p","'"+prefix+'-p')
 for i,a in enumerate(paths):
  for j,b in enumerate(paths[:i]):
   if gid=='letter-a-uppercase' or a.intersect(b):body+=f"\nself.relate('connect','{prefix}-path-{i+1}-1','{prefix}-path-{j+1}-1')"
 return body,paths
