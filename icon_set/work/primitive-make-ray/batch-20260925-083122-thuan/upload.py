from pathlib import Path
import json,subprocess,os
root=Path('icon_set/work/primitive-make-ray/batch-20260925-083122-thuan');rows=json.loads((root/'manifest.json').read_text())
env=dict(os.environ,SSL_CERT_FILE='/etc/ssl/cert.pem')
for row in rows:
 result=json.loads((Path(row['run'])/'result.json').read_text());note=row['note']
 if result['exception']:note+=' Drawing-specific visual exception authorized by user; automatic findings retained.'
 p=subprocess.run(['python3','icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',row['key'],'--run',row['run'],'--outcome','done','--note',note],env=env,text=True,capture_output=True)
 (Path(row['run'])/'finish.log').write_text(p.stdout+p.stderr)
 print(row['index'],row['key'],p.returncode,p.stdout[-700:],p.stderr[-700:],flush=True)
 if p.returncode:raise SystemExit(p.returncode)
