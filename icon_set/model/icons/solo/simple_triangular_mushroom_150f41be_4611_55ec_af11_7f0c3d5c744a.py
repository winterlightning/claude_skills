"""Simple Triangular Mushroom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '150f41be-4611-55ec-af11-7f0c3d5c744a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom_150f41be-4611-55ec-af11-7f0c3d5c744a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-triangular-mushroom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'triangular', 'mushroom')

    def build(self):
        # Plan: Tall triangular mushroom cap with rounded tip and a broad short stalk. Mirrored cap and shared stalk attachment points; no surface detail added. No useful exact Lucide match.
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

        path('cap',(6,27),[('L',(20,8)),('A',(28,8),4,2,True),('L',(42,27)),('L',(30,27)),('L',(18,27)),('L',(6,27))],True)
        path('stem',(18,27),[('L',(17,37)),('C',(24,42),(16,42),(21,42)),('C',(31,37),(27,42),(32,42)),('L',(30,27))]);join('cap','stem')
