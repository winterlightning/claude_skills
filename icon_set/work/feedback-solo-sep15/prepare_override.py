from pathlib import Path
import ast,json,hashlib,collections
ROOT=Path(__file__).resolve().parents[3];W=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
R=json.loads((W/'revisions.json').read_text());A={str(x['number']):x for x in json.loads((W/'inventory.json').read_text())};I=json.loads((W/'live-index.json').read_text());groups=collections.defaultdict(list)
def metadata(tree):
 out={}
 for node in tree.body:
  if isinstance(node,ast.Assign):
   for target in node.targets:
    if isinstance(target,ast.Name):
     try:out[target.id]=ast.literal_eval(node.value)
     except (ValueError,TypeError):pass
 return out
for n,r in R.items():
 source=W/'snapshot'/r['file'];md=metadata(ast.parse(source.read_text()));matches=[x for x in I if x['id']==r['parent']]
 if not matches:matches=[x for x in I if x['source']==md['SOURCE_ICON_ID'] and x['parent'] is None]
 assert len(matches)==1,(n,r['parent'],matches)
 groups[matches[0]['path']].append(dict(number=int(n),**r,current_id=matches[0]['id']))
plan=[]
for target,rs in sorted(groups.items()):
 chosen=max(rs,key=lambda r:r['number']);path=ROOT/target;original=path.read_text();current=ast.parse(original);new=ast.parse((W/'snapshot'/chosen['file']).read_text());md=metadata(current)
 current_class=next(n for n in current.body if isinstance(n,ast.ClassDef));new_class=next(n for n in new.body if isinstance(n,ast.ClassDef));new_class.name=current_class.name
 for n in new.body:
  if isinstance(n,ast.Assign):
   for t in n.targets:
    if isinstance(t,ast.Name) and t.id in ['SOURCE_ICON_ID','SOURCE_PATH']:n.value=ast.Constant(md.get(t.id))
 new_class.body=[n for n in new_class.body if not (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['variant_of','variant_label'] for t in n.targets))]
 for n in new_class.body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in n.targets):n.value=ast.Constant(chosen['current_id'])
 if isinstance(new.body[0],ast.Expr) and isinstance(new.body[0].value,ast.Constant):new.body[0].value.value=chosen['note']+' Applied to the original icon identity.'
 output=ast.unparse(ast.fix_missing_locations(new))+'\n';dest=W/'override-staged'/path.name;dest.parent.mkdir(exist_ok=True);dest.write_text(output)
 plan.append({'target':target,'id':chosen['current_id'],'before_sha256':hashlib.sha256(original.encode()).hexdigest(),'after_sha256':hashlib.sha256(output.encode()).hexdigest(),'selected_brief':chosen['number'],'selected_proposal':chosen['id'],'feedback_numbers':sorted(r['number'] for r in rs),'proposals':sorted({r['id'] for r in rs}),'staged':str(dest.relative_to(W))})
(W/'override-plan.json').write_text(json.dumps(plan,indent=2));print('Original files to overwrite:',len(plan));print('Different proposal choices:',[(x['id'],x['selected_brief'],len(x['proposals'])) for x in plan if len(x['proposals'])>1]);print('Target IDs containing v2/v3:',[x['id'] for x in plan if '-v2' in x['id'] or '-v3' in x['id']])
