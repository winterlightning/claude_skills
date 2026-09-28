from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Text Tool T: An uppercase serif T has a broad horizontal top with short downward ends, a central upright stem, and a small horizontal foot. Generate this component alone; exclude Circle Frame.\n\nConstruction: A centred T has short hanging top serifs and a symmetric horizontal foot.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c50b60b1-2dc6-4030-9b5e-382aaf24bf10'
SOURCE_PATH = 'pictographic-primitives/state/circle text tool_c50b60b1-2dc6-4030-9b5e-382aaf24bf10.svg'
AUTHOR = 'gpt-6'

class TextToolTVariant2(SourceFaithfulSideSub):
    icon_id = 'text-tool-t-v2'
    variant_of = 'text-tool-t'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('text', 'tool', 't', 'uppercase', 'serif', 'broad', 'horizontal', 'top')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Original circled text-tool T, retaining its two hanging top serifs and bottom foot."""
        circle(self, 'frame', 32, 32, 30)
        from icon_set.typeface.framed_source_forms import draw_text_tool_t
        draw_text_tool_t(self)
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
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase',)

TYPEFACE_PROFILE_VARIANTS = ('letter-t-source-serif',)
