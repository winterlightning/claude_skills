import json,hashlib,sys
sys.path.insert(0,str(__import__("pathlib").Path.cwd()))
from pathlib import Path
import cairosvg
from icon_set.model.icons.registry import create
from icon_set.model.profiles import STROKE
p=Path(__file__).resolve().parent
id='chevron-double-down-with-wide-arms'
m=json.loads(Path('published/sub32/manifest.json').read_text())
row=next(r for r in m['icons'] if r.get('icon_id')==id)
ic=create(id);r=ic.validate_icon();f=Path('published/sub32')/(id+'.svg');svg=f.read_text()
data={'icon_id':id,'status':r.status,'warnings':len(r.warnings),'errors':len(r.errors),'manifest_entry':row,'matches_model':svg==ic.to_svg(),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
assert r.status=='valid' and not r.warnings and not r.errors
assert data['matches_model']
(p/'export-verification.json').write_text(json.dumps(data,indent=2))
for theme,color,bg in [('light','#111','white'),('dark','#eee','#171717')]:
 for size in [32,192]:
  cairosvg.svg2png(bytestring=svg.replace('stroke="'+STROKE+'"','stroke="'+color+'"').encode(),write_to=str(p/f'09-export-{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
print(json.dumps(data,indent=2))
