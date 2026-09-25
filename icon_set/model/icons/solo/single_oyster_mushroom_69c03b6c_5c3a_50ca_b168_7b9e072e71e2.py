"""Single Oyster Mushroom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69c03b6c-5c3a-50ca-b168-7b9e072e71e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom oyster_69c03b6c-5c3a-50ca-b168-7b9e072e71e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-oyster-mushroom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('single', 'oyster', 'mushroom')

    def build(self):
        # Plan: Fan-shaped oyster mushroom with a thick stem and two rising gills. Mirrored fan construction; three gills reduced to two to preserve clearance. No useful exact Lucide match.
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

        path('mushroom',(24,6),[('C',(33,10),(29,6),(29,10)),('C',(42,18),(39,10),(42,14)),('C',(38,28),(42,22),(42,25)),('C',(30,36),(37,31),(31,32)),('A',(24,42),6,6,True),('A',(18,36),6,6,True),('C',(10,28),(17,32),(11,31)),('C',(6,18),(6,25),(6,22)),('C',(15,10),(6,14),(9,10)),('C',(24,6),(19,10),(19,6))],True)
        for j,(a,b) in enumerate((((18,18),(20,25)),((30,18),(28,25)))):line('gill-'+str(j),a,b)
