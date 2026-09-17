"""Steaming Hot Soup Bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75dfc3e6-5295-5ecc-bf6f-267b14ed090d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pho_75dfc3e6-5295-5ecc-bf6f-267b14ed090d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-hot-soup-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('steaming', 'hot', 'soup', 'bowl')

    def build(self):
        # Plan: Wide soup bowl with three steam trails and a flared foot. Mirrored bowl and shared foot nodes; Lucide soup informs the curved bowl and sparse steam.
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

        path('bowl',(6,24),[('L',(42,24)),('C',(30,34),(40,30),(35,34)),('L',(18,34)),('C',(6,24),(13,34),(8,30))],True)
        poly('foot',(18,34),(14,42),(34,42),(30,34));join('foot','bowl')
        for j,x in enumerate((14,24,34)):path('steam-'+str(j),(x,6),[('C',(x,15),(x-3,9),(x+3,12))])
