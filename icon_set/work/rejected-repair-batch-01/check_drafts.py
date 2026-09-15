import json,sys,importlib.util
from pathlib import Path
from icon_set.model.icons import registry
from icon_set.validation.library_qa import inspect_icon
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
def load(r,side='after'):
 p=ROOT/(r['original_model'] if side=='before' else r.get('variant_path',r['original_model']))
 name='icon_set.model.icons.solo._draft_'+side+'_'+str(r['batch_index'])
 spec=importlib.util.spec_from_file_location(name,p);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
 ident=r['icon_id'] if side=='before' else r.get('variant_id',r['icon_id'])
 return next(c for c in vars(mod).values() if isinstance(c,type) and c.__module__==name and getattr(c,'icon_id',None)==ident)
if __name__=='__main__':
 rows=json.loads((OUT/'batch.json').read_text());result=[];(OUT/'qa').mkdir(exist_ok=True)
 for r in rows:
  if len(sys.argv)>1 and str(r['batch_index']) not in sys.argv[1:]:continue
  q=inspect_icon(load(r)());svg=q.pop('_svg',None)
  if svg:(OUT/'previews'/f'{r["batch_index"]}-after.svg').write_text(svg)
  (OUT/'qa'/f'{r["batch_index"]}.json').write_text(json.dumps(q,indent=2))
  result.append({'index':r['batch_index'],'id':q['icon_id'],'status':q['status'],'errors':q['errors'],'warnings':q['warnings']})
  if q['status']!='pass':print(r['batch_index'],r['icon_id'],q['status'],q['errors'],q['warnings'],flush=True)
 (OUT/'after-validation.json').write_text(json.dumps(result,indent=2))
 print('Pass:',sum(r['status']=='pass' for r in result),'of',len(result))
