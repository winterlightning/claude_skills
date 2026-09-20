"""Build the three accepted profiles together after both batches are activated."""
import json,subprocess,sys
from pathlib import Path
W=Path(__file__).resolve().parent;dirs=[W,W.parent/'side-repair-50-priority-8'];args=[sys.executable,'-m','icon_set','build','--no-png','--no-report']
for w in dirs:
 for r in json.loads((w/'accepted.json').read_text()):args+=['--icon',r['candidate_python']]
with (W/'build.log').open('w') as f:r=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT)
for w in dirs:(w/'build-result.json').write_text(json.dumps({'exit_code':r.returncode,'shared_build_log':str(W/'build.log')}))
raise SystemExit(r.returncode)
