from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1e1fac7c-54c5-4468-baea-d2c722f0520d'
SOURCE_PATH='icon_set/work/todo-references/self payment computer pound_1e1fac7c-54c5-4468-baea-d2c722f0520d.svg'
AUTHOR='gpt-6'
PLAN='Payment terminal with pound symbol, two right-hand rules and stand.'
CONSTRUCTION_REFERENCES='Lucide monitor and pound-sterling: round hook, crossbar and foot.'
OMISSIONS='None.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='self-payment-computer-pound'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('self', 'payment', 'computer', 'pound')

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
        self.add_arc('pound-hook',(23,16),(15,16),radius_x=4,sweep=False)
        self.add_polyline('pound-stem',(15,16),(15,21),(15,26));self.relate('connect','pound-hook','pound-stem')
        self.add_arc('pound-turn',(15,26),(12,29),radius_x=3);self.relate('connect','pound-stem','pound-turn')
        self.add_polyline('pound-base',(12,29),(24,29));self.relate('connect','pound-turn','pound-base')
        self.add_polyline('crossbar',(12,21),(15,21),(20,21));self.relate('connect','pound-stem','crossbar')

KEYSHAPE_REASON='The complete composition uses centerline extremes (6,6)–(42,42).'
FINAL_REDUCTIONS='No semantic elements omitted. Larger currency glyph retained for legibility; menu rules shortened and screen corners use round joins.'
