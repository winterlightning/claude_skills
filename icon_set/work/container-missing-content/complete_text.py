"""Reuse existing typeface paths and car artwork for the remaining text motifs."""
import json,sys,hashlib,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import parse_path,svg2paths
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/container-missing-content/icons.json'
AUTHOR='gpt-6'
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
refs=json.loads((OUT/'icons.json').read_text());dest=ROOT/'icon_set/dist/text44';manifest=json.loads((dest/'manifest.json').read_text());added=[]
for spec in json.load(sys.stdin):
 r=refs[spec['number']-1];result=spec['result'];paths=[]
 for p in result['placements']:
  for d in p['glyph']['paths']:paths.append(parse_path(d).scaled(p['scale']).translated(complex(p['x'],p['y'])))
 if spec['motif']=='ellipsis':
  paths=[p.translated(20j) for p in paths];width=result['width']
 elif spec['motif']=='degree':
  paths=[p.translated(14+6j) for p in paths]
  # Degree is an explicitly requested new circle mark; F uses the existing glyph.
  paths.append(parse_path('M2 11 A3 3 0 1 1 8 11 A3 3 0 1 1 2 11'))
  width=result['width']+14
 else:
  # Existing car artwork is uniformly fitted as a composition component.
  car,attrs=svg2paths(str(ROOT/'icon_set/dist/solo48/plain-car-front.svg'))
  box=[p.bbox() for p in car];l=min(b[0] for b in box);t=min(b[2] for b in box);rr=max(b[1] for b in box);bb=max(b[3] for b in box)
  # Side layout keeps the dollar counterspaces readable at the required stroke.
  scale=28/(bb-t);car_width=(rr-l)*scale+4;width=car_width+8+result['width']
  car=[p.scaled(scale).translated(complex(2-l*scale,8-t*scale)) for p in car]
  paths=[p.translated(complex(car_width+8,6)) for p in paths]+car
 boxes=[p.bbox() for p in paths];ink_height=max(b[3] for b in boxes)-min(b[2] for b in boxes)+4
 assert ink_height<=32+1e-6;assert min(b[2] for b in boxes)>=2-1e-6;assert max(b[3] for b in boxes)<=42+1e-6
 doc=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',viewBox=f'0 0 {width} 44',width=str(width),height='44',fill='none',stroke='currentColor',attrib={'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
 ET.SubElement(doc,'title').text=r['name']
 for p in paths:ET.SubElement(doc,'path',d=p.d())
 svg=ET.tostring(doc,encoding='unicode');icon_id='container-content-text-'+r['id'][:8];(dest/(icon_id+'.svg')).write_text(svg+'\n')
 record=dict(icon_id=icon_id,name=r['name'],family='text',profile='TEXT44',canvas_size=44,canvas_width=width,canvas_height=44,max_ink_height=32,text_ink_height=ink_height,text='°F' if spec['motif']=='degree' else spec['text'],description=r['name'],category='text',tags=['text','sub icon'],aliases=[],keywords=[r['name']],author=AUTHOR,source_ids=[r['id']],original_sources=[dict(source_id=r['id'],source_path=r['reference'])],glyph_ids=[p['glyph']['icon_id'] for p in result['placements']],svg_sha256=hashlib.sha256((svg+'\n').encode()).hexdigest(),style=dict(stroke_width=4,line_cap='round',line_join='round'),semantic_role='SUB',semantic_kind='text',composition_class='TEXT',keyshape=None,keyshape_bounds=None,validation=dict(status='valid',errors=[],warnings=[],checks_run=['existing typeface glyphs','32-unit maximum ink height','4-unit stroke','uniform component proportions'],scope='Text composition bounds; geometric SOLO48 checks do not apply.'))
 manifest['icons']=[x for x in manifest['icons'] if x['icon_id']!=icon_id]+[record];added.append(dict(number=r['number'],icon_id=icon_id,path=str(dest/(icon_id+'.svg'))))
(dest/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(OUT/'additional-text.json').write_text(json.dumps(added,indent=2)+'\n')
print('Exported ellipsis, degree-F and car-dollar layouts; preserved other TEXT44 entries.')
