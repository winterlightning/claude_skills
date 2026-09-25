'Shopping cart. Straight sloped basket walls, continuous left handle slope, equal round wheels at one baseline. Bounds (6,6)-(42,42).\nConstruction: Lucide shopping-cart: basket rails and equal wheel circles.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2007d848-4f3e-4571-a43a-9e9ad6abf259'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cart 1_2007d848-4f3e-4571-a43a-9e9ad6abf259.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shopping-cart-rounded'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('shopping', 'cart', 'rounded')

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
        poly('handle',(6,6),(12,6),(14,14))
        poly('basket',(14,14),(42,14),(38,28),(18,28),closed=True);join('handle','basket')
        for i,x in enumerate((20,36)):circle(f'wheel-{i}',x,39,3)
