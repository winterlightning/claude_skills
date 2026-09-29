import json,subprocess
from pathlib import Path
b=Path('icon_set/work/primitive-fix-thuan/batch-20260929T044747Z');xs=json.loads((b/'final.json').read_text());assert len(xs)==20
for x in xs:
 note=x['result']['comparison']+(' Drawing-bound visual exception accepted under user authorization; automatic findings retained.' if x['result']['accepted_exception'] else ' Full automatic validation passed without warnings.')
 cmd=['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',x['key'],'--run',x['run'],'--outcome','done','--note',note]
 p=subprocess.run(cmd,text=True,capture_output=True);(Path(x['run'])/'finish-output.txt').write_text(p.stdout+p.stderr);print(x['index'],p.returncode,p.stdout+p.stderr,flush=True)
 if p.returncode:raise SystemExit(p.returncode)
