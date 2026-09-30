from pathlib import Path
import json,subprocess,sys,os
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
rows=json.loads((ROOT/'batch.json').read_text())
audit=json.loads((ROOT/'pre-finish-history-audit.json').read_text())
assert len(rows)==20 and len(audit)==20 and all(x['disapprovals']==1 for x in audit)
env={**os.environ,'SSL_CERT_FILE':'/etc/ssl/cert.pem'}
for i,r in enumerate(rows,1):
 m=json.loads((ROOT/f'latest-{i}.json').read_text());assert (REPO/m['result_dir']/'result.json').is_file()
 existing=REPO/r['claim_dir']/'result.json'
 if existing.is_file():
  result=json.loads(existing.read_text());assert result['outcome']=='done';print(i,r['key'],'already completed',flush=True);continue
 cmd=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',m['result_dir'],'--outcome','done','--note',m['comparison']]
 p=subprocess.run(cmd,cwd=REPO,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (ROOT/f'finish-{i:02}.log').write_text(p.stdout)
 print(f'{i}/20: {p.stdout.strip()}',flush=True)
 if p.returncode:raise SystemExit(p.returncode)
print('All 20 finish calls accepted.',flush=True)
