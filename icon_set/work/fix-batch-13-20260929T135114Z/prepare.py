from pathlib import Path
import json,io,cairosvg
from PIL import Image,ImageDraw
B=Path(__file__).parent
claims=json.loads((B/'recovered-claims.json').read_text())
if (B/'new-claims.json').exists():claims+=json.loads((B/'new-claims.json').read_text())
rows=[]
for claim in claims:
 i=claim['item'];key=i['key']
 matches=[]
 for p in (Path('icon_set/work/primitive-fix-thuan')/key.replace('/','__')).glob('*/claim.json'):
  c=json.loads(p.read_text())
  if c['work']['claimed_at']==claim['work']['claimed_at']:matches.append(p.parent)
 if len(matches)!=1:continue
 fix=matches[0];refs=list((fix/'reference').glob('*.svg'));before=fix/'before'/(i['icon_id']+'.svg')
 if not refs or not before.exists():continue
 rows.append({'key':key,'fix_dir':str(fix),'reference':str(refs[0]),'before':str(before),'feedback':i.get('feedback')})
(B/'claims.json').write_text(json.dumps(rows,indent=2))
for page in range((len(rows)+4)//5):
 c=Image.new('RGB',(650,850),'#dddddd');d=ImageDraw.Draw(c)
 for n,r in enumerate(rows[page*5:page*5+5]):
  y=n*170;d.text((5,y+2),r['key'],fill='black')
  for j,k in enumerate(['reference','before']):
   im=Image.open(io.BytesIO(cairosvg.svg2png(url=r[k],output_width=140,output_height=140,background_color='white'))).convert('RGB');c.paste(im,(j*310+30,y+22))
 c.save(B/f'comparison-{page}.png')
print(len(rows),'staged and scoped rows')
