"""Rounded skull and continuous back neck; two rounded mouth-to-throat passages spaced nine units apart.
Keyshape VRECT_L. Shared human user.svg smooth anatomy; supplied anatomical section defines the continuous neck.
Omissions: Minor lip contour omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '116c496d-58c8-4b77-9d43-fdb1d84aa352'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/throat problem_116c496d-58c8-4b77-9d43-fdb1d84aa352.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'head-and-throat-section-116c496d'
    keyshape = Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "health"
    categories = ("health", "primitives")
    aliases=()
    keywords=('head', 'and', 'throat', 'section', '116c496d')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('skull',(8,24),[('L',(12,17)),('C',(26,4),(12,9),(18,4)),('A',(40,18),14,14,True),('L',(40,26)),('C',(39,36),(40,30),(39,33)),('L',(39,44))])
        path('upper-passage',(8,24),[('L',(20,24)),('A',(30,34),10,10,True),('L',(30,44))]);join('skull','upper-passage')
        path('lower-passage',(8,33),[('L',(15,33)),('A',(21,39),6,6,True),('L',(21,44))])
        path('chin',(8,33),[('A',(12,37),4,4,False),('L',(12,44))]);join('chin','lower-passage')

