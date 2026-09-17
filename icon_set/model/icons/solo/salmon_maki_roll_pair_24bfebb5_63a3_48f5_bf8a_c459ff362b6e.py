"""Salmon Maki Sushi Rolls."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24bfebb5-63a3-48f5-bf8a-c459ff362b6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/salmon rolled maki sushi_24bfebb5-63a3-48f5-bf8a-c459ff362b6e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'salmon-maki-roll-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('salmon', 'maki', 'roll', 'pair')

    def build(self):
        # Plan: Supplied maki: two staggered square rolls. Repeated rounded square language; filling simplified to a circular core and topping divisions omitted for clarity. No useful exact Lucide match.
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

        rounded('front',6,20,28,42,5)
        path('back',(16,11),[('A',(21,6),5,5,True),('L',(37,6)),('A',(42,11),5,5,True),('L',(42,28)),('A',(37,33),5,5,True)])
        oval('filling',17,31,2,2)
