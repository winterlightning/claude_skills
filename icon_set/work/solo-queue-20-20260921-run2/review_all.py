import sys,json,ast,xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
import cairosvg
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
from icon_set.scripts.contact_sheet import _cell,THEMES
from icon_set.scripts.workspace import build_dist
W=Path(__file__).parent
names=[];results=[];icons=[]
for i in range(10):
 p=Path((W/f'{i:02}-original.txt').read_text());cls=next(n for n in ast.parse(p.read_text()).body if isinstance(n,ast.ClassDef));name=next(ast.literal_eval(n.value) for n in cls.body if isinstance(n,ast.Assign) and n.targets[0].id=='icon_id')
 icon=create(name);icons.append(icon);names.append(name)
 r=inspect_icon(icon);r.pop('_svg',None);(W/f'{i:02}-full-qa.json').write_text(json.dumps(r,indent=2,default=str));print(i,name,r['status'],r['errors'],r['warnings'],flush=True)
 d=json.loads((W/f'{i:02}-intake.json').read_text());results.append(dict(index=i,uuid=d['uuid'],name=name,source=str(p),reference_path='pictographic-primitives/'+d['row']['path'],status=r['status'],errors=r['errors'],warnings=r['warnings'],output=str(build_dist()/'solo48'/f'{name}.svg')))
for t,theme in THEMES.items():
 cells=''.join(_cell(icon,i%5,i//5,theme) for i,icon in enumerate(icons))
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="850" height="380"><rect width="850" height="380" fill="{theme["page"]}"/>'+cells+'</svg>'
 (W/f'contact-sheet-{t}.svg').write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(W/f'contact-sheet-{t}.png'))
(W/'results.json').write_text(json.dumps(results,indent=2))
