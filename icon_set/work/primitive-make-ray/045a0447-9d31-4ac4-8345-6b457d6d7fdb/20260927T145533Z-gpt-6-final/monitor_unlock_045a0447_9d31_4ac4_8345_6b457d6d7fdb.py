from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='045a0447-9d31-4ac4-8345-6b457d6d7fdb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-unlock/20260927T142540Z-thuan-mac-1/reference/monitor unlock_045a0447-9d31-4ac4-8345-6b457d6d7fdb.svg'
AUTHOR="gpt-6"
PLAN='Monitor with full pedestal and a compact solid lock bar below a visibly open shackle.'
class Drawing(Solo48):
    icon_id='monitor-unlock'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('monitor', 'unlock')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.monitor(8,4,40,36,44)
        # Solid lock bar gives the open shackle enough breathing room.
        self.add_line('body-left',(18,27),(20,27))
        self.add_line('body-right',(20,27),(30,27))
        self.add_contour('lock-body','body-left','body-right')
        self.add_line('shackle-stem',(20,27),(20,18))
        self.add_arc('shackle-arch',(20,18),(28,18),radius_x=4)
        self.add_contour('open-shackle','shackle-stem','shackle-arch')
        self.relate('connect','lock-body','open-shackle')

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
