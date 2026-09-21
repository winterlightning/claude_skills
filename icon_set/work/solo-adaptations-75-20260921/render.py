import importlib.util,io,json,pathlib,sys
from PIL import Image,ImageDraw
ROOT=pathlib.Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.renderers.png import render_png
WORK=pathlib.Path(__file__).parent
rows=json.loads((WORK/'validation.json').read_text())
for k in range(0,len(rows),15):
 im=Image.new('RGB',(1200,((len(rows[k:k+15])+4)//5)*250),'#e8e8e8');d=ImageDraw.Draw(im)
 for j,row in enumerate(rows[k:k+15]):
  spec=importlib.util.spec_from_file_location('icon_set.model.icons.solo._candidate',row['candidate']);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);icon=mod.Drawing()
  x=j%5*240;y=j//5*250
  for theme,ink,bg,offset in [('light','#111111','#ffffff',0),('dark','#ffffff','#171717',120)]:
   for scale,yy in [(2,0),(1,105)]:
    pic=Image.open(io.BytesIO(render_png(icon,ink=ink,scale=scale)))
    im.paste(bg,(x+offset,y+yy,x+offset+116,y+yy+100 if scale==2 else y+yy+60));im.paste(pic,(x+offset+8,y+yy+3),pic)
    (WORK/'previews'/f"{row['number']}-{theme}-{scale}.png").write_bytes(render_png(icon,ink=ink,scale=scale))
  d.text((x+5,y+174),f"{row['number']} {row['status']}",fill='black')
  d.text((x+5,y+194),row['icon_id'][:30],fill='black')
 im.save(WORK/f'candidates-{k//15}.png')
