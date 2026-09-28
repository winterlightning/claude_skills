'Teacup with flat rim, rounded bowl and right loop handle. Bowl sides tangent to quarter circles. Bounds (4,10)-(44,38).\nConstruction: Lucide coffee: quarter-circle bowl and continuous external handle.\nOmissions: None'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '87cc134f-642b-4561-bbf1-a36a28323ca8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-teacup/20260924T160658Z-thuan-mac/reference/tea_87cc134f-642b-4561-bbf1-a36a28323ca8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-teacup'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rounded', 'teacup')

    def build(self):

        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        path('cup',(4,10),[('L',(32,10)),('L',(32,14)),('L',(32,28)),('A',(18,38),14,10,True),('A',(4,28),14,10,True),('L',(4,10))],True)
        path('handle',(32,14),[('A',(44,21),12,7,True),('A',(32,28),12,7,True)]);join('handle','cup')
