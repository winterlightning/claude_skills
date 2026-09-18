import json,io,textwrap,html
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw,ImageFont
P=Path(__file__).resolve().parent;BASE=P.parents[1];items=json.loads((P/'generated-items.json').read_text());manifest={r['icon_id']:r for r in json.loads((BASE/'dist/text28/manifest.json').read_text())['icons']}
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',15);cards=[]
for theme in ['light','dark']:
 bg='#f3f5f7' if theme=='light' else '#18202b';fg='black' if theme=='light' else 'white'
 im=Image.new('RGB',(1152,1800),bg);d=ImageDraw.Draw(im)
 for i,r in enumerate(items):
  x=i%4*288;y=i//4*300;record=manifest[r['icon_id']];svg=BASE/'dist/text28'/(r['icon_id']+'.svg');document=svg.read_text().replace('currentColor',fg)
  art=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=document.encode(),scale=3))).convert('RGBA');art.thumbnail((260,145));im.paste(art,(x+(288-art.width)//2,y+15+(145-art.height)//2),art)
  native=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=document.encode()))).convert('RGBA');im.paste(native,(x+(288-native.width)//2,y+164),native)
  for j,line in enumerate(textwrap.wrap(f'{i+1}. {r["name"]}',32)):d.text((x+10,y+258+j*17),line,fill=fg,font=font)
  if theme=='light':cards.append(f'<article><h2>{i+1:02}. {html.escape(r["name"])}</h2><div class="compare"><figure><img src="references/{r["source_id"]}.svg"><figcaption>Original</figcaption></figure><figure><img src="../../dist/text28/{r["icon_id"]}.svg"><figcaption>Generated</figcaption></figure></div><p>Text ink 28 · stroke 4 · {"Mixed composition" if record.get("motif") else "Text"}</p><a href="../../dist/text28/{r["icon_id"]}.svg">SVG</a></article>')
 im.save(P/f'generated-{theme}.png')
(P/'generated.html').write_text('<!doctype html><meta charset="utf-8"><title>23 generated text icons</title><style>body{font:14px system-ui;background:#f4f6f8;margin:28px;color:#17212d}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px}article{background:white;border:1px solid #ddd;border-radius:12px;padding:18px}h2{font-size:16px}.compare{display:flex;gap:12px}figure{margin:0;width:50%;text-align:center}img{width:100%;height:150px;object-fit:contain}figcaption,p{color:#657080}</style><h1>23 generated text icons</h1><p>Typeface lettering has 28-unit visible ink height and 4-unit strokes. Mixed compositions add room for their non-text details. All artwork is trimmed to its visible ink bounds.</p><main>'+''.join(cards)+'</main>')
