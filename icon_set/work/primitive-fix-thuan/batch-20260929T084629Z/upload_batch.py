"""Upload and finish exactly the twenty already-claimed icons; never claim extras."""
import json,sys,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
BATCH=Path(__file__).resolve().parent
rows=json.loads((BATCH/'batch.json').read_text())
failed=[]
for index,row in enumerate(rows,1):
 out=ROOT/row['result_dir'];fix=ROOT/row['fix_dir']
 if (fix/'result.json').exists():
  existing=json.loads((fix/'result.json').read_text())
  assert existing['outcome']=='done'
  print(index,row['key'],'already finished in this claim',flush=True);continue
 assert (out/'result.json').exists(),out
 note=row['comparison']+' '+row['plan']+' Reviewed at native size in light and dark; AUTHOR=gpt-6.'
 record=json.loads((out/'result.json').read_text())
 if record.get('exception'):note+=' User-authorized drawing-specific exception; automatic findings retained.'
 command=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',row['key'],'--run',row['result_dir'],'--outcome','done','--note',note]
 print(f'{index}/20 finishing {row["key"]}',flush=True)
 completed=subprocess.run(command,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (out/'finish-upload.log').write_text(completed.stdout)
 print(completed.stdout,flush=True)
 if completed.returncode:failed.append(row['key'])
print('UNFINISHED:',failed,flush=True)
sys.exit(bool(failed))
