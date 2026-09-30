from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).parent
for r in json.loads((ROOT/'runs.json').read_text()):
 if len(sys.argv)>1 and r['icon_id'] not in sys.argv[1:]:continue
 if (Path(r['claim'])/'result.json').exists():continue
 p=Path(r['run']);m=run_module(p);icon=load_icon(m);v=icon.validate_icon();g=gate(m)
 (p/'validation.txt').write_text(v.describe()+'\n'+json.dumps(g,indent=2))
 svg=icon.to_svg();(p/(r['icon_id']+'.svg')).write_text(svg);render_previews(svg,r['icon_id'],48,p)
 print(r['icon_id'],v.status,g['status'],v.errors,v.warnings,g['errors'],g['warnings'],flush=True)
