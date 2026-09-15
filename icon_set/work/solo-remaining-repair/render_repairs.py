from pathlib import Path
import sys,json,html,io,math
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import build_paths
from PIL import Image,ImageDraw,ImageFont
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/repairs.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'repairs.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for page in range(math.ceil(len(rows)/20)):
 im=Image.new('RGB',(1250,800),'#fafafa');pen=ImageDraw.Draw(im)
 for j,r in enumerate(rows[page*20:page*20+20]):
  x=j%5*250;y=j//5*200;pen.text((x+5,y+5),f"{r['number']}. {r['icon_id'][:31]}",font=font,fill='#222')
  for offset,size,dark,center,id_ in [(5,96,False,True,r['icon_id']),(110,48,False,False,r['icon_id']),(178,48,True,False,r['icon_id']),(110,48,False,False,r['parent'])]:
   paths=''.join('<path d="'+html.escape(p['d'])+'"/>' for p in build_paths(create(id_).draw()));bg,fg=('#17191d','#fff') if dark else ('#fafafa','#202226')
   svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="{bg}"/><g fill="none" stroke="{fg}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" opacity="{.2 if center else 1}">{paths}</g>'
   if center:svg+=f'<g fill="none" stroke="#2563eb" stroke-width=".45">{paths}</g>'
   tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=(svg+'</svg>').encode(),output_width=size,output_height=size)));im.paste(tile,(x+offset,y+(100 if id_==r['parent'] else 30)))
  qpath=W/'repaired-qa'/f"{r['icon_id']}.json"
  if qpath.exists():
   q=json.loads(qpath.read_text());pen.text((x+5,y+155),q['status']+'; holes '+str(q['negative_space'].get('failed_hole_count'))+'; pinches '+str(q['negative_space'].get('pinch_count')),font=font,fill='#222')
 im.save(W/f'repairs-{page+1}.png')
