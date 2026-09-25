'Steaming car with raised hood. Connected roof/body silhouette, equal round wheels, raised hood and one steam stroke. Bounds (6,6)-(42,42).\nConstruction: Lucide car: wheels share the body sill and the body stays continuous.\nOmissions: Inset window and second steam wisp omitted for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1beff0b-613f-4495-8b2d-c0b3036fad7e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car repair engine_e1beff0b-613f-4495-8b2d-c0b3036fad7e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-car-with-raised-hood'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('steaming', 'car', 'with', 'raised', 'hood')

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
        path('body',(9,37),[('L',(6,37)),('L',(6,28)),('L',(15,17)),('L',(24,17)),('L',(32,25)),('L',(38,28)),('A',(42,32),4,4,True),('L',(42,37)),('L',(39,37))])
        for n,x in [('rear',14),('front',34)]:circle(n,x,37,5);join(n,'body')
        line('sill',(19,37),(29,37));join('sill','rear');join('sill','front')
        line('hood',(32,25),(42,21));join('hood','body')
        path('steam',(36,6),[('C',(36,13),(31,9),(40,10))])
