from pathlib import Path
import sys,json,io
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID=None;SOURCE_PATH=None;AUTHOR='gpt-6'
outs=sorted((ROOT/'icon_set/work/primitive-make-ray').glob('*/20260924T160658Z-thuan-mac-centerlines'))
for out in outs:
 m=next(out.glob('*.py'));icon=load_icon(m);r=icon.validate_icon();(out/'validation.txt').write_text(r.describe())
 svg=icon.to_svg();(out/f'{icon.icon_id}.svg').write_text(svg)
 render_previews(svg,icon.icon_id,48,out)
 meta=json.loads(next(out.glob('*.metadata.json')).read_text());ref=ROOT/meta['reference_path']
 cairosvg.svg2png(url=str(ref),write_to=str(out/'reference.png'),output_width=384,output_height=384)
 print(icon.icon_id,r.status,len(r.errors),len(r.warnings));
 if r.errors or r.warnings: print(r.describe())
for start in range(0,len(outs),5):
 im=Image.new('RGB',(900,185*len(outs[start:start+5])),'#ddd');d=ImageDraw.Draw(im)
 for i,out in enumerate(outs[start:start+5]):
  meta=json.loads(next(out.glob('*.metadata.json')).read_text());icon=meta['icon_id'];d.text((4,i*185+4),icon,fill='black')
  for j,(theme,size) in enumerate([('light',144),('dark',144),('light',48),('dark',48)]):
   svg=(out/f'{icon}.svg').read_text().replace('currentColor','#141413' if theme=='light' else '#f5f4ef')
   png=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size,background_color='#fff' if theme=='light' else '#1c1c19')
   pic=Image.open(io.BytesIO(png));im.paste(pic,(10+j*220,i*185+30))
 im.save(Path(__file__).parent/f'after-{start//5}.png')
