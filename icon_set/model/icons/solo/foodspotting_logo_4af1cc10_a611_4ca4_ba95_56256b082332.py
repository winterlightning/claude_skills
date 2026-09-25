"""A rounded camera with a raised top and circular lens; omit FOOD lettering and the nested lens ring for clarity; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4af1cc10-a611-4ca4-ba95-56256b082332'
SOURCE_PATH = 'pictographic-primitives/logos/food spotting logo 1_4af1cc10-a611-4ca4-ba95-56256b082332.svg'
AUTHOR = 'gpt-6'

class FoodspottingLogo(Solo48):
    icon_id = 'foodspotting-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('foodspotting', 'food', 'camera', 'logo', 'brand', 'restaurant', 'photo')

    def build(self):
        # Plan: A rounded camera with a raised top and circular lens; omit FOOD lettering and the nested lens ring for clarity; extremes (6,6)-(42,42).
        # Construction reference: Lucide camera original and atomic-debug: rounded housing, raised shoulder and single circular lens.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        def graph(edges):
            for name,a,b in edges: line(name,a,b)
            for i,(name,a,b) in enumerate(edges):
                for other,c,d in edges[:i]:
                    if {a,b}&{c,d}: join(name,other)

        path('camera',(10,14),[('L',(14,14)),('L',(20,6)),('L',(28,6)),('L',(34,14)),('L',(38,14)),('A',(42,18),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,18)),('A',(10,14),4,4,True)],True)
        circle('lens',24,28,5)
