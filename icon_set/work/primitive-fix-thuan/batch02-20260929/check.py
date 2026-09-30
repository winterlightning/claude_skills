from pathlib import Path
import sys,json,io
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
for i,r in enumerate(rows):
 if len(sys.argv)>1 and i not in [int(x) for x in sys.argv[1:]]:continue
 if not r.get('run'):continue
 run=Path(r['run']);p=run_module(run);icon=load_icon(p);rep=icon.validate_icon();g=gate(p)
 (run/'validation.txt').write_text(rep.describe()+'\n'+json.dumps(g,indent=2))
 (run/(r['id']+'.svg')).write_text(icon.to_svg())
 render_previews(icon.to_svg(),r['id'],48,run)
 print(i,r['id'],rep.status,g['status'],*rep.errors,*rep.warnings,*g['errors'],*g['warnings'],sep='\n  ',flush=True)
