from pathlib import Path
import sys,json,subprocess,time
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
b=Path(__file__).parent
rows=json.loads((b/'items.json').read_text())
for n,r in enumerate(rows,1):
 # Re-entry resumes only this batch's unfinished claims; successful finish records are authoritative.
 result=Path(r['fix_dir'])/'result.json'
 if result.exists() and json.loads(result.read_text()).get('outcome')=='done':
  print(n,r['key'],'already done',flush=True);continue
 note=r['change']+' AUTHOR=gpt-6.'
 if r.get('exception'): note+=' User-authorized drawing-bound visual exception; automatic findings retained.'
 command=['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',r['run'],'--outcome','done','--note',note]
 for attempt in range(3):
  done=subprocess.run(command,capture_output=True,text=True)
  (b/f'finish-{n:02}.log').write_text(done.stdout+done.stderr)
  print(n,done.stdout.strip(),done.stderr.strip(),flush=True)
  if done.returncode==0:break
  if done.returncode==2:raise SystemExit(f'Validation rejected {r["key"]}; repair required')
  if attempt==2:raise SystemExit(f'Upload needs retry: {r["key"]}')
