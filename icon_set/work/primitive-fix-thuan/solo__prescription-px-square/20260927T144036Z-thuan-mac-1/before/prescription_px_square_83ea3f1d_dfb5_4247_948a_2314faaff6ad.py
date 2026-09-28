from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='83ea3f1d-dfb5-4247-948a-2314faaff6ad'
SOURCE_PATH='pictographic-primitives/other/prescription px square_83ea3f1d-dfb5-4247-948a-2314faaff6ad.svg'
AUTHOR='gpt-6'
PLAN='Taller rounded enclosure opens distance between R bowl and rising X arm; shared X intersection at27,31. Hand-authored Rx, Lucide rounded enclosure vocabulary. No content omitted.'
class Drawing(Solo48):
    icon_id='prescription-px-square'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('prescription', 'px', 'square')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rect('frame',8,4,40,44,4)
        self.add_polyline('r-stem',(17,35),(17,22),(17,14),(25,14))
        self.add_arc('r-bowl',(25,14),(25,22),radius_x=4)
        self.add_line('r-return',(25,22),(17,22))
        self.relate('connect','r-stem','r-bowl');self.relate('connect','r-bowl','r-return');self.relate('connect','r-return','r-stem')
        self.add_polyline('rx-down',(25,22),(27,31),(31,35))
        self.add_polyline('rx-up',(23,33),(27,31),(31,29))
        self.relate('connect','rx-down','rx-up');self.relate('connect','rx-down','r-bowl');self.relate('connect','rx-down','r-return')

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
