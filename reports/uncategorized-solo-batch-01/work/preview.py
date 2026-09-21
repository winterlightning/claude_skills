import io,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
import cairosvg
from PIL import Image,ImageDraw
from icon_set.model.icons.registry import create
from icon_set.scripts.workspace import DEFAULT_PNG
BATCH=ROOT/'reports/uncategorized-solo-batch-01'
entries=json.loads((BATCH/'progress.json').read_text())['entries']
out=Path(DEFAULT_PNG)/'uncategorized-solo-batch-01';out.mkdir(parents=True,exist_ok=True)
for theme,bg,fg in [('light','#ffffff','#111111'),('dark','#171717','#eeeeee')]:
 for start in range(0,50,10):
  sheet=Image.new('RGB',(1000,460),bg);d=ImageDraw.Draw(sheet)
  for e in entries:
   n=e['number'];i=n-start-1
   if i<0 or i>=10 or not e.get('module'):continue
   try:svg=create(e['icon_id']).to_svg()
   except Exception as ex:print(n,ex);continue
   # Theme changes are renderer presentation only, never edits to exported SVGs.
   svg=svg.replace('currentColor',fg).replace('#000000',fg).replace('"black"',f'"{fg}"')
   native=cairosvg.svg2png(bytestring=svg.encode(),output_width=48,output_height=48,background_color=bg)
   (out/f'{n:02}-{theme}.png').write_bytes(native)
   im=Image.open(io.BytesIO(native));x=i%5*200;y=i//5*230
   sheet.paste(im.resize((144,144)),(x+28,y+10));sheet.paste(im,(x+76,y+160));d.text((x+6,y+215),f'{n:02} '+e['icon_id'][:26],fill=fg)
  sheet.save(out/f'authored-{start+1:02}-{theme}.png')
print(out)
