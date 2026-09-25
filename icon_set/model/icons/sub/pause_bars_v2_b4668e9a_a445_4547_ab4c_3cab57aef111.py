"""Tall rounded device with two short vertical marks and lower horizontal divider. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Tall rounded device with two short vertical marks and lower horizontal divider. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Pause Bars: Two separate equal vertical strokes stand parallel with a clear gap between them. Generate this component alone; exclude Phone Frame.\n\nConstruction: Two identical parallel vertical strokes retain the source pause spacing.\nKeyshape: VRECT_S; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'

class PauseBarsVariant2(SourceFaithfulSideSub):
    icon_id = 'pause-bars-v2'
    variant_of = 'pause-bars'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('pause', 'bars', 'separate', 'equal', 'vertical', 'strokes', 'stand', 'parallel')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 48

    def build(self):
        """Tall rounded device with two short vertical marks and lower horizontal divider."""
        box(self, 'frame', 2, 2, 30, 46, 6)
        self.add_line('divider', (2, 36), (30, 36))
        self.relate('connect', 'divider', 'frame')
        self.add_line('left-mark', (12, 13), (12, 25))
        self.add_line('right-mark', (20, 13), (20, 25))

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
