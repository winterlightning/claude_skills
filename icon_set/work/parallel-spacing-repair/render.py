import json
from pathlib import Path
from PIL import Image,ImageDraw
from io import BytesIO
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
w=Path('icon_set/work/parallel-spacing-repair'); a=json.loads((w/'targets.json').read_text())
for offset in range(0,len(a),16):
 sheet=Image.new('RGB',(960,800),'#f5f5f2'); d=ImageDraw.Draw(sheet)
 for j,row in enumerate(a[offset:offset+16]):
  icon=create(row['icon_id']);im=Image.open(BytesIO(render_png(icon,scale=3))).convert('RGBA');x=(j%4)*240;y=(j//4)*200
  sheet.paste(im,(x+48,y+12),im);d.text((x+8,y+165),str(offset+j)+' '+icon.icon_id[:32],fill='black')
 sheet.save(w/f'after-{offset//16}.png')
