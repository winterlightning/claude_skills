from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='8d871e7d-03c3-4f02-90aa-ec0ac69a56b5'
SOURCE_PATH='pictographic-primitives/mobile/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg'
AUTHOR='gpt-6'
PLAN='Phone with inward chevrons and hand grip. Lucide hand capsule construction. Finger stack reduced to one broad gripping finger; retain thumb and wrist. Human guide inspected, no head.'
class Drawing(Solo48):
    icon_id='squeeze-sides'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'mobile'
    aliases=()
    keywords=('squeeze', 'sides')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('phone',(18,22),(18,6),(30,6),(30,22),(30,42),(18,42),(18,30))
        self.path('grip',(10,22),[('L',(18,22)),('A',(18,30),4,4,True),('L',(10,30)),('A',(10,22),4,4,True)],True)
        self.relate('connect','phone','grip')
        self.add_polyline('left-arrow',(6,6),(10,10),(6,14))
        self.add_polyline('right-arrow',(42,6),(38,10),(42,14))
        self.path('thumb',(30,22),[('L',(34,22)),('A',(42,30),8,8,True),('L',(42,34))])
        self.add_line('wrist',(30,42),(42,42));self.relate('connect','thumb','phone');self.relate('connect','wrist','phone')

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
