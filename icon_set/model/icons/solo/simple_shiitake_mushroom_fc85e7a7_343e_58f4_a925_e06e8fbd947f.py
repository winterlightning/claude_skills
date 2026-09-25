"""Simple Shiitake Mushroom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc85e7a7-343e-58f4-a925-e06e8fbd947f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom shiitake_fc85e7a7-343e-58f4-a925-e06e8fbd947f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-shiitake-mushroom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'shiitake', 'mushroom')

    def build(self):
        # Plan: Low shiitake cap above a gently bent stem. Cap mirrors around 24; stem bends left as in the reference. Plain cap retained; no useful exact Lucide match.
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

        path('cap',(6,22),[('C',(24,6),(6,13),(14,6)),('C',(42,22),(34,6),(42,13)),('L',(30,22)),('L',(19,22)),('L',(6,22))],True)
        path('stem',(19,22),[('C',(16,36),(19,29),(17,32)),('C',(24,42),(14,42),(20,42)),('C',(29,36),(28,42),(30,39)),('L',(30,22))]);join('stem','cap')
