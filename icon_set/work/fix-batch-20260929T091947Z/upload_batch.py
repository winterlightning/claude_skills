from pathlib import Path
import json,subprocess,sys
root=Path(__file__).resolve().parents[3];batch=Path(__file__).parent
rows=json.loads((batch/'batch.json').read_text())
for i,r in enumerate(rows):
 dest=Path(r['result_dir']);result=json.loads((dest/'result.json').read_text())
 if (Path(r['fix_dir'])/'result.json').exists():
  print(i,'already finished',r['icon_id'],flush=True);continue
 args=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon','solo/'+r['icon_id'],'--run',str(dest),'--outcome','done','--note',result['changes']+(' User-authorized visual exception; automatic findings retained.' if result['accepted_exception'] else ' Strict validation and full QA pass.')]
 p=subprocess.run(args,cwd=root,text=True,capture_output=True)
 (dest/'finish.log').write_text(p.stdout+p.stderr)
 print(i,p.returncode,p.stdout.strip(),p.stderr.strip(),flush=True)
 if p.returncode:sys.exit(p.returncode)
