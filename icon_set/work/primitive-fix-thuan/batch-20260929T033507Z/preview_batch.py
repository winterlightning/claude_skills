from pathlib import Path
import json
from PIL import Image,ImageDraw
root=Path(__file__).parent
rows=json.loads((root/'runs.json').read_text())
for start in range(0,20,5):
 sheet=Image.new('RGB',(800,5*185),'#e5e5e5');d=ImageDraw.Draw(sheet)
 for j,row in enumerate(rows[start:start+5]):
  y=j*185;d.text((8,y+3),str(start+j+1)+' '+row['id'],fill='black')
  for x,name in [(8,'reference.png'),(170,'preview-light-384.png'),(445,'preview-dark-384.png')]:
   im=Image.open(Path(row['run'])/name).convert('RGBA');im.thumbnail((144,144));sheet.paste('white',(x,y+25,x+144,y+169));sheet.paste(im,(x,y+25),im)
  for x,name in [(335,'preview-light-48.png'),(610,'preview-dark-48.png')]:
   im=Image.open(Path(row['run'])/name);sheet.paste(im,(x,y+45))
 sheet.save(root/f'revisions-{start//5+1}.png')
