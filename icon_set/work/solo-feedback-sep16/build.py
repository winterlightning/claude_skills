from pathlib import Path
import json,sys,subprocess
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
plans=json.loads((W/'plan.json').read_text());cmd=[sys.executable,'icon_set/scripts/build.py','--family','solo','--dist',str(W/'build'),'--no-png','--no-report','--all']
for r in plans:
 if len(sys.argv)==1 or r['icon_id'] in sys.argv[1:]:cmd+=['--icon',r['new_path']]
r=subprocess.run(cmd);(W/'build-exit.txt').write_text(str(r.returncode));sys.exit(r.returncode)
