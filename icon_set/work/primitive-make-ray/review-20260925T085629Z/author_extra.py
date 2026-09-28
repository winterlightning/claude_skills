from pathlib import Path
import ast,json,shutil
ROOT=Path(__file__).resolve().parent
SOURCE_ICON_ID='per-input in extra-inputs.json'
SOURCE_PATH=str(ROOT/'extra-inputs.json')
AUTHOR='gpt-6'
# Reuse the authoring API helpers, without executing the earlier batch.
tree=ast.parse((ROOT/'author_batch.py').read_text())
HELPERS=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
NODE='''
    def node(self,name,x,y,r,d):
        # Four identical cubic quadrants; diagonal attachment points are explicit.
        quarter=[('C',(d,-d),(r//3,-r),(d,-r)),('C',(r,0),(r,-d),(r,-r//3))]
        def rot(p,i):
            a,b=p
            for _ in range(i): a,b=-b,a
            return (x+a,y+b)
        commands=[]
        for i in range(4):
            commands.extend((k,rot(e,i),rot(a,i),rot(b,i)) for k,e,a,b in quarter)
        self.path(name,(x,y-r),commands,True)
'''
PEN='''
        self.path('barrel',(22,26),[('L',(27,17)),('L',(32,8)),('C',(36,5),(33,6),(34,5)),('C',(40,9),(39,5),(40,6)),('C',(39,13),(40,10),(40,11)),('L',(34,22)),('L',(29,31)),('L',(22,26))],True)
        self.path('nib',(22,26),[('C',(18,40),(18,30),(18,34)),('C',(29,31),(27,36),(30,34)),('L',(22,26))],True)
        self.relate('connect','barrel','nib')
        self.path('writing',(4,42),[('C',(18,40),(10,36),(12,45))]);self.relate('connect','writing','nib')
'''
designs={
'fossil-tablet':('SQUARE','none (bone inspected; no useful skeleton match)','Restore the complete angular pterosaur skeleton with head, spine, spread limbs and tail inside a rounded stone tablet.', '''
        self.box('tablet',6,6,42,42,6)
        # Spine owns all branch nodes; deliberate asymmetry follows fossil pose.
        self.add_polyline('spine',(22,13),(18,19),(23,25),(28,29),(30,37))
        self.add_line('beak',(14,19),(18,19));self.relate('connect','beak','spine')
        self.add_polyline('upper-wing',(23,25),(30,21),(29,16),(34,14));self.relate('connect','upper-wing','spine')
        self.add_polyline('left-wing',(28,29),(21,32),(15,29),(13,36));self.relate('connect','left-wing','spine')
        self.add_polyline('right-leg',(30,37),(35,30),(38,32));self.relate('connect','right-leg','spine')
        self.add_line('tail',(30,37),(25,37));self.relate('connect','tail','spine');self.relate('connect','tail','right-leg')
'''),
'fountain-pen-drawing-a-stroke':('SQUARE','pen-line, pen-tool','Restore the side clip and barrel band; use a curved nib and smooth writing stroke.',PEN+'''
        self.add_line('band',(27,17),(34,22));self.relate('connect','band','barrel')
        self.path('clip',(32,8),[('C',(25,10),(28,6),(27,6)),('L',(19,21))]);self.relate('connect','clip','barrel')
'''),
'fountain-pen-writing':('SQUARE','pen-line, pen-tool','Restore the curved fountain nib and smooth writing flourish while keeping a clean rounded barrel.',PEN),
'four-node-molecular-diagram':('SQUARE','network','Restore a larger central atom and three smaller outer atoms, with straight bonds attached at explicit diagonal points.', '''
        self.node('center',24,25,6,4)
        for name,x,y in [('top',24,10),('left',10,38),('right',38,38)]:self.node(name,x,y,4,3)
        for name,a,b in [('top',(24,14),(24,19)),('left',(13,35),(20,29)),('right',(35,35),(28,29))]:
            self.add_line('bond-'+name,a,b);self.relate('connect','bond-'+name,name);self.relate('connect','bond-'+name,'center')
'''),
'four-node-network-hub':('SQUARE','network','Enlarge the four equal circular node openings and attach three radial links symmetrically to their edges.', '''
        self.node('center',24,24,4,3)
        for name,x,y in [('top',24,10),('left',10,38),('right',38,38)]:self.node(name,x,y,4,3)
        for name,a,b in [('top',(24,14),(24,20)),('left',(13,35),(21,27)),('right',(35,35),(27,27))]:
            self.add_line('link-'+name,a,b);self.relate('connect','link-'+name,name);self.relate('connect','link-'+name,'center')
'''),
'four-petal-stemmed-flower':('VRECT_L','flower-2','Restore the central flower disk, four equal rounded petals, two pointed leaves and a short visible stem below the leaf junction.', '''
        self.path('bloom',(18,10),[('A',(30,10),6,6,True),('A',(30,22),6,6,True),('A',(24,28),6,6,True),('A',(18,22),6,6,True),('A',(18,10),6,6,True)],True)
        self.circle('disk',24,16,3)
        self.add_polyline('stem',(24,28),(24,42),(24,44));self.relate('connect','stem','bloom')
        for name,sign in [('left',-1),('right',1)]:
            p=lambda x,y:(24+sign*x,y)
            self.path(name+'-leaf',(24,42),[('C',p(16,32),p(10,42),p(16,39)),('C',(24,42),p(7,32),p(2,36))],True)
            self.relate('connect',name+'-leaf','stem')
        self.relate('connect','left-leaf','right-leaf')
'''),
'four-toed-paw-print':('SQUARE','paw-print','Restore four oval toe pads and a broad softly lobed central pad, preserving bilateral symmetry.', '''
        for i,(x,y) in enumerate([(9,22),(17,10),(31,10),(39,22)]):
            self.path('toe-'+str(i),(x,y-5),[('A',(x,y+5),4,5,True),('A',(x,y-5),4,5,True)],True)
        self.path('pad',(24,24),[('C',(34,32),(30,24),(30,29)),('C',(32,44),(41,37),(40,44)),('C',(24,42),(28,44),(27,42)),('C',(16,44),(21,42),(20,44)),('C',(14,32),(8,44),(7,37)),('C',(24,24),(18,29),(18,24))],True)
''')}
rows=json.loads((ROOT/'extra-inputs.json').read_text())
for row in rows:
    ref=Path(row['reference']);uid=ref.stem[-36:];concept=ref.stem[:-37];icon_id=row['key'].split('/')[1]
    out=Path('icon_set/work/primitive-make-ray')/uid/'20260925T090617Z-thuan-redraw';out.mkdir(parents=True,exist_ok=False)
    (out/f'{icon_id}.metadata.json').write_text(json.dumps(dict(concept=concept,source_uuid=uid,reference_path=str(ref),icon_id=icon_id,author=AUTHOR),indent=2)+'\n')
    shutil.copyfile(ref,out/'reference.svg')
    key,lucide,plan,body=designs[icon_id]
    module=out/(icon_id.replace('-','_')+'_'+uid.replace('-','_')+'.py')
    module.write_text(f'''"""{plan}
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: {lucide}. Original reference establishes full subject and arrangement.
Keyshape {key}; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={uid!r}
SOURCE_PATH={str(ref)!r}
AUTHOR={AUTHOR!r}
class Drawing(Solo48):
    icon_id={icon_id!r}
    keyshape=Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(icon_id.split('-'))!r}
    def build(self):
{body}
{HELPERS}
{NODE if 'node' in icon_id else ''}
''')
    row.update(run=str(out),module=str(module),plan=plan,lucide=lucide)
(ROOT/'extra-runs.json').write_text(json.dumps(rows,indent=2)+'\n')
original=json.loads((ROOT/'runs.json').read_text());(ROOT/'runs.json').write_text(json.dumps(original+rows,indent=2)+'\n')
