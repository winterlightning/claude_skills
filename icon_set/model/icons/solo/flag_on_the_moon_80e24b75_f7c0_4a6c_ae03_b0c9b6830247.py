"""A rectangular flag stands on a vertical pole planted in a curved lunar surface. A small oval crater lies below the pole, and a large plain celestial disk hangs above-left.

SQUARE visible bounds (4,4)-(44,44); planted flag, curved lunar horizon, crater and distant body. Crater reduced to its near rim and distant disk reduced for clearance. No useful exact Lucide match. Scene asymmetry retains flag-right and celestial-body-left placement.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80e24b75-f7c0-4a6c-ae03-b0c9b6830247'
SOURCE_PATH = 'pictographic-primitives/science/moon flag_80e24b75-f7c0-4a6c-ae03-b0c9b6830247.svg'
AUTHOR = 'gpt-6'

class FlagOnTheMoon(Solo48):
    icon_id = 'flag-on-the-moon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('moon', 'flag', 'crater', 'lunar', 'space', 'exploration')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.circle('distant-body',12,12,6)
        self.add_polyline('pole',(28,12),(28,24),(28,30))
        self.add_polyline('flag',(28,12),(42,12),(42,24),(28,24))
        self.relate('connect','flag','pole')
        self.add_arc('ground-left',(6,32),(28,30),radius_x=36,radius_y=8)
        self.add_arc('ground-right',(28,30),(42,32),radius_x=36,radius_y=8)
        self.relate('connect','ground-left','pole');self.relate('connect','ground-right','pole');self.relate('connect','ground-left','ground-right')
        self.add_arc('crater',(24,40),(32,40),radius_x=4,radius_y=2,sweep=False)
