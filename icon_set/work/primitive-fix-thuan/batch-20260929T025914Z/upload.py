from pathlib import Path
import json,subprocess,sys
BATCH=Path(__file__).resolve().parent
entries=json.loads((BATCH/'final.json').read_text())
results=[]
for n,e in enumerate(entries,1):
 note=e['change']+' Compared original and rejected drawing; native light/dark visual review passed. User-authorized drawing-bound exception retains automatic findings. AUTHOR=gpt-6.'
 cmd=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon','solo/'+e['icon_id'],'--run',e['run'],'--outcome','done','--note',note]
 result=subprocess.run(cmd,text=True,capture_output=True)
 (BATCH/f'finish-{n:02d}.log').write_text(result.stdout+result.stderr)
 results.append(dict(key='solo/'+e['icon_id'],exit_code=result.returncode,stdout=result.stdout,stderr=result.stderr))
 (BATCH/'upload-results.json').write_text(json.dumps(results,indent=2)+'\n')
 print(f'{n}/20 '+result.stdout.strip()+' '+result.stderr.strip(),flush=True)
 if result.returncode:print('UPLOAD FAILED: retained for retry',flush=True)
