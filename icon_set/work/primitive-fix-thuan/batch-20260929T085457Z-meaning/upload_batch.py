"""Finish only this batch's twenty authorized, visually reviewed production claims."""
from pathlib import Path
import json, subprocess, sys

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).parent

def main():
 rows=json.loads((HERE/'finals.json').read_text())
 assert len(rows)==20 and len({r['key'] for r in rows})==20
 for row in rows:
  claim=ROOT/row['claim']
  done=claim/'result.json'
  if done.exists():
   saved=json.loads(done.read_text())
   assert saved['outcome']=='done' and saved['make_ray_run']==row['result_dir']
   print(row['key']+': verified already done',flush=True)
   continue
  note=row['plan']['change']
  note+=' Author: gpt-6. '
  note+=('User-authorized, drawing-bound visual exception; automatic findings retained.' if row['exception'] else
         'Full automatic validation and build gate pass with zero warnings.')
  args=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac',
        '--icon',row['key'],'--run',row['result_dir'],'--outcome','done','--note',note]
  print('Uploading '+row['key'],flush=True)
  proc=subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
  (ROOT/row['result_dir']/'production-finish.log').write_text(proc.stdout+proc.stderr)
  print(proc.stdout+proc.stderr,end='',flush=True)
  if proc.returncode:
   raise SystemExit(proc.returncode)
 print('All 20 production finishes confirmed.',flush=True)

if __name__=='__main__': main()
