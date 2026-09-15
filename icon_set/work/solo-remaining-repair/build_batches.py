from pathlib import Path
import sys,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/review-decisions.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'review-decisions.json').read_text());results=[]
for batch in range(5):
 group=rows[batch*100:batch*100+100];args=[sys.executable,'icon_set/scripts/build.py','--family','solo']
 for row in group:
  if batch==0 and row['number']!=52:continue  # The first run already exported the other99 unchanged outputs.
  args+=['--icon',row['file']]
 with (W/f'build-{batch+1}.log').open('w') as log:r=subprocess.run(args,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
 expected=sum(x['decision']=='blocked' for x in group)
 results.append(dict(batch=batch+1,returncode=r.returncode,expected_failures=expected));(W/'build-results.json').write_text(json.dumps(results,indent=2)+'\n');print('Batch',batch+1,'of5 finished; returncode',r.returncode,'expected unresolved',expected,flush=True)
 if bool(r.returncode)!=bool(expected):raise RuntimeError('Unexpected build outcome; inspect the log before continuing.')
