"""A side-view truck faces left with an angular cab, long flat bed, and two wheels. A large tilted dish with a projecting feed stands on supports above the bed.

SQUARE visible bounds (4,4)-(44,44). Left-facing utility truck with a tilted satellite dish on its bed. Cab window and extra dish supports omitted. Full round wheels meet the chassis at shared endpoints. Lucide truck and satellite-dish informed wheel placement and bowl/feed hierarchy; vehicle direction is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd03fdd9c-9e36-4735-9242-c0fcff7593ed'
SOURCE_PATH = 'pictographic-primitives/science/truck satelite_d03fdd9c-9e36-4735-9242-c0fcff7593ed.svg'
AUTHOR = 'gpt-6'

class SatelliteDishTruck(Solo48):
    icon_id = 'satellite-dish-truck'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('truck', 'satellite', 'dish', 'vehicle', 'antenna', 'communication')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('dish-left',(26,6),(22,14),radius_x=10,sweep=False)
        self.add_arc('dish-bottom',(22,14),(32,24),radius_x=10,sweep=False)
        self.add_arc('dish-right',(32,24),(38,22),radius_x=10,sweep=False)
        self.segments('rim',(38,22),(32,14),(26,6))
        self.add_contour('dish','dish-left','dish-bottom','dish-right','rim-1','rim-2',closed=True)
        self.add_line('feed',(32,14),(40,6));self.relate('connect','feed','dish')
        self.add_line('stand',(32,24),(32,28));self.relate('connect','stand','dish')
        self.add_polyline('truck',(10,38),(6,38),(6,28),(14,20),(18,20),(18,28),(32,28),(42,28),(42,38),(38,38))
        self.relate('connect','stand','truck')
        self.circle('wheel-left',14,38,4);self.circle('wheel-right',34,38,4)
        self.add_line('chassis',(18,38),(30,38))
        for n in ['wheel-left','wheel-right']:
            self.relate('connect',n,'truck');self.relate('connect',n,'chassis')
