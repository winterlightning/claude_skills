from audit import *
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.primitives import primitive_from_dict
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/human-repair-review/repairs.json'
AUTHOR='gpt-6'
repairs=json.loads((OUT/'repairs.json').read_text());outputs=[]
source={x['row']['icon_id']:x for x in rows}
for r in repairs:
 parent=load(source[r['icon_id']]);mod=importlib.import_module(type(parent).__module__)
 path,new_id,scaffold=prepare_variant(parent.icon_id,'solo','Correct human head and torso construction')
 sid=getattr(mod,'SOURCE_ICON_ID',None);sp=getattr(mod,'SOURCE_PATH',None)
 if sid:path=path.with_name(path.stem+'_'+sid.replace('-','_')+'.py')
 cls=next(n.name for n in ast.parse(scaffold).body if isinstance(n,ast.ClassDef) and any(isinstance(st,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in st.targets) and isinstance(st.value,ast.Constant) and st.value.value==new_id for st in n.body))
 record=r['after_record'];keyshape=record['keyshape'];keyshape={'HRECT_XL':'HRECT_L','HRECT_M':'HRECT_L','HRECT_S':'HRECT_L','VRECT_XL':'VRECT_L','VRECT_M':'VRECT_L','VRECT_S':'VRECT_L'}.get(keyshape,keyshape)
 prose='Human construction repair. '+ ' '.join(r['reasons'])+'\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
 lines=[repr(prose),'from ...keyshapes import Keyshape','from ._base import Solo48','',f'SOURCE_ICON_ID = {sid!r}',f'SOURCE_PATH = {sp!r}',f'AUTHOR = {AUTHOR!r}',f'HUMAN_CONSTRUCTION = {r["type"]!r}','',f'class {cls}(Solo48):',f'    icon_id = {new_id!r}',f'    variant_of = {parent.icon_id!r}',"    variant_label = 'Correct human head and torso construction'",f'    keyshape = Keyshape.{keyshape}',"    semantic_role = 'MAIN'","    semantic_kind = 'noun'",f'    category = {record["category"]!r}',f'    aliases = {tuple(record["aliases"])!r}',f'    keywords = {tuple(record["keywords"])!r}','','    def build(self):']
 for p in record['primitives']:
  id=p['element_id'];a=tuple(p['start']);b=tuple(p['end'])
  if p['kind']=='line':line=f'self.add_line({id!r}, {a!r}, {b!r})'
  elif p['kind']=='arc':line=f'self.add_arc({id!r}, {a!r}, {b!r}, radius_x={p["radius_x"]!r}, radius_y={p["radius_y"]!r}, large_arc={p["large_arc"]!r}, sweep={p["sweep"]!r})'
  else:line=f'self.add_bezier({id!r}, {a!r}, *{tuple(tuple(tuple(v) for v in seg) for seg in p["segments"])!r})'
  lines.append('        '+line)
 for c in record['contours']:lines.append(f'        self.add_contour({c["contour_id"]!r}, *{tuple(c["members"])!r}, closed={c["closed"]!r})')
 for rel in record['relationships']:lines.append(f'        self.relate({rel["kind"]!r}, *{tuple(rel["members"])!r})')
 for f in record.get('human_figures',[]):lines.append(f'        self.mark_human_figure({f["figure_id"]!r}, head={f["head"]!r}, torso={f["torso"]!r}, torso_junction={f["torso_junction"]!r})')
 text='\n'.join(lines)+'\n';compile(text,str(path),'exec')
 with path.open('x') as out:out.write(text)
 loaded=importlib.import_module('.'+path.stem,package='icon_set.model.icons.solo');i=getattr(loaded,cls)()
 # Only the title changes when assigning the variant ID; geometry must round-trip exactly.
 def paths(svg):
  import xml.etree.ElementTree as ET
  return [e.attrib['d'] for e in ET.fromstring(svg).iter() if e.tag.endswith('path')]
 assert paths(i.to_svg())==paths((OUT/'after'/f'{parent.icon_id}.svg').read_text())
 (OUT/'after'/f'{parent.icon_id}.svg').write_text(i.to_svg())
 outputs.append(dict(parent=parent.icon_id,icon_id=new_id,path=str(path.relative_to(ROOT)),source_icon_id=sid))
 print(new_id,flush=True)
 (OUT/'variants.json').write_text(json.dumps(outputs,indent=2))
