from pathlib import Path
import json,html,io,shutil,textwrap
import cairosvg
from PIL import Image,ImageDraw,ImageFont
OUT=Path(__file__).resolve().parent
BASE=OUT.parents[1]
items=json.loads((OUT/'inventory.json').read_text())['icons']
(OUT/'references').mkdir(exist_ok=True)
font_path='/System/Library/Fonts/Supplemental/Arial.ttf'
font=ImageFont.truetype(font_path,16)
small=ImageFont.truetype(font_path,13)
title=ImageFont.truetype(font_path,24)
sheet=Image.new('RGB',(1040,1380),'#f4f6f8');draw=ImageDraw.Draw(sheet)
draw.text((24,18),'23 container sub icons — no saved brief',font=title,fill='#17212d')
draw.text((24,50),'Original references · numbered for easy discussion',font=small,fill='#657080')
cards=[]
for i,r in enumerate(items):
 source=BASE/'dist/gallery/combination-originals'/f'{r["source_id"]}.svg'
 assert source.exists(),source
 dest=OUT/'references'/source.name;shutil.copyfile(source,dest)
 img=Image.open(io.BytesIO(cairosvg.svg2png(url=str(source),output_width=256,output_height=256))).convert('RGBA')
 bounds=img.getchannel('A').getbbox()
 if bounds:img=img.crop(bounds)
 img.thumbnail((145,130),Image.Resampling.LANCZOS)
 x=(i%4)*260+10;y=(i//4)*215+85
 draw.rounded_rectangle((x,y,x+240,y+200),radius=12,fill='white',outline='#dbe1e7')
 draw.text((x+12,y+10),f'{i+1:02}',font=small,fill='#657080')
 sheet.paste(img,(x+(240-img.width)//2,y+18+(130-img.height)//2),img)
 for j,line in enumerate(textwrap.wrap(r['name'],27)):
  draw.text((x+12,y+155+j*19),line,font=font,fill='#17212d')
 cards.append(f'<article><span>{i+1:02}</span><img src="references/{source.name}" alt="{html.escape(r["name"])}"><h2>{html.escape(r["name"])}</h2><p>Used in {r["pairings"]} container pair'+('s' if r['pairings']!=1 else '')+f'</p><a href="{html.escape(r["progression_url"],quote=True)}">Progression</a></article>')
sheet.save(OUT/'all-23.png')
(OUT/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>23 sub icons without briefs</title><style>body{font:15px system-ui;margin:28px;background:#f4f6f8;color:#17212d}h1{font-size:26px}header p{color:#657080}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px}article{background:white;border:1px solid #dbe1e7;border-radius:12px;padding:18px}article img{width:100%;height:140px;object-fit:contain;display:block;margin:10px 0 20px}h2{font-size:16px;line-height:1.4}span,p,a{font-size:13px}span,p{color:#657080}a{color:#2563eb}</style><header><h1>23 container sub icons without briefs</h1><p>All original references shown together. These are the 23 items from the latest inventory; items with existing briefs are excluded.</p></header><main>'''+''.join(cards)+'</main></html>')
print(OUT/'index.html')
