from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='84f3f807-398a-4f6c-9d2e-58805a5192a4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-spoon-and-folk/20260927T142540Z-thuan-mac-1/reference/monitor spoon and folk_84f3f807-398a-4f6c-9d2e-58805a5192a4.svg'
AUTHOR='gpt-6'
PLAN='Landscape monitor with full stand; separate round spoon bowl and two-prong fork with joined stems.'
class Drawing(Solo48):
    icon_id='monitor-spoon-and-folk'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('monitor', 'spoon', 'and', 'folk')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.monitor(4,8,44,32,40)
        self.circle('spoon-bowl',15,19,2)
        self.add_line('spoon-handle',(15,21),(15,23));self.relate('connect','spoon-bowl','spoon-handle')
        self.add_polyline('fork-head',(26,17),(26,20),(30,22),(34,20),(34,17))
        self.add_line('fork-handle',(30,22),(30,23))
        self.relate('connect','fork-head','fork-handle')

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
