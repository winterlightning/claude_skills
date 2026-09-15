"""Diagnostic views drawn from the model; exported icon SVGs are never patched."""
import json,io,textwrap
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import cairosvg
from .check_drafts import load
from icon_set.renderers.svg import build_paths
OUT=Path(__file__).resolve().parent
rows=json.loads((OUT/'batch.json').read_text())
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',11)
def diagnostic(icon):
 drawing=icon.draw();paths=build_paths(drawing)
 s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">','<path d="M24 0V48M0 24H48" fill="none" stroke="#df7777" stroke-width="0.25" stroke-dasharray="1 1"/>']
 colors=['#167bb7','#bc437c','#8d6c10','#158869']
 for i,p in enumerate(paths):
  s.append(f'<path d="{p["d"]}" fill="none" stroke="#dce2e8" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
 for i,p in enumerate(paths):
  c=colors[i%len(colors)];s.append(f'<path d="{p["d"]}" fill="none" stroke="{c}" stroke-width="0.55"/>')
  for atom in p['primitives']:
   for pt in (atom.start,atom.end):s.append(f'<circle cx="{pt.x}" cy="{pt.y}" r="0.6" fill="{c}"/>')
 return ''.join(s)+'</svg>'
if __name__=='__main__':
 for side in ['before','after']:
  for start in range(0,100,25):
   im=Image.new('RGB',(1250,1000),'white');d=ImageDraw.Draw(im)
   for j,r in enumerate(rows[start:start+25]):
    svg=diagnostic(load(r,side)());(OUT/'previews'/f'{r["batch_index"]}-{side}-centerline.svg').write_text(svg)
    p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=156,output_height=156)))
    x=j%5*250;y=j//5*200;im.paste(p,(x+44,y+4),p)
    for k,l in enumerate(textwrap.wrap(str(r['batch_index'])+'. '+r['icon_id'],35)[:2]):d.text((x+5,y+164+k*13),l,fill='#222',font=font)
   im.save(OUT/f'{side}-centerlines-{start//25+1}.png')
 print('100 centerline comparisons rendered.')
