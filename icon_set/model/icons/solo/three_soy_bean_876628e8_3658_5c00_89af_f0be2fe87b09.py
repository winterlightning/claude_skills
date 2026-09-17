"""Three Soy Beans."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '876628e8-3658-5c00-89af-f0be2fe87b09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/black bean_876628e8-3658-5c00-89af-f0be2fe87b09.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-soy-bean'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('three', 'soy', 'bean')

    def build(self):
        # Plan: Three separate soybeans in a loose triangular arrangement. One indented bean and two smooth ovals preserve the varied shapes. Interior crease omitted because the three small bodies need clear interiors; Lucide bean informs the concave side.
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

        path('left',(12,22),[('C',(18,28),(17,22),(18,25)),('C',(14,34),(18,31),(14,30)),('C',(12,42),(14,39),(15,42)),('C',(6,34),(7,42),(6,38)),('C',(12,22),(6,28),(7,22))],True)
        oval('upper',30,12,12,6)
        oval('lower',36,34,6,8)
