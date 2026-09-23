from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c8e04970-7ef3-408d-aa2e-0b6ea0ec0b65'
SOURCE_PATH='icon_set/work/todo-references/seat find_c8e04970-7ef3-408d-aa2e-0b6ea0ec0b65.svg'
AUTHOR='gpt-6'
PLAN='Walking person, rightward direction arrow and empty chair. Keep the complete find-seat scene.'
CONSTRUCTION_REFERENCES='Shared human-reference.md/full_body_ref.png: round head and coherent walking limbs; Lucide armchair informs the seat construction.'
OMISSIONS='Outlined person and chair material thickness reduced to coherent strokes; chair foot retained as a baseline.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='seat-find'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('seat', 'find')

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

    def build(self):
        self.circle('head',14,10,4)
        self.add_line('torso',(14,22),(14,32))
        self.add_polyline('arms',(8,28),(14,22),(20,28));self.relate('connect','torso','arms')
        self.add_polyline('legs',(6,42),(14,32),(22,42));self.relate('connect','torso','legs')
        self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
        self.add_polyline('arrowhead',(26,14),(30,18),(26,22))
        self.add_line('arrow-shaft',(23,18),(30,18));self.relate('connect','arrowhead','arrow-shaft')
        self.add_polyline('chair',(40,12),(42,20),(40,34),(30,34))
        self.add_line('chair-base',(30,42),(40,42))

KEYSHAPE_REASON='The complete composition uses centerline extremes (6,6)–(42,42).'
FINAL_REDUCTIONS='Outlined person and chair material thickness reduced to coherent strokes; chair foot retained as a baseline.'
