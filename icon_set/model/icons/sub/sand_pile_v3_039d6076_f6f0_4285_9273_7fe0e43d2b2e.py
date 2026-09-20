from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Sand Pile: Two sloping sides meet at a softly rounded peak to form an open triangular mound. Three tiny grain marks appear inside, with one above two lower marks.\n\nConstruction: A pointed mound has two matching open slopes and sparse detached grains.\nKeyshape: HRECT_XL; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'

class SandPileVariant3(SourceFaithfulSideSub):
    icon_id = 'sand-pile-v3'
    variant_of = 'sand-pile'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('sand', 'pile', 'sloping', 'sides', 'meet', 'softly', 'rounded', 'peak')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 40

    def build(self):
        """Open triangular sand pile with exactly three original grains."""
        self.add_polyline('pile', (2, 38), (24, 2), (46, 38))
        self.add_dot('grain-left', (15, 32))
        self.add_dot('grain-right', (33, 32))
        self.add_dot('grain-top', (24, 22))
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
