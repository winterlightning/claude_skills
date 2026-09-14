from pathlib import Path
import sys,json,io,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'targets.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',11)
(W/'parent-hashes.json').write_text(json.dumps({r['file']:hashlib.sha256(Path(r['file']).read_bytes()).hexdigest() for r in rows},indent=2))
for page in range(4):
 batch=rows[page*35:(page+1)*35];im=Image.new('RGB',(1250,((len(batch)+4)//5)*135),'white');d=ImageDraw.Draw(im)
 for n,r in enumerate(batch):
  x=n%5*250;y=n//5*135;d.text((x+3,y+3),str(page*35+n)+' '+r['id'],font=font,fill='black')
  tile=Image.open(io.BytesIO(render_png(create(r['id']),scale=2)));im.paste(tile,(x+70,y+25),tile)
 im.save(W/f'before-{page+1}.png')
