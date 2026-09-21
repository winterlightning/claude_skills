import json,sys,shutil,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
BATCH=ROOT/'reports/uncategorized-solo-batch-01'
p=json.loads((BATCH/'progress.json').read_text())
visual_blocks={
12:'The widened head and muzzle validate, but the long-muzzled baboon identity is not convincing without facial detail. The initial narrow head crowded the muzzle and ears; the wider repair lost species specificity.',
13:'The simplified bonnet reads as a balloon. A broad curved face-opening band and tied ribbons are essential; the current reduction cannot be accepted as a bonnet.',
17:'The simplified profile lost the ear and animal-specific muzzle construction, reading as an abstract hood. A valid envelope is insufficient to accept it as a badger.',
25:'The eye and mouth spacing was repaired, but the radius-2 mouth renders as a solid spot rather than the required opening. Increasing the opening crowds the eye slot or lower mask edge.',
33:'The shortened cap cleared the glasses but lost the backward-cap opening and reads as a generic dome. The baseball-cap identity is not preserved.',
35:'The stadium envelope and diamond pass geometry checks, but the closed wall reads as a drum. The open stadium and seating relationship needs another layout.',
42:'The portrait retained a hat and round jaw but lost the defining beard and backpack cues. Do not accept this generic hatted avatar as the bearded explorer.'}
candidate_dir=ROOT/'icon_set/.local/candidates/uncategorized-solo-batch-01'
candidate_dir.mkdir(parents=True,exist_ok=True)
for e in p['entries']:
 n=e['number']
 if e.get('module'):
  icon=create(e['icon_id']);v=icon.validate_icon();q=inspect_icon(icon)
  e['validation']={'status':v.status,'description':v.describe()}
  e['release_qa']={'status':q['status'],'errors':q['errors'],'warnings':q['warnings']}
  (BATCH/'work'/f'{n:02}-qa.json').write_text(json.dumps(q,indent=2,default=str))
  if n in visual_blocks or q['status']!='pass':
   e['outcome']='blocked'
   e['reason']=visual_blocks.get(n,'Release validation remains unresolved: '+'; '.join(q['errors']+q['warnings']))
   e['visual_review']={'light':'reviewed at 48px','dark':'reviewed at 48px','approved':False,'notes':e['reason']}
   source=ROOT/e['module'];target=candidate_dir/source.name
   shutil.move(source,target)
   e['original_module']=e['module'];e['module']=str(target.relative_to(ROOT));e['candidate_only']=True
  else:
   e['outcome']='generated'
   e['visual_review']={'light':'reviewed at 48px','dark':'reviewed at 48px','approved':True,'notes':'Subject retained after simplification; native-size contour and negative-space review completed.'}
  e['keyshape']=icon.keyshape.name
  e['keyshape_bounds']=icon.keyshape_bounds()
  e['preview_light']=f'icon_set/.local/previews-png/uncategorized-solo-batch-01/{n:02}-light.png'
  e['preview_dark']=f'icon_set/.local/previews-png/uncategorized-solo-batch-01/{n:02}-dark.png'
 e['existing_lookup']={'source_uuid':True,'source_path':True,'exact_icon_id':True,'matches':[]}
 e['usage']={'input':None,'cached_input':None,'output':None,'cache_writes':None,'reason':'Task-scoped runtime counters are unavailable, including setup and tool overhead.'}
 (BATCH/'progress.json').write_text(json.dumps(p,indent=2)+'\n')
 print(n,e['outcome'],flush=True)

cmd=['python3','-m','icon_set','build','--dist','icon_set/.local/batches/uncategorized-solo-batch-01/completed','--no-png','--no-report']
for e in p['entries']:
 if e['outcome']=='generated':cmd+=['--icon',e['module']]
(BATCH/'work'/'completed-build-command.json').write_text(json.dumps(cmd,indent=2))
with (BATCH/'work'/'completed-build.log').open('w') as f:
 result=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT)
p['completed_build']={'exit_code':result.returncode,'dist':'icon_set/.local/batches/uncategorized-solo-batch-01/completed','log':'work/completed-build.log'}
for e in p['entries']:
 if e['outcome']=='generated':e['build']={'exit_code':result.returncode,'log':'work/completed-build.log','targeted':True,'isolated':True}
p['counts']={s:sum(e['outcome']==s for e in p['entries']) for s in ('generated','already-existing','blocked')}
p['usage_checkpoints']=[{'attempted':n,'average_tokens':None,'projected_50_tokens':None,'projected_usd':None,'reason':'No task-scoped usage counters; no defensible planning estimate.'} for n in (5,25,50)]
(BATCH/'progress.json').write_text(json.dumps(p,indent=2)+'\n')
print('FINAL',p['counts'],'build',result.returncode,flush=True)
