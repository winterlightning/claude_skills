import json,importlib,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
import cairosvg
from PIL import Image,ImageDraw
out=Path(__file__).parent
paths=json.loads((out/'modules.json').read_text()); results=[]
for theme in ['light','dark']:
 sheet=Image.new('RGB',(1000,500),'white' if theme=='light' else '#191919');d=ImageDraw.Draw(sheet)
 for i,path in enumerate(paths):
  p=Path(path);icon=importlib.import_module('.'.join(p.with_suffix('').parts)).Drawing()
  if theme=='light':
   r=icon.validate_icon();text=r.describe();print(str(i+1)+' '+icon.icon_id+' '+text);(out/(icon.icon_id+'-validation.txt')).write_text(text);results.append({'path':path,'id':icon.icon_id,'status':r.status,'warnings':len(r.warnings)})
  svg=icon.to_svg();(out/(icon.icon_id+'.svg')).write_text(svg)
  for size,ox,oy in [(128,24,10),(48 if icon.family=='solo' else 32,65,150)]:
   png=out/(icon.icon_id+'-'+theme+'-'+str(size)+'.png')
   cairosvg.svg2png(bytestring=svg.replace('currentColor','#111111' if theme=='light' else '#ffffff').encode(),write_to=str(png),output_width=size,output_height=size)
   im=Image.open(png);sheet.paste(im,((i%5)*200+ox,(i//5)*250+oy),im)
  d.text(((i%5)*200+5,(i//5)*250+205),str(i+1)+'. '+icon.icon_id[:24],fill='black' if theme=='light' else 'white')
 sheet.save(out/('redraws-'+theme+'.png'))
(out/'validation.json').write_text(json.dumps(results,indent=2))
