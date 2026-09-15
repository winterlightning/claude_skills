from pathlib import Path
import subprocess,json,os
ROOT=Path(__file__).resolve().parents[3];W=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
plan=json.loads((W/'override-plan.json').read_text());args=['python3','-B','icon_set/scripts/build.py','--family','solo']
for row in plan:args+=['--icon',row['target']]
with (W/'override-build.log').open('w') as out:
 p=subprocess.run(args,cwd=ROOT,stdout=out,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
(W/'override-build-status.json').write_text(json.dumps({'exit_code':p.returncode,'selected_originals':len(plan)},indent=2));print('Original icon build exit',p.returncode)
