from pathlib import Path
import json,io,html
from PIL import Image,ImageDraw,ImageFont
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/dist/gallery/failures.html'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'before.json').read_text())
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for page in range(25):
 im=Image.new('RGB',(1250,880),'#fafafa'); pen=ImageDraw.Draw(im)
 for j,r in enumerate(rows[page*20:page*20+20]):
  x=j%5*250;y=j//5*220
  pen.text((x+5,y+5),f'{page*20+j+1}. {r["id"][:32]}',font=font,fill='#222222')
  paths=''.join('<path d="'+html.escape(p['d'])+'"/>' for p in r['paths'])
  for offset,size,dark,center in [(5,96,False,True),(110,48,False,False),(178,48,True,False)]:
   bg,fg=('#17191d','#ffffff') if dark else ('#fafafa','#202226')
   svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="{bg}"/><g fill="none" stroke="{fg}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" opacity="{.2 if center else 1}">{paths}</g>'
   if center:
    svg+=f'<g fill="none" stroke="#2563eb" stroke-width=".45">{paths}</g>'
    for pair in r['spacingPairs']:
     a,b=pair['a'],pair['b'];svg+=f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" stroke="#e11d48" stroke-width=".7"/>'
   tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=(svg+'</svg>').encode(),output_width=size,output_height=size)));im.paste(tile,(x+offset,y+32))
  import textwrap
  msg=r['issues'][0]['text'].split(': ',1)[-1]
  for k,line in enumerate(textwrap.wrap(msg,35)[:5]):pen.text((x+5,y+137+k*15),line,font=font,fill='#444444')
 im.save(W/f'centerlines-{page+1}.png')
