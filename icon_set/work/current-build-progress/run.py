from pathlib import Path
import sys,json,subprocess,datetime,collections,shutil
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import factories
W=Path(__file__).parent;D=ROOT/'icon_set/dist';r=factories();folders={'solo':'solo48','sub':'sub32','container':'container64'};errors=[];counts=collections.Counter()
for name in ['solo-review-batch-100.html','hole-review-batch-100.html','solo-remaining-review.html']:
 p=D/'gallery'/name
 if p.exists():shutil.copy2(p,W/name)
for folder in folders.values():(W/'inputs'/folder).mkdir(parents=True,exist_ok=True)
for ident,f in r.items():
 try:(W/'inputs'/folders[f.family]/(ident+'.svg')).write_text(f().to_svg());counts[f.family]+=1
 except Exception as e:errors.append({'icon':ident,'error':str(e)})
(W/'render-errors.json').write_text(json.dumps(errors,indent=2));print('Canonical current drawings:',dict(counts),'render errors:',len(errors),flush=True)
for family,folder in folders.items():
 print('QA overlays starting:',family,flush=True)
 with (W/(family+'-overlays.log')).open('w') as log:
  result=subprocess.run([sys.executable,'-u','qa_overlays.py',str(W/'inputs'/folder),'--out-dir',str(ROOT/'icon_set/work/qa_overlays'/folder),'--jobs','6','--force'],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
 print('QA overlays finished:',family,'exit',result.returncode,flush=True)
 if result.returncode:raise SystemExit(result.returncode)
print('Full build starting',flush=True)
with (W/'build.log').open('w') as log:
 result=subprocess.run([sys.executable,'-u','icon_set/scripts/build.py','--all','--debug'],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
print('Full build finished, exit:',result.returncode,flush=True)
(W/'build-exit.json').write_text(json.dumps({'exit_code':result.returncode,'completed_at':datetime.datetime.now().isoformat()}))
