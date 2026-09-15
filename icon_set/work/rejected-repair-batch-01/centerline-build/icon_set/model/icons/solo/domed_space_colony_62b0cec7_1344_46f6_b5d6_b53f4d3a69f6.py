"""Two tall angular building faces rise from a shared platform inside a rounded protective dome. One tower is taller and slopes to a central ridge; a horizontal base extends beyond the dome's sides.

HRECT_XL visible extremes (2,6)-(46,42); dome and two unequal towers kept as intrinsic habitat structure. Duplicate platform rim dropped. No useful Lucide exact match; intentional unequal towers.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62b0cec7-1344-46f6-b5d6-b53f4d3a69f6'
SOURCE_PATH = 'pictographic-primitives/science/colony_62b0cec7-1344-46f6-b5d6-b53f4d3a69f6.svg'
AUTHOR = 'gpt-6'

class DomedSpaceColony(Solo48):
    icon_id = 'domed-space-colony'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('colony', 'dome', 'building', 'space', 'habitat', 'settlement')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('dome',(4,28),(44,28),radius_x=20,radius_y=20)
        self.add_line('wall-left',(4,40),(4,28))
        for i,(a,b) in enumerate(zip((44,33,24,15),(33,24,15,4))):
            self.add_line(f'base-{i}',(a,40),(b,40))
        self.add_line('wall-right',(44,28),(44,40))
        self.add_contour('habitat','dome','wall-right','base-0','base-1','base-2','base-3','wall-left',closed=True)
        self.add_polyline('towers',(15,40),(15,25),(24,18),(24,26),(24,40))
        self.add_polyline('short-tower',(24,26),(33,31),(33,40))
        self.relate('connect','towers','habitat')
        self.relate('connect','short-tower','habitat')
        self.relate('connect','towers','short-tower')
