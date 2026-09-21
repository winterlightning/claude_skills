import importlib.util,json,pathlib,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
WORK=pathlib.Path(__file__).parent
rows=json.loads((WORK/'manifest.json').read_text());results=[]
for row in rows:
 try:
  spec=importlib.util.spec_from_file_location('icon_set.model.icons.solo._candidate',row['candidate'])
  mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
  icon=mod.Drawing();report=icon.validate_icon()
  result={**row,'status':report.status,'report':report.describe()}
  d=WORK/'previews';d.mkdir(exist_ok=True)
  (d/f"{row['number']}.svg").write_text(icon.to_svg())
 except Exception as e:result={**row,'status':'error','report':str(e)}
 results.append(result)
 print(row['number'],result['status'],flush=True)
 (WORK/'validation.json').write_text(json.dumps(results,indent=2)+'\n')
from collections import Counter
print(Counter(r['status'] for r in results))
