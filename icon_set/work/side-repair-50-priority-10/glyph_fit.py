"""Shared glyph reuse and small-size grid fitting; no per-icon replacement letters."""
import json,math,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import parse_path, Path as SvgPath, Line, QuadraticBezier, CubicBezier
from icon_set.scripts.sub_ink32 import _snap,_bounds
from icon_set.scripts.migrate_sub_profiles import primitive_calls
ROOT=Path(__file__).resolve().parents[3]
GLYPHS={g['icon_id']:g for g in json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())['glyphs']}
def hinted_paths(g):
 out=[]
 for d in g['paths']:
  p=parse_path(d)
  if g['icon_id'] in ('letter-w-uppercase','symbol-won-one-bar') and any(isinstance(s,QuadraticBezier) for s in p):
   # A turn smaller than the 4px stroke is represented by the same extremum
   # and the renderer's round join. All W uses share this optical treatment.
   vertices=[p[0].start]
   for i,s in enumerate(p):
    if isinstance(s,QuadraticBezier):vertices.append(s.point(.5))
    elif i==len(p)-1 or not isinstance(p[i+1],QuadraticBezier):vertices.append(s.end)
   # Remove the pre-turn line endpoint when replaced by its rounded extremum.
   out.append(SvgPath(*[Line(a,b) for a,b in zip(vertices,vertices[1:]) if a!=b]))
  else:out.append(p)
 return out

def fit(gid,height,cx,cy,prefix='g',width=32):
 g=GLYPHS[gid];l,t,r,b=g['bounds'];s=height/(b-t)
 paths=[p.scaled(s).translated(complex(cx-(l+r)*s/2,cy-(t+b)*s/2)) for p in hinted_paths(g)]
 # Integer-grid optical fitting separates the percent counters from its slash.
 # Shift whole counters, preserving their curves and dimensions.
 if gid == 'symbol-percent':
  midpoint=cx
  for i,p in enumerate(paths):
   bb=p.bbox()
   if abs(p.start-p.end)<1e-7:
    paths[i]=p.translated(complex(-1 if (bb[0]+bb[1])/2<midpoint else 1,0))
 fitted=_snap(paths,preserve_arcs=False,width=width)
 root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',viewBox=f'0 0 {width} 32')
 for p in fitted:ET.SubElement(root,'path',d=p.d())
 body='\n'.join(primitive_calls(ET.tostring(root,encoding='unicode'),text=True)).replace("'p",repr(prefix)[0]+prefix+'-p')
 # Additional declarations are limited to actual intersections of emitted
 # glyph strokes (currency crossbars and stems).
 for i,a in enumerate(fitted):
  for j,bp in enumerate(fitted[:i]):
   try:touch=bool(a.intersect(bp))
   except (AssertionError,ValueError,ZeroDivisionError):touch=False
   if touch:body+=f"\nself.relate('connect','{prefix}-path-{i+1}-1','{prefix}-path-{j+1}-1')"
 return body,fitted

def text(ids):
 # Uniform shared cap-height sizing; retain natural width and integer advance.
 top=min(GLYPHS[x]['bounds'][1] for x in ids);bottom=max(GLYPHS[x]['bounds'][3] for x in ids);scale=28/(bottom-top)
 bodies=[];cursor=0;allpaths=[]
 for i,gid in enumerate(ids):
  g=GLYPHS[gid];l,t,r,b=g['bounds'];gw=math.ceil((r-l)*scale+4)
  cx=cursor+2+(r-l)*scale/2;cy=2+((t+b)/2-top)*scale
  body,paths=fit(gid,(b-t)*scale,cx,cy,f'g{i}',width=1000);bodies.append(body);allpaths+=paths;cursor+=gw+5
 l,t,r,b=_bounds(allpaths)
 assert abs(t-2)<1e-7 and abs(b-30)<1e-7,(ids,t,b)
 return {'body':'\n'.join(bodies),'width':max(cursor-5,math.ceil(r+2)),'bounds':(int(l-2),0,int(math.ceil(r+2)),32),'glyphs':tuple(ids)}
