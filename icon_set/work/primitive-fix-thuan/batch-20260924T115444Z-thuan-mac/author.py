from pathlib import Path
import json,re,textwrap,sys,shutil
ROOT=Path.cwd();sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
AUTHOR='gpt-6'
SOURCE_ICON_ID=[re.search(r'[0-9a-f-]{36}$',next((Path(r)/'reference').glob('*.svg')).stem).group() for r in json.loads(Path(__file__).with_name('claims.json').read_text())]
SOURCE_PATH=[str(next((Path(r)/'reference').glob('*.svg'))) for r in json.loads(Path(__file__).with_name('claims.json').read_text())]
HELPERS='''
        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
'''
D={}
def design(i,key,notes,body,ref='No useful exact Lucide match; supplied reference controls the silhouette.',omissions='None'):
 D[i]=(key,notes,textwrap.dedent(body).strip(),ref,omissions)
design(0,'HRECT_L','Round the arched dial into its base and detach sparse dial marks from the rim. Retain circular needle hub and diagonal pointer.', '''
path('dial',(4,28),[('A',(24,8),20,20,True),('A',(44,28),20,20,True),('L',(44,34)),('A',(38,40),6,6,True),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,28))],True)
circle('hub',24,28,3)
line('needle',(27,28),(33,22));join('needle','hub')
self.add_dot('tick-top',(24,17));self.add_dot('tick-left',(13,25))
''','Lucide gauge: coherent circular dial and diagonal needle.','Reduce five fine ticks to two spaced marks.')
design(1,'SQUARE','Restore an upright broken rising path with tangent quarter-circle turns and a longer horizontal arrow shaft.', '''
path('lower',(6,42),[('L',(8,42)),('A',(16,34),8,8,False),('L',(16,31))])
path('upper',(16,22),[('L',(16,20)),('A',(24,12),8,8,True),('L',(25,12))])
line('terminal',(34,12),(42,12));poly('head',(36,6),(42,12),(36,18));join('terminal','head')
''','Lucide undo-2: tangent circular bends and 45-degree open arrowhead.')
design(2,'SQUARE','Restore a balanced dashed circular sweep and align the lower arrowhead with its counterclockwise tangent.', """
path('top',(12,10),[('C',(24,6),(16,7),(20,6))])
path('right',(38,12),[('C',(42,24),(41,16),(42,20))])
path('left',(7,18),[('C',(6,24),(6,20),(6,22)),('C',(7,30),(6,26),(6,28))])
path('bottom',(12,38),[('C',(24,42),(16,41),(20,42)),('C',(36,34),(30,42),(33,38))])
poly('head',(28,34),(36,34),(36,42));join('head','bottom')
""",'Lucide circle-dashed: spaced curved dashes; source counterclockwise arrow retained.','Nine tiny dashes reduced to four separated runs.')
design(3,'SQUARE','Restore the squash broad bulb, narrowed neck and a visible curved stem with smooth outline transitions.', '''
path('fruit',(18,42),[('C',(6,29),(11,42),(6,37)),('C',(20,17),(6,22),(14,21)),('C',(31,10),(25,13),(26,10)),('C',(42,19),(38,10),(42,12)),('C',(32,32),(42,24),(36,27)),('C',(18,42),(28,38),(27,42))],True)
path('stem',(31,10),[('C',(34,6),(34,10),(35,8))]);join('stem','fruit')
''')
WHEELS='''
for x in (12,36):circle(f'wheel-{x}',x,33,5)
line('sill',(17,33),(31,33));join('sill','wheel-12');join('sill','wheel-36')
join('body','wheel-12');join('body','wheel-36')
'''
design(4,'SQUARE','Restore a camper window and sloped windshield, rounded cabin corners and distinct equal circular wheels.', """
path('body',(10,38),[('A',(6,34),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(32,6)),('C',(36,11),(34,6),(35,8)),('L',(40,23)),('C',(42,28),(42,24),(42,25)),('L',(42,34)),('A',(38,38),4,4,True)])
for x in (14,34):circle(f'wheel-{x}',x,38,4);join('body',f'wheel-{x}')
line('sill',(18,38),(30,38));join('sill','wheel-14');join('sill','wheel-34')
poly('window',(15,15),(23,15),(23,23),(15,23),closed=True)
poly('windshield',(32,6),(32,23),(40,23));join('windshield','body')
""",'Lucide caravan/truck: rounded chassis and separate circular wheels.','Interior furnishing omitted.')
for i in [5,6,7,8]:
 design(i,'SQUARE','Replace flattened capsule shoulders with balanced rounded ends and tangent diagonal sidewalls; center the transverse seam.', '''
path('shell',(24,10),[('C',(31,6),(26,8),(28,6)),('C',(42,17),(37,6),(42,11)),('C',(38,24),(42,20),(40,22)),('L',(31,31)),('L',(24,38)),('C',(17,42),(22,40),(20,42)),('C',(6,31),(11,42),(6,37)),('C',(10,24),(6,28),(8,26)),('L',(17,17)),('L',(24,10))],True)
line('seam',(17,17),(31,31));join('seam','shell')
''','Lucide pill: parallel diagonal walls, smoothly rounded ends and perpendicular midpoint seam.')
for i in [9,11]:
 design(i,'HRECT_M','Broaden the cabin and lower the roof proportions; smooth the hood and trunk into a body with separate full circular wheels.', '''
path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,25)),('A',(8,21),4,4,True),('L',(10,21)),('L',(17,12)),('C',(21,10),(18,10),(19,10)),('L',(27,10)),('C',(31,12),(29,10),(30,11)),('L',(36,19)),('L',(40,20)),('C',(44,25),(43,21),(44,22)),('L',(44,30)),('A',(41,33),3,3,True)])
'''+WHEELS,'Lucide car: continuous roof/hood contour and separate round wheel outlines.')
design(10,'HRECT_M','Restore a wide divided window and smoothly rounded roof shoulders above two separate wheels.', '''
path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,25)),('A',(8,21),4,4,True),('L',(16,12)),('C',(20,10),(17,10),(18,10)),('L',(24,10)),('L',(28,10)),('C',(32,12),(30,10),(31,11)),('L',(40,21)),('A',(44,25),4,4,True),('L',(44,30)),('A',(41,33),3,3,True)])
poly('window-base',(8,21),(24,21),(40,21));join('window-base','body')
line('pillar',(24,10),(24,21));join('pillar','body');join('pillar','window-base')
'''+WHEELS,'Lucide car: rounded shoulder transitions and full wheels; source window division retained.')
design(12,'HRECT_M','Restore a flat-topped rounded cabin rather than a semicircle, and separate the circular wheels from the car body.', '''
path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,27)),('A',(12,19),8,8,True),('L',(24,19)),('L',(36,19)),('A',(44,27),8,8,True),('L',(44,30)),('A',(41,33),3,3,True)])
path('roof',(12,19),[('A',(21,10),9,9,True),('L',(24,10)),('L',(27,10)),('A',(36,19),9,9,True)])
line('pillar',(24,10),(24,19));join('roof','body');join('pillar','roof');join('pillar','body')
'''+WHEELS,'Lucide car: paired round wheels and coherent body; source rounded cabin.')
design(13,'HRECT_M','Restore equal circular wheels, soft cabin shoulders and rounded body corners for the side-view car.', '''
path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,27)),('A',(10,21),6,6,True),('L',(38,21)),('A',(44,27),6,6,True),('L',(44,30)),('A',(41,33),3,3,True)])
path('roof',(10,21),[('L',(17,12)),('C',(21,10),(18,10),(19,10)),('L',(27,10)),('C',(31,12),(29,10),(30,10)),('L',(38,21))]);join('roof','body')
'''+WHEELS,'Lucide car: shared wheel radius and smooth shell construction.')
design(14,'VRECT_L','Restore a front-view cabin, visible tire ends and two long smooth skidding tracks with equal spacing.', '''
path('body',(12,14),[('L',(14,14)),('L',(34,14)),('L',(36,14)),('A',(40,18),4,4,True),('L',(40,20)),('A',(36,24),4,4,True),('L',(12,24)),('A',(8,20),4,4,True),('L',(8,18)),('A',(12,14),4,4,True)],True)
path('cabin',(14,14),[('L',(17,6)),('C',(20,4),(18,4),(19,4)),('L',(28,4)),('C',(31,6),(29,4),(30,4)),('L',(34,14))]);join('cabin','body')
for x in (14,34):
 line(f'tire-{x}',(x,24),(x,27));join(f'tire-{x}','body')
for x in (16,32):
 path(f'track-{x}',(x,35),[('C',(x-3,39),(x-6,36),(x-6,38)),('C',(x,44),(x+4,41),(x+4,42))])
''','Lucide car-front: paired front body and tire ends; source wavy tracks retained.','Headlamps omitted as absent from source.')
design(15,'HRECT_M','Restore the broad van-like cabin, short door handle, lower hood and separate circular wheels.', '''
path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,21)),('L',(10,12)),('C',(14,10),(11,10),(12,10)),('L',(25,10)),('C',(29,12),(27,10),(28,11)),('L',(37,20)),('C',(44,25),(42,21),(44,21)),('L',(44,30)),('A',(41,33),3,3,True)])
line('handle',(18,21),(22,21))
'''+WHEELS,'Lucide car: simplified continuous roof/hood and rounded wheels.')
design(16,'HRECT_L','Round the cargo box and cab corners; restore complete wheels with clean shared axle-height attachments.', '''
path('body',(7,35),[('A',(4,32),3,3,True),('L',(4,12)),('A',(8,8),4,4,True),('L',(24,8)),('A',(28,12),4,4,True),('L',(28,17)),('L',(28,26)),('L',(28,35)),('L',(17,35))])
path('cab',(28,17),[('L',(33,17)),('C',(37,20),(35,17),(36,18)),('L',(40,26)),('A',(44,30),4,4,True),('L',(44,32)),('A',(41,35),3,3,True)])
line('cab-floor',(28,35),(31,35));line('window',(28,26),(40,26))
for x in (12,36):circle(f'wheel-{x}',x,35,5)
join('body','wheel-12');join('cab','wheel-36');join('body','cab');join('window','body');join('window','cab');join('cab-floor','body');join('cab-floor','wheel-36')
''','Lucide truck: round wheels, cargo/cab height contrast and sloped windshield.','Cargo lower stripe omitted for wheel clearance.')
design(17,'HRECT_L','Restore a broad rounded cargo body with a level base and full-sized equal wheels.', '''
path('body',(7,35),[('L',(4,35)),('L',(4,20)),('A',(16,8),12,12,True),('L',(32,8)),('A',(44,20),12,12,True),('L',(44,35)),('L',(41,35))])
for x in (12,36):circle(f'wheel-{x}',x,35,5);join('body',f'wheel-{x}')
line('sill',(17,35),(31,35));join('sill','wheel-12');join('sill','wheel-36')
''','Lucide caravan: rounded cargo roof and separate circular wheels.')
design(18,'SQUARE','Restore smooth curtain contours, clear radial clock hands and rounded seat backs; retain the cinema showtime composition.', '''
poly('top',(6,6),(10,6),(38,6),(42,6))
path('curtain-left',(10,6),[('C',(6,15),(10,11),(8,15)),('L',(6,26))])
path('curtain-right',(38,6),[('C',(42,15),(38,11),(40,15)),('L',(42,26))])
join('top','curtain-left');join('top','curtain-right')
circle('clock',24,23,7)
poly('hands',(24,16),(24,23),(27,23));join('hands','clock')
for x in (13,35):
 path(f'seat-{x}',(x-6,42),[('A',(x+6,42),6,6,True)])
''','Lucide theater: draped curtain contours and round-backed seats.','Three seat backs reduced to two; small curtain tie folds omitted.')
design(19,'SQUARE','Restore a larger companion circle and a narrow diagonal capsule with smoothly rounded ends.', '''
path('capsule',(23,6),[('C',(28,10),(25,6),(27,8)),('L',(40,30)),('C',(42,36),(41,32),(42,34)),('A',(36,42),6,6,True),('C',(31,38),(34,42),(32,40)),('L',(19,18)),('C',(17,12),(18,16),(17,14)),('A',(23,6),6,6,True)],True)
circle('companion',12,36,6)
''','Lucide pill: tangent capsule shoulders; source descending orientation and companion circle retained.')

if __name__=='__main__':
 runs=json.loads(Path(__file__).with_name('claims.json').read_text()); manifest=[]
 for i,r in enumerate(runs):
  fix=Path(r);item=json.loads((fix/'claim.json').read_text())['item'];ref=Path(SOURCE_PATH[i]);uuid=SOURCE_ICON_ID[i];concept=ref.stem[:-37];key,notes,body,construction,omissions=D[i]
  out=Path('icon_set/work/primitive-make-ray')/uuid/f'20260924T115444Z-thuan-mac-fix-{i:02}'
  out.mkdir(parents=True,exist_ok=True)
  meta={'concept':concept,'source_uuid':uuid,'reference_path':str(ref),'icon_id':item['icon_id'],'author':AUTHOR,'feedback':item['feedback']}
  (out/(item['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
  mod=out/(item['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  code=f'''"""{notes}\nConstruction: {construction}\nOmissions: {omissions}\nKeyshape {key}: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}
class Drawing(Solo48):
    icon_id = {item['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = {tuple(item['icon_id'].split('-'))!r}
    def build(self):
'''+HELPERS+'\n'+textwrap.indent(body,'        ')+'\n'
  mod.write_text(code)
  shutil.copyfile(ref,out/'reference.svg')
  import cairosvg
  cairosvg.svg2png(url=str(ref),write_to=str(out/'reference.png'),output_width=384,output_height=384,background_color='white')
  icon=load_icon(mod);report=icon.validate_icon();svg=icon.to_svg();(out/(item['icon_id']+'.svg')).write_text(svg)
  (out/'validation.txt').write_text(report.describe())
  render_previews(svg,item['icon_id'],48,out)
  print(i,item['icon_id'],report.describe(),flush=True)
  manifest.append({'i':i,'fix':str(fix),'out':str(out),'module':str(mod),'key':item['key'],'notes':notes,'construction':construction,'omissions':omissions})
 Path('icon_set/work/primitive-fix-thuan/batch-20260924T115444Z-thuan-mac/manifest.json').write_text(json.dumps(manifest,indent=2))
