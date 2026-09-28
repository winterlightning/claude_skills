"""A diagonal pen with a rounded cap, pointed nib and parallel return clip. Bounds (6,6)-(42,42). Shaft sides and clip follow the same diagonal direction.
Construction reference: Lucide pen and pencil: rounded diagonal cap and consistent barrel edges.
Omissions: Fine cap seam omitted to retain clip clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5bf3a0a-1b41-50cf-804b-aa24a6466f2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/content pen_e5bf3a0a-1b41-50cf-804b-aa24a6466f2e.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='writing-pen-with-clip'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "content"
    categories = ("primitives", "content")
    aliases=()
    keywords=('content', 'pen')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('pen',(6,42),[('L',(12,27)),('L',(31,8)),('C',(36,6),(33,6),(34,6)),('A',(42,12),6,6,True),('C',(40,16),(42,14),(41,15)),('L',(21,35)),('C',(6,42),(16,39),(11,41))],True)
        path('clip',(34,22),[('L',(38,26)),('A',(38,32),4,4,True),('L',(29,41))]);join('pen','clip')
