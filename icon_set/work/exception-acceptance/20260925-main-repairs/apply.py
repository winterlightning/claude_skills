"""Apply the prepared, explicitly approved batch with concurrency checks."""
from pathlib import Path
import json,hashlib,subprocess,sys
from datetime import datetime,timezone
ROOT=Path.cwd();OUT=ROOT/'icon_set/work/exception-acceptance/20260925-main-repairs'
rows=json.loads((OUT/'prepared.json').read_text())
for row in rows:
 target=ROOT/row['target']
 if hashlib.sha256(target.read_bytes()).hexdigest()!=row['previous_sha256']:
  raise SystemExit('Source changed since preparation; preserving it: '+row['target'])
for row in rows:
 (ROOT/row['target']).write_bytes((ROOT/row['staged']).read_bytes())
 approval=dict(row['exception'],module=row['target'],icon_id=row['icon_id'],applied_at=datetime.now(timezone.utc).isoformat(),latest_nonstandard_run_retained=bool(row['fallback']))
 (ROOT/row['run']/'exception-applied.json').write_text(json.dumps(approval,indent=2)+'\n')
 # Keep historical run results; the batch manifest is the authority for this acceptance.
(OUT/'applied.json').write_text(json.dumps(rows,indent=2)+'\n')
command=[sys.executable,'-m','icon_set','build','--no-png','--no-report','--jobs','4']
for row in rows:command+=['--icon',row['target']]
print('Applied 47 drawing-specific exceptions; building selected originals.',flush=True)
raise SystemExit(subprocess.call(command))
