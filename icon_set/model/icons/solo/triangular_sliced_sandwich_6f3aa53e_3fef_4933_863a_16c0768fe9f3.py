"""Triangular Sliced Sandwich."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f3aa53e-3fef-4933-863a-16c0768fe9f3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sandwich_6f3aa53e-3fef-4933-863a-16c0768fe9f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangular-sliced-sandwich'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('triangular', 'sliced', 'sandwich')

    def build(self):
        # Plan: Triangular sandwich with broad bread face and scalloped filling along the lower diagonal. Shared layer corners preserve the diagonal cut. Lucide sandwich informs the plain bread and reduced filling layer; texture simplified.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('bread',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('filling',(6,10),[('L',(6,24)),('C',(12,32),(6,29),(8,32)),('C',(22,40),(16,32),(16,40)),('C',(31,42),(26,40),(27,42)),('C',(38,38),(35,42),(36,40))]);join('filling','bread')
        line('texture',(28,18),(31,15))
