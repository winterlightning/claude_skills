"""Ordered batch 38 authoring, isolated from all library and runtime outputs."""
from pathlib import Path
import json,textwrap,importlib.util,traceback,cairosvg
from PIL import Image,ImageOps
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='592beacc-84e1-4868-af66-30a20a39dbfd'
SOURCE_PATH='icon_set/work/todo-references/rectangle list_592beacc-84e1-4868-af66-30a20a39dbfd.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'batch-inputs.json').read_text())
HELPERS='''
    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def bust(self,name,cx,cy,r,shoulder_half_width,shoulder_height):
        # Shared human reference: body apex exactly 8 below head outline.
        self.circle(name+'-head',cx,cy,r)
        apex=cy+r+8;end_y=apex+shoulder_height
        self.add_arc(name+'-shoulders',(cx-shoulder_half_width,end_y),(cx+shoulder_half_width,end_y),radius_x=shoulder_half_width,radius_y=shoulder_height)

    def cross(self,name,cx,cy,half):
        self.add_polyline(name+'-a',(cx-half,cy-half),(cx,cy),(cx+half,cy+half))
        self.add_polyline(name+'-b',(cx+half,cy-half),(cx,cy),(cx-half,cy+half))
        self.relate('connect',name+'-a',name+'-b')

    def reflection(self,direction):
        # Triangles mirror around the axis; only arrowhead direction changes.
        self.add_line('axis',(24,18),(24,42))
        for name,x,tip in (('left',6,16),('right',42,32)):
            self.add_polyline(name,(x,20),(tip,31),(x,42),closed=True)
        self.add_arc('arrow-arc',(14,16),(34,16),radius_x=10)
        x=14 if direction=='left' else 34
        self.add_polyline('arrowhead',(x-4,12),(x,16),(x+4,12))
        self.relate('connect','arrow-arc','arrowhead')
'''
# keyshape, structural plan, construction references, reductions, geometry
DESIGNS=[
('SQUARE','Rounded square list panel with three equal horizontal rules. A shared repeat owns row spacing.','Lucide list: consistent rows; rectangle-ellipsis: coherent rounded enclosure.','No source rules omitted; no bullet points added.', '''
self.box('panel',6,6,36,36,4)
for i,y in enumerate((16,24,32)):self.add_line(f'row-{i}',(15,y),(33,y))
'''),
('HRECT_M','Wide rounded text panel with a long upper rule and shorter lower rule, both left-aligned.','Lucide rectangle-ellipsis: rounded panel proportions; list: aligned text runs.','None.', '''
self.box('panel',4,10,40,28,3)
for name,y,end in (('long',19,35),('short',29,26)):self.add_line('text-'+name,(13,y),(end,y))
'''),
('HRECT_M','Wide password approval field with a right-aligned check and blank left half.','Lucide rectangle-ellipsis: rounded field construction.','None; source has no password dots.', '''
self.box('field',4,10,40,28,3)
self.add_polyline('check',(25,25),(29,29),(35,19))
'''),
('SQUARE','Framed person with circular detached head and a smooth broad shoulder arch. Subject and frame share x=24.','Shared human-reference.md and human_ref/user.svg own proportions and detached gap; Lucide rectangle-ellipsis supplies the frame.','Frame made taller to provide head/shoulder clearance.', '''
self.box('panel',6,6,36,36,4)
self.bust('person',24,18,3,8,4)
'''),
('VRECT_L','Portrait panel with four focus brackets around a head-and-shoulders silhouette. Bracket pairs mirror about x=24.','Shared human-reference.md/user.svg: circular head and shoulders; Lucide scan-face: corner focus brackets.','Hair and neck contour reduced to the shared detached-head vocabulary; all brackets retained.', '''
self.box('panel',8,4,32,40,4)
for name,points in [('tl',((14,18),(14,12),(18,12))),('tr',((30,12),(34,12),(34,18))),('bl',((14,30),(14,36),(18,36))),('br',((30,36),(34,36),(34,30)))]:self.add_polyline('focus-'+name,*points)
self.bust('person',24,20,3,6,3)
'''),
('HRECT_L','Rounded panel containing the full uppercase text SUB. Each glyph is authored as a coherent stroke or connected bowls.','Lucide rectangle-ellipsis: outer panel; letters hand-authored from supplied source.', 'None; all three letters retained.', '''
self.box('panel',4,8,40,32,4)
self.add_bezier('s',(18,17),((15,13),(9,15),(10,20)),((11,23),(17,23),(18,27)),((19,32),(12,34),(10,30)))
self.add_line('u-left',(23,16),(23,28))
self.add_arc('u-base',(23,28),(29,28),radius_x=3,sweep=False)
self.add_line('u-right',(29,28),(29,16));self.add_contour('u','u-left','u-base','u-right')
self.add_polyline('b-stem',(34,32),(34,24),(34,16),(36,16))
self.add_arc('b-upper',(36,16),(36,24),radius_x=4)
self.add_arc('b-lower',(36,24),(36,32),radius_x=4)
self.add_line('b-bottom',(36,32),(34,32));self.add_line('b-mid',(34,24),(36,24))
for a,b in [('b-stem','b-upper'),('b-upper','b-lower'),('b-lower','b-bottom'),('b-bottom','b-stem'),('b-mid','b-stem'),('b-mid','b-upper'),('b-mid','b-lower')]:self.relate('connect',a,b)
'''),
('HRECT_L','Two equivalent portrait busts inside a wide rounded panel. Shared head radius, shoulder widths and vertical positions preserve equality.','Shared human-reference.md/user.svg: equal circular heads and smooth shoulders; Lucide rectangle-ellipsis: frame.','None; both people retained.', '''
self.box('panel',4,8,40,32,4)
for name,cx in (('left',15),('right',33)):self.bust(name,cx,18,3,7,4)
'''),
('VRECT_M','Upright UV high indicator: long vertical stem attached to a low circular bulb inside a rounded panel.','Lucide rectangle-ellipsis: tangent rounded frame; source supplies indicator geometry.','None.', '''
self.box('panel',10,4,28,40,3)
self.circle('bulb',24,31,4)
self.add_line('stem',(24,13),(24,27));self.relate('connect','bulb','stem')
'''),
('VRECT_M','Upright UV medium indicator with the same bulb and frame as UV high, but a shorter stem.','Lucide rectangle-ellipsis: tangent rounded frame; UV pair shares dimensions.','None.', '''
self.box('panel',10,4,28,40,3)
self.circle('bulb',24,31,4)
self.add_line('stem',(24,21),(24,27));self.relate('connect','bulb','stem')
'''),
('VRECT_L','Portrait history panel enclosing a three-quarter circular return arrow and clock hands.','No local Lucide history original found; circular arc and attached arrow are constructed directly.','Minute ticks absent in source; no additions.', '''
self.box('panel',8,4,32,40,4)
self.add_arc('history',(24,34),(34,24),radius_x=10,large_arc=True)
self.add_polyline('arrow',(30,20),(34,24),(34,18));self.relate('connect','history','arrow')
self.add_polyline('hands',(24,18),(24,24),(28,28))
'''),
('HRECT_M','Wide rectangular panel enclosing four evenly spaced vertical rules. One series owns all strokes.','Lucide rectangle-ellipsis: panel; regular line series reconstructed from the supplied reference.','Corner arcs reduced to round joins for exact clearances; all four rules retained.', '''
self.add_polyline('panel',(4,10),(44,10),(44,38),(4,38),closed=True)
for i,x in enumerate((12,20,28,36)):self.add_line(f'rule-{i}',(x,18),(x,30))
'''),
('SQUARE','Rounded square panel containing a centered X with equal diagonal arms.','Lucide square-x: equal diagonals and matched enclosure corners.','None.', '''
self.box('panel',6,6,36,36,6)
self.cross('x',24,24,8)
'''),
('SQUARE','Diagonal recycling tag with its circular hole and a separate lower-right leaf with stem.','Lucide tag: clipped tag end and eyelet; leaf: coherent organic outline and vein.','Minor tag corner rounding simplified; tag and leaf retained.', '''
self.add_polyline('tag',(6,26),(26,6),(36,6))
self.add_arc('tag-corner',(36,6),(38,8),radius_x=2)
self.add_polyline('tag-return',(38,8),(38,17),(17,38),(6,28),(6,26))
self.add_contour('tag-outline','tag-1','tag-2','tag-corner','tag-return-1','tag-return-2','tag-return-3','tag-return-4',closed=True)
self.circle('eyelet',30,14,3)
self.add_bezier('leaf',(42,29),((32,27),(27,33),(30,38)),((34,44),(42,42),(42,29)))
self.add_polyline('stem',(26,42),(32,35),(36,33))
'''),
('HRECT_L','Two horizontal outlined bars with an upward sloping stroke attached to the lower bar. Shared width and eight-unit bar height.','No useful exact Lucide match; paired rectangles and diagonal stroke are reconstructed directly.','None.', '''
self.add_polyline('top-bar',(4,8),(44,8),(44,16),(4,16),closed=True)
self.add_polyline('bottom-bar',(4,32),(20,32),(44,32),(44,40),(4,40),closed=True)
self.add_line('slope',(20,32),(28,24));self.relate('connect','bottom-bar','slope')
'''),
('SQUARE','Mirrored triangles separated by a vertical axis, with an arched arrow pointing left overhead.','Lucide flip-horizontal-2: mirrored triangles and center axis. Source supplies the overhead directional arrow.','None.', '''
self.reflection('left')
'''),
('SQUARE','Mirrored triangles separated by a vertical axis, with an arched arrow pointing right overhead.','Lucide flip-horizontal-2: shared triangle construction; right variant changes only the overhead arrowhead.','None.', '''
self.reflection('right')
'''),
('SQUARE','Explosion with a diagonal capsule inside, beside a small house with an arched door. Preserve the full war/displacement scene.','No useful exact Lucide match; starburst and house contours reconstructed from source.','Two short peripheral impact rays omitted to reduce nonessential clutter.', '''
self.add_polyline('explosion',(18,6),(22,12),(30,8),(28,16),(34,18),(28,23),(31,30),(23,28),(20,34),(16,28),(8,31),(10,23),(6,18),(12,16),(10,10),(16,12),closed=True)
self.add_bezier('capsule',(15,17),((17,15),(19,17),(21,19)),((24,22),(22,25),(20,23)),((18,22),(13,19),(15,17)))
self.add_polyline('roof',(32,26),(42,34))
self.add_polyline('house',(24,38),(24,42),(40,42),(40,32));self.relate('connect','roof','house')
self.add_line('door-left',(29,42),(29,37))
self.add_arc('door-arch',(29,37),(35,37),radius_x=3)
self.add_line('door-right',(35,37),(35,42));self.add_contour('door','door-left','door-arch','door-right');self.relate('connect','house','door')
'''),
('SQUARE','Cao Dai eye inside an upright triangle. Outer triangle, symmetrical lens and circular iris share the vertical axis.','Lucide eye: smooth lens and circular iris; source owns the triangular enclosure.','None.', '''
self.add_polyline('triangle',(24,6),(42,42),(6,42),closed=True)
self.add_bezier('eye',(13,32),((19,24),(29,24),(35,32)),((29,40),(19,40),(13,32)))
self.circle('iris',24,32,3)
'''),
('HRECT_M','Diagonal bone beside a pointed leaf with a vein continuing into a stem. Preserve the organic asymmetry.','Lucide bone: paired rounded lobes and narrow shaft; leaf: curved pointed outline with stem.','None.', '''
self.add_bezier('bone',(12,16),((12,12),(10,10),(8,10)),((4,10),(4,15),(6,18)),((4,18),(4,20),(4,22)),((4,27),(10,28),(12,24)),((16,26),(20,28),(24,30)),((20,34),(24,38),(28,38)),((32,38),(33,32),(29,28)),((33,24),(28,19),(25,22)),((21,20),(16,18),(12,16)))
self.add_bezier('leaf',(44,12),((44,24),(43,31),(36,33)),((27,33),(29,18),(44,12)))
self.add_polyline('vein',(34,38),(36,33),(40,23));self.relate('connect','leaf','vein')
'''),
('HRECT_L','Nested outer and inner hexagons surrounding a circular center. Both hexagons share axis and paired sloping edges.','No useful exact Lucide match; symmetric polygon construction from source. Existing hidden draft inspected and found invalid, left unchanged.','None; both hexagons and center circle retained.', '''
cx,cy=24,24
for name,half_w,half_top,half_h in (('outer',20,10,16),('inner',10,5,8)):
 self.add_polyline(name,(cx-half_w,cy),(cx-half_top,cy-half_h),(cx+half_top,cy-half_h),(cx+half_w,cy),(cx+half_top,cy+half_h),(cx-half_top,cy+half_h),closed=True)
self.circle('center',24,24,3)
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
  p.write_text(source);rec={**row,'author':AUTHOR,'module':p.name,'keyshape':key,'keyshape_ink_bounds':bounds,'subject_and_plan':plan,'construction_references':refs,'omissions':omissions}
  try:
   spec=importlib.util.spec_from_file_location('batch38_'+row['source_uuid'],p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;(d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
   for size in (48,240):
    p=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
   print(row['concept'],report.describe(),flush=True)
  except Exception:
   rec['validation_status']='error';rec['error']=traceback.format_exc();(d/'validation.txt').write_text(rec['error']);print(row['concept'],rec['error'],flush=True)
  (d/'review-draft.json').write_text(json.dumps(rec,indent=2))

if __name__=='__main__':run()
