"""Rice Bowl with Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bfa0217-60fa-4d0e-a2c4-54c7d0e23e6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/rice_6bfa0217-60fa-4d0e-a2c4-54c7d0e23e6e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rice-bowl-upright-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('rice', 'bowl', 'upright', 'chopsticks')

    def build(self):
        # Plan: Lucide soup/salad: round bowl and attached rice mound. Leaning chopsticks at right; short foot removed.
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

        path('bowl',(6,26),[('L',(7,26)),('L',(21,26)),('L',(30,26)),('L',(39,26)),('L',(42,26)),('C',(24,42),(42,36),(33,42)),('C',(6,26),(15,42),(6,36))],True)
        path('rice',(7,26),[('A',(21,26),7,10,True)]);join('rice','bowl')
        line('stick-left',(30,26),(33,6));line('stick-right',(39,26),(42,6));join('stick-left','bowl');join('stick-right','bowl')
