"""Two cupped hands supporting a building, with matched flowing palms.
Plan: Two cupped hands supporting a building, with matched flowing palms.
Construction: Lucide hand original and atoms: smooth palms with rounded fingertip ends; mirrored about x=24.
Omissions: Tiny windows and finger creases omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '8788efae-9ba8-4acc-a2e4-90bca5c7c8d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/real estate favorite hold building_8788efae-9ba8-4acc-a2e4-90bca5c7c8d4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-hands-cupping-a-building'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('two', 'hands', 'cupping', 'a', 'building')

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
        for side in (-1,1):
         x=lambda a:24+side*a
         path('hand'+str(side),(x(7),42),[('C',(x(18),34),(x(7),38),(x(18),40)),('L',(x(18),24))])
         path('thumb'+str(side),(x(18),34),[('C',(x(10),31),(x(14),34),(x(12),31))]);join('hand'+str(side),'thumb'+str(side))
        poly('building',(14,21),(14,12),(24,12),(24,6),(34,12),(34,21),closed=True)
