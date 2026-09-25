"""Circle enclosing uppercase U and V in source order with shared glyphs. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle enclosing uppercase U and V in source order with shared glyphs. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'UV Text: An uppercase U with a rounded bottom stands beside an uppercase V formed by two sloping strokes. Generate this component alone; exclude Circle Frame.\n\nConstruction: An upright U and V retain the source letter order and shared baseline.\nKeyshape: HRECT_XL; final SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '48a70f65-2f7b-43c5-9745-85276a8b9bff'
SOURCE_PATH = 'pictographic-primitives/state/circle uv_48a70f65-2f7b-43c5-9745-85276a8b9bff.svg'
AUTHOR = 'gpt-6'

class UvTextState89Variant2(SourceFaithfulSideSub):
    icon_id = 'uv-text-state-89-v2'
    variant_of = 'uv-text-state-89'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('uv', 'text', 'uppercase', 'u', 'rounded', 'bottom', 'stands', 'beside')
    keyshape = Keyshape.SQUARE
    canvas_width = 56
    canvas_height = 56

    def build(self):
        """Circle enclosing uppercase U and V in source order with shared glyphs."""
        circle(self, 'frame', 28, 28, 26)
        self.add_line('u-p1-r1-1', (12, 19), (12, 30))
        self.add_bezier('u-p1-r1-2', (12, 30), ((11.589041095890408, 39.21917808219179), (24.41095890410959, 39.21917808219179), (24, 30)))
        self.add_line('u-p1-r1-3', (24, 30), (24, 19))
        self.add_contour('u-path-1-1', 'u-p1-r1-1', 'u-p1-r1-2', 'u-p1-r1-3', closed=False)
        self.add_line('v-p1-r1-1', (31, 19), (37, 36))
        self.add_bezier('v-p1-r1-2', (37, 36), ((37.666666666666664, 37.63963963963965), (38.333333333333336, 37.63963963963965), (39, 36)))
        self.add_line('v-p1-r1-3', (39, 36), (45, 19))
        self.add_contour('v-path-1-1', 'v-p1-r1-1', 'v-p1-r1-2', 'v-p1-r1-3', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-u-uppercase', 'letter-v-uppercase')
