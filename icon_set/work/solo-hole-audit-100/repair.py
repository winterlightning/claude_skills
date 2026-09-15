from pathlib import Path
import sys,ast,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-failed-batch-100/review-decisions.json'
AUTHOR='gpt-6'
changes={
'brick-firewall-v2':[("(28, 20)","(28, 16)")],
'crouching-mouse':[("self.add_bezier('chin', (44, 32), ((44, 36), (41, 38), (37, 38)))","self.add_bezier('chin', (44, 32), ((44, 37), (41, 40), (37, 40)))"),("self.add_line('belly', (37, 38), (14, 38))","self.add_line('belly', (37, 40), (18, 40))"),("self.add_bezier('back', (14, 38), ((7, 38), (6, 33), (9, 27)), ((12, 20), (18, 16), (25, 14)))","self.add_bezier('back', (18, 40), ((15, 40), (14, 36), (14, 32)), ((14, 24), (19, 18), (25, 14)))"),("self.add_bezier('tail', (9, 27), ((5, 29), (4, 32), (4, 35)), ((4, 38), (7, 40), (11, 40)))","self.add_bezier('tail', (18, 40), ((4, 40), (4, 35), (4, 29)))")]
}
rows=[]
for ident,edits in changes.items():
 p,new,text=prepare_variant(ident,'solo','Open flame counter' if ident.startswith('brick') else 'Clear curled tail')
 for a,b in edits:
  assert a in text,(ident,a);text=text.replace(a,b)
 tree=ast.parse(text);sid=next(n.value.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_ICON_ID' for t in n.targets))
 p=p.with_name(p.stem+'_'+sid.replace('-','_')+'.py');p.write_text(text)
 rows.append(dict(parent=ident,icon_id=new,file=str(p.relative_to(ROOT))))
Path(__file__).with_name('repairs.json').write_text(json.dumps(rows,indent=2))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
for row in rows:
 q=inspect_icon(create(row['icon_id']));print(row['icon_id'],q['status'],q['errors'],q['warnings']);print('holes',[(h['inscribed_radius_design_u'],h['center_viewbox']) for h in q['negative_space']['authored_holes']])
