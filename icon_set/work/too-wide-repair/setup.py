from pathlib import Path
import json,sys,re,ast,io
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons import registry
from icon_set.renderers.png import render_png
from PIL import Image,ImageDraw,ImageFont
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-wide-repair/queue.json'
AUTHOR='gpt-6'
rows=json.loads((W/'queue.json').read_text());mapping=[]
for r in rows:
 dest,ident,src=prepare_variant(r['id'],'solo','Correct width and full spacing review')
 match=re.search(r"SOURCE_ICON_ID = ['\"]([^'\"]+)",src)
 if match:dest=dest.with_name(dest.stem+'_'+match[1].replace('-','_')+'.py')
 with dest.open('x') as f:f.write(src)
 (W/'starting').mkdir(exist_ok=True);(W/'starting'/dest.name).write_text(src)
 mapping.append({'original':r['id'],'id':ident,'file':str(dest.relative_to(ROOT))});registry._FACTORIES=None
(W/'mapping.json').write_text(json.dumps(mapping,indent=2))
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
im=Image.new('RGB',(1250,6*165),'#f7f6f2');d=ImageDraw.Draw(im)
for i,r in enumerate(mapping):
 x=i%5*250;y=i//5*165;t=Image.open(io.BytesIO(render_png(registry.create(r['original']),scale=2)));im.paste(t,(x+75,y+10),t);d.text((x+10,y+122),r['original'],font=font,fill='#222')
im.save(W/'before.png');print('Prepared',len(mapping),'variants')
