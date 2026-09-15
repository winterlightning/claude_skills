from pathlib import Path
import json,sys,io,html
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'snapshot'))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg,build_paths
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
def centerline(icon):
 drawing=icon.draw();paths=build_paths(drawing);bits=['<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">','<rect width="48" height="48" fill="#fff"/>']
 for x in range(0,49,4):bits.extend([f'<path d="M{x} 0V48M0 {x}H48" stroke="#edf0f3" stroke-width=".2"/>'])
 for p in paths:bits.append(f'<path d="{html.escape(p["d"],quote=True)}" fill="none" stroke="#d0d7df" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
 for p in paths:bits.append(f'<path d="{html.escape(p["d"],quote=True)}" fill="none" stroke="#1864b6" stroke-width=".45" stroke-linecap="round" stroke-linejoin="round"/>')
 points=set()
 for p in drawing.primitives:points.update([(p.start.x,p.start.y),(p.end.x,p.end.y)])
 for x,y in points:bits.append(f'<circle cx="{x}" cy="{y}" r=".5" fill="#c33737"/>')
 bits.append('</svg>');return ''.join(bits)
def paste(im,doc,x,y,size):
 png=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=doc.encode(),output_width=size,output_height=size))).convert("RGBA");im.paste(png,(x,y),png)
if __name__=='__main__':
 R=json.loads((W/'revisions.json').read_text());A={x['number']:x for x in json.loads((W/'inventory.json').read_text())};Q=json.loads((W/'release-validation.json').read_text());nums=json.loads((W/'round2-numbers.json').read_text());C={};difference={}
 for n in nums:
  r=R[str(n)]
  try:
   old=create(r['parent']);new=create(r['id']);C[r['id']]=centerline(new);difference[str(n)]=[p['d'] for p in build_paths(old.draw())]!=[p['d'] for p in build_paths(new.draw())]
  except Exception as e:print(n,e)
 for i in range(0,len(nums),18):
  batch=nums[i:i+18]
  for theme,ink,bg in [('light','#111','#fff'),('dark','#f4f4f4','#171b20')]:
   im=Image.new('RGB',(1200,((len(batch)+3)//4)*210),bg);d=ImageDraw.Draw(im)
   for j,n in enumerate(batch):
    x=j%4*300;y=j//4*210;r=R[str(n)]
    try:
     paste(im,A[n]['before_svg'].replace('currentColor',ink),x+8,y+12,48)
     paste(im,render_svg(create(r['id'])).replace('currentColor',ink),x+72,y+12,48)
     paste(im,C[r['id']],x+144,y+12,144)
    except Exception as e:d.text((x+8,y+80),str(e)[:35],fill=ink)
    d.text((x+8,y+168),str(n)+' '+r['parent'][:29],fill=ink);d.text((x+8,y+188),Q.get(r['id'],{}).get('status','unchecked'),fill=ink)
   im.save(W/f'round2-{i//18+1}-{theme}.png')
 (W/'centerlines-round2.json').write_text(json.dumps(C));(W/'round2-difference.json').write_text(json.dumps(difference,indent=2));print('Unchanged', [n for n,d in difference.items() if not d])
