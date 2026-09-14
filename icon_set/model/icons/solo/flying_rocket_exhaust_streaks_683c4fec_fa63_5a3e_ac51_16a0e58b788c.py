"""A rounded rocket points diagonally upper-right with a circular porthole, two angular fins, and a short rear nozzle. Three separate diagonal exhaust streaks trail behind it toward the lower left.

SQUARE visible bounds (4,4)-(44,44); diagonal rocket, angular fins, porthole and three separated exhaust streaks. Porthole reduced to dot and rear nozzle seam omitted. Lucide rocket informed the pointed silhouette. Upper-right flight direction retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '683c4fec-fa63-5a3e-ac51-16a0e58b788c'
SOURCE_PATH = 'pictographic-primitives/science/rocket flying_683c4fec-fa63-5a3e-ac51-16a0e58b788c.svg'
AUTHOR = 'gpt-6'

class FlyingRocketExhaustStreaks(Solo48):
    icon_id = 'flying-rocket-exhaust-streaks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('rocket', 'flight', 'exhaust', 'porthole', 'fin', 'space')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('nose-upper',(22,18),(42,6),radius_x=20,radius_y=12)
        self.add_arc('nose-lower',(42,6),(36,26),radius_x=6,radius_y=20)
        self.segments('tail-body',(36,26),(30,32),(22,24),(22,18))
        self.add_contour('hull','nose-upper','nose-lower','tail-body-1','tail-body-2','tail-body-3',closed=True)
        self.add_polyline('fin-left',(22,18),(16,14),(8,18),(22,24))
        self.add_polyline('fin-right',(36,26),(42,34),(30,42),(30,32))
        self.relate('connect','fin-left','hull');self.relate('connect','fin-right','hull')
        self.add_dot('porthole',(32,18))
        self.add_line('exhaust-left',(6,29),(7,28))
        self.add_line('exhaust-center',(6,42),(14,34))
        self.add_line('exhaust-right',(18,42),(22,38))
