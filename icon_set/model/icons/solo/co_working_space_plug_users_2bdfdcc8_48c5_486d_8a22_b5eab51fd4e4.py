from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4'
SOURCE_PATH='pictographic-primitives/office/co working space plug users_2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4.svg'
AUTHOR='gpt-6'
PLAN='Two equal user heads radius3 and shoulders; actual detached ink gap4 (head bottom32, shoulder apex40). Human user.svg proportions; Lucide plug prongs separated8. Socket holes omitted for clearance; cords intentionally join side of heads as source.'
class Drawing(Solo48):
    icon_id='co-working-space-plug-users'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'office'
    aliases=()
    keywords=('co', 'working', 'space', 'plug', 'users')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        for i,cx in enumerate((14,34)):
            self.circle(f'head-{i}',cx,29,3)
            self.add_arc(f'shoulders-{i}',(cx-6,42),(cx+6,42),radius_x=6,radius_y=2)
        self.add_polyline('plug',(6,6),(14,6),(14,8),(14,16),(14,18),(6,18),closed=True)
        self.add_polyline('socket',(32,6),(42,6),(42,18),(32,18),closed=True)
        for i,y in enumerate((8,16)):
            self.add_line(f'pin-{i}',(14,y),(20,y));self.relate('connect','plug',f'pin-{i}')
        self.add_polyline('cord-left',(6,18),(6,26),(11,29))
        self.add_polyline('cord-right',(42,18),(42,26),(37,29))
        for a,b in [('cord-left','plug'),('cord-left','head-0'),('cord-right','socket'),('cord-right','head-1')]:self.relate('connect',a,b)

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
