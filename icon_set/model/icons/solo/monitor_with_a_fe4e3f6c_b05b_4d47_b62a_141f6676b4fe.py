from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='fe4e3f6c-b05b-4d47-b62a-141f6676b4fe'
SOURCE_PATH='pictographic-primitives/other/monitor with a_fe4e3f6c-b05b-4d47-b62a-141f6676b4fe.svg'
AUTHOR='gpt-6'
PLAN='Lucide monitor. A legs mirrored about24; enlarge triangular counter and move crossbar lower. No defining part omitted.'
class Drawing(Solo48):
    icon_id='monitor-with-a'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('monitor', 'with', 'a')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.monitor(8,4,40,36,44)
        self.add_polyline('a-left',(17,27),(18,25),(24,13))
        self.add_polyline('a-right',(24,13),(30,25),(31,27))
        self.add_line('a-bar',(18,25),(30,25))
        self.relate('connect','a-left','a-right','a-bar')

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
