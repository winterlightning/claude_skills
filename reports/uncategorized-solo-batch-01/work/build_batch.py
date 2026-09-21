import json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
BATCH=ROOT/'reports/uncategorized-solo-batch-01'
p=json.loads((BATCH/'progress.json').read_text())
for e in p['entries']:
 if not e.get('module'):continue
 n=e['number'];start=time.monotonic()
 qa=inspect_icon(create(e['icon_id']))
 (BATCH/'work'/f'{n:02}-qa.json').write_text(json.dumps(qa,indent=2,default=str))
 e['release_qa']={'status':qa['status'],'errors':qa['errors'],'warnings':qa['warnings']}
 cmd=['python3','-m','icon_set','build','--icon',e['module'],'--no-png','--no-report']
 r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 (BATCH/'work'/f'{n:02}-build.log').write_text(r.stdout+r.stderr)
 e['build']={'command':cmd,'exit_code':r.returncode,'log':f'work/{n:02}-build.log'}
 e['outcome']='awaiting-final-review' if qa['status']=='pass' and r.returncode==0 else 'blocked'
 (BATCH/'progress.json').write_text(json.dumps(p,indent=2)+'\n')
 print(n,qa['status'],'build',r.returncode,round(time.monotonic()-start,1),'s',flush=True)
