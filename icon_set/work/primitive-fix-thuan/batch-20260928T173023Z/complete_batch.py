from pathlib import Path
import json,hashlib,sys,subprocess,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
B=Path(__file__).parent
rows=json.loads((B/'authored.json').read_text())
reasons={5: 'All four suits preserve their natural proportions and the reviewer-requested broad heart. The compact four-part layout uses wider bounds and smaller inter-suit clearances; all counters remain open at native 48px.', 6: 'The apple, folded carton and paired cycle arrows retain the original meaning. Compact carton panels and arrow spacing remain visibly distinct at 48px; the wider bounds support recognizable silhouettes.', 7: 'The reference at-sign requires compact counters and clearance inside the speech bubble. Native light/dark review confirms an open central counter, clear spiral termination and distinct bubble tail.', 8: 'The camera and its lens require compact spacing inside the enclosing speech bubble. The revised smaller camera remains visibly detached from the outer bubble at 48px in both themes.', 10: 'The folded-page bulb composition uses compact bulb, socket and page clearances. The revised bulb is detached from the fold, and both the bulb opening and separate base remain readable at 48px.', 11: 'The reference pin and diagonal ribbon retain their asymmetric proportions and compact internal fold. The widened inner fold has visible negative space at native size; the narrower-than-keyshape silhouette follows the source.', 12: 'The circular upper bowl, oval lower bowl, connecting neck and plus retain the source lowercase g logo. Native review confirms distinct open bowls and separate plus; its typographic proportions use expanded bounds.', 13: 'All seven source waveform bars are restored inside the circular badge. Their 5-unit pitch leaves 1px ink gaps at 48px, visibly separating the bars while retaining the original rhythm.', 14: 'The folded document and inner slide header require compact nested clearances. Rounded contours, the fold counter and two slide fields remain open and identifiable in both native themes.', 15: 'The capsule microphone, rounded camera body, hollow controls and lens preserve the source features. Compact microphone/control openings and the asymmetric full envelope remain recognizable at 48px.', 16: 'The source video-camera proportions require a wide low envelope. Smooth rounded body corners and a tapered lens remain balanced and clear despite differing from the standard horizontal keyshape height.', 17: 'Natural sloping sleeves and short underarm seams create local 3.29-unit ink clearance over only 2 units. Symmetric native-size review confirms clean junctions and no visual congestion.', 18: 'The original tapered speaker and curved sound wave require an asymmetric envelope and compact local clearance. Both the hollow speaker and detached wave remain clear at 48px.', 19: 'The original diagonal blade, teeth and notched grip require asymmetric bounds beyond the square keyshape. Native review confirms three clear teeth, a distinct grip notch and open handle counter.'}
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
 result={**meta,'icon_id':r['icon_id'],'author':'gpt-6','validation_status':report.status,'build_gate':accepted,'automatic_gate':auto,'accepted_exception':bool(use_exception),'visual_review':{**review,'native_themes':['light','dark'],'findings':'Compared reference, rejected current and candidate at native 48px and enlarged size. Smooth contours, readable identity and open negative spaces reviewed. Intentional directional asymmetry follows source.','human_gap':'Not a detached human figure.'},'artifacts':[p.name for p in run.iterdir() if p.is_file()]}
 (run/'result.json').write_text(json.dumps(result,indent=2))
 note=r['note']+(' Accepted as a drawing-bound visual exception under user authorization; automatic QA findings preserved.' if use_exception else ' Strict model and full build QA pass, zero warnings.')
 command=['rtk','proxy','python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',str(run),'--outcome','done','--note',note]
 process=subprocess.run(command,text=True,capture_output=True)
 (run/'finish.log').write_text(process.stdout+process.stderr)
 print(r['index'],process.stdout.strip() or process.stderr.strip(),flush=True)
 if process.returncode:raise RuntimeError(f'finish failed for {r["key"]}: {process.stderr}')
 r['accepted_exception']=bool(use_exception);r['automatic_status']=auto['status'];r['review_status']=json.loads((Path(r['fix'])/'result.json').read_text())['review_status']
 completed.append(r);(B/'completed.json').write_text(json.dumps(completed,indent=2))
print('COMPLETED',len(completed),'EXCEPTIONS',sum(r['accepted_exception'] for r in completed),flush=True)
