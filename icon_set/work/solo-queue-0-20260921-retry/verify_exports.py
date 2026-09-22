from pathlib import Path
from icon_set.model.icons.registry import create
from icon_set.scripts.workspace import DEFAULT_DIST
from icon_set.scripts import contact_sheet
import json,cairosvg,xml.etree.ElementTree as ET,hashlib
from PIL import Image,ImageDraw
w=Path(__file__).parent
ids=['litter-tray-with-slotted-scoop','open-front-hooded-cloak','pick-entering-open-padlock']
icons=[create(uid) for uid in ids]
manifest={row['icon_id']:row for row in json.loads((DEFAULT_DIST/'solo48/manifest.json').read_text())['icons']}
checks=[]
for icon in icons:
 row=manifest[icon.icon_id];r=icon.validate_icon()
 assert r.status=='valid' and not r.errors and not r.warnings
 assert row['validation']['status']=='valid' and not row['validation']['warnings'] and not row['validation']['errors']
 f=DEFAULT_DIST/'solo48'/(icon.icon_id+'.svg');svg=f.read_text()
 def paths(s):return [x.attrib for x in ET.fromstring(s).iter() if x.tag.endswith('path')]
 assert paths(svg)==paths(icon.to_svg()),icon.icon_id+' export differs from source'
 assert hashlib.sha256(f.read_bytes()).hexdigest()==row['svg_sha256']
 checks.append({'icon_id':icon.icon_id,'export':str(f),'keyshape':row['keyshape'],'status':'valid','errors':0,'warnings':0,'current_geometry_matches':True,'manifest_sha256_matches':True})
contact_sheet.icons_in=lambda family:iter(icons)
for theme,bg,ink in [('light','#ffffff','#141413'),('dark','#1c1c19','#f5f4ef')]:
 svg=contact_sheet.render_sheet(theme,columns=3,family='solo');(w/f'review-{theme}.svg').write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(w/f'review-{theme}.png'))
 sheet=Image.new('RGB',(600,230),bg);d=ImageDraw.Draw(sheet)
 for j,uid in enumerate(ids):
  root=ET.fromstring((DEFAULT_DIST/'solo48'/(uid+'.svg')).read_text())
  for elem in root.iter():
   if elem.get('stroke') and elem.get('stroke')!='none':elem.set('stroke',ink)
  paint=ET.tostring(root)
  for size,x,y in [(120,j*200+40,10),(48,j*200+76,145)]:
   cairosvg.svg2png(bytestring=paint,write_to='/tmp/queue0-export.png',output_width=size,output_height=size,background_color=bg);sheet.paste(Image.open('/tmp/queue0-export.png'),(x,y))
  d.text((j*200+10,207),['Litter tray','Hooded cloak','Lock pick'][j],fill=ink)
 sheet.save(w/f'exports-{theme}.png')
(w/'export-verification.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
