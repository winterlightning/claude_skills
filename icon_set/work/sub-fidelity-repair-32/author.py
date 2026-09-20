"""Preserve parents; reuse verified complete variants or author independent replacements."""
import ast,json,sys,textwrap
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from designs import D,DIMS,GLYPHS
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/sub-fidelity-repair-32/batch.json'
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
 
 for attr in cl.body:
  if isinstance(attr,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='variant_of' for t in attr.targets):attr.value=ast.Constant(r['icon'])
 cl.bases=[ast.Name('SourceFaithfulSideSub',ast.Load())];cl.body+=ast.parse(f'keyshape=Keyshape.{shape}\ncanvas_width={DIMS[n][0]}\ncanvas_height={DIMS[n][1]}').body
 tree.body=[x for x in tree.body if not isinstance(x,ast.FunctionDef)];tree.body+=ast.parse(HELPERS).body;tree.body.insert(0,ast.parse('from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub').body[0])
 # Flatten polylines that participate in a larger contour into their named lines.
 bt=ast.parse(body)
 used={a.value for call in ast.walk(bt) if isinstance(call,ast.Call) and isinstance(call.func,ast.Attribute) and call.func.attr=='add_contour' for a in call.args[1:] if isinstance(a,ast.Constant)}
 replacements={}
 nb=[]
 for stmt in bt.body:
  call=stmt.value if isinstance(stmt,ast.Expr) else None
  if isinstance(call,ast.Call) and isinstance(call.func,ast.Attribute) and call.func.attr=='add_polyline' and call.args[0].value in used:
   name=call.args[0].value;pts=call.args[1:];replacements[name]=[name+'-'+str(i+1) for i in range(len(pts)-1)]
   for i in range(len(pts)-1):nb+=ast.parse('self.add_line('+repr(replacements[name][i])+','+ast.unparse(pts[i])+','+ast.unparse(pts[i+1])+')').body
  else:nb.append(stmt)
 bt.body=nb
 for call in ast.walk(bt):
  if isinstance(call,ast.Call) and isinstance(call.func,ast.Attribute) and call.func.attr=='add_contour':
   call.args=[a for arg in call.args for a in ([ast.Constant(x) for x in replacements[arg.value]] if isinstance(arg,ast.Constant) and arg.value in replacements else [arg])]
 body=ast.unparse(bt)
 cl.body+=ast.parse('def build(self):\n'+textwrap.indent('"""'+parts+'"""\n'+body,'    ')).body
 for x in tree.body:
  if isinstance(x,ast.Assign):
   for t in x.targets:
    if isinstance(t,ast.Name) and t.id in ('AUTHOR','SOURCE_PATH'):x.value=ast.Constant('gpt-6' if t.id=='AUTHOR' else r['source_path'])
 if n in (3,11,17,27):
  variants={3:('symbol-bitcoin-source-serifs',),11:('letter-i-source-plain',),17:('letter-o-source-round','digit-2-source-curved'),27:('letter-m-source-sloping',)}
  tree.body=[x for x in tree.body if not(isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='TYPEFACE_PROFILE_VARIANTS' for t in x.targets))]
  tree.body+=ast.parse('TYPEFACE_PROFILE_VARIANTS='+repr(variants[n])).body
 if n in GLYPHS:
  tree.body=[x for x in tree.body if not(isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='TYPEFACE_GLYPH_IDS' for t in x.targets))];tree.body+=ast.parse('TYPEFACE_GLYPH_IDS='+repr(GLYPHS[n])).body
 tree.body[0:0]=[ast.Expr(ast.Constant(parts+' Complete-source repair; previous variant preserved.'))]
 ast.fix_missing_locations(tree);dst.write_text(ast.unparse(tree)+'\n');out[key]=dict(number=n,parent=r['icon'],icon=uid,python_source=str(dst.relative_to(ROOT)),parts=parts,reason=parts,reused_existing_complete_variant=False)
(W/'candidates.json').write_text(json.dumps(out,indent=2));print('Prepared',len(out),'complete-composition candidates')
