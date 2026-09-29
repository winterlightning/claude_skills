from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
for i,r in enumerate(rows):
 if (Path(r['fix_dir'])/'result.json').exists():
  print(i,r['key'],'already finished',flush=True);continue
 args=['rtk','proxy','python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',r['run'],'--outcome','done','--note',r['change']+(' User-authorized visual exception: '+r['exception_reason'] if r.get('exception_reason') else '')]
 result=subprocess.run(args,text=True,capture_output=True)
 (ROOT/f'upload-{i:02}.txt').write_text(result.stdout+result.stderr)
 print(i,r['key'],'exit',result.returncode,result.stdout.strip(),result.stderr.strip(),flush=True)
