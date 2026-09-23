"""Batch 34: fresh standalone SOLO48 drawings in supplied order."""
from pathlib import Path
import json, importlib.util, textwrap, traceback
import cairosvg
from PIL import Image,ImageOps,ImageDraw
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='7b4f6d04-e199-443e-be81-3c0acef5ca62'
SOURCE_PATH='icon_set/work/todo-references/picture polaroid landscape_7b4f6d04-e199-443e-be81-3c0acef5ca62.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'batch-inputs.json').read_text())
HELPERS='''
    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,rx,ry,diagonal=True):
        if diagonal:
            self.add_polyline(name+'-a',(cx-rx,cy-ry),(cx,cy),(cx+rx,cy+ry))
            self.add_polyline(name+'-b',(cx+rx,cy-ry),(cx,cy),(cx-rx,cy+ry))
        else:
            self.add_polyline(name+'-a',(cx-rx,cy),(cx,cy),(cx+rx,cy))
            self.add_polyline(name+'-b',(cx,cy-ry),(cx,cy),(cx,cy+ry))
        self.relate('connect',name+'-a',name+'-b')

    def pin(self,name,cx,top,r,tip,style='broad'):
        cy=top+r
        self.add_arc(name+'-dome',(cx-r,cy),(cx+r,cy),radius_x=r)
        if style=='narrow':
            self.add_bezier(name+'-right',(cx+r,cy),((cx+r,cy+8),(cx+r-4,cy+11),(cx+7,tip-9)),((cx+3,tip-6),(cx+2,tip-4),(cx,tip)))
            self.add_bezier(name+'-left',(cx,tip),((cx-2,tip-4),(cx-3,tip-6),(cx-7,tip-9)),((cx-r+4,cy+11),(cx-r,cy+8),(cx-r,cy)))
        else:
            self.add_bezier(name+'-right',(cx+r,cy),((cx+r,cy+7),(cx+7,tip-6),(cx,tip)))
            self.add_bezier(name+'-left',(cx,tip),((cx-7,tip-6),(cx-r,cy+7),(cx-r,cy)))
        self.add_contour(name,name+'-dome',name+'-right',name+'-left',closed=True)

    def aircraft(self):
        # Intentionally oblique silhouette: shared wing roots and tapered tail.
        self.add_polyline('plane',(8,12),(12,11),(17,13),(23,11),(16,6),(20,4),(29,8),(35,6))
        self.add_arc('nose',(35,6),(39,10),radius_x=3)
        self.add_polyline('plane-bottom',(39,10),(31,13),(27,20),(23,20),(25,15),(13,18),(8,12))
        self.add_contour('aircraft','plane-1','plane-2','plane-3','plane-4','plane-5','plane-6','plane-7','nose','plane-bottom-1','plane-bottom-2','plane-bottom-3','plane-bottom-4','plane-bottom-5','plane-bottom-6',closed=True)
'''
# keyshape, plan, references, omissions, body
DESIGNS=[
('SQUARE','Polaroid landscape with two mountain peaks, upper-left sun and a wide bottom margin. Frame owns baseline attachments.','Lucide image: framed peaks and round sun.','Sun reduced to a small circle; corners use rounded stroke joins.', '''
self.add_polyline('frame',(6,6),(42,6),(42,34),(42,42),(6,42),(6,34),closed=True)
self.add_line('margin',(6,34),(42,34));self.relate('connect','frame','margin')
self.circle('sun',16,16,2)
self.add_polyline('mountains',(10,34),(18,28),(24,34),(32,22),(42,34));self.relate('connect','mountains','margin');self.relate('connect','mountains','frame')
'''),
('SQUARE','Stacked portrait pictures: front rounded panel with detached round head and smooth shoulders, rear panel visible at right.','Shared human-reference.md and human_ref/user.svg own head/shoulders; Lucide image supplies enclosure construction.','Facial detail absent in source; none added. Rear picture is an exposed outline only.', '''
self.box('front',6,6,28,36,6)
self.add_arc('rear-top',(34,14),(42,22),radius_x=8)
self.add_line('rear-side',(42,22),(42,26))
self.add_arc('rear-bottom',(42,26),(34,34),radius_x=8)
self.add_contour('rear','rear-top','rear-side','rear-bottom');self.relate('connect','front','rear')
self.circle('head',20,18,4)
self.add_bezier('shoulders',(12,42),((12,35),(15,30),(20,30)),((25,30),(28,35),(28,42)))
self.relate('connect','front','shoulders')
# Head bottom 22; shoulder apex 30: exactly 8 centerline / 4 ink.
'''),
('SQUARE','Three stacked landscape pictures. Front owns sun, two mountain peaks and lower caption margin; two rear L outlines retain the layer count.','Lucide image: frame, round sun, joined peaks.','No layers omitted; minor corner rounding simplified.', '''
self.box('front',6,6,26,26,2)
self.add_polyline('rear-1',(32,12),(37,12),(37,37),(12,37),(12,32))
self.add_polyline('rear-2',(37,18),(42,18),(42,42),(18,42),(18,37))
self.relate('connect','front','rear-1');self.relate('connect','rear-1','rear-2')
self.circle('sun',14,14,2)
self.add_polyline('mountains',(10,27),(16,20),(20,24),(26,16),(32,27));self.relate('connect','front','mountains')
self.add_line('margin',(6,27),(32,27));self.relate('connect','front','margin');self.relate('connect','mountains','margin')
'''),
('SQUARE','Framed sunshine above overlapping rounded hills. Five ray marks share the sun center; hills remain deliberately unequal.','Lucide image: rounded frame; circle construction for sun.','Ray lengths reduced; all five source directions retained.', '''
self.box('frame',6,6,36,36,4)
self.circle('sun',24,20,4)
self.add_line('ray-top',(24,11),(24,10))
for name,a,b in [('left',(14,20),(13,20)),('right',(34,20),(35,20)),('nw',(17,13),(16,12)),('ne',(31,13),(32,12))]:self.add_line('ray-'+name,a,b)
self.add_bezier('front-hill',(6,32),((13,25),(25,25),(29,36)));self.relate('connect','frame','front-hill')
self.add_bezier('back-hill',(27,32),((33,28),(38,31),(42,36)));self.relate('connect','frame','back-hill')
'''),
('SQUARE','Landscape picture with sun upper right and overlapping angular mountain ridges. Preserve diagonal asymmetry.','Lucide image: geometric peaks and framed sun.','Sun hole reduces to a tiny native-size disc; frame uses rounded joins.', '''
self.add_polyline('frame',(6,6),(42,6),(42,36),(42,42),(6,42),(6,29),closed=True)
self.add_polyline('back-mountain',(6,29),(18,17),(28,27));self.relate('connect','frame','back-mountain')
self.add_polyline('front-mountain',(22,33),(28,27),(31,24),(42,36));self.relate('connect','front-mountain','back-mountain');self.relate('connect','front-mountain','frame')
self.circle('sun',32,16,2)
'''),
('HRECT_M','Horizontal capsule split diagonally, checkmark in left half and X in right half. Capsule end radii match.','Lucide pill: tangent capsule ends and diagonal division.','No defining glyphs omitted.', '''
self.add_line('pill-top',(18,10),(30,10))
self.add_arc('pill-right',(30,10),(30,38),radius_x=14)
self.add_line('pill-bottom',(30,38),(18,38))
self.add_arc('pill-left',(18,38),(18,10),radius_x=14)
self.add_contour('pill','pill-top','pill-right','pill-bottom','pill-left',closed=True)
self.add_line('split',(27,10),(21,38));self.relate('connect','pill','split')
self.add_polyline('check',(10,24),(14,28),(20,20))
self.cross('x',33,24,3,4)
'''),
('SQUARE','Rounded pillbox with shallow lid division and medical plus centered below. Cross arms share one length.','Lucide pill: rounded medical object; rounded rectangle construction.','Outlined medical plus reduced to crossed strokes to preserve its identity with more space.', '''
self.box('box',6,6,36,36,6)
self.add_line('lid',(6,14),(42,14));self.relate('connect','box','lid')
self.cross('medical-plus',24,28,5,5,False)
'''),
('SQUARE','Large location pin with lower-right circular add badge. Pin and badge remain a complete composition.','Lucide map-pin: domed pin with pointed bottom.','None; badge and plus retained.', '''
self.pin('pin',17,6,11,36)
self.circle('badge',32,32,10)
self.cross('plus',32,32,2,2,False)
'''),
('VRECT_L','Blank pin with a rounded head and narrow inward-curving lower neck. Shared axis x=24.','Lucide map-pin: circular top with smooth lower contours.','None; no inner mark exists in the reference.', '''
self.pin('pin',24,4,16,44,'narrow')
'''),
('VRECT_L','Blank teardrop pin with broad sweeping lower sides. Shared axis x=24.','Lucide map-pin: circular dome and coherent pointed contour.','None; no inner mark exists in the reference.', '''
self.pin('pin',24,4,16,44)
'''),
('VRECT_L','Round map marker containing X, with a short narrow triangular tail below. Head symmetry and X share x=24.','Lucide map-pin: rounded head and point; X is hand-authored.','None.', '''
self.add_arc('dome',(8,20),(40,20),radius_x=16)
self.add_bezier('right',(40,20),((40,27),(35,33),(28,35)))
self.add_polyline('tail',(28,35),(24,44),(20,35))
self.add_bezier('left',(20,35),((13,33),(8,27),(8,20)))
self.add_contour('pin','dome','right','tail-1','tail-2','left',closed=True)
self.cross('x',24,20,5,5)
'''),
('VRECT_M','Location pin with round hole over a small ground X. The narrow crossing stays centered on the tip.','Lucide map-pin: circular hole and tapered pin.','Ground X compressed vertically to maintain the pin above it.', '''
self.pin('pin',24,4,14,32)
self.circle('hole',24,18,4)
self.cross('ground-x',24,41,6,3)
'''),
('VRECT_M','Broad rounded pin with a larger circular hole over a wide ground X. Softer base distinguishes it from pin x mark 2.','Lucide map-pin: domed head and hole.','None; broad X retained.', '''
self.add_arc('dome',(10,18),(38,18),radius_x=14)
self.add_bezier('right',(38,18),((38,25),(29,31),(25,33)),((24,34),(24,34),(23,33)))
self.add_bezier('left',(23,33),((19,31),(10,25),(10,18)))
self.add_contour('pin','dome','right','left',closed=True)
self.circle('hole',24,18,5)
self.cross('ground-x',24,40,9,4)
'''),
('VRECT_L','Round-headed straight map pin standing at the center of a wide ground X. Head and shaft share the vertical axis.','Lucide map-pin: round head vocabulary; straight pin reconstructed from source.','None.', '''
self.circle('head',24,12,8)
self.add_polyline('shaft',(24,20),(24,38));self.relate('connect','head','shaft')
self.cross('ground-x',24,38,16,6)
self.relate('connect','shaft','ground-x-a');self.relate('connect','shaft','ground-x-b')
'''),
('VRECT_L','Tall hollow map pin above a very wide, shallow ground X. Preserve source’s unequal pin and ground widths.','Lucide map-pin: circular aperture and teardrop contour.','None.', '''
self.pin('pin',24,4,11,32)
self.circle('hole',24,15,3)
self.cross('ground-x',24,40,16,4)
'''),
('VRECT_L','Oblique airplane above a divider, cocktail bowl, stem and citrus garnish below. All service elements remain together.','Lucide plane: coherent wing contour; martini: stem and foot construction, while preserving source’s round bowl.','Minor aircraft edge rounding simplified; garnish retained.', '''
# Aircraft is a single outline using explicit continuous segments.
self.add_polyline('aircraft',(8,12),(12,11),(17,13),(23,11),(16,6),(20,4),(29,8),(36,6),(40,8),(39,11),(31,13),(27,20),(23,20),(25,15),(13,18),closed=True)
self.add_line('divider',(8,26),(40,26))
self.add_arc('bowl',(15,32),(29,32),radius_x=7,radius_y=6,sweep=False)
self.add_line('rim',(15,32),(29,32));self.relate('connect','bowl','rim')
self.add_line('stem',(22,38),(22,44));self.relate('connect','bowl','stem')
self.add_polyline('foot',(18,44),(22,44),(26,44));self.relate('connect','stem','foot')
self.add_arc('citrus',(29,28),(29,34),radius_x=3)
'''),
('VRECT_L','Oblique airplane above a divider with fork and knife below. Fork owns shared tine spacing; knife keeps its curved blade.','Lucide plane: continuous wing silhouette; source determines utensil shapes.','None; aircraft, separator, fork and knife retained.', '''
self.add_polyline('aircraft',(8,12),(12,11),(17,13),(23,11),(16,6),(20,4),(29,8),(36,6),(40,8),(39,11),(31,13),(27,20),(23,20),(25,15),(13,18),closed=True)
self.add_line('divider',(8,26),(40,26))
self.add_line('fork-left',(12,32),(12,36))
self.add_arc('fork-bowl',(12,36),(20,36),radius_x=4,sweep=False)
self.add_line('fork-right',(20,36),(20,32))
self.add_contour('fork','fork-left','fork-bowl','fork-right')
self.add_polyline('fork-stem',(16,32),(16,40),(16,44));self.relate('connect','fork','fork-stem')
self.add_polyline('knife-back',(28,44),(28,40),(28,32))
self.add_bezier('blade',(28,32),((32,34),(36,36),(36,40)))
self.add_line('blade-bottom',(36,40),(28,40));self.relate('connect','knife-back','blade');self.relate('connect','blade','blade-bottom');self.relate('connect','knife-back','blade-bottom')
'''),
('VRECT_L','Walking traveler carrying a rectangular bag, with a small aircraft upper right. Head follows upper torso axis.','Shared human-reference.md/full_body_ref.png: circular head and coherent limbs; Lucide plane: directional wing branches.','Outlined limbs reduced to the shared stick-figure vocabulary. Bag and aircraft retained.', '''
self.circle('head',18,9,5)
self.add_line('torso',(18,22),(18,32))
self.add_polyline('arm-right',(18,22),(26,28),(30,28));self.relate('connect','torso','arm-right')
self.add_polyline('arm-left',(18,22),(12,25),(12,28));self.relate('connect','torso','arm-left')
self.box('bag',8,28,12,10,2);self.relate('connect','bag','arm-left')
self.add_polyline('legs',(13,44),(18,32),(30,44));self.relate('connect','torso','legs')
self.mark_human_figure('traveler',head='head',torso='torso',torso_junction='start')
# Head bottom is y14 and neck is y22: exactly 4 units visible ink gap.
self.add_polyline('plane-spine',(36,4),(36,10),(36,22))
self.add_polyline('wings',(32,14),(36,10),(40,14));self.relate('connect','plane-spine','wings')
self.add_polyline('tail',(33,24),(36,22),(39,24));self.relate('connect','plane-spine','tail')
'''),
('SQUARE','Television play button: antenna pair, rectangular screen, two feet and central play triangle. Symmetry axis x=24.','Lucide tv: paired antenna and screen; circle-play: simple triangular play glyph.','Rounded screen corners reduced to round stroke joins; triangle compressed vertically for the screen.', '''
self.add_polyline('screen',(6,14),(24,14),(42,14),(42,38),(36,38),(12,38),(6,38),closed=True)
self.add_polyline('antenna',(15,6),(24,14),(33,6));self.relate('connect','screen','antenna')
for i,x in enumerate((12,36)):
 self.add_line(f'foot-{i}',(x,38),(x,42));self.relate('connect','screen',f'foot-{i}')
self.add_polyline('play',(18,22),(30,26),(18,30),closed=True)
'''),
('CIRCLE','Play triangle centered optically within a circular outline. Right-pointing asymmetry carries direction.','Lucide circle-play: outer circle and one triangular contour.','None.', '''
self.circle('circle',24,24,20)
self.add_polyline('play',(18,14),(34,24),(18,34),closed=True)
''')]

def run():
 for row,(key,plan,refs,omissions,body) in zip(ROWS,DESIGNS):
  d=Path(row['result_dir']);p=d/(row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
  if (d/'result.json').exists():continue
  bounds=Keyshape[key].bounds_for(Profile.SOLO48)
  source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={row['source_uuid']!r}
SOURCE_PATH={row['reference_path']!r}
AUTHOR={AUTHOR!r}
PLAN={plan!r}
CONSTRUCTION_REFERENCES={refs!r}
OMISSIONS={omissions!r}
KEYSHAPE_INK_BOUNDS={bounds!r}

class Drawing(Solo48):
    icon_id={row['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(row['concept'].split())!r}
{HELPERS}
    def build(self):
{textwrap.indent(textwrap.dedent(body).strip(),'        ')}
'''
  p.write_text(source)
  rec={**row,'author':AUTHOR,'module':p.name,'keyshape':key,'keyshape_ink_bounds':bounds,'subject_and_plan':plan,'construction_references':refs,'omissions':omissions}
  try:
   spec=importlib.util.spec_from_file_location('batch34_'+row['source_uuid'],p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;(d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
   for size in (48,240):
    p=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
   print(row['concept'],report.describe(),flush=True)
  except Exception:
   rec['validation_status']='error';rec['error']=traceback.format_exc();(d/'validation.txt').write_text(rec['error']);print(row['concept'],rec['error'],flush=True)
  (d/'review-draft.json').write_text(json.dumps(rec,indent=2))

if __name__=='__main__':run()
