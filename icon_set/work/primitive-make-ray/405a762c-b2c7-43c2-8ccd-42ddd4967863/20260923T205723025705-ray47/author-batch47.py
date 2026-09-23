from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROWS=json.loads(Path('/tmp/ray47-204750-unique.json').read_text())
SOURCE_ICON_ID=[r['source_uuid'] for r in ROWS]
SOURCE_PATH=[r['reference_path'] for r in ROWS]
H='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
'''
D=[]
def add(plan,refs,o,b,frame=True):D.append((plan,refs,o,('self.box("frame",6,6,42,42,4)\n' if frame else '')+textwrap.dedent(b).strip()))
add('Square enclosure containing a frontal person with a closed torso and two arm seams.','human_ref/user.svg and full_body_ref.png: circular head, broad smooth shoulders and exact detached gap.','No defining parts omitted.', '''
self.circle('head',24,17,3)
self.add_bezier('torso',(24,28),((18,28),(15,29),(15,32)))
self.add_bezier('right-shoulder',(24,28),((30,28),(33,29),(33,32)))
self.add_polyline('body-base',(15,32),(15,35),(33,35),(33,32))
self.relate('connect','torso','right-shoulder');self.relate('connect','torso','body-base');self.relate('connect','right-shoulder','body-base')
for n,x in [('left',20),('right',28)]:self.add_line(n+'-arm',(x,32),(x,35));self.relate('connect',n+'-arm','body-base')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
for style in ('hangup','phone'):
 add('Rounded square with a curved telephone handset; handset orientation follows the source.','phone: continuous curved handset with shaped grips. The hangup source has no slash.','No defining parts omitted.',f'''
self.add_bezier('handset',(17,15),
    ((19,13),(20,15),(21,18)),
    ((23,21),(20,21),(19,24)),
    ((20,27),(24,30),(27,29)),
    ((29,26),(29,25),(32,27)),
    (({34 if style=='hangup' else 33},28),(35,29),(33,32)),
    ((29,37),(18,29),(15,22)),
    ((13,18),(15,16),(17,15)))
''')
add('Rounded square with a centered plus sign.','square-plus: shared central junction and equal arms.','No parts omitted.', '''
self.add_line('vertical',(24,15),(24,33))
self.add_line('horizontal',(15,24),(33,24));self.relate('connect','vertical','horizontal')
''')
add('Rounded square with three horizontal poll rows, the bottom row shorter.','Simple repeated horizontal strokes inside a canonical rounded square.','No parts omitted.', '''
for i,length in enumerate((18,18,10)):
    y=16+8*i;self.add_line('row-'+str(i),(15,y),(15+length,y))
''')
add('Rounded square containing a circular Q with a diagonal tail.','No exact local Lucide letter match; circular bowl and attached diagonal tail.','No parts omitted.', '''
self.circle('q-bowl',23,23,9)
self.add_line('q-tail',(29,29),(33,33));self.relate('connect','q-bowl','q-tail')
''')
add('Rounded square enclosing a smaller rounded square divided into four quarters.','Shared rectangular grid geometry; central cross joins the inner border.','No parts omitted.', '''
self.box('inner',15,15,33,33,2)
self.add_line('vertical',(24,15),(24,33));self.add_line('horizontal',(15,24),(33,24))
self.relate('connect','vertical','inner');self.relate('connect','horizontal','inner');self.relate('connect','vertical','horizontal')
''')
add('Rounded square containing two matching closing quotation marks.','quote: repeated rounded upper bowls and descending hooked tails.','No parts omitted.', '''
for n,x in [('left',17),('right',31)]:
    self.add_arc(n+'-top',(x-3,19),(x+3,19),radius_x=3)
    self.add_bezier(n+'-outside',(x+3,19),((x+3,26),(x+2,30),(x-1,32)))
    self.add_line(n+'-tip',(x-1,32),(x-3,29))
    self.add_bezier(n+'-inside',(x-3,29),((x,27),(x,24),(x,22)))
    self.add_arc(n+'-bowl',(x,22),(x-3,19),radius_x=3)
    self.add_contour(n,n+'-top',n+'-outside',n+'-tip',n+'-inside',n+'-bowl',closed=True)
''')
add('Rightward arrow inside a square enclosure with two chamfered right corners.','square-arrow-up: joined arrow construction; source owns asymmetric tag-like enclosure.','No parts omitted.', '''
self.add_polyline('frame',(6,6),(30,6),(42,18),(42,30),(30,42),(6,42),closed=True)
self.add_line('shaft',(15,24),(32,24));self.add_polyline('head',(25,17),(32,24),(25,31));self.relate('connect','shaft','head')
''',False)
add('Rounded square with three horizontal sliders and staggered circular knobs.','sliders-horizontal: shared track lengths, repeated knobs and staggered settings.','No parts omitted.', '''
for i,x in enumerate((21,27,20)):
    y=16+8*i
    self.circle('knob-'+str(i),x,y,2)
    self.add_line('left-'+str(i),(15,y),(x-2,y));self.add_line('right-'+str(i),(x+2,y),(33,y))
    self.relate('connect','knob-'+str(i),'left-'+str(i));self.relate('connect','knob-'+str(i),'right-'+str(i))
''')
add('Rounded square enclosing a degree mark and the letter F.','No exact local Lucide typography match; F is hand-authored with shared stem intersections.','Reconstructed the tiny source degree mark as a small circular degree sign.', '''
self.circle('degree',16,17,2)
self.add_polyline('f',(26,34),(26,16),(34,16))
self.add_line('f-bar',(26,25),(32,25));self.relate('connect','f','f-bar')
''')
add('Rounded square enclosing a degree mark and the letter C.','No exact local Lucide typography match; circular C arc and degree dot.','Reconstructed the tiny source degree mark as a degree dot.', '''
self.add_dot('degree',(14,15))
self.add_arc('c',(32,16),(32,32),radius_x=10,large_arc=True,sweep=False)
''')
add('Rounded square with two upward arrows above a shared horizontal baseline.','square-arrow-up: joined shaft/head; arrows share size and baseline.','No parts omitted.', '''
for n,x in [('left',18),('right',30)]:
    self.add_line(n+'-shaft',(x,16),(x,27))
    self.add_polyline(n+'-head',(x-4,20),(x,16),(x+4,20));self.relate('connect',n+'-shaft',n+'-head')
self.add_line('baseline',(15,35),(33,35))
''')
add('Rightward arrow in a rounded square, matching the supplied artwork despite the square-u filename.','square-plus/arrow construction: canonical enclosure and connected arrow.','No parts omitted; no U is present in source.', '''
self.add_line('shaft',(15,24),(33,24));self.add_polyline('head',(25,16),(33,24),(25,32));self.relate('connect','shaft','head')
''')
add('Bent upward arrow: horizontal approach from left turns upward inside a rounded square.','square-arrow-up: equal head wings; rounded elbow on the shaft.','No parts omitted.', '''
self.add_line('shaft-bottom',(15,33),(21,33))
self.add_arc('elbow',(21,33),(24,30),radius_x=3,sweep=False)
self.add_line('shaft-top',(24,30),(24,15));self.add_contour('shaft','shaft-bottom','elbow','shaft-top')
self.add_polyline('head',(18,21),(24,15),(30,21));self.relate('connect','shaft','head')
''')
for n in ('up-right','up'):
 add('Upward arrow in a rounded square; source direction is vertical.','square-arrow-up: shared central axis and equal arrowhead wings.','No parts omitted; tiny shaft/head discontinuity in source is joined coherently.', '''
self.add_line('shaft',(24,33),(24,15));self.add_polyline('head',(16,23),(24,15),(32,23));self.relate('connect','shaft','head')
''')
add('Rounded square with a circular user head and a smooth closed shoulder dome.','human_ref/user.svg and full_body_ref.png: circular head, symmetric shoulders and exact detached gap.','No parts omitted.', '''
self.circle('head',24,17,3)
self.add_arc('torso',(24,28),(15,34),radius_x=9,radius_y=6,sweep=False)
self.add_line('base',(15,34),(33,34))
self.add_arc('right-shoulder',(33,34),(24,28),radius_x=9,radius_y=6,sweep=False)
self.add_contour('body','torso','base','right-shoulder',closed=True)
self.mark_human_figure('user',head='head',torso='torso',torso_junction='start')
''')
add('Rounded square with a check mark, matching the supplied square-v artwork.','Joined two-segment check with deliberate asymmetry.','No parts omitted; source is a check rather than a letter V.', '''
self.add_polyline('check',(15,24),(22,31),(33,17))
''')
add('Upward arrow emerging through the open top of a squared enclosure.','square-arrow-up: coherent arrow shaft and head; open frame follows source.','No parts omitted.', '''
self.add_polyline('frame',(14,20),(6,20),(6,42),(42,42),(42,20),(34,20))
self.add_line('shaft',(24,30),(24,6));self.add_polyline('head',(18,12),(24,6),(30,12));self.relate('connect','shaft','head')
''',False)
for r,(plan,refs,o,b) in zip(ROWS,D):
 out=Path(r['out']);r.update(keyshape='SQUARE',plan=plan,construction_references=refs,omissions=o)
 src=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {r['source_uuid']!r}
SOURCE_PATH = {r['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Plan: {plan}
# References: {refs}
# Reduction: {o}

class AuthoredIcon(Solo48):
    icon_id = {r['icon_id']!r}
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(r['concept'].split())!r}

    def build(self):
'''+textwrap.indent(b,'        ')+'\n'+H
 r['module']=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py';(out/r['module']).write_text(src)
Path('/tmp/ray47-204750-unique.json').write_text(json.dumps(ROWS,indent=2));(Path(ROWS[0]['out'])/'author-batch47.py').write_text(Path(__file__).read_text());print('Authored',len(D))
