"""Original single crossbar, rounded open euro contour and flat central spine. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Original single crossbar, rounded open euro contour and flat central spine. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Euro Sign: A large C-shaped currency curve is crossed by a single horizontal bar extending left of its stem. The curve remains open on the right, with rounded upper and lower ends.\n\nConstruction: A vertically mirrored half ellipse flows tangentially into short horizontal terminals. A single source-faithful crossbar projects left of the curve.\nKeyshape: VRECT_L; centerline extremes follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f98fd830-ab70-4a21-8f49-67aa7e50b273'
SOURCE_PATH = 'pictographic-primitives/state/euro sign_f98fd830-ab70-4a21-8f49-67aa7e50b273.svg'
AUTHOR = 'gpt-6'

class EuroSignSubVariant3(SourceFaithfulSideSub):
    icon_id = 'euro-sign-sub-v3'
    variant_of = 'euro-sign-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('euro', 'sign', 'large', 'c', 'shaped', 'currency', 'curve', 'crossed')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Original single crossbar, rounded open euro contour and flat central spine."""
        self.add_bezier('upper-tip', (30, 5), ((27, 3), (23, 2), (20, 2)))
        self.add_bezier('upper', (20, 2), ((12, 2), (6, 7), (6, 13)))
        self.add_line('spine', (6, 13), (6, 19))
        self.add_bezier('lower', (6, 19), ((6, 25), (12, 30), (20, 30)))
        self.add_bezier('lower-tip', (20, 30), ((23, 30), (27, 29), (30, 27)))
        self.add_contour('curve', 'upper-tip', 'upper', 'spine', 'lower', 'lower-tip')
        self.add_line('bar', (2, 16), (20, 16))
        self.relate('connect', 'curve', 'bar')

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
