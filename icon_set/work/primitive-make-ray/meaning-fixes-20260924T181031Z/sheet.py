from pathlib import Path
from PIL import Image, ImageDraw
import json
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
batch=Path(__file__).parent
ps=sorted(batch.parent.glob('*/20260924T181031Z-meaning-*/candidate.json'),key=lambda p:json.loads(p.read_text())['icon_id'])
for offset in range(0,len(ps),8):
    subset=ps[offset:offset+8]
    im=Image.new('RGB',(1200,((len(subset)+3)//4)*290),'white');d=ImageDraw.Draw(im)
    for i,p in enumerate(subset):
        r=json.loads(p.read_text());x=i%4*300;y=i//4*290
        d.text((x+5,y+3),r['icon_id'][:36],fill='black');d.text((x+5,y+20),r['build_gate']['status'],fill='black')
        for j,t in enumerate(['light','dark']):
            large=Image.open(p.parent/f'preview-{t}-384.png').resize((144,144));im.paste(large,(x+j*150,y+40))
            native=Image.open(p.parent/f'preview-{t}-48.png');im.paste(native,(x+j*150+45,y+196))
    im.save(batch/f'review-{offset//8+1}.png')
