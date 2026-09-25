"""Circle enclosing a complete playback triangle and separate directional chevron. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle enclosing a complete playback triangle and separate directional chevron. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Previous Playback: A left-pointing outlined triangle sits beside a detached left chevron, both aligned across their centres. Generate this component alone; exclude Circle Frame.\n\nConstruction: A left triangle and separate left chevron keep the original ordering.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3294e22b-6050-499d-a5f0-136976417b3b'
SOURCE_PATH = 'pictographic-primitives/state/circle play backward_3294e22b-6050-499d-a5f0-136976417b3b.svg'
AUTHOR = 'gpt-6'

class PreviousPlaybackVariant2(SourceFaithfulSideSub):
    icon_id = 'previous-playback-v2'
    variant_of = 'previous-playback'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('previous', 'playback', 'left', 'pointing', 'outlined', 'triangle', 'sits', 'beside')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Circle enclosing a complete playback triangle and separate directional chevron."""
        circle(self, 'frame', 24, 24, 22)
        self.add_polyline('triangle', (35, 15), (23, 24), (35, 33), closed=True)
        self.add_polyline('chevron', (19, 15), (9, 24), (19, 33))

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
