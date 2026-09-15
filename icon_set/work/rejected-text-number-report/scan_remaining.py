exec((__import__('pathlib').Path(__file__).parent/'prepare.py').read_text().split('for start in range')[0])
keys={r['key'] for r in candidates}
remaining=[r for r in rows if r['key'] not in keys]
for n,r in enumerate(remaining):r['scan_index']=n+1
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',10)
for start in range(0,len(remaining),144):
 batch=remaining[start:start+144];im=Image.new('RGB',(1536,math.ceil(len(batch)/12)*124),'white');draw=ImageDraw.Draw(im)
 for j,r in enumerate(batch):
  x=j%12*128;y=j//12*124
  p=(ROOT/'icon_set/dist/gallery'/r['preview_url']).resolve()
  icon=Image.open(io.BytesIO(cairosvg.svg2png(url=str(p),output_width=66,output_height=66)))
  im.paste(icon,(x+31,y+5),icon)
  label=str(r['scan_index'])+'. '+r['icon_id']
  for k,line in enumerate(textwrap.wrap(label,23)[:3]):draw.text((x+3,y+75+k*12),line,fill='black',font=font)
  draw.rectangle((x,y,x+127,y+123),outline='#dddddd')
 im.save(OUT/f'scan-{start//144+1}.png')
(OUT/'remaining.json').write_text(json.dumps(remaining))
print(len(remaining))
