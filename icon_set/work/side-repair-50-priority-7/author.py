"""Persist independently editable variants once; re-running edits only this batch's variants."""
import ast,json,sys,textwrap
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from designs import D
GLYPHS={}
TEXT={}
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH=str(W/'batch.json')
AUTHOR='gpt-6'
helpers=ast.parse((ROOT/'icon_set/work/sub-failed-repair-50/repair.py').read_text())
HELPERS=next(ast.literal_eval(n.value) for n in helpers.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
rows=json.loads((W/'batch.json').read_text());out=json.loads((W/'candidates.json').read_text()) if (W/'candidates.json').exists() else {}
for n,(shape,parts,ref,body) in D.items():
 r=rows[n-1]
 if str(n) in out:
  dst=ROOT/out[str(n)]['python_source'];uid=out[str(n)]['icon'];text=dst.read_text()
 else:
  dst,uid,text=prepare_variant(r['icon'],'sub','Source-faithful side-combination centerline repair')
  dst=dst.with_name(dst.stem+'_'+r['source_uuid'].replace('-','_')+'.py')
 t=ast.parse(text);cl=next(x for x in t.body if isinstance(x,ast.ClassDef));cl.body=[x for x in cl.body if not (isinstance(x,ast.FunctionDef) and x.name=='build')]
 for x in cl.body:
  if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='keyshape' for y in x.targets):x.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),shape,ast.Load())
 for x in t.body:
  if isinstance(x,ast.Assign):
   for target in x.targets:
    if isinstance(target,ast.Name) and target.id in ('AUTHOR','SOURCE_PATH'):x.value=ast.Constant('gpt-6' if target.id=='AUTHOR' else r['source_path'])
 t.body=[x for x in t.body if not isinstance(x,ast.FunctionDef)]
 t.body+=ast.parse(HELPERS).body
 if n in TEXT:
  spec=TEXT[n]
  for node in t.body:
   if isinstance(node,ast.ImportFrom) and node.module=='_base':node.module='_text_base';node.names=[ast.alias('TextSub32')]
  cl.bases=[ast.Name('TextSub32',ast.Load())]
  attrs={'text_canvas_width':spec['width'],'text_ink_bounds':spec['bounds']}
  cl.body=[x for x in cl.body if not (isinstance(x,ast.Assign) and any(isinstance(z,ast.Name) and z.id in attrs for z in x.targets))]
  cl.body+=ast.parse('\n'.join(k+' = '+repr(v) for k,v in attrs.items())).body
  t.body=[x for x in t.body if not (isinstance(x,ast.Assign) and any(isinstance(z,ast.Name) and z.id=='TYPEFACE_GLYPH_IDS' for z in x.targets))]
  t.body+=ast.parse('TYPEFACE_GLYPH_IDS = '+repr(spec['glyphs'])).body
 if n in GLYPHS:
  t.body=[x for x in t.body if not (isinstance(x,ast.Assign) and any(isinstance(z,ast.Name) and z.id=='TYPEFACE_GLYPH_IDS' for z in x.targets))]
  t.body+=ast.parse('TYPEFACE_GLYPH_IDS = '+repr(GLYPHS[n])).body
 cl.body+=ast.parse('def build(self):\n'+textwrap.indent('"""'+parts+' Construction reference: '+ref+'."""\n'+textwrap.dedent(body),'    ')).body
 ast.fix_missing_locations(t);dst.write_text(ast.unparse(t)+'\n')
 out[str(n)]={'number':n,'parent':r['icon'],'icon':uid,'python_source':str(dst.relative_to(ROOT)),'parts':parts,'lucide_reference':ref}
 (W/'candidates.json').write_text(json.dumps(out,indent=2))
print('Authored',len(out),'variants')
