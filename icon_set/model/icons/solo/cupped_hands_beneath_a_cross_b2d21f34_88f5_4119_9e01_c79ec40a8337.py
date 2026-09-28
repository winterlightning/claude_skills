"""Cross above mirrored cupped hand contours. Shared hand dimensions around x24; tangent-continuous rounded finger and palm transitions. Lucide hand informs rounded fingertips; source pose retained with fingers grouped.
Keyshape VRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b2d21f34-88f5-4119-9e01-c79ec40a8337'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/religion hands_b2d21f34-88f5-4119-9e01-c79ec40a8337.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='cupped-hands-beneath-a-cross'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('cupped', 'hands', 'beneath', 'a', 'cross')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        poly('cross-stem',(24,4),(24,12),(24,22));poly('cross-arm',(16,12),(24,12),(32,12));join('cross-stem','cross-arm')
        for j,s in enumerate((-1,1)):
            def p(x,y):return (24+s*x,y)
            path(f'hand-{j}',p(16,44),[('L',p(16,32)),('A',p(8,32),4,4,s==-1),('C',p(4,40),p(8,36),p(4,36)),('L',p(4,44))])
