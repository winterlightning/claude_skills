"""Speech bubble with tail and uppercase HI using shared glyphs. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Speech bubble with tail and uppercase HI using shared glyphs. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'HI Text: The uppercase letters HI stand side by side, with two uprights joined by a central crossbar in the H and a plain vertical I. Generate this component alone; exclude Round Speech Bubble.\n\nConstruction: An uppercase H and plain I retain their separate vertical stems.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0cb3967a-bb52-468d-b419-77a7865d4cd3'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble round hi_0cb3967a-bb52-468d-b419-77a7865d4cd3.svg'
AUTHOR = 'gpt-6'

class HiTextVariant2(SourceFaithfulSideSub):
    icon_id = 'hi-text-v2'
    variant_of = 'hi-text'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('hi', 'text', 'uppercase', 'letters', 'stand', 'side', 'uprights', 'joined')
    keyshape = Keyshape.SQUARE
    canvas_width = 56
    canvas_height = 56

    def build(self):
        """Speech bubble with tail and uppercase HI using shared glyphs."""
        self.add_bezier('ul', (28, 2), ((13, 2), (2, 11), (2, 25)))
        self.add_bezier('ll', (2, 25), ((2, 33), (7, 39), (14, 43)))
        self.add_line('tail-1', (14, 43), (4, 54))
        self.add_line('tail-2', (4, 54), (18, 46))
        self.add_bezier('base', (18, 46), ((23, 48), (26, 48), (28, 48)))
        self.add_bezier('lr', (28, 48), ((43, 48), (54, 37), (54, 25)))
        self.add_bezier('ur', (54, 25), ((54, 11), (43, 2), (28, 2)))
        self.add_contour('frame', 'ul', 'll', 'tail-1', 'tail-2', 'base', 'lr', 'ur', closed=True)
        self.add_line('h-p1-r1-1', (15, 16), (15, 34))
        self.add_contour('h-path-1-1', 'h-p1-r1-1', closed=False)
        self.add_line('h-p2-r1-1', (28, 16), (28, 34))
        self.add_contour('h-path-2-1', 'h-p2-r1-1', closed=False)
        self.add_line('h-p3-r1-1', (15, 25), (28, 25))
        self.add_contour('h-path-3-1', 'h-p3-r1-1', closed=False)
        self.relate('connect', 'h-path-3-1', 'h-path-1-1')
        self.relate('connect', 'h-path-3-1', 'h-path-2-1')
        from icon_set.typeface.source_composition_forms import draw_plain_i
        draw_plain_i(self)

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
TYPEFACE_PROFILE_VARIANTS = ('letter-i-source-plain',)
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-i-uppercase')
