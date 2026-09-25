from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Mountain Image: Two unequal mountain peaks form a continuous zigzag, with the taller peak on the right and a tiny sun mark above-left. Generate this component alone; exclude Rounded Square Frame.\n\nConstruction: Two unequal open mountain peaks retain the source upper-left tiny sun stroke and no baseline.\nKeyshape: HRECT_XL; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828'
SOURCE_PATH = 'pictographic-primitives/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.svg'
AUTHOR = 'gpt-6'

class MountainImageState206Variant3(SourceFaithfulSideSub):
    icon_id = 'mountain-image-state-206-v3'
    variant_of = 'mountain-image-state-206'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('mountain', 'image', 'unequal', 'peaks', 'form', 'continuous', 'zigzag', 'taller')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Rounded image frame, small sun mark and both mountains connected to the lower-left and right frame."""
        box(self, 'frame', 2, 2, 46, 46, 5)
        self.add_dot('sun', (15, 15))
        self.add_polyline('mountains', (10, 39), (17, 30), (23, 35), (34, 19), (46, 36))
        self.relate('connect', 'mountains', 'frame')
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
