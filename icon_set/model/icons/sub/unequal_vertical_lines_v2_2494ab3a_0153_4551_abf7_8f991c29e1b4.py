"""Magnifying glass enclosing two unequal vertical marks. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Magnifying glass enclosing two unequal vertical marks. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Unequal Vertical Lines: Two detached upright strokes share their top alignment; the left stroke is short and the right extends substantially farther downward. Generate this component alone; exclude Magnifying Glass Frame.\n\nConstruction: Two parallel strokes share a top alignment; only the right stroke spans full height.\nKeyshape: VRECT_S; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2494ab3a-0153-4551-abf7-8f991c29e1b4'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass barcode_2494ab3a-0153-4551-abf7-8f991c29e1b4.svg'
AUTHOR = 'gpt-6'

class UnequalVerticalLinesVariant2(SourceFaithfulSideSub):
    icon_id = 'unequal-vertical-lines-v2'
    variant_of = 'unequal-vertical-lines'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('unequal', 'vertical', 'lines', 'detached', 'upright', 'strokes', 'share', 'top')
    keyshape = Keyshape.SQUARE
    canvas_width = 40
    canvas_height = 40

    def build(self):
        """Magnifying glass enclosing two unequal vertical marks."""
        circle(self, 'glass', 16, 16, 14)
        self.add_line('handle', (26, 26), (38, 38))
        self.relate('connect', 'glass', 'handle')
        self.add_line('short', (12, 10), (12, 16))
        self.add_line('long', (20, 10), (20, 22))

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
