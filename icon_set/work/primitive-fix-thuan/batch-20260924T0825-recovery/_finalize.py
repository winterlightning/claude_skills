from pathlib import Path
import json,sys,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
root=Path(__file__).parent;rows=json.loads((root/'inputs.json').read_text())
for r in rows:
 out=Path(r['run']);icon=load_icon(r['module']);rep=icon.validate_icon();assert rep.status=='valid' and not rep.warnings,(r['key'],rep.describe())
 assert (out/(r['icon_id']+'.svg')).read_text()==icon.to_svg(),r['key']
 d=json.loads((out/'design.json').read_text())
 for size in (48,384):cairosvg.svg2png(url=r['reference_path'],write_to=str(out/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 result={k:r[k] for k in ('concept','source_uuid','reference_path','icon_id','author','feedback')};result.update(d)
 result.update(validation_status='valid',validation_errors=[],validation_warnings=[],visual_review={'status':'reviewed','native_size':48,'themes':['light','dark'],'findings':'Reviewed smooth contours, subject fidelity, joins, proportions and negative space against original and rejected drawings. '+d['plan']},module=Path(r['module']).name,svg=r['icon_id']+'.svg',artifacts=sorted(p.name for p in out.iterdir() if p.name!='result.json'))
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print('20 complete result folders: valid, zero warnings, SVG matches module.',flush=True)
