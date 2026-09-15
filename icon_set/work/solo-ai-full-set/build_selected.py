from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];w=Path(__file__).parent
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/solo-ai-full-set/release-check.json'
passed={q['icon_id'] for q in json.loads((w/'release-check.json').read_text()) if q['status']=='pass'}
rows=[r for r in json.loads((w/'batch.json').read_text()) if r['icon_id'] in passed]+json.loads((w/'construction-cleanup.json').read_text())
cmd=[sys.executable,'icon_set/scripts/build.py','--family','solo','--no-report']
for r in rows:cmd.extend(['--icon',r['path']])
print('Building',len(rows),'passing variants',flush=True)
p=subprocess.run(cmd,cwd=ROOT);sys.exit(p.returncode)
