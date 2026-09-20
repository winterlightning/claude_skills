"""Check repeated shared glyphs and exact ink height without creating letters."""
import json,sys,hashlib,inspect
from pathlib import Path
from svgpathtools import parse_path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import build_paths
from icon_set.validation.envelope import visible_bounds
from text_designs import TEXT,glyphs
c=json.loads((W/'candidates.json').read_text());reports={};seen={}
for n,spec in TEXT.items():
 m=create(c[str(n)]['icon']);module=inspect.getmodule(type(m))
 assert tuple(module.TYPEFACE_GLYPH_IDS)==spec['glyphs']
 paths=[parse_path(p['d']) for p in build_paths(m.draw())]
 index=0
 for gid in spec['glyphs']:
  count=len(glyphs[gid]['paths']);part=paths[index:index+count];index+=count
  anchor=part[0][0].start;normalized=[p.translated(-anchor) for p in part]
  if gid in seen:assert normalized==seen[gid],f'Shared glyph differs: {gid}'
  else:seen[gid]=normalized
 assert index==len(paths)
 bounds=visible_bounds(m.draw().primitives,radius=2);assert bounds[1]==0 and bounds[3]==32
 assert all(float(v).is_integer() for v in bounds)
 assert m.validate_icon().status=='valid'
 reports[n]={'glyph_ids':spec['glyphs'],'ink_bounds':bounds,'canvas_width':m.text_canvas_width,'repeated_glyph_geometry_identical':True,'shared_catalog_sha256':hashlib.sha256((ROOT/'icon_set/typeface/glyphs.json').read_bytes()).hexdigest()}
(W/'text-verification.json').write_text(json.dumps(reports,indent=2));print('6 shared-typeface profiles verified; repeated glyph geometry identical.')
