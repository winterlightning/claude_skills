"""A diagonal writing pencil with a rounded end and triangular sharpened tip. Bounds (6,6)-(42,42); two shaft edges share a diagonal axis and uniform width.
Construction reference: Lucide pencil: diagonal barrel, rounded end and separate tip divider.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86362575-c445-5e6b-a685-a3226f016d8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/content pen_86362575-c445-5e6b-a685-a3226f016d8c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='writing-pencil'
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
        path('pencil',(6,42),[('L',(12,28)),('L',(31,9)),('C',(37,6),(33,7),(35,6)),('A',(42,11),5,5,True),('C',(39,17),(42,13),(41,15)),('L',(20,36)),('L',(6,42))],True)
        line('tip-divider',(12,28),(20,36));join('tip-divider','pencil')
