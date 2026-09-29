from pathlib import Path
import json,sys,concurrent.futures
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
ROOT=Path('icon_set/work/meaning-fixes-20260928')
def check(pair):
 n,r=pair;p=Path(r['module']);icon=load_icon(p);report=icon.validate_icon();g=gate(p)
 out=Path(r['result_dir']);(out/'validation.txt').write_text(report.describe()+'\n\n'+json.dumps(g,indent=2))
 v=dict(status=report.status,errors=list(report.errors),warnings=list(report.warnings),gate=g)
 (out/'validation.json').write_text(json.dumps(v,indent=2))
 return n,v
if __name__=='__main__':
 R=json.loads((ROOT/'runs.json').read_text());indices=sys.argv[1:];pairs=[p for p in R.items() if not indices or p[0] in indices]
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as ex:
  for n,v in ex.map(check,pairs):print(n,json.dumps(v),flush=True)
