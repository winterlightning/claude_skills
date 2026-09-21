import json,hashlib,sqlite3,io
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
from icon_set.scripts.workspace import DEFAULT_DIST,DEFAULT_DATABASE
from icon_set.scripts.primitive_status import load_status,merge
p=Path(__file__).parent
models=json.loads((p/'models.json').read_text())
names=[Path(f).read_text().split('icon_id = ')[1].splitlines()[0].strip("\"'") for f in models]
manifest=json.loads((DEFAULT_DIST/'solo48/manifest.json').read_text())
rows={r['icon_id']:r for r in manifest['icons']}
verified=[]
for name in names:
 r=rows[name]; svg=DEFAULT_DIST/'solo48'/f'{name}.svg'
 assert r['validation']['status']=='valid' and not r['validation']['errors'] and not r['validation']['warnings']
 assert hashlib.sha256(svg.read_bytes()).hexdigest()==r['svg_sha256']
 verified.append(dict(icon_id=name,svg=str(svg),validation=r['validation']['status'],warnings=r['validation']['warnings']))
for theme,bg,fg in [('light','#ffffff','#141413'),('dark','#1c1c19','#f5f4ef')]:
 sheet=Image.new('RGB',(800,225),bg);d=ImageDraw.Draw(sheet)
 for n,name in enumerate(names):
  raw=(DEFAULT_DIST/'solo48'/f'{name}.svg').read_text().replace('currentColor',fg)
  for size,offset in [(96,(n*200+15,15)),(48,(n*200+130,110))]:
   im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=raw.encode(),output_width=size,output_height=size)))
   sheet.paste(im,offset,im)
  d.text((n*200+8,180),name[:27],fill=fg)
 sheet.save(p/f'export-{theme}.png')
with sqlite3.connect(DEFAULT_DATABASE) as c:statuses=load_status(c)
ids=json.loads((p/'ids.json').read_text())
catalog=json.loads((DEFAULT_DIST/'gallery/primitives.json').read_text())
final=[r for r in merge(catalog['rows'],statuses) if r['uuid'] in ids]
assert len(final)==10
assert sum(r['status']=='generated' for r in final)==4
assert sum(r['status']=='skip' for r in final)==6
(p/'final-status.json').write_text(json.dumps(final,indent=2))
(p/'exports-verified.json').write_text(json.dumps(verified,indent=2))
print(json.dumps(verified,indent=2))
print('Final gallery: 4 generated, 5 prepared combinations, 1 uncertain; 0 TODO.')
