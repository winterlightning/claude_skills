from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='485264e5-d5d9-4af5-a33a-88ae3ae2126e'
SOURCE_PATH='pictographic-primitives/other/rectangle employee resume_485264e5-d5d9-4af5-a33a-88ae3ae2126e.svg'
AUTHOR='gpt-6'
PLAN='Résumé portrait with right-side text and lower text. Human-reference user.svg: head bottom16, shoulder apex24 =8 centerline/4 ink. Two side marks share an8-unit step; bottom rows reduced from2 to1.'
class Drawing(Solo48):
    icon_id='rectangle-employee-resume'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'employee', 'resume')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('frame',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.circle('person-head',20,14,2)
        self.add_arc('shoulders',(17,26),(23,26),radius_x=3,radius_y=2)
        for i,y in enumerate((16,24)):self.add_line(f'side-{i}',(31,y),(32,y))
        self.add_line('text',(17,35),(31,35))

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
