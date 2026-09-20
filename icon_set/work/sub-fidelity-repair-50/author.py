"""Preserve parents; reuse verified complete variants or author independent replacements."""
import ast,json,sys,textwrap
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from designs import D,DIMS,GLYPHS
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/sub-fidelity-repair-50/batch.json'
AUTHOR='gpt-6'
helpers=ast.parse((ROOT/'icon_set/work/sub-failed-repair-50/repair.py').read_text());HELPERS=next(ast.literal_eval(n.value) for n in helpers.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
rows=json.loads((W/'batch.json').read_text());out=json.loads((W/'candidates.json').read_text()) if (W/'candidates.json').exists() else {}
for r in rows:
 n=r['number'];key=str(n)
 if n not in D:
  v=r['replacement'];out[key]=dict(number=n,parent=r['icon'],icon=v['new_id'],python_source=v['new_model_path'],parts=v.get('parts',[]),reason=v['reason'],reused_existing_complete_variant=True);continue
 shape,parts,ref,body=D[n]
 if key in out:dst=ROOT/out[key]['python_source'];uid=out[key]['icon'];source=dst.read_text()
 else:
  dst,uid,source=prepare_variant(r['icon'],'sub','Complete original restored on a proportionate canvas');dst=dst.with_name(dst.stem+'_'+r['source_uuid'].replace('-','_')+'.py')
 tree=ast.parse(source);cl=next(x for x in tree.body if isinstance(x,ast.ClassDef));cl.body=[x for x in cl.body if not isinstance(x,ast.FunctionDef) and not(isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id in ('keyshape','canvas_width','canvas_height') for y in x.targets))]
 cl.bases=[ast.Name('SourceFaithfulSideSub',ast.Load())];cl.body+=ast.parse(f'keyshape=Keyshape.{shape}\ncanvas_width={DIMS[n][0]}\ncanvas_height={DIMS[n][1]}').body
 tree.body=[x for x in tree.body if not isinstance(x,ast.FunctionDef)];tree.body+=ast.parse(HELPERS).body;tree.body.insert(0,ast.parse('from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub').body[0])
 cl.body+=ast.parse('def build(self):\n'+textwrap.indent('"""'+parts+'"""\n'+body,'    ')).body
 for x in tree.body:
  if isinstance(x,ast.Assign):
   for t in x.targets:
    if isinstance(t,ast.Name) and t.id in ('AUTHOR','SOURCE_PATH'):x.value=ast.Constant('gpt-6' if t.id=='AUTHOR' else r['source_path'])
 if n in GLYPHS:
  tree.body=[x for x in tree.body if not(isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='TYPEFACE_GLYPH_IDS' for t in x.targets))];tree.body+=ast.parse('TYPEFACE_GLYPH_IDS='+repr(GLYPHS[n])).body
 ast.fix_missing_locations(tree);dst.write_text(ast.unparse(tree)+'\n');out[key]=dict(number=n,parent=r['icon'],icon=uid,python_source=str(dst.relative_to(ROOT)),parts=parts,reason=parts,reused_existing_complete_variant=False)
(W/'candidates.json').write_text(json.dumps(out,indent=2));print('Prepared',len(out),'complete-composition candidates')
