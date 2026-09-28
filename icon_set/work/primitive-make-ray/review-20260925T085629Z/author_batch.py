from pathlib import Path
import json, re, shutil

ROOT = Path(__file__).resolve().parent
SOURCE_ICON_ID = 'per-input in inputs.json'
SOURCE_PATH = str(ROOT / 'inputs.json')
AUTHOR = 'gpt-6'

HELPERS = '''
    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
'''

designs={
'dashboard-gauge':('HRECT_L','gauge','Restore five scale marks and an open needle hub; smooth symmetric dial.', '''
        self.path('dial',(8,40),[('C',(4,28),(5,36),(4,32)),('C',(10,14),(4,22),(6,18)),('C',(24,8),(14,10),(18,8)),('C',(38,14),(30,8),(34,10)),('C',(44,28),(42,18),(44,22)),('C',(40,40),(44,32),(43,36)),('L',(8,40))],True)
        for name,a,b in [('left',(4,28),(8,28)),('upper-left',(10,14),(13,17)),('top',(24,8),(24,12)),('upper-right',(38,14),(35,17)),('right',(44,28),(40,28))]:
            self.add_line(name,a,b);self.relate('connect',name,'dial')
        self.circle('hub',24,29,3)
        self.add_line('needle',(24,26),(31,19));self.relate('connect','needle','hub')
'''),
'devilish-heart':('SQUARE','heart','Restore curved crescent horns and a clear hooked arrow tail around a balanced heart.', '''
        self.path('heart',(21,19),[('C',(12,16),(18,15),(15,14)),('C',(7,23),(8,17),(7,19)),('C',(21,35),(7,28),(15,32)),('C',(30,28),(25,32),(28,30)),('C',(35,23),(33,26),(35,25)),('C',(30,16),(35,19),(34,17)),('C',(21,19),(27,14),(24,15))],True)
        self.path('horn-left',(12,16),[('C',(6,6),(8,13),(6,10)),('C',(7,23),(5,14),(5,19))]);self.relate('connect','horn-left','heart')
        self.path('horn-right',(30,16),[('C',(36,6),(34,13),(36,10)),('C',(35,23),(37,14),(37,19))]);self.relate('connect','horn-right','heart')
        self.path('tail',(30,28),[('L',(36,28)),('A',(42,34),6,6,True),('A',(36,40),6,6,True),('L',(27,40))]);self.relate('connect','tail','heart')
        self.add_polyline('arrow',(30,36),(25,40),(30,44));self.relate('connect','arrow','tail')
'''),
'diagonal-butternut-squash':('SQUARE','none','Rebuild a round bulb, softly tapering neck and short curved outlined stem.', '''
        self.path('squash',(28,12),[('C',(36,12),(30,9),(34,9)),('C',(36,22),(40,15),(39,19)),('C',(28,35),(32,27),(31,31)),('C',(18,42),(26,40),(23,42)),('C',(6,30),(11,42),(6,37)),('C',(13,20),(6,25),(9,22)),('C',(28,12),(19,17),(24,16))],True)
        self.path('stem',(28,12),[('C',(34,6),(29,8),(31,6)),('C',(40,12),(38,6),(42,8)),('L',(38,16))]);self.relate('connect','stem','squash')
'''),
'diagonal-double-ended-wrench':('SQUARE','wrench','Restore the solid outlined handle and opposed crescent jaws with half-turn symmetry.', '''
        # A half-turn defines both jaw and handle sides from one source contour.
        half=[('C',(23,17),(22,4),(24,11)),('L',(31,25)),('C',(42,38),(39,23),(44,30)),('L',(35,31)),('C',(31,35),(32,30),(30,32)),('L',(38,42))]
        commands=half+[(k,(48-e[0],48-e[1]),*((48-p[0],48-p[1]) for p in args)) for k,e,*args in half]
        self.path('wrench',(10,6),commands,True)
'''),
'diagonal-eyedropper-with-long-collar':('SQUARE','pipette','Restore a tapered nozzle and smoothly rounded bulb, keeping a clear projecting collar.', '''
        self.path('outline',(6,42),[('L',(10,36)),('C',(12,29),(9,33),(10,31)),('L',(30,11)),('L',(34,7)),('C',(41,7),(36,5),(39,5)),('C',(41,14),(43,9),(43,12)),('L',(37,18)),('L',(19,36)),('C',(12,38),(17,38),(15,39)),('L',(6,42))],True)
        self.add_polyline('collar',(25,8),(30,13),(35,18),(40,23));self.relate('connect','collar','outline')
'''),
'diagonal-oval-coffee-bean':('VRECT_L','bean','Replace the pointed leaf silhouette with a smooth full oval and flowing diagonal seam.', '''
        self.path('bean',(31,4),[('C',(40,16),(37,4),(40,9)),('C',(17,44),(40,30),(29,44)),('C',(8,32),(11,44),(8,39)),('C',(31,4),(8,18),(19,4))],True)
        self.path('seam',(31,4),[('C',(24,24),(29,11),(29,18)),('C',(17,44),(19,30),(19,37))]);self.relate('connect','seam','bean')
'''),
'diagonal-paintbrush-with-curved-bristles':('SQUARE','paintbrush','Round the handle tip, taper the neck and make the bristle tuft flow smoothly into its pointed tip.', '''
        self.path('outline',(6,42),[('C',(12,28),(10,39),(10,31)),('C',(20,25),(14,23),(17,23)),('L',(35,8)),('C',(41,7),(37,6),(39,5)),('C',(41,13),(43,9),(43,11)),('L',(25,30)),('C',(6,42),(29,39),(18,44))],True)
        self.add_line('joint',(20,25),(25,30));self.relate('connect','joint','outline')
'''),
'diagonal-paintbrush-with-ferrule-band':('SQUARE','paintbrush','Restore a tapered rounded handle with a distinct broad ferrule and flowing bristle tuft.', '''
        self.path('outline',(6,42),[('C',(12,28),(10,39),(10,31)),('C',(20,25),(14,23),(17,23)),('L',(25,19)),('L',(35,8)),('C',(41,7),(37,6),(39,5)),('C',(41,13),(43,9),(43,11)),('L',(30,24)),('L',(25,30)),('C',(6,42),(29,39),(18,44))],True)
        self.add_line('joint',(20,25),(25,30));self.relate('connect','joint','outline')
        self.add_line('ferrule',(25,19),(30,24));self.relate('connect','ferrule','outline')
'''),
'diagonal-side-handle-nightstick':('VRECT_M','none','Restore the shallow diagonal baton and rounded outlined perpendicular side grip.', '''
        self.path('baton',(28,8),[('C',(34,4),(29,5),(31,4)),('C',(38,10),(37,4),(39,7)),('L',(29,39)),('C',(23,44),(28,42),(26,44)),('C',(19,38),(20,44),(18,41)),('L',(22,28)),('L',(24,22)),('L',(28,8))],True)
        self.path('grip',(24,22),[('L',(14,19)),('C',(12,25),(9,18),(8,24)),('L',(22,28))]);self.relate('connect','grip','baton')
'''),
'dice':('SQUARE','dice-1','Use consistent six-unit corner radii and enlarge the outlined central pip so it reads as a circle.', '''
        self.box('die',6,6,42,42,6)
        self.circle('pip',24,24,4)
'''),
'dining-plate-fork':('HRECT_L','utensils','Restore all three fork tines with equal spacing, rounded shoulders and a separate round plate.', '''
        self.circle('plate',14,24,10)
        self.path('fork',(32,8),[('L',(32,20)),('A',(38,26),6,6,False),('A',(44,20),6,6,False),('L',(44,8))])
        self.add_polyline('middle-handle',(38,8),(38,26),(38,40));self.relate('connect','middle-handle','fork')
'''),
'dining-table-chairs-flower-vase':('SQUARE','sprout','Restore two table legs, recognizable chair seats and a tapering vase with three flower heads.', '''
        self.add_polyline('table',(13,30),(18,30),(20,30),(28,30),(30,30),(35,30))
        for name,x in [('left',18),('right',30)]:
            self.add_line(name+'-leg',(x,30),(x,42));self.relate('connect',name+'-leg','table')
        for name,x,s in [('left',6,1),('right',42,-1)]:
            self.path(name+'-chair',(x,24),[('C',(x+2*s,30),(x+2*s,24),(x+2*s,27)),('L',(x+2*s,37)),('L',(x+2*s,42))])
            self.add_polyline(name+'-seat',(x+2*s,37),(x+7*s,37),(x+7*s,42));self.relate('connect',name+'-seat',name+'-chair')
        self.add_polyline('vase',(20,30),(21,22),(27,22),(28,30));self.relate('connect','vase','table')
        self.path('stem-left',(24,22),[('C',(15,12),(23,15),(18,18))]);self.relate('connect','stem-left','vase')
        self.path('stem-right',(24,22),[('C',(33,9),(25,13),(30,16))]);self.relate('connect','stem-right','vase');self.relate('connect','stem-left','stem-right')
        self.circle('flower-left',15,9,3);self.relate('connect','flower-left','stem-left')
        self.circle('flower-top',33,6,3);self.relate('connect','flower-top','stem-right')
        self.circle('flower-right',36,17,2)
        self.add_line('branch',(24,22),(34,17));self.relate('connect','branch','stem-left');self.relate('connect','branch','stem-right');self.relate('connect','branch','vase');self.relate('connect','branch','flower-right')
'''),
'dragonfly':('VRECT_L','none','Restore a larger oval head, four slender smooth wings and a long tail; derive wings by reflection.', '''
        self.path('head',(24,4),[('A',(24,12),6,4,True),('A',(24,4),6,4,True)],True)
        self.add_polyline('body',(24,12),(24,22),(24,28),(24,44));self.relate('connect','body','head')
        for name,sign in [('left',-1),('right',1)]:
            p=lambda x,y:(24+sign*x,y)
            self.path(name+'-upper',(24,22),[('C',p(11,16),p(4,17),p(7,16)),('C',p(16,20),p(14,16),p(16,17)),('C',(24,22),p(16,26),p(5,26))],True)
            self.path(name+'-lower',(24,28),[('C',p(13,27),p(6,27),p(10,25)),('C',p(16,32),p(15,28),p(16,30)),('C',(24,28),p(16,39),p(3,37))],True)
            self.relate('connect','body',name+'-upper');self.relate('connect','body',name+'-lower')
        self.relate('connect','left-upper','right-upper');self.relate('connect','left-lower','right-lower')
''')}

rows=json.loads((ROOT/'inputs.json').read_text())
for row in rows:
    ref=Path(row['reference']); uid=ref.stem[-36:]; concept=ref.stem[:-37]
    icon_id=row['key'].split('/',1)[1]
    out=Path('icon_set/work/primitive-make-ray')/uid/'20260925T085629Z-thuan-redraw'
    out.mkdir(parents=True,exist_ok=False)
    metadata={'concept':concept,'source_uuid':uid,'reference_path':str(ref),'icon_id':icon_id,'author':AUTHOR}
    (out/f'{icon_id}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    shutil.copyfile(ref,out/'reference.svg')
    key,reference,plan,body=designs[icon_id]
    module=out/(icon_id.replace('-','_')+'_'+uid.replace('-','_')+'.py')
    text=f'''"""{plan}
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: {reference}. Original source establishes full subject and arrangement.
Keyshape: {key}; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(icon_id.split('-'))!r}
    def build(self):
{body}
{HELPERS}
'''
    module.write_text(text)
    row.update(run=str(out),module=str(module),plan=plan,lucide=reference)
(ROOT/'runs.json').write_text(json.dumps(rows,indent=2)+'\n')
