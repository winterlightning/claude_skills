"""Left-facing upright duck: round head, long neck, swept breast and broad body. Lucide bird informs coherent curved silhouette and equal legs. Omit tiny eye and wing to keep open negative space. Deliberate directional asymmetry.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c9adb3c-aebd-46fe-9aef-76d1c1639608'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bog_5c9adb3c-aebd-46fe-9aef-76d1c1639608.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='upright-duck-with-long-neck'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('upright', 'duck', 'with', 'long', 'neck')
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

        path('duck',(12,14),[('A',(24,14),6,8,True),('L',(24,22)),('A',(28,26),4,4,False),('L',(42,26)),('C',(32,36),(42,33),(38,36)),('L',(22,36)),('C',(12,28),(16,36),(12,33)),('C',(15,20),(12,25),(14,22)),('C',(12,14),(13,19),(12,17))],True)
        line('beak',(6,14),(12,14));join('beak','duck')
        for x in (22,32):line(f'leg-{x}',(x,36),(x,42));join(f'leg-{x}','duck')
