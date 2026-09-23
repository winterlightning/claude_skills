from pathlib import Path
import json, textwrap, importlib.util, cairosvg
SOURCE_ICON_ID='8e9b7bc2-90cb-457c-b184-e60fb8d06b7b'
SOURCE_PATH='icon_set/work/todo-references/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
items=json.loads((ROOT/'batch-inputs.json').read_text())
HELPERS='''
    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, x, y, right, bottom, r=3):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r),(x+r,y)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            part=f'{name}-{i}'
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,r):
        for suffix,p in [('left',(cx-r,cy)),('right',(cx+r,cy)),('top',(cx,cy-r)),('bottom',(cx,cy+r))]:
            self.add_line(name+'-'+suffix,p,(cx,cy))
        self.relate('connect',*[name+'-'+s for s in ('left','right','top','bottom')])

    def clipboard(self):
        self.box('clip',17,4,31,12,4)
        self.add_polyline('board',(17,8),(8,8),(8,44),(40,44),(40,8),(31,8))
        self.relate('connect','clip','board')
'''
designs=[]
def add(key,plan,body,ref='file-text',omissions='None; details recomposed for SOLO48.'):
 designs.append((key,plan,textwrap.dedent(body),ref,omissions))
add('SQUARE','Two repeated front-facing cars below a central lightning bolt; shared car dimensions preserve equality.', '''
for i,x in enumerate((6,30)):
    self.add_polyline(f'car-{i}',(x,38),(x,32),(x+3,26),(x+9,26),(x+12,32),(x+12,38),closed=True)
    for j,dx in enumerate((0,12)):
        self.add_line(f'wheel-{i}-{j}',(x+dx,38),(x+dx,42))
        self.relate('connect',f'car-{i}',f'wheel-{i}-{j}')
self.add_polyline('lightning',(26,6),(18,16),(25,16),(22,22),(32,12),(25,12),closed=True)
self.add_polyline('noise-left',(6,14),(8,18),(10,14))
self.add_polyline('noise-right',(40,8),(42,12),(40,16))
''','car-front','Rounded wheel lobes reduced to round-ended wheel stems; both cars and three noise marks retained.')
for name in ['note 1','note dollar sign','note']:
 body='self.clipboard()\n'
 if name=='note dollar sign':body+='''self.add_bezier('dollar', (29,22), ((19,16),(17,27),(24,28)), ((33,29),(29,38),(19,34)))
self.add_line('dollar-stem-top',(24,17),(24,20))
self.add_line('dollar-stem-bottom',(24,36),(24,39))
# Dollar stems remain detached; no contact waiver.

'''
 add('VRECT_L','Upright clipboard with centered capsule clip and open board wall behind it.',body,'clipboard')
add('SQUARE','Square note block with three equally spaced top binding strokes.', '''
self.add_polyline('page',(6,18),(6,42),(42,42),(42,18),(42,14),(6,14),(6,18))
for i,x in enumerate((14,24,34)):
    self.add_line(f'ring-{i}',(x,6),(x,22))
    self.relate('connect','page',f'ring-{i}')
''','notebook-pen')
add('VRECT_L','Flip checklist: page frame, top separator, check and short writing runs.', '''
self.box('page',8,4,40,44,4)
self.add_line('flip-rule',(8,14),(40,14))
self.relate('connect','page','flip-rule')
self.add_polyline('check',(17,24),(20,27),(23,22))
self.add_dot('entry',(31,25))
for i,(a,b) in enumerate(((17,23),(31,31))):self.add_line(f'row-{i}',(a,35),(b,35))
''','file-text')
add('SQUARE','Rounded medical note enclosure surrounding an equal-arm outlined medical cross.', '''
self.box('page',6,6,42,42,4)
c=24;outer=9;inner=4
self.add_polyline('medical-cross',(c-inner,c-outer),(c+inner,c-outer),(c+inner,c-inner),(c+outer,c-inner),(c+outer,c+inner),(c+inner,c+inner),(c+inner,c+outer),(c-inner,c+outer),(c-inner,c+inner),(c-outer,c+inner),(c-outer,c-inner),(c-inner,c-inner),closed=True)
''','file-text')
add('VRECT_L','Upright text page with folded upper-right corner and two writing rules.', '''
self.add_polyline('page',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)
self.add_polyline('fold',(28,4),(28,16),(40,16))
self.relate('connect','page','fold')
for i,(y,end) in enumerate(((25,30),(35,26))):self.add_line(f'text-{i}',(17,y),(end,y))
''','file-text','Three text rows reduced to two to preserve readable spacing.')
add('VRECT_L','Text page with lower-right dog-ear; two text lines above the fold.', '''
self.add_polyline('page',(8,4),(40,4),(40,32),(28,44),(8,44),closed=True)
self.add_polyline('fold',(28,44),(28,32),(40,32))
self.relate('connect','page','fold')
for i,(y,end) in enumerate(((14,31),(23,26))):self.add_line(f'text-{i}',(17,y),(end,y))
''','file-text','Three text rows reduced to two to preserve readable spacing.')
add('VRECT_L','Top-bound spiral notebook with three repeated open loops and two writing rules.', '''
self.box('page',8,12,40,44,3)
for i,x in enumerate((14,24,34)):
    self.add_arc(f'loop-{i}-top',(x-3,7),(x+3,7),radius_x=3)
    self.add_line(f'loop-{i}-side',(x+3,7),(x+3,16))
    self.add_contour(f'loop-{i}',f'loop-{i}-top',f'loop-{i}-side')
    self.relate('connect','page',f'loop-{i}')
for i,(y,end) in enumerate(((25,31),(35,27))):self.add_line(f'text-{i}',(17,y),(end,y))
''','notebook-pen','Three text rows reduced to two; loop returns simplified.')
add('VRECT_M','Single tall oval zero centered on the vertical axis.',"self.oval('zero',24,24,14,20)",None)
add('VRECT_L','Nun portrait with circular jaw, arched veil, broad shoulders and chest cross. Human reference owns head and shoulder proportions.', '''
self.add_arc('veil-top',(13,16),(35,16),radius_x=11,radius_y=12)
self.add_polyline('veil-left',(35,16),(40,38),(40,44),(8,44),(8,38),(13,16))
self.contours.pop()
self.add_contour('veil','veil-top',*[f'veil-left-{i}' for i in range(1,6)],closed=True)
self.add_arc('jaw',(17,16),(31,16),radius_x=7,sweep=False)
self.add_line('brow',(31,16),(17,16))
self.add_contour('face','jaw','brow',closed=True)
self.add_arc('shoulders',(8,39),(40,39),radius_x=16,radius_y=8)
self.relate('connect','veil','shoulders')
self.cross('cross',24,36,4)
''',None,'Neck collar and inner headwear seam omitted to limit crowding; veil, face, shoulders and cross retained.')
add('CIRCLE','Circular exclude symbol split at four diagonal attachment nodes, with crossing diagonals sharing the center.', '''
points=[(12,8),(40,12),(36,40),(8,36)]
for i in range(4):
    self.add_arc(f'rim-{i}',points[i],points[(i+1)%4],radius_x=20)
    self.add_line(f'spoke-{i}',points[i],(24,24))
    self.relate('connect',f'rim-{i}',f'spoke-{i}')
    self.relate('connect',f'rim-{(i-1)%4}',f'spoke-{i}')
self.add_contour('rim',*[f'rim-{i}' for i in range(4)],closed=True)
self.relate('connect',*[f'spoke-{i}' for i in range(4)])
''',None)
add('SQUARE','Rounded square containing an off-center circular subtraction region.', '''
self.box('square',6,6,42,42,3)
self.oval('cutout',26,26,7)
''',None)
add('VRECT_L','Left-facing head silhouette with repeated checklist symbols inside; intentional facial asymmetry preserves profile.', '''
self.add_bezier('cranium',(8,19),((8,9),(14,4),(24,4)),((34,4),(40,12),(40,20)),((40,27),(35,29),(35,36)))
self.add_polyline('face',(35,36),(35,44),(18,44),(18,36),(10,36),(10,27),(8,27),(8,19))
self.contours.pop()
self.add_contour('head','cranium',*[f'face-{i}' for i in range(1,8)],closed=True)
for i,y in enumerate((14,24)):
    self.add_polyline(f'check-{i}',(16,y),(18,y+2),(21,y-2))
    self.add_line(f'text-{i}',(29,y),(32,y))
self.add_polyline('empty-box',(24,33),(29,33),(29,38),(24,38),closed=True)
''',None,'Final checklist writing run omitted to keep the neck readable.')
add('SQUARE','Regular-looking octagon with equal paired diagonal cuts about both axes.', '''
x0,x1=6,42;cut=11
self.add_polyline('octagon',(x0+cut,x0),(x1-cut,x0),(x1,x0+cut),(x1,x1-cut),(x1-cut,x1),(x0+cut,x1),(x0,x1-cut),(x0,x0+cut),closed=True)
''','octagon')
add('SQUARE','Office workstation: monitor left, clock right, desk across bottom and two legs.', '''
self.box('monitor',6,8,26,24,2)
self.add_line('stand',(16,24),(16,32));self.relate('connect','monitor','stand')
self.oval('clock',36,12,6)
self.add_polyline('hands',(36,8),(36,12),(39,12))
self.add_polyline('desk',(6,32),(42,32),(40,36),(8,36),closed=True)
self.relate('connect','stand','desk')
for i,(x,end) in enumerate(((10,6),(38,42))):
    self.add_line(f'leg-{i}',(x,36),(end,42));self.relate('connect','desk',f'leg-{i}')
self.add_line('cup',(36,24),(36,32));self.relate('connect','cup','desk')
''','laptop','Monitor bezel and cup width reduced to simple strokes.')
add('SQUARE','Open document contour and diagonal signing pencil with pointed nib.', '''
self.add_polyline('page',(42,29),(42,42),(6,42),(6,6),(26,6))
self.add_polyline('pencil',(18,32),(22,21),(35,8),(42,15),(29,28),closed=True)
self.add_line('ferrule',(29,14),(36,21));self.relate('connect','pencil','ferrule')
''','notebook-pen')
add('CIRCLE','Circular Onam flower with six radial petals around a small center; mirrored diagonal petals share definitions.', '''
self.oval('rim',24,24,20)
self.oval('center',24,24,4)
self.add_bezier('petal-top',(24,20),((16,17),(20,10),(24,7)),((28,10),(32,17),(24,20)))
self.add_bezier('petal-bottom',(24,28),((16,31),(20,38),(24,41)),((28,38),(32,31),(24,28)))
for side in (-1,1):
    for vertical in (-1,1):
        def p(x,y):return (24+side*x,24+vertical*y)
        self.add_bezier(f'petal-{side}-{vertical}',p(4,2),(p(7,10),p(14,11),p(17,8)),(p(16,2),p(10,0),p(4,2)))
''','flower','None; six petals and enclosing circle retained.')
add('SQUARE','Remote doctor bust above a laptop at lower left, with medical cross at right. Detached head/body gap is 8 centerline units, 4 visible units.', '''
self.oval('head',30,12,6)
self.add_arc('shoulders',(18,38),(30,26),radius_x=12)
self.add_arc('shoulders-right',(30,26),(42,38),radius_x=12)
self.add_contour('body','shoulders','shoulders-right')
self.add_polyline('laptop',(6,42),(8,34),(8,26),(16,26))
self.add_line('base',(6,42),(28,42));self.relate('connect','laptop','base')
self.cross('medical',34,34,4)
''','laptop','Laptop screen partly open as in reference; shoulder sides simplified.')
assert len(designs)==len(items)
for n,(item,design) in enumerate(zip(items,designs),1):
 key,plan,body,ref,omissions=design
 out=Path(item['result_dir']);ident=item['icon_id'];uid=item['source_uuid']
 module_name=ident.replace('-','_')+'_'+uid.replace('-','_')+'.py'
 source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {item['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Construction plan: {plan}
# Keyshape visible extremes are supplied by Keyshape.{key}.bounds_for(SOLO48).
# Lucide construction reference: {ref or 'No useful subject match; shared human reference for portraits'}.
class Drawing(Solo48):
    icon_id = {ident!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(item['concept'].split())!r}
    def build(self):
{textwrap.indent(body.strip(),'        ')}
{HELPERS}
'''
 (out/module_name).write_text(source)
 spec=importlib.util.spec_from_file_location('candidate_'+str(n),out/module_name);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 result={**item,'author':AUTHOR,'keyshape':key,'construction_plan':plan,'lucide_reference':ref,'omissions':omissions,'module':module_name}
 try:
  icon=mod.Drawing();report=icon.validate_icon();(out/'validation.txt').write_text(report.describe());result['validation_status']=report.status
  svg=icon.to_svg();(out/(ident+'.svg')).write_text(svg)
  for theme in ['light','dark']:
   for size in [48,240]:
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,negate_colors=theme=='dark',background_color='#181818' if theme=='dark' else 'white')
  print(n,ident,report.status,flush=True)
 except Exception as exc:
  result['validation_status']='error';result['error']=repr(exc);(out/'validation.txt').write_text(repr(exc));print(n,ident,repr(exc),flush=True)
 (out/'pending-review.json').write_text(json.dumps(result,indent=2))
