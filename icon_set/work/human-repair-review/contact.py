from audit import *
import io,cairosvg
from PIL import Image,ImageDraw
from icon_set.renderers.svg import _move_to,_segment
rows_by={x['row']['icon_id']:x for x in rows}
audit=json.loads((OUT/'audit.json').read_text())
for batch in range(3):
 im=Image.new('RGB',(1440,880),'#fff');dr=ImageDraw.Draw(im)
 for j,a in enumerate(audit[batch*24:(batch+1)*24]):
  i=load(rows_by[a['icon_id']]);by=i.draw().by_id();svg=i.to_svg();root=svg[:svg.rfind('</svg>')];root=root.replace('stroke="currentColor"','stroke="#ccd1d5"')
  for f in a['figures']:
   for key,color in [('head_members','#008d9e'),('torso_members','#db7100')]:
    for name in f[key]:
     p=by[name];root+=f'<path d="{_move_to(p)}{_segment(p)}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
  root+='</svg>';x=j%6*240;y=j//6*220
  for doc,w,dx in [(svg,64,5),(root,144,84)]:
   pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=doc.encode(),output_width=w,output_height=w)));im.paste(pic,(x+dx,y+5),pic)
  dr.text((x+5,y+156),str(a['number'])+' '+a['icon_id'][:31],fill='#111')
  dr.text((x+5,y+175),a['type'],fill='#456')
  gaps=[f"{f['ink_gap']:.2f}u / {f['axis_error_degrees']:.0f}deg" for f in a['figures'] if 'ink_gap' in f]
  dr.text((x+5,y+192),'; '.join(gaps),fill='#456')
 im.save(OUT/f'audit-{batch}.png')
