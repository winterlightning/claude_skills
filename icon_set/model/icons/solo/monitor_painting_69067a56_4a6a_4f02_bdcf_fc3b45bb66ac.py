from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='69067a56-4a6a-4f02-bdcf-fc3b45bb66ac'
SOURCE_PATH='pictographic-primitives/other/monitor painting_69067a56-4a6a-4f02-bdcf-fc3b45bb66ac.svg'
AUTHOR='gpt-6'
PLAN='Wider screen; Lucide palette kidney curve and monitor vocabulary. Omit pigment dots and horizontal foot bar. Brush bristle outline reduced to a round head with a joined handle.'
class Drawing(Solo48):
    icon_id='monitor-painting'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('monitor', 'painting')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('screen',(4,8),(44,8),(44,36),(24,36),(4,36),closed=True)
        self.add_line('stand',(24,36),(24,40));self.relate('connect','screen','stand')
        self.path('palette',(19,17),[('A',(13,22),6,5,False),('A',(19,27),6,5,False),('B',(24,25),(23,27),(24,27)),('B',(23,22),(24,23),(23,24)),('B',(19,17),(25,18),(23,17))],True)
        self.circle('brush-head',34,18,2)
        self.add_line('brush-handle',(34,20),(33,28));self.relate('connect','brush-head','brush-handle')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start;members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='B':self.add_bezier(eid,at,(*args,end))
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,q=4):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)

    def monitor(self,l=6,t=6,r=42,b=34,foot=42):
        q=4
        self.path('screen',(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(24,b)),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        self.add_line('stand',(24,b),(24,foot))
        self.add_polyline('foot',(16,foot),(24,foot),(32,foot))
        self.relate('connect','stand','screen');self.relate('connect','stand','foot')
