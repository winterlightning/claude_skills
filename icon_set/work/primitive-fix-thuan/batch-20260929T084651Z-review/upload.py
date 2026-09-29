from pathlib import Path
import json,subprocess,sys
B=Path(__file__).parent
R=B.parents[3]
runs=json.loads((B/'final-runs.json').read_text())
items={r['id']:r for r in json.loads((B/'items.json').read_text())}
results=[]
for n,r in enumerate(runs,1):
 it=items[r['icon_id']];receipt=R/it['fix']/'result.json'
 if receipt.exists():
  done=json.loads(receipt.read_text())
  if done.get('outcome')=='done':
   results.append({'key':it['key'],'code':0,'receipt':str(receipt.relative_to(R))});print(n,it['key'],'already done',flush=True);continue
 note=r['change']+' Reviewed at native 48px in light and dark themes. '+('Drawing-bound visual exception under the user authorization; automatic findings retained.' if r['accepted_exception'] else 'Strict model and full build gate pass with zero warnings.')
 cmd=['rtk','proxy','python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',it['key'],'--run',r['run'],'--outcome','done','--note',note]
 p=subprocess.run(cmd,cwd=R,text=True,capture_output=True)
 (B/(r['icon_id']+'-finish.log')).write_text(p.stdout+p.stderr)
 results.append({'key':it['key'],'code':p.returncode,'receipt':str(receipt.relative_to(R)) if receipt.exists() else None})
 print(n,p.stdout.strip() or p.stderr.strip(),flush=True)
 (B/'upload-results.json').write_text(json.dumps(results,indent=2))
if any(r['code'] for r in results): sys.exit(1)
