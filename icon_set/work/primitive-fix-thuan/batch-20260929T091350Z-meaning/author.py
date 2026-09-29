from pathlib import Path
import json, textwrap, sys, datetime, shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
HELPERS='''
def path(icon, name, start, commands, closed=False):
    members=[]
    p=start
    for i,command in enumerate(commands):
        tag=f"{name}-{i}"
        q=(command[1],command[2])
        if command[0]=='L': icon.add_line(tag,p,q)
        else: icon.add_arc(tag,p,q,radius_x=command[3],radius_y=command[4],sweep=command[5])
        members.append(tag)
        p=q
    if closed and p != start:
        tag=f"{name}-close"
        icon.add_line(tag,p,start)
        members.append(tag)
    icon.add_contour(name,*members,closed=closed)

def circle(icon,name,cx,cy,r):
    path(icon,name,(cx-r,cy),[('A',cx+r,cy,r,r,True),('A',cx-r,cy,r,r,True)],True)

def rect(icon,name,x,y,w,h,r=2):
    path(icon,name,(x+r,y),[('L',x+w-r,y),('A',x+w,y+r,r,r,True),('L',x+w,y+h-r),('A',x+w-r,y+h,r,r,True),('L',x+r,y+h),('A',x,y+h-r,r,r,True),('L',x,y+r),('A',x+r,y,r,r,True)],True)

def bust(icon,name,cx,cy,r,half,base):
    # Detached circular head; shoulders start exactly 8 centerline units below its lower extent.
    circle(icon,name+'-head',cx,cy,r)
    top=cy+r+8
    path(icon,name+'-body',(cx-half,base),[('L',cx-half,top+half),('A',cx,top,half,half,True),('A',cx+half,top+half,half,half,True),('L',cx+half,base)])
'''
SPECS={}
def spec(n,keyshape,body,omissions='Fine reference detail omitted where it would not survive 48px.'):
 SPECS[n]=(keyshape,textwrap.dedent(body).strip(),omissions)

spec(1,'SQUARE','''
# Root owns one large cloud and three joined, differently roofed buildings.
path(self,'cloud',(10,19),[('A',10,11,4,4,True),('A',22,11,6,6,True),('A',22,19,4,4,True),('L',10,19)],True)
self.add_polyline('low-building',(6,42),(6,33),(16,33),(16,42))
self.add_polyline('house',(16,42),(16,31),(24,25),(32,31),(32,42))
self.add_polyline('tower',(32,42),(32,6),(42,6),(42,42),(6,42))
for y in (16,26): self.add_dot(f'window-{y}',(37,y))
self.add_line('house-window',(24,32),(24,35))
self.relate('connect','low-building','house')
self.relate('connect','house','tower')
self.relate('connect','low-building','tower')
''')
spec(2,'VRECT_L','''
# Three swept rotor blades and a narrow tapered support; asymmetric blade directions are intentional.
circle(self,'hub',24,19,3)
path(self,'blade-up',(22,16),[('L',23,4),('A',29,13,9,9,True),('L',27,17)])
path(self,'blade-left',(21,19),[('A',8,31,17,17,False),('L',19,25),('L',23,22)])
path(self,'blade-right',(27,19),[('L',40,27),('A',27,25,12,12,True),('L',25,22)])
self.add_polyline('mast',(22,27),(19,44),(29,44),(26,27))
self.add_line('ground',(8,44),(40,44))
self.relate('connect','mast','ground')
''')
spec(3,'HRECT_L','''
# Three cards fan about the lower area; front card owns the diamond suit.
self.add_polyline('back-card',(16,12),(4,17),(12,39),(17,37))
self.add_polyline('middle-card',(16,29),(16,8),(33,8),(33,12))
self.add_polyline('front-card',(27,13),(44,20),(35,40),(18,33),closed=True)
self.add_polyline('diamond',(31,23),(34,28),(29,31),(26,26),closed=True)
''','Tiny corner ranks omitted; three fanned cards and diamond suit retained.')
spec(4,'VRECT_L','''
# Three equal visual feather widths converge to a cork band; rounded tips replace the rejected straight rim.
path(self,'left-feather',(17,32),[('L',8,12),('A',18,10,6,6,True),('L',21,32)])
path(self,'middle-feather',(18,10),[('A',30,10,6,6,True),('L',27,32)])
path(self,'right-feather',(30,10),[('A',40,12,6,6,True),('L',31,32)])
path(self,'cork',(17,32),[('L',31,32),('L',31,37),('A',17,37,7,7,True),('L',17,32)],True)
for a,b in [('left-feather','middle-feather'),('middle-feather','right-feather'),('left-feather','cork'),('middle-feather','cork'),('right-feather','cork')]: self.relate('connect',a,b)
''','Individual feather barbs omitted; fan is upright for a more stable UI silhouette.')
spec(5,'SQUARE','''
# Flame instances share a teardrop construction; the central flame rises two units higher.
for i,cx in enumerate((10,24,38)):
    top=6 if i==1 else 8
    path(self,f'flame-{i}',(cx,top),[('L',cx+3,top+5),('A',cx-3,top+5,3,4,True),('L',cx,top)],True)
rect(self,'burner',6,24,36,10,3)
for x in (14,34):
    self.add_line(f'leg-{x}',(x,34),(x,42))
    self.relate('connect','burner',f'leg-{x}')
self.add_line('ground',(6,42),(42,42))
for x in (14,34): self.relate('connect',f'leg-{x}','ground')
''')
recycle='''
# Three broad clockwise ribbon arrows; separated returns preserve the central triangular opening.
self.add_polyline('top-arrow',(17,4),(25,4),(34,18),(38,16),(35,26),(25,24),(29,21),(21,10),(14,10),closed=True)
self.add_polyline('left-arrow',(15,17),(5,18),(9,21),(3,31),(6,35),(12,35),(10,32),(16,23),(20,25),closed=True)
self.add_polyline('bottom-arrow',(40,29),(44,35),(40,42),(24,42),(24,44),(17,38),(24,32),(24,36),(36,36),closed=True)
'''
spec(6,'SQUARE',recycle,'Small folded seam lines omitted; wide three-arrow recycling topology retained.')
spec(7,'SQUARE',recycle,'Small folded seam lines omitted; wide three-arrow recycling topology retained.')
spec(8,'SQUARE','''
# Square faceplate contains a round recess; two pin holes and flat-topped earth aperture identify type K.
rect(self,'faceplate',4,4,40,40,5)
circle(self,'socket',24,24,13)
for x in (19,29): self.add_dot(f'pin-{x}',(x,19))
path(self,'earth',(20,27),[('L',28,27),('A',20,27,4,4,True)],True)
''','Screw fixings omitted, matching the source.')
spec(9,'SQUARE','''
# Source uses genuine continuous necks, not detached heads. Three identical portrait outlines sit on an orthogonal chart.
for name,cx,cy in [('leader',24,8),('left',12,32),('right',36,32)]:
 path(self,name,(cx-3,cy+4),[('A',cx-4,cy,4,4,True),('A',cx+4,cy,4,4,True),('A',cx+3,cy+4,4,4,True),('L',cx+7,cy+8),('L',cx+7,cy+12),('L',cx-7,cy+12),('L',cx-7,cy+8),('L',cx-3,cy+4)],True)
self.add_line('trunk',(24,20),(24,24))
self.add_polyline('branch',(12,27),(12,24),(24,24),(36,24),(36,27))
self.relate('connect','trunk','branch')
self.relate('connect','trunk','leader')
''','Continuous anatomical necks follow the source; tiny facial features omitted.')
spec(10,'SQUARE','''
# Three complete torso silhouettes; shared side-person proportions flank a taller center person.
for name,cx,cy,r,half,base in [('center',24,10,5,6,44),('left',8,16,3,5,42),('right',40,16,3,5,42)]:
 circle(self,name+'-head',cx,cy,r)
 top=cy+r+8
 path(self,name+'-body',(cx-half,base),[('L',cx-half,top+half),('A',cx,top,half,half,True),('A',cx+half,top+half,half,half,True),('L',cx+half,base),('L',cx-half,base)],True)
''','Hands and feet simplified into three complete torso silhouettes; central figure is larger.')

spec(11,'HRECT_L','''
# Mouthpiece feeds upper tube and flared bell; three capped valve stems intersect the tubing loop.
self.add_line('mouthpiece',(4,20),(11,20))
self.add_line('mouthpiece-rim',(4,17),(4,23))
self.add_line('lead-pipe',(11,20),(32,20))
self.add_polyline('bell',(32,20),(44,8),(44,32),(32,20))
path(self,'tubing',(31,23),[('A',24,38,8,8,True),('L',16,38),('A',16,22,8,8,True),('L',31,22)])
for x in (14,22,30):
 self.add_line(f'valve-{x}',(x,11),(x,30))
 self.add_line(f'cap-{x}',(x-1,11),(x+1,11))
 self.relate('connect',f'valve-{x}',f'cap-{x}')
self.relate('connect','mouthpiece','mouthpiece-rim')
self.relate('connect','mouthpiece','lead-pipe')
self.relate('connect','lead-pipe','bell')
''','Minor tube joints omitted; flared bell, valve caps and loop retained.')
spec(12,'SQUARE','''
# A semicircular pastry shell is cut by a sloping sealed edge; crimp marks follow that edge.
path(self,'pastry',(6,40),[('A',42,31,19,27,True),('L',6,40)],True)
path(self,'filling-ridge',(15,30),[('A',33,28,10,8,True)])
for i,(x,y) in enumerate(((15,38),(24,36),(33,34))):
 self.add_line(f'crimp-{i}',(x,y),(x-1,y-3))
''','Many rim crimps reduced to three short marks.')
spouse='''
# Two circular heads share radius six. Front bust occludes the left edge of the rear bust.
circle(self,'front-head',15,12,6)
circle(self,'rear-head',35,12,6)
path(self,'front-body',(6,42),[('L',6,35),('A',15,26,9,9,True),('A',24,35,9,9,True),('L',24,42)])
path(self,'rear-body',(31,27),[('A',35,26,9,9,True),('A',42,33,7,7,True),('L',42,42)])
'''
spec(13,'SQUARE',spouse,'Bust bottoms left open in the shared user style; oval heads normalized to circular heads.')
spec(14,'SQUARE',spouse,'Bust bottoms left open in the shared user style; oval heads normalized to circular heads.')
spec(15,'SQUARE','''
# Back folder has a visible left side and top tab; front folder occludes its lower-right portion.
path(self,'rear',(6,33),[('L',6,8),('A',8,6,2,2,True),('L',17,6),('L',22,11),('L',35,11),('A',37,13,2,2,True),('L',37,16)])
path(self,'front',(17,42),[('A',15,40,2,2,True),('L',15,22),('A',17,20,2,2,True),('L',24,20),('L',29,25),('L',40,25),('A',42,27,2,2,True),('L',42,40),('A',40,42,2,2,True),('L',17,42)],True)
''','Hidden rear edges omitted by occlusion, not left as incomplete folders.')
spec(16,'SQUARE','''
# Each pattypan has a scalloped saucer silhouette and short stalk; foreground overlaps the rear fruit.
path(self,'rear',(20,23),[('L',19,17),('A',23,10,6,5,True),('A',31,9,7,4,True),('A',39,13,6,4,True),('A',42,21,5,5,True),('A',32,26,11,5,True)])
self.add_polyline('rear-stem',(31,9),(34,4),(37,5))
path(self,'front',(6,30),[('A',12,24,8,6,True),('A',20,24,6,4,True),('A',28,28,7,4,True),('A',31,35,5,5,True),('A',22,42,12,7,True),('A',10,38,12,7,True),('A',6,30,6,6,True)],True)
self.add_polyline('front-stem',(13,23),(14,18),(17,17))
path(self,'front-rib',(23,30),[('A',20,37,12,12,True)])
path(self,'rear-rib',(34,14),[('A',33,19,9,9,True)])
''','Fine organic ribbing reduced to one curved rib per fruit.')
spec(17,'HRECT_L','''
# Two equal riders share circular heads and seated shoulders; shell has a rounded nose and lower runner.
for i,cx in enumerate((14,29)):
 circle(self,f'rider-{i}-head',cx,10,4)
 path(self,f'rider-{i}-body',(cx-5,26),[('A',cx,22,5,4,True),('A',cx+5,26,5,4,True)])
path(self,'shell',(6,27),[('L',32,27),('A',44,35,12,8,True),('A',38,38,6,3,True),('L',13,38),('A',6,27,7,11,True)],True)
self.add_polyline('runner',(4,44),(38,44),(44,41))
for x in (15,33): self.add_line(f'strut-{x}',(x,38),(x,44))
''','Hands and feet remain concealed by the shell as in the reference.')
spec(18,'SQUARE','''
# Centered ring suspends two skulls. Each skull owns its dome, squared jaw, paired eyes and tooth notch.
circle(self,'loop',24,7,3)
self.add_line('left-cord',(22,10),(15,18))
self.add_line('right-cord',(26,10),(34,18))
for name,cx,cy in [('left',14,27),('right',35,29)]:
 path(self,name+'-skull',(cx-8,cy),[('A',cx+8,cy,8,9,True),('L',cx+8,cy+5),('L',cx+5,cy+7),('L',cx+5,cy+13),('L',cx-5,cy+13),('L',cx-5,cy+7),('L',cx-8,cy+5),('L',cx-8,cy)],True)
 for dx in (-3,3): self.add_dot(name+f'-eye-{dx}',(cx+dx,cy+1))
 self.add_line(name+'-teeth',(cx,cy+10),(cx,cy+13))
 self.relate('connect',name+'-skull',name+'-teeth')
''','Nasal cavity and extra tooth divisions omitted to keep the sockets readable.')
spec(19,'HRECT_L','''
# Mirrored molars have two rounded roots; archwire passes through square brackets.
for name,cx in [('left',13),('right',35)]:
 path(self,name+'-tooth',(cx-8,17),[('A',cx-4,10,5,7,True),('A',cx+4,10,5,4,False),('A',cx+8,17,5,7,True),('L',cx+6,34),('A',cx+2,34,2,3,True),('L',cx+1,29),('A',cx-1,29,1,2,False),('L',cx-2,34),('A',cx-6,34,2,3,True),('L',cx-8,17)],True)
 self.add_polyline(name+'-bracket',(cx-3,19),(cx+3,19),(cx+3,25),(cx-3,25),closed=True)
self.add_line('wire-left',(4,22),(10,22))
self.add_line('wire-middle',(16,22),(32,22))
self.add_line('wire-right',(38,22),(44,22))
''','Gumline and extra band hardware omitted; two roots per tooth and square brackets retained.')
spec(20,'HRECT_L','''
# Two towers support a broad sagging central cable and a straight deck. Quarter ellipses meet tangentially at the sag.
for x in (12,36): self.add_line(f'tower-{x}',(x,6),(x,36))
path(self,'cable',(4,26),[('A',12,10,22,22,False),('A',24,24,12,14,False),('A',36,10,12,14,False),('A',44,26,22,22,False)])
self.add_line('deck',(4,28),(44,28))
self.add_line('central-suspender',(24,24),(24,28))
self.relate('connect','central-suspender','cable')
self.relate('connect','central-suspender','deck')
path(self,'water',(4,42),[('A',14,42,7,4,False),('A',24,42,7,4,True),('A',34,42,7,4,False),('A',44,42,7,4,True)])
''','Water reduced to one wave and hangers to the central suspender to preserve open cable spans.')

def main(indices):
 rows=json.loads((BATCH/'items.json').read_text())
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
 for n in indices:
  row=rows[n-1]; ref=Path(row['reference']); uid=ref.stem[-36:]; concept=ref.stem[:-37]
  run=Path('icon_set/work/primitive-make-ray')/uid/f'{stamp}-meaning-{n:02}'
  run.mkdir(parents=True)
  meta=dict(concept=concept,source_uuid=uid,reference_path=str(ref),icon_id=row['icon_id'],author=AUTHOR)
  (run/(row['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  shape,body,omissions=SPECS[n]
  source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}
# Reference comparison: {row['comparison']}
# Revision: {row['change']}
# Construction references inspected: {row['construction_references']}
{HELPERS}
class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{shape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(concept.split())!r}
    def build(self):
{textwrap.indent(body,'        ')}
'''
  module=run/(row['icon_id'].replace('-','_')+'_'+uid.replace('-','_')+'.py')
  module.write_text(source)
  shutil.copy(ref,run/'reference.svg')
  icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
  (run/(row['icon_id']+'.svg')).write_text(svg)
  render_previews(svg,row['icon_id'],48,run)
  (run/'validation.txt').write_text(report.describe())
  row.update(run=str(run),module=str(module),keyshape=shape,omissions=omissions)
  (BATCH/'items.json').write_text(json.dumps(rows,indent=2))
  print(n,row['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
if __name__=='__main__': main([int(s) for s in sys.argv[1:]] or range(1,21))
