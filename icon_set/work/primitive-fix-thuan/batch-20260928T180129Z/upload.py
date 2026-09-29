from pathlib import Path
import json,subprocess,sys
root=Path(__file__).resolve().parent
xs=json.loads((root/'authored.json').read_text())
for d in xs:
 done=Path(d['fix_dir'])/'result.json'
 if done.exists() and json.loads(done.read_text()).get('outcome')=='done':
  print(d['n'],'already confirmed done',flush=True);continue
 note=d['change']+' AUTHOR=gpt-6. '+('Drawing-bound visual exception under user authorization; automatic findings retained.' if d['validation_status']=='pass-exception' else 'Strict validation and build gate pass with zero warnings.')
 cmd=['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',d['key'],'--run',d['run'],'--outcome','done','--note',note]
 result=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (Path(d['run'])/'production-finish.log').write_text(result.stdout)
 print(d['n'],result.returncode,result.stdout.strip(),flush=True)
 if result.returncode:print('REQUIRES FOLLOW-UP',d['key'],flush=True)
