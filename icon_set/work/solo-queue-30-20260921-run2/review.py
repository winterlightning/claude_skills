import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
import cairosvg
from icon_set.model.icons.registry import create
from icon_set.scripts.contact_sheet import _cell,THEMES
w=Path(__file__).parent
for ident in sys.argv[1:]:
 icon=create(ident);r=icon.validate_icon();(w/(ident+'-validation.txt')).write_text(r.describe());print(ident,r.describe())
 for theme in ('light','dark'):
  t=THEMES[theme];svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="340" height="200"><rect width="340" height="200" fill="{t["page"]}"/>'+_cell(icon,0,0,t)+'</svg>'
  cairosvg.svg2png(bytestring=svg.encode(),write_to=str(w/(ident+'-'+theme+'.png')))
 manifest=json.loads(Path('published/solo48/manifest.json').read_text());print('manifest type',type(manifest).__name__,'export',Path('published/solo48/'+ident+'.svg').exists())
