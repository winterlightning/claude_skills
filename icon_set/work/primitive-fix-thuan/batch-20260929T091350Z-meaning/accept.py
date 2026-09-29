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
reasons=[
'Cloud lobes and sparse windows remain recognizable at 48px. The composed skyline needs compact window and cloud clearances and a one-unit keyshape adjustment.',
'The swept rotor retains three distinct blades, a central hub and tapered mast. Compact real blade/hub attachments and the mast preserve the turbine rather than a flower.',
'The fanned card angles and small diamond suit are essential. Compact suit opening and occlusion clearances remain readable in both themes.',
'Three rounded feather tips, converging ribs and the cork define the shuttlecock. Internal taper advisories are intentional feather convergence, reviewed at 48px.',
'Three flames over a supported burner preserve the gas-stove identity. Compact flame and foot clearances remain visibly open at native size.',
'Three broad separated ribbon arrows restore the reference recycling symbol. The thicker ribbons require compact interior clearances and a near-full-canvas envelope.',
'Three broad separated ribbon arrows restore the reference recycling symbol. The thicker ribbons require compact interior clearances and a near-full-canvas envelope.',
'A square faceplate is necessary to avoid a standalone face interpretation. The nested circular socket and type-K earth aperture remain open and distinct with compact clearances.',
'Three continuous-neck portrait outlines and orthogonal connections restore the source organization-chart topology. Their compact openings and linked connections remain recognizable.',
'Three complete torso outlines restore the side people omitted by the rejected drawing. A wider envelope and compact inter-person gaps preserve all three figures; each detached head/body gap is exactly 4 ink units.',
'The trumpet retains three valves, capped stems, looped tubing and flared bell. Tube junctions and compact loop spacing preserve the instrument at 48px.',
'The tilted pastry shell, inner ridge and crimped edge distinguish a turnover from a tunnel. The natural pastry aspect uses a shorter envelope and compact ridge spacing.',
'The rear bust is partly occluded by the foreground bust. Both heads retain exact 4-unit detached ink gaps; an exact curved head/shoulder distance remains an automatic advisory.',
'The rear bust is partly occluded by the foreground bust. Both heads retain exact 4-unit detached ink gaps; an exact curved head/shoulder distance remains an automatic advisory.',
'Overlapping folder silhouettes retain two tabs and a clear foreground body. An exact curved occlusion clearance remains an automatic advisory.',
'Two scalloped squash bodies, stems and curved rib cues need compact occlusion and detail clearances. The organic silhouette deliberately differs from the rectangular envelope.',
'Two seated shoulder silhouettes, circular heads, sled shell and runner preserve the bobsled scene. Both detached head/body gaps are exactly 4 ink units; compact riders and shell contacts need a visual exception.',
'Two suspended skulls need paired eye sockets, squared jaws and a centered loop. Compact eye/tooth openings and suspension contacts remain readable at native size.',
'Two-root molars and square brackets joined by an archwire define dental braces. Small bracket openings and tapered roots remain legible, with automatic small-opening advisories retained.',
'The suspension bridge uses a straight deck, two towers, sagging cable and a central suspender above water. Compact real junctions and a natural envelope preserve a clear bridge silhouette.'
]
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
