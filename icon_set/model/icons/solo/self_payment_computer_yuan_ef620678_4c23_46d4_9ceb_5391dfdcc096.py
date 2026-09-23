from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ef620678-4c23-46d4-9ceb-5391dfdcc096'
SOURCE_PATH='icon_set/work/todo-references/self payment computer yuan_ef620678-4c23-46d4-9ceb-5391dfdcc096.svg'
AUTHOR='gpt-6'
PLAN='Payment terminal with yuan Y and one crossbar, plus two rules and stand.'
CONSTRUCTION_REFERENCES='Lucide monitor and japanese-yen: branching Y construction. Source has one currency bar.'
OMISSIONS='No components omitted; source single crossbar preserved.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='self-payment-computer-yuan'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('self', 'payment', 'computer', 'yuan')

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
        self.add_polyline('screen',(6,6),(42,6),(42,34),(24,34),(6,34),closed=True)
        self.add_line('stand',(24,34),(24,42));self.relate('connect','screen','stand')
        self.add_polyline('foot',(16,42),(24,42),(32,42));self.relate('connect','stand','foot')
        for i,y in enumerate((18,26)):self.add_line(f'equals-{i}',(32,y),(34,y))

    def send(self,direction):
        self.box('panel',6,6,36,36,4)
        if direction=='left':
            self.add_polyline('head',(23,17),(16,24),(23,31));self.add_line('shaft',(16,24),(33,24))
        else:
            self.add_polyline('head',(25,17),(32,24),(25,31));self.add_line('shaft',(32,24),(15,24))
        self.relate('connect','head','shaft')

    def build(self):
        self.terminal()
        self.add_polyline('yuan-top',(14,14),(19,21),(24,14))
        self.add_polyline('yuan-stem',(19,21),(19,22),(19,26));self.relate('connect','yuan-top','yuan-stem')
        self.add_polyline('yuan-bar',(14,22),(19,22),(24,22));self.relate('connect','yuan-stem','yuan-bar')

KEYSHAPE_REASON='The complete composition uses centerline extremes (6,6)–(42,42).'
FINAL_REDUCTIONS='No semantic elements omitted. Currency glyph reduced in height; menu rules shortened and screen corner arcs replaced by round joins.'
