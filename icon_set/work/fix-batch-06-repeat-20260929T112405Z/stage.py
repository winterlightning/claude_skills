import json,sys
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
root=Path(__file__).parent
rows=json.loads((root/'claims.json').read_text()) if (root/'claims.json').exists() else []
for stamp in sys.argv[1:]:
 for p in sorted(Path('icon_set/work/primitive-fix-thuan').glob(f'*/{stamp}/claim.json')):
  i=json.loads(p.read_text())['item']
  if i['key'] in {r['key'] for r in rows}:continue
  rows.append(dict(key=i['key'],fix=str(p.parent),reference=str(next((p.parent/'reference').glob('*.svg'))),before=str(next((p.parent/'before').glob('*.svg'))),feedback=i.get('feedback'),reason=i.get('reason')))
(root/'claims.json').write_text(json.dumps(rows,indent=2))
for page in range((len(rows)+4)//5):
 canvas=Image.new('RGB',(670,1050),'white');d=ImageDraw.Draw(canvas)
 for n,r in enumerate(rows[page*5:page*5+5]):
  d.text((5,n*210),f'{page*5+n} '+r['key'],fill='black')
  for j,kind in enumerate(('reference','before')):
   dst=root/f'{page*5+n}-{kind}.png'
   cairosvg.svg2png(url=r[kind],write_to=str(dst),output_width=175,output_height=175,background_color='white')
   canvas.paste(Image.open(dst).convert('RGB'),(j*330+15,n*210+25))
 canvas.save(root/f'comparison-{page}.png')
for n,r in enumerate(rows):print(n,r['key'],r.get('feedback') or '(no feedback)')
