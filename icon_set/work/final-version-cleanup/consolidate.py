from pathlib import Path
import sys,json,shutil,hashlib,datetime
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts import consolidate_variants as cv
from icon_set.model.icons.registry import factories
W=Path(__file__).parent;D=ROOT/'icon_set/dist'
r=factories();plan,errors=cv.plan_groups(r);errors+=cv.check_plan(plan,r);assert not errors,errors
cv.svg_hashes(plan,r)
for g in plan:
 q=json.loads((D/'qa'/g['family']/g['latest']/'metrics.json').read_text())
 assert q['svg_sha256']==g['old_sha'],g['latest']
 assert q['status']=='pass' or g['latest']=='react-logo-v2',(g['latest'],q['status'])
 g['expected_status']=q['status']
b=ROOT/'icon_set/data'/('final-version-cleanup-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
cv.backup(plan,cv.DEFAULT_DB,b)
reviews=ROOT/'icon_set/model/contracts/spacing-reviews.v1.json';shutil.copy2(reviews,b/reviews.name)
shutil.copytree(D/'gallery',b/'gallery')
records=json.loads(reviews.read_text())
for g in plan:
 key=g['family']+'/'+g['latest'];record=records['icons'].get(key)
 for ident in [g['latest']]+[o['icon_id'] for o in g['olds']]:records['icons'].pop(g['family']+'/'+ident,None)
 if record:
  assert record['svg_sha256']==g['old_sha'],key
  record['svg_sha256']=g['new_sha'];records['icons'][g['family']+'/'+g['root']]=record
cv.apply_sources(plan)
reviews.write_text(json.dumps(records,indent=2)+'\n')
counts=cv.migrate_database(plan,cv.DEFAULT_DB)
(W/'plan.json').write_text(json.dumps(plan,indent=2)+'\n');(W/'backup.txt').write_text(str(b)+'\n');print('Consolidated',len(plan),'groups; removed',sum(len(g['olds']) for g in plan),'redundant registered versions. Backup:',b);print(counts)
