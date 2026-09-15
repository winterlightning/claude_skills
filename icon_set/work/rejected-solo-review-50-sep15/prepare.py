from pathlib import Path
import json,sqlite3,hashlib,io,sys,xml.etree.ElementTree as ET
sys.path.insert(0,str(Path.cwd()))
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='http://localhost:8000/gallery/index.html?tab=icons&family=solo&status=rejected'
AUTHOR='gpt-6'
names='acro-yoga-folded-balance adaptive-headlight affinity-publisher-logo air-pollution-fire airship-over-cloud angry-bird ant anteater aperture-shutter arabian-man arched-stone-bridge arched-tap-spraying-water arrange-number arrow-angle-right arrow-angle-up arrow-dot-corner-down-right arrow-dot-down arrow-dot-left arrow-dot-right arrow-dot-up arrow-left-right arrow-rectangle-left-84253ba9 arrow-up-celsius artillery-field-gun artillery-gun-outriggers automatic-rifle avatar-fire-fighter-woman avatar-jockey-man avatar-judo-athlete-man avatar-judo-athlete-woman avatar-korean-woman avatar-muslim-man-outfit avatar-pajamas-woman avatar-police-woman-1 avatar-ship-crew-navy-1 avatar-woman-air-hostess-1 avatar-woman-store-clerk avatar-woman-store-clerk-3 award-flower-rosette azadi-tower baby-face-with-bow baby-head baby-walker balancing-stick-pose bartainder bbc-iplayer-logo beaded-loop-with-heart-charm beading-wire-with-beads bench-vise bikini'.split()
c=json.loads(Path('icon_set/dist/gallery/icons.json').read_text());lookup={i['icon_id']:i for i in c['icons']+c['failed_icons']};items=[lookup[n] for n in names]
db=sqlite3.connect('file:icon_set/data/feedback.sqlite3?mode=ro',uri=True)
for i in items:
 p=(Path('icon_set/dist/gallery')/i['preview_url']).resolve();s=p.read_bytes();(W/(i['icon_id']+'.svg')).write_bytes(s)
 i['review_sha256']=hashlib.sha256(s).hexdigest();i['feedback']=[r[0] for r in db.execute('select feedback from feedback where icon=? order by id',(i['key'],))]
(W/'snapshot.json').write_text(json.dumps(items,indent=2))
def render(s,size,fg='#17252b',bg=None,center=False):
 root=ET.fromstring(s)
 for e in root.iter():
  if e.get('stroke') and e.get('stroke')!='none':e.set('stroke',fg)
  if e.get('fill') and e.get('fill') not in ('none','transparent'):e.set('fill',fg)
  if center and e.get('stroke-width'):e.set('stroke-width','0.45')
 return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=size,output_height=size,background_color=bg))).convert('RGBA')
for page in range(5):
 im=Image.new('RGB',(1400,1250),'#edf1f2');d=ImageDraw.Draw(im)
 for j,i in enumerate(items[page*10:(page+1)*10]):
  x=j%2*700;y=j//2*250;s=(W/(i['icon_id']+'.svg')).read_bytes()
  d.text((x+12,y+8),str(page*10+j+1)+'. '+i['icon_id'],fill='black')
  for xpos,sz,fg,bg,cl in [(15,150,'#17252b',None,False),(190,150,'#1687c2',None,True),(370,48,'#17252b','white',False),(435,48,'white','#18181b',False)]:
   r=render(s,sz,fg,bg,cl);im.paste(r,(x+xpos,y+38),r)
  d.text((x+15,y+198),'Generated            Centerlines       48px light/dark',fill='black')
  if i['original_sources']:
   p=Path('icon_set/dist/gallery')/i['original_sources'][0]['url']
   if p.exists():
    r=render(p.read_bytes(),135);im.paste(r,(x+545,y+40),r)
  d.text((x+550,y+198),'Original',fill='black')
  d.text((x+15,y+218),' | '.join(i['feedback'])[:98],fill='#843b32')
 im.save(W/f'sheet-{page+1}.png')
print('50 snapshots; five sheets ready',flush=True)
from icon_set.model.icons.registry import create
out=[]
for j,i in enumerate(items):
 try:
  icon=create(i['icon_id']);r=icon.validate_icon();s=icon.to_svg();row={'icon_id':i['icon_id'],'status':r.status,'description':r.describe(),'model_matches_snapshot':hashlib.sha256(s.encode()).hexdigest()==i['review_sha256']}
 except Exception as e:row={'icon_id':i['icon_id'],'status':'error','description':str(e)}
 out.append(row);(W/'validation.json').write_text(json.dumps(out,indent=2));print(j+1,i['icon_id'],row['status'],flush=True)
