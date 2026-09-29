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
# Stage root owns mirrored drapes and a complete central standing figure.
# Curtain arcs meet the frame at true shared tie-back points.
self.add_polyline('frame',(14,42),(6,42),(6,26),(6,6),(16,6),(32,6),(42,6),(42,26),(42,42),(34,42))
path(self,'left-drape',(16,6),[('A',6,26,10,20,True),('A',14,42,8,16,True)])
path(self,'right-drape',(32,6),[('A',42,26,10,20,False),('A',34,42,8,16,False)])
self.relate('connect','frame','left-drape')
self.relate('connect','frame','right-drape')
circle(self,'head',24,16,4)
self.add_line('torso',(24,28),(24,35))
self.add_polyline('arms',(18,32),(24,28),(30,32))
self.add_polyline('legs',(20,42),(24,35),(28,42))
self.relate('connect','torso','arms')
self.relate('connect','torso','legs')
self.mark_human_figure('performer',head='head',torso='torso',torso_junction='start')
''','Curtain pleats and costume details omitted. The performer uses the shared stick-figure construction with an exact 4-unit detached head gap.')
spec(2,'SQUARE','''
# Two separate subjects: an upright person and a seated pointed-ear pet.
# Person: head bottom 14, neck 22, exact 8 centerline / 4 ink gap.
circle(self,'head',12,10,4)
self.add_line('torso',(12,22),(12,32))
self.add_polyline('arms',(6,28),(6,22),(12,22),(18,22),(18,28))
self.add_polyline('legs',(8,42),(12,32),(16,42))
self.relate('connect','torso','arms')
self.relate('connect','torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
# Pet head is an ear polygon with a circular jaw. Body joins at exact 3-4-5 circle points.
path(self,'pet-head',(28,26),[('L',28,18),('L',33,22),('L',38,18),('L',38,26),('A',36,30,5,5,True),('A',30,30,5,5,True),('A',28,26,5,5,True)],True)
path(self,'pet-body',(30,30),[('A',25,38,12,12,False),('L',25,42),('L',33,42),('L',42,42),('L',42,38),('A',36,30,12,12,False)])
self.add_line('pet-forelegs',(33,35),(33,42))
self.relate('connect','pet-head','pet-body')
self.relate('connect','pet-body','pet-forelegs')
''','Facial details and tail omitted as in the source. Pet ears, jaw, haunches and front-leg division remain.')
spec(3,'VRECT_L','''
# Frontal person: circular head and smooth shoulders frame a real arm sling.
# Head bottom 14; shoulder top 22 gives exactly 4 ink units of separation.
circle(self,'head',24,9,5)
path(self,'body-arm',(8,42),[('L',8,30),('A',16,22,8,8,True),('L',30,22),('L',32,22),('A',38,28,6,6,True),('L',40,33),('A',35,38,5,5,True),('L',20,38),('A',20,32,3,3,True),('L',30,32),('L',34,32)])
self.add_polyline('sling-strap',(30,22),(20,32),(30,32),(30,22))
self.add_polyline('left-torso',(20,38),(16,38),(16,44))
self.relate('connect','body-arm','left-torso')
self.add_line('right-torso',(32,38),(32,44))
self.relate('connect','body-arm','sling-strap')
self.relate('connect','body-arm','right-torso')
''','Lower legs and fine clothing seams omitted; triangular sling and the supported forearm retained.')
spec(4,'SQUARE','''
# Side-view writer with a continuous upright leg and a hand resting at the desk.
# Circular head bottom 12 and shoulder top 20 are exactly 8 apart on centerlines.
circle(self,'head',36,8,4)
path(self,'writer',(36,20),[('A',42,26,6,6,True),('L',42,41),('A',36,41,3,3,True),('L',36,29),('L',32,32),('L',24,32),('A',24,26,3,3,True),('L',30,26),('L',36,20)],True)
self.add_polyline('desk',(4,44),(4,34),(28,34),(28,44))
self.add_line('paper',(8,28),(18,28))
self.add_line('pen',(18,28),(24,18))
self.relate('connect','paper','pen')
''','Floating source document marks replaced by a paper stroke on the work surface. Upright leg and hand-to-pen relationship carry the action.')
spec(5,'VRECT_M','''
# Side-facing pregnant silhouette: belly projects left, one bent arm rests to the right.
# Head bottom 12; upper shoulder at y20 leaves exactly 4 ink units.
circle(self,'head',24,8,4)
path(self,'body',(24,20),[('L',22,20),('A',18,24,4,4,False),('L',18,27),('A',10,38,8,11,False),('L',18,38),('L',18,40),('A',26,40,4,4,False),('L',26,38),('L',31,38),('L',28,25),('L',24,20)],True)
self.add_polyline('arm',(24,20),(38,26),(34,34))
self.relate('connect','body','arm')
''','One visible leg follows the side-view source. Fine garment details omitted; rounded abdomen and bent arm preserved.')
spec(6,'SQUARE','''
# A ridged elongated whole fruit sits behind its five-lobed cross-section.
# Star points use coherent shallow arcs instead of a generic sharp badge.
path(self,'whole-fruit',(15,36),[('A',8,34,10,8,True),('A',32,6,25,25,True),('A',35,17,13,13,True)])
self.add_line('ridge',(8,34),(32,6))
self.relate('connect','whole-fruit','ridge')
path(self,'slice',(30,18),[('A',35,26,15,15,True),('A',44,28,17,17,True),('A',38,34,18,18,True),('A',39,44,19,19,True),('A',30,40,17,17,True),('A',21,44,17,17,True),('A',22,34,19,19,True),('A',16,28,18,18,True),('A',25,26,17,17,True),('A',30,18,15,15,True)],True)
self.add_dot('seed-core',(30,33))
''','Tiny five-line seed pattern reduced to one central seed mark. Asymmetry preserves the cut-fruit arrangement.')
spec(7,'SQUARE','''
# Leaning rider and stationary exercise-bike housing. Torso points toward the head via a 5-12-13 triangle.
# Head radius 5 and center-to-neck distance 13 prove exact 8 centerline / 4 ink clearance.
circle(self,'head',27,8,5)
self.add_line('torso',(22,20),(17,32))
self.add_polyline('arms',(22,20),(30,26),(40,24))
self.add_polyline('pedaling-leg',(17,32),(25,35),(21,39))
self.relate('connect','torso','arms')
self.relate('connect','torso','pedaling-leg')
self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
self.add_polyline('handle-support',(40,24),(43,23),(36,36))
path(self,'housing',(13,32),[('A',7,38,6,6,False),('A',13,44,6,6,False),('L',40,44),('A',44,40,4,4,False),('A',40,36,4,4,False),('L',36,36)])
self.relate('connect','handle-support','housing')

''','Rear leg and inner flywheel spokes omitted. Large housing and a planted base distinguish the stationary bike from a scooter.')

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
if __name__=='__main__': main([int(s) for s in sys.argv[1:]] or range(1,8))
