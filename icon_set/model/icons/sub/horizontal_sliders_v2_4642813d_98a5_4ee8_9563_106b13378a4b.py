"""Rounded panel, two tracks and two offset circular knobs. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Rounded panel, two tracks and two offset circular knobs. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Horizontal Sliders: Two horizontal tracks each carry a circular knob, positioned left on the upper track and right on the lower one. Generate this component alone; exclude Rounded Square Frame.\n\nConstruction: Two horizontal slider tracks meet circular knobs at exact cardinal endpoints.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4642813d-98a5-4ee8-9563-106b13378a4b'
SOURCE_PATH = 'pictographic-primitives/state/square slider_4642813d-98a5-4ee8-9563-106b13378a4b.svg'
AUTHOR = 'gpt-6'

class HorizontalSlidersVariant2(SourceFaithfulSideSub):
    icon_id = 'horizontal-sliders-v2'
    variant_of = 'horizontal-sliders'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('horizontal', 'sliders', 'tracks', 'carry', 'circular', 'knob', 'positioned', 'left')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 42

    def build(self):
        """Rounded panel, two tracks and two offset circular knobs."""
        box(self, 'frame', 2, 2, 46, 40, 4)
        circle(self, 'knob-top', 18, 13, 4)
        circle(self, 'knob-bottom', 30, 28, 4)
        self.add_line('tl', (9, 13), (14, 13))
        self.add_line('tr', (22, 13), (39, 13))
        self.add_line('bl', (9, 28), (26, 28))
        self.add_line('br', (34, 28), (39, 28))
        for p in ['tl', 'tr']:
            self.relate('connect', p, 'knob-top')
        for p in ['bl', 'br']:
            self.relate('connect', p, 'knob-bottom')

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
