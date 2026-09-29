from pathlib import Path
from PIL import Image, ImageDraw
import json,sys
B=Path(__file__).parent
R=B.parents[3]
sys.path.insert(0,str(R))
from icon_set.scripts.build_gate import gate
runs=json.loads((B/'runs.json').read_text())
if '--gate' in sys.argv:
 for i,r in enumerate(runs):
  p=R/r['run'];g=gate(p/r['module'])
  (p/'gate.json').write_text(json.dumps(g,indent=2))
  print(i+1,r['icon_id'],g['status'],'errors',len(g['errors']),'warnings',len(g['warnings']),flush=True)
  for e in g['errors']+g['warnings']: print(' ',e,flush=True)
else:
 for page in range(4):
  im=Image.new('RGB',(900,5*230),'#eeeeee');d=ImageDraw.Draw(im)
  for j,r in enumerate(runs[page*5:page*5+5]):
   y=j*230;p=R/r['run'];d.text((8,y+5),f"{page*5+j+1} {r['icon_id']}",fill='black')
   for k,(f,size) in enumerate([('reference.png',180),('preview-light-384.png',180),('preview-dark-384.png',180),('preview-light-48.png',48),('preview-dark-48.png',48)]):
    x=[10,210,410,620,690][k];v=Image.open(p/f).convert('RGB');v=v.resize((size,size)) if size==180 else v;im.paste(v,(x,y+30))
  im.save(B/f'candidates-{page}.png')
