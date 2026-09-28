"""Ramen Bowl with Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e320bcf-f02f-5659-b42d-7ea2762d83bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/asian food noodles_0e320bcf-f02f-5659-b42d-7ea2762d83bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ramen-bowl-raised-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('ramen', 'bowl', 'raised', 'chopsticks')

    def build(self):
        # Plan: Lucide soup: broad rim and single rounded bowl. Lifted noodles and chopsticks remain asymmetric; food portions and foot omitted for clearance.
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

        path('bowl',(6,26),[('L',(18,26)),('L',(28,26)),('L',(42,26)),('C',(24,42),(42,35),(34,42)),('C',(6,26),(14,42),(6,35))],True)
        path('noodles',(18,26),[('L',(18,6)),('L',(28,6)),('L',(28,26))]);join('noodles','bowl')
        line('stick-top',(28,6),(42,6));join('stick-top','noodles')
        line('stick-bottom',(28,14),(42,14));join('stick-bottom','noodles')
