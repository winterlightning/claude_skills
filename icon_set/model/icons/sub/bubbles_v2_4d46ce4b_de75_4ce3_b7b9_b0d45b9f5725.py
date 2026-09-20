"""Two circular bubbles with the original unequal sizes and diagonal tangency. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Two circular bubbles with the original unequal sizes and diagonal tangency. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Bubbles: A large circular bubble touches a smaller circle at its upper-right edge. Both interiors are empty, and the two rounded outlines meet without a separate action or status mark.\n\nConstruction: Two round bubbles with unequal radii; a clear gap replaces the source overlap.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725'
SOURCE_PATH = 'pictographic-primitives/state/bubble_4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725.svg'
AUTHOR = 'gpt-6'

class BubblesVariant2(SourceFaithfulSideSub):
    icon_id = 'bubbles-v2'
    variant_of = 'bubbles'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('bubbles', 'large', 'circular', 'bubble', 'touches', 'smaller', 'circle', 'upper')
    keyshape = Keyshape.SQUARE
    canvas_width = 36
    canvas_height = 40

    def build(self):
        """Two circular bubbles with the original unequal sizes and diagonal tangency."""
        self.add_arc('large-a', (26, 11), (8, 35), radius_x=15)
        self.add_arc('large-b', (8, 35), (26, 11), radius_x=15)
        self.add_contour('large', 'large-a', 'large-b', closed=True)
        self.add_arc('small-a', (26, 11), (32, 3), radius_x=5)
        self.add_arc('small-b', (32, 3), (26, 11), radius_x=5)
        self.add_contour('small', 'small-a', 'small-b', closed=True)
        self.relate('connect', 'large', 'small')

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
