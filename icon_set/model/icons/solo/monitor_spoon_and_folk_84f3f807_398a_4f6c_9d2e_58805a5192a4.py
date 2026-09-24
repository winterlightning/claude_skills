from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='84f3f807-398a-4f6c-9d2e-58805a5192a4'
SOURCE_PATH='pictographic-primitives/other/monitor spoon and folk_84f3f807-398a-4f6c-9d2e-58805a5192a4.svg'
AUTHOR='gpt-6'
PLAN='Lucide monitor; circular spoon bowl with joined handle and open knife blade contour. Omit rear blade line to remove tiny enclosed wedge, retaining curved cutting edge and handle.'
class Drawing(Solo48):
    icon_id='monitor-spoon-and-folk'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('monitor', 'spoon', 'and', 'folk')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.monitor()
        self.circle('spoon-bowl',18,18,3)
        self.add_line('spoon-handle',(18,21),(18,25));self.relate('connect','spoon-bowl','spoon-handle')
        self.path('knife',(30,15),[('B',(33,22),(32,17),(33,20)),('L',(30,22)),('L',(30,25))])

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
