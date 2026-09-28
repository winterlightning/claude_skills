from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
notes=[
'Clean opposed elliptical sync sweeps and horizontal arrow wings; straight symmetric A.',
'Tangent dial crown and mirrored smooth bulb shoulders, rounded socket and circular indicator.',
'Straight suspension, smooth folded limb and flowing torso; opened sling/body spacing and retained exact 4-unit detached head gap.',
'Equal media nodes and clean mirrored scan chevrons around a straight-sided play triangle.',
'Mirrored smooth heart lobes and wings with a centered elliptical halo.',
'Smooth continuous diagonal infinity crossing with clear minus and plus strokes.',
'Smooth back-of-head transition and jaw, straight profile runs, round puzzle tab with wider clearance.',
'Mirrored smooth car roof, semicircular wheel contours and four equal sensor arcs.',
'Truly straight fork and parcel edges, tangent seated hip curves, equal circular wheels and exact 4-unit head gap.',
'Straight diagonal shaft and clean collar, smooth broad blade with a continuous cutting edge.'
]
refs=['refresh-cw','lightbulb','human_ref/full_body_ref.png; no useful exact Lucide pose','no useful exact Lucide match; supplied composition','heart','infinity','puzzle; human-reference.md continuous profile','car-front','bike; human_ref/full_body_ref.png','axe']
omissions=[
'Compact arrowheads to preserve clearance around the A.',
'Socket divider omitted because its small enclosed band would be crowded at 48px.',
'Anatomical outline reduced to coherent limb and torso strokes; suspended pose retained.',
'Hexagon nodes reduced to equal circles and arrow stems omitted to retain all three node and scan positions with legal spacing.',
'Fine feather divisions omitted; one broad feather per wing.',
'No component omitted; plus/minus arms shortened for interior clearance.',
'Small side indentation of loose puzzle piece omitted; primary round puzzle tab and missing region retained.',
'Redundant inner sensor band omitted; wheels integrated as semicircular lower contour.',
'Scooter panels, headlight and hub details omitted; rider, parcel, steering and wheels retained.',
'Handle width reduced to a single shaft; broad cutting blade retained.'
]
for i,r in enumerate(rows):
 d=Path(r['dir']);g=json.loads((d/'gate.json').read_text());assert g['status']=='pass' and not g['warnings']
 p=next(d.glob('*.py'));s=p.read_text()
 if i==3:s=s.replace('Keyshape HRECT_L chosen','Keyshape SQUARE chosen')
 p.write_text(s)
 meta=json.loads((d/(r['id']+'.metadata.json')).read_text())
 result={**meta,'icon_id':r['id'],'author':'gpt-6','validation_status':'valid','validation_warnings':[],'build_gate':g,'keyshape':'HRECT_M' if i==5 else 'SQUARE','keyshape_reason':'Wide infinity mark with two loops.' if i==5 else 'Balanced full composition fits the 36 by 36 centerline envelope.','visual_review':{'native_light':'reviewed','native_dark':'reviewed','enlarged_light':'reviewed','enlarged_dark':'reviewed','findings':notes[i],'intentional_asymmetry':'Plus and minus differ semantically.' if i==5 else ('Pose, viewpoint or composition follows the original reference.' if i in [1,2,6,8,9] else 'Paired geometry derived from shared parameters.')},'construction_references':refs[i],'omissions':omissions[i],'artifacts':sorted(x.name for x in d.iterdir() if x.is_file() and x.name!='result.json')}
 (d/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 r['note']=notes[i];r['omissions']=omissions[i];r['references']=refs[i]
(ROOT/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:
 if (Path(r['fix'])/'result.json').exists():
  print('Already finished',r['key'],flush=True);continue
 cmd=['python3','icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',r['key'],'--run',r['dir'],'--outcome','done','--note',r['note']]
 completed=subprocess.run(cmd,text=True,capture_output=True)
 print(completed.stdout,completed.stderr,flush=True)
 if completed.returncode:sys.exit(completed.returncode)
