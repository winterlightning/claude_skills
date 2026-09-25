"""A large circular lens joins a straight handle extending diagonally toward the lower right. The lens is empty, and its round outline meets the handle directly without a separate collar.

SQUARE visible bounds (4,4)-(44,44); one large circular lens with a lower-right handle. Lucide search informed circle plus direct handle. No detail dropped; handle direction is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aaa50182-047b-43ed-8260-9042ec663a23'
SOURCE_PATH = 'pictographic-primitives/science/explore_aaa50182-047b-43ed-8260-9042ec663a23.svg'
AUTHOR = 'gpt-6'

class PlainMagnifyingGlass(Solo48):
    icon_id = 'plain-magnifying-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('magnifier', 'lens', 'search', 'glass', 'inspection', 'optics')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('lens-main',(30,33),(33,30),radius_x=15,large_arc=True)
        self.add_arc('lens-handle-sector',(33,30),(30,33),radius_x=15)
        self.add_contour('lens','lens-main','lens-handle-sector',closed=True)
        self.add_line('handle',(33,30),(42,42))
        self.relate('connect','handle','lens')
