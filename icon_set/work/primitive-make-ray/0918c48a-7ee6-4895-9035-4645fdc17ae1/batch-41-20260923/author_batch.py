"""Ordered standalone SOLO48 authoring for TODO batch 41."""
from pathlib import Path
import json,textwrap,importlib.util,traceback,cairosvg
from PIL import Image,ImageOps
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='0918c48a-7ee6-4895-9035-4645fdc17ae1'
SOURCE_PATH='icon_set/work/todo-references/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg'
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

    def magnifier(self):
        # The handle node (30,33) is exactly radius 15 from (21,21).
        pts=[(6,21),(21,6),(36,21),(30,33),(6,21)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'lens-{i}',a,b,radius_x=15)
        self.add_contour('lens',*(f'lens-{i}' for i in range(4)),closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','lens','handle')

    def score(self,y):
        self.add_arc('two-top',(12,y+4),(20,y+4),radius_x=4)
        self.add_polyline('two-bottom',(20,y+4),(12,y+12),(20,y+12));self.relate('connect','two-top','two-bottom')
        for i,cy in enumerate((y+3,y+11)):self.add_dot(f'colon-{i}',(25,cy))
        self.box('zero',31,y,8,12,4)

    def terminal(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42));self.relate('connect','screen','stand')
        self.add_polyline('foot',(16,42),(24,42),(32,42));self.relate('connect','stand','foot')
        for i,y in enumerate((18,26)):self.add_line(f'equals-{i}',(31,y),(35,y))

    def send(self,direction):
        self.box('panel',6,6,36,36,4)
        if direction=='left':
            self.add_polyline('head',(23,17),(16,24),(23,31));self.add_line('shaft',(16,24),(33,24))
        else:
            self.add_polyline('head',(25,17),(32,24),(25,31));self.add_line('shaft',(32,24),(15,24))
        self.relate('connect','head','shaft')
'''
DESIGNS=[
('HRECT_L','Hanging scoreboard showing the complete score 2:0. Two equal top hangers attach to a rounded panel.','Lucide monitor: rounded board; score digits hand-authored from source.','None; both digits, colon and hangers retained.', '''
self.box('panel',4,14,40,26,3)
for i,x in enumerate((13,35)):
 self.add_polyline(f'hanger-{i}',(x,8),(x,14),(x,17));self.relate('connect','panel',f'hanger-{i}')
self.score(21)
'''),
('SQUARE','Standing scoreboard with the full 2:0 score above two supporting posts. Score glyphs share the first scoreboard construction.','Lucide monitor: panel; source defines freestanding posts.','None.', '''
self.box('panel',6,6,36,26,3)
for i,x in enumerate((13,35)):
 self.add_line(f'post-{i}',(x,32),(x,42));self.relate('connect','panel',f'post-{i}')
self.score(14)
'''),
('SQUARE','Empty comic action bubble with inward-curving edges and six detached action rays. Opposite sides mirror around (24,24).','No useful exact Lucide match; source provides the concave burst and ray pattern.','Ray lengths reduced to preserve surrounding space; all six rays retained.', '''
self.add_bezier('burst',(6,24),((10,23),(12,20),(10,16)),((14,18),(17,15),(18,12)),((22,17),(26,17),(30,12)),((31,15),(34,18),(38,16)),((36,20),(38,23),(42,24)),((38,25),(36,28),(38,32)),((34,30),(31,33),(30,36)),((26,31),(22,31),(18,36)),((17,33),(14,30),(10,32)),((12,28),(10,25),(6,24)))
for name,a,b in [('top',(24,6),(24,7)),('bottom',(24,41),(24,42)),('nw',(8,6),(10,8)),('ne',(38,8),(40,6)),('sw',(8,42),(10,40)),('se',(38,40),(40,42))]:self.add_line('ray-'+name,a,b)
'''),
('SQUARE','Eight-point seal outline with cardinal points and broad square corner shoulders. Shared step-six coordinates preserve symmetry.','Lucide badge: coherent closed seal contour; source supplies angular rather than scalloped edges.','None.', '''
self.add_polyline('seal',(24,6),(30,12),(36,12),(36,18),(42,24),(36,30),(36,36),(30,36),(24,42),(18,36),(12,36),(12,30),(6,24),(12,18),(12,12),(18,12),closed=True)
'''),
('HRECT_M','Rounded search field with a small magnifier at right. A real 3-4-5 attachment node connects its handle.','Lucide search: circular lens and attached handle; rounded bar rebuilt on SOLO48.','Handle shortened; capsule ends made less semicircular to open the glyph clearance.', '''
self.box('field',4,10,40,28,10)
self.add_arc('search-upper',(23,24),(33,24),radius_x=5)
self.add_arc('search-right',(33,24),(31,28),radius_x=5)
self.add_arc('search-lower',(31,28),(23,24),radius_x=5)
self.add_contour('search','search-upper','search-right','search-lower',closed=True)
self.add_line('handle',(31,28),(34,29));self.relate('connect','search','handle')
'''),
('SQUARE','Large magnifying glass with a round lens and lower-right handle. Handle attachment is an exact circle point.','Lucide search: one round lens and one attached handle.','None.', '''
self.magnifier()
'''),
('SQUARE','Walking person, rightward direction arrow and empty chair. Keep the complete find-seat scene.','Shared human-reference.md/full_body_ref.png: round head and coherent walking limbs; Lucide armchair informs the seat construction.','Outlined person and chair material thickness reduced to coherent strokes; chair foot retained as a baseline.', '''
self.circle('head',14,10,4)
self.add_line('torso',(14,22),(14,32))
self.add_polyline('arms',(8,28),(14,22),(21,27));self.relate('connect','torso','arms')
self.add_polyline('legs',(8,42),(14,32),(22,42));self.relate('connect','torso','legs')
self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
self.add_polyline('arrowhead',(26,14),(30,18),(26,22))
self.add_line('arrow-shaft',(23,18),(30,18));self.relate('connect','arrowhead','arrow-shaft')
self.add_polyline('chair',(40,12),(42,20),(40,34),(30,34))
self.add_line('chair-base',(30,42),(40,42))
'''),
('SQUARE','Partial person silhouette with a large magnifier in front at lower right. Preserve head, shoulder and visible torso edges.','Shared human-reference.md/user.svg: circular head and shoulder; Lucide search: lens/handle.','No major components omitted; shoulder is deliberately interrupted by the magnifier.', '''
self.circle('head',16,12,6)
self.add_polyline('body-side',(6,42),(6,34))
self.add_arc('shoulder',(6,34),(14,26),radius_x=8)
self.add_line('shoulder-top',(14,26),(22,26));self.add_contour('body','body-side-1','shoulder','shoulder-top')
self.add_line('arm-edge',(12,34),(12,42))
self.add_line('body-right',(28,40),(28,42))
self.add_arc('lens-top',(20,28),(40,28),radius_x=10)
self.add_arc('lens-right',(40,28),(36,36),radius_x=10)
self.add_arc('lens-bottom',(36,36),(20,28),radius_x=10)
self.add_contour('lens','lens-top','lens-right','lens-bottom',closed=True)
self.add_line('handle',(36,36),(42,42));self.relate('connect','lens','handle')
'''),
('SQUARE','Front-facing car with two radio arcs above. Car sides, wheels and headlights mirror around x=24.','Lucide car-front: joined roof, fascia and wheels.','Headlight outlines reduced to dots; wheel outlines reduced to short stems.', '''
self.box('body',6,26,36,10,4)
self.add_polyline('roof',(12,26),(16,18),(32,18),(36,26));self.relate('connect','body','roof')
for i,x in enumerate((12,36)):
 self.add_line(f'wheel-{i}',(x,36),(x,42));self.relate('connect','body',f'wheel-{i}')
for i,x in enumerate((14,34)):self.add_dot(f'headlight-{i}',(x,31))
self.add_arc('radio-outer',(14,10),(34,10),radius_x=10,radius_y=4)
self.add_arc('radio-inner',(18,14),(30,14),radius_x=6,radius_y=3)
'''),
('SQUARE','Payment terminal with dollar symbol at left and two equality/menu rules at right, supported by a stand.','Lucide monitor: screen and stand; dollar-sign: S contour crossed by vertical stem.','No currency or rule omitted.', '''
self.terminal()
self.add_bezier('dollar',(22,15),((21,14),(19,14),(18,14)),((12,14),(12,19),(18,20)),((24,21),(24,26),(18,26)),((16,26),(15,26),(14,25)))
self.add_polyline('dollar-stem',(18,11),(18,14),(18,20),(18,26),(18,29));self.relate('connect','dollar','dollar-stem')
'''),
('SQUARE','Payment terminal with euro symbol and two right-hand rules. Frame and stand match the currency series.','Lucide monitor and euro: open round C contour with a crossing bar.','Single crossbar matches source; no components omitted.', '''
self.terminal()
self.add_arc('euro-top',(22,13),(14,21),radius_x=8,sweep=False)
self.add_arc('euro-bottom',(14,21),(22,29),radius_x=8,sweep=False)
self.add_contour('euro','euro-top','euro-bottom')
self.add_polyline('crossbar',(12,21),(14,21),(22,21));self.relate('connect','euro','crossbar')
'''),
('SQUARE','Payment terminal with pound symbol, two right-hand rules and stand.','Lucide monitor and pound-sterling: round hook, crossbar and foot.','None.', '''
self.terminal()
self.add_arc('pound-hook',(23,16),(15,16),radius_x=4,sweep=False)
self.add_polyline('pound-stem',(15,16),(15,21),(15,26));self.relate('connect','pound-hook','pound-stem')
self.add_arc('pound-turn',(15,26),(12,29),radius_x=3);self.relate('connect','pound-stem','pound-turn')
self.add_polyline('pound-base',(12,29),(24,29));self.relate('connect','pound-turn','pound-base')
self.add_polyline('crossbar',(12,21),(15,21),(20,21));self.relate('connect','pound-stem','crossbar')
'''),
('SQUARE','Payment terminal with yuan Y and one crossbar, plus two rules and stand.','Lucide monitor and japanese-yen: branching Y construction. Source has one currency bar.','No components omitted; source single crossbar preserved.', '''
self.terminal()
self.add_polyline('yuan-top',(14,13),(19,21),(24,13))
self.add_polyline('yuan-stem',(19,21),(19,23),(19,29));self.relate('connect','yuan-top','yuan-stem')
self.add_polyline('yuan-bar',(14,23),(19,23),(24,23));self.relate('connect','yuan-stem','yuan-bar')
'''),
('CIRCLE','Semicolon with circular upper dot and an open rounded comma below. Common center x=24; comma flows into its tapered tail.','No useful exact Lucide match; punctuation reconstructed as circular arcs and one coherent tail.','None.', '''
self.circle('dot',24,10,6)
self.add_arc('comma-left',(24,37),(18,31),radius_x=6)
self.add_arc('comma-top-left',(18,31),(24,25),radius_x=6)
self.add_arc('comma-top-right',(24,25),(30,31),radius_x=6)
self.add_bezier('comma-tail',(30,31),((30,37),(28,41),(24,44)))
self.add_contour('comma','comma-left','comma-top-left','comma-top-right','comma-tail')
'''),
('SQUARE','Rounded square containing a left-pointing send-back arrow.','Lucide monitor: equal frame corners; arrow hand-authored from source.','None.', '''
self.send('left')
'''),
('SQUARE','Rounded square containing a right-pointing arrow, preserving the supplied send-backward reference.','Lucide monitor: equal frame corners; arrow mirrors send back.','None; source direction preserved even though filename says backward.', '''
self.send('right')
'''),
('SQUARE','Person with outstretched arms in an open-front cylindrical enclosure. Rim, side bands, window edges and figure are one complete scene.','Shared human-reference.md/full_body_ref.png: round head and coherent torso/limbs. Cylinder reconstructed from source.','Tiny upper rim ticks omitted; front opening, side bands and person retained.', '''
self.add_arc('rim-top',(6,12),(42,12),radius_x=18,radius_y=6)
self.add_bezier('rim-right',(42,12),((42,14),(39,15),(36,16)))
self.add_bezier('rim-left',(12,16),((9,15),(6,14),(6,12)))
self.add_polyline('wall-left',(6,12),(6,26),(6,36));self.relate('connect','rim-top','wall-left');self.relate('connect','rim-left','wall-left')
self.add_polyline('wall-right',(42,12),(42,26),(42,36));self.relate('connect','rim-top','wall-right');self.relate('connect','rim-right','wall-right')
self.add_bezier('bottom',(6,36),((6,38),(8,40),(12,40)),((16,41),(20,42),(24,42)),((28,42),(32,41),(36,40)),((40,40),(42,38),(42,36)))
self.relate('connect','bottom','wall-left');self.relate('connect','bottom','wall-right')
for name,x,rim in (('left',12,'rim-left'),('right',36,'rim-right')):
 self.add_polyline('window-'+name,(x,16),(x,29),(x,40));self.relate('connect','window-'+name,rim);self.relate('connect','window-'+name,'bottom')
self.add_bezier('band-left',(6,26),((6,28),(9,29),(12,29)))
self.add_bezier('band-right',(36,29),((39,29),(42,28),(42,26)))
for name in ('left','right'):
 self.relate('connect','band-'+name,'wall-'+name);self.relate('connect','band-'+name,'window-'+name)
self.circle('head',24,18,4)
self.add_line('torso',(24,30),(24,35))
self.add_polyline('arms',(16,30),(24,30),(32,30));self.relate('connect','torso','arms')
self.add_polyline('legs',(22,38),(24,35),(26,38));self.relate('connect','torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
('SQUARE','Magnifying glass containing a complete eye lens and circular iris. Preserve all three nested outlines and handle.','Lucide search: round magnifier; previously inspected Lucide eye: symmetric lens and circular iris.','None.', '''
self.magnifier()
self.add_bezier('eye',(10,21),((16,12),(26,12),(32,21)),((26,30),(16,30),(10,21)))
self.circle('iris',21,21,4)
'''),
('SQUARE','Uppercase serif M with upright outer stems, deep diagonal center and four horizontal serifs.','Lucide type: explicit serif terminals; M construction follows supplied character.','Double hairline outlines reduced to single coherent strokes while retaining the M and all serifs.', '''
self.add_polyline('m',(10,42),(10,6),(24,42),(38,6),(38,42))
for side,x in (('left',10),('right',38)):
 for level,y in (('top',6),('bottom',42)):
  name=f'{side}-{level}';self.add_polyline(name,(x-4,y),(x,y),(x+4,y));self.relate('connect','m',name)
'''),
('HRECT_M','Rounded service panel with two plus marks: lower small cross and taller upper-right cross. Preserve their unequal vertical extents.','Lucide monitor: rounded enclosure; hand-authored plus symbols from source.','Horizontal arms share length; larger right cross retains a longer lower stem.', '''
self.box('panel',4,10,40,28,5)
self.add_polyline('small-horizontal',(13,26),(16,26),(19,26))
self.add_polyline('small-vertical',(16,23),(16,26),(16,29));self.relate('connect','small-horizontal','small-vertical')
self.add_polyline('large-horizontal',(29,21),(32,21),(35,21))
self.add_polyline('large-vertical',(32,19),(32,21),(32,29));self.relate('connect','large-horizontal','large-vertical')
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
   spec=importlib.util.spec_from_file_location('batch41_'+row['source_uuid'],p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;(d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
   for size in (48,240):
    out=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(out).convert('RGB')).save(d/f'dark-{size}.png')
   print(row['concept'],report.describe(),flush=True)
  except Exception:
   rec['validation_status']='error';rec['error']=traceback.format_exc();(d/'validation.txt').write_text(rec['error']);print(row['concept'],rec['error'],flush=True)
  (d/'review-draft.json').write_text(json.dumps(rec,indent=2))

if __name__=='__main__':run()
