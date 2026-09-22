import sys,json,importlib.util,inspect
from pathlib import Path
import cairosvg
sys.path.insert(0,str(Path.cwd()))
p=Path(__file__).resolve().parent
i=int(sys.argv[1]);u=json.loads((p/'ids.json').read_text())[i]
f=next(Path('icon_set/model/icons/solo').glob('*'+u.replace('-','_')+'.py'))
spec=importlib.util.spec_from_file_location('icon_set.model.icons.solo.'+f.stem,f);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
cls=next(c for n,c in vars(m).items() if inspect.isclass(c) and c.__module__==m.__name__)
ic=cls();r=ic.validate_icon();(p/f'{i+1:02}-validation.txt').write_text(r.describe());print(r.describe())
svg=ic.to_svg()
for theme in ['light','dark']:
 from icon_set.model.profiles import STROKE
 s=svg.replace('stroke="'+STROKE+'"','stroke="'+('#111111' if theme=='light' else '#eeeeee')+'"')
 for size in [48,240]:
  cairosvg.svg2png(bytestring=s.encode(),write_to=str(p/f'{i+1:02}-draft-{theme}-{size}.png'),output_width=size,output_height=size,background_color='white' if theme=='light' else '#171717')
