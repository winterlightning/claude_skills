"""Circle, outlined head, smooth open shoulders and separate right-hand minus. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle, outlined head, smooth open shoulders and separate right-hand minus. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'User Bust: A circular head sits above an open semicircular shoulder line. Generate this component alone; exclude Circle Frame, Minus Sign.\n\nConstruction: A circular head above open shoulders; body-top is head-bottom plus 8 centreline units (4 ink).\nKeyshape: SQUARE; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9f8da9e5-3911-4d36-a97e-ea83c9dff05a'
SOURCE_PATH = 'pictographic-primitives/state/circle user minus_9f8da9e5-3911-4d36-a97e-ea83c9dff05a.svg'
AUTHOR = 'gpt-6'

class UserBustSubVariant2(SourceFaithfulSideSub):
    icon_id = 'user-bust-sub-v2'
    variant_of = 'user-bust-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('user', 'bust', 'circular', 'head', 'sits', 'open', 'semicircular', 'shoulder')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Circle, outlined head, smooth open shoulders and separate right-hand minus."""
        circle(self, 'frame', 24, 24, 22)
        circle(self, 'head', 19, 17, 6)
        self.add_bezier('shoulders', (13, 35), ((16, 29.666666666666668), (25, 29.666666666666668), (28, 35)))
        self.add_line('minus', (33, 26), (39, 26))

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
