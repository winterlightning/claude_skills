"""Verify exact shared-glyph reuse and repeated-letter consistency."""
import json,sys,hashlib,inspect
from pathlib import Path
from svgpathtools import parse_path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import build_paths
from icon_set.validation.envelope import visible_bounds
from text_designs import TEXT
c=json.loads((W/'candidates.json').read_text());reports={}
for n in (32,38,40):
 m=create(c[str(n)]['icon']);spec=TEXT[n];module=inspect.getmodule(type(m))
 assert tuple(module.TYPEFACE_GLYPH_IDS)==spec['glyphs']
 paths=[parse_path(p['d']) for p in build_paths(m.draw())]
 if n in (38,40):
  a,b=paths[:2];offset=b[0].start-a[0].start
  assert abs(offset.imag)<1e-9 and offset.real==round(offset.real)
  assert a==b.translated(-offset),'Repeated C glyph changed drawing'
  if n==38:canonical_c=a
  else:assert paths[0]==canonical_c,'C differs between CC and CCPA'
 bounds=visible_bounds(m.draw().primitives,radius=2);assert bounds[1]==0 and bounds[3]==32
 assert all(float(v).is_integer() for v in bounds)
 assert m.validate_icon().status=='valid'
 reports[n]={'glyph_ids':spec['glyphs'],'ink_bounds':bounds,'canvas_width':m.text_canvas_width,'repeat_geometry_identical':True if n!=32 else None,'shared_catalog_sha256':hashlib.sha256((ROOT/'icon_set/typeface/glyphs.json').read_bytes()).hexdigest()}
(W/'text-verification.json').write_text(json.dumps(reports,indent=2));print('3 shared-typeface profiles verified; repeated C geometry identical.')
