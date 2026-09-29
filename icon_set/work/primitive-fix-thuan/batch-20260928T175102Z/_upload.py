from pathlib import Path
import json,subprocess,os,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
items=json.loads((HERE/'items.json').read_text())
env=os.environ.copy();env['SSL_CERT_FILE']='/etc/ssl/cert.pem'
failures=[]
for i,it in enumerate(items):
 fix=ROOT/it['fix']
 if (fix/'result.json').exists():
  prior=json.loads((fix/'result.json').read_text())
  if prior.get('outcome')=='done':print(i,it['key'],'already done',flush=True);continue
 note=it['change']+' AUTHOR gpt-6. '+('Drawing-bound visual exception under user-authorized discretion; original automatic findings retained.' if it['exception'] else 'Strict model and full build gate pass with zero warnings.')
 cmd=['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',it['key'],'--run',it['run'],'--outcome','done','--note',note]
 p=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True)
 (fix/'finish-command.log').write_text(p.stdout+p.stderr)
 print(i,p.stdout.strip() or p.stderr.strip(),flush=True)
 if p.returncode:failures.append((i,p.returncode,p.stderr))
(HERE/'upload-summary.json').write_text(json.dumps({'count':len(items),'failures':failures},indent=2))
sys.exit(bool(failures))
