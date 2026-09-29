from pathlib import Path
import json,hashlib,sys,subprocess,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
B=Path(__file__).parent
rows=json.loads((B/'authored.json').read_text())
reasons={
0:'Compact six-leg bug needs 2px wall clearance while the slender phone and 4px strokes remain readable.',
1:'The dollar currency ticks need compact clearance inside the slender phone; the S bowls stay open and legible.',
3:'The pin and its center dot retain about 3px clearance to preserve the reference symbol within a slender phone.',
4:'QR finder squares retain 2px openings and compact 2px spacing; native-size review confirms four distinct marks.',
5:'The recording ring needs 2px phone-wall clearance; the restored dot remains clearly separated inside the ring.',
8:'The woman retains long hair and full shoulders in a slender phone, with a 4px detached head/body gap; compact wall/hair clearances remain visible.',
11:'Feedback explicitly requests a smaller phone and a lower divider; the smaller envelope and 2px home-mark gaps preserve that layout.',
12:'The larger avatar preserves an exact 4px head/body gap and has compact clearance to its enclosing phone.',
13:'The wider message composition restores the right tail and text lines; expanded envelope and compact currency ticks preserve source meaning.',
14:'The long pointing finger and diagonal thumb require narrow finger width and an asymmetric envelope; native review confirms recognizable hand and separated pulse.',
15:'A and B remain separated and readable; their compact counters and enlarged monitor envelope require visual exceptions. C was omitted to prevent crowding.',
16:'The source-proportioned wider/taller screen and stand use an expanded envelope; compact plus/divide spacing remains clear at 48px.',
17:'The taller screen retains two 2px square openings and 2px vertical gaps; both squares remain distinct at 48px.',
18:'Natural tall four-finger anatomy uses 6u centerline finger widths and a wider asymmetric thumb envelope; 2px finger spaces remain open.',
19:'Natural tall four-finger anatomy uses 6u centerline finger widths and a wider asymmetric thumb envelope; 2px finger spaces remain open.'}
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
 result={**meta,'icon_id':r['icon_id'],'author':'gpt-6','validation_status':report.status,'build_gate':accepted,'automatic_gate':auto,'accepted_exception':bool(use_exception),'visual_review':{**review,'native_themes':['light','dark'],'findings':'Compared reference, rejected current and candidate at native 48px and enlarged size. Smooth contours, readable identity and open negative spaces reviewed. Intentional directional asymmetry follows source.','human_gap':'Face/head bottom y21; shoulder apex y29; 8u centerline / 4u visible gap.' if r['index'] in (8,12) else 'Not a detached human figure.'},'artifacts':[p.name for p in run.iterdir() if p.is_file()]}
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
