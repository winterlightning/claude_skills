from pathlib import Path
import sys,json,io
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
from PIL import Image,ImageDraw
WORK=Path(__file__).parent
rows=json.loads((WORK/'batch.json').read_text()); results=[]
for r in rows:
 i=create(r['icon_id']); report=i.validate_icon();results.append(dict(icon_id=i.icon_id,status=report.status,report=report.describe()))
 if report.status!='valid': print(i.icon_id,report.describe(),flush=True)
(WORK/'validation.json').write_text(json.dumps(results,indent=2))
print('Valid',sum(r['status']=='valid' for r in results),'/',len(results),flush=True)
for theme,ink,bg in [('light','#111111','#ffffff'),('dark','#f4f4f4','#16181c')]:
 for start in range(0,len(rows),25):
  sheet=Image.new('RGB',(1000,750),bg);d=ImageDraw.Draw(sheet)
  for j,r in enumerate(rows[start:start+25]):
   i=create(r['icon_id']); im=Image.open(io.BytesIO(render_png(i,ink=ink,scale=2)));native=Image.open(io.BytesIO(render_png(i,ink=ink)))
   x=j%5*200;y=j//5*150;sheet.paste(im,(x+20,y+5),im);sheet.paste(native,(x+135,y+45),native);d.text((x+4,y+110),f'{start+j+1}. '+r['parent'][:27],fill=ink)
  sheet.save(WORK/f'after-{theme}-{start//25+1}.png')
