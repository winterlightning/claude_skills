from author import ROOT,REPO,ROWS
from PIL import Image,ImageDraw
import json
for start in range(0,20,5):
 sheet=Image.new('RGB',(1050,5*235),'#eeeeee');d=ImageDraw.Draw(sheet)
 for j in range(start,min(start+5,20)):
  m=json.loads((ROOT/f'latest-{j+1}.json').read_text());out=REPO/m['result_dir'];y=(j-start)*235
  d.text((8,y+3),f"{j+1}. {m['icon_id']} [{m['validation_status']}/{m['build_gate']['status']}]",fill='black')
  for k,t in enumerate(['light','dark']):
   for size,x in [(384,20+k*460),(48,240+k*460)]:
    im=Image.open(out/f'preview-{t}-{size}.png').convert('RGB')
    if size==384:im=im.resize((192,192))
    sheet.paste(im,(x,y+30))
 sheet.save(ROOT/f'after-{start//5+1}.png')
