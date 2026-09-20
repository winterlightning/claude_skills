import sys,json,io,html,shutil,xml.etree.ElementTree as E
from pathlib import Path
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
rows=json.loads((W/'candidates.json').read_text());assets=W/'review-assets';assets.mkdir(exist_ok=True);im=Image.new('RGB',(960,780),'#f5f5f5');d=ImageDraw.Draw(im);cards=[]
for j,r in enumerate(rows):
 m=create(r['compact']);svg=m.to_svg();(assets/f'{j}-after.svg').write_text(svg);(assets/f'{j}-before.svg').write_text(create(r['parent']).to_svg());shutil.copy2(ROOT/r['source_path'],assets/f'{j}-original.svg')
 d.text((10,j*260+5),r['icon']+' — compact 32 x 32, outer 4 / inner 2',fill='black')
 for k,key in enumerate(['original','before','after']):
  s=(assets/f'{j}-{key}.svg').read_text();a=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=190,output_height=190)));im.paste(a,(20+k*220,j*260+40),a);d.text((20+k*220,j*260+25),key,fill='black')
 for k,bg in enumerate(['white','#243129']):
  d.rectangle((700,j*260+40+k*80,800,j*260+110+k*80),fill=bg)
  a=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.replace('currentColor','white' if k else 'black').encode())));im.paste(a,(730,j*260+60+k*80),a)
 cards.append('<article><h2>'+html.escape(r['icon'])+'</h2>'+''.join(f'<figure><figcaption>{key}</figcaption><img src="review-assets/{j}-{key}.svg" width="180" height="180"></figure>' for key in ['original','before','after'])+f'<figure><figcaption>Actual size</figcaption><img src="review-assets/{j}-after.svg" width="32" height="32"></figure></article>')
im.save(W/'comparison.png')
(W/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Compact sub icons</title><style>body{font:14px system-ui;background:#f5f5f5;padding:20px}article{background:white;padding:16px;margin:16px 0}figure{display:inline-block;margin:15px}figcaption{margin-bottom:10px}img{object-fit:contain}</style><h1>Compact 32px versions</h1><p>Original composition retained. 4px outer outline / 2px inner characters. Explicit user-approved exceptions to standard sub rules.</p>'+''.join(cards))
print(W/'comparison.png')
