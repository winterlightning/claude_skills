"""Circular outline around uppercase O and the lowered smaller 2. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circular outline around uppercase O and the lowered smaller 2. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Oxygen Text: A large uppercase O is followed at lower right by a smaller numeral 2, forming the text O₂. Generate this component alone; exclude Circle Frame.\n\nConstruction: A large oval O and smaller lowered 2 preserve the source subscript arrangement.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '937fbb98-3693-46f2-91da-e8ed80b0bdc3'
SOURCE_PATH = 'pictographic-primitives/state/circle oxi_937fbb98-3693-46f2-91da-e8ed80b0bdc3.svg'
AUTHOR = 'gpt-6'

class OxygenTextVariant2(SourceFaithfulSideSub):
    icon_id = 'oxygen-text-v2'
    variant_of = 'oxygen-text'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('oxygen', 'text', 'large', 'uppercase', 'o', 'followed', 'lower', 'right')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Circular outline around uppercase O and the lowered smaller 2."""
        circle(self, 'frame', 32, 32, 30)
        from icon_set.typeface.source_composition_forms import draw_oxygen
        draw_oxygen(self)

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
TYPEFACE_PROFILE_VARIANTS = ('letter-o-source-round', 'digit-2-source-curved')
TYPEFACE_GLYPH_IDS = ('letter-o-uppercase', 'digit-2')
