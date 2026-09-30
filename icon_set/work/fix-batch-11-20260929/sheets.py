from pathlib import Path
from PIL import Image,ImageDraw
import json
root=Path(__file__).parent;rs=json.loads((root/'runs.json').read_text())[5:]
for batch in range(3):
 sheet=Image.new('RGB',(740,1000),'#ddd');d=ImageDraw.Draw(sheet)
 for i,r in enumerate(rs[batch*5:batch*5+5]):
  p=Path(r['run']);d.text((8,i*200+5),r['icon_id'],fill='black')
  for j,t in enumerate(['light','dark']):
   if (p/f'preview-{t}-384.png').exists():
    sheet.paste(Image.open(p/f'preview-{t}-384.png').resize((156,156)),(j*370+10,i*200+28));sheet.paste(Image.open(p/f'preview-{t}-48.png'),(j*370+205,i*200+80))
 sheet.save(root/f'remaining-candidates-{batch}.png')
