"""Complete speech bubble with lower-right tail and two unequal text lines. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Complete speech bubble with lower-right tail and two unequal text lines. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Text Lines: Two horizontal text lines are stacked with space between them, with the upper line longer than the lower one. Generate this component alone; exclude Speech Bubble.\n\nConstruction: Two left-aligned strokes with a shorter lower line.\nKeyshape: HRECT_M; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6a4e0e5c-8709-4b7b-8b0f-54f63ae80f41'
SOURCE_PATH = 'pictographic-primitives/state/chat bubble 1_6a4e0e5c-8709-4b7b-8b0f-54f63ae80f41.svg'
AUTHOR = 'gpt-6'

class TextLinesVariant2(SourceFaithfulSideSub):
    icon_id = 'text-lines-v2'
    variant_of = 'text-lines'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('text', 'lines', 'horizontal', 'are', 'stacked', 'space', 'between', 'them')
    keyshape = Keyshape.SQUARE
    canvas_width = 40
    canvas_height = 36

    def build(self):
        """Complete speech bubble with lower-right tail and two unequal text lines."""
        self.add_line('top', (6, 2), (34, 2))
        self.add_arc('tr', (34, 2), (38, 6), radius_x=4)
        self.add_line('right', (38, 6), (38, 22))
        self.add_arc('br', (38, 22), (34, 26), radius_x=4)
        self.add_line('tail-1', (34, 26), (30, 26))
        self.add_line('tail-2', (30, 26), (30, 34))
        self.add_line('tail-3', (30, 34), (20, 26))
        self.add_line('tail-4', (20, 26), (6, 26))
        self.add_arc('bl', (6, 26), (2, 22), radius_x=4)
        self.add_line('left', (2, 22), (2, 6))
        self.add_arc('tl', (2, 6), (6, 2), radius_x=4)
        self.add_contour('frame', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_line('long', (12, 10), (28, 10))
        self.add_line('short', (12, 18), (22, 18))

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
