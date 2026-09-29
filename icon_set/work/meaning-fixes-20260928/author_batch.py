from pathlib import Path
import json,re,textwrap,sys,io
from datetime import datetime,timezone
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
ROOT=Path('icon_set/work/meaning-fixes-20260928')
AUTHOR='gpt-6'
ITEMS=json.loads((ROOT/'claims.json').read_text())
# Designs authored after visually comparing every original and rejected drawing.
D={}
def design(n,key,problem,change,ref,code):D[n]=(key,problem,change,ref,textwrap.dedent(code))
design(1,'SQUARE','The heads were attached to the limbs; the upper pose became a tall arch with no supporting arm.','Restore two detached heads, a shallow upper bridge, an arm and two lower supports.','human_ref/full_body_ref.png', '''
circle('upper-head',10,13,4)
circle('lower-head',10,31,4)
path('upper-torso',(22,13),[C((42,13),(28,6),(36,6))])
line('upper-arm',(22,13),(22,24));join('upper-arm','upper-torso')
line('upper-leg',(42,13),(42,29));join('upper-leg','upper-torso')
line('lower-torso',(22,31),(42,31))
line('lower-arm',(22,31),(22,42));join('lower-arm','lower-torso')
line('lower-leg',(42,31),(42,42));join('lower-leg','lower-torso')
self.mark_human_figure('upper',head='upper-head',torso='upper-torso-0',torso_junction='start')
self.mark_human_figure('lower',head='lower-head',torso='lower-torso',torso_junction='start')
''')
design(2,'VRECT_L','An extra head-like ring at the top and a single shared body obscured the two-person pose.','Keep exactly two right-facing detached heads and two horizontal torsos, with the upper curled leg and lower bent leg.','human_ref/full_body_ref.png', '''
circle('upper-head',38,24,4);circle('lower-head',38,42,4)
line('upper-torso',(26,24),(10,24))
path('upper-leg',(26,24),[C((23,12),(31,20),(22,16)),C((26,5),(19,5),(23,3)),C((28,9),(29,5),(30,8))])
join('upper-torso','upper-leg')
line('lower-torso',(26,42),(12,42))
path('lower-leg',(26,42),[C((26,25),(28,38),(26,30))]);join('lower-torso','lower-leg')
self.mark_human_figure('upper',head='upper-head',torso='upper-torso',torso_junction='start')
self.mark_human_figure('lower',head='lower-head',torso='lower-torso',torso_junction='start')
''')
design(3,'HRECT_L','The broad pirate hat became a domed helmet, the cross collapsed, and the beard was narrow and angular.','Restore the flared tricorn silhouette, readable crossed mark, rounded face sides and pointed full beard.','skull', '''
path('hat',(4,22),[C((13,13),(4,17),(8,13)),C((24,6),(15,6),(19,6)),C((35,13),(29,6),(33,6)),C((44,22),(40,13),(44,17)),L((35,25)),C((13,25),(29,21),(19,21)),L((4,22))],True)
poly('cross-a',(21,12),(27,18));poly('cross-b',(27,12),(21,18))
path('face-left',(14,25),[C((17,34),(14,30),(15,32))])
path('face-right',(34,25),[C((31,34),(34,30),(33,32))])
path('beard',(24,30),[C((32,35),(29,30),(32,32)),C((24,44),(32,38),(27,42)),C((16,35),(21,42),(16,38)),C((24,30),(16,32),(19,30))],True)
''')
design(4,'SQUARE','The mug left wall disappeared behind a large bread shape and the handle became a tiny loop.','Restore a visible mug body, rounded foam, a generous side handle and a separate rounded loaf with one scoring cut.','beer', '''
path('foam',(10,17),[C((8,9),(4,17),(4,10)),C((17,8),(11,6),(14,6)),C((29,8),(18,1),(28,1)),C((35,17),(39,5),(41,17)),L((10,17))],True)
line('mug-left',(10,17),(10,27));join('foam','mug-left')
path('mug-right',(35,17),[L((35,35)),C((29,42),(35,40),(33,42)),L((27,42))]);join('foam','mug-right')
path('handle',(35,22),[L((39,22)),C((44,27),(44,22),(44,24)),L((44,31)),C((39,36),(44,34),(43,36)),L((35,36))])
path('loaf',(4,42),[C((4,38),(3,41),(3,40)),C((26,38),(6,26),(24,26)),C((26,42),(27,40),(27,41)),L((4,42))],True)
line('score',(15,31),(15,35))
''')
design(5,'SQUARE','The flattened scalloped outline read as a cloud or flower, with no anatomical folds.','Use a taller paired-lobe outline and two short inward folds while retaining an undivided centre.','brain', '''
for side in (-1,1):
 p=lambda x,y:(24+side*x,y)
 path('lobe-'+str(side),p(0,11),[C(p(8,6),p(2,4),p(7,4)),C(p(13,13),p(12,6),p(14,9)),C(p(18,23),p(20,13),p(21,19)),C(p(17,33),p(22,27),p(21,32)),C(p(9,41),p(20,39),p(15,44)),C(p(0,38),p(4,44),p(1,43))])
 path('fold-'+str(side),p(13,13),[C(p(10,19),p(14,16),p(12,19))]);join('lobe-'+str(side),'fold-'+str(side))
join('lobe--1','lobe-1')
''')
design(6,'SQUARE','The browser toolbar had no controls and the oversized single-bar currency mark dominated the frame.','Add a clear browser toolbar with two controls and restore a finer-positioned yuan mark in the lower-right content area.','panel-top', '''
rounded('browser',6,6,42,42,4)
line('toolbar',(6,16),(42,16))
self.add_dot('control-one',(13,11));self.add_dot('control-two',(21,11))
poly('yuan-fork',(25,23),(31,30),(37,23))
line('yuan-stem',(31,30),(31,37))
line('yuan-bar',(26,33),(36,33))
''')
design(7,'SQUARE','Straight triangular wedges replaced the rounded banana fruits.','Restore three nested sweeping banana contours, blunt curved tips, and their shared upright stalk.','banana', '''
path('outer',(31,6),[L((37,6)),L((37,12)),C((43,28),(42,16),(45,23)),C((22,42),(40,37),(30,44)),C((16,39),(19,42),(17,41)),C((32,13),(30,33),(35,23)),L((31,6))],True)
path('middle',(32,13),[C((8,32),(30,29),(19,34)),C((16,39),(9,37),(12,39))])
path('upper',(32,13),[C((6,23),(26,25),(15,26)),C((8,32),(4,27),(6,30))])
''')
design(8,'VRECT_L','The rabbit was squared off like a letter H, with only one eye and no recognizable face or holding paw.','Restore a rounded rabbit face, two outward ears, paired eyes, a small nose and a paw holding an egg.','rabbit', '''
path('rabbit',(12,34),[C((9,20),(5,30),(6,24)),C((8,6),(4,11),(4,3)),C((18,17),(12,3),(15,9)),C((24,17),(20,16),(22,16)),C((34,6),(28,6),(32,3)),C((33,20),(38,3),(39,10)),C((35,26),(35,22),(36,24))])
path('cheek',(12,34),[C((24,35),(16,38),(21,37))])
self.add_dot('eye-left',(14,25));self.add_dot('eye-right',(25,25));self.add_dot('nose',(19,30))
path('body',(12,34),[C((10,44),(10,38),(10,40))])
path('egg',(35,27),[C((42,39),(39,27),(42,35)),C((28,40),(42,47),(30,47)),C((35,27),(26,35),(31,27))],True)
path('paw',(21,39),[L((27,38)),C((29,41),(30,37),(31,40)),L((23,43))])
''')
design(9,'SQUARE','The aircraft became a jagged lightning shape and the fire merged into it.','Restore a rounded nose, diagonal fuselage, wing and tail, with a separate flame and two smoke wisps.','plane', '''
path('plane',(8,24),[L((14,27)),L((14,31)),L((36,40)),C((41,35),(43,41),(45,37)),L((31,30)),L((24,19)),L((19,17)),L((20,27)),L((11,23)),L((8,16)),L((6,15)),L((6,22)),C((8,24),(6,23),(7,24))],True)
path('wing',(20,32),[L((8,40)),L((13,43)),L((29,36))])
path('flame',(34,24),[C((31,14),(28,22),(31,18)),C((36,7),(35,17),(38,12)),C((42,25),(42,14),(46,20))])
path('smoke-one',(8,8),[C((9,4),(5,6),(10,6))])
path('smoke-two',(18,9),[C((19,4),(15,7),(20,6))])
''')
design(10,'HRECT_L','The kneeling legs collapsed into a triangular blob and the hand/body pose was ambiguous.','Draw a clear backbend, vertical reaching arm, bent knees and a horizontal shin, preserving the head position.','human_ref/full_body_ref.png', '''
circle('head',38,8,5)
path('torso',(33,20),[C((15,26),(27,20),(20,21)),C((7,37),(10,30),(7,34))])
path('knees',(7,37),[C((10,40),(7,40),(8,40)),L((24,40))]);join('torso','knees')
line('thigh',(15,26),(15,39));join('torso','thigh')
line('arm',(33,20),(33,40));join('arm','torso')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
''')
design(11,'SQUARE','The flag and doorway collapsed into thick marks; the camper was crowded against the tent.','Restore a triangular tent opening, a small flag, and a distinct camper head and shoulder behind the tent.','tent + human_ref/user.svg', '''
poly('tent',(5,42),(20,16),(35,42),(5,42),closed=True)
poly('door',(15,42),(20,32),(25,42))
poly('flag',(20,16),(20,5),(28,8),(20,11))
circle('head',37,12,5)
path('shoulder',(30,26),[C((43,31),(33,22),(43,24)),L((43,42)),L((36,42))])
''')
design(12,'HRECT_L','The hull read as a bowl and the paddler had no clear bent arm or seated lean; water was omitted.','Restore the leaning seated figure, bent arm, diagonal paddle, pointed canoe bow and two wave troughs.','sailboat + human_ref/full_body_ref.png', '''
circle('head',18,8,4)
line('torso',(18,20),(14,31))
poly('arm',(18,20),(26,22),(33,16));join('torso','arm')
poly('leg',(14,31),(24,31),(25,28));join('torso','leg')
line('paddle',(38,7),(24,34))
path('canoe',(4,32),[L((34,32)),C((41,27),(39,32),(40,30)),C((41,39),(46,30),(46,36))])
path('water',(4,41),[C((16,40),(9,44),(12,44)),C((28,40),(20,44),(24,44)),C((40,41),(32,44),(36,44))])
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
design(13,'SQUARE','The defining almond-shaped Divine Eye was replaced by a small circle.','Restore the eye contour and centred pupil inside the triangular symbol.','eye', '''
poly('triangle',(24,5),(44,42),(4,42),(24,5),closed=True)
path('eye',(13,28),[C((35,28),(19,18),(29,18)),C((13,28),(29,38),(19,38))],True)
self.add_dot('pupil',(24,28))
''')
design(14,'HRECT_L','The rider became a disconnected head over an angular frame; the seated posture and scooter body were lost.','Restore the capped head, bent riding arm and leg, rounded scooter shell, parcel box and two open wheels.','car + human_ref/full_body_ref.png', '''
circle('head',26,8,4);line('cap-brim',(23,7),(34,7))
line('torso',(26,20),(25,28))
poly('arm',(26,20),(34,24),(38,24));join('torso','arm')
poly('leg',(25,28),(31,30),(31,36));join('torso','leg')
rounded('parcel',5,18,17,28,2)
path('scooter',(4,35),[C((13,31),(4,32),(7,31)),L((25,31)),L((27,37)),L((38,37)),L((39,28))])
line('steering',(38,24),(41,35))
circle('wheel-back',11,40,4);circle('wheel-front',41,40,4)
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
design(15,'SQUARE','The impact became a closed badge and the car halves looked like two separate small cars.','Restore an open sharp impact burst above one car split by a central zigzag break, with two circular wheels.','car', '''
poly('burst',(6,23),(3,19),(11,19),(8,10),(17,14),(23,4),(27,14),(37,9),(34,19),(44,19),(41,23))
path('left-car',(21,27),[L((14,27)),L((9,34)),L((6,35)),L((6,41)),L((8,41))])
poly('left-break',(21,27),(18,33),(24,37),(20,44),(16,44))
path('right-car',(29,27),[L((35,27)),L((39,34)),C((44,38),(44,34),(44,35)),L((44,41)),L((42,41))])
poly('right-break',(29,27),(26,33),(32,37),(28,44),(34,44))
circle('left-wheel',12,42,4);circle('right-wheel',38,42,4)
''')
design(16,'HRECT_M','The progress bar was nearly square, so it read as a prohibition or capsule symbol.','Restore the long horizontal capsule proportions and a diagonal progress boundary.','No useful exact Lucide match; rounded enclosure construction from panel-top.', '''
path('capsule',(12,16),[L((29,16)),L((36,16)),A((36,32),8,8,True),L((19,32)),L((12,32)),A((12,16),8,8,True)],True)
line('progress',(29,16),(19,32));join('capsule','progress')
''')
design(17,'VRECT_M','The device lacked its lower phone panel and the pound glyph had a straight bar-like foot.','Restore a rounded handset with bottom separator and a recognizable curved pound stem and baseline.','smartphone', '''
rounded('phone',10,4,38,44,5)
line('phone-bottom',(10,36),(38,36))
path('pound',(28,15),[C((24,11),(28,12),(27,11)),C((20,16),(21,11),(20,13)),L((20,25)),C((17,29),(20,27),(19,29)),L((29,29))])
line('pound-crossbar',(17,21),(26,21))
''')
design(18,'SQUARE','The square wall plate and flattened recess were removed, leaving a generic circle with two lines.','Restore a rounded square plate, flattened circular recess and matching vertical slots.','plug', '''
rounded('plate',6,6,42,42,5)
path('recess',(17,14),[L((31,14)),C((31,34),(39,18),(39,30)),L((17,34)),C((17,14),(9,30),(9,18))],True)
for x in (20,28):line('slot-'+str(x),(x,21),(x,27))
''')
design(19,'SQUARE','The wall plate disappeared and the pin holes were rendered as filled dots.','Restore the square wall plate and two circular pin openings inside the grounded round recess.','plug', '''
rounded('plate',5,5,43,43,5)
circle('recess',24,24,13)
circle('pin-left',19,24,3);circle('pin-right',29,24,3)
line('earth-top',(24,11),(24,16));line('earth-bottom',(24,32),(24,37))
''')
design(20,'SQUARE','The anchor nodes were tall ovals and the diagonal connectors merged into one heavy arrow-like shape.','Restore four equal circular vector nodes and three distinct spokes with deliberate node-edge attachments.','spline', '''
circle('hub',9,24,4)
circle('upper',30,7,4);circle('right',41,24,4);circle('lower',30,41,4)
line('horizontal',(13,24),(37,24));join('hub','horizontal');join('right','horizontal')
line('upper-spoke',(12,21),(27,10))
line('lower-spoke',(12,27),(27,38))
''')
HELPERS='''
        def path(name,start,commands,closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(commands):
                if end==here and kind=='L':continue
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        L=lambda end:('L',end)
        C=lambda end,c1,c2:('C',end,c1,c2)
        A=lambda end,rx,ry,sweep:('A',end,rx,ry,sweep)
        line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
def generate(indices):
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 manifest=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else {}
 for n in indices:
  it=ITEMS[n-1];key,problem,change,ref,code=D[n]
  src=Path(it['reference']);m=re.search(r'([0-9a-f-]{36})$',src.stem);uuid=m[1];concept=src.stem[:m.start()].rstrip('_ ')
  out=Path('icon_set/work/primitive-make-ray')/uuid/(stamp+'-meaning-fix');out.mkdir(parents=True,exist_ok=False)
  metadata=dict(concept=concept,source_uuid=uuid,reference_path=str(src))
  (out/(it['id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
  record={**it,**metadata,'result_dir':str(out),'problem':problem,'change':change,'construction_reference':ref,'keyshape':key,'author':AUTHOR}
  (out/'review-before.json').write_text(json.dumps(record,indent=2))
  module=out/(it['id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  module.write_text(f'"""{change}\nPlan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.\nBefore: {problem}\nConstruction: {ref}.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {str(src)!r}\nAUTHOR = {AUTHOR!r}\n\nclass RevisedIcon(Solo48):\n    icon_id = {it["id"]!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(concept.split())!r}\n\n    def build(self):\n'+HELPERS+textwrap.indent(code,'        '))
  record['module']=str(module);manifest[str(n)]=record
  icon=load_icon(module);svg=icon.to_svg();(out/(it['id']+'.svg')).write_text(svg)
  render_previews(svg,it['id'],48,out)
  import cairosvg
  for name,p in [('reference',src),('before',Path(it['before']))]:cairosvg.svg2png(url=str(p),write_to=str(out/(name+'.png')),output_width=384,output_height=384,background_color='white')
  print(n,it['id'],out,flush=True)
 (ROOT/'runs.json').write_text(json.dumps(manifest,indent=2))
if __name__=='__main__':generate([int(x) for x in sys.argv[1:]] or list(D))
