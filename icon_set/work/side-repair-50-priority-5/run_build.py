import json,subprocess,sys
from pathlib import Path
w=Path(__file__).resolve().parent
args=[sys.executable,'-m','icon_set','build','--no-png','--no-report']
for r in json.loads((w/'accepted.json').read_text()):args+=['--icon',r['candidate_python']]
with (w/'build.log').open('w') as f:result=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT)
(w/'build-result.json').write_text(json.dumps({'exit_code':result.returncode}))
raise SystemExit(result.returncode)
