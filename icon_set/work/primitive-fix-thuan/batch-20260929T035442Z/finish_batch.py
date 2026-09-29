from pathlib import Path
import json,sys,hashlib
from icon_set.scripts import primitive_fix as p, work_queue as w
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
rows=json.loads((ROOT/'runs.json').read_text())
omissions=['Fine robe panel seams omitted; long parted hair, circular jaw and central robe collar retained.', 'Fine robe panel seams omitted; long parted hair, circular jaw and central robe collar retained.', 'Tiny device detailing reduced to the phone control; both foreground devices, laptop side edges and notched base retained.', 'No defining feature omitted; two vertically stacked outlined squares restored.', 'No defining feature omitted; two tall upright panels, connecting body and curved base retained.', 'Fine rim curvature simplified; deep hull, three signal arcs and water retained.', 'No defining feature omitted; low lard portion, curled end and rectangular tray retained.', 'Laurel reduced to three paired leaf strokes along one curved twig; head profile and crown direction retained.', 'Fine facial contour detail simplified; open laughing mouth, closed eyes and both large tears retained.', 'Tiny wheel hubs omitted; unequal wheels, mower hood, steering stem and back/seat retained.', 'Beam reduced to one clear stroke and lattice reduced to one X; horsehead, pump rod and counterweight retained.', 'Minor pastry contour irregularities simplified; plump mass, two curled ends and four rolling seams retained.', 'Scale count reduced to the major overlapping rows; pointed crown, lower lobes and stem retained.', 'Tiny box markings omitted; open canopy, cab, large front wheel and original stacked-box arrangement retained. No rear wheel invented.', 'Tiny eye omitted to keep the head open; split comb, beak, plump body, tail lobes and feet retained.', 'Small lip bulges simplified to a clear open mouth; closed eye, anatomical neck and three sneeze rays retained.', 'Fine skin folds omitted; long pointing index, thumb, palm and all three folded-finger steps retained.', 'Tiny eye omitted; woolly contour, drooping ear, muzzle and two short legs retained.', 'No defining feature omitted; removed the unreferenced heavy waistband and raised the crotch.', 'Figure represented with the shared stick-figure vocabulary; elevated chair, two ladder rungs and two water rows retained.']

# Final local handoff is written only after visual inspection and all QA gates.
for i,row in enumerate(rows):
 run=Path(row['run']);SOURCE_ICON_ID=run.parent.name;SOURCE_PATH=row['reference']
 assert row['gate_status']=='pass'
 icon=p.load_icon(Path(row['module']))
 result={'source_uuid':SOURCE_ICON_ID,'reference_path':SOURCE_PATH,'concept':Path(SOURCE_PATH).stem[:-37],
 'icon_id':row['id'],'author':AUTHOR,'keyshape':icon.keyshape.name,
 'validation_status':row['validation_status'],'build_gate_status':row['gate_status'],
 'accepted_exception':row['accepted_exception'],'exception_reason':row['exception_reason'],
 'automatic_errors':row['automatic_errors'],'automatic_warnings':row['automatic_warnings'],
 'visual_review':'Inspected original and rejected drawing, then native 48px and enlarged output in light and dark. Defining features restored; rounded strokes and negative spaces remain legible.',
 'original_current_comparison':row['comparison'],'reviewer_feedback':row['feedback'],'changes':row['change'],
 'references_used':row['references'],'omissions':omissions[i],
 'human_spacing_evidence': ('Circular r9 jaw reaches y26; shoulder minimum is y30. Centerline gap 4 minus two 2px half-strokes = zero visible ink gap.' if i in (0,1) else 'Head center (14,8), r4, neck (14,20): 20-(8+4)-4 = exactly 4 ink units. Head is aligned on the vertical torso axis.' if i==19 else None),
 'artifacts':sorted(x.name for x in run.iterdir() if x.is_file())}
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
raw=w.call
def reliable(base,method,path,body=None,query=None):
 for n in range(6):
  try:return raw(base,method,path,body,query)
  except w.ApiError as e:
   if e.status:raise
   print('Network retry',n+1,method,path,flush=True)
 raise RuntimeError('Production connection unavailable after six attempts')
w.call=reliable
failed=[]
for row in rows:
 outcome_path=Path(row['fix'])/'result.json'
 if outcome_path.exists():
  saved=json.loads(outcome_path.read_text())
  if saved.get('outcome')=='done' and saved.get('review_status')=='ready':
   print('Already verified done',row['key'],flush=True);continue
 note=row['change']+' Compared original and rejected drawing; reviewed at 48px in both themes. AUTHOR=gpt-6. User-authorized exact-SVG visual exception; automatic findings retained.'
 try:
  rc=p.main(['finish','--worker','thuan-mac','--icon',row['key'],'--run',row['run'],'--outcome','done','--note',note])
  if rc:failed.append(row['key'])
 except Exception as e:
  failed.append(row['key']);print('Finish error',row['key'],str(e),flush=True)
print('FINISH FAILURES:',failed,flush=True)
raise SystemExit(bool(failed))
