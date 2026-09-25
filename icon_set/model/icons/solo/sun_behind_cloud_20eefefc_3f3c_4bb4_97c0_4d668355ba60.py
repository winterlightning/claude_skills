"""Sun behind a broad cloud with tangent-continuous rounded lobes.
Plan: Sun behind a broad cloud with tangent-continuous rounded lobes.
Construction: Lucide cloud-sun: separate sun arc and soft cloud lobes.
Omissions: Reduced ray count to one diagonal ray for required spacing."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '20eefefc-3f3c-4bb4-97c0-4d668355ba60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sun cloud_20eefefc-3f3c-4bb4-97c0-4d668355ba60.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sun-behind-cloud'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('sun', 'behind', 'cloud')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('cloud',(14,42),[('A',(6,34),8,8,True),('A',(14,26),8,8,True),('C',(24,22),(18,26),(16,22)),('C',(34,26),(32,22),(30,26)),('A',(42,34),8,8,True),('A',(34,42),8,8,True),('L',(14,42))],True)
        path('sun',(6,14),[('A',(22,14),8,8,True)])
        line('ray',(34,8),(36,6))
