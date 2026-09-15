from pathlib import Path
import ast,json
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='avatar-sources.json'
AUTHOR='gpt-6'
plans=json.loads((W/'plan.json').read_text());sources=json.loads((W/'avatar-sources.json').read_text())
for r in plans:
 if r['icon_id'] not in sources:continue
 source=Path(sources[r['icon_id']]);s=source.read_text();tree=ast.parse(s)
 cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));cls.name=r['class_name']
 attrs={'icon_id':r['new_id'],'variant_of':r['icon_id'],'variant_label':'Refined solo portrait after visual rejection','human_construction':'bust'}
 cls.body=[n for n in cls.body if not(isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in attrs for t in n.targets))]
 cls.body[0:0]=[ast.Assign(targets=[ast.Name(id=k,ctx=ast.Store())],value=ast.Constant(value=v)) for k,v in attrs.items()]
 ast.fix_missing_locations(tree);Path(r['new_path']).write_text(ast.unparse(tree)+'\n')
 r['geometry_reference']=str(source);r['change']='Reconstructed from the matching SOLO48 portrait: circular jaw, contact with curved shoulders, and preserved clothing/headwear.'
(W/'plan.json').write_text(json.dumps(plans,indent=2))
