from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7a8b5b6b-d72f-42df-9379-3389fd1e33fd'
SOURCE_PATH='icon_set/work/todo-references/self driving car_7a8b5b6b-d72f-42df-9379-3389fd1e33fd.svg'
AUTHOR='gpt-6'
PLAN='Front-facing car with two radio arcs above. Car sides, wheels and headlights mirror around x=24.'
CONSTRUCTION_REFERENCES='Lucide car-front: joined roof, fascia and wheels.'
OMISSIONS='Headlight outlines reduced to dots; wheel outlines reduced to short stems.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='self-driving-car'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('self', 'driving', 'car')

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
        self.box('body',6,26,36,10,4)
        self.add_polyline('roof',(12,26),(16,18),(32,18),(36,26));self.relate('connect','body','roof')
        for i,x in enumerate((12,36)):
         self.add_line(f'wheel-{i}',(x,36),(x,42));self.relate('connect','body',f'wheel-{i}')
        for i,x in enumerate((14,34)):self.add_dot(f'headlight-{i}',(x,31))
        self.add_arc('radio-outer',(14,10),(34,10),radius_x=10,radius_y=4)
        self.add_arc('radio-inner',(18,14),(30,14),radius_x=6,radius_y=3)

KEYSHAPE_REASON='The complete composition uses centerline extremes (6,6)–(42,42).'
FINAL_REDUCTIONS='Headlight outlines reduced to dots; wheel outlines reduced to short stems.'
