"""Three heart-shaped leaves joined at a common centre and a curved lower stem. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Three heart-shaped leaves joined at a common centre and a curved lower stem. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Three-Leaf Clover: Three heart-shaped leaves meet at a shared central junction, pointing upward, left, and right. A narrow curved stem descends from the junction beneath the spreading leaves.\n\nConstruction: A single trefoil outline has three rounded lobes and a separate curved stem sharing its base.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '15eae920-a828-4e82-80ae-2bcb9cd7a2f2'
SOURCE_PATH = 'pictographic-primitives/state/clover_15eae920-a828-4e82-80ae-2bcb9cd7a2f2.svg'
AUTHOR = 'gpt-6'

class ThreeLeafCloverVariant2(SourceFaithfulSideSub):
    icon_id = 'three-leaf-clover-v2'
    variant_of = 'three-leaf-clover'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('leaf', 'clover', 'heart', 'shaped', 'leaves', 'meet', 'shared', 'central')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Three heart-shaped leaves joined at a common centre and a curved lower stem."""
        self.add_bezier('tl', (16, 16), ((12, 12), (8, 10), (8, 8)))
        self.add_bezier('tla', (8, 8), ((6, 4), (8, 2), (12, 2)))
        self.add_bezier('tnl', (12, 2), ((14, 2), (15, 4), (16, 6)))
        self.add_bezier('tnr', (16, 6), ((17, 4), (18, 2), (20, 2)))
        self.add_bezier('tra', (20, 2), ((24, 2), (26, 4), (24, 8)))
        self.add_bezier('tr', (24, 8), ((24, 10), (20, 12), (16, 16)))
        self.add_contour('top', 'tl', 'tla', 'tnl', 'tnr', 'tra', 'tr', closed=True)
        self.add_bezier('lt', (16, 16), ((9, 12), (2, 5), (2, 10)))
        self.add_bezier('ln', (2, 10), ((2, 13), (4, 15), (6, 16)))
        self.add_bezier('lb', (6, 16), ((4, 17), (2, 19), (2, 22)))
        self.add_bezier('le', (2, 22), ((2, 28), (10, 22), (16, 16)))
        self.add_contour('left', 'lt', 'ln', 'lb', 'le', closed=True)
        self.add_bezier('rt', (16, 16), ((23, 12), (30, 5), (30, 10)))
        self.add_bezier('rn', (30, 10), ((30, 13), (28, 15), (26, 16)))
        self.add_bezier('rb', (26, 16), ((28, 17), (30, 19), (30, 22)))
        self.add_bezier('re', (30, 22), ((30, 28), (22, 22), (16, 16)))
        self.add_contour('right', 'rt', 'rn', 'rb', 're', closed=True)
        self.add_bezier('stem', (16, 16), ((16, 24), (16, 27), (13, 30)))
        for a, b in [('top', 'left'), ('top', 'right'), ('left', 'right'), ('stem', 'top'), ('stem', 'left'), ('stem', 'right')]:
            self.relate('connect', a, b)

def box(s, n, l, t, r, b, k=3):
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
