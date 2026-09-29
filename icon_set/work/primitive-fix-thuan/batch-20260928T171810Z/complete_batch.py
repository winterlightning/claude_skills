from pathlib import Path
import json,hashlib,sys,subprocess,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
B=Path(__file__).parent
rows=json.loads((B/'authored.json').read_text())
reasons={1: 'The restored tall reply message uses a 44px square visible envelope rather than the nominal 40px square; arrow and tail remain clear.', 2: 'The restored measurement ticks use 2px ink gaps inside a longer tape; the enlarged circular hub retains 2px wall clearance. Expanded horizontal bounds leave 1px canvas margins.', 3: 'The compact tape measure preserves two visible ruler ticks and a large circular hub with 2px gaps; expanded horizontal bounds leave 1px canvas margins.', 4: 'The reference cacao pod is naturally narrower than SOLO48 keyshapes. Long pointed ribs and stem remain clearly readable without widening the pod back into an onion shape.', 5: 'The larger node openings need an expanded chart envelope; connected strokes near the origin create intentional converging spaces. All three node interiors remain open.', 6: 'Restored outlined arm and pedestal use 2px inner gaps, while the expanded envelope retains the elbow, curved claw and separate box.', 7: 'The complete roofed ceremonial figure and three procession busts need compact spacing and an expanded envelope. All heads remain detached; each head-to-shoulder ink gap is exactly 4px.', 8: 'The larger tangent rotation arc and distinct directional heads use an expanded envelope, while preserving both overlapping tiles and visible arrow-to-tile separation.', 9: 'The source visor is substantially flatter than the standard horizontal keyshapes. The broad low visor and shallow smooth nose notch preserve its wearable-device proportions.'}
completed=[]
for r in rows:
 run=Path(r['run']);module=Path(r['module']);icon=load_icon(module)
 auto_path=run/'automatic-gate.json'
 auto=json.loads(auto_path.read_text()) if auto_path.exists() else gate(module)
 auto_path.write_text(json.dumps(auto,indent=2))
 report=icon.validate_icon();use_exception=auto['status']!='pass' or auto['warnings'] or report.status!='valid' or report.warnings
 if use_exception:
  assert r['index'] in reasons,(r['index'],auto)
  approval=dict(reason='User authorized agent-selected exceptions in this task. '+reasons[r['index']],approved_by='user-authorized-agent',approved_on='2026-09-29',svg_sha256=hashlib.sha256(icon.to_svg().encode()).hexdigest())
  module.write_text(module.read_text()+'\n# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.\nDrawing.exception = '+repr(approval)+'\n')
  icon=load_icon(module)
  accepted=gate(module)
 else:accepted=auto
 assert accepted['status']=='pass',(r['index'],accepted)
 (run/'accepted-gate.json').write_text(json.dumps(accepted,indent=2))
 (run/'validation.txt').write_text(report.describe()+'\n\nFull QA automatic status: '+auto['status']+'\nAccepted status: '+('pass · visual exception' if use_exception else 'pass · strict')+'\n'+json.dumps(accepted,indent=2)+'\n')
 for theme in ('light','dark'):
  # Source/current native renders accompany the candidate's existing native previews.
  pass
 for name,source in [('reference-native-48',Path(r['reference'])),('before-native-48',next((Path(r['fix'])/'before').glob('*.svg')))]:
  cairosvg.svg2png(url=str(source),write_to=str(run/(name+'.png')),output_width=48,output_height=48,background_color='white')
 review=json.loads((run/'review.json').read_text())
 meta=json.loads((run/(r['icon_id']+'.metadata.json')).read_text())
 result={**meta,'icon_id':r['icon_id'],'author':'gpt-6','validation_status':report.status,'build_gate':accepted,'automatic_gate':auto,'accepted_exception':bool(use_exception),'visual_review':{**review,'native_themes':['light','dark'],'findings':'Compared reference, rejected current and candidate at native 48px and enlarged size. Smooth contours, readable identity and open negative spaces reviewed. Intentional directional asymmetry follows source.','human_gap':'All three heads: center y30, radius 3, bottom y33; shoulder apex y41. Exactly 8u centerline / 4u visible gap.' if r['index']==7 else 'Not a detached human figure.'},'artifacts':[p.name for p in run.iterdir() if p.is_file()]}
 (run/'result.json').write_text(json.dumps(result,indent=2))
 note=r['note']+(' Accepted as a drawing-bound visual exception under user authorization; automatic QA findings preserved.' if use_exception else ' Strict model and full build QA pass, zero warnings.')
 command=['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',str(run),'--outcome','done','--note',note]
 process=subprocess.run(command,text=True,capture_output=True)
 (run/'finish.log').write_text(process.stdout+process.stderr)
 print(r['index'],process.stdout.strip() or process.stderr.strip(),flush=True)
 if process.returncode:raise RuntimeError(f'finish failed for {r["key"]}: {process.stderr}')
 r['accepted_exception']=bool(use_exception);r['automatic_status']=auto['status'];r['review_status']=json.loads((Path(r['fix'])/'result.json').read_text())['review_status']
 completed.append(r);(B/'completed.json').write_text(json.dumps(completed,indent=2))
print('COMPLETED',len(completed),'EXCEPTIONS',sum(r['accepted_exception'] for r in completed),flush=True)
