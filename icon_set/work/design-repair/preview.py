from pathlib import Path
import json,sys,io,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
from PIL import Image,ImageDraw,ImageFont
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/design-repair/mapping.json'
AUTHOR='gpt-6'
rows=json.loads((W/'mapping.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',13)
results=[]
for r in rows:
 obj=create(r['id']);report=obj.validate_icon().describe();results.append(dict(r,validation=report));(W/(r['id']+'.svg')).write_text(obj.to_svg());print(r['id'],report)
(W/'results.json').write_text(json.dumps(results,indent=2))
for theme,bg,fg in [('light','#f7f6f2','#202226'),('dark','#17191d','#f1f2f5')]:
 im=Image.new('RGB',(1250,1060),bg);d=ImageDraw.Draw(im);d.text((20,15),'DESIGN REPAIRS — 48px native + 2× inspection',font=font,fill=fg)
 for i,r in enumerate(results):
  x=i%5*250;y=i//5*200+45;obj=create(r['id'])
  for scale,dx,dy in [(2,28,12),(1,158,60)]:
   tile=Image.open(io.BytesIO(render_png(obj,ink=fg,scale=scale)));im.paste(tile,(x+dx,y+dy),tile)
  d.text((x+12,y+128),r['original'],font=font,fill=fg);d.text((x+12,y+151),'PASS' if r['validation']=='status: valid' else r['validation'].splitlines()[0],font=font,fill=fg)
 im.save(W/f'preview-{theme}.png')
# Six before/after sheets make changes reviewable without changing the old artifacts.
for start in range(0,25,5):
 group=results[start:start+5];im=Image.new('RGB',(1250,300),'#f7f6f2');d=ImageDraw.Draw(im)
 for i,r in enumerate(group):
  x=i*250;d.text((x+10,15),r['original'],font=font,fill='#202226')
  for j,ident in enumerate([r['original'],r['id']]):
   tile=Image.open(io.BytesIO(render_png(create(ident),ink='#202226',scale=2)));im.paste(tile,(x+12+j*125,60),tile);d.text((x+12+j*125,175),'Before' if j==0 else 'After',font=font,fill='#202226')
 im.save(W/f'compare-{start//5+1}.png')
