"""A circular pulley hangs from a horizontal support, with a square weight suspended on a vertical rope at its left. The rope on the right slopes downward and ends in an arrow indicating the pull direction.

SQUARE visible bounds (4,4)-(44,44); overhead support, pulley, suspended square weight and arrow at rope end. Arrow depicts the physical pull direction, not a separate status badge. No useful Lucide exact match; left weight/right pull arrangement retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e80a70b1-266d-5b86-9dec-2937b25cb7bf'
SOURCE_PATH = 'pictographic-primitives/science/physics law_e80a70b1-266d-5b86-9dec-2937b25cb7bf.svg'
AUTHOR = 'gpt-6'

class PulleyAndHangingWeight(Solo48):
    icon_id = 'pulley-and-hanging-weight'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('pulley', 'weight', 'rope', 'force', 'physics', 'mechanics')

    def segments(self, name, *points):
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'{name}-{i}', a, b)

    def circle(self, name, x, y, r):
        points = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        """Lower the suspended weight to separate its top edge from the pulley rim."""
        self.add_polyline('support', (6, 6), (24, 6), (42, 6))
        self.add_line('hanger', (24, 6), (24, 14))
        self.circle('pulley', 24, 20, 6)
        self.relate('connect', 'hanger', 'support')
        self.relate('connect', 'hanger', 'pulley')
        self.add_line('rope-left', (18, 20), (16, 34))
        self.add_polyline('weight', (6, 34), (16, 34), (26, 34), (26, 42), (6, 42), closed=True)
        self.relate('connect', 'rope-left', 'pulley')
        self.relate('connect', 'rope-left', 'weight')
        self.add_line('rope-right', (30, 20), (42, 36))
        self.add_polyline('pull-arrow', (34, 34), (42, 36), (42, 28))
        self.relate('connect', 'rope-right', 'pulley')
        self.relate('connect', 'rope-right', 'pull-arrow')
