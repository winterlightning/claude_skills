import json,io,math,textwrap
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import cairosvg
from .check_drafts import load
from icon_set.renderers.svg import render_svg
OUT=Path(__file__).resolve().parent
rows=json.loads((OUT/'batch.json').read_text());dest=OUT/'previews';dest.mkdir(exist_ok=True)
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',11)
for r in rows:
 for side,ident in [('before',r['icon_id']),('after',r.get('variant_id',r['icon_id']))]:
  svg=render_svg(load(r,side)());(dest/f'{r["batch_index"]}-{side}.svg').write_text(svg)
for theme in ['light','dark']:
 for start in range(0,len(rows),25):
  bg='#fff' if theme=='light' else '#171c22';fg='#171c22' if theme=='light' else '#f7f8fa'
  im=Image.new('RGB',(1500,850),bg);d=ImageDraw.Draw(im)
  for j,r in enumerate(rows[start:start+25]):
   x=j%5*300;y=j//5*170
   for k,side in enumerate(['before','after']):
    svg=(dest/f'{r["batch_index"]}-{side}.svg').read_text()
    # Render the same model in each theme; exported source remains canonical.
    for size,dy in [(72,6),(48,88)]:
     pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)))
     ink=Image.new('RGBA',pic.size,fg);ink.putalpha(pic.getchannel('A'))
     im.paste(ink,(x+36+k*140,y+dy),ink)
   for k,line in enumerate(textwrap.wrap(str(r['batch_index'])+'. '+r['icon_id']+(' • revised' if r.get('variant_id') else ''),44)[:2]):d.text((x+5,y+140+k*12),line,fill=fg,font=font)
   d.rectangle((x,y,x+299,y+169),outline='#999')
  im.save(OUT/f'{theme}-{start//25+1}.png')
print('Rendered all 100 models before/after in both themes, including native 48px.')
