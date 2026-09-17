"""Floor Plan with Dimensions.

Plan: SQUARE (6,6)-(42,42). Three unequal rooms in a rounded plan at lower
right; horizontal and vertical double-headed dimension arrows above and left.
Shared grid owns room partitions and dimension endpoints. Lucide ruler provides
measurement construction; the original owns the orthogonal dimension layout.
Reduction: three rooms retain varied subdivision without narrow extra rooms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ca2f2ef-216c-4cf8-b821-70f0289c61a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/construction/real estate dimensions block_2ca2f2ef-216c-4cf8-b821-70f0289c61a3.svg'
AUTHOR = "gpt-6"

class FloorPlanWithDimensions(Solo48):
    icon_id = 'floor-plan-with-dimensions'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('floor', 'plan', 'with', 'dimensions')

    def build(self):
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path("plan",(26,22),[("L",(32,22)),("L",(38,22)),("A",(42,26),4,4,True),("L",(42,32)),("L",(42,38)),("A",(38,42),4,4,True),("L",(32,42)),("L",(26,42)),("A",(22,38),4,4,True),("L",(22,26)),("A",(26,22),4,4,True)],True)
        self.add_polyline("rooms",(32,22),(32,32),(32,42))
        self.add_line("partition",(32,32),(42,32))
        self.relate("connect","rooms","plan")
        self.relate("connect","partition","plan")
        self.relate("connect","rooms","partition")
        self.add_line("width",(22,9),(42,9))
        self.add_polyline("width-left",(25,6),(22,9),(25,12))
        self.add_polyline("width-right",(39,6),(42,9),(39,12))
        for n in ("width-left","width-right"):self.relate("connect","width",n)
        self.add_line("height",(9,22),(9,42))
        self.add_polyline("height-top",(6,25),(9,22),(12,25))
        self.add_polyline("height-bottom",(6,39),(9,42),(12,39))
        for n in ("height-top","height-bottom"):self.relate("connect","height",n)
