from pathlib import Path
import os,sys,json,subprocess
BATCH=Path(__file__).resolve().parent;ROOT=BATCH.parents[3]
items=json.loads((BATCH/'items.json').read_text());results=json.loads((BATCH/'final-results.json').read_text())
env=os.environ.copy();env['SSL_CERT_FILE']='/etc/ssl/cert.pem'
completed=[];failed=[]
for item,result in zip(items,results):
 receipt=ROOT/item['fix_dir']/'result.json'
 if receipt.exists():
  existing=json.loads(receipt.read_text())
  if existing.get('outcome')=='done':completed.append(item['key']);print(item['key']+': already confirmed done',flush=True);continue
 note=result['change']
 if result['accepted_exception']:note+=' Native-size reviewed; accepted drawing-specific exception under user authorization, automatic findings retained.'
 cmd=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',item['key'],'--run',result['result_dir'],'--outcome','done','--note',note]
 p=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True)
 (ROOT/result['result_dir']/'upload.log').write_text(p.stdout+p.stderr)
 print(p.stdout or p.stderr,flush=True)
 if p.returncode==0:completed.append(item['key'])
 else:failed.append(dict(key=item['key'],returncode=p.returncode,error=p.stderr))
(BATCH/'upload-status.json').write_text(json.dumps(dict(completed=completed,failed=failed),indent=2))
print('Confirmed done:',len(completed),'Failed:',len(failed),flush=True)
