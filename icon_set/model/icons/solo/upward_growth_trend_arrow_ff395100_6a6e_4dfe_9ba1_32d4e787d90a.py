'Upward zigzag trend arrow with equal 45-degree rising and falling segments and a square arrowhead. Bounds (4,10)-(44,38).\nConstruction: Lucide trending-up: straight zigzag diagonals and equal arrowhead arms.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff395100-6a6e-4dfe-9ba1-32d4e787d90a'
SOURCE_PATH = 'pictographic-primitives/other/arrow trend up_ff395100-6a6e-4dfe-9ba1-32d4e787d90a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-growth-trend-arrow'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('upward', 'growth', 'trend', 'arrow')

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
        poly('trend',(4,38),(18,24),(24,30),(44,10))
        poly('head',(28,10),(44,10),(44,26));join('trend','head')
