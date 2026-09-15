import json,subprocess,sys
from pathlib import Path
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='snapshot.json'
AUTHOR='gpt-6'
a=json.loads((W/'snapshot.json').read_text())
cmd=[sys.executable,'icon_set/scripts/build.py','--family','solo','--dist',str(W/'build'),'--no-png','--no-report','--all']
for i in a:cmd+=['--icon',i['python_source']['path']]
r=subprocess.run(cmd);(W/'build-exit.txt').write_text(str(r.returncode));sys.exit(r.returncode)
