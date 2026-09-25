'Sydney Opera House. Three distinct curved shells rise from a straight podium, tallest at the center. Bounds (4,8)-(44,40).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: Smallest rear shell omitted to retain clear separation.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c7364773-fda3-4a38-a60d-6690249945af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/sydney opera house 1_c7364773-fda3-4a38-a60d-6690249945af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sydney-opera-house-shells'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitive", "primitives")
    aliases = ()
    keywords = ('sydney', 'opera', 'house', 'shells')

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
        poly('podium',(4,32),(14,32),(26,32),(40,32),(44,32),(44,40),(4,40),closed=True)
        path('left-shell',(14,32),[('L',(8,18)),('C',(26,32),(17,19),(23,24))]);join('left-shell','podium')
        path('middle-shell',(26,32),[('L',(20,8)),('C',(34,24),(30,10),(34,18))]);join('middle-shell','podium')
        path('right-shell',(26,32),[('C',(34,24),(28,28),(30,25)),('C',(44,22),(37,23),(40,22)),('L',(40,32))]);join('right-shell','podium');join('right-shell','middle-shell')
