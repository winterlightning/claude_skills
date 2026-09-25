"""Two wireless arcs above a rounded card with a small lower-right mark. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Two wireless arcs above a rounded card with a small lower-right mark. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Wireless Waves: Two broad curved wireless waves sit one above the other. Generate this component alone; exclude Payment Card.\n\nConstruction: Two upward-bowed waves mirror around x16 with a generous gap.\nKeyshape: HRECT_L; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bee75746-47a6-40de-8e1b-8dbf994b4ff7'
SOURCE_PATH = 'pictographic-primitives/state/card wifi_bee75746-47a6-40de-8e1b-8dbf994b4ff7.svg'
AUTHOR = 'gpt-6'

class WirelessWavesVariant2(SourceFaithfulSideSub):
    icon_id = 'wireless-waves-v2'
    variant_of = 'wireless-waves'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('wireless', 'waves', 'broad', 'curved', 'sit', 'other')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 40

    def build(self):
        """Two wireless arcs above a rounded card with a small lower-right mark."""
        self.add_bezier('outer', (5, 5), ((12, 1), (20, 1), (27, 5)))
        self.add_bezier('inner', (10, 12), ((14, 9), (18, 9), (22, 12)))
        box(self, 'card', 2, 20, 30, 38, 3)
        self.add_line('mark', (19, 30), (22, 30))

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
