"""Package the 51 source-linked outputs, retaining actual release/review states."""
from pathlib import Path
import sys,json,html,base64,io,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
import cairosvg
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
OUT=Path(__file__).resolve().parent
refs=json.loads((OUT/'icons.json').read_text());models={r['number']:r for r in json.loads((OUT/'complete-models.json').read_text())}
for n,id in {5:'braille-six-dot-cell',25:'elevator-direction-doors',26:'empty-battery-content',40:'person-height-measurement-content'}.items():models[n]=dict(icon_id=id,kind='authored')
texts={u:r for r in json.loads((ROOT/'icon_set/dist/text44/manifest.json').read_text())['icons'] for u in r['source_ids']}
release={r['icon_id']:r for r in json.loads((ROOT/'icon_set/dist/solo48/manifest.json').read_text())['icons']}
failed={r['icon_id']:r for r in json.loads((ROOT/'icon_set/dist/failed/solo48/manifest.json').read_text())['icons']}
drafts=OUT/'draft-svg';drafts.mkdir(exist_ok=True)
rows=[];cards=[];pictures=[]
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for r in refs:
 n=r['number'];id=None
 if n in models:
  m=models[n];id=m['icon_id'];status='reused' if m['kind']=='reused' else 'generated';p=ROOT/'icon_set/dist/solo48'/(id+'.svg')
  if id not in release or not p.exists():
   p=drafts/(id+'.svg');p.write_text(create(id).to_svg());status='review';detail='; '.join(failed[id]['errors']) if id in failed else create(id).validate_icon().describe()
  else:detail='SOLO48 model and export checks passed.'
 elif r['id'] in texts:
  t=texts[r['id']];id=t['icon_id'];p=ROOT/'icon_set/dist/text44'/(id+'.svg');status='generated';detail='Existing glyph layout with at most 32 units total ink height; degree mark added for Fahrenheit.' if n==21 else 'Existing glyph layout, at most 32 units total ink height.'
 else:raise RuntimeError('Missing output '+str(n))
 document=p.read_text();rows.append({**r,'icon_id':id,'output':str(p),'status':status,'validation':detail});pictures.append((n,r['name'],document,status))
 def image(document):return '<img src="data:image/svg+xml;base64,'+base64.b64encode(document.encode()).decode()+'">'
 cards.append('<article data-name="'+html.escape(r['name'].lower(),quote=True)+'"><h2>'+str(n)+'. '+html.escape(r['name'])+'</h2><div class="pair"><figure>'+image(Path(r['reference']).read_text())+'<figcaption>Reference</figcaption></figure><figure>'+image(document)+'<figcaption>Result</figcaption></figure></div><p class="'+status+'">'+status.title()+'</p><details><summary>Validation and source</summary><p>'+html.escape(detail)+'</p><small>'+r['id']+'</small></details><a download="'+id+'.svg" href="data:image/svg+xml;base64,'+base64.b64encode(document.encode()).decode()+'">Download SVG</a></article>')
counts={k:sum(r['status']==k for r in rows) for k in ['generated','reused','review']}
(OUT/'generation-status.json').write_text(json.dumps(rows,indent=2)+'\n')
(OUT/'generated.html').write_text('''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>51 container content icons</title><style>body{font:15px system-ui;background:#f4f5f0;padding:28px;color:#202820;max-width:1500px;margin:auto}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}article{background:white;padding:20px;border-radius:12px;border:1px solid #dee4d8}h2{font-size:16px;min-height:42px}.pair{display:flex;gap:20px;justify-content:center}figure{margin:0;text-align:center}img{width:96px;height:96px;object-fit:contain}figcaption,small{font-size:12px;color:#65735f}p{line-height:1.5}.review{color:#9c5700}details{font-size:12px;margin:12px 0}a{color:#35613d}input{padding:13px;border:1px solid #c8d0c2;border-radius:8px;margin:12px 0 24px;width:300px;max-width:90%}[hidden]{display:none!important}</style><h1>51 container content icons</h1><p>'''+f"{counts['generated']} generated · {counts['reused']} reused · {counts['review']} awaiting validation review"+'''</p><p>All 51 references have an SVG. Items marked Review are drafts and are not ready for combination use. The unframed horizontal dots reuse three existing period glyphs, preserving their natural shape. Two-line text uses smaller glyphs to stay within 32 units total ink height.</p><p><a href="dimension-audit.html">Compare original and generated ink dimensions for all 51 icons</a></p><input id="search" type="search" placeholder="Search icons"><main>'''+''.join(cards)+'''</main><script>document.getElementById('search').addEventListener('input',e=>{for(const card of document.querySelectorAll('article'))card.hidden=!card.dataset.name.includes(e.target.value.toLowerCase())});</script>''')
for theme,bg,fg in [('light','#ffffff','#202820'),('dark','#171c18','#ffffff')]:
 im=Image.new('RGB',(1200,9*160+50),bg);draw=ImageDraw.Draw(im);draw.text((15,12),'51 container content icons · '+theme+' · native and enlarged previews',font=font,fill=fg)
 for i,(n,name,s,status) in enumerate(pictures):
  x=i%6*200;y=i//6*160+40
  for scale,dx in [(1,8),(2,88)]:
   a=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor',fg).replace('#202820',fg).encode(),scale=scale))).convert('RGBA');a.thumbnail((108,90) if scale==2 else (72,48));im.paste(a,(x+dx,y+5),a)
  for j,line in enumerate(textwrap.wrap(f'{n}. {name}',27)):draw.text((x+8,y+100+j*15),line,font=font,fill=fg)
  if status=='review':draw.text((x+8,y+143),'Review draft',font=font,fill='#c78b3c')
 im.save(OUT/f'complete-{theme}.png')
print(counts)
