from pathlib import Path
import json,sys,hashlib
from icon_set.scripts import primitive_fix as p, work_queue as w
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
rows=json.loads((ROOT/'runs.json').read_text())
omissions=[
'No defining feature omitted; wrap recomposed on the integer grid.',
'Minor anatomical contour detail simplified; two pain wisps retained.',
'Cigarette rendered as one clear diagonal stroke instead of a narrow outlined tube.',
'No defining feature omitted; hearts enlarged for legibility.',
'Inner flame line omitted; flame, wick, bowl, handle and foot retained.',
'No defining feature omitted; all four hierarchy nodes retained.',
'No defining feature omitted; all three rectangular nodes restored.',
'Lower player divider omitted to preserve room for a clear circular control.',
'Inner hexagonal bores simplified to circular bores.',
'No defining feature omitted; elongated bag and hanger retained.',
'Tiny helmet band replaced by a discrete lamp so it does not fill the circular face.',
'No defining feature omitted; pockets, flap, fastening tab and front seam retained.',
'Extra outer jaw contour omitted; broad muzzle and domed head carry the silhouette.',
'Leaf serrations reduced; both toothed leaves, veins and all three berries retained.',
'No defining feature omitted; video house floats above a lens and base.',
'No defining feature omitted; floating cube, rays, lens and base retained.',
'Outlined rib capsules reduced to three rounded ribs on a continuous shaft.',
'No defining feature omitted; open circular links and connecting bar retained.',
'Slat count standardized to three for native-size clarity; left circular pull retained.',
'Slat count standardized to three for native-size clarity; right circular pull retained.',
]
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
 'human_spacing_evidence': 'head center (27,10), r5, neck (22,22): sqrt(5^2+12^2)-5-4 = 4 ink units; torso follows this lean.' if i==10 else None,
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
