from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='fea7afa8-61b7-411c-860f-fcb3e2894cf6'
SOURCE_PATH='pictographic-primitives/other/preferences_fea7afa8-61b7-411c-860f-fcb3e2894cf6.svg'
AUTHOR='gpt-6'
PLAN='Lucide settings: radial teeth around shared hub. Panel moved left to give half gear a wider annulus; mirror gear around y24, paired panel marks. No defining components omitted.'
class Drawing(Solo48):
    icon_id='preferences'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('preferences',)
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('panel',(24,6),(24,9),(24,18),(24,30),(24,39),(24,42),(6,42),(6,6),closed=True)
        for i,y in enumerate((14,30)):self.add_line(f'mark-{i}',(14,y),(14,y+4))
        self.add_polyline('gear',(24,9),(30,10),(34,6),(40,12),(36,16),(42,18),(42,30),(36,32),(40,36),(34,42),(30,38),(24,39))
        self.add_arc('hub',(24,18),(24,30),radius_x=6)
        self.relate('connect','panel','gear');self.relate('connect','panel','hub')

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
