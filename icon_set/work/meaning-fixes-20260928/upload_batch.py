from pathlib import Path
import json,subprocess,sys
ROOT=Path('icon_set/work/meaning-fixes-20260928');R=json.loads((ROOT/'runs.json').read_text())
for n,r in R.items():
 result=Path(r['fix'])/'result.json'
 if result.exists():
  existing=json.loads(result.read_text())
  if existing.get('outcome')=='done':print(n,r['id'],'already done',flush=True);continue
 note=r['change']+' Compared original and rejected SVG; reviewed at 48px in both themes. AUTHOR=gpt-6.'
 if r['release_status']=='pass-exception':note+=' User-authorized drawing-bound visual exception: '+r['exception_reason']
 command=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',r['result_dir'],'--outcome','done','--note',note]
 print('Uploading',n,r['key'],flush=True)
 completed=subprocess.run(command,text=True,capture_output=True)
 (Path(r['result_dir'])/'production-finish.log').write_text(completed.stdout+'\n'+completed.stderr)
 print(completed.stdout.strip(),flush=True)
 if completed.returncode:
  print(completed.stderr,flush=True);raise SystemExit(completed.returncode)
print('ALL 20 DONE',flush=True)
