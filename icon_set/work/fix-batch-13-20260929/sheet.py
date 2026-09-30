import json,sys
from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent; repo=root.parents[2]
rows=json.loads((root/'latest.json').read_text())
ids=list(map(int,sys.argv[1:])) or list(range(1,21))
for start in range(0,len(ids),5):
    chunk=ids[start:start+5];s=Image.new('RGB',(980,len(chunk)*280),'#dddddd');d=ImageDraw.Draw(s)
    for y,i in enumerate(chunk):
        r=rows[str(i)];p=repo/r['run'];d.text((5,y*280+3),f"{i}: {r['icon_id']} — {r['build_gate']['status']}",fill='black')
        for x,n in [(0,'reference.png'),(245,'light-240.png'),(490,'dark-240.png'),(760,'light-48.png'),(830,'dark-48.png')]:
            im=Image.open(p/n).convert('RGB');s.paste(im,(x,y*280+30))
    s.save(root/f'candidates-{start//5+1}.png')
