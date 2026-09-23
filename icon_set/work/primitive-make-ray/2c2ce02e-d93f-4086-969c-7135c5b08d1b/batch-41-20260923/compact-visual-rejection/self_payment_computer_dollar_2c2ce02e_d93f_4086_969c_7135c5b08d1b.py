from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2c2ce02e-d93f-4086-969c-7135c5b08d1b'
SOURCE_PATH='icon_set/work/todo-references/self payment computer dollar_2c2ce02e-d93f-4086-969c-7135c5b08d1b.svg'
AUTHOR='gpt-6'
PLAN='Payment terminal with dollar symbol at left and two equality/menu rules at right, supported by a stand.'
CONSTRUCTION_REFERENCES='Lucide monitor: screen and stand; dollar-sign: S contour crossed by vertical stem.'
OMISSIONS='No currency or rule omitted.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='self-payment-computer-dollar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('self', 'payment', 'computer', 'dollar')

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
        self.add_bezier('dollar',(22,17),((21,16),(19,16),(18,16)),((13,16),(13,19),(18,20)),((24,21),(24,24),(18,24)),((16,24),(15,24),(14,23)))
        self.add_polyline('dollar-stem',(18,14),(18,16),(18,20),(18,24),(18,26));self.relate('connect','dollar','dollar-stem')
