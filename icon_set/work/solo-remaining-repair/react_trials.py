from pathlib import Path
import sys,ast,inspect,concurrent.futures,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID='d36538a0-eba4-47cf-8fa5-4782d3bb6574'
SOURCE_PATH='pictographic-primitives/logos/react native logo_d36538a0-eba4-47cf-8fa5-4782d3bb6574.svg'
AUTHOR='gpt-6'
def trial(ry):
 from icon_set.model.icons.registry import create
 from icon_set.validation.library_qa import inspect_icon
 parent=create('react-logo');cls=type(parent);t=ast.parse(Path(inspect.getfile(cls)).read_text());c=next(x for x in t.body if isinstance(x,ast.ClassDef));f=next(x for x in c.body if isinstance(x,ast.FunctionDef) and x.name=='build');s=ast.unparse(f).replace('rx, ry = (20, 9)',f'rx, ry = (20, {ry})');ns={};exec(s,ns);candidate=type('Candidate',(cls,),{'build':ns['build']})();q=inspect_icon(candidate)
 return dict(ry=ry,status=q['status'],errors=q['errors'],holes=q['negative_space'].get('failed_hole_count'),pinches=q['negative_space'].get('pinch_count'))
if __name__=='__main__':
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
  for r in pool.map(trial,[8,10,11,12,13,14,15]):print(json.dumps(r),flush=True)
