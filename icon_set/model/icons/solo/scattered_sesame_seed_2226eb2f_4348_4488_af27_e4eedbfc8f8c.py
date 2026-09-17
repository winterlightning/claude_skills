"""Scattered Sesame Seeds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2226eb2f-4348-4488-af27-e4eedbfc8f8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sesame_2226eb2f-4348-4488-af27-e4eedbfc8f8c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scattered-sesame-seed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('scattered', 'sesame', 'seed')

    def build(self):
        # Plan: Five separate teardrop sesame seeds in a loose quincunx. One seed definition owns the swollen body and pointed tip; tiny interior mark omitted. No useful exact Lucide match.
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

        for j,(x,y) in enumerate(((10,12),(38,12),(24,24),(10,36),(38,36))):
         path(f'seed-{j}',(x,y-6),[('C',(x+4,y+1),(x+1,y-3),(x+4,y-2)),('C',(x,y+6),(x+4,y+4),(x+2,y+6)),('C',(x-4,y+1),(x-2,y+6),(x-4,y+4)),('C',(x,y-6),(x-4,y-2),(x-1,y-3))],True)
