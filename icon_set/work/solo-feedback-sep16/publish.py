from pathlib import Path
import sys,json,subprocess
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
plans=json.loads((W/'plan.json').read_text())
cmd=[sys.executable,'icon_set/scripts/build.py','--family','solo','--all','--no-report']
for r in plans:cmd+=['--icon',r['new_path']]
p=subprocess.run(cmd);(W/'publish-exit.txt').write_text(str(p.returncode));sys.exit(p.returncode)
