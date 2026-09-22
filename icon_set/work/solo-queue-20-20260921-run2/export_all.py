import sys,subprocess,time
from pathlib import Path
W=Path(__file__).parent
cmd=[sys.executable,'-m','icon_set','build','--no-png','--no-report']
for i in range(10):cmd+=['--icon',(W/f'{i:02}-original.txt').read_text()]
for attempt in range(20):
 with (W/'build-all.log').open('w') as f:
  r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
 output=(W/'build-all.log').read_text()
 if r.returncode==2 and 'Build output is busy' in output:
  print('Waiting for shared output lock; attempt',attempt+1,flush=True)
  time.sleep(15)
  continue
 print('build exit',r.returncode,flush=True)
 print(output,flush=True)
 break
else:
 print('Shared output remained busy after 20 attempts.',flush=True)
