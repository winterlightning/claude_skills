from pathlib import Path
import json,subprocess
W=Path(__file__).resolve().parent;S=W/'snapshot';r=json.loads((W/'revisions.json').read_text())
args=['python3','icon_set/scripts/build.py','--family','solo','--dist',str(W/'build'),'--png-dir',str(W/'png')]
for file in sorted(set(v['file'] for v in r.values())):args.extend(['--icon',str(S/file)])
with (W/'build.log').open('w') as out:
 p=subprocess.run(args,cwd=S,stdout=out,stderr=subprocess.STDOUT)
(W/'build-status.json').write_text(json.dumps({'exit_code':p.returncode,'variant_count':len(set(v['id'] for v in r.values()))}))
print('Build exit',p.returncode)
