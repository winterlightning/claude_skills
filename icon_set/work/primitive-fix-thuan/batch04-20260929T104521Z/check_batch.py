import json,sys
from pathlib import Path
from PIL import Image,ImageDraw
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate

AUTHOR='gpt-6'
ROOT=Path(__file__).parent
items=json.loads((ROOT/'items.json').read_text())
selected=list(map(int,sys.argv[1:])) or list(range(1,18))
for n in selected:
    it=items[n-1]
    p=sorted(Path(it['run']).parent.glob('20260929-batch04-attempt*'))[-1]
    q=next(p.glob('*.py'))
    try:
        i=load_icon(q);r=i.validate_icon();g=gate(q,p/'gate')
        print(n,i.icon_id,r.describe(),g,flush=True)
        (p/'validation.txt').write_text(r.describe()+'\n'+str(g))
        (p/'gate.json').write_text(json.dumps(g,indent=2))
        s=i.to_svg();(p/(i.icon_id+'.svg')).write_text(s);render_previews(s,i.icon_id,48,p)
        it['latest']=str(p);it['gate']=g['status'];it['validation']=r.status
    except Exception as e:print(n,type(e).__name__,str(e),flush=True)
(ROOT/'items.json').write_text(json.dumps(items,indent=2))
for start in range(0,17,6):
    im=Image.new('RGB',(1080,640),'#eee');dr=ImageDraw.Draw(im)
    for k,it in enumerate(items[start:start+6]):
        p=Path(it.get('latest',it['run']));x=k%3*360;y=k//3*320
        dr.text((x+5,y+5),f'{start+k+1} '+it['key'][5:35]+' '+it.get('gate','?'),fill='black')
        if (p/'preview-light-384.png').exists():
            im.paste(Image.open(p/'preview-light-384.png').resize((216,216)),(x+60,y+25))
            im.paste(Image.open(p/'preview-light-48.png'),(x+105,y+255))
            im.paste(Image.open(p/'preview-dark-48.png'),(x+185,y+255))
    im.save(ROOT/f'latest-{start//6}.png')
