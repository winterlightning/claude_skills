import importlib.util,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.validation.library_qa import inspect_icon
WORK=pathlib.Path(__file__).parent
results=[]
for row in json.loads((WORK/'validation.json').read_text()):
 if row['status']!='valid':continue
 spec=importlib.util.spec_from_file_location('icon_set.model.icons.solo._candidate',row['candidate']);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 qa=inspect_icon(mod.Drawing());qa.pop('_svg',None)
 results.append({'number':row['number'],'icon_id':row['icon_id'],'qa':qa})
 print(row['number'],qa['status'],qa['errors'],qa['warnings'],flush=True)
 (WORK/'full-qa.json').write_text(json.dumps(results,indent=2)+'\n')
