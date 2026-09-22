import sys,json,ast
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
import cairosvg
from icon_set.model.icons.registry import create
from icon_set.scripts.contact_sheet import _cell,THEMES
from icon_set.scripts.workspace import build_dist
W=Path(__file__).parent
i=int(sys.argv[1]);p=Path((W/f'{i:02}-original.txt').read_text());tree=ast.parse(p.read_text());cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));name=next(ast.literal_eval(n.value) for n in cls.body if isinstance(n,ast.Assign) and n.targets[0].id=='icon_id')
icon=create(name);r=icon.validate_icon();(W/f'{i:02}-validation.txt').write_text(r.describe());print(r.describe())
for t,theme in THEMES.items():
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="340" height="200"><rect width="340" height="200" fill="{theme["page"]}"/>'+_cell(icon,0,0,theme)+'</svg>'
 cairosvg.svg2png(bytestring=svg.encode(),write_to=str(W/f'{i:02}-{t}.png'))
 export=build_dist()/'solo48'/f'{name}.svg'
 if export.exists():
  raw=export.read_text().replace('currentColor',theme['ink'])
  cairosvg.svg2png(bytestring=raw.encode(),write_to=str(W/f'{i:02}-export-{t}.png'),output_width=48,output_height=48,background_color=theme['page'])
manifest=json.loads((build_dist()/'solo48/manifest.json').read_text())
print('manifest match:',name in json.dumps(manifest))
