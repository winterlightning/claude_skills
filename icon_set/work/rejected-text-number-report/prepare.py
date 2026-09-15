import json,io,math,textwrap
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
rows=json.load(open('/private/tmp/rejected-report-catalog.json'))
candidates=json.load(open('/private/tmp/rejected-text-candidates.json'))
extra='tnt-detonator-plunger br c5 circle-r compass-east eight-ball east-direction-marker fuel-gauge-dial height-limit-4m increase-indent iot-hub-nodes iot-pin-markers ligature liras logistic-weight lte-edge maximum-height-4m mechanical-cash-register milestone-marker-divided minus-one-increment nagras-sign network-5g-symbol paragraph-1 paragraph-center-align paragraph-spacing parking periodic-table ps receipt rel-file-path remaining-range-indicator rh rip-gravestone rotate-left-45 rotation-y-axis rtf-format settings-on shop-sign slot-machine smart square-brackets symbol-air-defence symbol-armor symbol-artillery symbol-aviation symbol-light-recon symbol-medical symbol-mountain-infantry symbol-non-specific symbol-signals taxi-front taxi-front-oval-lights time-clock-six tracker-smartwatch ux vip-crown-queen visibility-distance width-limit-2-5m width-limit-4m written-scroll'.split()
keys={r['key'] for r in candidates}
candidates+= [r for r in rows if r['icon_id'] in extra and r['key'] not in keys]
candidates.sort(key=lambda r:r['key'])
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for n,row in enumerate(candidates):row['review_index']=n+1
for start in range(0,len(candidates),64):
 batch=candidates[start:start+64];im=Image.new('RGB',(1600,math.ceil(len(batch)/8)*170),'#ffffff');draw=ImageDraw.Draw(im)
 for j,row in enumerate(batch):
  x=(j%8)*200;y=(j//8)*170
  p=(ROOT/'icon_set/dist/gallery'/row['preview_url']).resolve()
  png=cairosvg.svg2png(url=str(p),output_width=100,output_height=100)
  icon=Image.open(io.BytesIO(png));im.paste(icon,(x+50,y+8),icon)
  label=str(row['review_index'])+'. '+row['icon_id']
  for k,line in enumerate(textwrap.wrap(label,27)):draw.text((x+8,y+113+k*15),line,fill='#17251a',font=font)
  draw.rectangle((x,y,x+199,y+169),outline='#dddddd')
 im.save(OUT/f'candidates-{start//64+1}.png')
(OUT/'candidates.json').write_text(json.dumps(candidates,indent=2))
print('Candidates:',len(candidates))
