from pathlib import Path
import json,io,sys
from PIL import Image,ImageDraw
import cairosvg
p=Path(__file__).resolve().parent
claims=json.loads((p/'claims.json').read_text())
runs=json.loads((p/'runs.json').read_text()) if (p/'runs.json').exists() else {}
for start in range(0,len(claims),5):
 sheet=Image.new('RGB',(1040,1125),'#eee');d=ImageDraw.Draw(sheet)
 for j,e in enumerate(claims[start:start+5]):
  i=start+j+1;y=j*225;r=runs.get(str(i));d.text((5,y+2),str(i)+' '+e['key']+(' / '+r['status']+' / '+r['gate'] if r else ''),fill='black')
  for k,src in enumerate([Path(e['reference']),Path(e['result_dir'])/'before'/f"{e['item']['icon_id']}.svg"]):
   im=Image.open(io.BytesIO(cairosvg.svg2png(url=str(src),output_width=150,output_height=150,background_color='#ffffff')));sheet.paste(im,(10+k*215,y+48));d.text((10+k*215,y+27),'Reference' if k==0 else 'Rejected',fill='black')
  if r:
   for k,theme in enumerate(['light','dark']):
    im=Image.open(Path(r['run'])/f'preview-{theme}-384.png').resize((150,150));sheet.paste(im,(440+k*295,y+48));sheet.paste(Image.open(Path(r['run'])/f'preview-{theme}-48.png'),(620+k*295,y+90));d.text((440+k*295,y+27),'Fixed / '+theme,fill='black')
 sheet.save(p/f"{sys.argv[1] if len(sys.argv)>1 else 'comparison'}-{start//5+1}.png")
