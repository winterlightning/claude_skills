from pathlib import Path
import json,sys,subprocess
root=Path(__file__).resolve().parent;repo=root.parents[2]
rows=json.loads((root/'batch.json').read_text())
for i in map(int,sys.argv[1:]):
 r=rows[i];claim=repo/r['claim_dir']
 if (claim/'result.json').exists():
  print(i,'already finished',flush=True);continue
 run=repo/r['result_dir']
 result=json.loads((run/'result.json').read_text());assert result['icon_id']==r['icon_id'];assert result['build_gate']['status']=='pass',(i,result['build_gate'])
 design=json.loads((run/'design.json').read_text())
 note=design['change']
 if result['build_gate'].get('exception'):note+=' User-authorized visual exception; automatic findings retained.'
 p=subprocess.run(['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',str(run.relative_to(repo)),'--outcome','done','--note',note],cwd=repo,text=True,capture_output=True)
 (run/'production-finish.txt').write_text(p.stdout+p.stderr)
 print(i,p.returncode,p.stdout,p.stderr,flush=True)
 if p.returncode:sys.exit(p.returncode)
