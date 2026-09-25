from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Arrow Trend Down: A zigzag line descends overall from upper left to lower right, finishing in an open arrowhead after a central rise. Generate this component alone; exclude Circle Frame.\n\nConstruction: A continuous zigzag falls overall to an open lower-right head.\nKeyshape: HRECT_XL; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8f851035-a23c-4987-b4d5-c04e4caed827'
SOURCE_PATH = 'pictographic-primitives/state/circle downtrend arrow_8f851035-a23c-4987-b4d5-c04e4caed827.svg'
AUTHOR = 'gpt-6'

class ArrowTrendDownVariant2(SourceFaithfulSideSub):
    icon_id = 'arrow-trend-down-v2'
    variant_of = 'arrow-trend-down'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('arrow', 'trend', 'down', 'zigzag', 'line', 'descends', 'overall', 'upper')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Outer circle and descending zigzag arrow retaining its intermediate upward step and lower-right head."""
        circle(self, 'frame', 32, 32, 30)
        self.add_polyline('shaft', (14, 22), (27, 35), (35, 27), (48, 42))
        self.add_polyline('head', (48, 32), (48, 42), (38, 42))
        self.relate('connect', 'head', 'shaft')
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub

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
