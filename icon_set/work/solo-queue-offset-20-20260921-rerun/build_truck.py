import json,subprocess,sys,time
from pathlib import Path
p=Path(__file__).parent
rows=[r for r in json.loads((p/'accepted.json').read_text()) if r['id']=='truck-carrying-a-house']
cmd=[sys.executable,'-m','icon_set','build']
for r in rows: cmd+=['--icon',r['source']]
cmd+=['--no-png','--no-report']
for attempt in range(30):
    result=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(result.stdout,flush=True)
    if result.returncode==0:
        (p/'truck-build.log').write_text(result.stdout);break
    if 'Build output is busy' not in result.stdout:
        (p/'truck-build.log').write_text(result.stdout);sys.exit(result.returncode)
    print('Waiting for shared output lock',attempt+1,flush=True);time.sleep(10)
else: sys.exit(2)
