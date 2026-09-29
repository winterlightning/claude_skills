from pathlib import Path
import json,subprocess,sys
BATCH=Path(__file__).parent
items=json.loads((BATCH/'final-runs.json').read_text())
for i,e in enumerate(items,1):
 previous=Path(e['fix_dir'])/'result.json'
 if previous.exists() and json.loads(previous.read_text()).get('outcome')=='done':
  print(i,e['key'],'already done',flush=True);continue
 note=e['notes']+' Author: gpt-6. '+('User-authorized SVG-bound visual exception; automatic findings preserved.' if e['accepted_exception'] else 'Full validation passes without exceptions.')
 command=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',e['key'],'--run',e['run'],'--outcome','done','--note',note]
 result=subprocess.run(command,text=True,capture_output=True)
 (BATCH/f'upload-{i:02d}.txt').write_text(result.stdout+'\n'+result.stderr)
 print(i,result.returncode,result.stdout.strip() or result.stderr.strip(),flush=True)
 if result.returncode:sys.exit(result.returncode)
