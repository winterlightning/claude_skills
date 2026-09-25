"""An open horizontal hand beneath three equal streams of running water. Lucide hand informs rounded grouped fingers; droplets construction uses straight repeated marks. Tangent thumb/palm transitions replace sudden bends.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a34cf5c7-6f9d-4929-bade-fa576555a44e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/locker room wash hands 1_a34cf5c7-6f9d-4929-bade-fa576555a44e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hand-under-running-water'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('hand', 'under', 'running', 'water')
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

        path('hand',(6,34),[('L',(16,34)),('C',(22,31),(19,34),(20,33)),('C',(27,28),(24,29),(25,28)),('C',(32,34),(31,28),(34,31)),('L',(36,34)),('A',(42,38),6,4,True),('A',(36,42),6,4,True),('L',(6,42))])
        for j,x in enumerate((16,28,40)):
            line(f'water-{j}',(x,6),(x,8));self.add_dot(f'drop-{j}',(x,17))
