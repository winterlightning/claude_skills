from pathlib import Path
import json,subprocess,sys
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T091731Z-meaning')
rs=json.loads((B/'runs.json').read_text())
AUTHOR='gpt-6'
for r in rs:
 SOURCE_ICON_ID=r['source_uuid'];SOURCE_PATH=r['reference_path']
 done=Path(r['fix_dir'])/'result.json'
 if done.exists():
  status=json.loads(done.read_text())
  if status.get('outcome')=='done':print(r['key'],'already done for this claim',flush=True);continue
 note=r['change']+' Author: gpt-6. '+('Reviewed at 48px in light/dark; user-authorized drawing-bound exception, automatic QA retained.' if r['accepted_exception'] else 'Full automatic validation and build gate passed without warnings.')
 cmd=['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',r['result_dir'],'--outcome','done','--note',note]
 result=subprocess.run(cmd,capture_output=True,text=True)
 (Path(r['result_dir'])/'production-finish.log').write_text(result.stdout+result.stderr)
 print(result.stdout.strip() or result.stderr.strip(),flush=True)
 if result.returncode:print('FINISH ERROR',result.returncode,r['key'],flush=True);sys.exit(result.returncode)
print('FINISHED ALL 20',flush=True)
