from pathlib import Path
import json,io
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/dist/gallery/icons.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
names='''binoculars bird-house bird-life blood-bag blood-cell boat boat-transportation bomb-explosive bone bone-1 book book-book-pages book-close book-close-1 book-close-2 book-close-49781b64 book-close-5a3d7973 book-close-content book-content book-open book-open-1 book-open-1-6ed65acc book-open-1-899601b3 book-open-1-df25e3f8 book-open-1421392c book-open-a147931e book-open-b5768591 book-open-e1dee87f book-pages bowl box box-25bec113 box-45b3bf7f box-45de01b0 box-805cc175 box-a4589238 box-bfb848d1 box-shipping boxing-glove brain brain-1 brain-f98adc76 brain-head bread bread-loaf bread-slice bread-slice-food bricks building building-1 building-68b98b76 building-735a4c8f building-building building-c2e118c4 building-dac12e36 buildings'''.split()
lib={i['icon_id']:i for i in json.load(open(SOURCE_PATH))['icons']};rows=[lib[n] for n in names]
(W/'candidates.json').write_text(json.dumps(rows,indent=2))
for start in range(0,len(rows),24):
 subset=rows[start:start+24];sheet=Image.new('RGB',(1000,140*((len(subset)+5)//6)),'white');d=ImageDraw.Draw(sheet)
 for j,r in enumerate(subset):
  im=Image.open(io.BytesIO(cairosvg.svg2png(url=str(Path('icon_set')/r['svg_path']),output_width=96,output_height=96)));x=j%6*166;y=j//6*140;sheet.paste(im,(x+28,y+4),im);d.text((x+3,y+106),f'{start+j+1} '+r['icon_id'][:24],fill='black')
 sheet.save(W/f'before-{start//24+1}.png')
