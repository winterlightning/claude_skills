"""Build lettering on a 24-unit visible-height grid from source centerlines.

Preserve smooth curves, then fit the complete stroke envelope to integer width.
The unrelated SOLO48 registry remains historical.
"""
from pathlib import Path
import json
import sys
import hashlib
import math
import xml.etree.ElementTree as ET
from svgpathtools import parse_path, Path as SVGPath, Line, CubicBezier, Arc

ROOT=Path(__file__).resolve().parents[2]
if __package__ in (None, ""):
    sys.path.insert(0, str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='Letters/'
AUTHOR='gpt-6'

# Source-space semantic bands, measured from the reference bodies. Dots,
# ascenders and descenders do not participate. j's baseline is an optical
# estimate from the i-sized body, above its compact hook.
BANDS={'B':(372.506,855.5),'D':(372.506,855.5),'F':(357,859),
       'G':(128,632.183),'H':(371.5,852.5),'I':(373.56,851.06),
       'J':(242.5,720),'K':(369.984,852.984),'L':(368,853),
       'P':(133,618.501),'Q':(133,618.501),'T':(364,859),
       'Y':(133,687.216)}

# Targeted repairs: coherent outlines replace exporter fragments; all dimensions
# follow source proportions rather than a prescribed envelope.
REPAIRS={
 '0':['M262 358 A250 205 0 0 1 762 358 L762 666 A250 205 0 0 1 262 666 Z'],
 'E':['M755 512.5 C755 378.571 646.429 270 512.5 270 C378.571 270 270 378.571 270 512.5 C270 646.429 378.571 755 512.5 755 C601.9 755 679.9 706.7 721.886 634.905','M270 512.5 L755 512.5'],
 'H':['M289 171 V852.5','M289 594.391 C289 471.292 388.792 371.5 511.891 371.5 C634.991 371.5 734.782 471.292 734.782 594.391 V852.5'],
 'I':['M512 173.7815 L512 173.7815','M512 373.56 V851.06'],
 'J':['M423 999.235 C540.967 999.235 600.541 1009.77 600.541 898.033 V242.5','M600.541 44.25 L600.541 44.25'],
 'K':['M308 171 V852.984','M716.293 369.984 L308 564.851 L716.293 852.984'],
 'M':['M512.293 443.146 V755.126','M162 755.126 V443.146 C162 346.416 240.416 268 337.146 268 C433.877 268 512.293 346.416 512.293 443.146 C512.293 346.416 590.709 268 687.439 268 C784.17 268 862.586 346.416 862.586 443.146 V755.126'],
 'V':['M297 269.82 L467.25 715.574 C477.5 742.4 493 755 513 755 C533 755 544.671 746 554 721.5 L726.305 269'],
 'Y':['M254 133 C289.067 194.852 451.53 532.586 527.023 687.216','M769.429 133 L510.946 723.972 C510.946 723.972 472.394 803.426 414.278 844.668 C368.319 877.282 275.578 891 275.578 891'],
}

def ellipse(cx,cy,rx,ry):
 return parse_path(f'M{cx-rx} {cy} A{rx} {ry} 0 1 1 {cx+rx} {cy} A{rx} {ry} 0 1 1 {cx-rx} {cy} Z')

def source_paths(source):
 if source.stem in REPAIRS:return [parse_path(d) for d in REPAIRS[source.stem]]
 paths=[]
 for el in ET.parse(source).getroot():
  tag=el.tag.rsplit('}',1)[-1]
  if tag=='path' and el.get('stroke'):
   for run in parse_path(el.attrib['d']).continuous_subpaths():
    # Exporter crumbs on bowls are <= .003 units, far below source stroke 87.
    segments=[s for s in run if s.length()>0.05]
    if segments:paths.append(SVGPath(*segments))
  elif tag in ('ellipse','circle'):
   cx,cy=float(el.get('cx')),float(el.get('cy'))
   rx=float(el.get('rx',el.get('r')));ry=float(el.get('ry',el.get('r')))
   # The sole transformed ellipse is rotated 180° about its own center.
   if el.get('transform') and not el.get('transform').startswith('rotate(180 '):raise ValueError('Unexpected ellipse transform')
   paths.append(ellipse(cx,cy,rx,ry))
 return paths

def bounds(paths):
 boxes=[p.bbox() for p in paths]
 return [min(b[0] for b in boxes),min(b[2] for b in boxes),max(b[1] for b in boxes),max(b[3] for b in boxes)]

def canonical(icon_id,character,kind,paths,band=None,source=None,preferred=True):
 full=bounds(paths);top,baseline=band or (full[1],full[3])
 target=24 if kind in ('lowercase','symbol') else 24*52/36
 scale=target/(baseline-top)
 # Uniform similarity only: no independent x/y stretching. Place the natural
 # ink envelope at center for preview; the preview viewBox can expand freely.
 transformed=[p.scaled(scale).translated(complex(24-(full[0]+full[2])*scale/2,24-(full[1]+full[3])*scale/2)) for p in paths]
 dy=24-(full[1]+full[3])*scale/2
 box=bounds(transformed)
 ds=[p.d() for p in transformed]
 identity=hashlib.sha256(json.dumps(ds,separators=(',',':')).encode()).hexdigest()
 return dict(icon_id=icon_id,character=character,kind=kind,preferred=preferred,
             body_top=top*scale+dy,baseline=baseline*scale+dy,body_height=target,
             bounds=box,measurement='source-body-band' if band else 'natural-stroke-bounds',
             paths=ds,preview_box=[min(0,box[0]-3),min(0,box[1]-3),max(48,box[2]+3)-min(0,box[0]-3),max(48,box[3]+3)-min(0,box[1]-3)],svg_sha256=identity,source_path=str(source.relative_to(ROOT)) if source else None,
             source_sha256=hashlib.sha256(source.read_bytes()).hexdigest() if source else None,
             author=AUTHOR,geometry_policy='natural-proportions-no-keyshape',
             construction='Repaired source fragments; retained curve character' if source and source.stem in REPAIRS else 'Source centerlines with subpixel crumbs removed' if source else 'Keyboard symbol on shared body and baseline band' if kind=='symbol' else 'Matching uppercase monoline construction')

# Uppercase definitions share natural cap height, but have independent widths.
# Smooth bowls use coherent elliptical/cubic curves; thin letters stay narrow.
CAPS={
'A':['M10 42 L22.5 6 Q24 3 25.5 6 L38 42','M15.5 26 H32.5'],
'B':['M12 42 V6 H24 C39 6 39 24 24 24 H12','M24 24 C40 24 40 42 24 42 H12'],
'C':['M33.192388 11.272078 A13 18 0 1 0 33.192388 36.727922'],
'D':['M12 6 H22 C42 6 42 42 22 42 H12 Z'],
'E':['M35 6 H13 V42 H35','M13 24 H31'],
'F':['M35 6 H13 V42','M13 24 H31'],
'G':['M33.192388 11.272078 A13 18 0 1 0 37 24 H27'],
'H':['M11 6 V42','M37 6 V42','M11 24 H37'],
'I':['M18 6 H30','M24 6 V42','M18 42 H30'],
'J':['M18 6 H33 V31 C33 46 15 47 12 36'],
'K':['M12 6 V42','M37 6 L12 25 L37 42'],
'L':['M14 6 V42 H35'],
'M':['M7 42 V6 L24 29 L41 6 V42'],
'N':['M11 42 V6 L37 42 V6'],
'O':['M11 24 A13 18 0 1 1 37 24 A13 18 0 1 1 11 24 Z'],
'P':['M12 42 V6 H25 C41 6 41 25 25 25 H12'],
'Q':['M11 24 A13 18 0 1 1 37 24 A13 18 0 1 1 11 24 Z','M28 33 L39 46'],
'R':['M12 42 V6 H25 C41 6 41 25 25 25 H12','M25 25 L38 42'],
'S':['M35 11 C32 4 14 3 12 15 C10 27 35 21 36 33 C37 46 16 47 11 38'],
'T':['M10 6 H38','M24 6 V42'],
'U':['M11 6 V29 C11 47 37 47 37 29 V6'],
'V':['M10 6 L22 40 Q24 46 26 40 L38 6'],
'W':['M5 6 L13 40 Q14 44 15 40 L23 9 Q24 5 25 9 L33 40 Q34 44 35 40 L43 6'],
'X':['M11 6 L37 42','M37 6 L11 42'],
'Y':['M10 6 L24 25 L38 6','M24 25 V42'],
'Z':['M13 6 H34 Q36 6 34.5 8 L13.5 40 Q12 42 14 42 H35'],
}

GEOMETRY_POLICY = 'grid-ink-height24'


def fit_base_grid(glyph):
 """Fit the complete round-stroke envelope to height 24 and integer width.

 Keep semantic body metrics for text layout, but size by the whole glyph.
 Flat marks have no path height: their stroke must supply the 24-unit height.
 """
 glyph = dict(glyph)
 left, top, right, bottom = glyph['bounds']
 width, height = right-left, bottom-top
 stroke = 4 if height > 1e-9 else 24
 sy = (24-stroke)/height if height > 1e-9 else 24/glyph.get('stroke_width', 4)
 ink_width = max(stroke, math.floor(width*sy+stroke+0.5))
 sx = (ink_width-stroke)/width if width > 1e-9 else sy
 def scale_point(p):
  return complex(p.real*sx, p.imag*sy)
 transformed = []
 offset = complex(stroke/2-left*sx, stroke/2-top*sy)
 for d in glyph['paths']:
  segments = []
  for segment in parse_path(d):
   if isinstance(segment, Arc):
    # All source ellipses are axis aligned. Preserve their exact curves.
    if segment.rotation % 180:
     raise ValueError('Grid fitting requires an axis-aligned ellipse')
    segment = Arc(scale_point(segment.start), scale_point(segment.radius),
                  segment.rotation, segment.large_arc, segment.sweep,
                  scale_point(segment.end))
   else:
    segment = segment.scaled(sx, sy)
   segments.append(segment.translated(offset))
  transformed.append(SVGPath(*segments))
 paths = [p.d() for p in transformed]
 glyph.update(paths=paths, bounds=bounds(transformed),
              body_top=stroke/2+(glyph['body_top']-top)*sy,
              baseline=stroke/2+(glyph['baseline']-top)*sy,
              body_height=glyph['body_height']*sy,
              stroke_width=stroke, ink_width=ink_width, ink_height=24,
              preview_box=[0, 0, ink_width, 24],
              geometry_policy=GEOMETRY_POLICY,
              svg_sha256=hashlib.sha256(json.dumps(paths,separators=(',',':')).encode()).hexdigest())
 return glyph


def build():
 glyphs=[]
 for source in sorted((ROOT/'Letters').glob('*.svg')):
  stem=source.stem;kind='digit' if stem.isdigit() else 'lowercase'
  char=stem[0].lower();suffix='-large' if stem=='o' else ''
  icon_id=('digit-' if kind=='digit' else 'letter-')+char+suffix
  glyphs.append(canonical(icon_id,char,kind,source_paths(source),BANDS.get(stem),source,stem!='o'))
 for char,ds in CAPS.items():
  glyphs.append(canonical('letter-'+char.lower()+'-uppercase',char,'uppercase',
                          [parse_path(d) for d in ds],(6,42) if char=='Q' else None))
 if __package__:
  from .typeface_symbols import SYMBOLS
 else:
  from typeface_symbols import SYMBOLS
 for char,(name,ds) in SYMBOLS.items():
  glyphs.append(canonical('symbol-'+name,char,'symbol',[parse_path(d) for d in ds],(18,42)))
 # Preserve exact glyph paths recovered from existing approved text artwork.
 glyphs.extend(json.loads((ROOT/'icon_set/typeface/reused-glyphs.json').read_text()))
 glyphs = [fit_base_grid(glyph) for glyph in glyphs]
 target=ROOT/'icon_set/typeface/glyphs.json';target.parent.mkdir(exist_ok=True)
 from icon_set.typeface.sub32 import PROFILE_VARIANTS
 target.write_text(json.dumps({'schema_version':3,'geometry_policy':GEOMETRY_POLICY,'glyphs':glyphs,'profile_variants':PROFILE_VARIANTS},indent=2)+'\n')
 print(f'Built {len(glyphs)} grid-fitted 24-unit glyphs -> {target}')

if __name__=='__main__':build()
