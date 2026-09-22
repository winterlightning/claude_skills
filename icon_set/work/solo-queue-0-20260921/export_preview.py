from pathlib import Path
import ast,json,io,sys
sys.path.insert(0,str(Path.cwd()))
import cairosvg
from PIL import Image,ImageDraw
w=Path(__file__).resolve().parent
rs=[r for r in json.loads((w/'results.json').read_text()) if r['outcome']!='unresolved']
manifest={r['icon_id']:r for r in json.loads(Path('published/solo48/manifest.json').read_text())['icons']}
labels=['Bicycle in rack','Cycling helmet','Rounded tree','Birdcage','Spouting whale','Infant bonnet','Exposed brain']
sheet=Image.new('RGB',(168*7,440),'white');draw=ImageDraw.Draw(sheet)
verified=[]
for j,(r,label) in enumerate(zip(rs,labels)):
 tree=ast.parse(Path(r['python_original']).read_text());c=next(n for n in tree.body if isinstance(n,ast.ClassDef));id=next(ast.literal_eval(n.value) for n in c.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in n.targets))
 svg_path=Path('published/solo48')/(id+'.svg')
 if id=='domed-cycling-helmet-with-chin-strap' and '--candidate-helmet' in sys.argv:
  from icon_set.model.icons.registry import create
  svg=create(id).to_svg()
 else:
  assert id in manifest,id
  assert manifest[id]['profile']=='SOLO48'
  svg=svg_path.read_text()
  verified.append({'uuid':r['uuid'],'icon_id':id,'svg':str(svg_path),'manifest':'published/solo48/manifest.json'})
 for row,(bg,ink) in enumerate([('#ffffff','#111111'),('#202020','#f4f4f4')]):
  x=j*168;y=row*220
  draw.rectangle((x,y,x+168,y+220),fill=bg)
  painted=svg.replace('currentColor',ink)
  for size,dx,dy in [(96,36,12),(48,60,130)]:
   raw=cairosvg.svg2png(bytestring=painted.encode(),output_width=size,output_height=size,background_color=bg)
   sheet.paste(Image.open(io.BytesIO(raw)).convert('RGB'),(x+dx,y+dy))
  draw.text((x+12,y+194),label,fill=ink)
name='export-preview-candidate.png' if '--candidate-helmet' in sys.argv else 'export-preview.png'
sheet.save(w/name)
(w/'manifest-verification.json').write_text(json.dumps(verified,indent=2))
print(name,len(verified),'verified exports')
