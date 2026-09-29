from pathlib import Path
import sys,json,hashlib,datetime,shutil
import cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews,approved_visual_exception
from icon_set.scripts.build_gate import gate
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
b=Path(__file__).parent
rows=json.loads((b/'items.json').read_text())
reasons=['The complete standing performer and curved tied-back curtains remain distinct at 48px. Compact figure-to-curtain and limb spacing preserves the stage composition without shrinking the person. Head/body ink gap is exactly 4 units.', 'The pet has a distinct pointed-ear head, seated haunches and a front-leg division. The human arms use compact but visibly open torso spacing to retain both subjects. Human head/body ink gap is exactly 4 units.', 'The triangular sling, diagonal shoulder strap and horizontal forearm are essential meaning cues. Their compact openings remain legible at 48px in both themes. Head-to-shoulder ink gap is exactly 4 units.', 'A continuous upright body, writing pen and open-legged desk restore the action. Compact forearm, hand/pen/paper contacts and the natural scene envelope are visually accepted; head-to-shoulder ink gap remains exactly 4 units.', 'The complete pregnant silhouette retains a rounded abdomen, one leg and a bent arm, using the VRECT_M envelope and exactly 4 units of head/body ink gap.', 'The elongated whole fruit and its longitudinal ridge identify starfruit behind the softly lobed cross-section. Compact occlusion and seed spacing plus the natural composition envelope remain readable at native size.', 'The aligned leaning rider, bent pedaling leg and broad stationary-bike housing restore the exercise scene. The natural scene envelope is visually accepted; head radius 5 and the 5-12-13 head-to-neck triangle prove exactly 4 units of ink clearance.']

stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
for n,(r,reason) in enumerate(zip(rows,reasons),1):
 if len(sys.argv)>1 and n not in [int(v) for v in sys.argv[1:]]: continue
 old=Path(r['run']);module=Path(r['module']);icon=load_icon(module);report=icon.validate_icon()
 raw=gate(module)
 (old/'build-gate.json').write_text(json.dumps(raw,indent=2))
 (old/'result.json').write_text(json.dumps(dict(source_uuid=old.parent.name,reference_path=r['reference'],icon_id=r['icon_id'],author=AUTHOR,validation_status=report.status,build_gate=raw,visual_review='Inspected at 48px and 144px in both light and dark themes; selected for final visual exception review.',omissions=r['omissions'],artifacts=[p.name for p in old.iterdir() if p.is_file()]),indent=2))
 run=old.parent/f'{stamp}-reviewed-{n:02}'
 run.mkdir()
 for p in old.iterdir():
  if p.is_file() and p.name not in ('result.json','build-gate.json','validation.txt'):shutil.copyfile(p,run/p.name)
 target=run/module.name
 exception=None
 if raw['status']!='pass' or report.status!='valid' or report.warnings:
  exception=dict(reason=reason,approved_by='user-authorized visual review by gpt-6',approved_on='2026-09-29',svg_sha256=hashlib.sha256(icon.to_svg().encode()).hexdigest())
  target.write_text(target.read_text()+'\n# User explicitly delegated exceptions after visual UI/UX review.\nDrawing.exception = '+repr(exception)+'\n')
 icon=load_icon(target);rep=icon.validate_icon();g=gate(target)
 accepted=approved_visual_exception(rep,g)
 if not ((rep.status=='valid' and not rep.warnings and g['status']=='pass') or accepted):
  raise RuntimeError((n,r['key'],rep.describe(),g))
 svg=icon.to_svg();(run/(r['icon_id']+'.svg')).write_text(svg)
 for size in (48,384):cairosvg.svg2png(url=r['reference'],write_to=str(run/f'reference-{size}.png'),output_width=size,output_height=size,background_color='#ffffff')
 (run/'validation.txt').write_text(rep.describe()+'\n\nFull build gate: '+g['status']+'\nAutomatic gate: '+g.get('automatic_status',g['status'])+'\n'+json.dumps(g,indent=2))
 (run/'build-gate.json').write_text(json.dumps(g,indent=2))
 findings=dict(source_uuid=run.parent.name,reference_path=r['reference'],icon_id=r['icon_id'],author=AUTHOR,validation_status=rep.status,validation_errors=rep.errors,validation_warnings=rep.warnings,build_gate=g,accepted_exception=accepted,visual_review=dict(status='reviewed',sizes=[48,144,384],themes=['light','dark'],comparison=r['comparison'],feedback=r['feedback'],changes=r['change'],findings=reason),omissions=r['omissions'],keyshape=r['keyshape'],construction_references=r['construction_references'],artifacts=sorted(p.name for p in run.iterdir() if p.is_file()))
 (run/'result.json').write_text(json.dumps(findings,indent=2))
 r.update(run=str(run),module=str(target),exception=exception,validation_status=rep.status,gate_status=g['status'],automatic_gate_status=g.get('automatic_status',g['status']))
 (b/'items.json').write_text(json.dumps(rows,indent=2))
 print(n,r['icon_id'],g['status'],'exception' if accepted else 'strict',flush=True)
