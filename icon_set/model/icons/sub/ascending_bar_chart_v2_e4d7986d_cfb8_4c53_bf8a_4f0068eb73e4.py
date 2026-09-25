from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Ascending Bar Chart: Three vertical bars rise from a shared horizontal baseline, increasing in height from left to right. Generate this component alone; exclude Circle Frame.\n\nConstruction: Three regularly spaced bars increase in height across a shared baseline.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4'
SOURCE_PATH = 'pictographic-primitives/state/circle bar_e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4.svg'
AUTHOR = 'gpt-6'

class AscendingBarChartVariant2(SourceFaithfulSideSub):
    icon_id = 'ascending-bar-chart-v2'
    variant_of = 'ascending-bar-chart'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('ascending', 'bar', 'chart', 'vertical', 'bars', 'rise', 'shared', 'horizontal')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Three ascending vertical bars and shared baseline, inside the complete circle."""
        circle(self, 'frame', 24, 24, 22)
        self.add_line('baseline', (14, 34), (34, 34))
        for n, x, y in [('small', 16, 26), ('medium', 24, 20), ('large', 32, 14)]:
            self.add_line(n, (x, y), (x, 34))
            self.relate('connect', n, 'baseline')
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
